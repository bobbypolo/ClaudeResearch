# Explicit Gap Declarations

Two gaps identified during research that could not be resolved to HIGH confidence.

---

## Gap 1: Synthetic Odds Generation for SGP Backtesting

### Description
No academic or practitioner sources describe methodology for generating historical Same Game Parlay (SGP) odds where such odds were not recorded by sportsbooks.

### Claim Affected
"Historical SGP backtesting is possible with full fidelity"

### Current Confidence
**LOW** - No sources found

### Reason for Gap
- SGP products are relatively new (post-2018 widespread adoption)
- Historical SGP odds not systematically archived
- No academic papers address synthetic reconstruction
- Practitioner sources describe current pricing, not historical reconstruction

### Impact
- Cannot validate SGP-specific edge detection strategies on historical data
- Limited to forward-testing for SGP strategies
- Backtesting must rely on synthetic approximations

### Blocking
- Full confidence in SGP strategy profitability
- Historical performance attribution
- Strategy optimization on historical data

### Resolution Path

**Approach 1: Copula-Based Synthesis**
1. Collect historical single-leg odds for all SGP components
2. Apply calibrated vine copula to model dependencies
3. Generate synthetic joint probability: P(SGP) = copula_joint × ∏margins
4. Convert to synthetic odds with estimated vig markup

**Approach 2: Limited Historical Validation**
1. Collect available historical SGP prices (post-2020)
2. Compare synthetic vs. actual where overlap exists
3. Quantify synthetic-actual discrepancy
4. Use discrepancy as confidence interval on backtest results

**Validation Required**
- Compare synthetic SGP prices to actual recorded prices (where available)
- Document discrepancy distribution
- Apply discrepancy as systematic error in backtest interpretation

---

## Gap 2: Correlation Collision Detection

### Description
No sources address monitoring portfolio-level exposure to latent factors across multiple parlays.

### Claim Affected
"Portfolio latent factor exposure can be systematically monitored and managed"

### Current Confidence
**LOW** - No sports-specific sources

### Reason for Gap
- Financial factor models (e.g., Fama-French) not directly applicable to sports
- Sports betting literature focuses on individual bet edge, not portfolio risk
- No academic work on factor decomposition for betting portfolios

### Impact
- Risk of hidden concentration in latent factors
- Example: Multiple parlays all exposed to "Chiefs QB health" factor
- Correlated drawdowns if latent factor realizes negatively

### Blocking
- Robust portfolio diversification
- Concentration risk management
- True portfolio risk assessment

### Resolution Path

**Approach 1: PCA Factor Extraction**
1. Build matrix of historical leg outcomes (legs × events)
2. Apply PCA to extract principal components
3. Interpret components as latent factors (weather, injuries, etc.)
4. Monitor portfolio loading on each factor

**Approach 2: Named Factor Model**
1. Define explicit factors: team form, player health, weather, etc.
2. Estimate factor loadings for each leg type
3. Aggregate portfolio exposure to each factor
4. Set concentration limits (e.g., max 20% exposure to single factor)

**Relevant Literature for Adaptation**
- S20: Bouchaud & Potters (2009) - RMT for factor extraction
- S21: Yang et al. (2015) - Robust covariance for heavy tails
- Financial factor model literature (Fama-French, Carhart)

**Validation Required**
- Build factor model on historical data
- Test whether factor exposure predicts correlated losses
- Establish concentration limits empirically

---

## Gap Status Summary

| Gap | Severity | Workaround Available | Resolution Complexity |
|-----|----------|---------------------|----------------------|
| Synthetic SGP Odds | HIGH | Copula-based synthesis | MEDIUM |
| Correlation Collision | MEDIUM | PCA/named factors | HIGH |

Both gaps have viable resolution paths using established techniques from adjacent domains. Implementation can proceed while addressing these gaps in parallel.

---

*Gaps documented: 2026-02-04*
