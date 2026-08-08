# Changelog

## 0.1.1 — 2026-08-09

Legal-accuracy and release-hardening update.

- Corrected the assessment-plan and Annex I provider dates to 2 December 2027 and
  2 August 2028 respectively.
- Aligned Articles 4a, 5, 6, 10, 17 and 99 with Regulation (EU) 2026/1744, including
  deletion of Article 10(5), provider/deployer conditions for the new prohibitions,
  Article 6(1a)–(1c), and the undertaking condition for percentage-based fines.
- Connected every OSCAL parameter to a control statement and removed the contradictory
  `none` selection from the Annex III use-case parameter.
- Normalised amendment metadata, documented prior OSCAL component-definition work, and
  recorded that independent legal review remains pending.
- Pinned the validation dependency and added content-regression checks.

## 0.1.0 — 2026-08-07

First release. Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744
(in force 27 July 2026).

- OSCAL 1.1.2 catalog: 50 operator-facing controls, Chapters I–V, IX and XII.
- Five profiles: prohibited practices and AI literacy; Article 50 transparency; GPAI
  model provider; Annex III high-risk provider; Annex III high-risk deployer.
- Assessment plan: five-step high-risk provider readiness assessment.
- Template system security plan under `docs/examples/`.
- Amendment layer modelled explicitly: `application-date` / `application-date-original`,
  `amended-by`, `inserted-by`. High-risk deferral to 2027-12-02 / 2028-08-02 reflected.
- Articles 72, 73 and 86 marked `application-date-status: unresolved` — see
  `docs/AMENDMENTS.md`.
