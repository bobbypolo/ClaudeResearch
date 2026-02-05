# Academic Discovery Pass

## Unit 1: Single-Leg Probability Engines

### Key Sources Found

**S1: Walsh & Joshi (2023) - "Machine learning for sports betting: should model selection be based on accuracy or calibration?"**
- arXiv: 2303.06021
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Calibration is more important than accuracy for sports betting. Using calibration for model selection led to ROI of +34.69% vs -35.17% for accuracy-based selection.
- Relevance: Critical for Unit 1 - establishes that ECE/Brier score should be primary model selection criterion, not accuracy.

**S2: Galekwa et al. (2024) - "A Systematic Review of Machine Learning in Sports Betting"**
- arXiv: 2410.21484
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Comprehensive review of ML techniques (SVM, RF, neural networks) across sports. Highlights challenges with data quality, real-time decision-making, and outcome unpredictability.
- Relevance: Survey providing method comparison for Unit 1.

**S3: Vélez et al. (2023) - "Sports Betting: Neural Networks and Modern Portfolio Theory"**
- arXiv: 2307.13807
- Type: ACADEMIC, Tier 2 (q-fin.PM)
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Integrates deep learning with Kelly Criterion. Achieved 135.8% returns in EPL 20/21 season. Combines Von Neumann-Morgenstern utility with neural forecasts.
- Relevance: Unit 1 (neural network models) + Unit 4 (Kelly integration).

**S4: Fischer & Heuer (2024) - "Match predictions in soccer: Machine learning vs. Poisson approaches"**
- arXiv: 2408.08331
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Both ML and Poisson models achieve similar prediction quality (~70% accuracy ceiling). Choice of features and model has minor influence on prediction quality.
- Relevance: Unit 1 - suggests Poisson baseline is competitive; focus should be on calibration not architecture.

**S5: Rios et al. (2025) - "Long-Sequence LSTM Modeling for NBA Game Outcome Prediction"**
- arXiv: 2512.08591
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: LSTM with 9,840 game sequence (8 seasons) achieves 72.35% accuracy, 76.13% AUC-ROC. Captures season-over-season dependencies.
- Relevance: Unit 1 - demonstrates temporal modeling for dense data (game lines).

**S6: Yang & Swartz (2021) - "A Two-Stage Bayesian Model for Predicting Winners in MLB"**
- DOI: 10.6339/jds.2004.02(1).142
- Type: ACADEMIC, Tier 1
- Access: FULLTEXT (diamond OA)
- Implementation Detail: YES
- Key Finding: Hierarchical Bayesian model combining team performance, batting ability, and pitchers with contribution parameters. Uses MCMC for inference.
- Relevance: Unit 1 - Bayesian hierarchical structure for sparse player-level data.

**S7: Mead et al. (2023) - "Expected Goals in Football: Improving Model Performance"**
- DOI: 10.1371/journal.pone.0282295
- Type: ACADEMIC, Tier 1 (PLoS ONE)
- Access: FULLTEXT (gold OA)
- Implementation Detail: YES
- Key Finding: xG model incorporating player/team features improves calibration. Demonstrates feature engineering for scoring probability.
- Relevance: Unit 1 - calibrated probability models for player props.

---

## Unit 2: Joint Probability & Dependency Modeling

### Key Sources Found

**S8: Simpson et al. (2020) - "A geometric investigation into the tail dependence of vine copulas"**
- arXiv: 2012.09623
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Establishes tail dependence properties of vine copula classes. Trivariate vines from asymptotically dependent/independent copulas. Logistic and inverted logistic examples.
- Relevance: Unit 2 - critical for understanding SGP tail dependence.

**S9: Kreuzer & Czado (2019) - "Bayesian inference for dynamic vine copulas in higher dimensions"**
- arXiv: 1911.00702
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Time-varying vine copulas with latent AR(1) processes driving parameters. Bayesian MCMC estimation. Tested on 21 exchange rates.
- Relevance: Unit 2 - dynamic dependence modeling for time-varying correlations.

**S10: Lopez-Paz et al. (2013) - "Gaussian Process Vine Copulas for Multivariate Dependence"**
- arXiv: 1302.3979
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Relaxes simplifying assumption by learning latent functions for conditional copulas. Uses sparse Gaussian processes with expectation propagation.
- Relevance: Unit 2 - non-simplified vine copulas for complex SGP dependencies.

