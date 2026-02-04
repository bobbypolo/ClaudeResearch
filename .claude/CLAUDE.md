# Research ADE v2.0 - Project Constitution

## Overview

**Research ADE** is an autonomous research system that produces high-quality, evidence-based research outputs in a single session. The system uses MCP tools to search academic databases, preprint servers, and web resources.

**Version 2.0 Key Features:**
- 7-phase workflow with parallel execution
- Full-text access layer with Unpaywall integration
- Enforcement gates (Depth, Safety, Retraction)
- Citation snowballing (backward + forward)
- Intelligent deduplication pipeline
- Structured data extraction for comparisons
- Grey literature pass for BLUEPRINT deliverables
- Domain-aware recency policies
- Simplified confidence grading (HIGH/LOW/CONTESTED)

All outputs are persisted to `research/{slug}/` for reproducibility.

---

## The Seven Principles

### Principle 1: Write to Files, Not Context

**Rule**: All outputs MUST be written to `research/{slug}/` files. Return only summaries to orchestrator.

**v2.0 File Structure:**
```
research/{slug}/
├── SPEC.md                     # Input specification
├── STATE.json                  # Workflow state and config (v2.0 schema)
├── discovery/
│   ├── academic.md             # Academic pass results
│   ├── practitioner.md         # Practitioner pass (if run)
│   ├── counterevidence.md      # Counterevidence pass (always for standard+)
│   ├── grey_literature.md      # Grey literature pass (BLUEPRINT only)
│   └── snowball.md             # Citation snowball expansion
├── SOURCES.md                  # Curated source list
├── topics/
│   └── {unit}/
│       ├── findings.md         # Extracted evidence per unit
│       └── findings_structured.json  # Structured extraction (VERDICT/COMPARISON)
├── claims.md                   # Evidence registry
├── synthesis/
│   ├── final_deliverable.md    # PRIMARY OUTPUT
│   ├── critique.md             # Quality assessment
│   └── contradictions.md       # If contested
└── logs/
    ├── runlog.ndjson           # Tool execution log
    ├── checkpoint.md           # Resume checkpoint
    ├── dedup_log.json          # Deduplication decisions
    └── retraction_flags.json   # Retraction check results
```

---

### Principle 2: Quality Over Quantity

**Rule**: Find the RIGHT sources, not the MOST. Cap at 12 sources per research unit.

**Stop Conditions:**
- Min sources per unit met (quick=2, standard=3, thorough=5)
- Key claims have sufficient corroboration
- >50% duplicates in recent searches
- Snowball expansion adds diminishing returns

**Avoid:**
- Padding bibliographies
- Including low-quality sources for numbers
- Sources without full-text access when HIGH confidence needed

---

### Principle 3: Tier Sources with Access Verification

**Rule**: Maintain source quality mix AND verify access depth.

| Tier | Type | Default Target |
|------|------|----------------|
| **1** | Peer-reviewed, conferences, dissertations | 70% |
| **2** | Preprints, patents, tech reports | 25% |
| **3** | Industry, blogs, documentation | 5% |

**v2.0 Access Depth Tags:**
| Tag | Meaning |
|-----|---------|
| **FULLTEXT** | Complete document accessed and extracted |
| **ABSTRACT_ONLY** | Only abstract/metadata available |
| **PAYWALLED** | Behind paywall, no OA version found |

**Auto-Adjust:** If academic sources scarce, relax to 50/40/10.

**Never Cite:**
- No author/date
- News articles, forums
- SEO content, AI-generated
- Retracted papers (enforced by Retraction Gate)

---

### Principle 4: Gated Confidence

**Rule**: Three confidence levels with v2.0 enforcement gates.

| Level | Requirement |
|-------|-------------|
| **HIGH** | 3+ Tier-1/2 sources agree AND 2+ are FULLTEXT |
| **LOW** | 1-2 sources OR only ABSTRACT_ONLY/PAYWALLED |
| **CONTESTED** | Credible sources disagree |

**v2.0 Enforcement Gates:**

