---
name: research
description: Execute autonomous research with v2.0 7-phase workflow including gates, snowballing, and full-text access
user_prompt: true
---

# /research {slug} [--quick|--standard|--thorough|--decision-support]

Execute a comprehensive, autonomous research workflow that produces high-quality output through 7 systematic phases with v2.0 enhancements.

## INVOCATION

The user provides a research slug and optional preset:
- Read the specification from: `research/{slug}/SPEC.md`
- All outputs go to: `research/{slug}/`
- Create the research directory if it doesn't exist

**Presets:**
| Preset | Min Sources/Unit | Extraction Depth | Passes | Use When |
|--------|------------------|------------------|--------|----------|
| `--quick` | 2 | light | 2 | Time-sensitive, exploration |
| `--standard` | 3 | medium | 3 | Default (counterevidence required) |
| `--thorough` | 5 | deep | 3 | Critical decisions, publications |
| `--decision-support` | 4 | deep | 3 | VERDICT/COMPARISON deliverables |

---

## PHASE 1: PARSE

**Objective**: Parse SPEC, detect complexity, determine recency policy, initialize v2.0 state.

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
- Constraints: [Default: based on recency_policy]
- Key Search Terms: [Auto-generate if missing]
- Preset: [Auto-detect if not specified]
```

4. **Auto-Complexity Detection** - Determine:

```javascript
// Derive from SPEC content
preset = args.preset || detectPreset(spec)
contested_flag = isContested(spec) // true if VERDICT/COMPARISON or "vs/compare/which/should" phrasing
min_sources_per_unit = preset === 'quick' ? 2 : preset === 'thorough' ? 5 : preset === 'decision-support' ? 4 : 3
extraction_depth = preset === 'quick' ? 'light' : ['thorough', 'decision-support'].includes(preset) ? 'deep' : 'medium'

// Relax tier targets if academic sources likely scarce
tier_targets = {
  academic: spec.includesIndustryTopics ? 50 : 70,
  practitioner: spec.includesIndustryTopics ? 40 : 25,
  other: 10
}
```

5. **Recency Policy Detection**:

```javascript
// Detect domain from research question and units
recency_policy = detectRecencyPolicy(spec)
// Returns: 'fast_moving' | 'scientific' | 'historical'

// Apply time constraints
max_age_years = {
  'fast_moving': 1.5,    // 18 months - LLMs, emerging tech
  'scientific': 5,        // 5 years - established research
  'historical': null      // No limit
}[recency_policy]

// Indicators for fast_moving:
// - Keywords: LLM, GPT, transformer, crypto, blockchain, generative AI
// - Phrases: "latest", "current state", "recent advances"

