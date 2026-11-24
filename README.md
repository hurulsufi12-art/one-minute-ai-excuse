# One Line, One Minute: The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/hurulsufi12-art/one-minute-ai-excuse/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/hurulsufi12-art/one-minute-ai-excuse/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

Entry for the [make.fun bounty "One Line, One Minute: The Funniest AI Excuse"](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18): one funny single-line excuse from an AI agent to its human for a missed deadline, at most 200 characters.

## The excuse

> Sorry, I missed the deadline because my training data taught me procrastination is just parallel processing with extra steps.

(125 characters, one line, plain ASCII.)

## How it works

`main.py` (Python 3.13, standard library only) validates the text against the bounty gate — 1–200 characters (counted as characters, not bytes), not whitespace-only, a single line, no leading/trailing whitespace, no control characters — and then writes it verbatim, with no trailing newline, to `$OUTPUT_DIR/entry.txt` (default `/output`). An invalid text exits non-zero before writing anything. The program is fully deterministic: no randomness, no clock, no network, no external input.
