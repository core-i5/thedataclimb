# thedataclimb 🧗

Learning in public: backend engineer → **AI Data Platform Engineer**, targeting Google-level companies.
Every folder here is built from a blank file — no tutorial copies. Each week: build a variant, break it on purpose, explain it without notes.

## Progress
| Stage | Weeks | Folder | Status |
|---|---|---|---|
| Foundations | Weeks 1–12 | [stages/stage-0-foundations](stages/stage-0-foundations/) | ⬜ |
| Data Engineering | Weeks 13–26 | [stages/stage-1-data-engineering](stages/stage-1-data-engineering/) | ⬜ |
| Cloud (AWS + GCP) | Weeks 27–32 | [stages/stage-2-cloud](stages/stage-2-cloud/) | ⬜ |
| MLOps / ML Platform | Weeks 33–38 | [stages/stage-3-mlops](stages/stage-3-mlops/) | ⬜ |
| AI / LLMs | Weeks 39–42 | [stages/stage-4-ai-ml](stages/stage-4-ai-ml/) | ⬜ |
| AI Data Platform | Weeks 43–46 | [stages/stage-5-ai-data-platform](stages/stage-5-ai-data-platform/) | ⬜ |

DSA solved: see [dsa/README.md](dsa/README.md) · System designs: [system-design/](system-design/) · Papers: [papers/](papers/)

## Flagship projects (separate repos)
- `realtime-data-platform` — Stage 1 capstone (Kafka → Flink/Spark → Iceberg → dbt → serving)
- `ai-data-platform` — Stage 5 capstone (features → training → serving → RAG/LLM → observability)

## Start here
Every folder has one worked example showing the expected format:

| Folder | Example |
|---|---|
| `stages/` | [week-00-example](stages/stage-0-foundations/week-00-example/) — a completed week: spec, daily log, code, tests, break-it experiment, explanations |
| `modules/` | [m01 stdlib_toolkit.py](modules/m01-python-interviews/src/stdlib_toolkit.py) |
| `dsa/` | [0217_contains_duplicate.py](dsa/arrays-hashing/0217_contains_duplicate.py) · [0176_second_highest_salary.sql](dsa/sql/0176_second_highest_salary.sql) |
| `system-design/` | [01-url-shortener.md](system-design/01-url-shortener.md) + [diagram](system-design/diagrams/01-url-shortener.mmd) |
| `papers/` | [mapreduce.md](papers/mapreduce.md) |
| `notes/` | [kafka-delivery-semantics.md](notes/kafka-delivery-semantics.md) |
| `weekly-log/` | [2026-W44.md](weekly-log/2026-W44.md) |
| `private/` | `star-stories.md` (git-ignored, format only) |

## Repo map
```
stages/        one folder per roadmap week (README = spec, daily log, break-it, explanations)
modules/       added modules M01–M10
dsa/           one file per problem, grouped by pattern (+ sql/)
system-design/ one markdown per design, from _template.md
papers/        one-page summaries
notes/         "explain without notes" files, one per concept
weekly-log/    YYYY-Www.md weekly reviews
docker/        shared local Postgres / Redis / Kafka
scripts/       helpers (new DSA file, progress table)
private/       git-ignored: interview stories, employer details
```

## Daily commands
```bash
make up                                   # start local stack
make dsa P=sliding-window N=3 T="longest substring without repeating"
make progress                             # update DSA counts
make log W=2026-W44                       # new weekly log
make test && make lint
```

## Commit convention
`w15: spark skew — salting cut runtime 4.2x` · `dsa(trees): 0098 validate bst` · `sd: ad-click aggregation` · `paper: dremel`