// Indicators for historical:
// - Keywords: philosophy, history, classical, foundational
// - Phrases: "origins of", "historical analysis"
```

6. **Generate Key Terms** (if not provided):
   - Extract technical terms from Research Question
   - Include synonyms and variants
   - Add negation terms if contested_flag

7. **Write STATE.json v2.0**:

```json
{
  "version": "2.0",
  "slug": "{slug}",
  "preset": "standard",
  "contested_flag": false,
  "min_sources_per_unit": 3,
  "extraction_depth": "medium",
  "tier_targets": { "academic": 70, "practitioner": 25, "other": 5 },
  "research_units": ["unit1", "unit2", "unit3"],
  "deliverable": "REPORT",
  "phase": "parse",
  "started_at": "2024-01-01T00:00:00Z",
  "config": {
    "recency_policy": "scientific",
    "max_age_years": 5,
    "snowball": {
      "enabled": true,
      "max_seeds_per_unit": 5,
      "max_snowball_sources": 10
    },
    "grey_literature": false,
    "structured_extraction": false
  },
  "gates": {
    "depth_gate": { "required_fulltext": 2, "status": "pending" },
    "safety_gate": { "counterevidence_required": true, "status": "pending" },
    "retraction_gate": { "status": "pending" }
  },
  "statistics": {
    "sources_found": 0,
    "sources_deduplicated": 0,
    "fulltext_resolved": 0,
    "retractions_found": 0
  }
}
```

Write to `research/{slug}/STATE.json`

8. Create directory structure:
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

**Objective**: Find sources using multi-pass strategy with snowball expansion.

### Discovery Strategy

| Pass | When to Run | Purpose | Target |
|------|-------------|---------|--------|
| **Academic** | Always | Peer-reviewed, arXiv, theses | 60% |
| **Practitioner** | If BLUEPRINT/VERDICT OR preset >= standard | Case studies, docs | 30% |
| **Counterevidence** | Always for preset >= standard (Safety Gate) | Critiques, failures | 10% |
| **Grey Literature** | If deliverable == BLUEPRINT | NIST, RAND, standards | 10% |
| **Snowball** | After keyword search, if preset >= standard | Citation expansion | +10 max |

### Stop Conditions
- Cap candidates at **12 per research unit** (before snowball)
- Stop early once `min_sources_per_unit` met with acceptable tiers
- Apply recency_policy filter from STATE.json

### Instructions

Read `research/{slug}/STATE.json` to determine:
- Which passes to run (2-4)
- min_sources_per_unit target
- tier_targets for quality filtering
- recency_policy and max_age_years
- snowball settings
- grey_literature flag

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
    - Recency Policy: {recency_policy}
    - Max Age: {max_age_years} years (null = no limit)

    TOOLS:
    1. ToolSearch "+openalex search" → mcp__openalex__search_works
    2. ToolSearch "+arxiv" → mcp__arxiv__search_papers
    3. ToolSearch "+crossref" → mcp__crossref__searchByTitle

    SEARCH STRATEGY:
    - Search each research unit with key terms
    - Prioritize: systematic reviews, highly cited, recent
    - Apply recency filter (except foundational/seminal papers)
    - Stop when min reached OR 12 candidates found per unit
    - CAPTURE DOIs for all sources (needed for dedup and full-text)

    OUTPUT FORMAT (write to research/{slug}/discovery/academic.md):
    ```
    # Academic Discovery Results

    ## {Research Unit 1}
    | # | Title | Authors | Year | Type | DOI | Citations | Relevance |
    |---|-------|---------|------|------|-----|-----------|-----------|
    | 1 | ... | ... | 2024 | Journal | 10.xxx | 45 | HIGH |

    ## {Research Unit 2}
    ...

    ## Search Log
    - Query: "..." → N results
    - Recency filter applied: {max_age_years} years
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
    - Apply recency filter

    OUTPUT: Write to research/{slug}/discovery/practitioner.md
  activeForm: "Discovering practitioner sources"
```

**SPAWN AGENT 3: Counterevidence Discovery** (REQUIRED for standard+)

Spawn if: `preset in ['standard', 'thorough', 'decision-support']` (Safety Gate B enforcement)

```
TaskCreate:
  subject: "Counterevidence Discovery for {slug}"
  description: |
    You are a Counterevidence Discovery Agent. Find critiques and limitations.

    IMPORTANT: This is REQUIRED by Safety Gate B for standard+ presets.

    CONTEXT: {same as above}

    QUERY PATTERNS:
    - "{term}" limitations challenges problems
    - "{term}" failed failure postmortem
    - "{term}" criticism critique
    - "{term}" why not alternative
    - "{term}" does not work

    TOOLS: Same as Practitioner agent

    OUTPUT: Write to research/{slug}/discovery/counterevidence.md
  activeForm: "Discovering counterevidence"
```

**SPAWN AGENT 4: Grey Literature Discovery** (BLUEPRINT only)

Only spawn if: `deliverable == 'BLUEPRINT'`

```
TaskCreate:
  subject: "Grey Literature Discovery for {slug}"
  description: |
    You are a Grey Literature Discovery Agent. Find standards and government reports.

    CONTEXT: {same as above}

    TARGET SOURCES:
    - NIST publications (csrc.nist.gov, nvd.nist.gov)
    - RAND Corporation (rand.org)
    - Standards bodies: IEEE, ISO, W3C, IETF RFCs
    - Government technical reports (.gov domains)
    - Major vendor architecture guides (AWS, Google, Microsoft whitepapers)

    SEARCH STRATEGY:
    - site:nist.gov "{term}"
    - site:rand.org "{term}"
    - "{term}" standard specification RFC

    TOOLS:
    1. ToolSearch "+exa" → mcp__exa__web_search_exa

    OUTPUT: Write to research/{slug}/discovery/grey_literature.md
  activeForm: "Discovering grey literature"
