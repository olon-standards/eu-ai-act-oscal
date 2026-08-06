# Contributing

Accuracy is the product. The most valuable contributions are corrections.

## What is most wanted

1. **Citation errors** — a wrong article number, paragraph, annex reference or date.
   Please include the Official Journal text you checked against.
2. **Obligation statements that misstate the law** — a restatement that is materially
   narrower, broader, or that assigns a duty to the wrong operator.
3. **Amendment tracking** — the Act is being amended. If a provision changes and this
   catalog still reflects the old text, that is a defect.
4. **Missing operator-facing obligations** — see `docs/SCOPE.md` for what is deliberately
   out of scope before filing.
5. **Prior art** — if other OSCAL content exists for the Act, the README's claim needs
   narrowing. Please say so.

## Ground rules

- **Cite the Official Journal.** A change to a control statement, article number or date
  needs a link to <https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng> (or the relevant
  amending regulation) and the text you relied on. Secondary sources are useful context
  but do not settle a citation.
- **Don't assert a date the text doesn't give.** Where the Regulation is genuinely
  ambiguous, the catalog records it as unresolved. Adding a confident date to an
  unresolved item needs the primary source that resolves it.
- **Statutory parameters may not be relaxed.** Values fixed by the Regulation carry an
  OSCAL `constraint` saying so. Changing one is a citation change, not a preference.
- **Validate before opening a PR**: `./scripts/validate.sh` must pass.

## Sign-off

Contributions are under Apache-2.0 with a Developer Certificate of Origin sign-off
(see `DCO`). Add `Signed-off-by: Name <email>` to each commit — `git commit -s`.
