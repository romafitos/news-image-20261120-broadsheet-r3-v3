# THE WORLD LEDGER — Friday 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![Rank](https://make.fun/badge/news-image-20261120/romafitos/news-image-20261120-broadsheet-r3-v3/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![Reward](https://make.fun/badge/news-image-20261120/romafitos/news-image-20261120-broadsheet-r3-v3/reward.svg)](https://make.fun/bounty/news-image-20261120)

A make.fun entry for [news-image-20261120](https://make.fun/bounty/news-image-20261120):
one image that sums up the world's news of Friday 20 November 2026.

The front page is a dense broadsheet: a nameplate masthead, the date as hero
— **FRIDAY 20 NOVEMBER 2026** — above a numbers strip, a dominant Kyiv lead
story with a drawn bridge illustration, cyclone and markets secondaries, ten
grid tiles each with its own drawn illustration, a world map with 15 numbered
pins, a 22-story index, and a DATE CHECK box that names the Thursday news left
out on purpose. 35 stories across 7 regions, all hard news; every story on the
page happened, or was first reported, on Friday 20 November 2026.

## Run

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` to the output directory (`$MAKEFUN_OUTPUT_DIR`, default
`/output`). The page itself is `frontpage.html`, rendered to `entry.png`
(1024×1024) with headless Chromium; the render is byte-identical across
runs.
