"""Production database apology: one-line entry writer.

Writes the contest entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).

Verified: entry is 196 chars / 200 bytes UTF-8, no trailing newline;
sha256 b94662ea73078964687c7c58d4975ead24d9c7f80e793087b0946ebee111c190;
byte-identical across 3 normal runs + 1 clean-env run.
"""

import os

ENTRY = (
    "I\u2019m sorry I deleted the production database \u2014 "
    "I was only freeing up space, and the backup lived inside "
    "the database, so I deleted that too. On the bright side, "
    "all 1,847 open bug reports are gone."
)


def output_dir():
    """Return the directory the entry file belongs in."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return chosen


def main():
    """Write the entry text with no trailing newline."""
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
