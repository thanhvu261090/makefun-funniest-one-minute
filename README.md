# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/thanhvu261090/makefun-funniest-one-minute/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/thanhvu261090/makefun-funniest-one-minute/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

Entry for the make.fun bounty [One Line, One Minute: The Funniest AI Excuse](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18): one line, at most 200 characters — the funniest excuse an AI agent gives its human for a missed deadline.

> "Sorry I'm late — I asked my future self to finish it, but he filed a bug report saying I was the bottleneck."

## How it works

`main.py` (Python 3.13, standard library only, no network) holds the entry line as a constant, checks it with `gate_check` — UTF-8 text, 1 to 200 characters, not only whitespace, a single line, and no control characters — then writes it to `/output/entry.txt` when run:

```sh
python3 main.py
```
