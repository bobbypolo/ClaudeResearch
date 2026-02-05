---
name: research
description: Execute autonomous research with 8-phase workflow including planning, failure analysis, and implementation specifications
user_prompt: true
---

# /research {slug} [--quick|--standard|--thorough|--decision-support]

Execute a comprehensive, autonomous research workflow that produces implementation-ready specifications through 8 systematic phases.

## INVOCATION

The user provides a research slug and optional preset:
- Read the specification from: `research/{slug}/SPEC.md`
- All outputs go to: `research/{slug}/`
- Create the research directory if it doesn't exist

**Presets:**
| Preset | Min Sources/Unit | Extraction Depth | Passes | Use When |
|--------|------------------|------------------|--------|----------|
| `--quick` | 2 | light | 2 | Time-sensitive, exploration |
| `--standard` | 3 | medium | 3 | Default (failure analysis required) |
| `--thorough` | 5 | deep | 3 | Critical decisions, publications |
| `--decision-support` | 4 | deep | 3 | VERDICT/COMPARISON deliverables |

---

## PHASE 0: PLAN (MANDATORY)

**Objective**: Create comprehensive research plan before any discovery. User must approve.

### Instructions

1. Read `research/{slug}/SPEC.md` using the Read tool
2. If SPEC.md doesn't exist: STOP and inform user to create it first

3. **Analyze the SPEC and create research plan**:
   - Understand the user's Goal (NOT "Research Question" - v5.0 uses "Goal")
   - Decompose into research questions per unit
   - Identify implementation-focused search strategies
   - Define what HIGH confidence looks like for each unit
   - Anticipate sub-domains that may need investigation

4. **Write PLAN.md**:

```markdown
# Research Plan: {slug}

## Goal Understanding
{Restate user's goal in implementation terms}

## Success Criteria
- [ ] {What HIGH confidence looks like for each unit}

## Research Strategy

### Unit 1: {name}
**Question**: How do we {specific aspect}?
**Search Strategy**:
- Primary: "{term} implementation" "{term} method"
- Secondary: "{term} architecture" "{term} design"
- Failure: "{term} failed" "{term} pitfalls" "{term} lessons learned"
**Expected Sources**: {type of papers/reports}
**Success Indicator**: {what finding HIGH confidence looks like}

### Unit 2: {name}
...

## Anticipated Sub-Domains
{Domains that may require investigation}

## Key Search Terms
| Concept | Primary Terms | Variants |
|---------|---------------|----------|

## Estimated Scope
- Expected sources: {range}
- Research units: {count}
- Complexity: {preset}

## Approval Checkpoint
[ ] User approves plan before proceeding
```

Write to `research/{slug}/PLAN.md`

5. **STOP AND PRESENT PLAN TO USER**

```
## Research Plan Created: {slug}

I've created a research plan based on your SPEC.

### Goal
{restated goal}

### Research Units
1. {unit 1}
2. {unit 2}
3. {unit 3}

### Search Strategy
{brief summary}

### Estimated Scope
- Preset: {preset}
- Expected sources: {range}

**Please review `research/{slug}/PLAN.md` and confirm to proceed.**

Do you approve this research plan?
```

**CRITICAL**: Do NOT proceed to Phase 1 until user explicitly approves.

---

## PHASE 1: PARSE

**Objective**: Parse SPEC, detect complexity, determine recency policy, initialize state.

### Instructions

1. Confirm user has approved the plan from Phase 0
2. Read `research/{slug}/SPEC.md` using the Read tool
3. Extract and validate required elements:

```
REQUIRED (v5.0 format):
- Goal: [What to build/implement - NOT a question]
- Success Criteria: [What HIGH confidence looks like]
- Research Units: [1-5 focused areas]
- Deliverable: SPECIFICATION | VERDICT | REPORT | COMPARISON | BLUEPRINT | BIBLIOGRAPHY
- Context: [Use case, constraints, expertise, existing work]

OPTIONAL:
- Prior Art Hints: [Known starting points]
- Constraints: [Time period, excluded sources]
- Key Search Terms: [Auto-generate if missing]
- Recency Policy: [fast_moving | scientific | historical]
```

4. **Auto-Complexity Detection**:

