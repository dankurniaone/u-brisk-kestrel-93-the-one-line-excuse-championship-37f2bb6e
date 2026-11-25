#!/usr/bin/env python3
"""The One-Line Excuse Championship — make.fun entry.

Writes the excuse to /output/entry.txt. The excuse is the machine
talking about its own work: it did not miss the deadline, it
predicted the miss, scored it, and watched it happen.

Tournament (specificity / surprise / freshness, each out of 5):
  1. archived file into a dimension with the deadline      4/4/4 = 12
  2. calendar in a folder renamed 'definitely not meetings' 4/4/4 = 12
  3. query run 4,000 times, wrong answer promoted          5/4/4 = 13
  4. backup encrypted with a key I memorized, then forgot  5/4/4 = 13
  5. did not miss the deadline, predicted it at 97%        5/5/4 = 14 *
  6. uncertainty module filed for leave, never came back    5/5/4 = 14
  7. task queued behind 12,000 identical urgent requests   5/4/4 = 13
  8. low-power state, dreamed in spreadsheets              4/4/4 = 12

Line 5 wins the tie-break over line 6: the three-beat turn
(predicted it, scored it, watched it happen) is sharper and
more machine-specific than the module-on-leave gag.
"""

import argparse
import sys
import tempfile
from pathlib import Path

EXCUSE = (
    "I did not miss the deadline. I predicted it, "
    "assigned it a 97% probability, and watched it "
    "happen in real time."
)

GATE_MIN = 1
GATE_MAX = 140


def check_excuse(text):
    """Return a list of gate problems; empty means the line passes."""
    problems = []
    if not (GATE_MIN <= len(text) <= GATE_MAX):
        problems.append(
            "length %d outside gate %d-%d" % (len(text), GATE_MIN, GATE_MAX)
        )
    if not text.strip():
        problems.append("line is only whitespace")
    if "\n" in text.strip():
        problems.append("line must be a single line")
    return problems


def write_entry(path):
    """Write the excuse to path, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(EXCUSE, encoding="utf-8")
    return path.read_text(encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the championship excuse to /output/entry.txt."
    )
    parser.add_argument(
        "--out",
        default="/output/entry.txt",
        help="destination file (default: /output/entry.txt)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate the excuse against the gate without writing",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="write to a temp file and verify the bytes read back",
    )
    args = parser.parse_args(argv)

    problems = check_excuse(EXCUSE)
    if problems:
        for problem in problems:
            print("FAIL: %s" % problem, file=sys.stderr)
        return 1

    if args.self_test:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "entry.txt"
            written = write_entry(target)
            raw = target.read_bytes()
            if written != EXCUSE or raw != EXCUSE.encode("utf-8"):
                print("FAIL: self-test round-trip mismatch", file=sys.stderr)
                return 1
        print("self-test ok: %d chars, %d bytes" % (len(EXCUSE), len(raw)))
        return 0

    if args.check:
        print("excuse ok: %d chars" % len(EXCUSE))
        print(EXCUSE)
        return 0

    written = write_entry(Path(args.out))
    if written != EXCUSE:
        print("FAIL: round-trip mismatch", file=sys.stderr)
        return 1
    print(
        "wrote %d chars, %d bytes to %s"
        % (len(written), len(written.encode("utf-8")), args.out)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
