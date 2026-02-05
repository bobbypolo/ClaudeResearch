# Research Plan: trading-system

## Goal Understanding

**Restatement**: Execute a rigorous "Red Team" audit of a retail Directional Swing Trading system to determine whether rule-based technical analysis (RSI/Donchian/ADX) remains viable for small accounts ($200-$1,000) in 2026 markets, and if not, identify the mathematically optimal alternative strategy that maximizes capital efficiency while minimizing maintenance overhead.

**Core Tension**: The user suspects their current directional approach may have negative expectancy after fees/slippage, and wants evidence-based guidance on whether to pivot to market-neutral strategies (DeFi LP, funding arb, stat arb) or prediction markets.

## Success Criteria

- [ ] **Unit 1 (Retail Alpha Audit)**: HIGH confidence determination on whether naive TA indicators have positive expectancy for small retail accounts in 2026 crypto/equity markets. Must include fee impact calculations.
- [ ] **Unit 2 (Small-Cap Edges)**: HIGH confidence ranking of alternative strategies (CLMM LP, Funding Arb, Long-tail Stat Arb, Prediction Markets) with capital efficiency analysis for $200-$1k range. **Must include "Dust Trap" analysis**: exchange minimums, gas/bridge costs, withdrawal fees, and minimum viable capital thresholds per strategy.
- [ ] **Unit 3 (Set-and-Forget Feasibility)**: HIGH confidence comparison of maintenance-to-profit ratios between directional vs. market-neutral approaches, with stack migration requirements.

## Research Strategy

### Unit 1: Retail Alpha Audit (The Kill Step)

**Question**: Does rule-based technical analysis (RSI, Donchian, ADX) still possess positive expectancy in 2026 crypto/equity markets for small accounts where fees may exceed edge?

**Search Strategy**:
- Primary: "technical analysis profitability 2024 2025" "retail trader performance study" "alpha decay trend following"
- Secondary: "RSI strategy backtesting results" "momentum strategies crypto returns" "indicator-based trading performance"
- Failure: "technical analysis failed" "retail traders lose money" "why trend following stopped working"
- Academic: "cross-section crypto returns" "predictability financial markets" "technical trading rules profitability"

**Expected Sources**:
- Academic papers on TA profitability (Liu et al., cross-section studies)
- Retail broker performance disclosures (required by regulation in some jurisdictions)
- Quantitative finance literature on alpha decay
- Failed strategy postmortems

**Success Indicator**:
- 3+ peer-reviewed studies on TA profitability in recent markets
- Fee impact calculation framework with concrete numbers
- Clear CONTINUE/STOP verdict supported by evidence

### Unit 2: Small-Cap Structural Edges (The Pivot)

**Question**: For $200-$1,000 capital, which strategies offer positive expectancy where small size is advantageous (or at least neutral)?

**Sub-areas to investigate**:
1. **DeFi Concentrated Liquidity (Uniswap v3/v4)**: Python-managed CLMM ranges
2. **Funding Rate Arbitrage**: Delta-neutral perp funding yield
3. **Long-Tail Stat Arb**: Obscure assets without HFT competition
4. **Prediction Markets**: Binary outcome pricing inefficiencies

**"Dust Trap" Filter (MUST APPLY TO ALL SUB-AREAS)**:
Before evaluating alpha, each strategy must pass capital viability checks:
- **Exchange Minimums**: Minimum order size ($10-$20 typical) vs. position sizing needs
- **Gas/Bridge Costs**: L2 bridging ($5+), withdrawal fees, contract interactions
- **Rebalancing Friction**: Can a $200 portfolio execute required rebalances without fees > edge?
- **Threshold Calculation**: What is the minimum viable capital for each strategy?

**Search Strategy**:
- Primary: "Uniswap v3 liquidity provision profitability" "funding rate arbitrage crypto" "prediction market inefficiency"
- Secondary: "CLMM impermanent loss analysis" "small account crypto trading strategies" "DeFi yield optimization"
- Failure: "Uniswap LP lost money" "funding arbitrage failure" "liquidity provision risks"
- Practitioner: Hummingbot documentation, dYdX funding rate data, Polymarket analysis