| Gate | Check | Failure Action |
|------|-------|----------------|
| **Gate A: Depth** | HIGH confidence requires >=2 FULLTEXT Tier-1/2 sources | Downgrade to LOW |
| **Gate B: Safety** | Counterevidence pass runs for standard+ presets | Block synthesis until complete |
| **Gate C: Retraction** | No retracted papers in HIGH claims | Remove source, recalculate confidence |

No MEDIUM. If it's not HIGH, it's LOW or CONTESTED.

---

### Principle 5: SPEC-Responsive Synthesis

**Rule**: Output format MUST match requested deliverable.

| Deliverable | When to Use | Special Handling |
|-------------|-------------|------------------|
| **VERDICT** | "Which should I use?" | Structured extraction required |
| **REPORT** | "What is X?" | Comprehensive findings |
| **COMPARISON** | "Compare A vs B" | Structured extraction required |
| **BLUEPRINT** | "How to design X?" | Grey literature pass |
| **BIBLIOGRAPHY** | "What sources exist?" | Annotated list |

---

### Principle 6: Explicit Limitations

**Rule**: Always document gaps in `synthesis/critique.md`.

Document:
- Inaccessible sources (impact level) with access tags
- Thin coverage areas
- LOW confidence claims (noting if due to access limitations)
- CONTESTED findings
- What could invalidate conclusions
- Gate failures and their impact

---

### Principle 7: One-Session Completion

**Rule**: Complete in 7 phases with parallel execution where possible.

```
Phase 1: PARSE        Parse SPEC, detect complexity, recency policy → STATE.json
Phase 2: DISCOVER     2-3 passes + snowball expansion + grey literature
Phase 3: CURATE       Deduplicate, retraction check, full-text resolution → SOURCES.md
Phase 4: EXTRACT      Extract with depth tagging, structured extraction → findings
Phase 5: COMPILE      Build claims registry, enforce gates → claims.md
Phase 6: SYNTHESIZE   Generate deliverable → synthesis/final_deliverable.md
Phase 7: CRITIQUE     Self-assess with gate compliance → synthesis/critique.md
```

---

## v2.0 Subsystems

### Full-Text Access Layer

**Unpaywall Integration:**
```
API: https://api.unpaywall.org/v2/{doi}?email=research@example.com
```

**Resolution Order:**
1. Check Unpaywall for OA version
2. Try arXiv if preprint available
3. Use Firecrawl on publisher page
4. Fall back to ABSTRACT_ONLY

**Tag Assignment:**
- FULLTEXT: PDF/HTML accessed, 3+ sections extracted
- ABSTRACT_ONLY: Only abstract available
- PAYWALLED: No accessible version found

---

### Citation Snowballing

**When**: After initial keyword discovery, before curation.

**Process:**
1. **Backward**: Get references of top-cited papers via OpenAlex `get_work_references`
2. **Forward**: Get citing papers via OpenAlex `get_work_citations`
3. **Filter**: Apply recency policy, deduplicate against existing

**Limits:**
- Max 5 seed papers per unit
- Max 10 snowball sources per unit
- Only pursue for >= standard preset

---

### Deduplication Pipeline

**Canonical Key Generation:**
```
Priority 1: DOI (normalized, lowercase)
Priority 2: title|first_author_last|year fingerprint
```

**Merge Rules:**
- Keep peer-reviewed over preprint over web
- Keep version with better access (FULLTEXT > ABSTRACT_ONLY)
- Preserve all unique metadata

**Output**: `logs/dedup_log.json` with merge decisions

---

### Structured Data Extraction

**Applies to**: VERDICT and COMPARISON deliverables only.

**Extract:**
```json
{
  "benchmark_results": [
    {"metric": "F1 score", "value": 0.87, "dataset": "SQuAD", "source": "S1"}
  ],
  "statistical_claims": [
    {"claim": "p < 0.01", "context": "performance comparison", "source": "S2"}
  ],
  "comparisons": [
    {"item_a": "Method X", "item_b": "Method Y", "dimension": "speed", "winner": "X", "margin": "2.3x", "source": "S3"}
  ]
}
```

