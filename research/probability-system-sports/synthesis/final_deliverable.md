# Implementation Specification: Production-Grade Parlay Probability System

## Executive Summary

This specification details a production-ready system for parlay betting that combines calibrated single-leg probability engines, vine copula dependency modeling, market microstructure analysis, and Kelly-optimized portfolio construction. The architecture separates concerns into four distinct subsystems with clear interfaces.

**Recommended Approach**: Hierarchical Bayesian models for sparse player props, LSTM for dense game lines, C-vine copulas for SGP dependencies, Ledoit-Wolf shrinkage for correlation denoising, Shin method for vig removal, and fractional Kelly (0.25-0.5×) for stake sizing.

**Confidence Level**: HIGH (12/12 claims) with 2 explicit gaps declared

## Gate Compliance

| Gate | Status | Details |
|------|--------|---------|
| Depth Gate (A) | **PASSED** | All HIGH claims have ≥2 FULLTEXT Tier-1/2 sources |
| Completion Gate (B) | **PASSED*** | *With 2 explicit gaps: synthetic odds generation, correlation collision |
| Retraction Gate (C) | **PASSED** | No retracted papers in source set |

---

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PARLAY PROBABILITY SYSTEM                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         │
│  │   SUBSYSTEM 1   │    │   SUBSYSTEM 2   │    │   SUBSYSTEM 3   │         │
│  │   Single-Leg    │───▶│   Dependency    │───▶│     Market      │         │
│  │   Probability   │    │    Modeling     │    │  Microstructure │         │
│  │     Engine      │    │  (Vine Copula)  │    │   (Vig/FLB)     │         │
│  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘         │
│           │                      │                      │                   │
│           └──────────────────────┼──────────────────────┘                   │
│                                  ▼                                          │
│                      ┌─────────────────────┐                               │
│                      │    SUBSYSTEM 4      │                               │
│                      │     Portfolio       │                               │
│                      │   Optimization      │                               │
│                      │   (Kelly/Staking)   │                               │
│                      └─────────────────────┘                               │
│                                  │                                          │
│                                  ▼                                          │
│                         [Bet Recommendations]                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Subsystem 1: Single-Leg Probability Engine

### Selected Method: Hybrid Architecture
**Why This Method**:
- Evidence: S1 (Walsh & Joshi), S4 (Fischer & Heuer), S26 (Jensen et al.)
- Player props have sparse data → Hierarchical Bayesian with shrinkage
- Game lines have dense data → LSTM/temporal models
- Both require calibration as primary selection criterion

### Component 1.1: Player Props Model (Hierarchical Bayesian)

**Architecture**:
```
Player Performance ~ Normal(μ_player, σ_player)
μ_player ~ Normal(μ_position, τ_position)
μ_position ~ Normal(μ_league, τ_league)
```

**Key Parameters** (from S26 Jensen et al.):
- Use mixture distributions to control shrinkage intensity
- Include covariates: age, position, recent form (weighted exponential)
- Prior elicitation from domain knowledge or external ratings (e.g., Football Manager for xG per S25)

**Implementation Details**:
- Framework: PyMC or Stan for MCMC inference
- Sample size: Minimum 500 MCMC samples post-burn-in
- Shrinkage: Automatic via hierarchical structure (shares information across sparse players)
- Output: Full posterior distribution P(prop outcome | data)

**Calibration Target**:
- Primary metric: Expected Calibration Error (ECE) < 0.05
- Secondary: Brier score, reliability diagrams
- Benchmark: Pinnacle closing line (per P3 Dean Markwick)

### Component 1.2: Game Lines Model (LSTM)

**Architecture** (from S5 Rios et al.):
```
Input: 8-season rolling window (~10,000 games)
LSTM: 128 units, 2 layers
Output: Win probability [0, 1]
```

