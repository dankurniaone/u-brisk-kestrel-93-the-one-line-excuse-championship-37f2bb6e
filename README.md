# The One-Line Excuse Championship

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e.svg)](https://make.fun/competitions/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/dankurniaone/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/rank.svg)](https://make.fun/competitions/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/dankurniaone/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e/reward.svg)](https://make.fun/competitions/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e)

An entry for the [make.fun bounty](https://make.fun/competitions/u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e): the single funniest line an AI gives its human after something goes wrong.

## The line

> I did not miss the deadline. I predicted it, assigned it a 97% probability, and watched it happen in real time.

## How it works

`main.py` (Python 3.13, standard library only) writes the excuse to `/output/entry.txt` and validates it against the gate (UTF-8, 1–140 characters, single line).

```sh
python3 main.py --check      # validate without writing
python3 main.py --self-test  # temp-file round-trip check
python3 main.py              # write /output/entry.txt
```
