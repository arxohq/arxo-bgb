# arxo-bgb.git

[![LightNow capabilities](https://lightnow.ai/badge/io.arxo/de-bgb)](https://lightnow.ai/servers/io.arxo/de-bgb)

Pinned canon, executable as it stands: source text with provenance, the
model built over it and the scenarios that check its answers. The norms
here are data — they are executed by `law`; this repository carries no
rule code of its own.

## Contents

| Package | Version | Scenarios | Dependencies |
|---|---|---|---|
| `calc.kinship` | 0.1.0 | 39 | 0 |
| `de.bgb.core` | 0.1.0 | 1 | 0 |
| `doctrine.ius_privatum` | 0.1.0 | 37 | 0 |
| `de.bgb.fristen` | 0.1.0 | 86 | 1 |
| `de.bgb_1896` | 0.1.0 | 5 | 1 |
| `de.bgb.allgemeiner_teil` | 0.1.0 | 21 | 3 |
| `de.bgb.besitz_eigentum` | 0.1.0 | 143 | 2 |
| `de.bgb.betreuung` | 0.1.0 | 110 | 2 |
| `de.bgb.dienst_werk` | 0.1.0 | 210 | 2 |
| `de.bgb.ehe` | 0.1.0 | 57 | 3 |
| `de.bgb.ius_privatum` | 0.1.0 | 1 | 3 |
| `de.bgb.miete` | 0.1.0 | 31 | 2 |
| `de.bgb.sonstige_vertraege` | 0.1.0 | 498 | 2 |
| `de.bgb.uebergang` | 0.1.0 | 15 | 2 |
| `de.bgb.dingliche_rechte` | 0.1.0 | 123 | 3 |
| `de.bgb.erbfolge` | 0.1.0 | 40 | 4 |
| `de.bgb.schuldrecht_at` | 0.1.0 | 51 | 4 |
| `de.bgb.verwandtschaft` | 0.1.0 | 82 | 4 |
| `de.bgb.bereicherung_delikt` | 0.1.0 | 71 | 5 |
| `de.bgb.kauf` | 0.1.0 | 90 | 5 |
| `de.bgb.verfuegungen` | 0.1.0 | 82 | 5 |

## How it is verified

Every package is built by `package.py` with the pinned toolchain: compilation,
§267 scenarios on both evaluators, replay of saved evaluations and a rebuild
from the release itself. A failure of any step stops the build.

```sh
python3 tools/toolchain.py download --lock toolchain.lock.json --out /tmp/law-tools
python3 /tmp/law-tools/package.py packages/<name> \
    --lawc /tmp/law-tools/law-cli --offline --out /tmp/<name>-release
```

## Dependencies

Dependency bytes are pinned under `packages/<name>/deps/` and verified against the `contentHash` recorded in `law.lock`: the build and the CI are offline.

## Asking these packages

Two ways, the same slice of the canon and the same engine; the
difference is whose machine evaluates.

- **Hosted**: `https://mcp.arxo.io/mcp/de-bgb` — requests are evaluated on Arxo infrastructure.
- **Local**: `docker compose -f mcp/compose.yml up` — nothing leaves the machine.

`mcp/pin.json` records what either one must answer from: the
content hash of the canon profile, the pinned packages, the ABI
version of the engine and the availability of the hosted endpoint.
An answer that cannot be traced to that pin is not this repository's
answer.

## Worked cases

Each collection is a case package of its own: the facts, the questions and
the answers, with the pinned canon as its dependency. Ask one from its
directory with `law ask .` — nothing is downloaded.

| Collection | Cases | Questions |
|---|---:|---:|
| [`packages/de.bgb.fristen/examples/ein-fall-drei-kodizes`](packages/de.bgb.fristen/examples/ein-fall-drei-kodizes/README.md) | 6 | 4 |
| [`packages/de.bgb.fristen/examples/fristenrechner`](packages/de.bgb.fristen/examples/fristenrechner/README.md) | 8 | 16 |
| [`packages/de.bgb_1896/examples/ein-fall-zwei-jahrhunderte`](packages/de.bgb_1896/examples/ein-fall-zwei-jahrhunderte/README.md) | 5 | 6 |
| [`packages/de.bgb.miete/examples/kuendigung-und-mieterhoehung`](packages/de.bgb.miete/examples/kuendigung-und-mieterhoehung/README.md) | 6 | 14 |
| [`packages/de.bgb.uebergang/examples/vor-und-nach-2002`](packages/de.bgb.uebergang/examples/vor-und-nach-2002/README.md) | 4 | 9 |
| [`packages/de.bgb.erbfolge/examples/erbfolge-und-pflichtteil`](packages/de.bgb.erbfolge/examples/erbfolge-und-pflichtteil/README.md) | 8 | 18 |
| [`packages/de.bgb.schuldrecht_at/examples/rechtsbehelfe`](packages/de.bgb.schuldrecht_at/examples/rechtsbehelfe/README.md) | 6 | 6 |
| [`packages/de.bgb.schuldrecht_at/examples/verzugszinsen`](packages/de.bgb.schuldrecht_at/examples/verzugszinsen/README.md) | 5 | 9 |
| [`packages/de.bgb.schuldrecht_at/examples/widerruf`](packages/de.bgb.schuldrecht_at/examples/widerruf/README.md) | 6 | 12 |

## Rights

Code and model: see `LICENSE`. The pinned texts of the publishers keep their
own terms of reproduction, listed per package in `NOTICE`; those terms are
not covered by the code licence.

Maintainer: Rifat Dzhumagulov (hi@arxo.io). Address: git@github.com:arxohq/arxo-bgb.git.
