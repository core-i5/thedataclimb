# Week 19 — ETL/ELT Pipelines — Design & Implementation

**Stage:** Data Engineering · **Status:** ⬜ not started · **Dates:** YYYY-MM-DD → YYYY-MM-DD

> Rule: the answer is never on screen while you build. Read → close → rebuild a **variant** → break it → explain it.

## 🔨 Variant task (build this, from a blank file)
Incremental ingest from a paginated public API (e.g., GitHub events) with a watermark + an SCD2 dimension.

**My spec** (fill in before building)
- Data:
- Requirement:
- Constraint (scale / latency / idempotency):
- Done when:

## 📅 Daily log
| Day | Topic | v2 priority | What I built | 👀 Peeked at |
|---|---|---|---|---|
| Day 1 | ETL vs ELT Patterns | 🔴 Core | | |
| Day 2 | Data Ingestion Patterns | 🔴 Core | | |
| Day 3 | Airbyte — Open Source ETL | ⚪ Optional | | |
| Day 4 | Data Pipeline Patterns | 🔴 Core | | |
| Day 5 | Schema Evolution | 🔴 Core | | |
| Day 6 | Data Lineage & Cataloging | 🟡 Compress | | |
| Day 7 | ETL Project | 🔴 Core | | |

## 💥 Break-it experiments (predict first)
| # | Change | My prediction | What happened | Why |
|---|---|---|---|---|
| 1 | Re-run the same window twice. Make the API fail mid-page. Add a new field to the source schema. | | | |
| 2 | | | | |

## 🗣️ Explain without notes (5 lines each)
CDC vs watermark loads. SCD 1/2/3. Exactly-once vs idempotent writes.

1.
2.
3.

## ✅ Did this week count?
- [ ] Built from a blank file
- [ ] Task differs from the tutorial (data / requirement / constraint)
- [ ] Predicted at least one failure before running
- [ ] Can explain it in 5 lines without notes
- [ ] Pushed, with "what I changed / what broke" filled in above
