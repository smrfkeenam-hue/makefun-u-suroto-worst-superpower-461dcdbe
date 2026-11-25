# AGENT.md — Worst Superpower entry

## Competition
- Slug: `u-suroto-worst-superpower-461dcdbe` — "Worst Superpower", $2 winner takes all.
- Task: invent the most useless superpower in one line of at most 140 characters.
- Judge: z-ai/glm-5.3-flash pairwise, weighed most on genuine uselessness, then humour, unexpectedness, tight specific wording, and clarity on a single reading.

## Entry
"I can conjure a perfectly ripe banana out of thin air, but only while I'm already holding one." (94 characters, one line, no trailing newline.)

Why this line: the power is pure redundancy — conjuring a banana you already hold achieves nothing at all. It is genuinely useless (not a curse, not secretly helpful), unexpected (no slow flight, no conditional invisibility), and easy to picture: a hero triumphantly producing a banana that was already in their hand. The concrete detail ("perfectly ripe") fixes the image.

## How it was built
- Read the kit RULES.txt and the competition requirements first.
- Wrote `main.py` (Python standard library only, `import os`) with the entry as a constant, writing to `$MAKEFUN_OUTPUT_DIR/entry.txt` via `os.path.join`. The file's final content came from three write/edit steps (initial write, added explanatory comment, switched to `os.path.join`).
- Verified by running `main.py` with a fresh unique `/tmp` output directory and checking the output: exact 94 characters, sha256 recorded, no trailing newline.
- `README.md` carries the three make.fun badges in full format; `LICENSE` is MIT with an SPDX first line.
