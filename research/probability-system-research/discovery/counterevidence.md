# Counterevidence Discovery Results

**Research Question Under Test:** Is it feasible to build a production-grade probability system for parlays that can produce calibrated true probabilities, estimate joint probabilities for parlays/SGPs under dependence, identify +EV parlay combinations, and validate advantage out-of-sample?

**Safety Gate B Status:** COMPLETED
**Date:** 2026-02-04
**Preset:** thorough

---

## Category: Market Efficiency Challenges

| # | Title | Source | Year | Key Argument |
|---|-------|--------|------|--------------|
| CE1 | Statistical and Economic Tests of Efficiency in the English Premier League Soccer Betting Market | Brycki, J. (Dissertation, U. Sydney) | 2009 | Weak form efficiency tests show favourite-longshot bias exists but is not sufficiently exploitable for profit after transaction costs; market increasingly efficient over time |
| CE2 | Abnormal Returns in an Efficient Market? Statistical and Economic Weak Form Efficiency of Online Sports Betting | Tiitu, T. (Aalto University) | 2016 | Most extensive dataset to date shows online soccer betting markets are statistically and economically weak-form efficient between 2009-2014 |
| CE3 | NFL Betting Market Efficiency: Finding a Profitable Betting Strategy | Anderson, S. (Skidmore College) | 2019 | OLS regression analysis finds no evidence of profitable strategy for hot hand, streaks, or prime-time betting; market efficiently prices most information |
| CE4 | The Efficient Market Hypothesis and Gambling on NFL Games | Sung, Y.T. (U. Illinois) | 2011 | Tests EMH for NFL 2002-2009; finds favourite-longshot bias exists but market is fair/efficient overall |
| CE5 | Introduction to Prices vs. Handicapping: Place and Show Anomalies | Hausch, Lo & Ziemba | 2008 | Seminal work documenting that while inefficiencies exist, they are not large enough for practical exploitation in most markets |

**Key Implication:** Academic evidence consistently shows betting markets are near-efficient. Edge detection systems must overcome transaction costs (vig) and diminishing returns as any discovered edge gets arbitraged away.

---

## Category: Parlay-Specific Risks

| # | Title | Source | Year | Key Argument |
|---|-------|--------|------|--------------|
| CE6 | Parlay Betting Math on House Edge | Reddit r/sportsbook | 2022 | Mathematical demonstration that house edge compounds from ~5% on singles to ~27.6% on parlays |
| CE7 | Sports Betting: Why Parlay Bets are for Suckers | CollegeFootballWinning | 2015 | Nevada actual house take on parlays 2008-2014 was **31.47%** vs 4.55% on non-parlay football bets |
| CE8 | Find Out What the House Edge is on Parlays | BetFirm | N/A | 3-team parlay: 12.50% edge; 4-team: 31.25%; 5-team: 34.38% house advantage |
| CE9 | The Math Behind Parlay Betting | Establish The Run | 2024 | NJ sportsbooks held 19.9% on parlays in Jan 2024; if you win 50% at -110, parlaying compounds loss from -4.6% to -9% ROI |
| CE10 | Parlay Betting Explained | BettorEdge | 2025 | House edge on parlays at traditional sportsbooks approaches 16%; each additional leg compounds disadvantage |

**Key Implication:** Parlay mathematics fundamentally disadvantage bettors. Even with an edge on individual legs, the compounding effect requires significantly higher accuracy to overcome the structural house advantage.

---

## Category: Same-Game Parlay (SGP) Correlation Issues

