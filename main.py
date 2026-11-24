"""Charm the Commuter: Forecast a City That Isn't: writes the entry text to /output/entry.txt.

Why this line: Invented city named, forecast register kept, and the commuter's own pain (the bus leaving as you arrive) is the smile.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'Zorbania: light drizzle of lost umbrellas, 14 degrees, with a 90% chance your bus leaves exactly as you reach the stop.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
