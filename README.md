# The Word You'd Delete From the Dictionary

Entry for the make.fun contest
[u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2).

## The word

**no**

Erase it and nobody can refuse, deny, or disagree with anything ever
again — every request gets a yes, every argument loses its favourite
answer, and the language itself loses the power to say no.

## How it works

`main.py` (Python 3, standard library only) writes that one word to
`entry.txt` inside `MAKEFUN_OUTPUT_DIR` (default `/output`), exactly
two bytes, no trailing newline, and sets the file mode to 0644 so the
grader can read it. It writes nothing inside the repository.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
