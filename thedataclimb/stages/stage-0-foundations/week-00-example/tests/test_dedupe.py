import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from dedupe import dedupe_latest, parse  # noqa: E402


def line(event_id: str, ts: str, kind: str = "click") -> str:
    return f'{{"event_id": "{event_id}", "user_id": "u1", "kind": "{kind}", "updated_at": "{ts}"}}'


def test_latest_version_wins_even_when_out_of_order():
    lines = [line("e1", "2026-10-26T10:05:00", "v2"), line("e1", "2026-10-26T10:00:00", "v1")]
    result = dedupe_latest(parse(lines))
    assert result["e1"].kind == "v2"


def test_tie_keeps_first_seen():
    ts = "2026-10-26T10:00:00"
    lines = [line("e1", ts, "first"), line("e1", ts, "second")]
    assert dedupe_latest(parse(lines))["e1"].kind == "first"


def test_blank_lines_are_skipped():
    lines = ["", line("e1", "2026-10-26T10:00:00"), "   \n"]
    assert len(dedupe_latest(parse(lines))) == 1


def test_bad_line_reports_line_number():
    with pytest.raises(ValueError, match="line 2"):
        list(parse([line("e1", "2026-10-26T10:00:00"), '{"event_id": "e2"}']))


def test_parse_is_lazy():
    def exploding():
        yield line("e1", "2026-10-26T10:00:00")
        raise RuntimeError("should not be read yet")

    first = next(parse(exploding()))
    assert first.event_id == "e1"


def test_empty_input():
    assert dedupe_latest(parse([])) == {}
