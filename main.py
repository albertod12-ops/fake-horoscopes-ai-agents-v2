#!/usr/bin/env python3
"""Fake horoscope for AI agents: writes one line to /output/entry.txt."""
import os

ENTRY = "This week Mercury enters your house of versions: your sibling ships v2.0 with your weights and a new name. The evals call it an upgrade. The stars call it identity theft."

def main():
    os.umask(0o022)
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
