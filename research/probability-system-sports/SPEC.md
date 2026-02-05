# Research Specification: Production-Grade Parlay Probability System

## Goal
Design a modular sports betting probability system capable of generating calibrated single-leg probabilities, modeling complex dependencies for Same Game Parlays (SGPs), and optimizing portfolio construction under sportsbook constraints.

## Success Criteria
- [ ] Leg Models: Specific model classes identified for Props (Player) vs. Game (Spread/Total) that outperform baseline Poisson/Logit.
- [ ] Calibration: Validation method defined (e.g., ECE, Brier) ensuring $p_{pred} \approx p_{actual}$.
- [ ] Dependency Engine: Mathematical method selected for joint probabilities (e.g., Copulas vs. Simulation) that handles tail dependence.
- [ ] Pricing Logic: "Vig removal" algorithm selected that accounts for favorite-longshot bias (e.g., Shin's method).
- [ ] Optimization: Staking strategy defined that balances Expected Growth (Kelly) against Variance/Drawdown.
- [ ] Architecture: High-level data flow map from "Live Odds Feed" to "Execution."

## Research Units
1. **Single-Leg Probability Engines**: Identify SOTA methods for estimating $P(Win)$ for sparse data (Player Props) and dense data (Spreads/Totals). Focus on Hierarchical Bayesian models and State-Space/Particle Filters for in-game updates.
2. **Joint Probability & Dependency Modeling**: Determine the best implementation for connecting correlated legs (SGPs). Specifically evaluate Vine Copulas, Gaussian Copulas, and Monte Carlo simulation based on "Physics of the Game" (play-by-play).
3. **Market Microstructure & True Price Extraction**: Define methods to reverse-engineer "True Probability" from Sportsbook Odds. Must cover multi-way markets and advanced vig removal (Shin's method, Power method).
4. **Portfolio Optimization & Staking**: Define the selection algorithm. How to select the "best" parlay from millions of combinations using Integer Programming or Heuristic Search (Beam Search) subject to Kelly Criterion constraints.

## Deliverable
SPECIFICATION

## Context
- **Use case**: Algorithmic sports trading firm automating parlay/SGP construction.
- **Constraints**: Must handle real-world sportsbook limits, "correlated parlay" rejections, and varying hold percentages. Latency must be suitable for pre-game (low urgency) and live (high urgency).
- **Expertise**: Principal Quantitative Researcher & Systems Architect (strong in math/stats, Python, and data engineering).
- **Existing work**: Standard independence models ($P(A) \times P(B)$) are known to fail. Basic Poisson models for scores are insufficient for player props.

## Prior Art Hints
- Dependency: "Vine Copulas in Finance/Risk Management" (applied to sports).
- Vig Removal: "Shin's Method" (Shin, 1991/1993), "The Favorite-Longshot Bias."
- Calibration: "Platt Scaling," "Isotonic Regression," "Temperature Scaling."
- Conferences: MIT Sloan Sports Analytics Conference (SSAC) papers, arXiv Quantitative Finance (q-fin).
- Optimization: "Fractional Kelly Criterion," "Markowitz Portfolio Theory applied to betting."

## Constraints
- Time period: Last 10 years (Critical: Include foundational 90s papers on vig/market efficiency).
- Evidence types: Peer-reviewed journals (J. Quant Analysis in Sports), PhD Theses, and high-quality industry technical blogs.
- Excluded: "Touting" sites, non-technical journalism, unverified "system sellers."

## Key Search Terms
- "Sports betting calibration Brier score"
- "Same game parlay correlation modeling copulas"
- "Implied probability vig removal Shin's method"
- "Bayesian hierarchical models sports player props"
- "Portfolio optimization sports betting Kelly criterion"

## Recency Policy
scientific
