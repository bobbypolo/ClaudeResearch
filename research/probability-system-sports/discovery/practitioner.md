# Practitioner Discovery Pass

## Unit 1: Single-Leg Probability & Calibration

### Key Sources Found

**P1: Sportsbookadvisor (2025) - "Why 90% of Value Bets Aren't Actually Value: Probability Calibration"**
- URL: https://www.sportsbookadvisor.com/2025/12/06/why-90-of-value-bets-arent-actually-value
- Type: PRACTITIONER, Tier 3
- Access: FULLTEXT (web)
- Key Finding: Pinnacle closing line as industry standard for calibration testing. Systematic calibration errors lead to losses for most bettors.
- Relevance: Unit 1 - practical calibration benchmarking.

**P2: Pinnacle (2022) - "What is implied probability?"**
- URL: https://www.pinnacle.com/en/esports-hub/betting-articles/educational/implied-probability-odds-conversion
- Type: PRACTITIONER, Tier 3
- Access: FULLTEXT (web)
- Key Finding: Formulas for converting decimal and American odds to implied probability. Explains bookmaker margin calculation.
- Relevance: Unit 3 - fundamental implied probability conversion.

**P3: Dean Markwick (2019) - "Calibrating Odds"**
- URL: https://dm13450.github.io/2019/01/10/Odds-and-Winning.html
- Type: PRACTITIONER, Tier 3
- Access: FULLTEXT (web)
- Implementation Detail: YES
- Key Finding: Raw Pinnacle odds well-calibrated. Multinomial regression to adjust odds. Adjusting for over-round gives same predictions as raw odds.
- Relevance: Unit 1/3 - practical calibration analysis with code.

**P4: Štrumbelj (2014) - "On determining probability forecasts from betting odds"**
- URL: https://www.sciencedirect.com/science/article/abs/pii/S0169207014000533
- Type: ACADEMIC/PRACTITIONER crossover, Tier 1
- Access: PAYWALLED (abstract only)
- Key Finding: Shin probabilities more accurate than basic normalization or regression. Regression models calibrated but poor resolution.
- Relevance: Unit 3 - Shin method validation.

**P5: Geekculture Medium (2021) - "How to Compute Football Implied Probabilities"**
- URL: https://medium.com/geekculture/how-to-compute-football-implied-probabilities
- Type: PRACTITIONER, Tier 3
- Access: FULLTEXT (web)
- Implementation Detail: YES
- Key Finding: Empirical comparison of Multiplicative, Additive, Power, and Shin methods using log loss. Shin and Power generally outperform.
- Relevance: Unit 3 - method comparison with implementation.

---

## Unit 2: SGP Correlation Modeling

### Key Sources Found

**P6: Wizard of Odds (2025) - "Same-Game Parlays: The Mathematics of Correlation"**
- URL: https://wizardofodds.com/article/same-game-parlays-the-mathematics-of-correlation/
- Type: PRACTITIONER, Tier 3
- Access: FULLTEXT (web)
- Implementation Detail: YES
- Key Finding: Sportsbooks use correlation matrices (Pearson coefficients from historical data) to quantify SGP dependence. Detailed mathematical explanation of pricing.
- Relevance: Unit 2 - SGP pricing implementation details.

**P7: OddsIndex (2025) - "Same Game Parlay Correlation: How the Hidden Tax Works"**
- URL: https://oddsindex.com/guides/same-game-parlay-correlation
- Type: PRACTITIONER, Tier 3
- Access: FULLTEXT (web)
- Key Finding: Explains "correlation tax" - positive correlation leads to lower odds (discount), negative correlation leads to higher odds (penalty). Sportsbook pricing strategy exposed.
- Relevance: Unit 2/3 - understanding sportsbook SGP adjustments.

**P8: OpticOdds (2025) - "Correlation in Same Game Parlays: How Sportsbooks are Tackling the Challenge"**
- URL: https://opticodds.com/blog/correlation-in-same-game-parlays
- Type: PRACTITIONER, Tier 3
- Access: FULLTEXT (web)
- Key Finding: Real-time predictive modeling for correlation. AlgoOdds technology for dynamic SGP pricing. Bet Builder and SGP Engine tools.
- Relevance: Unit 2 - industry practice for dynamic correlation.

