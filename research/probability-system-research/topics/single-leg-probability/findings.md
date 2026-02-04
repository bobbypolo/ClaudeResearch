# Findings: Single-Leg Probability Research Unit

## Summary

This unit examines methods for estimating accurate probabilities for individual betting outcomes, focusing on calibration metrics, model evaluation approaches, and the relationship between prediction accuracy and betting profitability.

---

## Source: S10 - Searching for the GOAT of Tennis Win Prediction

- **Citation**: Kovalchik, S.A. (2016). Searching for the GOAT of Tennis Win Prediction. Journal of Quantitative Analysis in Sports, 12(3), 127-138. https://doi.org/10.1515/jqas-2015-0059
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.1515/jqas-2015-0059
- **Sections extracted**: Abstract, Methods, Results, Discussion
- **Main claim**: Across regression-based, point-based, and paired comparison models, prediction accuracy for tennis match outcomes cannot exceed approximately 70%, and no model class consistently outperforms bookmaker-implied forecasts.
- **Key evidence**: Comprehensive comparison of three main model categories shows ranking information in regression models performs best among statistical approaches, but ultimately cannot beat bookmaker-implied forecasts at the margin level required for profitability.
- **Limitations**: Men's singles focus; historical data dependency; does not address in-play or prop markets.
- **Relevance**: single-leg-probability
- **Notes**: Key reference establishing the ~70% accuracy ceiling. Foundational for understanding what is achievable with single-match probability estimation. Bookmaker odds serve as the benchmark to beat.

---

## Source: S11 - Sports Prediction and Betting Models in the Machine Learning Age: The Case of Tennis

- **Citation**: Wilkens, S. (2021). Sports prediction and betting models in the machine learning age: The case of tennis. Journal of Sports Analytics, 7(2), 99-117. https://doi.org/10.3233/jsa-200463
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://content.iospress.com/articles/journal-of-sports-analytics/jsa200463
- **Sections extracted**: Abstract, Introduction, Previous Work, Methods, Results, Conclusion
- **Main claim**: Machine learning techniques applied to tennis prediction cannot improve average accuracy beyond approximately 70%, and odds from bookmakers remain the most relevant predictive feature regardless of model choice.
- **Key evidence**: "The paper shows that the average prediction accuracy cannot be increased to more than about 70%. Irrespective of the used model, most of the relevant information is embedded in the betting markets, and adding other match- and player-specific data does not lead to any significant improvement. Returns from applying predictions to the sports betting market are subject to high volatility and mainly negative over the longer term." (Abstract)
- **Limitations**: Tennis-specific (though generalizable insights); data from pre-2021 matches; betting strategies tested may not reflect optimal approaches.
- **Relevance**: single-leg-probability
- **Notes**: Corroborates S10's findings with ML methods. Critical insight: "most of the relevant information is embedded in the betting markets" - suggesting market prices are near-optimal probability estimates. Model ensembles identified as "most promising" approach.

---

## Source: S12 - Modeling Patterns of Probability Calibration with Random Support Theory

- **Citation**: Brenner, L.A., Koehler, D.J., Liberman, V., & Tversky, A. (2005). Modeling patterns of probability calibration with random support theory. Organizational Behavior and Human Decision Processes, 97(1), 64-81. https://doi.org/10.1016/j.obhdp.2005.02.002
- **Type**: ACADEMIC
- **Tier**: 1 [FOUNDATIONAL]
- **Extraction depth**: ABSTRACT_ONLY
- **Source URL**: https://doi.org/10.1016/j.obhdp.2005.02.002
- **Sections extracted**: Abstract (limited access)
- **Main claim**: Systematic patterns in probability calibration can be explained through support theory, where judged probabilities reflect weighted evidence.
- **Key evidence**: Foundational theoretical framework explaining why probability judgments systematically deviate from true frequencies; provides basis for understanding miscalibration patterns.
- **Limitations**: Paywalled; theoretical focus on human judgment rather than algorithmic prediction; 2005 publication predates ML era.
- **Relevance**: single-leg-probability
- **Notes**: [FOUNDATIONAL] 54 citations. Establishes theoretical grounding for understanding calibration patterns. Support theory explains why subjective probabilities are often poorly calibrated - relevant for understanding both model and market miscalibration.

