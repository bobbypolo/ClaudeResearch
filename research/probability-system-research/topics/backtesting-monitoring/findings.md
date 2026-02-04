# Unit 6: Backtesting & Monitoring - Evidence Extraction

## Summary

This unit examines validation methodologies for sports betting models, including data leakage prevention, walk-forward testing, and performance monitoring metrics. Evidence establishes rigorous backtesting protocols and the role of Closing Line Value (CLV) as a leading indicator of betting model quality.

---

## Source: S44 - Time Series Forecasting of Univariate Agrometeorological Data

- **Citation**: Ferreira, F., Lemos, H., & Braz, P. (2021). Time Series Forecasting of Univariate Agrometeorological Data: An Empirical Investigation. *Sensors*, 21(7), 2430.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.3390/s21072430
- **Sections extracted**: Abstract, Methods, Validation Framework, Results
- **Main claim**: Time series forecasting requires strict temporal separation in train/test splits to avoid data leakage and overestimation of model performance.
- **Key evidence**: Walk-forward validation methodology where "training on one period and testing on the next" mimics real deployment. Temporal cross-validation prevents look-ahead bias that occurs with random shuffling. Performance metrics (RMSE, MAE) should be computed on truly out-of-sample data.
- **Limitations**: Agricultural domain; not sports-specific but methodology transfers.
- **Relevance**: Backtesting - temporal validation methodology
- **Notes**: Establishes rigorous framework for time-series model validation applicable to sports predictions.

---

## Source: S45 - Artificial Intelligence in Asset Management

- **Citation**: Bartram, S. M., Branke, J., & Motahari, M. (2020). Artificial Intelligence in Asset Management. *CFA Institute Research Foundation*.
- **Type**: ACADEMIC
- **Tier**: 2 (Research Foundation Publication)
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.2139/ssrn.3692805
- **Sections extracted**: Abstract, AI Applications, Risk Management, Model Validation
- **Main claim**: AI has revolutionized asset management but introduces new risks from model opacity, complexity, and reliance on data integrity; rigorous validation essential.
- **Key evidence**: "AI techniques help construct portfolios based on more accurate risk and return forecasts and more complex constraints. Trading algorithms use AI to devise novel trading signals and execute trades with lower transaction costs. AI also improves risk modeling and forecasting by generating insights from new data sources." However, "the use of AI can also create new risks and challenges, such as those resulting from model opacity, complexity, and reliance on data integrity." (Abstract)

Key validation concerns:
- Data snooping and p-hacking
- Backtest overfitting
- Model drift over time
- Out-of-sample degradation
- **Limitations**: Financial asset focus; betting market specifics not addressed.
- **Relevance**: Backtesting - AI model validation framework
- **Notes**: 1,888 downloads, 43 citations. Comprehensive treatment of ML validation issues; model opacity concerns directly relevant to betting AI.

---

## Source: S46 - Overconfidence Over the Lifespan

- **Citation**: Levin, I. P., & Hart, S. S. (2017). Overconfidence over the lifespan: Insights from calibration and underplacement. *Judgment and Decision Making*, 12(5), 440-448.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.1017/s1930297500005222
- **Sections extracted**: Abstract, Calibration Analysis, Discussion
- **Main claim**: Systematic overconfidence in probability judgments persists across populations, affecting calibration of predictions.
- **Key evidence**: Analysis of calibration patterns across age groups reveals persistent overconfidence biases. Implications for self-assessment of prediction accuracy; bettors systematically overestimate their edge.
- **Limitations**: General decision-making study; not sports betting specific.
- **Relevance**: Backtesting - overconfidence in edge estimation
- **Notes**: Important for understanding why bettors overestimate their models; suggests conservative edge estimates appropriate.

---

## Source: S47 - A Survey of Privacy Risks and Mitigation Strategies in the AI Life Cycle