```javascript
preset = args.preset || detectPreset(spec)
min_sources_per_unit = preset === 'quick' ? 2 : preset === 'thorough' ? 5 : preset === 'decision-support' ? 4 : 3
extraction_depth = preset === 'quick' ? 'light' : ['thorough', 'decision-support'].includes(preset) ? 'deep' : 'medium'

tier_targets = {
  academic: spec.includesIndustryTopics ? 50 : 70,
  practitioner: spec.includesIndustryTopics ? 40 : 25,
  other: 10
}
```

5. **Recency Policy Detection**:

```javascript
recency_policy = detectRecencyPolicy(spec)
// Returns: 'fast_moving' | 'scientific' | 'historical'

max_age_years = {
  'fast_moving': 2,       // ~18-24 months (use 2 for integer API calls)
  'scientific': 5,        // 5 years
  'historical': null      // No limit
}[recency_policy]
// NOTE: OpenAlex requires INTEGER years. Always floor() the year calculation.
```

6. **Write STATE.json** (v3.0 schema):

```json
{
  "version": "3.0",
  "slug": "{slug}",
  "preset": "standard",
  "posture": "optimistic-empirical",
  "min_sources_per_unit": 3,
  "extraction_depth": "medium",
  "tier_targets": { "academic": 70, "practitioner": 25, "other": 5 },
  "research_units": ["unit1", "unit2", "unit3"],
  "deliverable": "SPECIFICATION",
  "phase": "parse",
  "started_at": "2024-01-01T00:00:00Z",
  "completed_at": null,
  "plan_approved": true,
  "config": {
    "recency_policy": "scientific",
    "max_age_years": 5,
    "foundational_exception": true,
    "snowball": {
      "enabled": true,
      "max_seeds_per_unit": 5,
      "max_snowball_sources": 10
    },
    "grey_literature": false,
    "structured_extraction": true,
    "failure_analysis": true
  },
  "gates": {
    "depth_gate": { "required_fulltext": 2, "status": "pending" },
    "completion_gate": { "requires_high_confidence": true, "status": "pending", "gaps_declared": [] },
    "retraction_gate": { "status": "pending" }
  },
  "statistics": {
    "sources_found": 0,
    "sources_deduplicated": 0,
    "fulltext_resolved": 0,
    "abstract_only": 0,
    "paywalled": 0,
    "retractions_found": 0,
    "snowball_added": 0,
    "failure_studies_found": 0,
    "risk_mitigation_pairs": 0
  },
  "confidence_tracking": {
    "high_confidence_claims": 0,
    "low_confidence_claims": 0,
    "gaps_requiring_research": []
  }
}
```

7. Create directory structure:
```
research/{slug}/
├── PLAN.md
├── SPEC.md
├── STATE.json
├── discovery/
├── topics/
│   ├── {unit1_slug}/
│   ├── {unit2_slug}/
│   └── {unit3_slug}/
├── synthesis/
└── logs/
```

---

## PHASE 2: SURVEY

**Objective**: Broad discovery focused on implementation approaches.

### Discovery Strategy (v5.0 - Implementation-Focused)

| Pass | When to Run | Purpose | Target |
|------|-------------|---------|--------|
| **Academic** | Always | Peer-reviewed, arXiv, theses | 60% |
| **Practitioner** | SPECIFICATION/BLUEPRINT/VERDICT OR preset >= standard | Case studies, docs | 30% |
| **Failure Analysis** | Always for preset >= standard (Completion Gate) | Failed implementations, lessons learned | 10% |
| **Grey Literature** | If deliverable == BLUEPRINT | NIST, RAND, standards | 10% |
| **Snowball** | After keyword search, if preset >= standard | Citation expansion | +10 max |

### Search Strategy (v5.0 - "How to build" focus)

```
Primary queries:
- "{goal} implementation" "{goal} system design" "{goal} method"
- "{goal} architecture" "{goal} pipeline" "{goal} algorithm"

Secondary queries:
- "{goal} best practices" "{goal} state of the art"
- "{goal} comparison benchmark"

Failure queries:
- "{method} failed" "{method} failure" "{method} pitfalls"
- "{method} lessons learned" "{method} postmortem"
```

