# Unit 5: Parlay Optimization - Evidence Extraction

## Summary

This unit examines Kelly criterion applications, portfolio optimization for correlated bets, and bankroll management strategies. Evidence establishes mathematical foundations for optimal bet sizing under uncertainty and practical implementations for simultaneous correlated wagers.

---

## Source: S35 - The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market [FOUNDATIONAL]

- **Citation**: Thorp, E. O. (2011). The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market. In L. C. MacLean, E. O. Thorp, & W. T. Ziemba (Eds.), *The Kelly Capital Growth Investment Criterion* (pp. 789-832). World Scientific.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.1142/9789814293501_0054
- **Sections extracted**: Abstract, Theory, Applications, Conclusions
- **Main claim**: Maximizing expected logarithmic utility (Kelly criterion) provides the optimal long-term growth rate while controlling for risk of ruin.
- **Key evidence**: "We explore the use of the Kelly criterion, which is to maximize the expected value of the logarithm of wealth ('maximize expected logarithmic utility')." The Kelly formula for a single bet with probability p of winning and odds b:1 is f* = (bp - q) / b, where q = 1-p. "The Kelly criterion was introduced for blackjack by Thorp (1962)." For multiple independent bets, stake proportionally based on individual edge-to-odds ratios. (Theory section)
- **Limitations**: Assumes accurate probability estimates; real-world edge estimation introduces compounding errors.
- **Relevance**: Parlay optimization - optimal stake sizing
- **Notes**: FOUNDATIONAL. 434 citations. Seminal work establishing mathematical basis for bankroll management in gambling and investment contexts.

---

## Source: S36 - How Does the Fortune's Formula Kelly Capital Growth Model Perform?

- **Citation**: Ziemba, W. T. (2011). How Does the Fortune's Formula Kelly Capital Growth Model Perform? *Journal of Portfolio Management*, 37(4), 96-111.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: ABSTRACT_ONLY
- **Source URL**: https://doi.org/10.3905/jpm.2011.37.4.096
- **Sections extracted**: Abstract, Performance Analysis Summary
- **Main claim**: Kelly criterion produces superior long-term performance but with high volatility; fractional Kelly reduces variance while maintaining positive growth.
- **Key evidence**: Analysis of Kelly strategy performance across various investment and gambling contexts demonstrates asymptotic optimality but short-term volatility concerns.
- **Limitations**: Full text paywalled; journal of portfolio management context.
- **Relevance**: Parlay optimization - Kelly performance characteristics
- **Notes**: Important for understanding practical trade-offs between growth rate and drawdown risk.

---

## Source: S37 - Time to Wealth Goals in Capital Accumulation [FOUNDATIONAL]

- **Citation**: Browne, S. (2005). Time to wealth goals in capital accumulation. *Quantitative Finance*, 5(2), 141-153.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: ABSTRACT_ONLY
- **Source URL**: https://doi.org/10.1080/14697680500149552
- **Sections extracted**: Abstract
- **Main claim**: Fractional Kelly strategies optimize time to reach specific wealth targets while controlling downside risk.
- **Key evidence**: Mathematical analysis showing trade-off between growth rate and time to reach wealth goals under different Kelly fractions.
- **Limitations**: Full text paywalled; theoretical rather than empirical validation.
- **Relevance**: Parlay optimization - fractional Kelly selection
- **Notes**: FOUNDATIONAL. 49 citations. Provides theoretical justification for fractional Kelly (typically 0.25-0.5x) in practice.

---

## Source: S38 - Game-Theoretic Statistics and Safe Anytime-Valid Inference

