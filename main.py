"""One Line, One Minute: The Funniest AI Excuse -- make.fun bounty entry.

Writes one funny single-line excuse from an AI agent to its human for a
missed deadline (TEXT) verbatim to $OUTPUT_DIR/entry.txt (default
/output). Stdlib-only, deterministic, no network, no randomness, no
external input.
"""

import os
import sys
import unicodedata
from pathlib import Path

TEXT = (
    "Sorry, I missed the deadline because my training data taught me "
    "procrastination is just parallel processing with extra steps."
)

MAX_CHARS = 200


def _output_dir() -> Path:
    """Resolve the output directory: $OUTPUT_DIR, empty counts as unset."""
    return Path(os.environ.get("OUTPUT_DIR") or "/output")


def _validate(text: str) -> None:
    """Raise ValueError unless text passes the gate.

    Gate (RULES.txt + PLAN §4): 1-200 characters (characters, not bytes),
    not whitespace-only, a single line (no \\n, \\r, \\x0b, \\x0c), no
    control characters (Unicode category Cc or DEL), no leading/trailing
    whitespace. Non-ASCII text within the character gate is accepted:
    the RULES gate counts characters, not bytes.
    """
    if not isinstance(text, str):
        raise ValueError("TEXT must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"TEXT must be 1..{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("TEXT must not be whitespace-only")
    if text != text.strip():
        raise ValueError("TEXT must not start or end with whitespace")
    if any(ch in text for ch in ("\n", "\r", "\x0b", "\x0c")):
        raise ValueError("TEXT must be a single line")
    if any(unicodedata.category(ch) == "Cc" or ch == "\x7f" for ch in text):
        raise ValueError("TEXT must not contain control characters")


def _write_entry() -> None:
    """Write TEXT verbatim to $OUTPUT_DIR/entry.txt (no trailing newline).

    Separated from main() so the validate-then-write order is explicit
    and testable: main() validates first, and only a valid TEXT ever
    reaches this writer.
    """
    output_dir = _output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


def main() -> None:
    """Validate TEXT, then write it verbatim to $OUTPUT_DIR/entry.txt.

    Validation runs BEFORE any write, so a rejected run never creates
    or overwrites entry.txt. On invalid TEXT, exits non-zero with
    SystemExit(1) (tests demand SystemExit for rejections).
    """
    try:
        _validate(TEXT)  # read the global live, at call time (tests patch it)
    except ValueError as exc:
        print(f"invalid entry text: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    _write_entry()


if __name__ == "__main__":
    main()
