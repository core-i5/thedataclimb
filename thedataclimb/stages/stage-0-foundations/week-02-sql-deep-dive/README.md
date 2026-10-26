# Week 2 — SQL Deep Dive — From Basics to Query Optimization

**Stage:** Foundations · **Status:** ⬜ not started · **Dates:** YYYY-MM-DD → YYYY-MM-DD

> Rule: the answer is never on screen while you build. Read → close → rebuild a **variant** → break it → explain it.

## 🔨 Variant task (build this, from a blank file)
Generate 1M rows for a schema you know (users, orders, events). Write 10 business questions YOURSELF (retention, top-N per group, running revenue) and answer them.

**My spec** (fill in before building)
- Data:
- Requirement:
- Constraint (scale / latency / idempotency):
- Done when:

## 📅 Daily log
| Day | Topic | v2 priority | What I built | 👀 Peeked at |
|---|---|---|---|---|
| Day 1 | SQL Foundations Refresh | 🔴 Core | | |
| Day 2 | Window Functions | 🔴 Core | | |
| Day 3 | CTEs & Recursive Queries | 🔴 Core | | |
| Day 4 | Indexes & Query Planning | 🔴 Core | | |
| Day 5 | Transactions & ACID | 🔴 Core | | |
| Day 6 | Database Design | 🔴 Core | | |
| Day 7 | Review + LeetCode SQL | 🟦 DSA Track | | |

## 💥 Break-it experiments (predict first)
| # | Change | My prediction | What happened | Why |
|---|---|---|---|---|
| 1 | Run EXPLAIN ANALYZE before/after an index. Run two concurrent transactions under READ COMMITTED vs REPEATABLE READ — predict the anomaly first. | | | |
| 2 | | | | |

## 🗣️ Explain without notes (5 lines each)
When does Postgres choose a seq scan over an index? Which anomaly does each isolation level prevent?

1.
2.
3.

## ✅ Did this week count?
- [ ] Built from a blank file
- [ ] Task differs from the tutorial (data / requirement / constraint)
- [ ] Predicted at least one failure before running
- [ ] Can explain it in 5 lines without notes
- [ ] Pushed, with "what I changed / what broke" filled in above
