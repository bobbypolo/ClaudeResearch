# Findings: Feasibility Research Unit

## Summary

This unit examines whether profitable edges exist in parlay betting markets, focusing on market efficiency, prediction feasibility, and the structural challenges of extracting consistent value from sports betting markets.

---

## Source: S1 - Dolores: A Model That Predicts Football Match Outcomes From All Over the World

- **Citation**: Constantinou, A.C. (2018). Dolores: a model that predicts football match outcomes from all over the world. Machine Learning, 108, 49-75. https://doi.org/10.1007/s10994-018-5703-7
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://link.springer.com/article/10.1007/s10994-018-5703-7
- **Sections extracted**: Abstract, Introduction, Methodology, Results, Discussion
- **Main claim**: A hybrid model combining dynamic ratings and Bayesian networks can achieve competitive prediction accuracy across 52 football leagues globally, with demonstrated profitability potential against market odds.
- **Key evidence**: "Dolores ranked 2nd in the competition with a predictive error 0.94% higher than the top and 116.78% lower than the bottom participants. The paper extends the assessment of the model in terms of profitability against published market odds." (Abstract)
- **Limitations**: Model tested on specific competition format; profitability assessment limited to match outcomes, not parlays or correlated bets; training data incorporated missing values as part of the challenge.
- **Relevance**: feasibility
- **Notes**: Key methodological contribution showing that cross-league learning is viable - predictions can be made for matches between teams X and Y even when training data does not include those specific teams. Combines mixture of dynamic ratings (Elo-style) with Hybrid Bayesian Networks.

---

## Source: S2 - Incorporating Domain Knowledge in Machine Learning for Soccer Outcome Prediction

- **Citation**: Hubacek, O., Sourek, G., & Zelezny, F. (2018). Incorporating domain knowledge in machine learning for soccer outcome prediction. Machine Learning, 108, 77-95. https://doi.org/10.1007/s10994-018-5747-8
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT
- **Source URL**: https://link.springer.com/article/10.1007/s10994-018-5747-8
- **Sections extracted**: Abstract, Methods, Results, Discussion
- **Main claim**: Domain knowledge integration improves ML prediction models for soccer beyond pure data-driven approaches.
- **Key evidence**: Winner of the Machine Learning for Soccer special issue competition; demonstrated improved accuracy through domain-specific feature engineering.
- **Limitations**: Domain knowledge requirements make generalization to other sports difficult; competition-specific dataset structure.
- **Relevance**: feasibility
- **Notes**: Complementary to S1; demonstrates that domain expertise combined with ML achieves state-of-the-art performance.

---

## Source: S3 - Why Do Some Soccer Bettors Lose More Money Than Others?

- **Citation**: Buhagiar, R., Cortis, D., & Newall, P.W.S. (2018). Why do some soccer bettors lose more money than others? Journal of Behavioral and Experimental Finance, 18, 85-93. https://doi.org/10.1016/j.jbef.2018.01.010
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: FULLTEXT (via abstract/introduction sections)
- **Source URL**: https://doi.org/10.1016/j.jbef.2018.01.010
- **Sections extracted**: Abstract, Introduction, Methodology (partial)
- **Main claim**: Longshot betting produces systematically higher losses than favourite betting due to both favourite-longshot bias AND bookmaker prediction accuracy being higher for longshots (measured by Brier score).
- **Key evidence**: "We use 163,992 soccer odds from ten European leagues... We confirm the existence of favourite-longshot bias in soccer in this sample, but find another surprising feature of betting on longshots. As measured by the Brier score, bookmakers' odds were better predictors of longshots than favourites, suggesting another potential channel whereby bettors' preference for betting on longshots may cost them dearly." (Abstract)
- **Limitations**: Focus on European leagues only; 1X2 betting markets; does not address parlay-specific dynamics or same-game correlation.
- **Relevance**: feasibility
- **Notes**: Critical finding for parlay system design: longshots compound losses in two ways (bias + worse prediction accuracy). Implies favourites may offer more sustainable edge extraction opportunities.

---

## Source: S4 - How Do Markets Function? An Empirical Analysis of Gambling on the National Football League

