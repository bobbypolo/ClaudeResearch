# Research ADE v5.0 - Project Constitution

## Overview

**Research ADE** is an autonomous research system that produces **implementation-ready specifications** through systematic evidence gathering. The system uses MCP tools to search academic databases, preprint servers, and web resources.

**Core Philosophy:**
- **Optimistic-Empirical**: Solutions exist until proven otherwise
- **Implementation-Focused**: "How to build" not "is it possible"
- **HIGH Confidence Required**: Definitive answers or explicit gaps
- **Evidence-Based Recommendations**: Every method selection backed by sources

**Key Features:**
- 8-phase workflow with mandatory planning
- Implementation-oriented discovery
- Failure studies with risk-mitigation pairs
- Completion gate ensuring actionable output
- New SPECIFICATION deliverable type
- Full-text access layer with Unpaywall integration
- Citation snowballing (backward + forward)
- Intelligent deduplication pipeline

All outputs are persisted to `research/{slug}/` for reproducibility.

---

## The Eight Principles

### Principle 1: Plan Before Research

**Rule**: Every research project begins with a comprehensive plan that the user approves.

**PLAN Phase Requirements:**
1. Analyze user's goal statement
2. Decompose into research questions
3. Identify prior art search strategies
4. Define success criteria (what HIGH confidence looks like)
5. Anticipate potential sub-domains
6. Create research unit structure

**Outputs:**
- `research/{slug}/PLAN.md` - Research plan for user review
- Initial SPEC.md validation

**Critical**: Research does NOT proceed until user approves the plan.

---

### Principle 2: Implementation Over Assessment

**Rule**: Default posture is "How do we build this?" not "Is this feasible?"

**Discovery Focus:**
- Prioritize implementation papers
- Extract specific methods and parameters
- Find validation metrics and baselines
- Gather architectural patterns

**Search Strategy:**
```
Primary: "{goal} implementation" "{goal} system design" "{goal} method"
Secondary: "{goal} architecture" "{goal} pipeline" "{goal} best practices"
```

**Avoid:**
- Feasibility hedging ("it depends", "under certain conditions")
- Listing possibilities without selection
- Concluding with "more research needed" without specifics

---

### Principle 3: Write to Files, Not Context

**Rule**: All outputs MUST be written to `research/{slug}/` files. Return only summaries to orchestrator.

**File Structure:**
```
research/{slug}/
├── PLAN.md                      # Research plan (NEW)
├── SPEC.md                      # Input specification
├── STATE.json                   # Workflow state and config
├── discovery/
│   ├── academic.md              # Academic pass results
│   ├── practitioner.md          # Practitioner pass (if run)
│   ├── failure_analysis.md      # Failure studies (RENAMED)
│   ├── grey_literature.md       # Grey literature (BLUEPRINT only)
│   └── snowball.md              # Citation snowball expansion
├── SOURCES.md                   # Curated source list
├── topics/
│   └── {unit}/
│       ├── findings.md          # Extracted evidence per unit
│       └── findings_structured.json  # Structured extraction
├── claims.md                    # Evidence registry
├── synthesis/
│   ├── final_deliverable.md     # PRIMARY OUTPUT
│   ├── critique.md              # Quality assessment
│   ├── risk_mitigations.md      # Risk-mitigation pairs (NEW)
│   └── gaps.md                  # Gap declarations if any (NEW)
└── logs/
    ├── runlog.ndjson            # Tool execution log
    ├── checkpoint.md            # Resume checkpoint
    ├── dedup_log.json           # Deduplication decisions
    └── retraction_flags.json    # Retraction check results
```

---

### Principle 4: Quality Over Quantity

**Rule**: Find the RIGHT sources, not the MOST. Cap at 12 sources per research unit.

**Stop Conditions:**
- Min sources per unit met (quick=2, standard=3, thorough=5)
- Key claims have sufficient corroboration
- >50% duplicates in recent searches
- Snowball expansion adds diminishing returns

**Prioritize:**
- Sources with implementation detail (code, parameters, architecture)
- Validation studies with reproducible metrics
- Failure studies with lessons learned