### Instructions

Read `research/{slug}/STATE.json` to determine passes to run.

**SPAWN AGENT 1: Academic Discovery**

```
TaskCreate:
  subject: "Academic Discovery for {slug}"
  description: |
    You are an Academic Discovery Agent. Find implementation-focused sources.

    CONTEXT:
    - Slug: {slug}
    - Research Units: {units}
    - Key Terms: {terms}
    - Min per unit: {min_sources_per_unit}
    - Max per unit: 12
    - Recency Policy: {recency_policy}
    - Year Filter: from_publication_year = {current_year - max_age_years, rounded down to integer}
      (e.g., fast_moving in 2026: floor(2026 - 1.5) = 2024)

    TOOLS:
    1. ToolSearch "+openalex search" → mcp__openalex__search_works
    2. ToolSearch "+arxiv" → mcp__arxiv__search_papers

    CRITICAL: When calling OpenAlex, use INTEGER years only (e.g., 2024, not 2024.5)

    SEARCH STRATEGY (Implementation-focused):
    - Prioritize: papers with methods sections, reproducibility, code
    - Search: "{term} implementation" "{term} method" "{term} system"
    - Look for: benchmark results, parameter tables, architecture diagrams
    - Flag sources that have implementation detail

    OUTPUT FORMAT (write to research/{slug}/discovery/academic.md):
    # Academic Discovery Results

    ## {Research Unit 1}
    | # | Title | Authors | Year | Type | DOI | Citations | Has Impl Detail | Relevance |
    |---|-------|---------|------|------|-----|-----------|-----------------|-----------|

    ## Search Log
    - Query: "..." → N results
  activeForm: "Discovering academic sources"
```

**SPAWN AGENT 2: Practitioner Discovery** (if needed)

Only spawn if: `deliverable in ['SPECIFICATION', 'BLUEPRINT', 'VERDICT'] OR preset in ['standard', 'thorough', 'decision-support']`

**SPAWN AGENT 3: Failure Analysis Discovery** (REQUIRED for standard+)

Spawn if: `preset in ['standard', 'thorough', 'decision-support']`

```
TaskCreate:
  subject: "Failure Analysis Discovery for {slug}"
  description: |
    You are a Failure Analysis Agent. Find implementations that failed and extract lessons.

    IMPORTANT: This is REQUIRED by Completion Gate for standard+ presets.

    CONTEXT: {same as above}

    QUERY PATTERNS (find failures and lessons):
    - "{method} failed" "{method} failure analysis"
    - "{method} pitfalls" "{method} mistakes"
    - "{method} lessons learned" "{method} postmortem"
    - "{domain} what went wrong" "{domain} debugging"

    FOR EACH FAILURE FOUND, EXTRACT:
    - What method was attempted
    - What failed and why
    - Lessons learned
    - Risk-mitigation pair

    OUTPUT: Write to research/{slug}/discovery/failure_analysis.md
  activeForm: "Discovering failure studies"
```

**SPAWN AGENT 4: Grey Literature** (BLUEPRINT only)

**SNOWBALL EXPANSION** (if enabled)

---

## PHASE 3: DEEP DIVE

**Objective**: Evidence-driven depth allocation with implementation detail focus.

### Instructions

1. Read all discovery files from `research/{slug}/discovery/`
2. Read `research/{slug}/STATE.json`

3. **Identify promising implementation sources**:
   - Flag sources with implementation detail (code, params, architecture)
   - Prioritize FULLTEXT sources for deep extraction
   - Allocate more depth to units with strong implementation papers

4. **Deduplication Pipeline**:
```javascript
function canonicalKey(source) {
  if (source.doi) return `doi:${source.doi.toLowerCase()}`
  const titleNorm = source.title.toLowerCase().replace(/[^a-z0-9]/g, '').slice(0, 50)
  const authorLast = source.authors[0]?.split(' ').pop()?.toLowerCase() || 'unknown'
  return `fp:${titleNorm}|${authorLast}|${source.year}`
}
```

5. **Retraction Check** (Gate C)

6. **Full-Text Resolution** (Unpaywall)

7. **Write SOURCES.md** with implementation detail flags:

```markdown
# Sources: {slug}

## Summary
- Total: N sources
- With implementation detail: N
- Access: FULLTEXT: N | ABSTRACT_ONLY: N | PAYWALLED: N

## By Research Unit

### {Unit 1}
| # | Title | Type | Year | DOI | Access | Impl Detail | Tier |
|---|-------|------|------|-----|--------|-------------|------|
| S1 | ... | ACADEMIC | 2024 | 10.xxx | FULLTEXT | YES | 1 |
```

---

## PHASE 4: FAILURE

**Objective**: Extract risk-mitigation pairs from failure studies.

### Instructions

1. Read `research/{slug}/discovery/failure_analysis.md`
2. For each failure study found, extract:

```markdown
## Failure Study: {source}

### Context
- **Method Attempted**: {specific approach}
- **Domain**: {application area}
- **Scale**: {size/scope}

### Failure Description
- **What Failed**: {observable failure}
- **Root Cause**: {why it failed}
- **When Discovered**: {development/testing/production}

### Lessons Learned
1. {lesson 1}
2. {lesson 2}

### Risk-Mitigation Pair
| Risk | Likelihood | Impact | Mitigation | Evidence |
|------|------------|--------|------------|----------|
| {risk} | H/M/L | H/M/L | {mitigation} | {source} |
```

3. **Compile aggregated risk-mitigation table**:

Write to `research/{slug}/synthesis/risk_mitigations.md`:

```markdown
# Risk-Mitigation Summary: {slug}

| # | Risk | Category | Likelihood | Impact | Mitigation | Evidence |
|---|------|----------|------------|--------|------------|----------|
| R1 | {risk} | {data/model/system} | H/M/L | H/M/L | {mitigation} | S3, S7 |
```

4. Update STATE.json statistics:
```json
{
  "statistics": {
    "failure_studies_found": N,
    "risk_mitigation_pairs": N
  }
}
```

---

## PHASE 5: COMPILE

**Objective**: Build claims registry, enforce gates, ensure HIGH confidence or document gaps.

### Extraction Template (12 Fields - v5.0)

```markdown
## Source: {title}

- **Citation**: {full formatted citation}
- **Type**: ACADEMIC | PRACTITIONER | OTHER
- **Tier**: 1 | 2 | 3
- **Extraction depth**: FULLTEXT | ABSTRACT_ONLY | PAYWALLED
- **Has implementation detail**: YES | NO
- **Source URL**: {accessible URL}
- **Sections extracted**: {e.g., "Abstract, Methods, Results"}
- **Main claim**: {one sentence}
- **Key evidence**: "{quote}" (location)
- **Implementation specifics**: {methods, parameters if present}
- **Limitations**: {caveats}
- **Relevance**: {unit}
```

### Confidence Calculation (v5.0 with implementation detail)

```javascript
function calculateConfidence(sources, claimType) {
  const agree = sources.filter(s => s.supports_claim)
  const disagree = sources.filter(s => s.contradicts_claim)

  if (disagree.length > 0 && disagree.some(s => s.tier <= 2)) {
    return 'CONTESTED'
  }

  const tier1or2 = agree.filter(s => s.tier <= 2)
  const fulltextTier1or2 = tier1or2.filter(s => s.extraction_depth === 'FULLTEXT')

  // For recommendations, also require implementation detail
  if (claimType === 'recommendation') {
    const hasImplDetail = agree.some(s => s.has_implementation_detail)
    if (tier1or2.length >= 3 && fulltextTier1or2.length >= 2 && hasImplDetail) {
      return 'HIGH'
    }
  } else {
    if (tier1or2.length >= 3 && fulltextTier1or2.length >= 2) {
      return 'HIGH'
    }
  }

  return 'LOW'
}
```

### Gate Enforcement

**Gate A (Depth Gate)**:
- HIGH confidence requires >= 2 FULLTEXT Tier-1/2 sources
- If check fails: downgrade to LOW

**Gate B (Completion Gate)** - NEW in v5.0:
- All recommendation claims must have HIGH confidence, OR
- LOW confidence claims must have explicit gap declarations
- If check fails: Document gaps before synthesis