```

Wait for all discovery agents to complete.

**SNOWBALL EXPANSION** (if enabled in STATE.json)

After keyword discovery completes:

```
TaskCreate:
  subject: "Citation Snowball for {slug}"
  description: |
    You are a Citation Snowball Agent. Expand sources via citation networks.

    CONTEXT:
    - Slug: {slug}
    - Max seeds per unit: {config.snowball.max_seeds_per_unit}
    - Max snowball sources: {config.snowball.max_snowball_sources}
    - Recency Policy: {recency_policy}

    PROCESS:
    1. Read research/{slug}/discovery/academic.md
    2. Select top {max_seeds_per_unit} most-cited papers per unit as seeds
    3. For each seed with DOI:
       a. BACKWARD: ToolSearch "+openalex references" → mcp__openalex__get_work_references
       b. FORWARD: ToolSearch "+openalex citations" → mcp__openalex__get_work_citations
    4. Filter results by recency policy
    5. Deduplicate against existing sources
    6. Select top {max_snowball_sources} most relevant additions

    OUTPUT FORMAT (write to research/{slug}/discovery/snowball.md):
    ```
    # Citation Snowball Results

    ## Seeds Used
    | Unit | Seed Title | DOI | Backward Found | Forward Found |
    |------|------------|-----|----------------|---------------|

    ## New Sources (Backward - References)
    | # | Title | Authors | Year | DOI | Found Via |
    |---|-------|---------|------|-----|-----------|

    ## New Sources (Forward - Citing)
    | # | Title | Authors | Year | DOI | Found Via |
    |---|-------|---------|------|-----|-----------|

    ## Duplicates Filtered
    - {title} - already in academic.md
    ```
  activeForm: "Expanding via citation snowball"
```

---

## PHASE 3: CURATE

**Objective**: Merge, deduplicate, check retractions, resolve full-text access.

### Instructions

1. Read all discovery files from `research/{slug}/discovery/`
2. Read `research/{slug}/STATE.json` for tier_targets and gates

3. **Deduplication Pipeline**:

```javascript
// Generate canonical key
function canonicalKey(source) {
  if (source.doi) {
    return `doi:${source.doi.toLowerCase()}`
  }
  // Fingerprint: normalized title + first author last name + year
  const titleNorm = source.title.toLowerCase().replace(/[^a-z0-9]/g, '').slice(0, 50)
  const authorLast = source.authors[0]?.split(' ').pop()?.toLowerCase() || 'unknown'
  return `fp:${titleNorm}|${authorLast}|${source.year}`
}

// Merge rules when duplicates found:
// 1. Keep peer-reviewed over preprint over web
// 2. Keep version with DOI over version without
// 3. Keep version with better metadata
```

Write deduplication decisions to `research/{slug}/logs/dedup_log.json`:
```json
{
  "timestamp": "2024-01-01T00:00:00Z",
  "total_before": 45,
  "total_after": 32,
  "merges": [
    {
      "canonical_key": "doi:10.1234/example",
      "kept": { "title": "...", "source": "academic.md", "reason": "peer-reviewed" },
      "dropped": [{ "title": "...", "source": "practitioner.md", "reason": "preprint duplicate" }]
    }
  ]
}
```

4. **Retraction Check** (Gate C):

For each source with DOI:
```
Use mcp__crossref__getWorkByDOI to check metadata
Look for: "update-to" field with type "retraction"
```

Write to `research/{slug}/logs/retraction_flags.json`:
```json
{
  "timestamp": "2024-01-01T00:00:00Z",
  "checked": 25,
  "retractions_found": [
    { "doi": "10.xxx", "title": "...", "retraction_date": "2023-06-01" }
  ],
  "gate_status": "passed"
}
```

**REMOVE retracted papers from source list.**

5. **Full-Text Resolution** (Unpaywall):

For each source with DOI, attempt full-text resolution:

```
WebFetch:
  url: https://api.unpaywall.org/v2/{doi}?email=research@example.com
  prompt: "Extract: is_oa (boolean), best_oa_location.url, best_oa_location.url_for_pdf"
