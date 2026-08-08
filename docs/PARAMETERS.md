# Parameters

Statutory parameters are fixed by the Regulation and carry an OSCAL `constraint` recording that they may not be relaxed; they are pre-set in the profiles.
Organisation-defined parameters are deliberately left unset — an assessment that finds one unset has found a real gap.

10 statutory · 10 organisation-defined

| Control | Parameter | Label | Value | Kind |
|---|---|---|---|---|
| `aia-4` | `aia-4_prm_1` | AI-literacy programme review frequency | — | organisation-defined |
| `aia-6` | `aia-6_prm_1` | Annex III use case(s) engaged | — | organisation-defined |
| `aia-9` | `aia-9_prm_1` | risk-management review interval | — | organisation-defined |
| `aia-11` | `aia-11_prm_1` | technical-documentation review interval | — | organisation-defined |
| `aia-15` | `aia-15_prm_1` | declared accuracy metric | — | organisation-defined |
| `aia-15` | `aia-15_prm_2` | declared accuracy threshold | — | organisation-defined |
| `aia-15` | `aia-15_prm_3` | robustness and cybersecurity test interval | — | organisation-defined |
| `aia-17` | `aia-17_prm_1` | quality-management-system review interval | — | organisation-defined |
| `aia-18` | `aia-18_prm_1` | documentation retention period | 10 years | statutory |
| `aia-19` | `aia-19_prm_1` | log retention period | 6 months | statutory |
| `aia-27` | `aia-27_prm_1` | fundamental-rights impact assessment review trigger | — | organisation-defined |
| `aia-51` | `aia-51_prm_1` | training-compute presumption threshold | 10^25 floating point operations | statutory |
| `aia-51` | `aia-51_prm_2` | Commission notification deadline | 2 weeks | statutory |
| `aia-73` | `aia-73_prm_1` | serious-incident reporting deadline (general) | 15 days | statutory |
| `aia-73` | `aia-73_prm_2` | serious-incident reporting deadline (widespread infringement or critical-infrastructure disruption) | 2 days | statutory |
| `aia-73` | `aia-73_prm_3` | serious-incident reporting deadline (death of a person) | 10 days | statutory |
| `aia-86` | `aia-86_prm_1` | explanation response time | — | organisation-defined |
| `aia-99` | `aia-99_prm_1` | maximum fine — Article 5 prohibited practices | EUR 35 000 000 or 7 % of total worldwide annual turnover for the preceding financial year | statutory |
| `aia-99` | `aia-99_prm_2` | maximum fine — other operator or notified-body obligations | EUR 15 000 000 or 3 % of total worldwide annual turnover for the preceding financial year | statutory |
| `aia-99` | `aia-99_prm_3` | maximum fine — incorrect, incomplete or misleading information | EUR 7 500 000 or 1 % of total worldwide annual turnover for the preceding financial year | statutory |

## Notes

- **`aia-4_prm_1`** (organisation-defined) — Organisation-defined. The Regulation sets no interval; select one proportionate to the rate of change in the deployed AI estate. An unset value is a readiness gap, not by itself proof of a legal breach.
- **`aia-9_prm_1`** (organisation-defined) — Organisation-defined. Article 9 requires 'regular systematic review' without fixing an interval; select one proportionate to the system's risk profile and rate of change, and shorten it on material change or after a serious incident.
- **`aia-11_prm_1`** (organisation-defined) — Organisation-defined. Article 11 requires the documentation be 'kept up to date'; select a review interval and additionally trigger review on every substantial modification. The interval itself is not statutory.
- **`aia-15_prm_1`** (organisation-defined) — Organisation-defined. Article 15(3) requires the metric to be declared in the instructions for use; it does not prescribe which metric.
- **`aia-15_prm_2`** (organisation-defined) — Organisation-defined. The Regulation prescribes no numeric floor; the threshold must be appropriate to the intended purpose and consistent with what is declared under Article 13.
- **`aia-15_prm_3`** (organisation-defined) — Organisation-defined. Select an interval proportionate to the threat model and rate of model or data change.
- **`aia-17_prm_1`** (organisation-defined) — Organisation-defined. Article 17 prescribes no interval; select one proportionate to the size of the organisation and the risk profile of its high-risk AI portfolio.
- **`aia-18_prm_1`** (statutory) — Fixed by Article 18(1): a period ending 10 years after the high-risk AI system has been placed on the market or put into service. Not organisation-defined; may not be shortened.
- **`aia-19_prm_1`** (statutory) — Article 19(1) sets a floor of six months unless otherwise provided in applicable Union or national law. A longer period may be selected where the intended purpose requires it; a shorter period requires a legal basis.
- **`aia-27_prm_1`** (organisation-defined) — Organisation-defined. Article 27(2) requires a new assessment where any of the described elements changes or is no longer up to date; define the triggers and a periodic review interval.
- **`aia-51_prm_1`** (statutory) — Fixed by Article 51(2) at 10^25 FLOP. The Commission may amend the threshold by delegated act under Article 51(3); verify the currently applicable value before relying on this parameter.
- **`aia-51_prm_2`** (statutory) — Fixed by Article 52(1): without delay and in any event within two weeks after the requirement is met or it becomes known that it will be met.
- **`aia-73_prm_1`** (statutory) — Fixed by Article 73(2): immediately, and in any event not later than 15 days after becoming aware. Not organisation-defined; may not be extended.
- **`aia-73_prm_2`** (statutory) — Fixed by Article 73(3): not later than two days after becoming aware of that incident.
- **`aia-73_prm_3`** (statutory) — Fixed by Article 73(4): immediately after establishing, or on suspecting, a causal relationship, and not later than 10 days after the date of becoming aware.
- **`aia-86_prm_1`** (organisation-defined) — Organisation-defined. Article 86 fixes no deadline; select one consistent with the organisation's obligations under applicable Union data protection law and with any national implementing rules.
- **`aia-99_prm_1`** (statutory) — Fixed by Article 99(3).
- **`aia-99_prm_2`** (statutory) — Fixed by Article 99(4).
- **`aia-99_prm_3`** (statutory) — Fixed by Article 99(5).
