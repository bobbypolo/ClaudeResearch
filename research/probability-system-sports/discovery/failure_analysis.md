# Failure Analysis Pass

## Failure Study 1: Overfitting in Backtesting

### Source: Zimmermann (2017) - "Wages of wins"
- arXiv: 1702.05982

### What They Tried
- Method: ML models for match outcome prediction in NCAAB, NBA, NFL
- Context: Testing whether high-accuracy models translate to betting profits

### What Failed
- **Failure Mode**: High accuracy did not equal high payouts
- **Root Cause**: Models predicted correctly on "easy" matches (high favorite wins) but these have poor odds. Valuable bets are in uncertain matches where models performed worse.
- **When Discovered**: Out-of-sample testing against real betting markets

### Lessons Learned
1. Accuracy is a misleading metric for betting - calibration matters more
2. The type of matchups correctly predicted determines value, not overall accuracy
3. Markets are efficient on high-confidence outcomes

### Risk-Mitigation Pair
| Risk | Likelihood | Impact | Mitigation | Evidence |
|------|------------|--------|------------|----------|
| Model optimizes for accuracy, not profit | HIGH | HIGH | Use calibration metrics (Brier, ECE) for model selection | Walsh & Joshi (2023) |

---

## Failure Study 2: Data Quality in Backtesting

### Source: Clegg & Cartlidge (2023) - "Not feeling the buzz"
- arXiv: 2306.01740

### What They Tried
- Method: Replication of "buzz factor" betting strategy using Wikipedia page views
- Context: Tennis betting market, original study claimed profitable strategy

### What Failed
- **Failure Mode**: Single outlier bet ("Hercog bet") with erroneous odds drove majority of profits
- **Root Cause**: Data quality issue - one bet with incorrectly long odds dominated P&L
- **When Discovered**: During replication study examining individual bet records

### Lessons Learned
1. Always inspect individual bet distributions for outliers
2. Data cleaning is mandatory before backtesting conclusions
3. Markets may have become more efficient post-2020; strategies degrade over time
4. Replication studies are critical for validating betting research

### Risk-Mitigation Pair
| Risk | Likelihood | Impact | Mitigation | Evidence |
|------|------------|--------|------------|----------|
| Outlier bets dominate backtest P&L | MEDIUM | CRITICAL | Winsorize returns, inspect bet-level distributions | Clegg & Cartlidge (2023) |
| Historical inefficiencies closed | HIGH | HIGH | Regular strategy re-calibration, out-of-sample validation | Clegg & Cartlidge (2023) |

---

## Failure Study 3: Momentum Betting Fallacy

### Source: Ötting et al. (2022) - "Gambling on Momentum"
- arXiv: 2211.06052

### What They Tried
- Method: Betting on teams with "momentum" after equalizing goals
- Context: German Bundesliga live betting, high-frequency bookmaker data

### What Failed
- **Failure Mode**: Bettors staked 40% more on teams with apparent momentum; betting on momentum would lead to substantial losses
- **Root Cause**: Perceived momentum does not affect match outcomes on average; bookmaker does not offer favorable odds for momentum
- **When Discovered**: Analysis of staking patterns vs outcomes

### Lessons Learned
1. Behavioral biases (momentum illusion) are exploited by bookmakers
2. Markets efficiently price behavioral patterns
3. Cognitive biases lead to systematic losses

### Risk-Mitigation Pair
| Risk | Likelihood | Impact | Mitigation | Evidence |
|------|------------|--------|------------|----------|
| Incorporating spurious signals (momentum) | MEDIUM | HIGH | Require causal mechanism for each feature; test for price efficiency | Ötting et al. (2022) |

---

## Failure Study 4: Overfitting via Excessive Parameters

### Source: TheOver Blog (2026) + Sports Insights (2013)
- URLs: blog.theover.ai, sportsinsights.com

### What They Tried
- Method: Adding many filters (10+) to betting systems based on top-performing historical data
- Context: Commercial betting system development

