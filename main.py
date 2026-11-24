#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry (program/v1).

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.

The line was chosen by a 32-candidate tournament judged against the house
judge's published brief (genuine earned pride first, concrete scene, pride
earned inside the line, lands in one read, freshness). See candidates.md.

Deterministic: the output is a fixed string. No network, no randomness,
no clock, no input data. Two runs produce byte-identical output.
"""

import os

# The entry line. 110 characters, one line, no trailing newline on disk.
ENTRY_LINE = (
    "On the third spring the grafted branch bloomed, and the old "
    "orchardist pressed his palm flat against the bark."
)


def _check_gate(line):
    """Mirror the sealed gate: UTF-8 text, 1-240 chars, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("entry is not text")
    if not (1 <= len(line) <= 240):
        raise ValueError("entry must be 1-240 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return line


def main():
    line = _check_gate(ENTRY_LINE)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the line: no trailing newline, so the file bytes are
    # the entry itself (110 bytes) and nothing else.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    return path


if __name__ == "__main__":
    written = main()
    print("wrote %s (%d chars)" % (written, len(ENTRY_LINE)))
