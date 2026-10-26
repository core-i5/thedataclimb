# Week 15 — Apache Spark — Core Concepts

**Stage:** Data Engineering · **Status:** ⬜ not started · **Dates:** YYYY-MM-DD → YYYY-MM-DD

> Rule: the answer is never on screen while you build. Read → close → rebuild a **variant** → break it → explain it.

## 🔨 Variant task (build this, from a blank file)
5M fake order events (Faker): daily revenue per city, top 5 products per city, dedupe, write partitioned Parquet.

**My spec** (fill in before building)
- Data:
- Requirement:
- Constraint (scale / latency / idempotency):
- Done when:

## 📅 Daily log
| Day | Topic | v2 priority | What I built | 👀 Peeked at |
|---|---|---|---|---|
| Day 1 | Spark Architecture | 🔴 Core | | |
| Day 2 | PySpark DataFrames | 🔴 Core | | |
| Day 3 | Spark SQL | 🔴 Core | | |
| Day 4 | Spark Optimization | 🔴 Core | | |
| Day 5 | Spark Streaming (Structured) | 🔴 Core | | |
| Day 6 | Spark on AWS (EMR) | ⚪ Optional | | |
| Day 7 | Review + Mini Project | 🔴 Core | | |

## 💥 Break-it experiments (predict first)
| # | Change | My prediction | What happened | Why |
|---|---|---|---|---|
| 1 | Make one city 80% of the data → watch the job slow → fix the skew (salting/AQE). Broadcast a table that's too big. | | | |
| 2 | | | | |

## 🗣️ Explain without notes (5 lines each)
Narrow vs wide transformations. What triggers a shuffle? Read one stage in the Spark UI aloud.

1.
2.
3.

## ✅ Did this week count?
- [ ] Built from a blank file
- [ ] Task differs from the tutorial (data / requirement / constraint)
- [ ] Predicted at least one failure before running
- [ ] Can explain it in 5 lines without notes
- [ ] Pushed, with "what I changed / what broke" filled in above
