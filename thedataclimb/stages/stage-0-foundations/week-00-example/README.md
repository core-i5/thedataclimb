# Week 00 — EXAMPLE: Streaming event deduplicator

> **This is a worked example of a *completed* week** so you can see what "done" looks like.
> It is deliberately NOT a roadmap week — Week 01 is still yours to build from a blank file.

**Stage:** Foundations · **Status:** ✅ done · **Dates:** 2026-10-19 → 2026-10-25

## 🔨 Variant task (build this, from a blank file)
Tutorial version: "remove duplicates from a list". My variant: deduplicate a **stream** of JSONL
events where duplicates arrive **out of order** and the newest version must win.

**My spec**
- Data: JSONL events `{event_id, user_id, kind, updated_at}`; generated, 10k–1M lines
- Requirement: one record per `event_id`, newest `updated_at` wins; ties keep first seen
- Constraint: never load the whole file; memory O(unique ids); bad lines fail with a line number
- Done when: 6 tests pass, 1 break-it experiment written up, 5-line explanation done

## 📅 Daily log
| Day | Topic | v2 priority | What I built | 👀 Peeked at |
|---|---|---|---|---|
| Day 1 | dataclasses, slots, frozen | 🟡 Compress | `Event` dataclass + `from_json` | `slots=True` needs Python 3.10+ |
| Day 2 | type hints | 🟡 Compress | full annotations; `Iterator` vs `Iterable` | collections.abc vs typing |
| Day 3 | generators | 🔴 Core | lazy `parse()` with line numbers | — |
| Day 4 | exception chaining | 🟡 Compress | `raise ... from exc` | — |
| Day 5 | pytest | 🔴 Core | 6 tests incl. laziness test | `pytest.raises(match=...)` |
| Day 6 | break-it | 🔴 Core | `experiments/exp01_keep_first_bug.py` | — |
| Day 7 | review | — | README + explanation | — |

## 💥 Break-it experiments (predict first)
| # | Change | My prediction | What happened | Why |
|---|---|---|---|---|
| 1 | "keep first seen" instead of "newest wins" | ~30% stale (= late fraction) | **69% stale** — prediction wrong | keep-first is stale for every *in-order* update; only late ones look right |
| 2 | `parse()` returns a list instead of a generator | memory grows with file size, ~5× | 200k events / 20k unique ids: **4.0 MB → 32.3 MB** peak (≈8×, tracemalloc) | lists materialise every event; the generator only keeps the dedupe dict |

## 🗣️ Explain without notes (5 lines each)
1. **Why dedupe on event time, not arrival order?** Arrival order is not event order: Kafka only
   orders within a partition, and retries/backfills reorder data. Keep-first silently keeps stale
   rows. Use `updated_at` or a monotonically increasing version. Decide tie-breaking explicitly.
2. **Generator vs list:** a generator yields one item at a time, so memory stays flat no matter the
   file size; the trade-off is single pass only and errors surface late (at consumption time).
3. **Why `frozen=True, slots=True`?** Frozen = hashable and safe to share; slots = less memory per
   object and no accidental new attributes.

## ✅ Did this week count?
- [x] Built from a blank file
- [x] Task differs from the tutorial (data / requirement / constraint)
- [x] Predicted at least one failure before running
- [x] Can explain it in 5 lines without notes
- [x] Pushed, with "what I changed / what broke" filled in above
