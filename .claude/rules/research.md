# Research ADE v2.0 - Schemas and Rubrics

Comprehensive reference for the Research ADE v2.0 system with gates, full-text access, and structured extraction.

---

## 1. SPEC Schema

### Required Sections

```yaml
research_question: string        # Primary question to answer
research_units:                   # 1-5 focused areas
  - name: string
    key_terms: [string]
deliverables: enum               # VERDICT | REPORT | COMPARISON | BLUEPRINT | BIBLIOGRAPHY
user_context:
  use_case: string               # What user is trying to accomplish
  constraints: string            # Technical/budget/timeline limits
  expertise: string              # Team background
```

### Optional Sections

```yaml
constraints:
  time_period: string            # Default: based on recency_policy
  excluded: [string]             # Sources/perspectives to exclude
key_search_terms: [string]       # Auto-generate if missing
preset: enum                     # quick | standard | thorough | decision-support
domain_hint: enum                # fast_moving | scientific | historical (for recency)
```

---

## 2. STATE.json Schema v2.0

Written by Phase 1 (Parse), read by all subsequent phases.

```json
{
  "version": "2.0",
  "slug": "project-name",
  "preset": "standard",
  "contested_flag": false,
  "min_sources_per_unit": 3,
  "extraction_depth": "medium",
  "tier_targets": {
    "academic": 70,
    "practitioner": 25,
    "other": 5
  },
  "research_units": ["unit1", "unit2", "unit3"],
  "deliverable": "REPORT",
  "phase": "parse",
  "started_at": "2024-01-01T00:00:00Z",
  "completed_at": null,
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
    "depth_gate": {
      "required_fulltext": 2,
      "status": "pending"
    },
    "safety_gate": {
      "counterevidence_required": true,
      "status": "pending"
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
    "snowball_added": 0
  }
}
```

### Config Block Reference

| Field | Type | Description |
|-------|------|-------------|
| `recency_policy` | enum | `fast_moving` \| `scientific` \| `historical` |
| `max_age_years` | number \| null | 1.5 for fast_moving, 5 for scientific, null for historical |
| `snowball.enabled` | boolean | True for >= standard preset |
| `snowball.max_seeds_per_unit` | number | Max papers to use as snowball seeds |
| `snowball.max_snowball_sources` | number | Max sources to add via snowball |
| `grey_literature` | boolean | True only for BLUEPRINT deliverable |
| `structured_extraction` | boolean | True for VERDICT/COMPARISON deliverables |

### Gates Block Reference

| Gate | Purpose | Failure Action |
|------|---------|----------------|
| `depth_gate` | Ensure HIGH claims have FULLTEXT evidence | Downgrade to LOW |
| `safety_gate` | Ensure counterevidence was reviewed | Block synthesis |
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

### Access Depth Tags (v2.0)

| Tag | Meaning | Can Support HIGH? |
|-----|---------|-------------------|
| **FULLTEXT** | Complete document accessed, 3+ sections extracted | YES |
| **ABSTRACT_ONLY** | Only abstract/metadata available | NO (contributes to LOW) |
| **PAYWALLED** | Behind paywall, no OA version found | NO (contributes to LOW) |

### Never Cite

- No author attribution
- No date
- News articles (secondary)
- Forums (Reddit, StackOverflow)
- SEO/content farms
- Wikipedia (use only to find primaries)
- AI-generated (unverified)
- Retracted papers (enforced by Gate C)

---

## 4. Confidence Levels (v2.0 with Depth Gate)

| Level | Requirement | v2.0 Addition |
|-------|-------------|---------------|
| **HIGH** | 3+ Tier-1/2 academic sources agree | AND >= 2 must be FULLTEXT |
| **LOW** | 1-2 sources OR only Tier-2/3 | OR insufficient FULLTEXT access |
| **CONTESTED** | Credible sources disagree | Present both sides |

**v2.0 Decision Tree:**
```
Do sources agree?
├── No (credible disagreement) → CONTESTED
└── Yes → Are there 3+ Tier-1/2 sources?
    ├── No → LOW
    └── Yes → Are >= 2 of them FULLTEXT?
        ├── Yes → HIGH
        └── No → LOW (Depth Gate downgrade)
```

**Gate A Enforcement:**
- Before assigning HIGH confidence, verify:
  - At least 3 Tier-1 or Tier-2 sources support the claim
  - At least 2 of those sources have `extraction_depth: FULLTEXT`
- If check fails: downgrade to LOW, log reason

---

## 5. Extraction Template (v2.0 - 11 Fields)

```markdown
## Source: {title}

- **Citation**: {Full formatted citation}
- **Type**: ACADEMIC | PRACTITIONER | OTHER
- **Tier**: 1 | 2 | 3
- **Extraction depth**: FULLTEXT | ABSTRACT_ONLY | PAYWALLED
- **Source URL**: {Accessible URL - OA link preferred}
- **Sections extracted**: {e.g., "Abstract, Introduction, Methods, Results, Discussion"}
- **Main claim**: {One sentence summary}
- **Key evidence**: "{Quote or data point}" (p. X / Section Y)
- **Limitations**: {What this source doesn't cover}
- **Relevance**: {Which research unit}
- **Notes**: {Optional additional context}
```

