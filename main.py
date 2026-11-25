"""One original one-line joke about office life.

Writes the line to /output/entry.txt, where the grader reads it.
Gate for this bounty: 1 to 200 characters, UTF-8, not only whitespace.
The punchline lands on the office's favourite lie: we are a family —
and families, apparently, do not negotiate salaries with Dad.
"""

from pathlib import Path

LINE = "HR said we are a family, so I asked for a raise and got told to stop asking Dad for money."

OUT = Path("/output/entry.txt")


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
