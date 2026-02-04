# Research ADE v5.0 - Schemas and Rubrics

Comprehensive reference for the Research ADE system with gates, full-text access, failure analysis, and implementation specifications.

---

## 1. SPEC Schema

### Required Sections

```yaml
goal: string                      # What to build/implement (NOT a question)
success_criteria:                 # What HIGH confidence looks like
  - criterion: string
research_units:                   # 1-5 focused areas
  - name: string
    key_terms: [string]
deliverables: enum               # SPECIFICATION | VERDICT | REPORT | COMPARISON | BLUEPRINT | BIBLIOGRAPHY
context:
  use_case: string               # What user is trying to accomplish
  constraints: string            # Technical/budget/timeline limits
  expertise: string              # Team background
  existing_work: string          # What's already known/tried
```

### Optional Sections

```yaml
prior_art_hints: [string]        # Known starting points
constraints:
  time_period: string            # Default: based on recency_policy
  excluded: [string]             # Sources/perspectives to exclude
key_search_terms: [string]       # Auto-generate if missing
preset: enum                     # quick | standard | thorough | decision-support
domain_hint: enum                # fast_moving | scientific | historical (for recency)
```

---

## 2. STATE.json Schema

Written by Phase 1 (Parse), read by all subsequent phases.

```json
{
  "version": "3.0",
  "slug": "project-name",
  "preset": "standard",
  "posture": "optimistic-empirical",
  "min_sources_per_unit": 3,
  "extraction_depth": "medium",
  "tier_targets": {
    "academic": 70,
    "practitioner": 25,
    "other": 5
  },
  "research_units": ["unit1", "unit2", "unit3"],
  "deliverable": "SPECIFICATION",
  "phase": "plan",
  "started_at": "2024-01-01T00:00:00Z",
  "completed_at": null,
  "plan_approved": false,
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
    "depth_gate": {
      "required_fulltext": 2,
      "status": "pending"
    },
    "completion_gate": {
      "requires_high_confidence": true,
      "status": "pending",
      "gaps_declared": []
    },
    "retraction_gate": {
      "status": "pending"
    }
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

### Config Block Reference

| Field | Type | Description |
|-------|------|-------------|
| `posture` | string | `"optimistic-empirical"` (default) |
| `recency_policy` | enum | `fast_moving` \| `scientific` \| `historical` |
| `max_age_years` | number \| null | 1.5 for fast_moving, 5 for scientific, null for historical |
| `foundational_exception` | boolean | Include seminal papers regardless of age |
| `snowball.enabled` | boolean | True for >= standard preset |
| `failure_analysis` | boolean | True for >= standard preset |
| `structured_extraction` | boolean | True for SPECIFICATION/VERDICT/COMPARISON |

### Gates Block Reference

| Gate | Purpose | Failure Action |
|------|---------|----------------|
| `depth_gate` | Ensure HIGH claims have FULLTEXT evidence | Downgrade to LOW |
| `completion_gate` | Ensure HIGH confidence or gaps declared | Block synthesis |
| `retraction_gate` | Ensure no retracted papers in claims | Remove source |

---

## 3. Source Types

### Evidence Type Labels

| Type | Meaning |
|------|---------|
| **ACADEMIC** | Peer-reviewed, conferences, theses, arXiv, patents |
| **PRACTITIONER** | Engineering blogs, docs, tutorials, case studies |
| **OTHER** | Industry whitepapers, general web content |

### Source Tiers

| Tier | Examples | Trust Level |
|------|----------|-------------|
| **1** | Journals (IF > 1.0), NeurIPS/ICML/ACL/IEEE, PhD dissertations | HIGH |
| **2** | arXiv (credentialed authors), patents, tech reports | MEDIUM |
| **3** | Expert blogs, documentation, whitepapers | LOW |

### Access Depth Tags

| Tag | Meaning | Can Support HIGH? |
|-----|---------|-------------------|
| **FULLTEXT** | Complete document accessed, 3+ sections extracted | YES |
| **ABSTRACT_ONLY** | Only abstract/metadata available | NO (contributes to LOW) |
| **PAYWALLED** | Behind paywall, no OA version found | NO (contributes to LOW) |

### Implementation Detail Flag (NEW in v5.0)

Sources are additionally tagged if they contain implementation specifics:

| Has Implementation Detail | Indicators |
|---------------------------|------------|
| **YES** | Code snippets, pseudocode, architecture diagrams, parameter tables, reproducibility sections |
| **NO** | Theory only, conceptual, survey without specifics |

---

## 4. Confidence Levels (with Completion Gate)

| Level | Requirement |
|-------|-------------|
| **HIGH** | 3+ Tier-1/2 sources agree AND 2+ are FULLTEXT AND (for recommendations) implementation detail present |
| **LOW** | 1-2 sources OR only Tier-2/3 OR insufficient FULLTEXT OR no implementation detail |
| **CONTESTED** | Credible sources disagree |

**Decision Tree:**
```
Do sources agree?
├── No (credible disagreement) → CONTESTED
└── Yes → Are there 3+ Tier-1/2 sources?
    ├── No → LOW
    └── Yes → Are >= 2 of them FULLTEXT?
        ├── No → LOW (Depth Gate downgrade)
        └── Yes → Is this a recommendation claim?
            ├── No → HIGH
            └── Yes → Has implementation detail?
                ├── Yes → HIGH
                └── No → LOW (need implementation specifics)
