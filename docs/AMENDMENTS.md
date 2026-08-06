# Amendments — Regulation (EU) 2026/1744 (Digital Omnibus on AI)

**Regulation (EU) 2026/1744** of the European Parliament and of the Council of 8 July
2026, amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230.
Published in the Official Journal **24 July 2026**; entered into force **27 July 2026**
(third day after publication — a compressed timeline justified by urgency, because the
general application date it amends fell on 2 August 2026).

ELI: <https://eur-lex.europa.eu/eli/reg/2026/1744/oj>

This catalog models the AI Act **as amended**. The amendment layer is kept explicit —
every affected control carries `amended-by`, `amended-in-force`, and where a date moved,
both `application-date` and `application-date-original` — so that what changed stays
auditable instead of being silently folded into the base text.

## Application dates as rewritten

| Applies from | Obligations |
|---|---|
| 2 February 2025 | Chapters I and II — Article 5 prohibitions (a)–(h), Article 4 AI literacy |
| 2 August 2025 | Chapter V (GPAI), Chapter VII, Chapter XII, Chapter III §4, Article 78 |
| 27 July 2026 | Amended Article 4, new Article 4a, amended Article 99(1) and 99(6a), rewritten Article 113 |
| **2 August 2026** | **Article 50 transparency** · Article 11(1) SME template · Article 43(3) · Annex VIII §B reduction · Articles 75, 75a–75d |
| 2 December 2026 | New Article 5(1)(ba) and 5(1)(bb) prohibitions · Article 50(2) marking for systems placed before 2 Aug 2026 (Article 111(4)) |
| **2 December 2027** | **High-risk, stand-alone Annex III** — Chapter III requirements and operator obligations |
| 2 August 2028 | High-risk, embedded in Annex I products (Article 6(1)) |

## Control-level changes

**Deferred** (25 controls, all Chapter III): `aia-6`, `aia-8` … `aia-27`, `aia-43`,
`aia-47`, `aia-48`, `aia-49` — from 2026-08-02 to **2027-12-02**. `aia-6` additionally
carries the Annex I limb, moved from 2027-08-02 to **2028-08-02**.

**Inserted**: `aia-4a` (special-category data for bias detection and correction),
`aia-5.1.ba` (non-consensual intimate imagery), `aia-5.1.bb` (child sexual abuse
material).

**Substantively amended without a date change**:

| Control | Change |
|---|---|
| `aia-3` | SME and small mid-cap (SMC) definitions added; "safety component" rewritten — feeds Article 6 classification |
| `aia-4` | Softened: "take measures to support the development of AI literacy", replacing "ensure, to their best extent, a sufficient level of" |
| `aia-10` | Read with the new Article 4a, which generalises the special-category-data permission beyond Article 10(5) |
| `aia-11` | SMEs/SMCs may use a simplified Commission template for Annex IV (amendment applies 2026-08-02) |
| `aia-15` | Cyber Resilience Act compliance deemed to satisfy the cybersecurity requirement (new Article 42(3)) |
| `aia-17` | QMS proportionate to organisation size; simplified options for SMEs/SMCs (new Article 63(1)) |
| `aia-27` | FRIA/DPIA cross-references clarified; AI Office to provide an automated template tool |
| `aia-43` | Bodies notified under other harmonisation legislation apply by 28 January 2028 |
| `aia-49` | Annex VIII §B registration reduced (points 7 and 9 deleted); Article 6(3) self-assessed systems still register |
| `aia-50` | **Not deferred.** Marking transition to 2026-12-02 for pre-existing generative systems (Article 111(4)); Article 50(7) Commission power retained |
| `aia-99` | Non-monetary enforcement measures added to 99(1); new 99(6a) caps SMC fines at the lower of percentage or fixed amount |

## The unresolved question

Chapter IX — post-market monitoring (Article 72), serious-incident reporting (Article 73)
and the right to explanation (Article 86) — **applies from the unchanged general date of
2 August 2026**. None of those three articles appears among the provisions the Omnibus
amended.

But their subject matter is high-risk AI systems, and the obligations of stand-alone
Annex III high-risk systems were deferred to 2 December 2027. So on a literal reading,
from 2 August 2026 a provider owes post-market monitoring and incident reporting for a
class of system that does not yet owe any of the Chapter III obligations those provisions
presuppose.

Two readings are available:

1. **Literal** — Chapter IX applies 2 August 2026; the duties attach to any system that
   *is* high-risk, and Article 6(2) classification itself is deferred, so in practice
   nothing is in scope until 2 December 2027 and the earlier date is inert.
2. **Purposive** — the deferral carries the whole high-risk regime including its
   post-market limb, and 2 December 2027 is the operative date for these three too.

Both reach nearly the same practical result, but they differ for a provider whose system
was already classified high-risk before the deferral. **This catalog does not choose.**
Articles 72, 73 and 86 carry `application-date: 2026-08-02` (the date the Regulation
actually states for Chapter IX) together with
`application-date-status: unresolved-see-docs-amendments` and guidance pointing here.

If the Commission issues guidance or a consolidated reading settles this, that is a
correction worth an issue and a release.

## Provenance

Article structure and titles for the base Regulation were verified on 2026-07-27 against
the Official Journal text and cross-checked against per-article renderings. The amendment
layer was verified the same day against the Official Journal text of Regulation (EU)
2026/1744 for Articles 4, 4a, 5(1)(ba), 5(1)(bb), and against the recitals for the
Article 113 dates; the full replacement text of Article 113 was not retrievable in the
excerpt available and its dates are corroborated by three independent secondary analyses
in agreement. Treat the Article 113 dates as high-confidence but re-check them against
the consolidated text when EUR-Lex publishes it.
