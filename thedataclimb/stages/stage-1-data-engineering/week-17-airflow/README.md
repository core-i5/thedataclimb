# Week 17 — Apache Airflow — Workflow Orchestration

**Stage:** Data Engineering · **Status:** ⬜ not started · **Dates:** YYYY-MM-DD → YYYY-MM-DD

> Rule: the answer is never on screen while you build. Read → close → rebuild a **variant** → break it → explain it.

## 🔨 Variant task (build this, from a blank file)
Orchestrate your Week 15–16 jobs: daily DAG with a sensor, branching, retries, an SLA and a 30-day backfill.

**My spec** (fill in before building)
- Data:
- Requirement:
- Constraint (scale / latency / idempotency):
- Done when:

## 📅 Daily log
| Day | Topic | v2 priority | What I built | 👀 Peeked at |
|---|---|---|---|---|
| Day 1 | Airflow Architecture | 🔴 Core | | |
| Day 2 | Airflow DAG Design | 🔴 Core | | |
| Day 3 | Airflow Operators & Hooks | 🔴 Core | | |
| Day 4 | Airflow + dbt Integration | 🔴 Core | | |
| Day 5 | Airflow on AWS (MWAA) | ⚪ Optional | | |
| Day 6 | Airflow Monitoring & Alerting | 🟡 Compress | | |
| Day 7 | Airflow Mini Project | 🔴 Core | | |

## 💥 Break-it experiments (predict first)
| # | Change | My prediction | What happened | Why |
|---|---|---|---|---|
| 1 | Make one task non-idempotent → backfill twice → duplicates → fix with partition overwrite. | | | |
| 2 | | | | |

## 🗣️ Explain without notes (5 lines each)
Idempotency. catchup vs backfill. Executor types.

1.
2.
3.

## ✅ Did this week count?
- [ ] Built from a blank file
- [ ] Task differs from the tutorial (data / requirement / constraint)
- [ ] Predicted at least one failure before running
- [ ] Can explain it in 5 lines without notes
- [ ] Pushed, with "what I changed / what broke" filled in above