### Field Descriptions

| Field | Required | Description |
|-------|----------|-------------|
| Citation | Yes | Full academic citation format |
| Type | Yes | ACADEMIC / PRACTITIONER / OTHER |
| Tier | Yes | 1, 2, or 3 |
| Extraction depth | Yes (v2.0) | FULLTEXT / ABSTRACT_ONLY / PAYWALLED |
| Source URL | Yes (v2.0) | Best available URL (OA preferred) |
| Sections extracted | Yes (v2.0) | List of sections actually accessed |
| Main claim | Yes | Single sentence summary |
| Key evidence | Yes | Direct quote with location |
| Limitations | Yes | Caveats and gaps |
| Relevance | Yes | Which research unit |
| Notes | No | Additional context |

---

## 6. Structured Extraction Schema (v2.0)

**Applies to**: VERDICT and COMPARISON deliverables only.

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "unit": { "type": "string" },
    "extractions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "source_id": { "type": "string" },
          "benchmark_results": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "metric": { "type": "string" },
                "value": { "type": ["number", "string"] },
                "dataset": { "type": "string" },
                "conditions": { "type": "string" },
                "source_section": { "type": "string" }
              },
              "required": ["metric", "value"]
            }
          },
          "statistical_claims": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "claim": { "type": "string" },
                "context": { "type": "string" },
                "sample_size": { "type": ["number", "string"] },
                "effect_size": { "type": "string" },
                "source_section": { "type": "string" }
              },
              "required": ["claim", "context"]
            }
          },
          "comparisons": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "item_a": { "type": "string" },
                "item_b": { "type": "string" },
                "dimension": { "type": "string" },
                "winner": { "type": "string" },
                "margin": { "type": "string" },
                "conditions": { "type": "string" },
                "source_section": { "type": "string" }
              },
              "required": ["item_a", "item_b", "dimension"]
            }
          }
        },
        "required": ["source_id"]
      }
    }
  },
  "required": ["unit", "extractions"]
}
```

### Example

```json
{
  "unit": "model-performance",
  "extractions": [
    {
      "source_id": "S1",
      "benchmark_results": [
        {
          "metric": "F1 score",
          "value": 0.87,
          "dataset": "SQuAD 2.0",
          "conditions": "zero-shot",
          "source_section": "Table 3"
        },
        {
          "metric": "Accuracy",
          "value": "92.3%",
          "dataset": "MMLU",
          "conditions": "5-shot",
          "source_section": "Section 4.2"
        }
      ],
      "statistical_claims": [
        {
          "claim": "p < 0.001",
          "context": "Model A vs Model B on reasoning tasks",
          "sample_size": 1000,
          "effect_size": "Cohen's d = 0.45",
          "source_section": "Section 5"
        }
      ],
      "comparisons": [
        {
          "item_a": "GPT-4",
          "item_b": "Claude 3",
          "dimension": "inference speed",
          "winner": "Claude 3",
          "margin": "2.3x faster",
          "conditions": "batch size 32",
          "source_section": "Figure 5"
        }
      ]
    }
  ]
}
```

---

## 7. Deliverable Formats

### VERDICT (recommendation)

```markdown
# Verdict: {question}

## Gate Compliance
- Depth Gate (A): PASSED/FAILED
- Safety Gate (B): PASSED
- Retraction Gate (C): PASSED

## Recommendation
**{OPTION}** - Confidence: HIGH | LOW

## Comparison Matrix
| Factor | Option A | Option B | Evidence |

## Quantitative Comparison
| Metric | Option A | Option B | Winner | Source |
{from structured extraction}

## Key Evidence
- {claim} [HIGH] - S1 (FULLTEXT), S4 (FULLTEXT), S7 (FULLTEXT)
- {claim} [LOW] - S2 (ABSTRACT_ONLY)

## Caveats
- {limitation}
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
{Narrative with inline citations}
- {claim} [HIGH confidence] - 3 FULLTEXT sources
- {claim} [LOW confidence] - ABSTRACT_ONLY limitation

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
| Criterion | Option A | Option B | Confidence |

## Quantitative Data
{Table from structured extraction}

## Option A
### Strengths / Weaknesses / Best for

## Selection Guidance
- Choose A when: ...
- Choose B when: ...

## Sources
[with access tags]
```

### BLUEPRINT (implementation)

```markdown
# Blueprint: {topic}

## Gate Compliance
- All gates: PASSED/FAILED
- Grey literature: INCLUDED

## Architecture
{High-level design}

## Steps
### Step 1: {action}
- Evidence: {citation}
- Standard: {grey literature reference}
- Pitfalls: {warning}

## Best Practices

## Relevant Standards
{from grey literature pass}

## Sources
```

### BIBLIOGRAPHY (annotated)

```markdown
# Bibliography: {topic}

## Access Summary
- FULLTEXT: N sources
- ABSTRACT_ONLY: N sources
- PAYWALLED: N sources

