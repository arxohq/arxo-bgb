#!/usr/bin/env python3
"""Calendar snapshot §85 of `de.bgb.fristen` in the scoped mode.

The dataset itself is defined ONCE, in `corpus/gen_kz_clir.py`
(`de_bgb_feiertage_calendar_dataset`): the full corpus run writes it into
`corpus/clir/` with the other calendar artefacts (registry
verify/ci/data/package-generators.json, generator `constant-artifacts`).
`gen_kz_clir.py --only …` does not write calendar datasets, so this tool
writes the same bytes for the scoped work of the task and the lock row of
the resource (`law engine lock --write` keeps a calendar row it finds in the
previous lock but never discovers the package's own dataset). `--check`
compares bytes, hash of the `calendar` declaration and the lock row.

    python3 corpus/laws/de/bgb/fristen/tools/gen_kalender.py [--check]
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
#: Packages that import `de.bgb.fristen`: `lawc test` resolves the calendar
#: through the CONSUMER's lock, so each of them needs the same resource row
#: (`law engine lock --write` does not derive it from the dependency).
CONSUMERS = (PACKAGE.parent / "uebergang", PACKAGE.parent / "dienst-werk",
             PACKAGE.parent / "ehe", PACKAGE.parent / "verfuegungen",
             PACKAGE.parent / "erbfolge", PACKAGE.parent / "bereicherung-delikt")
NAME = "de-feiertage-bundesweit.calendar.json"
OUT = ROOT / "corpus/clir" / NAME
LOCAL = PACKAGE / NAME
NODE = "urn:de:corpus:clir:bgb-fristen#KALENDER_BUNDESWEIT"


def main() -> int:
    raw = de_bgb_feiertage_calendar_dataset()
    digest = "sha256:" + hashlib.sha256(raw).hexdigest()
    entry = {"capability": "law.calendar/0.1", "contentHash": digest, "id": NODE,
             "kind": "calendar-dataset", "path": NAME}
    declared = re.search(r'content_hash "([^"]+)"', (PACKAGE / "package.law").read_text(encoding="utf-8"))
    locks = [(PACKAGE / "law.lock", entry)]
    for consumer in CONSUMERS:
        if (consumer / "law.toml").is_file():
            locks.append((consumer / "law.lock", entry))
    if "--check" in sys.argv:
        problems = []
        if not OUT.is_file() or OUT.read_bytes() != raw:
            problems.append(f"stale dataset: {OUT}")
        if not LOCAL.is_file() or LOCAL.read_bytes() != raw:
            problems.append(f"stale in-package dataset: {LOCAL}")
        for lock_path, row in locks:
            lock = json.loads(lock_path.read_text(encoding="utf-8")) if lock_path.is_file() else None
            if lock is None or row not in lock.get("resources", []) or lock.get("lockVersion") != "0.2":
                problems.append(f"{lock_path.relative_to(ROOT)} lacks the calendar row {NODE} with {digest} (lock 0.2)")
        if not declared or declared.group(1) != digest:
            problems.append(f"package.law declares {declared.group(1) if declared else None}, dataset is {digest}")
        for problem in problems:
            print(problem)
        return 1 if problems else 0
    OUT.write_bytes(raw)
    LOCAL.write_bytes(raw)
    for lock_path, row in locks:
        dest = lock_path.parent / NAME
        if dest != LOCAL:
            dest.write_bytes(raw)
        if not lock_path.is_file():
            continue
        lock = json.loads(lock_path.read_text(encoding="utf-8"))
        rows = [r for r in lock.get("resources", []) if r.get("id") != NODE] + [row]
        lock["resources"] = sorted(rows, key=lambda r: (r["id"], r["path"]))
        # A lock that carries resources is lock 0.2 (§11); `lock --write` of a
        # consumer without own sidecars leaves 0.1, which lawc refuses for §85.
        lock["lockVersion"] = "0.2"
        lock_path.write_text(json.dumps(lock, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
