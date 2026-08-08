# Legal review status

This repository is a non-authoritative engineering representation of Regulation (EU)
2024/1689 as amended by Regulation (EU) 2026/1744. It is not legal advice.

## Current status

- Primary-source comparison by the maintainers: completed for release 0.1.1 on
  9 August 2026.
- OSCAL schema, profile-resolution and content-regression checks: automated in CI.
- Independent review by a qualified EU AI Act lawyer: **pending**.

Until the independent review is completed, users should verify decisions against the
Official Journal and obtain advice for their facts and jurisdiction. A green automated
check proves structural consistency; it does not prove a legal interpretation.

## Independent-review checklist

The reviewer should record their name or organisation, date, source version and findings,
and should cover at least:

1. control-to-article mapping and omitted operator obligations;
2. current application dates after Regulation (EU) 2026/1744;
3. Articles 4a, 5(1)(ba)/(bb), 6, 10, 17, 50, 72, 73, 86 and 99;
4. the unresolved Chapter IX timing described in `AMENDMENTS.md`; and
5. whether each organisation-defined parameter is clearly separated from statutory law.

Completion should be recorded in a pull request with the review evidence or a stable
reference to it. Do not replace this status with a verbal assurance.
