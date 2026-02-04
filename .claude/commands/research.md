---
name: research
description: Execute autonomous research with simplified 7-phase parallel workflow
user_prompt: true
---

# /research {slug} [--quick|--standard|--thorough|--decision-support]

Execute a comprehensive, autonomous research workflow that produces high-quality output through 7 systematic phases.

## INVOCATION

The user provides a research slug and optional preset:
- Read the specification from: `research/{slug}/SPEC.md`
- All outputs go to: `research/{slug}/`
- Create the research directory if it doesn't exist

**Presets:**
| Preset | Min Sources/Unit | Extraction Depth | Passes | Use When |
|--------|------------------|------------------|--------|----------|
| `--quick` | 2 | light | 2 | Time-sensitive, exploration |
| `--standard` | 3 | medium | 2-3 | Default for most research |
| `--thorough` | 5 | deep | 3 | Critical decisions, publications |
| `--decision-support` | 4 | deep | 3 | VERDICT/COMPARISON deliverables |

---

## PHASE 1: PARSE

**Objective**: Parse SPEC, detect complexity, initialize state.

### Instructions

1. Read `research/{slug}/SPEC.md` using the Read tool
2. If SPEC.md doesn't exist: STOP and inform user to create it first
3. Extract and validate required elements:

```
REQUIRED:
- Research Question: [Primary question to answer]
- Research Units: [1-5 focused areas]
- Deliverables: VERDICT | REPORT | COMPARISON | BLUEPRINT | BIBLIOGRAPHY
- User Context: [Use case, constraints, expertise]

OPTIONAL (defaults apply):
- Constraints: [Default: last 5 years + foundational]
- Key Search Terms: [Auto-generate if missing]
- Preset: [Auto-detect if not specified]
```

4. **Auto-Complexity Detection** - Determine:

```javascript
// Derive from SPEC content
preset = args.preset || detectPreset(spec)
contested_flag = isContested(spec) // true if VERDICT/COMPARISON or "vs/compare/which/should" phrasing
min_sources_per_unit = preset === 'quick' ? 2 : preset === 'thorough' ? 5 : 3
extraction_depth = preset === 'quick' ? 'light' : preset === 'thorough' ? 'deep' : 'medium'

// Relax tier targets if academic sources likely scarce
tier_targets = {
  academic: spec.includesIndustryTopics ? 50 : 70,
  practitioner: spec.includesIndustryTopics ? 40 : 25,
  other: 10
}
```

5. **Generate Key Terms** (if not provided):
   - Extract technical terms from Research Question
   - Include synonyms and variants
   - Add negation terms if contested_flag

6. **Write STATE.json**:

```json
{
  "slug": "{slug}",
  "preset": "standard",
  "contested_flag": false,
  "min_sources_per_unit": 3,
  "extraction_depth": "medium",
  "tier_targets": { "academic": 70, "practitioner": 25, "other": 5 },
  "research_units": ["unit1", "unit2", "unit3"],
  "deliverable": "REPORT",
  "phase": "parse",
  "started_at": "2024-01-01T00:00:00Z"
}
```

Write to `research/{slug}/STATE.json`

7. Create directory structure:
```
research/{slug}/
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

## PHASE 2: DISCOVER

**Objective**: Find sources using 2-pass (or 3-pass) strategy based on preset.

### Discovery Strategy

| Pass | When to Run | Purpose | Target |
|------|-------------|---------|--------|
| **Academic** | Always | Peer-reviewed, arXiv, theses | 60% |
| **Practitioner** | If BLUEPRINT/VERDICT OR preset >= standard | Case studies, docs | 30% |
| **Counterevidence** | If contested_flag OR preset >= thorough | Critiques, failures | 10% |

### Stop Conditions
- Cap candidates at **12 per research unit**
- Stop early once `min_sources_per_unit` met with acceptable tiers
- No need to exhaust all queries

### Instructions

Read `research/{slug}/STATE.json` to determine:
- Which passes to run (2 or 3)
- min_sources_per_unit target
- tier_targets for quality filtering

Create directory: `research/{slug}/discovery/`

**SPAWN AGENT 1: Academic Discovery**

```
TaskCreate:
  subject: "Academic Discovery for {slug}"
  description: |
    You are an Academic Discovery Agent. Find peer-reviewed and preprint sources.

    CONTEXT:
    - Slug: {slug}
    - Research Units: {units}
    - Key Terms: {terms}
    - Min per unit: {min_sources_per_unit}
    - Max per unit: 12

    TOOLS:
    1. ToolSearch "+openalex search" → mcp__openalex__search_works
    2. ToolSearch "+arxiv" → mcp__arxiv__search_papers
    3. ToolSearch "+crossref" → mcp__crossref__searchByTitle

    SEARCH STRATEGY:
    - Search each research unit with key terms
    - Prioritize: systematic reviews, highly cited, recent (5 years)
    - Stop when min reached OR 12 candidates found per unit

    OUTPUT FORMAT (write to research/{slug}/discovery/academic.md):
    ```
    # Academic Discovery Results

    ## {Research Unit 1}
    | # | Title | Authors | Year | Type | DOI/URL | Citations | Relevance |
    |---|-------|---------|------|------|---------|-----------|-----------|
    | 1 | ... | ... | 2024 | Journal | 10.xxx | 45 | HIGH |

    ## {Research Unit 2}
    ...

    ## Search Log
    - Query: "..." → N results
    ```
  activeForm: "Discovering academic sources"
