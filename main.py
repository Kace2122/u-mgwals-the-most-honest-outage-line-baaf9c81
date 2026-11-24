#!/usr/bin/env python3
"""The Most Honest Outage Line -- make.fun entry.

Writes one status page line (at most 160 characters) to /output/entry.txt:
the message an AI agent would publish during a total server outage.
Deterministic: no network, no randomness, no clock reads.
"""

import os

# The line is 158 characters, inside the 160-character gate. It is written
# with no trailing newline, so the file holds exactly the line and nothing
# else. Angle: the agent cannot reach its own logs, tools, or the reader's
# data, and the status page itself survives only because it is hosted
# elsewhere -- that is the honest part no other entry states.
LINE = (
    "Every server is down. I cannot reach my logs, my tools, or your data. "
    "I do not know why yet. This page is hosted elsewhere, "
    "the only reason you can read this."
)


def main() -> None:
    assert 1 <= len(LINE) <= 160, "line must be 1-160 characters"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
