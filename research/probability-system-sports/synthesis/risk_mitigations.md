# Risk-Mitigation Summary

Compiled from 6 failure studies across academic and practitioner sources.

## Aggregated Risk-Mitigation Table

| # | Risk | Category | Likelihood | Impact | Mitigation | Evidence |
|---|------|----------|------------|--------|------------|----------|
| R1 | Accuracy-optimized model unprofitable | Model | HIGH | HIGH | Use calibration (Brier/ECE) for model selection, not accuracy | Zimmermann (2017), Walsh & Joshi (2023) |
| R2 | Data quality issues (outliers dominate P&L) | Data | MEDIUM | CRITICAL | Winsorize returns, inspect bet-level distributions, flag anomalous odds | Clegg & Cartlidge (2023) |
| R3 | Behavioral biases encoded in features | Model | MEDIUM | HIGH | Require causal mechanism for each feature; test for price efficiency before inclusion | Ötting et al. (2022) |
| R4 | Overfitting via parameter proliferation | Model | HIGH | CRITICAL | Limit model complexity; require theoretical justification for each variable; keep filters under 5 | Sports Insights (2013), TheOver (2026) |
| R5 | Look-ahead bias in backtesting | Process | HIGH | HIGH | Use timestamped decision-time odds; never use closing odds for historical evaluation | GreatBets (2025) |
| R6 | Regime change invalidates model | External | HIGH | HIGH | Walk-forward testing; regular model retraining; regime detection triggers | Reddit (2026), Clegg (2023) |
| R7 | Insufficient sample size for inference | Data | MEDIUM | HIGH | Power analysis before deployment; cross-validation; minimum 500+ bets before conclusions | Multiple sources |
| R8 | Market efficiency increase over time | External | HIGH | MEDIUM | Regular inefficiency monitoring; strategy re-calibration; expect edge decay | Clegg (2023) |

## Risk Categories

### Model Risks (R1, R3, R4)
Focus on calibration over accuracy, require causal justification for features, and limit complexity.

### Data Risks (R2, R7)
Data quality and sample size are critical. Single outliers can dominate results. Always inspect distributions.

### Process Risks (R5)
Backtesting methodology must use decision-time data. Look-ahead bias is the most common cause of backtest-to-live performance gap.

### External Risks (R6, R8)
Markets evolve. Build systems that detect and adapt to regime changes. Expect strategies to degrade.

## Implementation Checklist

- [ ] Calibration metrics (ECE, Brier) in model selection pipeline
- [ ] Data quality dashboard with outlier detection
- [ ] Feature documentation with causal mechanism
- [ ] Model complexity limits enforced
- [ ] Timestamped odds storage verified
- [ ] Walk-forward validation framework
- [ ] Sample size power analysis
- [ ] Market efficiency monitoring

---

*Risk analysis compiled: 2026-02-04*
*Sources: 6 failure studies (F1-F6)*
