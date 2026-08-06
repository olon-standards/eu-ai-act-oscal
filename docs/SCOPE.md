# Scope

## What is modelled

50 controls covering the **operator-facing** obligations of Regulation (EU) 2024/1689 —
the duties that fall on providers, deployers, importers and distributors, and that an
organisation can be assessed against.

| Chapter | Articles modelled | Note |
|---|---|---|
| I — General provisions | 1, 2, 3, 4, 4a | 4a inserted by Reg (EU) 2026/1744 |
| II — Prohibited AI practices | 5(1)(a)–(h), 5(1)(ba), 5(1)(bb) | (ba) and (bb) inserted by the Omnibus |
| III §1 — Classification | 6 | |
| III §2 — Requirements | 8, 9, 10, 11, 12, 13, 14, 15 | |
| III §3 — Operator obligations | 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27 | |
| III §5 — Conformity, marking, registration | 43, 47, 48, 49 | |
| IV — Transparency | 50 | |
| V — GPAI models | 51, 53, 54, 55 | |
| IX §1–2 — Post-market, incidents | 72, 73 | |
| IX §4 — Remedies | 85, 86 | |
| XII — Penalties | 99 | included so findings can be weighted by exposure |

## What is deliberately not modelled

**Institutional and procedural articles.** These bind the Commission, Member States,
notifying authorities, notified bodies and the AI Office — not the operators this catalog
is for. Modelling them would produce controls nobody can be assessed against.

- Chapter III §4 (Articles 28–39) — designation and operation of notified bodies.
  Article 43(3) is referenced from the conformity-assessment control where it bears on
  operators.
- Chapter III §5 procedure (Articles 40, 41, 42, 44, 45, 46) — harmonised standards,
  common specifications, presumption of conformity, certificates, derogation. Article
  42(3) (Cyber Resilience Act equivalence) is noted in the Article 15 guidance.
- Chapter VI (Articles 57–63) — regulatory sandboxes and real-world testing. Relevant to
  operators who opt in; a candidate for a future `sandbox-participant` profile rather
  than the core catalog.
- Chapter VII (Articles 64–70) — governance: AI Office, the Board, advisory forum,
  scientific panel, national competent authorities.
- Chapter VIII (Article 71) — the EU database itself. The operator's *duty to register*
  in it is modelled as Article 49.
- Chapter IX §3 and §5 (Articles 74–84, 88–94) — market surveillance and enforcement
  powers, including the Articles 75, 75a–75d AI Office powers added by the Omnibus.
  Article 79(1) ("presenting a risk") is referenced from Articles 12 and 20 where the
  operator obligation depends on it.
- Chapter X (Articles 95, 96) — voluntary codes of conduct and Commission guidelines.
- Chapter XI (Articles 97, 98) — delegated acts and committee procedure.
- Articles 100 and 101 — penalties for Union institutions and for GPAI model providers.
  Article 99 is modelled; these two are not.
- Chapter XIII (Articles 102–113) except as amendment provenance — amendments to other
  Union instruments, transitional provisions, evaluation, entry into force. Article
  111(4) is referenced from Article 50 because it carries the marking transition.
- **Annexes** are referenced, not modelled as controls. Annex III drives an OSCAL
  `select` parameter on Article 6; Annex IV is linked from Article 11; Annexes V, VI,
  VII, VIII, XI, XII are cited in the controls that invoke them.

## Known limits of this release

1. **Chapter IX date interaction is unresolved.** Chapter IX applies from the unchanged
   general date of 2 August 2026; the high-risk obligations its provisions concern were
   deferred to 2 December 2027. Articles 72, 73 and 86 therefore carry
   `application-date-status: unresolved-see-docs-amendments` rather than a date this
   catalog cannot support. See [`AMENDMENTS.md`](AMENDMENTS.md).
2. **Article 5(1)(ba)/(bb) paragraph designations** are taken from the Official Journal
   text of Regulation (EU) 2026/1744 as read on 2026-07-27, three days after publication.
   Consolidated EUR-Lex renderings were not yet available; re-check against the
   consolidated text when it appears.
3. **Statements are restatements.** They are written to be assessable, which sometimes
   means splitting a paragraph or naming an implicit actor. They are not quotations.
4. **No XML or YAML serialisations** are shipped. Convert with `trestle` or `oscal-cli`
   if you need them.
5. **Single language.** English only.