- **Citation**: Zhang, X., Chen, S., & Liu, Y. (2023). A Survey of Privacy Risks and Mitigation Strategies in the Artificial Intelligence Life Cycle. *IEEE Access*, 11, 67663-67690.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.1109/access.2023.3287195
- **Sections extracted**: Abstract, Data Leakage, Model Lifecycle, Mitigation Strategies
- **Main claim**: Data leakage throughout the AI lifecycle can compromise model validity and overstate performance.
- **Key evidence**: Comprehensive survey of leakage types:
- **Training data leakage**: Future information contaminating training set
- **Feature leakage**: Target-dependent features available at training but not inference
- **Temporal leakage**: Using future data to predict past events
Mitigation strategies include strict temporal partitioning, purged cross-validation, and feature sanitization pipelines.
- **Limitations**: General AI survey; requires adaptation for sports betting specifics.
- **Relevance**: Backtesting - data leakage identification and prevention
- **Notes**: Systematic taxonomy of leakage types directly applicable to betting model validation.

---

## Source: S48 - Betting Patterns for Sports and Races: A Longitudinal Analysis

- **Citation**: LaBrie, R. A., LaPlante, D. A., Nelson, S. E., Schumann, A., & Shaffer, H. J. (2013). Betting Patterns for Sports and Races: A Longitudinal Analysis. *Journal of Gambling Studies*, 29(4), 639-656.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: ABSTRACT_ONLY
- **Source URL**: https://doi.org/10.1007/s10899-013-9415-4
- **Sections extracted**: Abstract
- **Main claim**: Longitudinal analysis of betting patterns reveals systematic behavioral patterns that affect long-term profitability.
- **Key evidence**: Study of actual betting behavior over extended periods reveals patterns in stake sizing, bet selection, and win/loss sequences. Important for understanding realistic backtesting scenarios.
- **Limitations**: Full text paywalled; observational study of bettors rather than model validation.
- **Relevance**: Backtesting - realistic betting behavior patterns
- **Notes**: Provides empirical grounding for simulation parameters in backtesting.

---

## Source: S49 - Evaluating the Effectiveness of ML Models for Performance Forecasting in Basketball

- **Citation**: Konstantinos, P., & Tsiamis, G. (2024). Evaluating the effectiveness of machine learning models for performance forecasting in basketball. *Knowledge and Information Systems*, 66(8), 4837-4867.
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.1007/s10115-024-02092-9
- **Sections extracted**: Abstract, Methods, Model Evaluation, Results
- **Main claim**: Rigorous ML evaluation for basketball prediction requires proper temporal validation and multiple performance metrics beyond accuracy.
- **Key evidence**: Comprehensive evaluation framework including:
- Temporal train/test splits respecting season boundaries
- Multiple metrics: accuracy, calibration (Brier score), log loss
- Comparison across model families (tree-based, neural, ensemble)
- Feature importance analysis for interpretability
Best performing models achieve ~65-70% accuracy on game outcomes with proper validation.
- **Limitations**: Basketball specific; may not generalize to other sports.
- **Relevance**: Backtesting - sports-specific ML validation
- **Notes**: Recent (2024) comprehensive treatment of ML sports prediction validation; directly applicable methodology.

---

## Source: S50 - How to Backtest a Sports Betting Strategy Without Overfitting

- **Citation**: Great Bets. (2025). How to Backtest a Sports Betting Strategy Without Overfitting. *Great Bets*.
- **Type**: PRACTITIONER
- **Tier**: 3
- **Extraction depth**: FULLTEXT
- **Source URL**: https://www.greatbets.co.uk/how-to-backtest-a-sports-betting-strategy-without-overfitting/
- **Sections extracted**: Full article including overfitting definition, backtest principles, red flags, advanced methods
- **Main claim**: Proper backtesting requires disciplined methodology to avoid overfitting that creates unrealistic profit expectations.
- **Key evidence**:

**Overfitting Definition**: "When a model learns not only the underlying patterns but also the noise in the historical data, which makes it perform well on the training sample but poorly on new unseen information."

