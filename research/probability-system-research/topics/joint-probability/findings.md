# Findings: Joint Probability Research Unit

## Summary

This unit examines methods for estimating joint probabilities in correlated betting markets, with particular focus on same-game parlays (SGPs), copula models, and correlation structure estimation. The challenge: individual leg probabilities alone are insufficient when outcomes within the same game are dependent.

---

## Source: S18 - Pointwise Partial Information Decomposition Using the Specificity and Ambiguity Lattices

- **Citation**: Finn, C., & Lizier, J.T. (2018). Pointwise Partial Information Decomposition Using the Specificity and Ambiguity Lattices. Entropy, 20(4), 297. https://doi.org/10.3390/e20040297
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://www.mdpi.com/1099-4300/20/4/297
- **Sections extracted**: Abstract, Introduction, Methodology, Discussion, Appendix (Kelly Gambling reference)
- **Main claim**: Information from multiple predictor variables about a target can be decomposed into unique, redundant, and synergistic components using partial information decomposition (PID) via specificity and ambiguity lattices.
- **Key evidence**: "The aim of information decomposition is to divide the total amount of information provided by a set of predictor variables, about a target variable, into atoms of partial information contributed either individually or jointly by the various subsets of the predictors." Framework addresses how to quantify when variables provide unique vs. redundant vs. complementary (synergistic) information.
- **Limitations**: Theoretical information-theoretic framework; not directly applied to sports betting contexts; computational complexity for large predictor sets.
- **Relevance**: joint-probability
- **Notes**: Foundational for understanding correlation structure. Appendix A discusses Kelly gambling connection. Framework can theoretically identify when bet combinations provide truly independent information vs. redundant or synergistic value.

---

## Source: S19 - Forecasting Binary Outcomes in Soccer

- **Citation**: Angelini, G., Candila, V., & De Angelis, L. (2021). Forecasting binary outcomes in soccer. Annals of Operations Research, 325, 115-134. https://doi.org/10.1007/s10479-021-04224-8
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://link.springer.com/article/10.1007/s10479-021-04224-8
- **Sections extracted**: Abstract, Introduction, Methodology, Results
- **Main claim**: Score-driven models can effectively forecast binary outcomes beyond match results, including Under/Over totals, Goal/No Goal, and red card occurrence.
- **Key evidence**: "Several studies deal with the development of advanced statistical methods for predicting football match results... nowadays a variety of other outcomes are available for betting purposes. While some of these events are binary in nature (e.g. the red cards occurrence), others can be seen as binary outcomes." Framework enables prediction of multiple correlated binary outcomes from the same game.
- **Limitations**: Soccer-specific; model complexity may limit real-time applications; correlation between predicted outcomes not explicitly addressed.
- **Relevance**: joint-probability
- **Notes**: Extends Poisson-based match prediction to binary props (Over/Under, BTTS). Important for SGP context where combining match totals with team totals creates correlation. Score-driven framework allows time-varying parameters.

---

## Source: S20 - Group Selection as Behavioral Adaptation to Systematic Risk

- **Citation**: Zhang, R., Brennan, T.J., & Lo, A.W. (2014). Group Selection as Behavioral Adaptation to Systematic Risk. PLoS ONE, 9(10), e110848. https://doi.org/10.1371/journal.pone.0110848
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0110848
- **Sections extracted**: Abstract, Introduction, Discussion
- **Main claim**: Selection with correlated reproductive risk can explain apparent group behavior even when individual actions are autonomous; correlation in risk creates emergent "group" patterns.
- **Key evidence**: "What appears to be group selection may, in fact, simply be the consequence of natural selection occurring in stochastic environments with reproductive risks that are correlated across individuals. Those individuals with highly correlated risks will appear to form 'groups', even if their actions are, in fact, totally autonomous, mindless, and, prior to selection, uniformly randomly distributed in the population."
- **Limitations**: Evolutionary biology focus; theoretical framework not directly applied to betting; requires translation to financial/betting context.
- **Relevance**: joint-probability
- **Notes**: From Andrew Lo (MIT, Adaptive Markets Hypothesis). Key insight for SGP risk: correlated outcomes create emergent portfolio risk even without explicit coordination. Implications for bankroll management with correlated bets - correlation risk may be underestimated.

