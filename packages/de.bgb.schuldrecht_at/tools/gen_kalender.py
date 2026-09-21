#!/usr/bin/env python3
"""Calendar rows §85 in the lock of `de.bgb.schuldrecht_at` (scoped mode).

The dataset itself is defined ONCE, in `corpus/gen_kz_clir.py`
(`de_bgb_feiertage_calendar_dataset`, ledger D-03) and written by the package
tool of `de.bgb.fristen`; this package only BINDS it with its own node
`KALENDER_BUNDESWEIT`, because the deadline policy of a case lives in the
package whose program the case runs (LDC-E1332) and the calendar it reads must
live there too. `law engine lock --write` never derives such a row, so this
tool writes it — for this package's node and for the node of the imported
`de.bgb.fristen`, whose rules compute the ends of the periods.

    python3 corpus/laws/de/bgb/schuldrecht-at/tools/gen_kalender.py [--check]
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / "corpus"))
from gen_kz_clir import de_bgb_feiertage_calendar_dataset  # noqa: E402

PACKAGE = Path(__file__).resolve().parents[1]
NAME = "de-feiertage-bundesweit.calendar.json"
OUT = ROOT / "corpus/clir" / NAME
NODES = ("urn:de:corpus:clir:bgb-schuldrecht-at#KALENDER_BUNDESWEIT",
         "urn:de:corpus:clir:bgb-fristen#KALENDER_BUNDESWEIT")


def rows(digest: str) -> list[dict]:
    return [{"capability": "law.calendar/0.1", "contentHash": digest, "id": node,
             "kind": "calendar-dataset", "path": NAME} for node in NODES]


def main() -> int:
    raw = de_bgb_feiertage_calendar_dataset()
    digest = "sha256:" + hashlib.sha256(raw).hexdigest()
    declared = re.search(r'content_hash "([^"]+)"', (PACKAGE / "package.law").read_text(encoding="utf-8"))
    lock_path = PACKAGE / "law.lock"
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    wanted = rows(digest)
    if "--check" in sys.argv:
        problems = []
        local = PACKAGE / NAME
        if not OUT.is_file() or OUT.read_bytes() != raw:
            problems.append(f"stale dataset: {OUT}")
        if not local.is_file() or local.read_bytes() != raw:
            problems.append(f"stale in-package dataset: {local}")
        for row in wanted:
            if row not in lock.get("resources", []) or lock.get("lockVersion") != "0.2":
                problems.append(f"law.lock lacks the calendar row {row['id']} with {digest} (lock 0.2)")
        if not declared or declared.group(1) != digest:
            problems.append(f"package.law declares {declared.group(1) if declared else None}, dataset is {digest}")
        for problem in problems:
            print(problem)
        return 1 if problems else 0
    local = PACKAGE / NAME
    if not OUT.is_file() or OUT.read_bytes() != raw:
        OUT.write_bytes(raw)
        print(f"written {OUT.relative_to(ROOT)}")
    local.write_bytes(raw)
    resources = [r for r in lock.get("resources", []) if r.get("id") not in NODES]
    lock["resources"] = sorted(resources + wanted, key=lambda r: r["id"])
    lock_path.write_text(json.dumps(lock, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"written {lock_path.relative_to(ROOT)}: calendar rows {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