## Essential Reading
### {Citation}
- Access: FULLTEXT | ABSTRACT_ONLY
- Summary: {coverage}
- Key insight: {contribution}
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
| More metadata vs less | More complete | Less complete |

### Log Format

```json
{
  "timestamp": "2024-01-01T00:00:00Z",
  "total_before": 45,
  "total_after": 32,
  "merges": [
    {
      "canonical_key": "doi:10.1234/example",
      "kept": {
        "title": "Example Paper",
        "source_file": "academic.md",
        "access": "FULLTEXT",
        "reason": "peer-reviewed with FULLTEXT"
      },
      "dropped": [
        {
          "title": "Example Paper (preprint)",
          "source_file": "practitioner.md",
          "reason": "preprint duplicate"
        }
      ]
    }
  ]
}
```

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

### Access Depth Assignment

```javascript
function assignAccessDepth(source, unpaywallResponse) {
  if (unpaywallResponse?.is_oa && unpaywallResponse?.best_oa_location?.url) {
    // Attempt to access and extract
    const sections = extractSections(unpaywallResponse.best_oa_location.url)
    if (sections.length >= 3) {
      return 'FULLTEXT'
    }
  }

  if (source.abstract) {
    return 'ABSTRACT_ONLY'
  }

  return 'PAYWALLED'
}
```

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

## 14. Contradiction Resolution

**When to Apply:** Only for VERDICT/COMPARISON or when contested_flag=true.

**Protocol:**
1. Why do they disagree? (data, methodology, scope, recency)
2. Prefer: replicated > out-of-sample > single study
3. Prefer: recent > older (evolving topics)
4. Prefer: higher tier > lower tier
5. **v2.0**: Prefer FULLTEXT > ABSTRACT_ONLY (can verify claims)

**Categories:**
- **RESOLVED**: One position clearly stronger
- **CONTEXT-DEPENDENT**: Both valid in different contexts
- **UNRESOLVED**: Insufficient evidence to decide

---

## 15. Saturation Criteria

**Stop discovery when:**
- Min sources per unit met (per preset)
- Last 2 searches returned >50% duplicates
- Key terms searched across source types
- 12 candidates max per unit (before snowball)
- Snowball returns <2 new relevant sources

**Continue if:**
- Research unit below minimum
- Critical perspective missing
- Only old sources (violates recency policy)
- No FULLTEXT sources for key claims

---

## 16. Critique Checklist (v2.0)

Before finalizing, verify:

- [ ] All gates passed (or failures documented)
- [ ] Sources meet tier targets
- [ ] HIGH claims have >= 2 FULLTEXT T1/T2 sources
- [ ] All LOW claims flagged (with reason)
- [ ] CONTESTED claims present both sides
- [ ] Limitations documented (including access)
- [ ] Deliverable matches SPEC request
- [ ] All files written to research/{slug}/

**Max 1 page critique.**

---

## 17. Presets Reference (v2.0)

| Preset | Sources/Unit | Extraction | Passes | Snowball | Counterevidence |
|--------|--------------|------------|--------|----------|-----------------|
| `quick` | 2 | light | 2 | No | No |
| `standard` | 3 | medium | 3 | Yes | **Yes** (Gate B) |
| `thorough` | 5 | deep | 3 | Yes | **Yes** (Gate B) |
| `decision-support` | 4 | deep | 3 | Yes | **Yes** (Gate B) |

### Preset Feature Matrix

| Feature | quick | standard | thorough | decision-support |
|---------|-------|----------|----------|------------------|
| Min sources/unit | 2 | 3 | 5 | 4 |
| Extraction depth | light | medium | deep | deep |
| Snowball expansion | No | Yes | Yes | Yes |
| Counterevidence (Gate B) | No | **Required** | **Required** | **Required** |
| Grey literature | No | No | No | BLUEPRINT only |
| Structured extraction | No | No | No | **Required** |
| Depth Gate (A) | No | Yes | Yes | Yes |

---

## 18. File Structure Reference (v2.0)

```
research/{slug}/
├── SPEC.md                      # Input specification
├── STATE.json                   # v2.0 state with gates & config
├── SOURCES.md                   # Source list with access tags
├── claims.md                    # Evidence registry with gate checks
├── discovery/
│   ├── academic.md              # Academic pass
│   ├── practitioner.md          # Practitioner pass
│   ├── counterevidence.md       # Counterevidence (standard+)
│   ├── grey_literature.md       # BLUEPRINT only
│   └── snowball.md              # Citation expansion
├── topics/
│   └── {unit}/
│       ├── findings.md          # 11-field extraction
│       └── findings_structured.json  # VERDICT/COMPARISON
├── synthesis/
│   ├── final_deliverable.md     # PRIMARY OUTPUT
│   ├── critique.md              # With gate compliance
│   └── contradictions.md        # If contested
└── logs/
    ├── runlog.ndjson            # Execution log
    ├── checkpoint.md            # Resume point
    ├── dedup_log.json           # Merge decisions
    └── retraction_flags.json    # Retraction results
```

---

*Last Updated: 2026-02-03*
*Version: 4.0*
