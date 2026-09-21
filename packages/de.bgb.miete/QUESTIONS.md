# Open questions

- This package's README/QUESTIONS status is file-only. Dual evaluation,
  bytewise differential and the named SHA for the current 33-package goal
  remain pending; §9 is not demonstrated and this is not a PASS claim.
- The marker scanner currently reads `analysis/saetze.json`, whose entries
  contain `status` and `witness` but no sentence text. The pinned article text
  in `sources.law` therefore needs an explicit scanner input decision before
  automated marker counts can replace the manual P2 ledger audit.
- Maintenance positions need a completeness certificate before they can be
  observed as `SATISFIED`; a single supporting fact correctly leaves the
  position `ACTIVE`.