**P9: Analytics.bet (2021) - "Patrick Mahomes and the Anatomy of a Correlated Parlay"**
- URL: https://analytics.bet/articles/patrick-mahomes-and-the-anatomy-of-a-correlated-parlay/
- Type: PRACTITIONER, Tier 3
- Access: FULLTEXT (web)
- Implementation Detail: YES
- Key Finding: Single uncertain variable (e.g., player availability) can create exploitable correlation. Positive correlation = standard payout too high = +EV opportunity.
- Relevance: Unit 2 - practical correlation identification.

**P10: CoreSportsBetting (2025) - "How to Use Monte Carlo Simulation in Parlay Betting Strategy"**
- URL: https://www.coresportsbetting.com/how-to-use-monte-carlo-simulation-in-parlay-a-betting-strategy/
- Type: PRACTITIONER, Tier 3
- Access: FULLTEXT (web)
- Implementation Detail: YES
- Key Finding: Step-by-step Monte Carlo implementation for parlay risk modeling. Spreadsheet and programming approaches. EV calculation and structure optimization.
- Relevance: Unit 2/4 - simulation-based parlay analysis.

**P11: BettingPros (2024) - "NBA SGP Builder Tool"**
- URL: https://blog.fantasypros.com/03-12-2024-same-game-parlay-tool/
- Type: PRACTITIONER, Tier 3
- Access: FULLTEXT (web)
- Implementation Detail: YES
- Key Finding: Real-time correlation grades for SGP legs. Algorithm calculates implied odds and cover probability based on correlation model.
- Relevance: Unit 2 - commercial implementation of correlation scoring.

**P12: Stanford Wong via BJ21 (2025) - "Correlated Parlays"**
- URL: https://bj21.com/articles/sports-betting/correlated-parlays
- Type: PRACTITIONER, Tier 3
- Access: FULLTEXT (web)
- Key Finding: Covariance as mathematical measure of correlation. Finding correlations sportsbooks allow is key. Single uncertain variable affecting multiple bets creates opportunity.
- Relevance: Unit 2 - expert practitioner perspective.

---

## Unit 3: Vig Removal & Market Structure

### Key Sources Found

*See P2-P5 above for vig removal methods.*

**P13: Clegg & Cartlidge (2023) - "Not feeling the buzz: Correction study of mispricing"**
- arXiv: 2306.01740
- Type: ACADEMIC/PRACTITIONER crossover, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Replication study showing importance of data cleaning in backtesting. Single outlier bet ("Hercog bet") drove majority of profits. Markets may have become more efficient post-2020.
- Relevance: Unit 3/Critical - backtesting methodology and data quality.

---

## Unit 4: Portfolio & Kelly Criterion

### Key Sources Found

**P14: Hubáček & Šír (2020) - "Beating the market with a bad predictive model"**
- arXiv: 2010.12508
- Type: ACADEMIC/PRACTITIONER crossover, Tier 2
- Access: FULLTEXT (arXiv)
- Implementation Detail: YES
- Key Finding: Systematic profits possible with inferior price-predicting model by decorrelating from market. Exploits market maker pricing biases.
- Relevance: Unit 4 - unconventional portfolio strategy.

---

## Summary Statistics

- **Total Practitioner Sources**: 14
- **Tier 3 (Industry/Blogs)**: 11 (79%)
- **Tier 1-2 Crossover**: 3 (21%)
- **FULLTEXT Access**: 13 (93%)
- **With Implementation Detail**: 9 (64%)

### Key Implementation Insights

1. **Calibration > Accuracy**: Multiple sources confirm Pinnacle closing line as benchmark for calibration testing.

2. **Shin/Power Methods**: Both practitioners and academics converge on Shin or Power method for vig removal. Simpler normalization methods underperform.

3. **SGP Correlation**: Sportsbooks use correlation matrices from historical data. "Correlation tax" adjusts odds for positive/negative correlation.

4. **Monte Carlo Simulation**: Widely recommended for parlay strategy modeling and risk assessment.

5. **Data Quality Critical**: Backtesting results highly sensitive to data quality; single outliers can dominate P&L.

### Identified Gaps

1. **Synthetic Odds Generation**: No practitioner sources describe generating historical SGP odds for backtesting.
2. **Correlation Collision Detection**: No sources address portfolio-level latent factor exposure across multiple parlays.
3. **Live Betting Implementation**: Limited practical guidance on particle filter / state-space implementations.

---

*Discovery completed: 2026-02-04*
*Search queries: 3*
*Databases: Exa Web Search*