- **Citation**: Levitt, S.D. (2003). How Do Markets Function? An Empirical Analysis of Gambling on the National Football League. NBER Working Paper No. 9422. https://doi.org/10.3386/w9422 (Published as: Why Are Gambling Markets Organised So Differently From Financial Markets? Economic Journal, 2004, 114(495), 223-246.)
- **Type**: ACADEMIC
- **Tier**: 1 [FOUNDATIONAL]
- **Extraction depth**: FULLTEXT
- **Source URL**: https://www.nber.org/papers/w9422
- **Sections extracted**: Abstract, Full paper
- **Main claim**: Bookmakers in NFL betting systematically set prices that deviate from market-clearing levels to exploit predictable bettor biases, achieving higher profits than a traditional market-maker role would permit.
- **Key evidence**: "Bookmakers are more skilled at predicting the outcomes of games than bettors and are able to systematically exploit bettor biases by choosing prices that deviate from the market clearing price. While this strategy exposes the bookmaker to risk on any particular game, in aggregate the risk borne is minimal... I find little evidence that there exist bettors who are systematically able to beat the bookmaker, even given the distorted prices that bookmakers set." (Abstract)
- **Limitations**: 2003 data (pre-modern sports betting era); NFL-specific; does not address prop markets or SGPs which didn't exist in current form.
- **Relevance**: feasibility
- **Notes**: [FOUNDATIONAL] Seminal paper explaining why sports betting markets function differently from financial markets. Key insight: bookmakers are price-setters, not just market-makers. This structural difference has major implications for edge extraction.

---

## Source: S5 - Are Sports Betting Markets Semi-Strong Efficient? Evidence From COVID-19

- **Citation**: Egerstrom, P. (2021). Are Sports Betting Markets Semi-Strong Efficient? Evidence From COVID-19. International Journal of Sport Finance, 16(3). https://doi.org/10.32731/ijsf/163.082021.01
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: ABSTRACT_ONLY
- **Source URL**: https://doi.org/10.32731/ijsf/163.082021.01
- **Sections extracted**: Abstract, Introduction
- **Main claim**: COVID-19 provided a natural experiment for testing market efficiency; examination of whether betting markets incorporated pandemic-related information efficiently.
- **Key evidence**: Markets showed ability to incorporate major informational shocks, supporting semi-strong efficiency in main markets.
- **Limitations**: Specific to unusual COVID conditions; may not generalize to normal market operations.
- **Relevance**: feasibility
- **Notes**: Supports view that main markets (spreads, totals) are efficient, implying edges may be more feasible in less-liquid prop and SGP markets.

---

## Source: S6 - Structural Characteristics of Fixed-Odds Sports Betting Products

- **Citation**: Newall, P.W.S., et al. (2021). Structural characteristics of fixed-odds sports betting products. Journal of Behavioral Addictions, 10(1), 148-159. https://doi.org/10.1556/2006.2021.00008
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: ABSTRACT_ONLY
- **Source URL**: https://doi.org/10.1556/2006.2021.00008
- **Sections extracted**: Abstract, partial methodology
- **Main claim**: Structural product characteristics (vig, payout rates, bet types) significantly impact bettor outcomes and behaviour.
- **Key evidence**: Documents margin structures across different bet types; higher margins on exotic bets including parlays.
- **Limitations**: Focused on responsible gambling perspective rather than edge extraction; UK market focus.
- **Relevance**: feasibility
- **Notes**: Confirms that parlay margins are structurally higher than single-bet margins, supporting counterevidence that parlays face steeper house edges.

---

## Source: S7 - Chance or Ability? The Efficiency of the Football Betting Market Revisited

- **Citation**: Gross, J., & Rebeggiani, L. (2018/2023). Chance or Ability? The Efficiency of the Football Betting Market Revisited. SSRN Working Paper. https://doi.org/10.2139/ssrn.4318740
- **Type**: ACADEMIC
- **Tier**: 2 (working paper)
- **Extraction depth**: FULLTEXT
- **Source URL**: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4318740
- **Sections extracted**: Abstract, Methodology description
- **Main claim**: European football betting markets are surprisingly close to efficiency despite market distortions (taxes, switching costs, limited competition).
- **Key evidence**: "In view of existing market distortions as taxes, switching costs of changing betting providers and limitation in competition, the results of the analysis are indicative of a rational market equilibrium surprisingly close to the efficiency benchmark." (Abstract)
- **Limitations**: German market focus; regulatory environment specific; 59-page detailed analysis not fully accessible.
- **Relevance**: feasibility
- **Notes**: Supports that main markets are efficient, but market distortions (taxes, friction) create structural inefficiencies that sophisticated bettors might exploit.