### What Failed
- **Failure Mode**: Models show excellent backtest performance but fail badly in live betting
- **Root Cause**: Capturing random noise rather than repeatable patterns; no underlying theory
- **When Discovered**: Live deployment

### Lessons Learned
1. Having an underlying theory/hypothesis is critical - data should increase/decrease confidence, not dictate the system
2. Keep strategy logic simple and rule-based
3. Large sample size required for robust conclusions
4. Must be able to "explain the edge"

### Risk-Mitigation Pair
| Risk | Likelihood | Impact | Mitigation | Evidence |
|------|------------|--------|------------|----------|
| Overfitting through parameter proliferation | HIGH | CRITICAL | Limit model complexity; require theoretical justification for each variable | Sports Insights (2013), TheOver (2026) |

---

## Failure Study 5: Look-Ahead Bias

### Source: GreatBets UK (2025)
- URL: greatbets.co.uk

### What They Tried
- Method: Backtesting using odds not actually available at bet placement time
- Context: Sports betting model validation

### What Failed
- **Failure Mode**: Backtest shows profit; live trading shows loss
- **Root Cause**: Using closing odds for evaluation when bets would have been placed at different (worse) odds
- **When Discovered**: Transition from backtest to live betting

### Lessons Learned
1. Use odds that were actually available at decision time
2. Line movement means closing odds ≠ placement odds
3. Market efficiency increases near event start

### Risk-Mitigation Pair
| Risk | Likelihood | Impact | Mitigation | Evidence |
|------|------------|--------|------------|----------|
| Look-ahead bias in backtesting | HIGH | HIGH | Use timestamped odds data; calculate at decision time, not closing | GreatBets (2025) |

---

## Failure Study 6: Regime Change

### Source: Reddit r/algotrading (2026)
- URL: reddit.com/r/algotrading

### What They Tried
- Method: Deploying strategies developed under historical market conditions
- Context: General algorithmic trading (applicable to sports betting)

### What Failed
- **Failure Mode**: Live strategy underperforms backtest
- **Root Cause**: Hidden assumptions - regime stability, perfect execution, stationarity
- **When Discovered**: Extended live trading periods

### Lessons Learned
1. Sports evolve: rule changes, player development, team dynamics
2. Market efficiency changes over time
3. Execution conditions differ from theoretical models

### Risk-Mitigation Pair
| Risk | Likelihood | Impact | Mitigation | Evidence |
|------|------------|--------|------------|----------|
| Regime change invalidates model | HIGH | HIGH | Walk-forward testing; regular model retraining; regime detection | Reddit (2026), Clegg (2023) |

---

## Aggregated Risk-Mitigation Table

| # | Risk | Category | Likelihood | Impact | Mitigation | Evidence |
|---|------|----------|------------|--------|------------|----------|
| R1 | Accuracy-optimized model unprofitable | Model | HIGH | HIGH | Use calibration (Brier/ECE) for selection | S1, Zimmermann |
| R2 | Data quality issues (outliers) | Data | MEDIUM | CRITICAL | Winsorize, inspect distributions | Clegg (2023) |
| R3 | Behavioral biases in features | Model | MEDIUM | HIGH | Require causal mechanism | Ötting (2022) |
| R4 | Overfitting via parameters | Model | HIGH | CRITICAL | Limit complexity, require theory | Sports Insights |
| R5 | Look-ahead bias | Process | HIGH | HIGH | Use timestamped decision-time odds | GreatBets |
| R6 | Regime change | External | HIGH | HIGH | Walk-forward, regular retraining | Reddit, Clegg |
| R7 | Insufficient sample size | Data | MEDIUM | HIGH | Power analysis, cross-validation | Multiple |
| R8 | Market efficiency increase | External | HIGH | MEDIUM | Regular inefficiency monitoring | Clegg (2023) |

---

*Failure analysis completed: 2026-02-04*
*Sources analyzed: 6 academic + 4 practitioner*
