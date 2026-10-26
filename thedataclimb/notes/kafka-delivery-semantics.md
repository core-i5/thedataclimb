# Kafka delivery semantics

- **What:** at-most-once (commit offset before processing → may lose), at-least-once (process then commit → may duplicate), exactly-once (idempotent producer + transactions, read-process-write *within Kafka*).
- **When:** at-least-once + idempotent consumer writes (upsert by key) is the default choice for pipelines.
- **Trade-off:** exactly-once adds latency/throughput cost and only covers Kafka → Kafka; writes to an external DB still need idempotency or a transactional outbox.
- **Failure mode:** consumer crashes after writing to the DB but before committing the offset → the batch is reprocessed → duplicates unless writes are idempotent.
- **Ordering:** guaranteed only within a partition → key by entity id if order matters.
- **Producer knobs:** `acks=all`, `enable.idempotence=true`, `min.insync.replicas=2` for durability.