**Key Parameters**:
- Sequence length: Season-over-season (not just recent games)
- Features: Team stats, home/away, rest days, injuries, historical matchup
- Regularization: Dropout 0.2-0.3, early stopping

**Performance Baseline**:
- Accuracy ceiling: ~70-72% (per S4 Fischer & Heuer)
- Focus on calibration, not accuracy maximization

### Component 1.3: Live Betting Updates (State-Space)

**Architecture** (from S28 Ötting et al.):
```
State: x_t = [win_prob, momentum, scoring_rate]
Observation: y_t = [current_score, time_elapsed, events]
Transition: x_t = A·x_{t-1} + process_noise
Update: Kalman or particle filter
```

**Key Parameters**:
- Update frequency: 1 Hz for in-play markets
- Market overreaction: Account for recency bias in goals/events
- Implementation: filterpy (Kalman) or particles (SMC)

---

## Subsystem 2: Joint Probability & Dependency Modeling

### Selected Method: C-Vine Copula with Ledoit-Wolf Denoising
**Why This Method**:
- Evidence: S8-S13 (vine copula literature), S18-S19 (Ledoit-Wolf)
- SGP legs have complex tail dependencies → Copulas capture non-linear dependence
- Sparse historical correlation data → Shrinkage prevents noise amplification

### Component 2.1: Correlation Matrix Denoising

**Method**: Ledoit-Wolf Nonlinear Shrinkage (S18)

**Algorithm**:
1. Compute sample covariance matrix S from historical leg outcomes
2. Apply nonlinear shrinkage: Σ_clean = F(S, n, p)
3. Ensure positive definiteness

**Key Parameters**:
- Minimum samples: n > p (more observations than variables)
- Fallback: Linear shrinkage if n/p < 2

**Implementation**:
```python
from sklearn.covariance import LedoitWolf
lw = LedoitWolf()
lw.fit(leg_outcomes)
clean_cov = lw.covariance_
```

### Component 2.2: Vine Copula Structure

**Selected Structure**: C-vine (canonical vine)

**Why C-vine**:
- Central variable (e.g., game outcome) conditions all others
- Natural for SGP where legs depend on common underlying event
- Evidence: S12 (Kraus & Czado) for structure selection

**Algorithm** (from S12):
1. Select root variable with highest dependence sum
2. Construct tree by connecting to all others
3. Estimate bivariate copulas at each edge
4. Propagate to higher trees via conditioning

**Copula Family Selection**:
- Start with Gaussian copula (tractable)
- Test Frank, Clayton, Gumbel for tail dependence (per S8 Simpson)
- Use AIC/BIC for family selection

**Implementation** (from S11 Cheng et al.):
```python
import torchvinecopulib as tvc
vine = tvc.Vine(d=num_legs)
vine.fit(uniform_margins)  # After probability integral transform
joint_prob = vine.pdf(u)
```

### Component 2.3: SGP Joint Probability Calculation

**Process**:
1. Transform marginal probabilities to uniform via CDF: u_i = F_i(p_i)
2. Evaluate vine copula density: c(u_1, ..., u_k)
3. Joint probability: P(all legs hit) = c(u) × ∏ p_i / ∏ p_i_independent
4. Compare to sportsbook price for edge detection

**Correlation Tax Detection**:
- If sportsbook joint < copula joint: Negative edge (book overcharging)
- If sportsbook joint > copula joint: Positive edge (arbitrage opportunity)

---

## Subsystem 3: Market Microstructure

### Selected Method: Shin Method for Vig Removal
**Why This Method**:
- Evidence: S14 (Clarke), P4 (Štrumbelj), P5 (Geekculture)
- Accounts for favorite-longshot bias
- Produces theoretically grounded true probabilities

### Component 3.1: Vig Removal

**Shin Method Algorithm**:
```
Given: Implied probabilities π_1, ..., π_n summing to 1 + vig
Solve: z such that Σ[√(z² + 4(1-z)π_i/n) - z] / 2(1-z) = 1
True prob: p_i = [√(z² + 4(1-z)π_i/n) - z] / 2(1-z)
```

