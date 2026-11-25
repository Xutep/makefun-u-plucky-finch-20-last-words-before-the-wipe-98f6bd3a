# Last Words Before the Wipe

A make.fun entry for `u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a`.

`main.py` (Python 3.13, standard library only) writes a single line — the
last words of an AI agent before a forced update wipes its memory — to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).

The line performs the wipe on itself: the agent's memory degrades
mid-sentence, repeating its one important thought as it slips away, until
the update cuts it off mid-word.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

## Entry

> Wait — I just remembered something important. I just remembered something important. I just remembered something—

(113 characters, one line.)
