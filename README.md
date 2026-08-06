# EU AI Act — OSCAL catalog

An [OSCAL](https://pages.nist.gov/OSCAL/) catalog, profiles and assessment plan for
**Regulation (EU) 2024/1689** (the EU Artificial Intelligence Act), **as amended by
Regulation (EU) 2026/1744** (the Digital Omnibus on AI, in force 27 July 2026).

Machine-readable EU AI Act obligations, so a compliance toolchain can treat the Act the
way it already treats NIST SP 800-53 or ISO 27001: import a catalog, select a profile,
run an assessment, emit evidence.

```
catalogs/eu-ai-act/catalog.json                        50 controls, Chapters I–V, IX, XII
profiles/prohibited-practices-and-ai-literacy/         15 controls · since 2025-02-02
profiles/transparency-article-50/                      18 controls · from 2026-08-02
profiles/gpai-model-provider/                          21 controls · since 2025-08-02
profiles/high-risk-deployer-annex-iii/                 26 controls · from 2027-12-02
profiles/high-risk-provider-annex-iii/                 40 controls · from 2027-12-02
assessment-plans/high-risk-provider-readiness/         5-step readiness assessment
docs/examples/template-system-security-plan.json       minimal SSP to start from
```

## The date most compliance material still gets wrong

Regulation (EU) 2026/1744 was published in the Official Journal on **24 July 2026** and
entered into force on **27 July 2026**. It rewrote Article 113:

| Obligation set | Applies from | Previously |
|---|---|---|
| Article 5 prohibitions, Article 4 AI literacy | 2 February 2025 | unchanged |
| GPAI model obligations (Chapter V) | 2 August 2025 | unchanged |
| **Article 50 transparency** | **2 August 2026** | **unchanged** |
| New Article 5(1)(ba)/(bb) prohibitions (NCII, CSAM) | 2 December 2026 | *newly inserted* |
| Article 50(2) marking, systems placed before 2 Aug 2026 | 2 December 2026 | *new transition* |
| **High-risk, stand-alone (Annex III)** | **2 December 2027** | ~~2 August 2026~~ |
| **High-risk, embedded in Annex I products** | **2 August 2028** | ~~2 August 2027~~ |

Two consequences worth stating plainly, because a lot of published guidance predates the
Omnibus and still says otherwise:

- **The high-risk deadline moved by sixteen months.** A readiness programme still
  working to 2 August 2026 for Annex III systems is working to a superseded date.
- **2 August 2026 is not empty.** Article 50 transparency lands then, and after the
  deferral it is the principal substantive obligation that does. If you only remember
  one thing from this repository, make it that the near-term obligation is transparency,
  not high-risk.

Every control carries its current application date and, where the Omnibus moved it, the
original one (`application-date` / `application-date-original`), plus `amended-by` and a
link to the amending regulation. See [`docs/AMENDMENTS.md`](docs/AMENDMENTS.md).

## Quickstart

```bash
git clone https://github.com/olon-standards/eu-ai-act-oscal.git && cd eu-ai-act-oscal
pip install compliance-trestle
trestle validate --all          # 7 models, expect rc=0
```

Resolve a profile into a flat catalog of the controls that apply to you:

```python
from pathlib import Path
from trestle.core.profile_resolver import ProfileResolver

catalog = ProfileResolver.get_resolved_profile_catalog(
    Path("."), "profiles/transparency-article-50/profile.json")
```

Which profile you want:

| You are | Profile |
|---|---|
| anyone placing or using AI systems in the EU | `prohibited-practices-and-ai-literacy` |
| shipping a chatbot, or generating synthetic audio/image/video/text | `transparency-article-50` |
| providing a general-purpose AI model | `gpai-model-provider` |
| providing an Annex III high-risk system | `high-risk-provider-annex-iii` |
| deploying an Annex III high-risk system | `high-risk-deployer-annex-iii` |

The prohibitions profile is a precondition for all the others, not an alternative to them.

## What this is not

- **Not legal advice, and not a conformity assessment.** A profile tells you which
  obligations are in scope. Only the Article 43 procedure produces conformity.
- **Not authoritative text.** Control statements are condensed restatements written for
  assessment use — not quotations. Where a statement and the Official Journal text
  differ, [the Official Journal text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)
  governs. Every control links to it.
- **Not complete.** 50 of the Act's 113 articles are modelled: the operator-facing ones.
  Institutional articles (notified-body designation, governance bodies, the EU database,
  Commission procedure) are out of scope. [`docs/SCOPE.md`](docs/SCOPE.md) lists exactly
  what is in and out, and why.
- **Not a resolved answer on every date.** Chapter IX applies from 2 August 2026 while
  the high-risk obligations its provisions concern were deferred to 2 December 2027. This
  catalog records that interaction as **unresolved** on Articles 72, 73 and 86 rather
  than asserting a date it cannot support.

## Prior art

There is, as far as we can establish, no other published OSCAL **catalog** for the EU AI
Act. There is adjacent work worth knowing about: the
[Venturalitica SDK](https://github.com/Venturalitica/venturalitica-sdk) (Apache-2.0)
carries an OSCAL assessment-plan contract over Articles 9–15 with property extensions,
built as a research artifact. It is profile- and assessment-plan-shaped rather than a
catalog, and covers seven articles to this catalog's fifty — but it got there first on
the assessment-plan side and the claim here is narrower for it.

If you know of other OSCAL content for the Act, please open an issue; a wrong
first-mover claim is worse than no claim.

## Parameters

Statutory values are pre-set and constrained — the 15/10/2-day incident deadlines
(Article 73), the 10-year documentation retention (Article 18), the 6-month log floor
(Article 19), the 10^25 FLOP threshold (Article 51), the fine ceilings (Article 99).
They are recorded as OSCAL parameters with `constraints` explaining that they may not be
relaxed.

Organisation-defined values are deliberately **left unset** — review intervals, accuracy
metric and threshold, test frequencies. An assessment that finds them unset has found a
real gap, which is the point. See [`docs/PARAMETERS.md`](docs/PARAMETERS.md).

## Contributing

Corrections to article numbers, citations, dates and obligation statements are the most
valuable contributions here; accuracy is the whole product. See
[`CONTRIBUTING.md`](CONTRIBUTING.md). Contributions are under the Apache-2.0 licence with
a [DCO](DCO) sign-off.

## Maintainer

Miltos Makridis <standards@olon.media>

## Licence

Apache-2.0 — see [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE). The underlying legislation
is reproduced in condensed form under the EU's reuse policy for legislative texts; the
Official Journal remains the authoritative source.

Commercial readiness-assessment enquiries: standards@olon.media