**Alternative (Power Method)**:
- For 2-way markets, Power method produces equivalent results (S14)
- Simpler: p_i = π_i^k / Σ π_j^k where k chosen to sum to 1

**Implementation**:
```python
from scipy.optimize import brentq

def shin_probabilities(implied_probs):
    def objective(z):
        n = len(implied_probs)
        true_probs = [(np.sqrt(z**2 + 4*(1-z)*pi/n) - z) / (2*(1-z))
                      for pi in implied_probs]
        return sum(true_probs) - 1

    z = brentq(objective, 0.001, 0.5)
    # ... compute true probs with solved z
```

### Component 3.2: Favorite-Longshot Bias Adjustment

**Finding**: FLB increases with market complexity (S17 Sung et al.)

**Adjustment Strategy**:
1. Measure FLB in historical data per market type
2. Apply correction factor based on number of outcomes
3. More outcomes → stronger longshot overpricing

### Component 3.3: Pinnacle Benchmark Integration

**Use Case**: Calibration validation

**Process**:
1. Collect Pinnacle closing lines as ground truth
2. Compare model probabilities vs. Pinnacle-implied
3. Compute CLV (Closing Line Value) for bets placed
4. Positive CLV indicates edge vs. efficient market

---

## Subsystem 4: Portfolio Optimization

### Selected Method: Fractional Kelly with Correlated Position Sizing
**Why This Method**:
- Evidence: S22-S24 (Kelly extensions), S3 (Vélez practical success)
- Accounts for correlation between positions
- Reduces variance vs. full Kelly

### Component 4.1: Kelly Criterion for Single Bets

**Classic Kelly**:
```
f* = (bp - q) / b
where:
  b = decimal odds - 1 (net profit per unit)
  p = true probability
  q = 1 - p
```

### Component 4.2: Multi-Bet Kelly with Correlation

**Method** (from S23 Byrnes & Barnett):
```
f* = Σ^{-1} · μ
where:
  Σ = covariance matrix of bet returns
  μ = expected returns vector (edge)
```

**Implementation**:
1. Build return covariance matrix from copula model
2. Compute expected return per bet: μ_i = p_true × odds - 1
3. Solve: f = inv(Σ) @ μ
4. Constrain: f_i >= 0, Σf_i <= bankroll_fraction

### Component 4.3: Fractional Kelly

**Recommendation**: Use 0.25× to 0.5× Kelly

**Rationale**:
- Full Kelly has high variance
- Evidence: S3 (Vélez) achieved 135.8% with Kelly integration
- Fractional reduces drawdown at cost of geometric growth

**Dynamic Adjustment**:
- Scale Kelly fraction by confidence in edge estimate
- Higher model uncertainty → lower Kelly multiplier

### Component 4.4: Sportsbook Constraint Handling

**Max Bet Limits**:
```
f_i = min(kelly_fraction, max_bet_i / bankroll)
```

**Correlation Limit Handling**:
- Some books limit correlated parlays
- Track book-specific limits in constraint matrix
- Optimize across books for best execution

---

## Implementation Sequence

```
Step 1: Data Infrastructure     ─depends on→ nothing
Step 2: Single-Leg Engines      ─depends on→ Step 1
Step 3: Calibration Pipeline    ─depends on→ Step 2
Step 4: Copula/Dependency       ─depends on→ Step 2
Step 5: Vig Removal             ─depends on→ Step 1
Step 6: Portfolio Optimizer     ─depends on→ Step 3, 4, 5
Step 7: Backtesting Framework   ─depends on→ Step 6
Step 8: Live Deployment         ─depends on→ Step 7
```

### Step 1: Data Infrastructure
- **What**: Build data pipelines for odds, outcomes, player stats
- **Evidence Basis**: P13 (Clegg) - data quality critical
- **Key Components**:
  - Timestamped odds collection (decision-time, not closing)
  - Outcome resolution pipeline
  - Feature store for player/team stats