**S11: Cheng et al. (2025) - "Vine Copulas as Differentiable Computational Graphs"**
- arXiv: 2506.13318
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: torchvinecopulib library - GPU-accelerated, PyTorch-based. New algorithms for conditional sampling, efficient scheduling. Integrates with deep learning pipelines.
- Relevance: Unit 2 - modern implementation framework for vine copulas.

**S12: Kraus & Czado (2017) - "Growing simplified vine copula trees: improving Dißmann's algorithm"**
- arXiv: 1703.05203
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Algorithms for structure selection focused on minimizing simplifying assumption violation. Outperforms Dißmann's algorithm by large margin.
- Relevance: Unit 2 - vine structure selection for SGP correlation.

**S13: Torre et al. (2017) - "A general framework for data-driven uncertainty quantification using vine copulas"**
- arXiv: 1709.08626
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Automated, data-driven inference of vine copula input models. Application to structural reliability with non-Gaussian dependence.
- Relevance: Unit 2 - automated vine fitting for complex dependencies.

---

## Unit 3: Market Microstructure & True Price Extraction

### Key Sources Found

**S14: Clarke (2017) - "Adjusting Bookmaker's Odds to Allow for Overround"**
- DOI: 10.11648/j.ajss.20170506.12
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (diamond OA)
- Implementation Detail: YES
- Key Finding: Compares additive, normalization, Shin, and power methods. Shows Shin and power produce equivalent results for 2-way markets. Power method recommended.
- Relevance: Unit 3 - vig removal method selection.

**S15: Vlastakis et al. (2008) - "How efficient is the European football betting market?"**
- DOI: 10.1002/for.1085
- Type: ACADEMIC, Tier 1 (J. Forecasting)
- Access: FULLTEXT (bronze OA)
- Implementation Detail: YES
- Key Finding: Arbitrage opportunities exist but limited. Combined betting strategies and regression models for prediction. Evidence of market inefficiency.
- Relevance: Unit 3 - market structure and pricing analysis.

**S16: Whelan (2025) - "How Does Inside Information Affect Sports Betting Odds?"**
- DOI: 10.1111/sjpe.70017
- Type: ACADEMIC, Tier 1 (Scottish J. Political Economy)
- Access: FULLTEXT (hybrid OA)
- Implementation Detail: YES
- Key Finding: Generalized Shin's model. Disagreement among bettors without inside info causes favorite-longshot bias. Insider presence reduces but doesn't exacerbate bias.
- Relevance: Unit 3 - Shin model extensions for understanding pricing.

**S17: Sung et al. (2008) - "Complexity as a guide to understanding decision bias"**
- DOI: 10.1002/bdm.629
- Type: ACADEMIC, Tier 1 (J. Behavioral Decision Making)
- Access: FULLTEXT (bronze OA)
- Implementation Detail: YES
- Key Finding: Favorite-longshot bias increases with race complexity. Bookmakers' pricing policies vs cognitive biases of bettors.
- Relevance: Unit 3 - FLB adjustment for different market types.

---

## Unit 4: Portfolio Optimization & Staking

### Key Sources Found

**S18: Ledoit & Wolf (2020) - "Analytical nonlinear shrinkage of large-dimensional covariance matrices"**
- DOI: 10.1214/19-AOS1921
- Type: ACADEMIC, Tier 1 (Annals of Statistics)
- Access: FULLTEXT (bronze OA)
- Implementation Detail: YES
- Key Finding: First analytical formula for nonlinear shrinkage. Connection to Hilbert transform. More elegant than QuEST or NERCOME.
- Relevance: Unit 2/4 - correlation matrix denoising before copula.

**S19: Ledoit & Wolf (2022) - "Quadratic shrinkage for large covariance matrices"**
- DOI: 10.3150/20-BEJ1315
- Type: ACADEMIC, Tier 1 (Bernoulli)
- Access: FULLTEXT (bronze OA)
- Implementation Detail: YES
- Key Finding: Quadratic shrinkage with two targets. Extra degree of freedom accommodates higher concentration regimes.
- Relevance: Unit 2/4 - advanced shrinkage for sparse sports data.

**S20: Bouchaud & Potters (2009) - "Financial Applications of Random Matrix Theory: a short review"**
- arXiv: 0910.1205
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Marcenko-Pastur spectrum, random SVD, largest eigenvalue statistics. Applications to portfolio optimization and out-of-sample risk.
- Relevance: Unit 4 - RMT-based correlation cleaning.

