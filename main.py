#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one single-line code review comment that approves a pull request
while carrying quiet existential dread, to entry.txt in the output dir.
"""

import os

COMMENT = (
    "Approved. Clean, tested, and quietly permanent: this will outlive "
    "the roadmap, the team, and everyone who reviewed it."
)


MAX_CHARS = 140


def validated_comment() -> str:
    """Return the comment after checking it against the bounty's gate:
    UTF-8 text of 1..140 characters, a single line, not only whitespace."""
    text = COMMENT.strip()
    encoded = text.encode("utf-8")  # raises if not UTF-8 encodable
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"comment is {len(text)} chars, cap is {MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("comment must be a single line")
    if not text or not encoded:
        raise ValueError("comment must not be blank")
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(validated_comment())


if __name__ == "__main__":
    main()