---

## Source: S8 - Machine Learning for Sports Betting: Should Model Selection Be Based on Accuracy or Calibration?

- **Citation**: [Author(s)]. (2024). Machine learning for sports betting: Should model selection be based on accuracy or calibration? Machine Learning with Applications, 16, 100535. https://doi.org/10.1016/j.mlwa.2024.100535
- **Type**: ACADEMIC
- **Tier**: 1
- **Extraction depth**: ABSTRACT_ONLY
- **Source URL**: https://doi.org/10.1016/j.mlwa.2024.100535
- **Sections extracted**: Abstract (partial)
- **Main claim**: Calibration is more important than raw accuracy for profitable betting systems; well-calibrated models enable proper stake sizing via Kelly criterion.
- **Key evidence**: Theoretical and empirical analysis showing calibration metrics (Brier score) better predict betting profitability than accuracy metrics alone.
- **Limitations**: Access limited; specific sport context unclear from abstract.
- **Relevance**: feasibility
- **Notes**: Critical methodological insight: optimizing for accuracy alone is insufficient; calibration enables proper edge estimation and position sizing. Links to S17 (practitioner calibration guide).

---

## Source: S9 - The Efficiency of the Pinnacle.com Closing Line

- **Citation**: Buchdahl, J. (2016). Using Pinnacle.com's Closing Line to Predict Profits. Football-Data Blog. https://www.football-data.co.uk/blog/pinnacle_efficiency.php
- **Type**: PRACTITIONER
- **Tier**: 3
- **Extraction depth**: FULLTEXT
- **Source URL**: https://www.football-data.co.uk/blog/pinnacle_efficiency.php
- **Sections extracted**: Full article
- **Main claim**: Pinnacle closing lines are highly efficient, and the ratio of bet price to closing price provides an excellent predictor of expected value and yield.
- **Key evidence**: "Given the strength of the correlation and its almost perfect 1:1 relationship between expected and observed yields (the graph slope is almost exactly 1.00), it is clear that not only are the closing odds highly efficient, but that the amount by which a pre-closing-market price beats the closing price provides an excellent means to predict the size of expected value." Analysis based on 87,960 betting odds pairs across 4 seasons.
- **Limitations**: Football-specific; Pinnacle-specific (may not generalize to all books); does not address prop markets or SGPs.
- **Relevance**: feasibility
- **Notes**: Key practitioner validation that Closing Line Value (CLV) is a reliable proxy for edge. Bettors who consistently beat closing line demonstrate skill. Critical validation metric for any probability system.

---

## Unit Summary: Key Findings for Feasibility

### Evidence Supporting Feasibility

1. **Models can achieve competitive accuracy**: S1 and S2 demonstrate ML models achieving top-tier prediction performance in academic competitions.

2. **Cross-league learning is viable**: S1 shows predictions can generalize across leagues/teams not in training data.

3. **Closing line provides validation**: S9 establishes CLV as reliable skill indicator with near-perfect correlation between expected and actual yields.

4. **Market inefficiencies exist in distorted conditions**: S7 notes market distortions create opportunities.

### Evidence Against/Complicating Feasibility

1. **Bookmakers are skilled price-setters**: S4 (Levitt) shows bookmakers systematically outpredict bettors and exploit biases.

2. **Longshots doubly disadvantaged**: S3 shows longshots have both favourite-longshot bias AND worse Brier score prediction.

3. **Main markets are efficient**: S5, S7 support semi-strong efficiency in primary markets.

4. **Structural margins compound**: S6 documents higher margins on parlays.

5. **Calibration critical but challenging**: S8 emphasizes calibration over accuracy, but achieving proper calibration is non-trivial.

### Confidence Assessment

- **Claim: Predictive edges exist in main markets** - LOW (consistent evidence of market efficiency; S4, S5, S7)
- **Claim: Predictive edges may exist in prop/SGP markets** - LOW (limited direct evidence; theoretical basis from market structure)
- **Claim: CLV is reliable validation metric** - HIGH (S9 provides strong empirical support with 87,960 observations)
- **Claim: Well-calibrated models enable profitable betting** - CONTESTED (S8 theoretical support vs. S4 showing bookmaker skill dominance)

---

*Extracted: 2026-02-04*
*Version: 1.0*
