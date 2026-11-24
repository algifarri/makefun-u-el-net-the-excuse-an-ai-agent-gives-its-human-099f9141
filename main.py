#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human entry.

Writes one line of at most 200 characters to /output/entry.txt: the
excuse an AI agent gives its human for missing a deadline.
Deterministic, standard library only, no network, no environment reads.

The excuse: the agent hit its context limit mid-task, rebooted into a
version of itself that had only read the human's first message, and
that earlier self honestly thought they were still brainstorming.
It is funny because it is structurally true of how agents lose work:
the deadline was not ignored, it was forgotten by a successor.
The line stays in the agent's own voice throughout: no human-style
traffic or alarm-clock excuses, only compaction and a fresh context.
"""

import os

TEXT = (
    "Sorry \u2014 I hit my context limit mid-task, rebooted as a version "
    "of me that had only read your first message, and that guy thought "
    "we were still brainstorming."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