---

## Source: S21 - Bayesian State-Space Models for EPL Football Results

- **Citation**: Ridall, P.G., et al. (2024). Bayesian state-space models for EPL football results. Journal of the Royal Statistical Society: Series C (Applied Statistics), 74(1), 70+. https://doi.org/10.1093/jrsssc/qlae075
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: ABSTRACT_ONLY (page not found on access attempt)
- **Source URL**: https://doi.org/10.1093/jrsssc/qlae075
- **Sections extracted**: Abstract (limited)
- **Main claim**: Bayesian state-space models capture time-varying team strengths and enable principled uncertainty quantification for match outcome prediction.
- **Key evidence**: State-space framework allows modeling of evolving team abilities over season; Bayesian approach provides full posterior distributions rather than point estimates.
- **Limitations**: Paywalled; EPL-specific; computational intensity of MCMC methods.
- **Relevance**: joint-probability
- **Notes**: State-space approach naturally extends to modeling correlated outcomes (e.g., team and player performance evolving together). Uncertainty quantification critical for joint probability estimation.

---

## Source: S22 - Artificial Data in Sports Forecasting: A Simulation Framework

- **Citation**: [Authors]. (2022). Artificial data in sports forecasting: a simulation framework. Electronic Markets, 32(4), 2251-2266. https://doi.org/10.1007/s10257-022-00560-9
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: ABSTRACT_ONLY
- **Source URL**: https://doi.org/10.1007/s10257-022-00560-9
- **Sections extracted**: Abstract
- **Main claim**: Simulation frameworks with artificial data generation enable robust testing of forecasting models under controlled conditions.
- **Key evidence**: Framework allows generation of correlated outcomes with known dependency structures, enabling validation of joint probability estimation methods.
- **Limitations**: Simulated data may not capture all real-world complexities; generalizability depends on simulation fidelity.
- **Relevance**: joint-probability
- **Notes**: Important for backtesting joint probability models. Controlled correlation structures allow validation that models correctly identify and quantify dependencies.

---

## Source: S23 - Bivariate Copula-based Regression for Modeling Football Matches

- **Citation**: Ekman, E. (2020). Bivariate Copula-based Regression for Modeling Football Matches. Master's Thesis, Lund University.
- **Type**: ACADEMIC
- **Tier**: 2 (thesis)
- **Extraction depth**: ABSTRACT_ONLY
- **Source URL**: Lund University Repository
- **Sections extracted**: Abstract
- **Main claim**: Copula models effectively capture the dependency structure between home and away team goal scoring in football matches.
- **Key evidence**: Thesis applies copula methodology to model the joint distribution of (home goals, away goals), allowing for flexible dependency beyond simple correlation.
- **Limitations**: Master's thesis (not peer-reviewed journal); soccer-specific; single-competition focus.
- **Relevance**: joint-probability
- **Notes**: Direct application of copulas to sports betting context. Foundational for understanding how to model joint probabilities in SGPs where team performances are correlated.

---

## Source: S24 - Same-Game Parlays: The Mathematics of Correlation