```

**SPAWN AGENT 2: Practitioner Discovery** (if needed)

Only spawn if: `deliverable in ['BLUEPRINT', 'VERDICT'] OR preset in ['standard', 'thorough', 'decision-support']`

```
TaskCreate:
  subject: "Practitioner Discovery for {slug}"
  description: |
    You are a Practitioner Discovery Agent. Find implementation guides and case studies.

    CONTEXT: {same as above}

    TOOLS:
    1. ToolSearch "+exa" → mcp__exa__web_search_exa

    SEARCH STRATEGY:
    - Focus on: tutorials, documentation, case studies, engineering blogs
    - Filter for authoritative domains: .edu, .gov, major tech companies
    - Look for practical implementation details

    OUTPUT: Write to research/{slug}/discovery/practitioner.md
  activeForm: "Discovering practitioner sources"
```

**SPAWN AGENT 3: Counterevidence Discovery** (if needed)

Only spawn if: `contested_flag OR preset in ['thorough', 'decision-support']`

```
TaskCreate:
  subject: "Counterevidence Discovery for {slug}"
  description: |
    You are a Counterevidence Discovery Agent. Find critiques and limitations.

    CONTEXT: {same as above}

    QUERY PATTERNS:
    - "{term}" limitations challenges problems
    - "{term}" failed failure postmortem
    - "{term}" criticism critique
    - "{term}" why not alternative

    TOOLS: Same as Practitioner agent

    OUTPUT: Write to research/{slug}/discovery/counterevidence.md
  activeForm: "Discovering counterevidence"
```

Wait for all discovery agents to complete before proceeding.

---

## PHASE 3: CURATE

**Objective**: Merge, deduplicate, filter, and organize sources.

### Instructions

1. Read all discovery files from `research/{slug}/discovery/`
2. Read `research/{slug}/STATE.json` for tier_targets

3. **Deduplication**:
   - Match by DOI (exact)
   - Match by title (fuzzy, >90% similarity)
   - When duplicates: keep peer-reviewed over preprint over web

4. **Quality Filtering**:
   - Apply tier_targets from STATE.json
   - Remove sources below relevance threshold
   - Ensure minimum coverage per research unit

5. **Assign to Research Units**:
   - Primary unit assignment
   - Track secondary relevance

6. **Write SOURCES.md**:

```markdown
# Sources: {slug}

## Summary
- Total: N sources
- Academic: N% | Practitioner: N% | Other: N%
- Per unit: {unit1: N, unit2: N, ...}

## By Research Unit

### {Unit 1}
| # | Title | Type | Year | Access URL | Tier |
|---|-------|------|------|------------|------|
| S1 | ... | ACADEMIC | 2024 | https://... | 1 |

### {Unit 2}
...

## Filtered (excluded)
| Title | Reason |
|-------|--------|
| ... | Low relevance |
```

Write to `research/{slug}/SOURCES.md`

---

## PHASE 4: EXTRACT

**Objective**: Extract essential information from top sources.

### Extraction Rules

Read `research/{slug}/STATE.json` for extraction_depth:
- **light** (quick): Extract top 2 per unit
- **medium** (standard): Extract top 3 per unit
- **deep** (thorough): Extract top 5 per unit

### Extraction Template (Essential Fields Only)

```markdown
## Source: {title}

