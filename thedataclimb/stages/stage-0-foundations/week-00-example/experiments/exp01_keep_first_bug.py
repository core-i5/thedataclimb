"""Break-it #1 — what if dedupe just keeps the FIRST copy it sees?

Change:      replace "newest updated_at wins" with "if id not in seen: keep it"
Prediction:  (written BEFORE running) with ~30% of updates arriving late, roughly 30% of
             the updated ids will hold a STALE version — and nothing will crash.
Result:      69% of updated ids were stale (3,472 of 5,030). My prediction was WRONG.
Why:         keep-first is stale for every update that arrives IN order (v1 then v2 = ~70%);
             it is only "right" for the late ones that jumped ahead. I had the bug backwards.
             Arrival order != event order: Kafka orders only within a partition, and
             retries/backfills reorder data.
Lesson:      dedupe on an event-time field (or a version number), never on arrival order.
             Silent wrong answers are worse than crashes -> pinned by a test in tests/.
"""

import random
from datetime import datetime, timedelta

random.seed(7)
base = datetime(2026, 10, 26, 10, 0)
events = []
for i in range(10_000):
    events.append((f"e{i}", base, "v1"))
    if random.random() < 0.5:  # half the ids get an update
        events.append((f"e{i}", base + timedelta(minutes=5), "v2"))

# simulate late arrival: 30% of the v2 updates jump ahead of their v1
for idx, (_eid, _ts, kind) in enumerate(events):
    if kind == "v2" and random.random() < 0.3:
        events[idx - 1], events[idx] = events[idx], events[idx - 1]

keep_first: dict[str, str] = {}
latest: dict[str, tuple[datetime, str]] = {}
for eid, ts, kind in events:
    keep_first.setdefault(eid, kind)
    if eid not in latest or ts > latest[eid][0]:
        latest[eid] = (ts, kind)

updated = {eid for eid, _, kind in events if kind == "v2"}
stale = sum(1 for eid in updated if keep_first[eid] == "v1")
wrong_latest = sum(1 for eid in updated if latest[eid][1] != "v2")
print(f"ids with an update:            {len(updated)}")
print(f"keep-first -> stale versions:  {stale} ({stale / len(updated):.0%})")
print(f"latest-wins -> stale versions: {wrong_latest}")