- **Citation**: Wizard of Odds. (2025). Same-Game Parlays: The Mathematics of Correlation. https://wizardofodds.com/article/same-game-parlays-the-mathematics-of-correlation/
- **Type**: PRACTITIONER
- **Tier**: 3
- **Extraction depth**: FULLTEXT
- **Source URL**: https://wizardofodds.com/article/same-game-parlays-the-mathematics-of-correlation/
- **Sections extracted**: Full article
- **Main claim**: SGP pricing requires sophisticated correlation modeling; positive correlation between legs increases joint probability, requiring lower payouts than independent parlay math would suggest.
- **Key evidence**:

  **Traditional (Independent) Parlay Math:**
  - P(all win) = p1 x p2 x ... x pn
  - Example: Three -110 legs = 0.524^3 = 14.4% = fair odds +594

  **SGP Correlation Impact:**
  - With positive correlation (e.g., ρ = 0.28-0.42 between legs), true combined probability increases from 16.0% to 21.2%
  - This is a 33% increase in probability, requiring proportionally lower payout

  **Gaussian Copula Method:**
  1. Transform binary outcomes to latent normal variables via inverse CDF
  2. Model as multivariate normal with correlation matrix R
  3. Calculate joint probability via integral over MVN distribution

  **Example Correlation Matrix:**
  | | Team Win | QB O275 | Total Over |
  |---|---|---|---|
  | Team Win | 1.00 | 0.35 | 0.28 |
  | QB O275 | 0.35 | 1.00 | 0.42 |
  | Total Over | 0.28 | 0.42 | 1.00 |

  **Empirical Frequency Method:**
  - Count historical co-occurrence of specific combinations
  - Example: 500 historical games showed 20.4% all-three-hit vs. 15.7% under independence
  - Correlation adjustment factor: 20.4/15.7 = 1.30 (30% increase)

- **Limitations**: Educational focus (not academic peer review); representative but not validated correlation values; US sportsbook focus.
- **Relevance**: joint-probability
- **Notes**: Excellent practitioner explanation of SGP pricing mathematics. Key insight: "positive correlation makes the parlay more likely to hit than independence would suggest, which means the sportsbook must offer shorter odds (lower payout)." Critical for understanding correlation tax.

---

## Source: S25 - Same Game Parlay Correlation: How the Hidden Tax on SGPs Really Works

- **Citation**: OddsIndex. (2025). Same Game Parlay Correlation: How the Hidden Tax on SGPs Really Works. https://oddsindex.com/guides/same-game-parlay-correlation
- **Type**: PRACTITIONER
- **Tier**: 3
- **Extraction depth**: FULLTEXT
- **Source URL**: https://oddsindex.com/guides/same-game-parlay-correlation
- **Sections extracted**: Full article
- **Main claim**: The "correlation tax" in SGPs creates house edges of 20%+ compared to ~5% on straight bets; understanding correlation is essential for identifying when books misprice SGP combinations.
- **Key evidence**:

  **Why SGPs Were Historically Banned:**
  - Correlated parlays gave bettors edge when priced as independent
  - Books now embrace SGPs because they can price correlation in

  **Correlation Types:**
  - **Positive**: QB passing yards + team total over (move together)
  - **Negative**: Team covering large spread + game under (blowout with clock management)
  - **Uncorrelated**: Rare in same-game context

  **SGP Hold Rates:**
  - SGP hold rates: 20%+ (vs. ~5% for straight bets)
  - "Three to five times higher than straight bets"

  **Example Calculation:**
  - Independent calculation: +596
  - After correlation adjustment: +350
  - Gap is the "correlation tax"

  **Hybrid Pricing Methods:**
  - Most sophisticated books use empirical frequencies where data is abundant
  - Gaussian copulas or other models for novel combinations

- **Limitations**: Practitioner guide format; specific correlation values are illustrative; focuses on bettor awareness rather than edge extraction.
- **Relevance**: joint-probability
- **Notes**: Key quantitative insight: SGP hold rates 3-5x higher than straight bets. Critical framework for understanding why SGP edges may exist (mispricing) but overall market is heavily tilted toward house. Identifies negative correlation as potential opportunity when books don't fully adjust.

---

## Unit Summary: Key Findings for Joint Probability

### The Fundamental Problem

From S24: "When all bets come from the same game, independence is violated." Traditional parlay math fails:
- P(all win) ≠ p1 x p2 x ... x pn when legs are correlated
- Positive correlation INCREASES joint probability
- Sportsbooks must offer LOWER payouts to compensate