---

### Principle 5: Tier Sources with Access Verification

**Rule**: Maintain source quality mix AND verify access depth.

| Tier | Type | Default Target |
|------|------|----------------|
| **1** | Peer-reviewed, conferences, dissertations | 70% |
| **2** | Preprints, patents, tech reports | 25% |
| **3** | Industry, blogs, documentation | 5% |

**Access Depth Tags:**
| Tag | Meaning |
|-----|---------|
| **FULLTEXT** | Complete document accessed and extracted |
| **ABSTRACT_ONLY** | Only abstract/metadata available |
| **PAYWALLED** | Behind paywall, no OA version found |

**Implementation Detail Flag:**
Sources are additionally flagged if they contain implementation specifics (code, parameters, architecture diagrams).

---

### Principle 6: Failure Studies as Learning

**Rule**: Counterevidence is reframed as failure analysis with risk-mitigation pairs.

**Old Approach (v4.0):**
- "Find reasons this might not work"
- Creates defensive, hedging output

**New Approach (v5.0):**
- "Find implementations that failed"
- "Extract lessons learned"
- "Pair each risk with a mitigation"

**Search Strategy:**
```
Primary: "{method} failed" "{method} failure" "{method} pitfalls"
Secondary: "{method} lessons learned" "{method} postmortem"
Tertiary: "{domain} what went wrong" "{domain} debugging"
```

**Output Format (per failure study):**
```markdown
## Failure Study: {source}

### What They Tried
- Method: {specific approach}
- Context: {conditions}

### What Failed
- Failure Mode: {observable failure}
- Root Cause: {why it failed}

### Lessons Learned
- {insight 1}
- {insight 2}

### Risk-Mitigation Pair
| Risk | Mitigation | Evidence |
|------|------------|----------|
| {risk from this failure} | {how to avoid} | {source} |
```

---

### Principle 7: HIGH Confidence or Explicit Gaps

**Rule**: Research ONLY ends when:
1. All recommendations have HIGH confidence, OR
2. Gaps are explicitly declared with clear documentation

**Confidence Levels:**
| Level | Requirement |
|-------|-------------|
| **HIGH** | 3+ Tier-1/2 sources agree AND 2+ are FULLTEXT AND implementation detail present |
| **LOW** | 1-2 sources OR only ABSTRACT_ONLY/PAYWALLED |
| **CONTESTED** | Credible sources disagree |

**Gap Declaration Format:**
```markdown
## Gap: {what is unknown}
- **Impact**: {why this matters for implementation}
- **Blocking**: {what can't be determined without this}
- **Resolution Path**: {what research would fill this gap}
```

**Completion Gate** enforces this before synthesis.

---

### Principle 8: One-Session Completion

**Rule**: Complete in 8 phases with parallel execution where possible.

```
Phase 0: PLAN         Comprehensive research plan → PLAN.md (user approval required)
Phase 1: PARSE        Parse SPEC, detect complexity, recency policy → STATE.json
Phase 2: SURVEY       Broad discovery pass (implementation-focused)
Phase 3: DEEP DIVE    Evidence-driven depth allocation
Phase 4: FAILURE      Failure studies + risk-mitigation extraction
Phase 5: COMPILE      Build claims registry, enforce gates → claims.md
Phase 6: SPECIFY      Generate deliverable → synthesis/final_deliverable.md
Phase 7: VALIDATE     Self-assess, ensure HIGH confidence → synthesis/critique.md
```

---

## Subsystems

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
1. **Backward**: Get references of top-cited papers via OpenAlex
2. **Forward**: Get citing papers via OpenAlex
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

---

### Implementation Detail Detection

**Sources flagged as having implementation detail if they contain:**
- Code snippets or pseudocode
- Architecture diagrams
- Parameter tables or configuration
- Reproducibility sections
- Benchmark comparisons with specific metrics

---

## Auto-Complexity Detection

The system auto-detects complexity from SPEC and applies presets:

| Preset | Sources/Unit | Extraction | Passes | Auto-Trigger |
|--------|--------------|------------|--------|--------------|
| `quick` | 2 | light | 2 | Simple questions |
| `standard` | 3 | medium | 3 | Default |
| `thorough` | 5 | deep | 3 | Complex/critical |
| `decision-support` | 4 | deep | 3 | VERDICT/COMPARISON |

---

## Discovery Strategy

| Pass | When | Purpose |
|------|------|---------|
| **Academic** | Always | Peer-reviewed + arXiv |
| **Practitioner** | BLUEPRINT/SPECIFICATION or >=standard | Case studies, docs |
| **Failure Analysis** | Always for >=standard | Failure studies, lessons learned |
| **Grey Literature** | BLUEPRINT only | Standards, gov reports |
| **Snowball** | >=standard preset | Citation expansion |

---

## Deliverable Types

| Deliverable | When to Use | Special Handling |
|-------------|-------------|------------------|
| **SPECIFICATION** | "How to build X?" (DEFAULT) | Implementation blueprint with method selections |
| **VERDICT** | "Which should I use?" | Structured extraction required |
| **COMPARISON** | "Compare A vs B" | Structured extraction required |
| **REPORT** | "What is X?" | Comprehensive findings |
| **BLUEPRINT** | "How to design X?" | Grey literature pass |
| **BIBLIOGRAPHY** | "What sources exist?" | Annotated list |

---

## Extraction Template

**12 Essential Fields:**
```markdown
- Citation: {full}
- Type: ACADEMIC | PRACTITIONER | OTHER
- Tier: 1 | 2 | 3
- Extraction depth: FULLTEXT | ABSTRACT_ONLY | PAYWALLED
- Has implementation detail: YES | NO
- Source URL: {accessible URL}
- Sections extracted: {e.g., "Abstract, Methods, Results"}
- Main claim: {one sentence}
- Key evidence: "{quote}" (location)
- Implementation specifics: {methods, parameters, if present}
- Limitations: {caveats}
- Relevance: {unit}
```

---

## Gates

| Gate | Check | Failure Action |
|------|-------|----------------|
| **Depth Gate (A)** | HIGH confidence requires >=2 FULLTEXT Tier-1/2 sources | Downgrade to LOW |
| **Completion Gate (B)** | All recommendations HIGH confidence OR gaps declared | Block synthesis until resolved |
| **Retraction Gate (C)** | No retracted papers in HIGH claims | Remove source, recalculate confidence |

---

## Recency Policy

**Auto-detect from topic:**

| Domain | Policy | Max Age | Example Topics |
|--------|--------|---------|----------------|
| **fast_moving** | 18 months | LLMs, crypto, emerging tech |
| **scientific** | 5 years | Established CS, biology |
| **historical** | No limit | Philosophy, history |

**Foundational Exception:** Seminal papers always included regardless of age.

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
| `/research {slug} [--preset]` | Execute 8-phase workflow |
| `/research-status {slug}` | Check progress |
| `/research-resume {slug}` | Resume from checkpoint |

**Presets:** `--quick`, `--standard`, `--thorough`, `--decision-support`

---

## Quick Reference

**Confidence:** HIGH (3+ T1/2 + 2 FULLTEXT + implementation detail) | LOW (1-2 or access-limited) | CONTESTED (disagree)

**Access Depth:** FULLTEXT | ABSTRACT_ONLY | PAYWALLED

**Evidence Types:** ACADEMIC | PRACTITIONER | OTHER

**Tiers:** T1 (peer-reviewed) | T2 (preprints) | T3 (industry)

**Gates:** Depth (HIGH needs FULLTEXT) | Completion (HIGH or gaps) | Retraction (no retracted)

**Recency:** fast_moving (18mo) | scientific (5yr) | historical (unlimited)

**Phases:** Plan → Parse → Survey → Deep Dive → Failure → Compile → Specify → Validate

**Default Posture:** "Solutions exist until proven otherwise"

---

*For detailed schemas, see `.claude/rules/research.md`*
*Version: 5.0*
