# Research ADE v5.0

**Autonomous Research System for Claude Code**

Research ADE executes comprehensive, evidence-based research that produces **implementation-ready specifications**. The system uses MCP tools to access academic databases (OpenAlex, arXiv) and web sources (Exa), synthesizing findings into actionable guidance with full source traceability.

---

## What's New in v5.0

### Implementation-Focused Output
- **SPECIFICATION** is the new default deliverable
- Outputs specific method recommendations with evidence
- Every recommendation requires HIGH confidence or explicit gap declaration
- No more "feasible under narrow conditions" conclusions

### Mandatory Planning Phase
- Research begins with comprehensive plan (PLAN.md)
- User approves plan before discovery starts
- Prevents research drift and ensures alignment with goals

### Failure Studies Replace Counterevidence
- Find implementations that failed and extract lessons
- Every risk paired with a mitigation from literature
- Constructive learning, not defensive hedging

### Completion Gate
- Research only ends with HIGH confidence recommendations
- LOW confidence claims require explicit gap declarations
- Clear, actionable output guaranteed

### Optimistic-Empirical Posture
- Default assumption: "Solutions exist until proven otherwise"
- Focus on "how to build" not "is it possible"
- Implementation-oriented search strategies

---

## Core Philosophy

| Aspect | v4.0 (Old) | v5.0 (New) |
|--------|------------|------------|
| **Default Question** | "Is this feasible?" | "How do we build this?" |
| **Default Deliverable** | REPORT | SPECIFICATION |
| **Counterevidence** | "Find reasons this might not work" | "Find failures and extract lessons" |
| **Completion** | Min sources met | HIGH confidence or gaps declared |
| **Output Style** | Assessment | Implementation guidance |

---

## Features

- **8-Phase Workflow**: Plan -> Parse -> Survey -> Deep Dive -> Failure -> Compile -> Specify -> Validate
- **Mandatory Planning**: User-approved research plan before execution
- **MCP-Powered Discovery**: OpenAlex (250M+ papers), arXiv (preprints), Exa (web)
- **Full-Text Access**: Unpaywall integration for open-access papers
- **Implementation Detail Detection**: Flag sources with code, parameters, architecture
- **Failure Analysis**: Extract risk-mitigation pairs from failure studies
- **Completion Gate**: Ensures HIGH confidence or explicit gaps
- **Parallel Agents**: Discovery agents run simultaneously for speed
- **Full Traceability**: Every claim links to sources with DOIs and tiers
- **Resumable**: STATE.json tracks progress; continue from any checkpoint

---

## Quick Start

### 1. Create SPEC with Goal (not Question)

```bash
mkdir -p research/my-project
```

Create `research/my-project/SPEC.md`:

```markdown
# Research Specification: My Project

## Goal
Build a [specific system/solution] that can [accomplish specific outcome]

## Success Criteria
- [ ] Specific method recommendations identified for each component
- [ ] Implementation sequence with dependencies defined
- [ ] Data requirements documented
- [ ] Known risks paired with mitigations

## Research Units
1. [Component/method area 1]
2. [Component/method area 2]
3. [Component/method area 3]

## Deliverable
SPECIFICATION

## Context
- Use case: [what you're building]
- Constraints: [technical limitations]
- Expertise: [your team's background]
- Existing work: [what you already know]
```

### 2. Run Research

```
/research my-project --thorough
```

### 3. Review and Approve Plan

The system creates `PLAN.md` first. Review the research strategy and approve before execution proceeds.

### 4. Get Implementation Specification

Final output in `synthesis/final_deliverable.md`:
- Selected methods for each component with evidence
- Implementation sequence with dependencies
- Data requirements
- Risk-mitigation table from failure studies
- Validation approach

---

## Commands

| Command | Description |
|---------|-------------|
| `/research {slug}` | Execute 8-phase workflow |
| `/research {slug} --quick` | Fast mode (2 sources/unit, no failure analysis) |
| `/research {slug} --standard` | Default (3 sources/unit, failure analysis) |
| `/research {slug} --thorough` | Deep (5 sources/unit, comprehensive) |
| `/research-status {slug}` | Check progress and plan status |
| `/research-resume {slug}` | Continue interrupted research |
| `/research-validate {slug}` | Validate sources and check gates |
| `/cite {DOI or title}` | Quick citation lookup |

