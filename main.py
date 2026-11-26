#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single line (1-240 characters) to /output/entry.txt: a quiet,
earned moment of pride for someone in a scene. Standard library only,
no network, deterministic.

The line: "After forty years of night shifts, my father finally hung his
boots by the door, and my mother — who never once said she was proud —
polished them anyway, twice."

Why it wins: a concrete scene (boots by the door, a mother polishing
them) with two real people, and the pride is earned inside the line by
forty years of night shifts — never asserted, never congratulated. The
turn lands on the last word: "twice" is the quiet confession that she
was proud all along. No trophy, no podium, no graduation — a fresh,
domestic image instead of the stock ones.
"""
import os

ENTRY = (
    "After forty years of night shifts, my father finally hung his boots "
    "by the door, and my mother \u2014 who never once said she was proud "
    "\u2014 polished them anyway, twice."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
