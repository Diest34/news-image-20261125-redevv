# The World in One Image — Wednesday, 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Diest34/news-image-20261125-redevv/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Diest34/news-image-20261125-redevv/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

An entry for the [make.fun](https://make.fun/r/y12bs3e6) bounty
**“Sum up 25 November's world news in one image”** — a newspaper front page
that sums up Wednesday, 25 November 2026 in a single picture.

## The image

A front page with the day's date up top, a three-scene photograph
(a Red Sea port under missile fire, a U.S. courtroom, a police cordon
outside a supermarket at night), and the five stories that defined the day:

1. **Houthis threaten Jeddah ports; coalition strikes Hodeidah** — after
   a drone hit Riyadh's PIF Tower, the coalition orders the port evacuated
   and the Houthis vow to hit Jeddah and every Saudi Red Sea port.
2. **Huawei convicted on 10 of 12 counts** — a Brooklyn jury finds bank
   fraud and trade-secret theft; racketeering acquitted.
3. **Gunmen hold 25 hostage in Cartagena supermarket** — after a failed
   armoured-truck robbery, masked men seize shoppers in an Éxito store;
   five elderly women freed.
4. **Zelensky: U.S. is blocking paid missile deliveries** — Kyiv says
   Washington is holding up weapons it already paid for as attacks go on.
5. **Germany forecasts a record €1 trillion tax haul** — Berlin expects
   tax revenue to top one trillion euros in 2027 for the first time.

Plus an “Also” line (Medvedev floats a preventive nuclear strike, the
CIA and ODNI report a breach of an unclassified network, the BJP and
Shiromani Akali Dal reunite) and a one-line summary of the day.

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to the harness output path. No network, deterministic output:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png — 1024×1024 PNG, under 1 MiB
```

## Licence

MIT — see [LICENSE](LICENSE).