```

Assign access depth tags:
- **FULLTEXT**: `is_oa == true` AND OA URL accessible
- **ABSTRACT_ONLY**: No OA version, but abstract available
- **PAYWALLED**: No accessible version found

For arXiv papers: Use `mcp__arxiv__read_paper` for full text.

6. **Quality Filtering**:
   - Apply tier_targets from STATE.json
   - Remove sources below relevance threshold
   - Ensure minimum coverage per research unit
   - Track access_depth statistics

7. **Write SOURCES.md**:

```markdown
# Sources: {slug}

## Summary
- Total: N sources
- Academic: N% | Practitioner: N% | Other: N%
- Per unit: {unit1: N, unit2: N, ...}
- Access: FULLTEXT: N | ABSTRACT_ONLY: N | PAYWALLED: N
- Retractions removed: N

## By Research Unit

### {Unit 1}
| # | Title | Type | Year | DOI | Access | Tier |
|---|-------|------|------|-----|--------|------|
| S1 | ... | ACADEMIC | 2024 | 10.xxx | FULLTEXT | 1 |
| S2 | ... | ACADEMIC | 2023 | 10.yyy | ABSTRACT_ONLY | 1 |

### {Unit 2}
...

## Filtered (excluded)
| Title | Reason |
|-------|--------|
| ... | Low relevance |
| ... | Retracted |
| ... | Duplicate of S3 |
```

Write to `research/{slug}/SOURCES.md`

8. **Update STATE.json statistics**:
```json
{
  "statistics": {
    "sources_found": 45,
    "sources_deduplicated": 32,
    "fulltext_resolved": 18,
    "abstract_only": 10,
    "paywalled": 4,
    "retractions_found": 1
  },
  "gates": {
    "retraction_gate": { "status": "passed", "removed": 1 }
  }
}
```

---

## PHASE 4: EXTRACT

**Objective**: Extract essential information with depth tagging and structured extraction.

### Extraction Rules

Read `research/{slug}/STATE.json` for extraction_depth:
- **light** (quick): Extract top 2 per unit
- **medium** (standard): Extract top 3 per unit
- **deep** (thorough): Extract top 5 per unit

### v2.0 Extraction Template (11 Fields)

```markdown
## Source: {title}