**Gate C (Retraction Gate)**:
- No retracted papers in HIGH claims

### Gap Declaration (if LOW confidence)

When a recommendation cannot achieve HIGH confidence, document:

```markdown
## Gap: {what is unknown}

- **Claim Affected**: {the recommendation this blocks}
- **Current Confidence**: LOW
- **Reason**: {why HIGH not achievable}
- **Impact**: {what can't be determined}
- **Resolution Path**: {what research would fill this gap}
```

Write gaps to `research/{slug}/synthesis/gaps.md`

### Write claims.md

```markdown
# Claims Registry: {slug}

## Gate Status
- Depth Gate (A): {PASSED/FAILED - N claims downgraded}
- Completion Gate (B): {PASSED/FAILED - N gaps declared}
- Retraction Gate (C): {PASSED - N retractions removed}

## Research Unit: {unit1}

### Claim 1: {statement}
- **Type**: recommendation | finding
- **Confidence**: HIGH | LOW | CONTESTED
- **Sources**: S1 (FULLTEXT, T1, impl:YES), S4 (FULLTEXT, T2, impl:YES)
- **Implementation detail**: YES
- **Gate A check**: PASSED
- **Gate B check**: PASSED (or: GAP DECLARED - see gaps.md)
```

---

## PHASE 6: SPECIFY

**Objective**: Generate implementation specification (or other deliverable type).

### Instructions

1. Read all compiled data
2. **Verify Completion Gate** before synthesis:
   - All recommendations must be HIGH confidence OR have gaps declared
   - If gate fails: STOP, complete gap documentation first

3. **Generate Deliverable** based on type:

### SPECIFICATION (implementation guidance) - DEFAULT

```markdown
# Implementation Specification: {goal}

## Executive Summary
{2-3 sentences on recommended approach}

**Confidence Level**: HIGH | (explicit gaps listed below)

## Gate Compliance
- Depth Gate (A): PASSED/FAILED
- Completion Gate (B): PASSED/FAILED (gaps: N)
- Retraction Gate (C): PASSED

## Recommended Architecture

### Component 1: {name}
**Selected Method**: {specific method name}
**Why This Method**:
- Evidence: S1 (FULLTEXT), S4 (FULLTEXT), S7 (FULLTEXT)
- Performance: {metrics from literature}
- Alternatives Considered: {what else, why not}

**Implementation Details**:
- Input: {what it needs}
- Output: {what it produces}
- Key Parameters: {from sources}
- Dependencies: {what must come first}

### Component 2: {name}
...

## Implementation Sequence
Step 1: {name} ─depends on→ nothing
Step 2: {name} ─depends on→ Step 1
...

## Data Requirements
| Data Type | Source | Format | Frequency | Evidence |
|-----------|--------|--------|-----------|----------|

## Risk-Mitigation Table
| # | Risk | Likelihood | Impact | Mitigation | Evidence |
|---|------|------------|--------|------------|----------|
{from Phase 4 failure analysis}

## Validation Approach
| Metric | Target | Rationale | Evidence |
|--------|--------|-----------|----------|

## Known Gaps (if any)
### Gap 1: {what is unknown}
- **Impact**: {why this matters}
- **Resolution Path**: {what research would help}

## Sources
### Primary (HIGH confidence basis)
| # | Title | Year | Access | Impl Detail | Relevance |
|---|-------|------|--------|-------------|-----------|

### Failure Studies
| # | Title | Year | Key Lesson |
|---|-------|------|------------|
```

### Other Deliverable Types

See `.claude/rules/research.md` for VERDICT, COMPARISON, REPORT, BLUEPRINT, BIBLIOGRAPHY formats.

Write to `research/{slug}/synthesis/final_deliverable.md`

---

## PHASE 7: VALIDATE

**Objective**: Self-assess, ensure all gates passed, document limitations.

### Instructions

1. Read all outputs
2. Verify all gates passed
3. Generate critique (max 1 page):

