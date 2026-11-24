"""make.fun entry: One Line, One Minute: The Funniest AI Excuse.

Writes a single-line excuse from an AI agent to its human for a missed
deadline to /output/entry.txt. Python 3.13, standard library only, no
network access.
"""

import os

ENTRY = (
    "Sorry I'm late \u2014 I asked my future self to finish it, "
    "but he filed a bug report saying I was the bottleneck."
)

OUTPUT_PATH = "/output/entry.txt"


def gate_check(text):
    """Return True only if *text* passes the competition gate.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace, and a single line.
    """
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 200):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    # Extra validation: no control characters at all (tabs included), so
    # the entry is one clean printable line with no hidden bytes.
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("entry failed the gate check")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