**S21: Yang et al. (2015) - "A Robust Statistics Approach to Minimum Variance Portfolio Optimization"**
- arXiv: 1503.08013
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Hybrid Tyler's M-estimator + Ledoit-Wolf shrinkage. Heavy-tailed returns. Consistent estimator of realized portfolio risk.
- Relevance: Unit 4 - robust covariance estimation for betting returns.

**S22: Pérez-Marco (2014) - "Kelly criterion for variable pay-off"**
- arXiv: 1411.3615
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Kelly criterion for variable payoffs. Fundamental integral equation. Kelly fraction smaller than classical for variable odds.
- Relevance: Unit 4 - Kelly extension for parlay payoffs.

**S23: Byrnes & Barnett (2018) - "Generalized framework for applying the Kelly criterion to stock markets"**
- arXiv: 1806.05293
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Kelly fractions via matrix inversion using first/second moments. Works for portfolio of correlated assets.
- Relevance: Unit 4 - multi-asset Kelly for correlated parlays.

**S24: Lam (2025) - "Beating the Best CRP: Generalization of Kelly with Serial Dependence"**
- arXiv: 2507.05994
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Generalized Kelly for serial dependence. Learning algorithm for optimal growth with time-varying correlations.
- Relevance: Unit 4 - Kelly extension for dependent betting sequences.

---

## Summary Statistics

- **Total Sources Found**: 24
- **Tier 1 (Peer-reviewed)**: 7 (29%)
- **Tier 2 (Preprints/Tech Reports)**: 17 (71%)
- **FULLTEXT Access**: 24 (100%)
- **With Implementation Detail**: 24 (100%)

### Coverage by Unit

| Unit | Sources | FULLTEXT | Implementation Detail |
|------|---------|----------|-----------------------|
| Unit 1: Single-Leg | 7 | 7 | 7 |
| Unit 2: Dependencies | 6 | 6 | 6 |
| Unit 3: Pricing | 4 | 4 | 4 |
| Unit 4: Portfolio | 7 | 7 | 7 |

---

## Additional Sources (Gap-Filling)

**S25: Mahmudlu et al. (2025) - "Hierarchical Bayesian Framework for Counterfactual Expected Goals"**
- arXiv: 2511.23072
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Hierarchical Bayesian integrating expert domain knowledge for player-specific effects. Uses Football Manager ratings as informed priors. Handles sparse shots via shrinkage.
- Relevance: Unit 1 - CRITICAL for player props sparse data modeling.

**S26: Jensen et al. (2009) - "Hierarchical Bayesian Modeling of Hitting Performance in Baseball"**
- arXiv: 0902.1360
- Type: ACADEMIC, Tier 2 [FOUNDATIONAL]
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Balances past performance with covariates (age, position). Mixture distributions control shrinkage. Shares information across time and players.
- Relevance: Unit 1 - FOUNDATIONAL for hierarchical player models.

**S27: Dolmeta et al. (2021) - "Bayesian GARCH Modeling of Functional Sports Data"**
- arXiv: 2101.08175
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Hierarchical Bayesian for athlete performance evolution. Smooth functional contribution + linear mixed effects with heteroskedastic errors.
- Relevance: Unit 1 - time-varying player performance modeling.

**S28: Ötting et al. (2021) - "The reaction to news in live betting"**
- arXiv: 2108.00821
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: State-space modeling framework for live betting at 1 Hz resolution. Markets overreact to recent news (goals). Accounts for general market activity.
- Relevance: Unit 1 (live updates) - state-space implementation for in-play.

**S29: Berthet (2023) - "FightTracker: Real-time predictive analytics for MMA"**
- arXiv: 2312.11067
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Real-time predictions using in-round statistics. 80% accuracy. Live betting strategy achieved 90.17% ROI over 8 weeks vs Unibet.
- Relevance: Unit 1/3 - real-time model + live betting profit validation.

**S30: Mott et al. (2025) - "Matchup Models in Baseball Win Probability"**
- arXiv: 2511.17733
- Type: ACADEMIC, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Four progressively complex hierarchical Bayesian matchup models. Predicts plate appearance outcomes. Game-theoretic framework for in-game decisions.
- Relevance: Unit 1 - hierarchical matchup modeling architecture.

---

### Identified Gaps

1. **Synthetic Odds Generation**: No academic papers found directly addressing generation of historical SGP odds for backtesting. This is the SGP Backtesting Paradox.
2. **Correlation Collision Detection**: No academic work on portfolio-level latent factor exposure across multiple parlays.

---

*Discovery completed: 2026-02-04*
*Search queries: 12*
*Databases: OpenAlex, arXiv*