---

## Presets

| Preset | Sources/Unit | Passes | Failure Analysis | Use When |
|--------|--------------|--------|------------------|----------|
| `--quick` | 2 | 2 | No | Exploration, simple questions |
| `--standard` | 3 | 3 | Yes | Default for most research |
| `--thorough` | 5 | 3 | Yes | Critical implementations |
| `--decision-support` | 4 | 3 | Yes | VERDICT/COMPARISON |

---

## How It Works

### Phase 0: Plan (NEW)
- Analyzes user's goal statement
- Decomposes into research questions
- Creates research strategy document
- **User must approve before proceeding**

### Phase 1: Parse
- Reads SPEC.md, validates required sections
- Auto-detects complexity and recency policy
- Writes STATE.json with configuration

### Phase 2: Survey
- Spawns parallel discovery agents
- **Implementation-focused search queries**
- Prioritizes sources with code, parameters, architecture

### Phase 3: Deep Dive
- Evidence-driven depth allocation
- Extracts detailed implementation specifications
- Flags sources with implementation detail

### Phase 4: Failure Analysis (RENAMED)
- Searches for failed implementations
- Extracts lessons learned
- **Creates risk-mitigation pairs**

### Phase 5: Compile
- Builds claims registry with confidence levels
- **Enforces Completion Gate**: HIGH confidence or gaps declared
- Compiles risk-mitigation table

### Phase 6: Specify
- Generates implementation specification
- Includes method selections with evidence
- Documents gaps explicitly if present

### Phase 7: Validate
- Self-assesses source quality and coverage
- Verifies all gates passed
- Documents limitations

---

## Output Files

```
research/{slug}/
├── PLAN.md                      # Research plan (requires approval)
├── SPEC.md                      # Input specification
├── STATE.json                   # Workflow state
├── discovery/
│   ├── academic.md              # Academic sources
│   ├── practitioner.md          # Practitioner sources
│   ├── failure_analysis.md      # Failure studies (NEW name)
│   ├── grey_literature.md       # BLUEPRINT only
│   └── snowball.md              # Citation snowballing
├── SOURCES.md                   # Curated source list
├── topics/
│   └── {unit}/
│       ├── findings.md          # Extracted evidence
│       └── findings_structured.json
├── claims.md                    # Evidence registry
├── synthesis/
│   ├── final_deliverable.md     # PRIMARY OUTPUT
│   ├── critique.md              # Quality assessment
│   ├── risk_mitigations.md      # Compiled risk-mitigation pairs
│   └── gaps.md                  # Explicit gaps (if any)
└── logs/
    └── ...
```

---

## Deliverable Types

| Type | Use When | Output Format |
|------|----------|---------------|
| **SPECIFICATION** | "How to build X?" (DEFAULT) | Implementation blueprint |
| **VERDICT** | "Which should I use?" | Recommendation with evidence |
| **COMPARISON** | "Compare A vs B" | Neutral side-by-side |
| **REPORT** | "What is X?" | Comprehensive findings |
| **BLUEPRINT** | "How to design X?" | Architecture + standards |
| **BIBLIOGRAPHY** | "What sources exist?" | Annotated list |

---

## Confidence Levels

| Level | Requirement | Display |
|-------|-------------|---------|
| **HIGH** | 3+ Tier-1/2 sources + 2+ FULLTEXT + implementation detail | Recommended with confidence |
| **LOW** | 1-2 sources OR no implementation detail | Requires gap declaration |
| **CONTESTED** | Sources disagree | Both positions presented |

---

## Gates

| Gate | Purpose | Failure Action |
|------|---------|----------------|
| **Depth Gate (A)** | HIGH claims need FULLTEXT sources | Downgrade to LOW |
| **Completion Gate (B)** | All recommendations need HIGH or gaps | Block synthesis |
| **Retraction Gate (C)** | No retracted papers | Remove source |