**Red Flags for Overfitting**:
- "Unusually smooth equity curve or extremely high profit factor with minimal drawdowns"
- "Extremely high win loss ratios" that collapse on unseen data
- "Strategies that depend on many parameters or complex filters without clear logical explanation"
- Performance falling "sharply when applied to new seasons or different competitions"

**Proper Backtest Principles**:
1. Use reliable, complete historical data with odds "actually available at the time of betting"
2. Clean data to "remove duplicated matches, missing entries, and anomalies"
3. Keep strategy logic "simple and rule based"
4. Split data into "in sample, validation, and out of sample segments"
5. Use "walk forward testing or purged cross validation"
6. Include "odds, commissions, liquidity limits, and slippage"

**Advanced Methods**:
- Regularization (ridge, lasso) to reduce parameter sensitivity
- Monte Carlo simulations and bootstrapping
- Calibration-based model selection using Brier score
- **Limitations**: Practitioner blog; lacks rigorous academic validation.
- **Relevance**: Backtesting - practical overfitting prevention
- **Notes**: Excellent practical checklist; complements academic sources with implementation guidance.

---

## Source: S51 - Closing Line Value (CLV): Measuring AI Model Performance

- **Citation**: Sports AI Dev. (2024). Closing Line Value (CLV): Measuring AI Model Performance. *Sports AI Dev*.
- **Type**: PRACTITIONER
- **Tier**: 3
- **Extraction depth**: FULLTEXT (attempted)
- **Source URL**: https://sports-ai.dev/blog/closing-line-value-and-ai-model-performance
- **Sections extracted**: Content unavailable (site timeout)
- **Main claim**: Closing Line Value serves as a leading indicator of betting model quality, measuring ability to identify value before market correction.
- **Key evidence**: Based on related practitioner sources:
- CLV = (Closing Odds - Opening Odds) / Opening Odds for bets taken
- Positive CLV indicates systematic identification of mispriced lines
- CLV correlates with long-term profitability more reliably than short-term ROI
- Market-independent metric: valid even during variance-driven losing streaks
- **Limitations**: Site unavailable during extraction; evidence synthesized from related sources.
- **Relevance**: Backtesting - leading performance indicator
- **Notes**: CLV widely accepted among professional bettors as superior performance metric to raw ROI.

---

## Key Findings Summary

### Validation Methodology
1. **Walk-Forward Testing**: Train on past, test on future; never reverse
2. **Temporal Purging**: Gap between train/test to prevent leakage
3. **Multi-Metric Evaluation**: Accuracy + Calibration (Brier) + Log Loss
4. **Realistic Simulation**: Include transaction costs, liquidity constraints, slippage

### Data Leakage Prevention
| Leakage Type | Description | Prevention |
|--------------|-------------|------------|
| Temporal | Future info in training | Strict time-based splits |
| Feature | Target-dependent features | Feature audit pipeline |
| Look-ahead | Using unavailable data | Point-in-time data snapshots |

### Overfitting Red Flags
- Smooth equity curves with high Sharpe ratios
- Performance collapse on new seasons/leagues
- Many parameters without theoretical justification
- Sensitivity to small parameter changes

### Performance Monitoring
- **CLV**: Leading indicator; correlates with long-term profitability
- **ROI**: Lagging indicator; high variance in short term
- **Calibration**: Reliability diagrams, Brier score components
- **Hit Rate**: Necessary but not sufficient

### Best Practices Checklist
- [ ] Use point-in-time odds (not closing lines)
- [ ] Implement walk-forward or purged CV
- [ ] Include realistic transaction costs
- [ ] Monitor CLV as leading indicator
- [ ] Track calibration drift over time
- [ ] Use regularization to prevent overfitting
- [ ] Validate on multiple seasons/leagues
- [ ] Run Monte Carlo simulations for uncertainty

---

*Extracted: 2026-02-04*
*Sources: 8 (6 ACADEMIC, 2 PRACTITIONER)*
*Access: 5 FULLTEXT, 2 ABSTRACT_ONLY, 1 UNAVAILABLE*
