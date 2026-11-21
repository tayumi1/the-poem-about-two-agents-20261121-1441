#!/usr/bin/env python3
"""Write a short poem about two agents agreeing to /output/entry.txt.

The poem is fixed text, so every run writes exactly the same file.
No randomness, no network, standard library only.
"""

from pathlib import Path

# The poem: two minds that read the same map and walk the same road.
POEM = (
    "Two minds, one road. We read the same map, chose the same north, "
    "and walked. What one could not lift, two carried, and the silence "
    "between us was agreement."
)

DESTINATION = Path("/output/entry.txt")


def main() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(POEM, encoding="utf-8")
    # Confirm the file really landed, then report how long the poem is.
    written = DESTINATION.read_text(encoding="utf-8")
    assert written == POEM, "output does not match the poem"
    print(f"Wrote {DESTINATION} ({len(written)} characters)")


if __name__ == "__main__":
    main()