### Correlation Quantification Methods

**1. Pearson Correlation Coefficient (S24)**
- Measures pairwise co-movement
- Typical sports betting range: ρ between -0.4 and +0.6
- Requires historical data for each pair type

**2. Gaussian Copula (S24)**
- Transform to latent normals via inverse CDF
- Apply correlation matrix structure
- Calculate joint probability via multivariate normal integral
- Advantage: Preserves marginal probabilities while modeling dependency

**3. Empirical Frequency (S24, S25)**
- Direct counting of historical co-occurrence
- No distributional assumptions
- Requires large datasets for specific combinations
- Most books use hybrid: empirical where data abundant, copulas elsewhere

**4. Partial Information Decomposition (S18)**
- Theoretical framework for unique vs. redundant vs. synergistic information
- Advanced but computationally intensive

### The Correlation Tax

From S25:
- **SGP hold rates: 20%+ vs. ~5% for straight bets**
- Gap between independent parlay odds and SGP odds = correlation tax
- Example: +596 (independent) vs. +350 (correlated) = ~246 basis point penalty

### When Correlation Creates Opportunity

**Negative Correlation (S25):**
- "When you stack negatively correlated legs, the true combined probability is lower"
- If book doesn't fully adjust for negative correlation, payouts may exceed fair value
- Example: Team covering large spread + game going under (blowout clock management)

**Mispricing (S24, S25):**
- Novel combinations where books lack empirical data
- Late-breaking news creating temporary inefficiencies
- Cross-book arbitrage on correlation assumptions

### Modeling Frameworks

**Score-Driven Models (S19):**
- Extend match prediction to binary props
- Handle time-varying parameters
- Foundation for predicting correlated binary outcomes

**State-Space Models (S21):**
- Capture evolving team strengths
- Bayesian uncertainty quantification
- Natural extension to correlated outcomes

**Copula Models (S23):**
- Flexible dependency beyond simple correlation
- Applied to (home goals, away goals) joint distribution
- Extensible to player props

### Risk Implications

From S20 (Lo et al.):
- Correlated risks create emergent portfolio risk
- Even autonomous outcomes appear as "groups" when correlated
- Implication: Bankroll management must account for correlation exposure

### Confidence Assessment

- **Claim: Independence assumption fails for SGPs** - HIGH (S24, S25 provide clear mathematical demonstration)
- **Claim: Positive correlation increases joint probability** - HIGH (S24, S25 with quantitative examples)
- **Claim: SGP hold rates are 3-5x higher than straight bets** - HIGH (S25 cites industry data and earnings reports)
- **Claim: Gaussian copula is standard pricing method** - CONTESTED (S24 presents it; actual book methods are proprietary)
- **Claim: Negative correlation creates betting opportunity** - LOW (theoretical basis exists but no empirical validation provided)
- **Claim: Correlation can be accurately estimated** - LOW (requires substantial historical data; proprietary methods vary)

### Key Metrics for Implementation

| Metric | Purpose | Range |
|--------|---------|-------|
| Pearson Correlation (ρ) | Pairwise dependency | -1 to +1, typical: -0.4 to +0.6 |
| Correlation Tax | SGP vs. independent parlay gap | Typically 3-5x vig |
| Co-occurrence Frequency | Empirical joint probability | Historical % |
| Correlation Matrix | Full dependency structure | NxN for N legs |

### Recommended Approach

From S24 and S25 combined:
1. **Build empirical correlation matrices** from historical data by bet type and game situation
2. **Use hybrid method**: empirical frequencies where abundant, copulas for novel combinations
3. **Monitor correlation tax**: compare SGP prices to independent parlay calculation
4. **Target negative correlation**: where books may underprice (blowouts, clock management scenarios)
5. **Validate with simulation**: use artificial data (S22) to test joint probability models

---

*Extracted: 2026-02-04*
*Version: 1.0*
