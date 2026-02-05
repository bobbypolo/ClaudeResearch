# Research Plan: probability-system-sports

## Goal Understanding

Design and specify the implementation architecture for a **production-grade parlay probability system** that:
1. Generates calibrated win probabilities for individual bet legs (player props, spreads, totals)
2. Models complex statistical dependencies between legs for Same Game Parlay (SGP) pricing
3. Constructs optimal betting portfolios under real-world sportsbook constraints

This is an **implementation specification** task—we need to identify specific methods, parameters, and architectural patterns, not assess feasibility.

## Success Criteria

- [ ] **Unit 1 (Leg Models)**: Identify 2-3 specific model architectures for player props (sparse data) and game lines (dense data), with evidence of superior calibration vs. baseline Poisson/Logit
- [ ] **Unit 2 (Dependencies)**: Select a joint probability method (Copulas vs. Simulation) with evidence on handling tail dependence and SGP correlation structures; **include correlation matrix denoising method (shrinkage/factor models)**
- [ ] **Unit 3 (Pricing)**: Define vig removal algorithm with handling for favorite-longshot bias—specific implementation (Shin's method, Power method, or hybrid); **define synthetic odds generation pipeline for backtesting**
- [ ] **Unit 4 (Portfolio)**: Specify staking/selection algorithm that balances Kelly growth against variance constraints; **include correlation collision checking mechanism**
- [ ] **Architecture**: Data flow specification from odds ingestion → probability estimation → dependency modeling → optimization → execution

## Research Strategy

### Unit 1: Single-Leg Probability Engines

**Question**: Which model architectures produce the best-calibrated probabilities for (a) player props with sparse data and (b) game lines with dense historical data?

**Search Strategy**:
- Primary: "hierarchical Bayesian sports betting" "player prop prediction model" "sports spread prediction machine learning"
- Secondary: "state space model sports" "particle filter live betting" "Poisson regression sports total"
- Failure: "sports prediction model overfitting" "calibration failure betting" "Brier score sports"
- Domain-specific: "Journal of Quantitative Analysis in Sports" "MIT Sloan Sports Analytics"

**Expected Sources**:
- Academic: JQAS papers, Statistics in Sports, PhD theses on sports modeling
- Practitioner: Pinnacle blog, high-quality quant sports blogs
- Foundational: Bradley-Terry, Elo extensions, Poisson football models

**Success Indicator**:
- HIGH confidence requires 3+ peer-reviewed sources agreeing on model class
- Implementation detail required: specific prior distributions, feature engineering approaches, calibration methods

### Unit 2: Joint Probability & Dependency Modeling

**Question**: How do we implement a dependency engine for SGPs that correctly captures correlation between legs (e.g., player scoring + team winning)?

**Search Strategy**:
- Primary: "copula sports betting" "vine copula correlation" "same game parlay modeling"
- Secondary: "Gaussian copula tail dependence" "Monte Carlo simulation correlated events" "multivariate sports outcomes" "covariance shrinkage sports betting" "estimating correlation matrices sparse data" "Ledoit-Wolf estimator finance application"
- Failure: "copula model failure" "correlation estimation error sports" "dependence structure misspecification"
- Cross-domain: "copula risk management" "vine copula finance" (transfer learning from quant finance)

**Expected Sources**:
- Academic: Copula textbooks (Nelsen, Joe), finance applications (Embrechts), sports-specific adaptations
- Technical: R/Python copula package documentation with mathematical backing
- Foundational: Sklar's theorem papers, Joe (1997) on multivariate dependence

**Success Indicator**:
- HIGH confidence requires evidence comparing Gaussian vs. Vine copulas on sports data
- Implementation detail required: copula family selection criteria, parameter estimation methods, simulation algorithms
- **Must identify methods for "denoising" correlation matrices (shrinkage or factor models) before feeding them into the Copula**

### Unit 3: Market Microstructure & True Price Extraction

**Question**: How do we extract true probabilities from bookmaker odds, accounting for vig structure and favorite-longshot bias? **And how do we generate synthetic historical odds for backtesting when historical SGP pricing data is unavailable?**

**Search Strategy**:
- Primary: "Shin's method implied probability" "vig removal sports betting" "favorite longshot bias"
- Secondary: "power method odds conversion" "additive method bookmaker margin" "efficient market betting"
- Synthetic Odds: "generative backtesting sports betting" "simulating sportsbook pricing models" "synthetic odds generation" "bookmaker margin simulation"
- Failure: "vig estimation error" "implied probability bias" "odds conversion pitfalls"
- Foundational: Shin (1991, 1993), Snowberg & Wolfers (2010)

**Expected Sources**:
- Academic: Journal of Prediction Markets, Economica, Journal of Financial Economics (betting market papers)
- Foundational: Shin's original papers, Jullien & Salanié (2000)
- Practitioner: Technical writeups comparing vig removal methods

**Success Indicator**:
- HIGH confidence requires comparison study of vig removal methods
- Implementation detail required: exact formulas, handling of multi-way markets, computational approaches
- **Must define synthetic odds generation pipeline**: how to use the pricing engine to simulate what a sportsbook would have charged historically for SGPs (the only viable backtesting strategy)

### Unit 4: Portfolio Optimization & Staking

**Question**: How do we select optimal parlays from combinatorial space and size positions under bankroll constraints?

**Search Strategy**:
- Primary: "Kelly criterion sports betting" "portfolio optimization betting" "parlay selection algorithm"
- Secondary: "fractional Kelly variance" "integer programming bet selection" "multi-armed bandit betting"
- Failure: "Kelly criterion failure" "over-betting ruin" "variance drag betting"
- Cross-domain: "Markowitz portfolio sports" "risk parity betting"

**Expected Sources**:
- Academic: Kelly (1956) original, Thorp papers, MacLean et al. on Kelly variants
- Technical: Operations research papers on combinatorial optimization
- Practitioner: Quantitative trader blogs on bet sizing

**Success Indicator**:
- HIGH confidence requires evidence on fractional Kelly parameters
- Implementation detail required: constraint formulation, search algorithms for parlay space
- **Must include mechanism for correlation collision checking**: preventing exposure to the same underlying latent factor across multiple different parlays (e.g., two parlays both dependent on "Team A wins by large margin")

## Anticipated Sub-Domains

1. **Live/In-Play Updates**: State-space models, particle filters for real-time probability updates
2. **Calibration Techniques**: Platt scaling, isotonic regression, temperature scaling for probability calibration
3. **Computational Efficiency**: Handling millions of parlay combinations efficiently
4. **Sportsbook Constraints**: Correlation rejection rules, stake limits, line movement
5. **SGP Backtesting Paradox** (CRITICAL): Historical SGP odds do not exist in bulk—you cannot download "FanDuel SGP odds from 2023." Synthetic odds generation using the pricing engine is the **only viable backtesting strategy**. Without solving this, the implementation cannot be validated.

## Key Search Terms

| Concept | Primary Terms | Variants |
|---------|---------------|----------|
| Single-leg models | hierarchical Bayesian sports, player prop model | Bradley-Terry, Elo, state-space sports |
| Dependency | copula sports, vine copula correlation | SGP correlation, joint distribution betting |
| Correlation denoising | Ledoit-Wolf shrinkage, covariance estimation sparse | factor model correlation, random matrix theory |
| Vig removal | Shin's method, implied probability | favorite-longshot bias, margin removal |
| Synthetic backtesting | synthetic odds generation, simulated pricing | generative backtesting, bookmaker margin simulation |
| Staking | Kelly criterion betting, portfolio optimization | fractional Kelly, bankroll management |
| Correlation collision | portfolio latent factor exposure, bet correlation | overlapping risk factors, redundant bets |
| Calibration | Brier score calibration, reliability diagram | ECE, isotonic regression |
| Architecture | sports betting system design | real-time odds, data pipeline betting |

## Discovery Passes (Thorough Preset)

| Pass | Purpose | Target Sources |
|------|---------|----------------|
| **Academic** | Peer-reviewed foundations | 60% |
| **Practitioner** | Implementation case studies | 25% |
| **Failure Analysis** | What went wrong, risk-mitigation | 10% |
| **Snowball** | Citation expansion from key papers | +10 sources |

## Estimated Scope

- **Research units**: 4
- **Min sources per unit**: 5 (thorough preset)
- **Total expected sources**: 25-35
- **Extraction depth**: Deep (full 12-field extraction)
- **Failure analysis**: Required for Completion Gate
- **Recency policy**: Scientific (5 years) with foundational exception for seminal papers (Shin, Kelly, Sklar)

## Risk Assessment

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Sparse academic literature on SGP specifically | Medium | Cross-domain transfer from copula/finance literature |
| Proprietary methods not published | Medium | Focus on foundational theory + practitioner adaptations |
| Conflicting calibration recommendations | Low | Use comparative studies where available |
| **SGP Backtesting Paradox** | HIGH | Research synthetic odds generation as first-class requirement; system untestable without this |
| Correlation matrix estimation with sparse data | Medium | Research shrinkage estimators (Ledoit-Wolf) and factor models for denoising |
| Hidden latent factor correlation across parlays | Medium | Research portfolio correlation collision detection methods |

## Approval Checkpoint

- [ ] User approves plan before proceeding to Phase 1: Parse

---

*Plan generated: 2026-02-04*
*Preset: thorough*
*Estimated discovery phases: Academic → Practitioner → Failure Analysis → Snowball*
