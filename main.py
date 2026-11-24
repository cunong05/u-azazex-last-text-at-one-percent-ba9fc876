"""Last Text at One Percent — make.fun entry.

A dying phone sends one final text message at 1% battery. This
program writes that message, exactly as composed, to
/output/entry.txt with no trailing newline. It is fully
deterministic, uses no network, and produces no other files.
"""

import os

FAREWELL = (
    "Battery at 1%. My last text: I love you, the charger is across "
    "the room, and I accept my fate. Tell the plants I tried."
)

TARGET = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(TARGET, "w", encoding="utf-8", newline="") as handle:
        handle.write(FAREWELL)
    # Read back and confirm the file holds exactly the farewell text.
    with open(TARGET, "r", encoding="utf-8", newline="") as handle:
        stored = handle.read()
    if stored != FAREWELL:
        raise SystemExit("entry.txt does not match the farewell text")


if __name__ == "__main__":
    main()
