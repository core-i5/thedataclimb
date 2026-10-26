.PHONY: up down test lint dsa progress log

up:            ## start local Postgres / Redis / Kafka
	docker compose -f docker/docker-compose.yml up -d

down:
	docker compose -f docker/docker-compose.yml down

test:          ## run all tests
	pytest -q

lint:
	ruff check . && ruff format --check .

dsa:           ## make dsa P=trees N=98 T="validate bst"
	python scripts/new_dsa.py $(P) $(N) "$(T)"

progress:      ## refresh DSA progress table
	python scripts/dsa_progress.py

log:           ## make log W=2026-W44
	cp weekly-log/_template.md weekly-log/$(W).md
