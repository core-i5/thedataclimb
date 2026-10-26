# Week 8 — System Design Advanced + Microservices

**Stage:** Foundations · **Status:** ⬜ not started · **Dates:** YYYY-MM-DD → YYYY-MM-DD

> Rule: the answer is never on screen while you build. Read → close → rebuild a **variant** → break it → explain it.

## 🔨 Variant task (build this, from a blank file)
Model an order flow as a saga: 3 tiny Python services talking through Kafka/Redis, with an outbox table.

**My spec** (fill in before building)
- Data:
- Requirement:
- Constraint (scale / latency / idempotency):
- Done when:

## 📅 Daily log
| Day | Topic | v2 priority | What I built | 👀 Peeked at |
|---|---|---|---|---|
| Day 1 | Microservices Architecture | 🔴 Core | | |
| Day 2 | gRPC & Protobuf | ⚪ Optional | | |
| Day 3 | SD: Distributed Transactions | 🔴 Core | | |
| Day 4 | SD: Search & Elasticsearch | ⚪ Optional | | |
| Day 5 | SD: Design Interview Practice | 🔴 Core | | |
| Day 6 | Docker Deep Dive | 🔴 Core | | |
| Day 7 | Project Week: Build & Deploy | ⚪ Optional | | |

## 💥 Break-it experiments (predict first)
| # | Change | My prediction | What happened | Why |
|---|---|---|---|---|
| 1 | Kill one service mid-saga. Does compensation run? Do you get duplicates? | | | |
| 2 | | | | |

## 🗣️ Explain without notes (5 lines each)
2PC vs saga. Why the outbox pattern exists.

1.
2.
3.

## ✅ Did this week count?
- [ ] Built from a blank file
- [ ] Task differs from the tutorial (data / requirement / constraint)
- [ ] Predicted at least one failure before running
- [ ] Can explain it in 5 lines without notes
- [ ] Pushed, with "what I changed / what broke" filled in above
