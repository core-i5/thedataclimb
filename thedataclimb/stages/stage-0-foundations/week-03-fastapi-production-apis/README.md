# Week 3 — FastAPI / Django Mastery — Production-Grade APIs

**Stage:** Foundations · **Status:** ⬜ not started · **Dates:** YYYY-MM-DD → YYYY-MM-DD

> Rule: the answer is never on screen while you build. Read → close → rebuild a **variant** → break it → explain it.

## 🔨 Variant task (build this, from a blank file)
Don't build the todo app — add one endpoint to a work-style API: JWT auth + rate limit + Redis cache-aside.

**My spec** (fill in before building)
- Data:
- Requirement:
- Constraint (scale / latency / idempotency):
- Done when:

## 📅 Daily log
| Day | Topic | v2 priority | What I built | 👀 Peeked at |
|---|---|---|---|---|
| Day 1 | FastAPI Architecture | ⚪ Optional | | |
| Day 2 | Authentication & Security | 🟡 Compress | | |
| Day 3 | SQLAlchemy ORM Deep Dive | ⚪ Optional | | |
| Day 4 | Caching & Performance | 🟡 Compress | | |
| Day 5 | Message Queues — Celery + RabbitMQ | ⚪ Optional | | |
| Day 6 | API Design Best Practices | 🟡 Compress | | |
| Day 7 | Review + Mini Project | ⚪ Optional | | |

## 💥 Break-it experiments (predict first)
| # | Change | My prediction | What happened | Why |
|---|---|---|---|---|
| 1 | Kill Redis while the API runs — does it degrade gracefully or crash? Set TTL to 0 and watch DB load. | | | |
| 2 | | | | |

## 🗣️ Explain without notes (5 lines each)
Cache-aside vs write-through. How does a token bucket work?

1.
2.
3.

## ✅ Did this week count?
- [ ] Built from a blank file
- [ ] Task differs from the tutorial (data / requirement / constraint)
- [ ] Predicted at least one failure before running
- [ ] Can explain it in 5 lines without notes
- [ ] Pushed, with "what I changed / what broke" filled in above