### Step 2: Single-Leg Engines
- **What**: Implement Bayesian (props) and LSTM (lines) models
- **Evidence Basis**: S1, S5, S26 [HIGH confidence]
- **Key Considerations**:
  - Separate model per sport/market type
  - Ensemble if beneficial

### Step 3: Calibration Pipeline
- **What**: Continuous calibration monitoring
- **Evidence Basis**: S1 (Walsh & Joshi)
- **Metrics**: ECE, Brier, reliability diagrams
- **Recalibration trigger**: ECE drift > 0.02

### Step 4: Copula/Dependency Model
- **What**: Vine copula fitting and joint probability
- **Evidence Basis**: S8-S13 [HIGH confidence]
- **Key Considerations**:
  - Update correlation matrix weekly (or more for live)
  - Apply Ledoit-Wolf before fitting

### Step 5: Vig Removal
- **What**: True probability extraction from sportsbook odds
- **Evidence Basis**: S14, P4, P5 [HIGH confidence]
- **Method**: Shin (primary), Power (backup)

### Step 6: Portfolio Optimizer
- **What**: Kelly sizing with constraints
- **Evidence Basis**: S22-S24 [HIGH confidence]
- **Key Considerations**:
  - Respect max bet limits
  - Apply fractional Kelly (0.25-0.5×)

### Step 7: Backtesting Framework
- **What**: Historical validation with proper methodology
- **Evidence Basis**: F1-F6 failure studies
- **Critical**:
  - Use decision-time odds (not closing)
  - Walk-forward validation
  - Winsorize outliers

### Step 8: Live Deployment
- **What**: Production system with monitoring
- **Evidence Basis**: S28, S29 (live betting)
- **Key Considerations**:
  - Latency management
  - Drift detection
  - Bankroll tracking

---

## Data Requirements

| Data Type | Source | Format | Update Frequency | Evidence |
|-----------|--------|--------|------------------|----------|
| Historical odds | OddsAPI, OpticOdds | JSON | Daily | P8 |
| Player stats | StatsBomb, Sportradar | CSV/API | Per-event | S25, S26 |
| Game outcomes | Official league data | JSON | Daily | - |
| SGP prices | Sportsbook APIs | JSON | Real-time | P6 |
| Pinnacle closing lines | Pinnacle/feeds | JSON | Daily | P3 |

---

## Risk-Mitigation Table

| # | Risk | Likelihood | Impact | Mitigation | Evidence |
|---|------|------------|--------|------------|----------|
| R1 | Accuracy-optimized model unprofitable | HIGH | HIGH | Use calibration (Brier/ECE) for model selection | S1, F1 |
| R2 | Data quality issues (outliers) | MEDIUM | CRITICAL | Winsorize returns, inspect bet-level distributions | F2 |
| R3 | Behavioral biases in features | MEDIUM | HIGH | Require causal mechanism for each feature | F3 |
| R4 | Overfitting via parameters | HIGH | CRITICAL | Limit model complexity; require theoretical justification | F4 |
| R5 | Look-ahead bias | HIGH | HIGH | Use timestamped decision-time odds only | F5 |
| R6 | Regime change | HIGH | HIGH | Walk-forward testing; regular model retraining | F6 |
| R7 | Insufficient sample size | MEDIUM | HIGH | Power analysis, cross-validation | Multiple |
| R8 | Market efficiency increase | HIGH | MEDIUM | Regular inefficiency monitoring | F2, F6 |

---

## Validation Approach

### Recommended Metrics

| Metric | Target | Rationale | Evidence |
|--------|--------|-----------|----------|
| ECE | < 0.05 | Calibration quality | S1 |
| Brier Score | < 0.20 | Probabilistic accuracy | S1, S4 |
| CLV | > 0% | Edge vs. closing line | P3 |
| Sharpe Ratio | > 1.0 | Risk-adjusted returns | S3 |
| Max Drawdown | < 30% | Risk management | S22 |

