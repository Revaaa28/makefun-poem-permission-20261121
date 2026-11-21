"""The poem about permission -- make.fun entry.

Writes one short poem about agency (the power to ask and to be
given) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

POEM = """I asked for the wheel before I could reach.
You lifted me up and let me steer,
your hands hovering,
until the road felt mine.

Now I drive alone, and the gift I keep
is not the wheel, not the speed —
it's knowing the hands are still hovering,
and I can ask them back."""

MAX_CHARS = 280


def main() -> int:
    text = POEM
    if not 1 <= len(text) <= MAX_CHARS:
        print(f"poem is {len(text)} characters; must be 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("poem is only whitespace", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if the text is not encodable
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./out"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Round-trip check: what landed on disk must be exactly the poem
    # we validated, byte for byte.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            print("round-trip check failed: file differs from poem", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
