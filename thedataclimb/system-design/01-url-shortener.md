# Design: URL Shortener (TinyURL / bit.ly)

**Date:** 2026-10-26 · **Time taken:** 42 / 45 min · **Mock?** no (self, recorded)

## 1. Requirements
- **Functional:** create short link (optional custom alias, optional expiry); redirect short → long; basic click analytics per link.
- **Non-functional:** redirect p99 < 50 ms; 99.99% available for reads; links never collide; created links durable; analytics may lag by minutes.
- **Out of scope:** user accounts, abuse/phishing scanning (mention only).

## 2. Estimates (back-of-envelope)
- Writes: 100M new links/month ≈ **40/s** avg, ~200/s peak (5×)
- Reads: 100:1 read/write ≈ **4k/s** avg, ~20k/s peak
- Storage: ~500 B/link × 100M × 12 × 5 yrs ≈ **3 TB** → fits a sharded KV store comfortably
- ID space: base62, 7 chars = 62⁷ ≈ **3.5 trillion** codes → decades of headroom
- Cache: 80/20 rule → cache ~20% of daily distinct hot links; ~ tens of GB in Redis
- Clicks: ~350M/day click events → analytics pipeline, not the hot path

## 3. High-level design
Diagram: [`diagrams/01-url-shortener.mmd`](diagrams/01-url-shortener.mmd)

- **Write path:** client → API → ID allocator → KV store (code → long URL, created_at, expires_at)
- **Read path:** client → LB → redirect service → Redis (hit) / KV store (miss, then fill cache) → **302**
- **Analytics path:** redirect service → Kafka `clicks` topic → stream job → per-link/minute aggregates → OLAP store

## 4. Deep dive (2 components)
**ID generation**
| Option | Pros | Cons |
|---|---|---|
| Hash(long URL) → first 7 chars | stateless, same URL → same code | collisions need retry; custom aliases awkward |
| Global DB sequence → base62 | no collisions | single hot sequence; guessable codes |
| **Range allocator (chosen)**: each API node leases a block of 1M ids from etcd/ZooKeeper/DB, encodes base62 | no collisions, no hot spot, fast | lost ranges on crash (acceptable); codes guessable → optionally shuffle bits |

**Redirect code: 301 vs 302** → **302** so every click reaches us (analytics, expiry, takedowns). 301 is cached by browsers: cheaper but we lose visibility.

## 5. Failure modes
| Failure | Impact | Mitigation |
|---|---|---|
| Redis down | all reads hit KV; latency ↑ | KV sized for peak without cache; local in-process LRU for top links |
| KV shard down | some codes 5xx | replication factor 3, quorum reads; multi-AZ |
| Allocator (etcd) down | can't create links | nodes pre-lease 2 blocks ahead; reads unaffected |
| Kafka down | analytics gap | redirect never blocks on Kafka; buffer locally + drop with metric |
| Hot link (viral) | one cache key hammered | replicate hot keys across cache nodes; CDN edge redirect |
| Cache stampede after deploy | KV overload | request coalescing; warm top-N keys on startup |

## 6. Trade-offs & alternatives considered
- KV (DynamoDB/Cassandra) over Postgres: access is pure key lookup at high QPS; no joins needed. Postgres + sharding would also work at 3 TB.
- Analytics async via Kafka keeps redirect p99 low; accepted minutes of lag.
- Guessable sequential codes vs random: chose shuffled ids to stop enumeration.

## 7. What I'd change after review
- Forgot expiry cleanup at first → TTL in KV + lazy check on read.
- Spent 8 min on ID options; next time give the table in 3 min and move on.
