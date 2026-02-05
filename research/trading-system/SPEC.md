Research Specification: Algo-Trading Strategy Pivot Analysis
Goal
Conduct a "Red Team" audit of a retail Directional Swing Trading system (Freqtrade/Python) and determine the mathematically optimal strategy for a Small-Cap ($200-$1,000), Low-Maintenance automated portfolio in the 2026 market regime.

Success Criteria
[ ] Expectancy Validation: Mathematical proof (via literature or logic) regarding the viability of rule-based TA (RSI/Donchian) for small accounts after fees/slippage.

[ ] Strategy Selection: A definitive choice between Directional (Trend/Mean Rev) vs. Market Neutral (Arb/Liquidity/Funding) based on capital efficiency constraints.

[ ] Stack Alignment: Confirmation if the current stack (Freqtrade/Alpaca) fits the recommended strategy or if a migration (e.g., to Hummingbot/Rust) is required.

Research Units
1. The "Retail Alpha" Audit (The Kill Step)
Objective: Determine if "Naive Technical Analysis" (Rule-based indicators without ML) still possesses positive expectancy in 2026 crypto/equity markets. Key Question: Does the alpha decay of standard indicators (RSI, ADX) render them useless for small accounts where fees > edge? Search Terms: "profitability of technical analysis crypto 2024-2026", "retail trader performance statistical analysis", "alpha decay of trend following strategies".

2. Small-Cap Structural Edges (The Pivot)
Objective: Identify strategies where $200-$1,000 is an advantage or at least not a blocker. Investigation Targets:

DeFi Concentrated Liquidity (Uniswap v4/v5): Can a Python script managing CLMM ranges outperform directional trading?

Funding Rate Arbitrage: Is the yield on delta-neutral perp funding high enough to justify the setup?

Long-Tail Stat Arb: Trading obscure assets where HFTs don't bother competing.

Prediction Markets (Polymarket/Gnosis): Is there more inefficiency in binary outcome pricing than asset pricing?

3. "Set-and-Forget" Feasibility Analysis
Objective: Evaluate the maintenance-to-profit ratio. Comparison:

Directional: High variance, requires constant "rule tweaking" (not truly set-and-forget).

Market Neutral: Lower variance, but requires rigorous risk management (liquidation prevention).

Deliverable
Primary Deliverable: THE PIVOT REPORT Must include:

The Verdict: STOP or CONTINUE with Directional Swing.

The Strategy Spec: The exact mechanism recommended (e.g., "Switch to Delta-Neutral Grid Trading on Solana DEXs").

The Architecture Shift: What needs to change in the Docker container? (e.g., "Drop Freqtrade, implement dydx-v4-client").

Context
Current Stack: Python, Docker, Redis, Postgres, Freqtrade (Crypto), Alpaca (Equities).

Current Strategy: Donchian/RSI/ADX (Directional).

Constraints:

Capital: $200 - $1,000 USD (Hard constraint).

Philosophy: "Earned Complexity" (No ML/AI until rules fail).

Goal: Autonomous income (low human intervention).

Prior Art Hints
Literature: "The Cross-Section of Crypto-Asset Returns" (Liu et al.), Papers on "Uniswap v3/v4 Liquidity Provision Profitability."

Systems: Hummingbot (Market Making), Freqtrade (Directional), Kelvin (DeFi Structuring).

Constraints
Exclusions: Do not recommend High-Frequency Trading (HFT) or Latency Arbitrage (impossible with Python/Retail hardware).

Reality Check: Explicitly calculate the impact of trading fees (0.1% - 0.6%) on a $200 account executing high-turnover strategies.

Recency Policy
Recency: fast_moving (Crypto/DeFi changes monthly; rely on 2025-2026 data).