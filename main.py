#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun bounty entry.

Writes one word to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: the same bytes on every run, no input, no randomness, no
network. Standard library only.

The word: "unsubscribed". An ex summed up as a newsletter you finally
opted out of — the relationship recast as inbox spam, and the breakup
as the one click that stops the daily messages. The joke is the frame
shift: nobody unsubscribes from a person, yet everyone has felt the
relief of unsubscribing from something that kept showing up uninvited.
It is instantly readable as a verdict on a former partner, it lands at
a glance with no caption, it is not the obvious insult ("toxic",
"cheater", "ghost"), and anyone who has ever hit unsubscribe — or
wished a person came with one — nods at it.
"""

import os
from pathlib import Path

ENTRY = "unsubscribed"

# Gate: /output/entry.txt must be UTF-8 text of 1 to 111 characters,
# not only white space. One word, no punctuation tricks, no trailing
# newline (the gate counts every character).
assert 1 <= len(ENTRY.strip()) <= 111, "entry must be 1-111 characters"
assert ENTRY.strip(), "entry must not be only white space"
assert ENTRY.strip() == ENTRY, "entry must be exactly one word"
assert " " not in ENTRY and "\t" not in ENTRY and "\n" not in ENTRY, "entry must be one word"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