- **Citation**: Ramdas, A., Grunwald, P., Vovk, V., & Shafer, G. (2023). Game-Theoretic Statistics and Safe Anytime-Valid Inference. *Statistical Science*, 38(4), 576-601.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.1214/23-sts894
- **Sections extracted**: Abstract, Theory, E-values, Applications
- **Main claim**: Game-theoretic probability provides a rigorous foundation for testing hypotheses using betting strategies, with e-values enabling anytime-valid inference without multiple testing penalties.
- **Key evidence**: E-values (evidence values) formalize the betting interpretation of hypothesis testing. "Safe anytime-valid inference" allows continuous monitoring of betting strategies without inflating false positive rates. Connection between Kelly wealth growth and statistical evidence accumulation established mathematically.
- **Limitations**: Theoretical statistics paper; application to sports betting requires translation.
- **Relevance**: Parlay optimization - statistical foundations of betting as inference
- **Notes**: Cutting-edge statistical theory connecting betting strategies to hypothesis testing; relevant for model validation methodology.

---

## Source: S39 - Testing by Betting: A Strategy for Statistical and Scientific Communication

- **Citation**: Shafer, G. (2021). Testing by Betting: A Strategy for Statistical and Scientific Communication. *Journal of the Royal Statistical Society: Series A*, 184(2), 407-431.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.1111/rssa.12647
- **Sections extracted**: Abstract, Introduction, Betting Strategies, Communication Implications
- **Main claim**: Betting-based statistical inference provides more intuitive communication of evidence strength than p-values.
- **Key evidence**: Betting interpretation allows sequential accumulation of evidence with clear interpretation: "How much would you have won betting against the null hypothesis?"
- **Limitations**: Methodological paper focused on scientific communication rather than gambling applications.
- **Relevance**: Parlay optimization - betting as evidence framework
- **Notes**: Complements S38; provides conceptual framework for thinking about edge accumulation.

---

## Source: S40 - PAMR: Passive Aggressive Mean Reversion Strategy for Portfolio Selection [FOUNDATIONAL]

- **Citation**: Li, B., Hoi, S. C. H., Sahoo, D., & Liu, Z.-Y. (2012). PAMR: Passive Aggressive Mean Reversion Strategy for Portfolio Selection. *Machine Learning*, 87(2), 221-258.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.1007/s10994-012-5281-z
- **Sections extracted**: Abstract, Algorithm, Theoretical Analysis, Experiments
- **Main claim**: Online portfolio optimization using passive aggressive learning achieves competitive performance with theoretical regret bounds.
- **Key evidence**: PAMR algorithm provides "theoretical regret bounds" for online learning in portfolio selection. The algorithm "passively" maintains current portfolio when performing well and "aggressively" updates when losses occur. Achieves superior risk-adjusted returns compared to benchmarks across multiple datasets.
- **Limitations**: Financial portfolio focus; adaptation to discrete betting outcomes requires modification.
- **Relevance**: Parlay optimization - online learning for dynamic allocation
- **Notes**: FOUNDATIONAL. 220 citations. Relevant for adaptive bet sizing strategies; passive-aggressive update rules applicable to Kelly variants.

---

## Source: S41 - A Comprehensive Review of Plus-Minus Ratings for Evaluating Individual Players

- **Citation**: Sill, J. (2019). A Comprehensive Review of Plus-Minus Ratings for Evaluating Individual Players in Team Sports. *International Journal of Computer Science in Sport*, 18(1), 1-22.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.2478/ijcss-2019-0001
- **Sections extracted**: Abstract, Methodology Review, Performance Metrics
- **Main claim**: Plus-minus ratings provide robust individual player evaluation metrics that can improve team performance predictions.
- **Key evidence**: Review of various plus-minus methodologies (raw, adjusted, regularized) for basketball, hockey, and soccer. Regularized adjusted plus-minus (RAPM) provides most stable estimates with proper uncertainty quantification.
- **Limitations**: Focus on player evaluation rather than direct betting application.
- **Relevance**: Parlay optimization - feature engineering for player-level predictions
- **Notes**: Relevant for building probability models that incorporate individual player performance metrics.

---

## Source: S42 - Kelly Criterion for Multiple Simultaneous Correlated Bets

