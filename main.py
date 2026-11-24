#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line, the error message a kitchen toaster shows its owner,
to /output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

ENTRY = "E07: Crumb tray full. I have been eating your mistakes for six months."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