| # | Title | Source | Year | Key Argument |
|---|-------|--------|------|--------------|
| CE11 | Same-Game Parlays: The Mathematics of Correlation | Wizard of Odds | 2025 | Positive correlation means true joint probability is higher than independence assumption; sportsbooks offer shorter odds to compensate, creating a "correlation tax" |
| CE12 | Same Game Parlay Correlation: How the Hidden Tax on SGPs Really Works | OddsIndex | 2025 | Documents the "hidden vig" - sportsbooks offer significantly lower odds than naive parlay calculators when legs are positively correlated |
| CE13 | Correlation in Same Game Parlays: How Sportsbooks are Tackling... | OpticOdds | 2025 | Accurately pricing SGP correlation is computationally complex; underestimation creates risk but overestimation protects book profit |
| CE14 | The Hidden Risk of Same Game Parlays | YouTube (FanDuel/DraftKings) | 2024 | Sportsbooks control the juice behind the scenes; positive correlation systematically hurts bettor expected value |
| CE15 | What the Sportsbooks Aren't Telling You About SGPs | YouTube | 2025 | SGPs are one of the most profitable products for sportsbooks; potentially one of the worst bets for bettors |
| CE16 | SGP Engine by OpticOdds | OpticOdds | 2025 | Commercial tools use "advanced analytics and real-time modeling" to manage correlations dynamically - bettors compete against sophisticated proprietary systems |

**Key Implication:** Modeling SGP correlations correctly is the core challenge. Sportsbooks have invested heavily in correlation pricing engines; bettors face an information/compute asymmetry. The copula-based approach in the research faces real-world competition from well-resourced book algorithms.

---

## Category: Model/Technical Limitations

| # | Title | Source | Year | Key Argument |
|---|-------|--------|------|--------------|
| CE17 | Information Leakage in Backtesting | SSRN #3836631 | 2022 | Information leakage causes significant overestimation of out-of-sample performance; randomized splits fail with time series data |
| CE18 | How to Backtest a Sports Betting Strategy Without Overfitting | Great Bets UK | 2025 | Overfitting captures noise not signal; look-ahead bias from using unavailable odds common failure mode |
| CE19 | Overfitting & Data-Snooping in Backtests | Surmount AI | N/A | Models memorize historical quirks; strict temporal splits (walk-forward) and parameter freezing essential |
| CE20 | Backtest Overfitting in the Machine Learning Era | SSRN #4686376 | 2024 | CPCV method superior; Walk-Forward shows "increased temporal variability and weaker stationarity" - standard validation methods insufficient |
| CE21 | The Probability of Backtest Overfitting | Western Michigan U. | 2017 | Framework for Probability of Backtest Overfitting (PBO); standard hold-out methods unreliable for investment/betting backtests |
| CE22 | Backtest Overfitting and the Post-hoc Probability Fallacy | Math Investor | 2022 | Multiple hypothesis testing on same dataset creates spurious strategies; post-hoc probability calculations misleading |
| CE23 | 3 Subtle Ways Data Leakage Can Ruin Your Models | Machine Learning Mastery | 2025 | Target leakage, train-test contamination, and temporal leakage all cause models to appear better than reality |
| CE24 | Evaluating Betting Model Performance | BetBetter World | 2025 | Look-ahead bias (using post-close odds) is form of data leakage specific to betting backtests |

**Key Implication:** Out-of-sample validation is notoriously difficult in betting contexts. The research must demonstrate resistance to: (1) temporal leakage, (2) data snooping from multiple hypothesis testing, (3) look-ahead bias from odds availability, and (4) regime changes in market dynamics.

---

## Category: Practical/Implementation Challenges

