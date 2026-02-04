# Research ADE - Schemas and Rubrics

Simplified reference for the Research ADE system.

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
  time_period: string            # Default: "last 5 years + foundational"
  excluded: [string]             # Sources/perspectives to exclude
key_search_terms: [string]       # Auto-generate if missing
preset: enum                     # quick | standard | thorough | decision-support
```

---

## 2. STATE.json Schema

Written by Phase 1 (Parse), read by all subsequent phases.

```json
{
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
  "completed_at": null
}
```

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

### Never Cite

- No author attribution
- No date
- News articles (secondary)
- Forums (Reddit, StackOverflow)
- SEO/content farms
- Wikipedia (use only to find primaries)
- AI-generated (unverified)
- Retracted papers

---

## 4. Confidence Levels

| Level | Requirement | Action |
|-------|-------------|--------|
| **HIGH** | 3+ Tier-1 academic sources agree | State with confidence |
| **LOW** | 1-2 sources OR only Tier-2/3 | Flag as tentative |
| **CONTESTED** | Credible sources disagree | Present both sides |

**Decision Tree:**
```
Do sources agree?
├── No → CONTESTED
└── Yes → Are there 3+ Tier-1 sources?
    ├── Yes → HIGH
    └── No → LOW
```

---

## 5. Extraction Template

**Essential 8 fields only:**

```markdown
## Source: {title}

- **Citation**: {Full formatted citation}
- **Type**: ACADEMIC | PRACTITIONER | OTHER
- **Tier**: 1 | 2 | 3
- **Main claim**: {One sentence summary}
- **Key evidence**: "{Quote or data point}" (p. X / Section Y)
- **Limitations**: {What this source doesn't cover}
- **Relevance**: {Which research unit}
- **Notes**: {Optional additional context}
```

---

## 6. Deliverable Formats

### VERDICT (recommendation)

```markdown
# Verdict: {question}

## Recommendation
**{OPTION}** - Confidence: HIGH | LOW

## Comparison Matrix
| Factor | Option A | Option B |

## Key Evidence
- {claim} [HIGH] - S1, S4, S7
- {claim} [LOW] - S2

## Caveats
- {limitation}

## Sources
[Numbered list]
```

### REPORT (comprehensive)

```markdown
# Report: {topic}

## Summary
{2-3 paragraphs}

## Findings

### {Research Unit 1}
{Narrative with inline citations}
- {claim} [HIGH confidence]

## Limitations
- {gaps}

## Sources
```

### COMPARISON (neutral)

```markdown
# Comparison: {options}

## Matrix
| Criterion | Option A | Option B |

## Option A
### Strengths / Weaknesses / Best for

## Selection Guidance
- Choose A when: ...
- Choose B when: ...
```

### BLUEPRINT (implementation)

```markdown
# Blueprint: {topic}

## Architecture
{High-level design}

## Steps
### Step 1: {action}
- Evidence: {citation}
- Pitfalls: {warning}

## Best Practices
```

### BIBLIOGRAPHY (annotated)

```markdown
# Bibliography: {topic}

## Essential Reading
### {Citation}
- Summary: {coverage}
- Key insight: {contribution}
```

---

## 7. Contradiction Resolution

**When to Apply:** Only for VERDICT/COMPARISON or when contested_flag=true.

**Protocol:**
1. Why do they disagree? (data, methodology, scope, recency)
2. Prefer: replicated > out-of-sample > single study
3. Prefer: recent > older (evolving topics)
4. Prefer: higher tier > lower tier

**Categories:**
- **RESOLVED**: One position clearly stronger
- **CONTEXT-DEPENDENT**: Both valid in different contexts
- **UNRESOLVED**: Insufficient evidence to decide

---

## 8. Saturation Criteria

**Stop discovery when:**
- Min sources per unit met (per preset)
- Last 2 searches returned >50% duplicates
- Key terms searched across source types
- 12 candidates max per unit

**Continue if:**
- Research unit below minimum
- Critical perspective missing
- Only old sources (>5 years for tech)

---

## 9. Critique Checklist

Before finalizing, verify:

- [ ] Sources meet tier targets
- [ ] All LOW claims flagged
- [ ] CONTESTED claims present both sides
- [ ] Limitations documented
- [ ] Deliverable matches SPEC request
- [ ] All files written to research/{slug}/

**Max 1 page critique.**

---

## 10. Presets Reference

| Preset | Sources/Unit | Extraction | Passes |
|--------|--------------|------------|--------|
| `quick` | 2 | light (abstract OK) | 2 (academic + practitioner) |
| `standard` | 3 | medium | 2-3 |
| `thorough` | 5 | deep | 3 (+ counterevidence) |
| `decision-support` | 4 | deep | 3 |

---

*Last Updated: 2026-02-03*
*Version: 3.0 - Simplified*
