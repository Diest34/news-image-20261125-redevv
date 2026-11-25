# News Image — 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Diest34/news-image-20261125-redevv/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Diest34/news-image-20261125-redevv/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image that sums up the world news of 25 November 2026.

## The entry

`entry.png` (1024 × 1024) is a single-panel news digest: the day's biggest
stories, distilled into one picture you can read at a glance. It was made
for the make.fun **News Image 20261125** bounty.

- **Bounty:** https://make.fun/bounty/news-image-20261125
- **Referral code:** `y12bs3e6`
- **Image:** `entry.png` — 1024 × 1024 PNG

## Reproduce it

```bash
python3 main.py
```

`main.py` copies the bundled `entry.png` to `/output/entry.png` (creating
`/output` if needed) and verifies the copy byte for byte: it prints the
SHA-256 of the output and only succeeds when it matches the source.

## How it works

1. `main.py` locates `entry.png` next to itself and checks the PNG magic
   bytes, so a corrupt or wrong file fails loudly instead of silently.
2. It copies the file to `/output/entry.png`, creating the folder first.
3. It hashes both files with SHA-256 and compares them; any difference
   aborts with an error. A successful run prints the output path, size,
   and hash.

## Files

| File | What it is |
| --- | --- |
| `entry.png` | The entry image, 1024 × 1024 |
| `main.py` | Deterministic reproduction script (Python 3.13) |
| `LICENSE` | MIT license |

## License

MIT — see [LICENSE](LICENSE).