| # | Title | Source | Year | Key Argument |
|---|-------|--------|------|--------------|
| CE25 | Why Do Most Sports Bettors Lose | BetAndBeat | 2022 | Systematic biases: chasing losses, emotional betting, insufficient research time, placing too many wagers |
| CE26 | 4% Of Online Gamblers Won Over 5-Year Period | GamblingHarm.org | 2024 | **Only 4% of bettors net positive over 5 years**; platforms actively limit/throttle winning accounts |
| CE27 | Why Do Sports Bettors Gamble Until They Lose | GamblingHarm.org | 2025 | Psychological traps: gambler's fallacy, illusion of skill, near-miss effect keep bettors engaged despite negative EV |
| CE28 | How Sportsbooks Identify Sharp Bettors | BetsBooster | N/A | CLV tracking, bet timing, price sensitivity lead to account limits/bans; first withdrawal often triggers review |
| CE29 | CLV Betting Guide | Sharp Football Analysis | 2025 | Beating closing line requires multiple accounts and early betting - operational complexity compounds |
| CE30 | What Is Closing Line Value | GamblingSite | 2025 | Sportsbooks **limit or ban bettors** who consistently beat closing line; sharp bettors face account restrictions |
| CE31 | Why Closing Line Value is a SCAM | The Lock Talk (Substack) | 2026 | CLV meaningless in low-liquidity markets, prop bets, and markets where key info post-dates close; prop limits hit quickly |
| CE32 | BetSharp Homepage | BetSharp | N/A | "Recreational sportsbooks like FanDuel often **restrict or ban sharp gamblers**" - operational reality for profitable bettors |
| CE33 | Why 95% of Sports Bettors Go BROKE | YouTube | 2025 | Bankroll management failure, not pick quality, is primary cause of ruin; variance underestimated |
| CE34 | Why Is Sports Betting Not Profitable | UnderdogChance | 2024 | Vig ensures house profit regardless of outcome; emotional decisions, poor bankroll management compound structural disadvantage |

**Key Implication:** Even with a theoretical edge, **practical implementation faces severe constraints**: account limits/bans, liquidity constraints, execution challenges, and psychological pressures. The 4% long-term winner statistic is sobering.

---

## Category: Kelly Criterion and Bankroll Risks

| # | Title | Source | Year | Key Argument |
|---|-------|--------|------|--------------|
| CE35 | Structures in Credit Risk Modelling | Tran, C.S. (QUT) | 2021 | Kelly criterion shifts from dichotomous classification to optimal allocation; edge estimation errors compound into ruin risk |
| CE36 | Ergodicity and You: Adaptive Heuristics | Zovas, J. (Penn) | 2019 | Life requires margin of safety from ruin; adaptive heuristics needed because non-ergodic environments don't allow recovery from total loss |
| CE37 | Leverage and Uncertainty | Turlakov, M. (SSRN) | 2017 | Uncertainty in edge estimates amplifies Kelly fraction variance; over-betting leads to ruin faster than under-betting leads to sub-optimal growth |

**Key Implication:** Kelly betting requires accurate edge estimates. If probability calibration or EV calculations contain systematic errors, Kelly sizing amplifies those errors into accelerated bankroll depletion.

---

## Category: Favorite-Longshot Bias and Probability Miscalibration

| # | Title | Source | Year | Key Argument |
|---|-------|--------|------|--------------|
| CE38 | Gender Behavior in Betting Markets | Muller et al. | 2011 | 5+ million NZ bets show favourite-longshot bias exists; betting sizes disproportionately decrease with odds |
| CE39 | Loss Aversion and Mental Accounting: The Favorite Longshot Bias | Qiu, J. (Max Planck) | 2007 | Behavioral economics explains systematic mispricing but doesn't imply exploitability after vig |
| CE40 | Fair Odds for Noisy Probabilities | Nash, U.W. (arXiv) | 2018 | When probability estimates are noisy, the "fair" odds differ from frequency-implied odds; FLB emerges from uncertainty |
| CE41 | Sonic Thunder vs Brian the Snail: Fast-sounding Racehorse Names | Merz, Flepp & Franck | 2019 | Markets incorporate irrelevant information (horse names); winning probabilities for "fast-sounding" names overstated |

**Key Implication:** Systematic biases exist in market-implied probabilities, but they are (1) well-documented, (2) partially priced in by sophisticated participants, and (3) may persist because they don't survive transaction costs.

---

## Category: Copula and Joint Probability Challenges

| # | Title | Source | Year | Key Argument |
|---|-------|--------|------|--------------|
| CE42 | Bivariate Copula-based Regression for Modeling Results of Football Matches | Ekman, R. (Lund University) | 2020 | Copula methods for football match modeling; challenges in parameter estimation and copula selection |
| CE43 | In-game Betting and the FA English Premier League: The Contribution of Prediction Models | Andersen & Hassel | 2019 | Bivariate models for live betting; notes dependence structure challenges in real-time prediction |
| CE44 | Joint Modelling of Two Count Variables | Osiewalski & Marzec | 2018 | Technical challenges in joint modeling when one variable can be degenerate; Bayesian inference complexity |

