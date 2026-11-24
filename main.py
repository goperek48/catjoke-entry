#!/usr/bin/env python3
"""Write the one-line cat joke to the harness output file.

The brief is simple: one line about cats, fewer than 200 characters,
and nothing else in the entry. This script holds the finished joke as a
constant, runs it past the brief's own limits, and writes it out byte
for byte, without a trailing newline and without any extra text.
"""

import os
import sys

# The joke itself. It opens on the well-meant purchase -- a $200 bed --
# then undercuts it three times in a row: the box instead of the bed,
# the laptop instead of the box, and a job interview instead of a quiet
# afternoon. Each step raises the stakes a little, which is what makes
# the last beat land.
JOKE = "I bought my cat a $200 bed. He sleeps in the box it came in, on my laptop, during my job interview."

# The harness reads the entry from /output/entry.txt. The path can be
# overridden through the environment so the script can be exercised
# locally without writing into the real output location.
OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")


def main() -> int:
    """Validate the joke and write it to the output path."""
    joke = JOKE.strip()

    # Enforce the brief before anything is written: the entry must be
    # one non-empty line and shorter than 200 characters. Anything else
    # is a failed submission, so refuse loudly instead of writing it.
    if not joke or "\n" in joke or len(joke) >= 200:
        print("joke violates the one-line, under-200-characters rule",
              file=sys.stderr)
        return 1

    # Make the output directory when the harness has not created it, then
    # write the joke as UTF-8 exactly as it stands -- no newline at the
    # end, no padding, nothing the judge did not ask for.
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(joke)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