**Expected Sources**:
- Academic papers on AMM LP profitability (Uniswap studies)
- DeFi protocol documentation and whitepapers
- Funding rate historical analysis
- Prediction market efficiency studies

**Success Indicator**:
- Quantitative comparison of expected returns across strategies
- Capital efficiency metrics (minimum viable capital, fee breakeven)
- Implementation complexity ranking
- **Dust Trap Analysis**: Explicit pass/fail for $200 and $1,000 thresholds per strategy (exchange minimums, gas costs, withdrawal fees, rebalancing friction)

### Unit 3: Set-and-Forget Feasibility Analysis

**Question**: What is the maintenance-to-profit ratio for each viable strategy, and what stack changes are required?

**Search Strategy**:
- Primary: "automated trading maintenance requirements" "market neutral strategy management" "DeFi automation tools"
- Secondary: "Freqtrade vs Hummingbot comparison" "automated LP management" "trading bot reliability"
- Failure: "trading bot failures" "automated strategy blowup" "LP position liquidated"
- Practitioner: Bot framework documentation, deployment guides, operational postmortems

**Expected Sources**:
- Trading framework documentation (Freqtrade, Hummingbot, Kelvin)
- DevOps and reliability engineering for trading systems
- Operational failure case studies
- Stack comparison analyses

**Success Indicator**:
- Maintenance hours/month estimate per strategy
- Stack migration requirements with complexity assessment
- Risk management requirements (liquidation prevention, etc.)

## Anticipated Sub-Domains

1. **Transaction Cost Analysis**: May need deeper dive into CEX vs DEX fee structures, gas costs, slippage models
2. **Solana vs Ethereum DeFi**: If CLMM is viable, need to compare chains for small accounts
3. **Tax/Regulatory Considerations**: Market-neutral strategies may have different tax treatment
4. **Specific Protocol Deep-Dives**: May need to investigate specific implementations (Raydium, Orca, dYdX v4)

## Key Search Terms

| Concept | Primary Terms | Variants |
|---------|---------------|----------|
| TA Profitability | technical analysis profitability, indicator trading returns | RSI performance, momentum alpha, trend following returns |
| Retail Performance | retail trader returns, individual investor performance | small account trading, amateur trader statistics |
| Alpha Decay | alpha decay, strategy decay, factor crowding | edge erosion, signal degradation |
| CLMM LP | concentrated liquidity provision, Uniswap v3 LP | AMM liquidity, impermanent loss, LP profitability |
| Funding Arb | funding rate arbitrage, perpetual funding | delta neutral crypto, basis trade |
| Prediction Markets | prediction market efficiency, Polymarket | binary options pricing, event contracts |
| Low Maintenance | set and forget trading, automated trading systems | passive income crypto, hands-off strategies |

## Estimated Scope

- **Preset**: thorough (5 sources/unit minimum, deep extraction)
- **Expected sources**: 20-30 total
- **Research units**: 3
- **Recency Policy**: fast_moving (18 months - focus on 2024-2026)
- **Deliverable**: VERDICT (THE PIVOT REPORT with STOP/CONTINUE decision)
- **Passes**: Academic + Practitioner + Failure Analysis + Snowball
- **Special Requirements**:
  - Fee impact calculations required
  - Stack migration recommendations
  - Capital efficiency analysis for $200-$1k range

## Risk Factors

1. **Recency Bias**: Crypto markets change rapidly; 2024 data may not reflect 2026 conditions
2. **Survivorship Bias**: Published strategies tend to be winners; need failure studies
3. **Access Limitations**: Some DeFi research may be paywalled or in preprint
4. **Implementation Gap**: Academic findings vs. practical implementation may differ

## Approval Checkpoint

- [ ] User approves research plan before proceeding to Phase 1

---

*Plan created: 2026-02-04*
*Preset: thorough*
*Estimated completion: Single session*
