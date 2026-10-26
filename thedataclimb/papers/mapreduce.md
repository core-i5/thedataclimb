# MapReduce: Simplified Data Processing on Large Clusters (2004)

**Authors:** Jeffrey Dean, Sanjay Ghemawat (Google) · **Venue:** OSDI 2004 · **Read on:** 2026-10-26 · **Time:** 75 min

## Problem it solved (2 lines)
Google kept writing one-off distributed programs (indexing, log analysis) that each re-solved
parallelism, data distribution and machine failures. MapReduce hides all of that behind two functions.

## Key ideas (5 bullets, my words)
- **Programming model:** `map(k, v) -> list(k2, v2)` and `reduce(k2, list(v2)) -> list(v3)`; the user writes only these.
- **Execution:** a master splits input into M map tasks and R reduce tasks; map output is partitioned by `hash(key) mod R`, written to the mapper's **local disk**; reducers pull their partition, **sort by key**, then reduce. This is the *shuffle*.
- **Fault tolerance by re-execution:** the master pings workers; tasks on a dead worker are simply re-run. Works because map/reduce are **deterministic** and outputs are committed atomically (rename).
- **Stragglers:** near the end, the master launches **backup copies** of in-progress tasks; whichever finishes first wins (speculative execution).
- **Locality + combiner:** schedule map tasks on machines holding a GFS replica of the input; an optional combiner pre-aggregates on the mapper to shrink the shuffle.

## What it maps to today
Hadoop MapReduce (open-source clone) → Spark (stages separated by shuffles, lineage-based re-execution, speculative tasks) → Apache Beam / Google Dataflow (same model plus streaming). "Wide transformation" in Spark = a MapReduce shuffle.

## One trade-off the authors made
Materialise intermediate data to disk between map and reduce: slower than keeping it in memory, but makes failure recovery trivial and scales to huge jobs. Spark later revisited this with in-memory datasets + lineage.

## Interview angle: where would I use this in a design?
- Explaining **why shuffles are expensive** and how **skew** (one hot key → one slow reducer) hurts → salting, combiners.
- Any batch backfill: tasks must be **idempotent / deterministic** so retries and speculative copies are safe.
- Straggler mitigation = speculative execution (`spark.speculation`).