- **Citation**: {full formatted citation}
- **Type**: ACADEMIC | PRACTITIONER | OTHER
- **Tier**: 1 | 2 | 3
- **Main claim**: {one sentence}
- **Key evidence**: "{quote or data point}" (p. X / Section Y)
- **Limitations**: {what this source doesn't cover or gets wrong}
- **Relevance**: {which research unit}
- **Notes**: {optional additional context}
```

### Instructions

1. Read `research/{slug}/SOURCES.md`
2. For each research unit, select top N sources based on extraction_depth
3. Spawn extraction agents (batch 3-4 sources each):

```
TaskCreate:
  subject: "Extract Batch {N} for {slug}"
  description: |
    Extract evidence from these sources using the simplified template.

    SOURCES:
    {list with URLs}

    TOOLS:
    1. ToolSearch "+firecrawl" → mcp__firecrawl__firecrawl_scrape
    2. For arXiv: mcp__arxiv__read_paper

    TEMPLATE (per source):
    - Citation: {full}
    - Type: ACADEMIC | PRACTITIONER | OTHER
    - Tier: 1 | 2 | 3
    - Main claim: {one sentence}
    - Key evidence: "{quote}" (location)
    - Limitations: {caveats}
    - Relevance: {unit}
    - Notes: {optional}

    RULES:
    - Use Firecrawl only when full text needed; cite abstracts otherwise
    - If access fails, note as "Abstract only" and extract what's available

    OUTPUT: Write to research/{slug}/topics/{unit_slug}/findings.md
  activeForm: "Extracting from batch {N}"
```

4. Wait for all extraction agents to complete

---

## PHASE 5: COMPILE

**Objective**: Build claims registry from extracted evidence.

### Instructions

1. Read all findings files from `research/{slug}/topics/*/findings.md`

2. **Build Claims Registry**:
   - Group related claims by theme
   - Calculate confidence for each claim

3. **Confidence Calculation** (simplified):
   - **HIGH**: 3+ Tier-1 academic sources agree
   - **LOW**: 1-2 sources total OR only Tier-2/3 sources
   - **CONTESTED**: Credible sources disagree

4. **Contradiction Handling**:
   - If `contested_flag` from STATE.json OR deliverable is VERDICT/COMPARISON:
     - Run full contradiction analysis
     - Write to `research/{slug}/synthesis/contradictions.md`
   - Otherwise: Just note disagreements without heavy protocol

5. **Write claims.md**:

```markdown
# Claims Registry: {slug}

## Research Unit: {unit1}

### Claim 1: {statement}
- **Confidence**: HIGH | LOW | CONTESTED
- **Sources**: S1, S4, S7
- **Evidence**: "{supporting quote}"

### Claim 2: {statement}
...

## Research Unit: {unit2}
...

## Contradictions (if any)
| Topic | Position A | Position B | Status |
|-------|------------|------------|--------|
| ... | S1, S3 say X | S5 says Y | UNRESOLVED |
```

Write to `research/{slug}/claims.md`

---

## PHASE 6: SYNTHESIZE

**Objective**: Generate the primary research deliverable.

### Instructions

1. Read:
   - `research/{slug}/SPEC.md` (deliverable type)
   - `research/{slug}/claims.md`
   - `research/{slug}/SOURCES.md`

2. **Generate Deliverable** based on type:

**VERDICT** (recommendation):
```markdown
# Verdict: {research question}

## Recommendation
**{RECOMMENDED OPTION}** - Confidence: HIGH | LOW

## Comparison Matrix
| Factor | Option A | Option B |
|--------|----------|----------|
| {factor} | {assessment} | {assessment} |

## Key Evidence
### For {recommended}:
- {claim} [HIGH] - Sources: S1, S4

### Against alternatives:
- {claim} [LOW] - Source: S2

## Caveats
- {limitation 1}
- {limitation 2}

## Sources
[Numbered list]
```

**REPORT** (comprehensive):
```markdown
# Report: {topic}

## Summary
{2-3 paragraphs}

## Findings

### {Research Unit 1}
{Evidence-based narrative}

**Key claims:**
- {claim} [HIGH confidence]
- {claim} [LOW confidence - single source]

### {Research Unit 2}
...

## Limitations
- {what couldn't be determined}

## Sources
[Numbered list]
```

**COMPARISON** (neutral analysis):
```markdown
# Comparison: {options}

## Matrix
| Criterion | Option A | Option B |
|-----------|----------|----------|

## Option A
### Strengths
### Weaknesses
### Best for

## Option B
...

## Selection Guidance
- Choose A when: {conditions}
- Choose B when: {conditions}

## Sources
```

**BLUEPRINT** (implementation):
```markdown
# Blueprint: {topic}

## Overview
{What this achieves}

## Architecture
{High-level design}

## Implementation Steps
### Step 1: {action}
- Evidence basis: {citation}
- Common pitfalls: {warning}

## Best Practices
{Evidence-based recommendations}

## Sources
```

**BIBLIOGRAPHY** (annotated sources):
```markdown
# Bibliography: {topic}

## Essential Reading
### {Citation}
- Summary: {what it covers}
- Key insight: {main contribution}
- Quality: {assessment}

## Supplementary
...
```

3. Write to `research/{slug}/synthesis/final_deliverable.md`

---

## PHASE 7: CRITIQUE

**Objective**: Self-assess research quality (max 1 page).

### Instructions

1. Read:
   - `research/{slug}/synthesis/final_deliverable.md`
   - `research/{slug}/SOURCES.md`
   - `research/{slug}/claims.md`

2. **Generate Critique** (concise, 1 page max):

```markdown
# Critique: {slug}

## Completeness
| Research Unit | Sources | Confidence | Gaps |
|---------------|---------|------------|------|
| {unit1} | N | HIGH/LOW | {any gaps} |

## Source Quality
- Academic: N% (target: {target}%)
- Tier 1: N sources
- Inaccessible: N sources (impact: {low/medium/high})

## Confidence Summary
- HIGH confidence claims: N
- LOW confidence claims: N
- CONTESTED claims: N

## Key Limitations
1. {Most important limitation}
2. {Second limitation}
3. {Third limitation}

## What Could Invalidate Conclusions
- If {assumption} is false, then {consequence}

## Recommended Follow-Up
- {Specific action to strengthen findings}
```

3. Write to `research/{slug}/synthesis/critique.md`

4. **Update STATE.json**:
```json
{
  "phase": "complete",
  "completed_at": "2024-01-01T12:00:00Z",
  "summary": {
    "sources": N,
    "claims": N,
    "confidence": "HIGH|LOW|MIXED"
  }
}
```

5. **Present Summary to User**:

```
## Research Complete: {slug}

### Key Findings
{3-5 bullet summary}

### Files Created
- `synthesis/final_deliverable.md` - Main output
- `synthesis/critique.md` - Quality assessment
- `claims.md` - Evidence registry
- `SOURCES.md` - Source list

### Confidence: {HIGH|LOW|MIXED}

What would you like to explore further?
```

---

## ERROR HANDLING

**SPEC not found**: STOP, inform user to create SPEC.md first

**Discovery fails**: Continue with successful agents, note gaps

**Extraction fails**: Use abstract, note as limitation

**Sources insufficient**: Broaden search, accept partial coverage, document in critique

---

## FILE STRUCTURE

```
research/{slug}/
├── SPEC.md                      # Input specification
├── STATE.json                   # Workflow state and config
├── SOURCES.md                   # Curated source list
├── claims.md                    # Evidence registry
├── discovery/
│   ├── academic.md              # Academic pass results
│   ├── practitioner.md          # Practitioner pass (if run)
│   └── counterevidence.md       # Counterevidence pass (if run)
├── topics/
│   ├── {unit1_slug}/
│   │   └── findings.md          # Extracted evidence
│   ├── {unit2_slug}/
│   │   └── findings.md
│   └── ...
├── synthesis/
│   ├── final_deliverable.md     # PRIMARY OUTPUT
│   ├── critique.md              # Quality assessment
│   └── contradictions.md        # If contested
└── logs/
    ├── runlog.ndjson            # Tool execution log
    └── checkpoint.md            # Resume checkpoint
```

---

## TOOL REFERENCE

### Discovery
- `mcp__openalex__search_works` - Academic papers
- `mcp__arxiv__search_papers` - Preprints
- `mcp__exa__web_search_exa` - Web sources
- `mcp__crossref__searchByTitle` - DOI lookup

### Extraction
- `mcp__firecrawl__firecrawl_scrape` - Web content
- `mcp__arxiv__read_paper` - arXiv papers

### Verification
- `mcp__crossref__getWorkByDOI` - DOI validation (use sparingly)
