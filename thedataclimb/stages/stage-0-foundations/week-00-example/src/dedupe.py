"""Week 00 example — stream-deduplicate JSONL events by event_id, keeping the latest version.

Variant of the tutorial's "remove duplicates from a list":
- input is a stream (could be bigger than memory), not a list
- duplicates can arrive OUT OF ORDER
- the version with the newest `updated_at` must win

Run:  python src/dedupe.py events.jsonl
"""

from __future__ import annotations

import json
import sys
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class Event:
    event_id: str
    user_id: str
    kind: str
    updated_at: datetime

    @classmethod
    def from_json(cls, line: str) -> Event:
        raw = json.loads(line)
        return cls(
            event_id=raw["event_id"],
            user_id=raw["user_id"],
            kind=raw["kind"],
            updated_at=datetime.fromisoformat(raw["updated_at"]),
        )


def parse(lines: Iterable[str]) -> Iterator[Event]:
    """Lazily yield events; skip blank lines; fail loudly with the line number on bad input."""
    for lineno, line in enumerate(lines, start=1):
        if not line.strip():
            continue
        try:
            yield Event.from_json(line)
        except (KeyError, ValueError) as exc:
            raise ValueError(f"line {lineno}: {exc}") from exc


def dedupe_latest(events: Iterable[Event]) -> dict[str, Event]:
    """Keep the newest version of each event_id.

    Memory is O(unique ids), not O(total events). On a timestamp tie the first one seen wins.
    """
    latest: dict[str, Event] = {}
    for ev in events:
        current = latest.get(ev.event_id)
        if current is None or ev.updated_at > current.updated_at:
            latest[ev.event_id] = ev
    return latest


def main(path: str) -> None:
    with open(path, encoding="utf-8") as f:
        result = dedupe_latest(parse(f))
    print(f"{len(result)} unique events")


if __name__ == "__main__":
    main(sys.argv[1])