```

**Completion Gate Enforcement:**
- Before synthesis, verify:
  - All recommendation claims have HIGH confidence, OR
  - LOW confidence claims have explicit gap declarations
- If check fails: Block synthesis, require gap documentation

---

## 5. Extraction Template (12 Fields)

```markdown
## Source: {title}

- **Citation**: {Full formatted citation}
- **Type**: ACADEMIC | PRACTITIONER | OTHER
- **Tier**: 1 | 2 | 3
- **Extraction depth**: FULLTEXT | ABSTRACT_ONLY | PAYWALLED
- **Has implementation detail**: YES | NO
- **Source URL**: {Accessible URL - OA link preferred}
- **Sections extracted**: {e.g., "Abstract, Introduction, Methods, Results, Discussion"}
- **Main claim**: {One sentence summary}
- **Key evidence**: "{Quote or data point}" (p. X / Section Y)
- **Implementation specifics**: {Methods, parameters, architecture if present}
- **Limitations**: {What this source doesn't cover}
- **Relevance**: {Which research unit}
```

### Field Descriptions

| Field | Required | Description |
|-------|----------|-------------|
| Citation | Yes | Full academic citation format |
| Type | Yes | ACADEMIC / PRACTITIONER / OTHER |
| Tier | Yes | 1, 2, or 3 |
| Extraction depth | Yes | FULLTEXT / ABSTRACT_ONLY / PAYWALLED |
| Has implementation detail | Yes | YES / NO |
| Source URL | Yes | Best available URL (OA preferred) |
| Sections extracted | Yes | List of sections actually accessed |
| Main claim | Yes | Single sentence summary |
| Key evidence | Yes | Direct quote with location |
| Implementation specifics | If present | Methods, parameters, configuration |
| Limitations | Yes | Caveats and gaps |
| Relevance | Yes | Which research unit |

---

## 6. Failure Analysis Schema (NEW in v5.0)

### Failure Study Template

```markdown
## Failure Study: {source title}

### Context
- **Method Attempted**: {specific approach they tried}
- **Domain**: {application area}
- **Scale**: {size/scope of the attempt}
- **Timeframe**: {when this was attempted}

### Failure Description
- **What Failed**: {observable failure mode}
- **Root Cause**: {underlying reason}
- **When Discovered**: {at what stage - development, testing, production}

### Lessons Learned
1. {lesson 1}
2. {lesson 2}
3. {lesson 3}

### Risk-Mitigation Pair
| Risk | Likelihood | Impact | Mitigation | Evidence |
|------|------------|--------|------------|----------|
| {risk from this failure} | H/M/L | H/M/L | {how to prevent/handle} | {source citation} |
```

### Aggregated Risk-Mitigation Table

Compile all failure studies into:

```markdown
# Risk-Mitigation Summary

| # | Risk | Category | Mitigation | Confidence | Source |
|---|------|----------|------------|------------|--------|
| R1 | {risk} | {data/model/system/process} | {mitigation} | HIGH/LOW | S3, S7 |
| R2 | {risk} | {category} | {mitigation} | HIGH/LOW | S12 |
```

---

## 7. Deliverable Formats

### SPECIFICATION (implementation guidance) - NEW DEFAULT

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
- Alternatives Considered: {what else exists, why not chosen}

**Implementation Details**:
- Input: {what it needs}
- Output: {what it produces}
- Key Parameters: {configuration from sources}
- Dependencies: {what must come first}

### Component 2: {name}
...

## Implementation Sequence

```
Step 1: {name} ─depends on→ nothing
Step 2: {name} ─depends on→ Step 1
Step 3: {name} ─depends on→ Step 1, Step 2
...
```

### Step 1: {name}
- **What**: {description}
- **Method**: {specific approach}
- **Evidence Basis**: S1, S4 [HIGH confidence]
- **Key Considerations**: {from failure studies}

### Step 2: {name}
...

## Data Requirements

| Data Type | Source | Format | Update Frequency | Evidence |
|-----------|--------|--------|------------------|----------|
| {type} | {source} | {format} | {frequency} | S2 |

## Risk-Mitigation Table

| # | Risk | Likelihood | Impact | Mitigation | Evidence |
|---|------|------------|--------|------------|----------|
| R1 | {from failure studies} | H/M/L | H/M/L | {specific mitigation} | S3, S7 |

## Validation Approach

### Recommended Metrics
| Metric | Target | Rationale | Evidence |
|--------|--------|-----------|----------|
| {metric} | {target value} | {why this target} | S5 |

### Testing Strategy
1. {validation step 1}
2. {validation step 2}

## Known Gaps (if any)

### Gap 1: {what is unknown}
- **Impact**: {why this matters}
- **Blocking**: {what can't be determined}
- **Resolution Path**: {what research would help}

## Sources

### Primary (HIGH confidence basis)
| # | Title | Year | Access | Implementation Detail | Relevance |
|---|-------|------|--------|----------------------|-----------|
| S1 | {title} | {year} | FULLTEXT | YES | {how used} |

### Supporting
| # | Title | Year | Access | Relevance |
|---|-------|------|--------|-----------|

### Failure Studies
| # | Title | Year | Key Lesson |
|---|-------|------|------------|
```

### VERDICT (recommendation)

```markdown
# Verdict: {decision question}

## Gate Compliance
- Depth Gate (A): PASSED/FAILED
- Completion Gate (B): PASSED/FAILED
- Retraction Gate (C): PASSED

## Recommendation
**{OPTION}** - Confidence: HIGH | LOW (with gaps)

## Comparison Matrix
| Factor | Option A | Option B | Evidence |
|--------|----------|----------|----------|
| {factor} | {assessment} | {assessment} | S1, S4 |

## Quantitative Comparison
| Metric | Option A | Option B | Winner | Source |
|--------|----------|----------|--------|--------|
| {metric} | {value} | {value} | A/B/Tie | S2 |

## Key Evidence
### For {recommended}:
- {claim} [HIGH] - Sources: S1 (FULLTEXT), S4 (FULLTEXT)

### Against alternatives:
- {claim} [HIGH] - Sources: S2 (FULLTEXT), S5 (FULLTEXT)

## Risk-Mitigation for Chosen Option
| Risk | Mitigation | Evidence |
|------|------------|----------|
| {risk} | {mitigation} | S7 |

## Caveats
- {limitation 1}
- {access limitations}

## Sources
[Numbered list with access tags]
```

### REPORT (comprehensive)

```markdown
# Report: {topic}

## Gate Compliance
- All gates: PASSED/FAILED

## Summary
{2-3 paragraphs}

## Findings

### {Research Unit 1}
{Evidence-based narrative}

**Key claims:**
- {claim} [HIGH confidence] - 3 FULLTEXT sources
- {claim} [LOW confidence] - reason

### {Research Unit 2}
...

## Limitations
- {gaps}
- {access limitations}

## Sources
[Numbered list with access tags]
```

### COMPARISON (neutral)

```markdown
# Comparison: {options}

## Gate Compliance
- All gates: PASSED/FAILED

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
### Strengths
### Weaknesses
### Best for

## Selection Guidance
- Choose A when: {conditions}
- Choose B when: {conditions}

## Sources
[with access tags]
```

### BLUEPRINT (architecture)

```markdown
# Blueprint: {topic}

## Gate Compliance
- All gates: PASSED/FAILED
- Grey literature: INCLUDED

## Overview
{What this achieves}

## Architecture
{High-level design}

## Implementation Steps
### Step 1: {action}
- Evidence basis: {citation} [confidence]
- Standards reference: {grey literature citation if applicable}
- Common pitfalls: {from failure studies}

## Best Practices
{Evidence-based recommendations}

## Relevant Standards
{From grey literature pass}

## Sources
```

### BIBLIOGRAPHY (annotated)

```markdown
# Bibliography: {topic}

## Summary
- Total sources: N
- Access: FULLTEXT: N | ABSTRACT_ONLY: N | PAYWALLED: N
- Implementation detail: N sources

## Essential Reading
### {Citation}
- Access: FULLTEXT | ABSTRACT_ONLY
- Has implementation detail: YES | NO
- Summary: {coverage}
- Key insight: {contribution}

## Supplementary
...
```

---

## 8. Recency Policy

### Domain Detection

| Domain | Indicators | Max Age |
|--------|-----------|---------|
| **fast_moving** | LLM, GPT, transformer, crypto, blockchain, "latest", "current state" | 18 months |
| **scientific** | Default for academic topics | 5 years |
| **historical** | Philosophy, history, "origins", "foundational" | No limit |

### Application Rules

1. Apply max_age filter during discovery
2. **Exception**: Seminal/foundational papers always included
3. Mark foundational papers with `[FOUNDATIONAL]` tag
4. Prefer recent over old when equal quality

---

## 9. Deduplication Pipeline

### Canonical Key Generation

```javascript
function canonicalKey(source) {
  // Priority 1: DOI (normalized)
  if (source.doi) {
    return `doi:${source.doi.toLowerCase().trim()}`
  }

  // Priority 2: Fingerprint
  const titleNorm = source.title
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, '')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, 50)

  const authorLast = extractLastName(source.authors?.[0]) || 'unknown'
  const year = source.year || 'unknown'

  return `fp:${titleNorm}|${authorLast}|${year}`
}
```

### Merge Rules

| Scenario | Keep | Drop |
|----------|------|------|
| Peer-reviewed vs preprint | Peer-reviewed | Preprint |
| With DOI vs without | With DOI | Without |
| FULLTEXT vs ABSTRACT_ONLY | FULLTEXT | ABSTRACT_ONLY |
| Has implementation detail vs not | With detail | Without (if same source) |
| More metadata vs less | More complete | Less complete |

---

## 10. Retraction Check

### Process

1. For each source with DOI, query Crossref
2. Check `message.update-to` field for retraction notices
3. Check `message.is-retracted` boolean (if available)

### Log Format

```json
{
  "timestamp": "2024-01-01T00:00:00Z",
  "checked": 25,
  "retractions_found": [
    {
      "doi": "10.1234/retracted",
      "title": "Retracted Paper Title",
      "retraction_notice_doi": "10.1234/retraction",
      "retraction_date": "2023-06-01",
      "reason": "Data fabrication"
    }
  ],
  "gate_status": "passed",
  "action_taken": "removed_from_sources"
}
```

---

## 11. Unpaywall Integration

### API Endpoint

```
GET https://api.unpaywall.org/v2/{doi}?email=research@example.com
```

### Response Fields Used

| Field | Purpose |
|-------|---------|
| `is_oa` | Boolean - is open access available |
| `best_oa_location.url` | URL to OA version |
| `best_oa_location.url_for_pdf` | Direct PDF link |
| `best_oa_location.license` | License type (cc-by, etc.) |
| `best_oa_location.version` | published, accepted, submitted |

---

## 12. Citation Snowball

### Process

1. Select top N most-cited papers per unit as seeds
2. For each seed with DOI:
   - **Backward**: `mcp__openalex__get_work_references` - papers this cites
   - **Forward**: `mcp__openalex__get_work_citations` - papers citing this
3. Filter by recency policy
4. Deduplicate against existing sources
5. Add top matches up to limit

### Limits

| Preset | Snowball Enabled | Max Seeds | Max Additions |
|--------|------------------|-----------|---------------|
| quick | No | - | - |
| standard | Yes | 5 | 10 |
| thorough | Yes | 5 | 10 |
| decision-support | Yes | 5 | 10 |

---

## 13. Grey Literature Sources

### Target Domains (BLUEPRINT only)

| Source | Domain | Type |
|--------|--------|------|
| NIST | csrc.nist.gov, nvd.nist.gov | Government standards |
| RAND | rand.org | Research reports |
| IEEE | standards.ieee.org | Technical standards |
| ISO | iso.org | International standards |
| W3C | w3.org | Web standards |
| IETF | rfc-editor.org | Internet standards |
| AWS | docs.aws.amazon.com/whitepapers | Vendor architecture |
| Google | cloud.google.com/architecture | Vendor architecture |
| Microsoft | docs.microsoft.com/azure/architecture | Vendor architecture |

---

## 14. Gap Declaration Format

When a claim cannot achieve HIGH confidence, document the gap:

```markdown
## Gap: {what is unknown}

- **Claim Affected**: {the recommendation/claim this blocks}
- **Current Confidence**: LOW
- **Reason**: {why HIGH not achievable - sources, access, novelty}
- **Impact**: {what can't be determined without this}
- **Blocking**: {downstream decisions affected}
- **Resolution Path**: {what specific research would fill this gap}
  - Search: {specific queries to try}
  - Sources: {types of sources needed}
  - Experts: {who might know}
```

---

## 15. Saturation Criteria

**Stop discovery when:**
- Min sources per unit met (per preset)
- Last 2 searches returned >50% duplicates
- Key terms searched across source types
- 12 candidates max per unit (before snowball)
- Snowball returns <2 new relevant sources
- Implementation detail found for key methods

**Continue if:**
- Research unit below minimum
- No FULLTEXT sources with implementation detail for recommendations
- Critical failure mode not documented
- Completion Gate would fail

---

## 16. Critique Checklist

Before finalizing, verify:

- [ ] All gates passed (or failures documented)
- [ ] Sources meet tier targets
- [ ] HIGH claims have >= 2 FULLTEXT T1/T2 sources
- [ ] Recommendation claims have implementation detail
- [ ] All LOW claims have gap declarations
- [ ] CONTESTED claims present both sides
- [ ] Failure studies extracted risk-mitigation pairs
- [ ] Limitations documented (including access)
- [ ] Deliverable matches SPEC request
- [ ] All files written to research/{slug}/

**Max 1 page critique.**

---

## 17. Presets Reference

| Preset | Sources/Unit | Extraction | Passes | Snowball | Failure Analysis |
|--------|--------------|------------|--------|----------|------------------|
| `quick` | 2 | light | 2 | No | No |
| `standard` | 3 | medium | 3 | Yes | **Yes** |
| `thorough` | 5 | deep | 3 | Yes | **Yes** |
| `decision-support` | 4 | deep | 3 | Yes | **Yes** |

### Preset Feature Matrix

| Feature | quick | standard | thorough | decision-support |
|---------|-------|----------|----------|------------------|
| Min sources/unit | 2 | 3 | 5 | 4 |
| Extraction depth | light | medium | deep | deep |
| Snowball expansion | No | Yes | Yes | Yes |
| Failure Analysis | No | **Yes** | **Yes** | **Yes** |
| Grey literature | No | No | No | BLUEPRINT only |
| Structured extraction | No | Yes | Yes | **Yes** |
| Depth Gate (A) | No | Yes | Yes | Yes |
| Completion Gate (B) | No | Yes | Yes | Yes |

---

## 18. File Structure Reference

```
research/{slug}/
├── PLAN.md                      # Research plan (NEW - requires approval)
├── SPEC.md                      # Input specification
├── STATE.json                   # Workflow state with gates & config
├── SOURCES.md                   # Source list with access tags
├── claims.md                    # Evidence registry with gate checks
├── discovery/
│   ├── academic.md              # Academic pass
│   ├── practitioner.md          # Practitioner pass
│   ├── failure_analysis.md      # Failure studies (RENAMED from counterevidence)
│   ├── grey_literature.md       # BLUEPRINT only
│   └── snowball.md              # Citation expansion
├── topics/
│   └── {unit}/
│       ├── findings.md          # 12-field extraction
│       └── findings_structured.json  # Structured extraction
├── synthesis/
│   ├── final_deliverable.md     # PRIMARY OUTPUT
│   ├── critique.md              # With gate compliance
│   ├── risk_mitigations.md      # Compiled risk-mitigation pairs (NEW)
│   └── gaps.md                  # Explicit gap declarations (NEW, if any)
└── logs/
    ├── runlog.ndjson            # Execution log
    ├── checkpoint.md            # Resume point
    ├── dedup_log.json           # Merge decisions
    └── retraction_flags.json    # Retraction results
```

---

*Last Updated: 2026-02-04*
*Version: 5.0*