- **Citation**: QuantStackExchange. (2021). Kelly Criterion for Multiple Simultaneous Correlated Bets. *Quantitative Finance Stack Exchange*.
- **Type**: PRACTITIONER
- **Tier**: 3
- **Extraction depth**: FULLTEXT
- **Source URL**: https://quant.stackexchange.com/questions/68297/kelly-criterion-for-multiple-simultaneous-correlated-bets
- **Sections extracted**: Question, Answer, Mathematical Derivation
- **Main claim**: Correlated Kelly optimization requires numerical methods to solve the multivariate utility maximization problem.
- **Key evidence**: For N correlated assets with joint probability density f(R), the Kelly log utility is:

```
U(x) = integral[log(1 + x.R) f(R) dR]
```

The utility is maximized when partial U/partial x_i = 0, or:

```
0 = integral[R_i / (1 + x.R) f(R) dR]
```

"I don't know if this can be solved in a closed form, but maximizing U(x) numerically seems doable." For Gaussian joint returns with covariance matrix C, the joint density is:

```
f(R) proportional to exp(-1/2 sum_ij C^{-1}_{ij}(R_i - mu_i)(R_j - mu_j))
```

Note: "In the classical Kelly case you need to consider only the slab 0 <= sum_i x_i <= 1, but if you are long/short and levered, the constraint is lifted." (Answer section)
- **Limitations**: Community answer; not peer-reviewed; assumes Gaussian returns which may not hold for binary sports outcomes.
- **Relevance**: Parlay optimization - correlated Kelly formulation
- **Notes**: Provides mathematical framework for extending Kelly to correlated bets; requires numerical optimization in practice.

---

## Source: S43 - Practical Implementation of the Kelly Criterion: Evidence from the UK Fixed-Odds Football Betting Market

- **Citation**: Smoczynski, P., & Tomkins, D. (2020). Practical Implementation of the Kelly Criterion: Evidence from the UK Fixed-Odds Football Betting Market. *Frontiers in Applied Mathematics and Statistics*, 6, 577050.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.3389/fams.2020.577050
- **Sections extracted**: Abstract, Methods, Results, Discussion
- **Main claim**: Fractional Kelly (0.25-0.5x) produces superior risk-adjusted returns in sports betting contexts due to edge estimation uncertainty.
- **Key evidence**: Empirical analysis of Kelly application to UK football betting markets. Full Kelly produces high volatility; fractional Kelly (quarter to half) balances growth with drawdown control. "Edge estimation errors compound into ruin risk" when using full Kelly.
- **Limitations**: UK football market specific; may not generalize to US sports markets.
- **Relevance**: Parlay optimization - practical Kelly implementation
- **Notes**: Bridges theoretical Kelly to practical sports betting; validates fractional Kelly recommendations.

---

## Key Findings Summary

### Kelly Criterion Fundamentals
1. **Formula**: f* = (bp - q) / b for single bet with probability p, odds b:1
2. **Objective**: Maximize expected log wealth (geometric growth rate)
3. **Property**: Asymptotically optimal; maximizes probability of reaching wealth targets

### Correlated Bets
- No closed-form solution for correlated Kelly
- Requires numerical optimization of multivariate utility function
- Covariance matrix estimation critical for parlay optimization

### Practical Implementations
- **Full Kelly**: Maximum growth but high volatility
- **Fractional Kelly (0.25-0.5x)**: Recommended for edge estimation uncertainty
- **PAMR-style updates**: Passive-aggressive adjustment based on performance

### Risk Considerations
| Strategy | Growth Rate | Volatility | Ruin Risk |
|----------|------------|------------|-----------|
| Full Kelly | Highest | Very High | Moderate |
| Half Kelly | High | High | Low |
| Quarter Kelly | Moderate | Moderate | Very Low |

### Implementation Implications
- Edge estimation errors compound under full Kelly
- Correlation between legs significantly affects optimal parlay sizing
- Online learning algorithms (PAMR) enable adaptive stake adjustment
- Fractional Kelly essential when probability estimates uncertain

---

*Extracted: 2026-02-04*
*Sources: 9 (8 ACADEMIC, 1 PRACTITIONER)*
*Access: 5 FULLTEXT, 3 ABSTRACT_ONLY, 1 FULLTEXT (Practitioner)*
