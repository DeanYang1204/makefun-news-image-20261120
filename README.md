[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/DeanYang1204/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/DeanYang1204/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Built for [make.fun's "Sum up 20 November's world news in one image" bounty](https://make.fun/bounty/news-image-20261120) — $250 in USDC.

# Friday 20 November 2026 — the day in one image

Entry for make.fun's **news-image-20261120** bounty ($250, 50 paid places).
One 1024×1024 image that sums up Friday 20 November 2026 in four stories,
laid out as a newspaper front page: a header naming the day, a 2×2 grid of
photographic panels, and a short factual caption under each one. All type is
drawn with PIL — no generated panel carries any text, so nothing is garbled.

## The four stories (all happened / first reported on 20 November 2026)

1. **CYCLONE AKVAN HITS — Landfall near Gopalpur, Odisha, at noon.**
   Severe cyclonic storm crosses the coast with winds 90–100 km/h, gusts to
   110; over 300,000 people evacuated (IMD bulletin; live evacuation tracker).
   The 19 November entry covered the storm's approach; the landfall is the
   distinct 20 November event.
2. **PHILLIPS MAKES HISTORY — Glenn Phillips hits 118 in Wellington.**
   On day 2 of the first Test at Basin Reserve, Phillips becomes the first
   player to score centuries against India in all three formats in one
   calendar year (ICC).
3. **COP31 CLOSES TODAY — Final day in Antalya.**
   The latest draft cover decision drops every fossil-fuel reference, cut
   from 144 paragraphs to 80; the adaptation-finance target of $120 billion
   a year by 2035 is kept.
4. **GUPTA SENTENCED — New York court sentences him today.**
   Nikhil Gupta, who pleaded guilty in February 2026 to a murder-for-hire
   plot targeting Gurpatwant Singh Pannun, is sentenced by the US District
   Court in New York; prosecutors sought 24 years.

Earlier stories (the Shenzhen summit, GTA VI, the ICJ Myanmar ruling, the
Han Duck-soo retrial, the US–Venezuela deal, the Anthropic IPO) all landed
on 18–19 November and are not presented as today's news.

## How it was made

- Four square panels generated with Gemini (web version), one per story,
  photographic/editorial style, with no text in the generated images. Each
  panel was read back at full resolution: no garbled text, the US flag on
  the courthouse is correct, the conference flags are clean.
- The front page was composed with PIL
  (`~/workspace/makefun-news20-dev/compose.py`, kept out of this repo):
  navy header band with the date, 2×2 grid, captions drawn in DejaVu Sans.
- The finished image was read back visually: the date is prominent, all
  four stories are recognisable, captions are legible and match the facts,
  no garbled text, no fifth story.

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), after checking the
image is a whole JPEG or PNG, at most 1 MiB, and exactly 1024×1024. Two
runs write byte-identical files.

## Verification

- `entry.png`: JPEG, 1024×1024, 279,870 bytes
  (sha256 `c1710e2e6ae25ddf77b1c8b913229c15043dd1bb0f56eaa595d1c58ba11c52ee`)
- Two runs of `main.py` produce the same sha256.

## License

MIT — see [LICENSE](LICENSE).