**Key Implication:** Copula-based joint probability estimation is technically sound but faces practical challenges: copula family selection, parameter estimation with limited data, and computational cost for real-time applications.

---

## Summary of Key Counterarguments

### 1. Market Efficiency Challenge
Academic evidence shows betting markets are near-efficient. Edges, if they exist, are small and likely to be arbitraged away once discovered. The claim that a system can "identify +EV parlay combinations" faces the reality that markets quickly incorporate new information.

### 2. Parlay House Edge Structure
Parlay mathematics fundamentally favor the house. Nevada data shows 31%+ house edge on parlays vs ~5% on singles. Even accurate probability estimation must overcome this structural disadvantage, which compounds multiplicatively.

### 3. SGP Correlation Pricing Arms Race
Sportsbooks invest heavily in correlation pricing engines. Bettors using naive copula models compete against sophisticated commercial systems (like OpticOdds' SGP Engine). The asymmetry in computational resources and real-time data access disadvantages independent modelers.

### 4. Backtesting Validity Concerns
Backtest overfitting is a documented problem across quantitative finance. Standard validation methods (train/test splits, k-fold) fail for time series data. The research must demonstrate CPCV or similar rigorous out-of-sample validation to claim edge persistence.

### 5. Account Limits and Operational Reality
**Only 4% of online bettors are net profitable over 5 years**, and winning bettors face account restrictions. Any system demonstrating profitability will quickly encounter limits at recreational sportsbooks, forcing migration to exchanges (Betfair) or professional books (Pinnacle) with lower margins.

### 6. Kelly Criterion Fragility
Kelly betting optimizes long-term growth but requires accurate edge estimation. Small errors in probability calibration or correlation modeling can convert Kelly from growth-optimal to ruin-accelerating.

### 7. Closing Line Value as Validation Metric
CLV is the industry standard for validating betting edge, but:
- Meaningless in low-liquidity prop markets
- Sharp bettors who achieve CLV get limited
- Line movements can be driven by public money, not sharp information

### 8. Psychological and Practical Implementation
Even with mathematical edge, behavioral factors (chasing losses, overconfidence after wins, insufficient patience) derail most systematic approaches. The 95% failure rate reflects implementation failure as much as edge absence.

---

## Risk Matrix for Research Claims

| Claim | Key Risk | Mitigation Required |
|-------|----------|---------------------|
| Calibrated true probabilities | Miscalibration in tails (longshots) | Demonstrate calibration curves across odds ranges |
| Joint probability estimation | Copula misspecification; correlation estimation error | Test multiple copula families; bootstrap confidence intervals |
| +EV identification | Overfitting; look-ahead bias; transaction costs | Walk-forward validation; account for realistic vig |
| Out-of-sample validation | Temporal leakage; regime change | CPCV methodology; multi-year holdout periods |
| Production deployment | Account limits; liquidity constraints | Multi-book strategy; exchange-based execution |

---

## Sources Consulted

### Academic (OpenAlex)
- Brycki, J. (2009). Statistical and Economic Tests of Efficiency in the EPL Soccer Betting Market
- Tiitu, T. (2016). Abnormal Returns in an Efficient Market?
- Hausch, Lo & Ziemba (2008). Introduction to Prices vs. Handicapping
- Muller et al. (2011). Gender Behavior in Betting Markets
- Nash, U.W. (2018). Fair Odds for Noisy Probabilities (arXiv)
- Ekman, R. (2020). Bivariate Copula-based Regression for Football

### Practitioner (Exa Web Search)
- BetAndBeat, GamblingHarm.org, CollegeFootballWinning, BetFirm
- Establish The Run, BettorEdge, Wizard of Odds, OddsIndex
- OpticOdds, Sharp Football Analysis, BetsBooster
- Machine Learning Mastery, Surmount AI, Math Investor
- SSRN papers on backtest overfitting

---

*Counterevidence Discovery completed for Safety Gate B compliance.*
*Total sources reviewed: 44*
*Categories covered: 7*
