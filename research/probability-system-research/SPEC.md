# Research Specification: Parlay-Capable Sports Probability System

## Research Question
Is it feasible to build a production-grade probability system that can:
1) produce calibrated true probabilities (p_true) for single legs,
2) estimate joint probabilities (p_joint) for parlays (including SGPs) under dependence,
3) identify +EV parlay combinations versus sportsbook pricing,
and validate this advantage out-of-sample against market baselines (closing line / implied probabilities)?

## Research Units
1. Feasibility: Are parlays beatable vs singles in practice?
   - Under what conditions (market type, promos, mispriced correlation, niche props)?
2. Single-leg probability engine (p_true)
   - Best validated methods for spreads/totals/props/live markets
   - Calibration and uncertainty quantification
3. Joint probability & dependence modeling (p_joint) for parlays/SGPs
   - Simulation vs copulas vs multivariate Bayesian/GLMM vs scenario/game-script mixtures
   - Validation methods for joint models
4. Sportsbook pricing reality & EV translation
   - Vig/hold modeling by market type
   - SGP correlation pricing (as publicly documented)
   - Promo/boost EV and rules constraints (voids, payout caps, restrictions)
5. Parlay construction as optimization
   - Algorithms to select leg combinations under constraints
   - Uncertainty-aware selection (avoid “edge stacking”)
   - Staking for correlated bets (Kelly variants, risk constraints)
6. Backtesting & monitoring
   - Walk-forward, leakage controls, time alignment to line availability
   - Calibration drift + CLV tracking + robustness tests
7. System architecture blueprint
   - End-to-end stack: data → features → models → calibration → pricing/EV → optimizer → monitoring

## Deliverables
- REPORT: Structured findings by research unit, each including:
  - Summary of best-supported methods
  - What evidence shows works / doesn’t work
  - Data requirements and implementation implications
- VERDICT: Recommendation with confidence level:
  - Feasibility verdict (not feasible / feasible only under narrow conditions / feasible with strong system)
  - Minimum viable architecture + validation plan

## Constraints
- Time period:
  - Foundational modeling theory: no strict limit (include seminal/high-citation work)
  - Sportsbook pricing / SGP mechanics / promos: prefer last 5 years
  - Engineering/stack best practices: prefer last 3 years
- Evidence types:
  - Primary: peer-reviewed journals, PhD theses/dissertations, top conference proceedings
  - Secondary: reputable preprints (clearly labeled)
  - Tertiary: patents/technical filings for pricing mechanics (if relevant), practitioner reports (clearly labeled)
  - Exclude: forums/tipster content as evidence
- Minimum sources:
  - ≥ 6 high-quality sources per research unit (peer-reviewed/thesis/proceedings preferred)
  - Total ≥ 30 core sources across the project

## User Context
We are building a parlay-capable betting system that must be probability-driven (calibrated p_true),
dependence-aware (p_joint not naive multiplication), sportsbook-price-aware (vig/SGP pricing/promos),
and validated out-of-sample with strict anti-leakage controls.
We need an implementable blueprint, not a conceptual survey.

## Key Search Terms
- "sports betting calibration log loss Brier score"
- "closing line value CLV evaluation sports prediction"
- "same game parlay correlation pricing"
- "copula model player props joint probability"
- "hierarchical bayesian player projection sparse data"
- "state space model win probability in-game"
- "possession-based simulation NBA points distribution"
- "play-by-play simulation NFL prop outcomes"
- "vig removal prop markets hold estimation"
- "correlated Kelly criterion portfolio betting"
- "walk-forward optimization sports betting leakage"
- "parlay expected value dependence model"

## Quality Gates (must follow)
1. Evidence grading: label every key claim as peer-reviewed / thesis / proceedings / preprint / patent / practitioner / journalism.
2. Paper extraction template (for every core source):
   - data provenance + years + sample size
   - target definition + market type
   - model class
   - validation protocol + leakage controls
   - metrics (must include log loss or Brier) + calibration evidence
   - baseline vs market odds/closing line when available
   - limitations + reproducibility
3. Market baseline requirement: assess lift vs implied odds/closing line, not accuracy alone.
4. Contradiction handling: when sources disagree, explain why and prefer replicated + out-of-sample evidence.
5. Boundary: do not include illegal or deceptive methods; keep focus on modeling/engineering/validation.