---

## Source Tiers

| Tier | Examples | Target |
|------|----------|--------|
| **1** | Peer-reviewed journals, major conferences | 70% |
| **2** | arXiv preprints, patents, tech reports | 25% |
| **3** | Expert blogs, documentation | 5% |

---

## Prerequisites

### Required MCP Servers

| Server | Purpose | API Key |
|--------|---------|---------|
| **OpenAlex** | Academic papers (250M+) | Free |
| **arXiv** | Preprints | Free |
| **Exa** | Web search | Required |
| **Firecrawl** | Content extraction | Required |
| **Crossref** | DOI validation, retraction checking | Free |

### Optional Services

| Service | Purpose | API Key |
|---------|---------|---------|
| **Unpaywall** | Full-text PDF access | Free (no key needed) |

### Configuration

See `docs/RESEARCH_SETUP.md` for MCP server configuration.

---

## Example: Probability System Research

### SPEC (v5.0 format)

```markdown
# Research Specification: Sports Probability System

## Goal
Build a production-grade probability system for sports betting that can
predict single-leg probabilities, model correlations across legs, and
optimize parlay construction for positive expected value.

## Success Criteria
- [ ] Model architecture recommendations with evidence
- [ ] Calibration method selection
- [ ] Correlation modeling approach
- [ ] Validation metrics with targets

## Research Units
1. Single-leg probability models
2. Correlation/dependence modeling
3. Calibration methods
4. Portfolio optimization

## Deliverable
SPECIFICATION

## Context
- Use case: Building a betting probability system
- Constraints: Limited to public data sources
- Expertise: Data science team with ML experience
- Existing work: Basic ML models attempted
```

### Expected Output

Instead of "feasible under narrow conditions", you get:

```markdown
# Implementation Specification: Sports Probability System

## Executive Summary
Build using gradient boosted trees for single-leg prediction,
Vine Copulas for correlation modeling, Isotonic Regression for
calibration, and fractional Kelly with correlation adjustment.

**Confidence Level**: HIGH

## Recommended Architecture

### Component 1: Single-Leg Probability Engine
**Selected Method**: XGBoost with feature engineering from play-by-play
**Evidence Basis**: S1 (FULLTEXT), S4 (FULLTEXT), S12 (FULLTEXT)
...

## Risk-Mitigation Table
| Risk | Mitigation | Evidence |
|------|------------|----------|
| Calibration drift | Weekly recalibration with holdout | S7 |
| Overfitting to historical | Walk-forward validation | S3, S8 |
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Plan not approved | Review PLAN.md, modify if needed, then approve |
| LOW confidence on recommendations | Check for implementation detail in sources |
| Completion Gate failed | Document gaps explicitly |
| No sources with implementation detail | Broaden search to include tutorials, case studies |

---

## Documentation

| File | Content |
|------|---------|
| `docs/RESEARCH_SETUP.md` | MCP setup, permissions |
| `docs/IMPLEMENTATION_PLAN_v5.md` | v5.0 design rationale |
| `.claude/CLAUDE.md` | System constitution |
| `.claude/rules/research.md` | Schemas and rubrics |
| `templates/SPEC.md` | SPEC template |
| `templates/PLAN.md` | PLAN template |

---

## Migration from v4.0

### SPEC Changes
- "Research Question" → "Goal" (use action verbs: Build, Design, Implement)
- "Success Criteria" section is now required
- "Prior Art Hints" section added (optional)

### Deliverable Changes
- Default is now SPECIFICATION (was REPORT)
- SPECIFICATION is new deliverable type

### Gate Changes
- Safety Gate → Completion Gate
- Completion Gate requires HIGH confidence or explicit gaps

### File Changes
- `counterevidence.md` → `failure_analysis.md`
- New: `PLAN.md`, `risk_mitigations.md`, `gaps.md`

---

**Version 5.0** | Implementation-Focused Research with Mandatory Planning and Completion Gates
