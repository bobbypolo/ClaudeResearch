# Research ADE - Project Constitution

## Overview

**Research ADE** is an autonomous research system that produces high-quality, evidence-based research outputs in a single session. The system uses MCP tools to search academic databases, preprint servers, and web resources.

**Key Features:**
- 7-phase workflow with parallel execution
- Auto-complexity detection with presets
- File-based state for resumability
- Simplified confidence grading (HIGH/LOW/CONTESTED)
- Minimal extraction templates

All outputs are persisted to `research/{slug}/` for reproducibility.

---

## The Seven Principles

### Principle 1: Write to Files, Not Context

**Rule**: All outputs MUST be written to `research/{slug}/` files. Return only summaries to orchestrator.

**File Structure:**
```
research/{slug}/
├── SPEC.md                     # Input specification
├── STATE.json                  # Workflow state and config
├── discovery/
│   ├── academic.md             # Academic pass results
│   ├── practitioner.md         # Practitioner pass (if run)
│   └── counterevidence.md      # Counterevidence pass (if run)
├── SOURCES.md                  # Curated source list
├── topics/
│   └── {unit}/findings.md      # Extracted evidence per unit
├── claims.md                   # Evidence registry
├── synthesis/
│   ├── final_deliverable.md    # PRIMARY OUTPUT
│   ├── critique.md             # Quality assessment
│   └── contradictions.md       # If contested
└── logs/
    ├── runlog.ndjson           # Tool execution log
    └── checkpoint.md           # Resume checkpoint
```

---

### Principle 2: Quality Over Quantity

**Rule**: Find the RIGHT sources, not the MOST. Cap at 12 sources per research unit.

**Stop Conditions:**
- Min sources per unit met (quick=2, standard=3, thorough=5)
- Key claims have sufficient corroboration
- >50% duplicates in recent searches

**Avoid:**
- Padding bibliographies
- Including low-quality sources for numbers

---

### Principle 3: Tier Sources

**Rule**: Maintain source quality mix with flexible targets.

| Tier | Type | Default Target |
|------|------|----------------|
| **1** | Peer-reviewed, conferences, dissertations | 70% |
| **2** | Preprints, patents, tech reports | 25% |
| **3** | Industry, blogs, documentation | 5% |

**Auto-Adjust:** If academic sources scarce, relax to 50/40/10.

**Never Cite:**
- No author/date
- News articles, forums
- SEO content, AI-generated
- Retracted papers

---

### Principle 4: Simple Confidence

**Rule**: Three confidence levels only.

| Level | Requirement |
|-------|-------------|
| **HIGH** | 3+ Tier-1 academic sources agree |
| **LOW** | 1-2 sources OR only Tier-2/3 |
| **CONTESTED** | Credible sources disagree |

No MEDIUM. If it's not HIGH, it's LOW or CONTESTED.

---

### Principle 5: SPEC-Responsive Synthesis

**Rule**: Output format MUST match requested deliverable.

| Deliverable | When to Use |
|-------------|-------------|
| **VERDICT** | "Which should I use?" → Recommendation |
| **REPORT** | "What is X?" → Comprehensive findings |
| **COMPARISON** | "Compare A vs B" → Neutral analysis |
| **BLUEPRINT** | "How to design X?" → Architecture |
| **BIBLIOGRAPHY** | "What sources exist?" → Annotated list |

---

### Principle 6: Explicit Limitations

**Rule**: Always document gaps in `synthesis/critique.md`.

Document:
- Inaccessible sources (impact level)
- Thin coverage areas
- LOW confidence claims
- CONTESTED findings
- What could invalidate conclusions

---

### Principle 7: One-Session Completion

**Rule**: Complete in 7 phases with parallel execution where possible.

```
Phase 1: PARSE        Parse SPEC, detect complexity → STATE.json
Phase 2: DISCOVER     2-3 passes (academic, practitioner, counterevidence)
Phase 3: CURATE       Deduplicate, filter → SOURCES.md
Phase 4: EXTRACT      Extract evidence → topics/*/findings.md
Phase 5: COMPILE      Build claims registry → claims.md
Phase 6: SYNTHESIZE   Generate deliverable → synthesis/final_deliverable.md
Phase 7: CRITIQUE     Self-assess → synthesis/critique.md
```

---

## Auto-Complexity Detection

The system auto-detects complexity from SPEC and applies presets:

| Preset | Sources/Unit | Extraction | Passes | Auto-Trigger |
|--------|--------------|------------|--------|--------------|
| `quick` | 2 | light | 2 | Simple questions |
| `standard` | 3 | medium | 2 | Default |
| `thorough` | 5 | deep | 3 | Complex/critical |
| `decision-support` | 4 | deep | 3 | VERDICT/COMPARISON |

**Contested Flag:** Set true if VERDICT/COMPARISON or "vs/compare/which/should" in SPEC.

---

## Discovery Strategy

| Pass | When | Purpose |
|------|------|---------|
| **Academic** | Always | Peer-reviewed + arXiv |
| **Practitioner** | BLUEPRINT/VERDICT or >=standard | Case studies, docs |
| **Counterevidence** | contested_flag or >=thorough | Critiques, failures |

---

## Simplified Extraction

**8 Essential Fields Only:**
```markdown
- Citation: {full}
- Type: ACADEMIC | PRACTITIONER | OTHER
- Tier: 1 | 2 | 3
- Main claim: {one sentence}
- Key evidence: "{quote}" (location)
- Limitations: {caveats}
- Relevance: {unit}
- Notes: {optional}
```

---

## Contradiction Handling

**Only for VERDICT/COMPARISON or contested_flag:**
1. Analyze why they disagree
2. Prefer: replicated > recent > higher tier
3. Categorize: RESOLVED | CONTEXT-DEPENDENT | UNRESOLVED

**Otherwise:** Just note disagreements, don't run heavy protocol.

---

## MCP Tools

| Tool | Purpose |
|------|---------|
| `mcp__openalex__search_works` | Academic papers |
| `mcp__arxiv__search_papers` | Preprints |
| `mcp__exa__web_search_exa` | Web sources |
| `mcp__firecrawl__firecrawl_scrape` | Content extraction |
| `mcp__crossref__getWorkByDOI` | DOI validation (use sparingly) |

---

## Skills

| Skill | Purpose |
|-------|---------|
| `/research {slug} [--preset]` | Execute 7-phase workflow |
| `/research-status {slug}` | Check progress |
| `/research-resume {slug}` | Resume from checkpoint |

**Presets:** `--quick`, `--standard`, `--thorough`, `--decision-support`

---

## Quick Reference

**Confidence:** HIGH (3+ T1) | LOW (1-2 or T2/T3 only) | CONTESTED (disagree)

**Evidence Types:** ACADEMIC | PRACTITIONER | OTHER

**Tiers:** T1 (peer-reviewed) | T2 (preprints) | T3 (industry)

**Phases:** Parse → Discover → Curate → Extract → Compile → Synthesize → Critique

---

*For detailed schemas, see `.claude/rules/research.md`*
