# Week 16 — Apache Kafka — Event Streaming

**Stage:** Data Engineering · **Status:** ⬜ not started · **Dates:** YYYY-MM-DD → YYYY-MM-DD

> Rule: the answer is never on screen while you build. Read → close → rebuild a **variant** → break it → explain it.

## 🔨 Variant task (build this, from a blank file)
Stream your own fake app events (clicks/check-ins) into a 3-partition topic keyed by user; consumer group with manual commits computes per-user counts.

**My spec** (fill in before building)
- Data:
- Requirement:
- Constraint (scale / latency / idempotency):
- Done when:

## 📅 Daily log
| Day | Topic | v2 priority | What I built | 👀 Peeked at |
|---|---|---|---|---|
| Day 1 | Kafka Architecture | 🔴 Core | | |
| Day 2 | Kafka Producers | 🔴 Core | | |
| Day 3 | Kafka Consumers | 🔴 Core | | |
| Day 4 | Kafka Streams & KSQL | ⚪ Optional | | |
| Day 5 | Kafka Connect | 🟡 Compress | | |
| Day 6 | Kafka in Production | 🟡 Compress | | |
| Day 7 | Kafka + Spark Integration | 🔴 Core | | |

## 💥 Break-it experiments (predict first)
| # | Change | My prediction | What happened | Why |
|---|---|---|---|---|
| 1 | Kill a consumer mid-batch → duplicates? Set acks=0 and kill a broker → lost messages? Trigger a rebalance. | | | |
| 2 | | | | |

## 🗣️ Explain without notes (5 lines each)
At-most / at-least / exactly-once. Why ordering is only per partition.

1.
2.
3.

## ✅ Did this week count?
- [ ] Built from a blank file
- [ ] Task differs from the tutorial (data / requirement / constraint)
- [ ] Predicted at least one failure before running
- [ ] Can explain it in 5 lines without notes
- [ ] Pushed, with "what I changed / what broke" filled in above