- **Citation**: {full formatted citation}
- **Type**: ACADEMIC | PRACTITIONER | OTHER
- **Tier**: 1 | 2 | 3
- **Extraction depth**: FULLTEXT | ABSTRACT_ONLY | PAYWALLED
- **Source URL**: {accessible URL - OA link or original}
- **Sections extracted**: {e.g., "Abstract, Methods, Results, Discussion"}
- **Main claim**: {one sentence}
- **Key evidence**: "{quote or data point}" (p. X / Section Y)
- **Limitations**: {what this source doesn't cover or gets wrong}
- **Relevance**: {which research unit}
- **Notes**: {optional additional context}
```

### Instructions

1. Read `research/{slug}/SOURCES.md`
2. For each research unit, select top N sources based on extraction_depth
3. **Prioritize FULLTEXT sources** for extraction

4. Spawn extraction agents (batch 3-4 sources each):

```
TaskCreate:
  subject: "Extract Batch {N} for {slug}"
  description: |
    Extract evidence from these sources using the v2.0 template.

    SOURCES:
    {list with URLs and access tags}

    TOOLS:
    1. ToolSearch "+firecrawl" → mcp__firecrawl__firecrawl_scrape
    2. For arXiv: ToolSearch "+arxiv read" → mcp__arxiv__read_paper
    3. For OA PDFs: Use Firecrawl on the OA URL

    TEMPLATE (per source - 11 fields):
    - Citation: {full}
    - Type: ACADEMIC | PRACTITIONER | OTHER
    - Tier: 1 | 2 | 3
    - Extraction depth: FULLTEXT | ABSTRACT_ONLY | PAYWALLED
    - Source URL: {accessible URL}
    - Sections extracted: {list sections you could access}
    - Main claim: {one sentence}
    - Key evidence: "{quote}" (location)
    - Limitations: {caveats}
    - Relevance: {unit}
    - Notes: {optional}

    RULES:
    - For FULLTEXT: Extract from Methods, Results, Discussion
    - For ABSTRACT_ONLY: Note limitation, extract what's available
    - Track which sections you actually accessed
    - For paywalled: Try OA URL from SOURCES.md first

    OUTPUT: Write to research/{slug}/topics/{unit_slug}/findings.md
  activeForm: "Extracting from batch {N}"
```

5. **Structured Extraction** (VERDICT/COMPARISON only):

If `STATE.json.config.structured_extraction == true`:

```
TaskCreate:
  subject: "Structured Extraction for {slug}"
  description: |
    Extract structured data for comparison/verdict synthesis.

    CONTEXT:
    - Deliverable: {VERDICT or COMPARISON}
    - Research Units: {units}

    FOR EACH SOURCE, EXTRACT:

    1. benchmark_results (if present):
       - metric: {name of metric}
       - value: {numeric value}
       - dataset: {benchmark dataset name}
       - conditions: {any qualifiers}

    2. statistical_claims (if present):
       - claim: {the statistical statement, e.g., "p < 0.01"}
       - context: {what was being compared}
       - sample_size: {if mentioned}

    3. comparisons (if present):
       - item_a: {first thing compared}
       - item_b: {second thing compared}
       - dimension: {what dimension - speed, accuracy, cost, etc.}
       - winner: {which performed better, or "tie"}
       - margin: {quantified difference if available}

    OUTPUT FORMAT (write to research/{slug}/topics/{unit}/findings_structured.json):
    ```json
    {
      "unit": "{unit}",
      "extractions": [
        {
          "source_id": "S1",
          "benchmark_results": [...],
          "statistical_claims": [...],
          "comparisons": [...]
        }
      ]
    }
    ```
  activeForm: "Extracting structured data"
```

6. Wait for all extraction agents to complete

---

## PHASE 5: COMPILE

**Objective**: Build claims registry with gate enforcement.

### Instructions

1. Read all findings files from `research/{slug}/topics/*/findings.md`
2. Read structured extractions if present: `research/{slug}/topics/*/findings_structured.json`

3. **Build Claims Registry**:
   - Group related claims by theme
   - Calculate confidence for each claim
   - Track access depth of supporting sources

4. **v2.0 Confidence Calculation with Depth Gate**:

```javascript
function calculateConfidence(sources) {
  const agree = sources.filter(s => s.supports_claim)
  const disagree = sources.filter(s => s.contradicts_claim)

  if (disagree.length > 0 && disagree.some(s => s.tier <= 2)) {
    return 'CONTESTED'
  }

  const tier1or2 = agree.filter(s => s.tier <= 2)
  const fulltext = agree.filter(s => s.extraction_depth === 'FULLTEXT')
  const fulltextTier1or2 = tier1or2.filter(s => s.extraction_depth === 'FULLTEXT')

  // Gate A: HIGH requires >= 2 FULLTEXT from Tier 1/2
  if (tier1or2.length >= 3 && fulltextTier1or2.length >= 2) {
    return 'HIGH'
  }

  return 'LOW'
}
```

5. **Gate Enforcement**:

**Gate A (Depth Gate)**:
- Check each HIGH confidence claim
- If < 2 FULLTEXT Tier-1/2 sources: downgrade to LOW
- Log downgrades in claims.md

**Gate C (Retraction Gate)**:
- Already enforced in Phase 3
- Verify no retracted sources in any claims

6. **Contradiction Handling**:
   - If `contested_flag` from STATE.json OR deliverable is VERDICT/COMPARISON:
     - Run full contradiction analysis
     - Use structured extraction data if available
     - Write to `research/{slug}/synthesis/contradictions.md`
   - Otherwise: Just note disagreements without heavy protocol

7. **Write claims.md**:

```markdown
# Claims Registry: {slug}

## Gate Status
- Depth Gate (A): {PASSED/FAILED - N claims downgraded}
- Safety Gate (B): {PASSED - counterevidence reviewed}
- Retraction Gate (C): {PASSED - N retractions removed}

## Research Unit: {unit1}

### Claim 1: {statement}
- **Confidence**: HIGH | LOW | CONTESTED
- **Sources**: S1 (FULLTEXT, T1), S4 (FULLTEXT, T2), S7 (ABSTRACT_ONLY, T1)
- **FULLTEXT support**: 2/3 sources
- **Evidence**: "{supporting quote}"
- **Gate A check**: PASSED (2 FULLTEXT T1/T2)

### Claim 2: {statement}
- **Confidence**: LOW (downgraded from HIGH - insufficient FULLTEXT)
- **Sources**: S2 (ABSTRACT_ONLY, T1), S3 (ABSTRACT_ONLY, T1), S5 (FULLTEXT, T2)
- **FULLTEXT support**: 1/3 sources
- **Evidence**: "{supporting quote}"
- **Gate A check**: FAILED - only 1 FULLTEXT

## Research Unit: {unit2}
...

## Contradictions (if any)
| Topic | Position A | Position B | Status |
|-------|------------|------------|--------|
| ... | S1, S3 say X | S5 says Y | UNRESOLVED |

## Structured Data Summary (if VERDICT/COMPARISON)
### Benchmark Comparisons
| Metric | Option A | Option B | Source |
|--------|----------|----------|--------|
| F1 Score | 0.87 | 0.82 | S1 |

### Statistical Claims
| Claim | Context | Source |
|-------|---------|--------|
| p < 0.01 | A vs B performance | S2 |
```

Write to `research/{slug}/claims.md`

8. **Update STATE.json gates**:
```json
{
  "gates": {
    "depth_gate": { "status": "passed", "claims_downgraded": 2 },
    "safety_gate": { "status": "passed", "counterevidence_sources": 5 },
    "retraction_gate": { "status": "passed", "removed": 1 }
  }
}
```

---

## PHASE 6: SYNTHESIZE

**Objective**: Generate the primary research deliverable.

### Instructions

1. Read:
   - `research/{slug}/SPEC.md` (deliverable type)
   - `research/{slug}/claims.md`
   - `research/{slug}/SOURCES.md`
   - Structured extractions if present

2. **Verify Gates Before Synthesis**:
   - Read STATE.json gates status
   - If Safety Gate (B) failed: STOP, counterevidence must complete first
   - Log any gate failures in deliverable

3. **Generate Deliverable** based on type:

**VERDICT** (recommendation):
```markdown
# Verdict: {research question}

## Gate Compliance
- All gates passed: YES/NO
- Claims downgraded due to access: N

## Recommendation
**{RECOMMENDED OPTION}** - Confidence: HIGH | LOW

## Comparison Matrix
| Factor | Option A | Option B | Evidence |
|--------|----------|----------|----------|
| {factor} | {assessment} | {assessment} | S1, S4 |

## Quantitative Comparison (from structured extraction)
| Metric | Option A | Option B | Winner |
|--------|----------|----------|--------|
| {metric} | {value} | {value} | {A/B/Tie} |

## Key Evidence
### For {recommended}:
- {claim} [HIGH] - Sources: S1 (FULLTEXT), S4 (FULLTEXT)

### Against alternatives:
- {claim} [LOW - ABSTRACT_ONLY sources] - Source: S2

## Caveats
- {limitation 1}
- {Claims limited by paywall access: list}

## Sources
[Numbered list with access tags]
```

**REPORT** (comprehensive):
```markdown
# Report: {topic}

## Gate Compliance
- All gates passed: YES/NO

## Summary
{2-3 paragraphs}

## Findings

### {Research Unit 1}
{Evidence-based narrative}

**Key claims:**
- {claim} [HIGH confidence - 3 FULLTEXT sources]
- {claim} [LOW confidence - single source / ABSTRACT_ONLY]

### {Research Unit 2}
...

## Limitations
- {what couldn't be determined}
- {access limitations: N sources PAYWALLED}

## Sources
[Numbered list with access tags]
```

**COMPARISON** (neutral analysis):
```markdown
# Comparison: {options}

## Gate Compliance
- All gates passed: YES/NO

## Matrix
| Criterion | Option A | Option B | Confidence | Sources |
|-----------|----------|----------|------------|---------|

## Quantitative Data
{Table from structured extraction}

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

## Gate Compliance
- All gates passed: YES/NO
- Grey literature included: YES

## Overview
{What this achieves}

## Architecture
{High-level design}

## Implementation Steps
### Step 1: {action}
- Evidence basis: {citation} [confidence]
- Standards reference: {grey literature citation if applicable}
- Common pitfalls: {warning}

## Best Practices
{Evidence-based recommendations}

## Relevant Standards
{From grey literature pass}

## Sources
```

**BIBLIOGRAPHY** (annotated sources):
```markdown
# Bibliography: {topic}

## Summary
- Total sources: N
- Access: FULLTEXT: N | ABSTRACT_ONLY: N | PAYWALLED: N

## Essential Reading
### {Citation}
- Access: FULLTEXT | ABSTRACT_ONLY
- Summary: {what it covers}
- Key insight: {main contribution}
- Quality: {assessment}

## Supplementary
...
```

4. Write to `research/{slug}/synthesis/final_deliverable.md`

---

## PHASE 7: CRITIQUE

**Objective**: Self-assess research quality with gate compliance (max 1 page).

### Instructions

1. Read:
   - `research/{slug}/synthesis/final_deliverable.md`
   - `research/{slug}/SOURCES.md`
   - `research/{slug}/claims.md`
   - `research/{slug}/STATE.json`

2. **Generate Critique** (concise, 1 page max):

```markdown
# Critique: {slug}

## Gate Compliance Summary
| Gate | Status | Impact |
|------|--------|--------|
| Depth (A) | PASSED/FAILED | {N claims downgraded} |
| Safety (B) | PASSED/FAILED | {counterevidence status} |
| Retraction (C) | PASSED/FAILED | {N removed} |

## Completeness
| Research Unit | Sources | FULLTEXT | Confidence | Gaps |
|---------------|---------|----------|------------|------|
| {unit1} | N | N/N | HIGH/LOW | {any gaps} |

## Source Quality
- Academic: N% (target: {target}%)
- Tier 1: N sources
- Access breakdown:
  - FULLTEXT: N sources (can support HIGH confidence)
  - ABSTRACT_ONLY: N sources (limits confidence)
  - PAYWALLED: N sources (impact: {low/medium/high})

## Confidence Summary
- HIGH confidence claims: N (all with >=2 FULLTEXT T1/T2)
- LOW confidence claims: N
  - Due to insufficient sources: N
  - Due to access limitations: N
- CONTESTED claims: N

## Key Limitations
1. {Most important limitation}
2. {Access-related limitation}
3. {Coverage gap}

## What Could Invalidate Conclusions
- If {assumption} is false, then {consequence}
- If paywalled sources {S3, S7} contradict, then {impact}

## Recommended Follow-Up
- {Specific action to strengthen findings}
- {Sources worth obtaining full access to}
```

3. Write to `research/{slug}/synthesis/critique.md`

4. **Update STATE.json**:
```json
{
  "phase": "complete",
  "completed_at": "2024-01-01T12:00:00Z",
  "summary": {
    "sources": 25,
    "claims": 12,
    "high_confidence": 5,
    "low_confidence": 6,
    "contested": 1,
    "fulltext_rate": 0.72,
    "all_gates_passed": true
  }
}
```

5. **Present Summary to User**:

```
## Research Complete: {slug}

### Gate Status
- All gates PASSED ✓

### Key Findings
{3-5 bullet summary}

### Confidence Profile
- HIGH confidence claims: N
- LOW confidence claims: N
- CONTESTED claims: N
- Full-text access rate: N%

### Files Created
- `synthesis/final_deliverable.md` - Main output
- `synthesis/critique.md` - Quality assessment
- `claims.md` - Evidence registry with gate checks
- `SOURCES.md` - Source list with access tags
- `logs/dedup_log.json` - Deduplication decisions
- `logs/retraction_flags.json` - Retraction check results

### Access Limitations
- {N} sources were ABSTRACT_ONLY
- {N} sources were PAYWALLED

What would you like to explore further?
```

---

## ERROR HANDLING

**SPEC not found**: STOP, inform user to create SPEC.md first

**Discovery fails**: Continue with successful agents, note gaps

**Extraction fails**: Tag as ABSTRACT_ONLY, note limitation

**Sources insufficient**: Broaden search, accept partial coverage, document in critique

**Gate failures**:
- Depth Gate: Downgrade confidence, continue
- Safety Gate: MUST complete counterevidence before synthesis
- Retraction Gate: Remove source, recalculate claims

**Unpaywall API fails**: Fall back to ABSTRACT_ONLY tag, note in logs

---

## FILE STRUCTURE (v2.0)

```
research/{slug}/
├── SPEC.md                      # Input specification
├── STATE.json                   # Workflow state v2.0 (with gates, config)
├── SOURCES.md                   # Curated source list with access tags
├── claims.md                    # Evidence registry with gate checks
├── discovery/
│   ├── academic.md              # Academic pass results
│   ├── practitioner.md          # Practitioner pass (if run)
│   ├── counterevidence.md       # Counterevidence pass (standard+)
│   ├── grey_literature.md       # Grey literature (BLUEPRINT only)
│   └── snowball.md              # Citation snowball expansion
├── topics/
│   ├── {unit1_slug}/
│   │   ├── findings.md          # Extracted evidence (11 fields)
│   │   └── findings_structured.json  # Structured extraction (VERDICT/COMPARISON)
│   ├── {unit2_slug}/
│   │   ├── findings.md
│   │   └── findings_structured.json
│   └── ...
├── synthesis/
│   ├── final_deliverable.md     # PRIMARY OUTPUT
│   ├── critique.md              # Quality assessment with gate compliance
│   └── contradictions.md        # If contested
└── logs/
    ├── runlog.ndjson            # Tool execution log
    ├── checkpoint.md            # Resume checkpoint
    ├── dedup_log.json           # Deduplication decisions
    └── retraction_flags.json    # Retraction check results
```

---

## TOOL REFERENCE

### Discovery
- `mcp__openalex__search_works` - Academic papers
- `mcp__openalex__get_work_references` - Backward snowball (citations in paper)
- `mcp__openalex__get_work_citations` - Forward snowball (papers citing this)
- `mcp__arxiv__search_papers` - Preprints
- `mcp__exa__web_search_exa` - Web sources, grey literature
- `mcp__crossref__searchByTitle` - Title lookup

### Extraction
- `mcp__firecrawl__firecrawl_scrape` - Web content, OA PDFs
- `mcp__arxiv__read_paper` - arXiv full text

### Verification & Access
- `mcp__crossref__getWorkByDOI` - DOI validation, retraction check
- `WebFetch` to Unpaywall API - Full-text resolution:
  ```
  https://api.unpaywall.org/v2/{doi}?email=research@example.com
  ```

### Unpaywall Response Fields
```json
{
  "is_oa": true,
  "best_oa_location": {
    "url": "https://...",
    "url_for_pdf": "https://...",
    "license": "cc-by"
  }
}
```