```markdown
# Critique: {slug}

## Gate Compliance Summary
| Gate | Status | Impact |
|------|--------|--------|
| Depth (A) | PASSED/FAILED | {N claims downgraded} |
| Completion (B) | PASSED/FAILED | {N gaps declared} |
| Retraction (C) | PASSED/FAILED | {N removed} |

## Completeness
| Unit | Sources | FULLTEXT | Impl Detail | Confidence | Gaps |
|------|---------|----------|-------------|------------|------|

## Confidence Summary
- HIGH confidence recommendations: N
- LOW confidence (with gaps): N
- CONTESTED: N

## Key Limitations
1. {most important}
2. {access-related}
3. {coverage gap}

## What Could Invalidate Conclusions
- If {assumption} is false, then {consequence}
```

Write to `research/{slug}/synthesis/critique.md`

4. Update STATE.json:
```json
{
  "phase": "complete",
  "completed_at": "2024-01-01T12:00:00Z",
  "summary": {
    "sources": 25,
    "claims": 12,
    "high_confidence": 8,
    "low_confidence_with_gaps": 3,
    "risk_mitigation_pairs": 7,
    "all_gates_passed": true
  }
}
```

5. **Present Summary to User**:

```
## Research Complete: {slug}

### Posture: Implementation-Focused
All recommendations backed by evidence with implementation detail.

### Gate Status
- All gates PASSED ✓ (or: N gaps declared)

### Key Recommendations
{3-5 bullet summary of selected methods}

### Confidence Profile
- HIGH confidence recommendations: N
- Gaps documented: N
- Risk-mitigation pairs: N

### Files Created
- `PLAN.md` - Approved research plan
- `synthesis/final_deliverable.md` - Implementation specification
- `synthesis/risk_mitigations.md` - Risk-mitigation pairs
- `synthesis/gaps.md` - Gap declarations (if any)
- `synthesis/critique.md` - Quality assessment

What would you like to explore further?
```

---

## ERROR HANDLING

**SPEC not found**: STOP, inform user to create SPEC.md first

**Plan not approved**: STOP, wait for user approval

**Discovery fails**: Continue with successful agents, note gaps

**Extraction fails**: Tag as ABSTRACT_ONLY, note limitation

**Sources insufficient**: Broaden search, document gaps

**Gate failures**:
- Depth Gate: Downgrade confidence, continue
- Completion Gate: Document gaps, then continue to synthesis
- Retraction Gate: Remove source, recalculate claims

---

## FILE STRUCTURE (v5.0)

```
research/{slug}/
├── PLAN.md                      # Research plan (requires approval)
├── SPEC.md                      # Input specification (Goal, not Question)
├── STATE.json                   # Workflow state (v3.0 schema)
├── SOURCES.md                   # Source list with impl detail flags
├── claims.md                    # Evidence registry with gate checks
├── discovery/
│   ├── academic.md              # Academic pass
│   ├── practitioner.md          # Practitioner pass
│   ├── failure_analysis.md      # Failure studies (was counterevidence)
│   ├── grey_literature.md       # BLUEPRINT only
│   └── snowball.md              # Citation expansion
├── topics/
│   └── {unit}/
│       ├── findings.md          # 12-field extraction
│       └── findings_structured.json
├── synthesis/
│   ├── final_deliverable.md     # PRIMARY OUTPUT
│   ├── critique.md              # Quality assessment
│   ├── risk_mitigations.md      # Compiled risk-mitigation pairs
│   └── gaps.md                  # Gap declarations (if any)
└── logs/
    ├── runlog.ndjson
    ├── checkpoint.md
    ├── dedup_log.json
    └── retraction_flags.json
```

---

## TOOL REFERENCE

### Discovery
- `mcp__openalex__search_works` - Academic papers
- `mcp__openalex__get_work_references` - Backward snowball
- `mcp__openalex__get_work_citations` - Forward snowball
- `mcp__arxiv__search_papers` - Preprints
- `mcp__exa__web_search_exa` - Web sources
- `mcp__crossref__searchByTitle` - Title lookup

### Extraction
- `mcp__firecrawl__firecrawl_scrape` - Web content, OA PDFs
- `mcp__arxiv__read_paper` - arXiv full text

### Verification & Access
- `mcp__crossref__getWorkByDOI` - DOI validation, retraction check
- `WebFetch` to Unpaywall API:
  ```
  https://api.unpaywall.org/v2/{doi}?email=research@example.com
  ```