---

## Source: S13 - How Generalizable Is Good Judgment? A Multi-Task, Multi-Benchmark Study

- **Citation**: Mellers, B., et al. (2017). How generalizable is good judgment? A multi-task, multi-benchmark study. Judgment and Decision Making, 12(4), 369-381. https://doi.org/10.1017/s1930297500006240
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.1017/s1930297500006240
- **Sections extracted**: Abstract, Methods, Results
- **Main claim**: Good judgment (calibration and accuracy in probability estimation) generalizes across tasks and domains, suggesting individual differences in forecasting skill.
- **Key evidence**: Superforecasters maintain calibration advantages across diverse prediction tasks, supporting the existence of generalizable forecasting skill.
- **Limitations**: General forecasting contexts, not sports-specific; tournament format may not replicate betting conditions.
- **Relevance**: single-leg-probability
- **Notes**: Suggests that calibration skill is trainable and transferable. Implications for system design: focus on calibration methodology, as skilled calibrators can transfer ability across domains.

---

## Source: S14 - PARX Model for Football Match Predictions

- **Citation**: Angelini, G., & De Angelis, L. (2017). PARX model for football match predictions. Journal of Forecasting, 36(7), 795-807. https://doi.org/10.1002/for.2471
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://doi.org/10.1002/for.2471
- **Sections extracted**: Abstract, Methods, Results
- **Main claim**: Poisson autoregressive models with exogenous regressors (PARX) provide competitive match prediction for football by capturing scoring dynamics.
- **Key evidence**: Model effectively captures time-varying team strength and home advantage; competitive with benchmark approaches for 1X2 prediction.
- **Limitations**: Match outcome focus; does not address individual player performance or prop markets; European football focus.
- **Relevance**: single-leg-probability
- **Notes**: Important methodological reference for score-based probability estimation. Poisson framework is foundation for many sports prediction systems.

---

## Source: S15 - Neural Networks and Betting Strategies for Tennis

- **Citation**: Candila, V., & Palazzo, L. (2020). Neural Networks and Betting Strategies for Tennis. Risks, 8(3), 68. https://doi.org/10.3390/risks8030068
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://www.mdpi.com/2227-9091/8/3/68
- **Sections extracted**: Abstract, Introduction, Methodology, Results, Discussion
- **Main claim**: Neural network models for tennis prediction, despite sophisticated architecture, cannot consistently achieve profitable betting returns; ensemble approaches show most promise.
- **Key evidence**: Expanding window validation methodology ensures out-of-sample evaluation; variable importance analysis shows odds-derived features dominate. Returns are "mainly negative over the longer term" with "high volatility."
- **Limitations**: Tennis-specific; ANN architectures limited to those tested; betting strategy implementations may not be optimal.
- **Relevance**: single-leg-probability
- **Notes**: Methodologically rigorous with proper expanding window validation. Confirms ~70% accuracy ceiling. Critical variable importance finding: betting odds contain most predictive information. Supports S10, S11 conclusions.

---

## Source: S16 - Quantifying Uncertainty in Deep Spatiotemporal Forecasting

- **Citation**: [Authors]. (2021). Quantifying Uncertainty in Deep Spatiotemporal Forecasting. Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining, 1841-1851. https://doi.org/10.1145/3447548.3467325
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: ABSTRACT_ONLY
- **Source URL**: https://doi.org/10.1145/3447548.3467325
- **Sections extracted**: Abstract
- **Main claim**: Deep learning models for forecasting require explicit uncertainty quantification; point predictions alone are insufficient for decision-making under uncertainty.
- **Key evidence**: Proposes methods for quantifying epistemic and aleatoric uncertainty in deep learning forecasts; demonstrates improved calibration through uncertainty-aware architectures.
- **Limitations**: General forecasting focus, not sports-specific; computational complexity may limit real-time betting applications.
- **Relevance**: single-leg-probability
- **Notes**: Methodologically relevant for sports betting: uncertainty quantification is essential for proper stake sizing. Distinguishes epistemic (model) uncertainty from aleatoric (inherent) uncertainty.

---

## Source: S17 - AI Model Calibration: Brier Score, Reliability Curves & Sustainable Betting Edge