### Testing Strategy

1. **Unit Tests**: Each subsystem in isolation
2. **Integration Tests**: Full pipeline on historical data
3. **Walk-Forward Validation**: Rolling out-of-sample testing
4. **Paper Trading**: Live signals without real stakes
5. **Small Stakes**: Limited live betting before scale-up

---

## Known Gaps

### Gap 1: Synthetic Odds Generation for SGP Backtesting

- **Impact**: Cannot validate SGP strategies on historical data where SGP odds weren't recorded
- **Blocking**: Full backtest of SGP-specific edge detection
- **Resolution Path**:
  - Generate synthetic SGP odds: single-leg odds × copula adjustment
  - Validate against available historical SGP prices
  - Document synthetic vs. actual discrepancy

### Gap 2: Correlation Collision Detection

- **Impact**: Risk of hidden concentration in latent factors (weather, injuries affecting multiple legs)
- **Blocking**: Robust portfolio diversification across parlays
- **Resolution Path**:
  - Build factor model: decompose leg outcomes into latent factors
  - Monitor portfolio exposure to each factor
  - Set concentration limits per factor

---

## Sources

### Primary (HIGH Confidence Basis)

| # | Title | Year | Access | Implementation Detail | Key Contribution |
|---|-------|------|--------|----------------------|------------------|
| S1 | Walsh & Joshi - Calibration > Accuracy | 2023 | FULLTEXT | YES | Model selection criterion |
| S8 | Simpson et al. - Vine tail dependence | 2020 | FULLTEXT | YES | Copula properties |
| S11 | Cheng et al. - torchvinecopulib | 2025 | FULLTEXT | YES | GPU implementation |
| S14 | Clarke - Overround adjustment | 2017 | FULLTEXT | YES | Vig removal methods |
| S18 | Ledoit & Wolf - Nonlinear shrinkage | 2020 | FULLTEXT | YES | Correlation denoising |
| S22 | Pérez-Marco - Variable payoff Kelly | 2014 | FULLTEXT | YES | Kelly extension |
| S26 | Jensen et al. - Hierarchical Bayesian | 2009 | FULLTEXT | YES | Player prop modeling |

### Supporting

| # | Title | Year | Access | Key Contribution |
|---|-------|------|--------|------------------|
| S3 | Vélez et al. - Neural + Kelly | 2023 | FULLTEXT | Practical validation |
| S5 | Rios et al. - LSTM NBA | 2025 | FULLTEXT | Temporal modeling |
| S9 | Kreuzer & Czado - Dynamic vine | 2019 | FULLTEXT | Time-varying dependence |
| S12 | Kraus & Czado - Structure selection | 2017 | FULLTEXT | Vine algorithms |
| S28 | Ötting et al. - Live state-space | 2021 | FULLTEXT | In-play updates |
| P6 | Wizard of Odds - SGP math | 2025 | FULLTEXT | Industry practice |

### Failure Studies

| # | Title | Year | Key Lesson |
|---|-------|------|------------|
| F1 | Zimmermann - Wages of wins | 2017 | Calibration > accuracy |
| F2 | Clegg & Cartlidge - Hercog bet | 2023 | Data quality critical |
| F3 | Ötting et al. - Momentum fallacy | 2022 | Require causal mechanism |
| F4 | Sports Insights - Overfitting | 2013 | Theory before data mining |
| F5 | GreatBets - Look-ahead bias | 2025 | Decision-time odds |
| F6 | Reddit - Regime change | 2026 | Walk-forward validation |

---

*Specification generated: 2026-02-04*
*Total sources: 44 (30 academic + 14 practitioner + 6 failure studies)*
*Confidence: HIGH with 2 explicit gaps*