**Output**: `topics/{unit}/findings_structured.json`

---

### Grey Literature Pass

**When**: BLUEPRINT deliverable only.

**Sources:**
- NIST publications
- RAND Corporation
- Standards bodies (IEEE, ISO, W3C)
- Government technical reports (.gov domains)
- Major vendor architecture guides

**Output**: `discovery/grey_literature.md`

---

### Recency Policy

**Auto-detect from topic:**

| Domain | Policy | Max Age | Example Topics |
|--------|--------|---------|----------------|
| **fast_moving** | 18 months | LLMs, crypto, emerging tech |
| **scientific** | 5 years | Established CS, biology |
| **historical** | No limit | Philosophy, history |

**Foundational Exception:** Seminal papers always included regardless of age.

---

## Auto-Complexity Detection

The system auto-detects complexity from SPEC and applies presets:

| Preset | Sources/Unit | Extraction | Passes | Auto-Trigger |
|--------|--------------|------------|--------|--------------|
| `quick` | 2 | light | 2 | Simple questions |
| `standard` | 3 | medium | 3 | Default (counterevidence now required) |
| `thorough` | 5 | deep | 3 | Complex/critical |
| `decision-support` | 4 | deep | 3 | VERDICT/COMPARISON |

**Contested Flag:** Set true if VERDICT/COMPARISON or "vs/compare/which/should" in SPEC.

---

## Discovery Strategy

| Pass | When | Purpose |
|------|------|---------|
| **Academic** | Always | Peer-reviewed + arXiv |
| **Practitioner** | BLUEPRINT/VERDICT or >=standard | Case studies, docs |
| **Counterevidence** | Always for >=standard (Safety Gate) | Critiques, failures |
| **Grey Literature** | BLUEPRINT only | Standards, gov reports |
| **Snowball** | >=standard preset | Citation expansion |

---

## Extraction Template

**v2.0: 11 Essential Fields:**
```markdown
- Citation: {full}
- Type: ACADEMIC | PRACTITIONER | OTHER
- Tier: 1 | 2 | 3
- Extraction depth: FULLTEXT | ABSTRACT_ONLY | PAYWALLED
- Source URL: {accessible URL}
- Sections extracted: {e.g., "Abstract, Methods, Results"}
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
2. Prefer: replicated > recent > higher tier > FULLTEXT
3. Categorize: RESOLVED | CONTEXT-DEPENDENT | UNRESOLVED

**Otherwise:** Just note disagreements, don't run heavy protocol.

---

## MCP Tools

| Tool | Purpose |
|------|---------|
| `mcp__openalex__search_works` | Academic papers |
| `mcp__openalex__get_work_references` | Backward snowball |
| `mcp__openalex__get_work_citations` | Forward snowball |
| `mcp__arxiv__search_papers` | Preprints |
| `mcp__arxiv__read_paper` | arXiv full text |
| `mcp__exa__web_search_exa` | Web sources |
| `mcp__firecrawl__firecrawl_scrape` | Content extraction |
| `mcp__crossref__getWorkByDOI` | DOI validation, retraction check |
| WebFetch (Unpaywall API) | Full-text resolution |

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

**Confidence:** HIGH (3+ T1/2 + 2 FULLTEXT) | LOW (1-2 or access-limited) | CONTESTED (disagree)

**Access Depth:** FULLTEXT | ABSTRACT_ONLY | PAYWALLED

**Evidence Types:** ACADEMIC | PRACTITIONER | OTHER

**Tiers:** T1 (peer-reviewed) | T2 (preprints) | T3 (industry)

**Gates:** Depth (HIGH needs FULLTEXT) | Safety (counterevidence required) | Retraction (no retracted)

**Recency:** fast_moving (18mo) | scientific (5yr) | historical (unlimited)

**Phases:** Parse → Discover → Curate → Extract → Compile → Synthesize → Critique

---

*For detailed schemas, see `.claude/rules/research.md`*
*Version: 2.0*
