"""Entry for 'The Word You'd Delete From the Dictionary'.

Writes a single word to /output/entry.txt (via MAKEFUN_OUTPUT_DIR).
The word is the one whose erasure leaves the funniest hole in the
language: without it, nobody can refuse, deny, or disagree with
anything ever again. Stdlib only, no network, no writes inside the repo.
"""

import os
import stat
import sys

WORD = "no"
MAX_CHARS = 77


def output_dir():
    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return target


def check_word(word):
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    if not word or not word.strip():
        raise ValueError("entry must not be empty")
    if len(word) > MAX_CHARS:
        raise ValueError("entry is longer than 77 characters")
    if any(char.isspace() for char in word):
        raise ValueError("entry must be exactly one word, no spaces")
    if word != word.strip():
        raise ValueError("entry must not carry surrounding whitespace")
    return word


def main():
    word = check_word(WORD)
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(word)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