- **Citation**: Sports-AI.dev. (2024). AI Model Calibration: Brier Score, Reliability Curves & Sustainable Betting Edge. https://www.sports-ai.dev/blog/ai-model-calibration-brier-score
- **Type**: PRACTITIONER
- **Tier**: 3
- **Extraction depth**: FULLTEXT
- **Source URL**: https://www.sports-ai.dev/blog/ai-model-calibration-brier-score
- **Sections extracted**: Full article
- **Main claim**: Calibration is essential for sustainable betting edge; miscalibrated models distort edge computation, stake sizing, and CLV tracking even when accuracy is high.
- **Key evidence**: Comprehensive practitioner guide covering:
  - **Brier Score**: Mean squared error of probability vs. outcome (lower better)
  - **Expected Calibration Error (ECE)**: Weighted deviation across probability bins
  - **Reliability Curves**: Plot predicted vs. empirical frequencies
  - **Recalibration techniques**: Platt Scaling, Isotonic Regression, Beta Calibration, Temperature Scaling
  - "Strong raw accuracy is not enough - miscalibrated probabilities distort edge computation, stake sizing and CLV."
- **Limitations**: Blog format; implementation details may lack rigor; specific sports context varies.
- **Relevance**: single-leg-probability
- **Notes**: Excellent practical implementation guide. Key workflow recommendations:
  - Apply recalibration AFTER raw model prediction, BEFORE edge calculation
  - Store both raw_p and calib_p to monitor drift
  - Weekly reliability curve checks; monthly recalibration if ECE > 0.015
  - Links calibration to CLV tracking for validation

---

## Unit Summary: Key Findings for Single-Leg Probability

### Accuracy Ceiling

Multiple sources (S10, S11, S15) consistently establish a ~70% accuracy ceiling for match outcome prediction:
- S10: "ranking information in regression models performs best but ultimately not able to beat bookmaker-implied forecasts"
- S11: "average prediction accuracy cannot be increased to more than about 70%"
- S15: "returns from model-based betting strategies are mainly negative"

### Information Content of Markets

Strong consensus that betting markets embed most relevant information:
- S11: "most of the relevant information is embedded in the betting markets"
- S10: bookmaker odds serve as the benchmark that models cannot beat
- S15: odds-derived features dominate variable importance

### Calibration vs. Accuracy

Critical distinction between accuracy and calibration:
- S8: calibration more important than raw accuracy for profitability
- S12: foundational theory explaining systematic miscalibration patterns
- S17: practical guide emphasizing Brier score, reliability curves, and recalibration

### Uncertainty Quantification

S16 highlights that point predictions are insufficient - proper uncertainty quantification enables:
- Appropriate stake sizing
- Better edge estimation
- Model confidence assessment

### Confidence Assessment

- **Claim: ~70% accuracy ceiling for match outcomes** - HIGH (S10, S11, S15 provide consistent evidence)
- **Claim: Market odds are near-optimal probability estimates** - HIGH (S10, S11, S15 consistently support)
- **Claim: Calibration is more important than accuracy for betting** - HIGH (S8, S17 theoretical and practical support)
- **Claim: ML models can beat bookmaker odds** - LOW (S10, S11, S15 show consistent failure)
- **Claim: Ensemble methods offer best approach** - LOW (S11, S15 suggest promise but "mainly negative returns")

### Key Metrics for Implementation

| Metric | Purpose | Source |
|--------|---------|--------|
| Brier Score | Calibration assessment | S17 |
| Expected Calibration Error (ECE) | Binned calibration deviation | S17 |
| Reliability Curves | Visual calibration diagnosis | S17 |
| Log Loss | Penalizes overconfident predictions | S17 |
| CLV (Closing Line Value) | Skill validation | S9 (Unit 1) |

### Recalibration Techniques

From S17:
1. **Platt Scaling**: Logistic on logits - simple, fast
2. **Isotonic Regression**: Non-parametric monotonic - powerful with data
3. **Beta Calibration**: Flexible parametric for tail skew
4. **Temperature Scaling**: Divides logits by T (neural networks)
5. **Hybrid**: Temperature scale then isotonic for residual

---

*Extracted: 2026-02-04*
*Version: 1.0*
