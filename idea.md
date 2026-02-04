# Research ADE v2.0 - Complete Implementation Plan

## Executive Summary

This document defines the complete upgrade path for Research ADE, transforming it from a "good foundation" to a PhD-grade autonomous research system. The core philosophy: **add enforcement gates and access capabilities, not phases**.

**Key Upgrades:**
1. Full-Text Access Layer (unblocks depth)
2. Two Enforcement Gates (ensures quality)
3. Citation Snowballing (finds hidden sources)
4. Deduplication Pipeline (prevents double-counting)
5. Retraction/Trust Verification (prevents citing bad science)
6. Structured Extraction (captures numbers, not just narratives)

---

## Part 1: Current State (Preserved)

These components are working and remain unchanged:

| Component | Status | Notes |
|-----------|--------|-------|
| File-based state | ✅ Keep | `research/{slug}/` structure |
| 7-phase workflow | ✅ Keep | Parse → Discover → Curate → Extract → Compile → Synthesize → Critique |
| Source tiering | ✅ Keep | Tier 1/2/3 classification |
| Confidence labels | ✅ Keep | HIGH/LOW/CONTESTED |
| Parallel discovery | ✅ Keep | Academic + Practitioner + Counter passes |
| Preset system | ✅ Keep | quick/standard/thorough/decision-support |
| MCP tool integration | ✅ Keep | OpenAlex, arXiv, Exa, Firecrawl, Crossref |

---

## Part 2: Full-Text Access Layer

### Problem
The FULLTEXT gate is meaningless if 60-70% of academic papers are paywalled. Without full-text access, "depth" becomes "only cite open access."

### Solution: Legal Full-Text Resolver Pipeline

```
resolve_fulltext(doi, metadata) → {status, content, source_url}

Step 1: Unpaywall Lookup
    ├── Query: GET https://api.unpaywall.org/v2/{doi}?email={email}
    ├── If oa_status != null → get best_oa_location.url_for_pdf or url_for_landing_page
    └── Prefer: publishedVersion > acceptedVersion > submittedVersion

Step 2: Preprint Fallback (if Unpaywall fails)
    ├── Check OpenAlex work object for open_access.oa_url
    ├── Check for has_repository_copy = true
    ├── Query arXiv by title + first author if no DOI match
    └── Check bioRxiv/medRxiv for life sciences

Step 3: Content Extraction
    ├── If PDF URL → Firecrawl with PDF mode
    ├── If HTML URL → Firecrawl standard scrape
    └── Extract: abstract, introduction, methods, results, discussion, conclusion

Step 4: Status Assignment
    ├── FULLTEXT: Successfully extracted body content
    ├── ABSTRACT_ONLY: Only metadata/abstract available
    └── PAYWALLED: No legal access found
```

### Unpaywall Integration

**API Details:**
- Endpoint: `https://api.unpaywall.org/v2/{doi}?email={your_email}`
- Rate limit: 100,000 requests/day
- No API key required, just email for identification
- Returns: OA status, PDF URLs, version info, host type

**Response Fields to Use:**
```json
{
  "is_oa": true,
  "best_oa_location": {
    "url_for_pdf": "https://...",
    "url_for_landing_page": "https://...",
    "version": "publishedVersion",
    "host_type": "publisher"
  },
  "oa_status": "gold|green|hybrid|bronze"
}
```

### MCP Tool Addition

Create or integrate an Unpaywall MCP tool:

```yaml
Tool: mcp__unpaywall__resolve_oa
Input: doi (string), email (string)
Output: {is_oa, pdf_url, landing_url, version, host_type}
```

If no MCP server available, implement via WebFetch to the Unpaywall API.

### Extraction Depth Tagging

Every source in `findings.md` gets an extraction depth tag:

```markdown
- **Extraction**: FULLTEXT | ABSTRACT_ONLY | PAYWALLED
- **Source URL**: {url used for extraction}
- **Sections Extracted**: [abstract, methods, results, discussion]
```

---

## Part 3: Enforcement Gates

### Gate A: Depth Gate (FULLTEXT Requirement)

**Rule:** A claim CANNOT be labeled HIGH confidence unless it has ≥2 supporting sources that are:
- Tier 1 or Tier 2
- Extraction depth = FULLTEXT

**Implementation:**

```python
def can_be_high_confidence(claim, supporting_sources):
    fulltext_tier1_2 = [s for s in supporting_sources
                        if s.extraction == "FULLTEXT"
                        and s.tier in [1, 2]]
    return len(fulltext_tier1_2) >= 2
```

**Consequences:**
- ABSTRACT_ONLY sources can inform background, context, and LOW claims
- PAYWALLED sources are logged but don't count toward confidence
- Forces the system to actually read papers, not just cite them

### Gate B: Safety Gate (Counterevidence Requirement)

**Rule:** For `standard` and `thorough` presets, ALWAYS run a bounded counterevidence pass.

**Implementation:**

```yaml
Counterevidence Pass:
  trigger: preset in [standard, thorough, decision-support] OR contested_flag = true
  queries_per_unit:
    - "{topic} limitations"
    - "{topic} failure modes"
    - "{topic} negative results"
    - "{topic} criticism"
  max_sources_per_unit: 2
  extraction: FULLTEXT only if materially conflicts with key claim
```

**Consequences:**
- Ensures "when it fails" perspective is always represented
- Bounded scope prevents open-ended investigation
- Light extraction unless conflict detected

### Gate C: Retraction Gate (Trust Verification)

**Rule:** No source can support a HIGH claim if it has been retracted or has major corrections.

**Implementation:**

```
retraction_check(dois[]) → {doi: {retracted, corrected, correction_doi}}

Step 1: Batch query Crossref for each DOI
Step 2: Check for:
    - update-to relationship (corrections)
    - retracted status
    - expression-of-concern
Step 3: If flagged:
    - Mark source as RETRACTED or CORRECTED in STATE.json
    - Block from HIGH confidence
    - Require explicit mention in synthesis
```

**Crossref Retraction Data:**
- Field: `relation.is-retracted-by` or `update-policy`
- Crossref has integrated Retraction Watch data since 2020

---

## Part 4: Citation Snowballing (OpenAlex)

### Purpose
Keyword search misses foundational papers and important follow-on work. Citation traversal finds what keywords can't.

### Snowball Algorithm

```
SNOWBALL(seed_papers, max_rounds=2, max_new_per_round=5):

    candidates = set(seed_papers)
    seen_ids = set()

    for round in range(max_rounds):
        new_this_round = []

        for seed in seed_papers:
            # Backward: papers this seed cites
            refs = openalex.get_work(seed.id).referenced_works
            refs = filter_by_tier_and_recency(refs)
            refs = refs[:3]  # top 3 most relevant

            # Forward: papers citing this seed
            citers = openalex.search(filter=f"cites:{seed.id}")
            citers = filter_by_tier_and_recency(citers)
            citers = citers[:3]  # top 3 most cited

            new_this_round.extend(refs + citers)

        # Deduplicate and filter already seen
        new_this_round = [p for p in new_this_round if p.id not in seen_ids]
        new_this_round = new_this_round[:max_new_per_round]

        if len(new_this_round) == 0:
            break  # Saturation reached

        candidates.update(new_this_round)
        seen_ids.update(p.id for p in new_this_round)
        seed_papers = new_this_round  # Next round seeds

    return candidates
```

### OpenAlex API Usage

**Get references (backward):**
```
GET https://api.openalex.org/works/{id}
→ response.referenced_works = [list of work IDs]
```

**Get citations (forward):**
```
GET https://api.openalex.org/works?filter=cites:{id}&sort=cited_by_count:desc
```

**Filter by quality:**
```
filter=type:journal-article,cited_by_count:>10,publication_year:>2019
```

### Integration Point

Snowballing runs inside DISCOVER phase, after initial keyword search:

```
DISCOVER:
    1. Keyword search (OpenAlex + arXiv) → seed papers
    2. Snowball expansion (backward + forward) → expanded candidates
    3. Practitioner pass (Exa) → practitioner sources
    4. Counterevidence pass → counter sources
    5. Merge all → raw candidate pool
```

---

## Part 5: Deduplication Pipeline

### Problem
Same paper appears in OpenAlex, arXiv, and Crossref with different IDs. Without dedup, you count it multiple times.

### Canonical Key Logic

```python
def canonical_key(source):
    # Prefer DOI as canonical identifier
    if source.doi:
        return normalize_doi(source.doi)

    # Fallback: fingerprint from metadata
    title_normalized = normalize_title(source.title)  # lowercase, remove punctuation
    first_author = source.authors[0].family_name.lower() if source.authors else "unknown"
    year = source.publication_year or "0000"

    return f"{title_normalized}|{first_author}|{year}"

def normalize_doi(doi):
    # Remove URL prefix, lowercase
    doi = doi.lower()
    doi = doi.replace("https://doi.org/", "")
    doi = doi.replace("http://dx.doi.org/", "")
    return doi
```

### Version Preference

When duplicates found, prefer:
1. Published version (has DOI from publisher)
2. Accepted manuscript (post-peer-review preprint)
3. Submitted version (pre-peer-review preprint)

OpenAlex helps here: `primary_location.version` indicates version type.

### Integration Point

Deduplication runs at the start of CURATE phase:

```
CURATE:
    1. Load all candidates from discovery passes
    2. Compute canonical key for each
    3. Group by canonical key
    4. For each group, select best version
    5. Output deduplicated SOURCES.md
```

---

## Part 6: Structured Data Extraction

### Problem
Research quality often depends on numbers: benchmarks, effect sizes, performance metrics. Prose extraction misses this.

### Extraction Schema for Numeric Claims

When extracting from FULLTEXT, run a structured extraction pass:

```yaml
Structured Extraction Prompt:
  "Extract all quantitative claims from this paper:
   - Benchmark results (model, dataset, metric, value)
   - Statistical findings (effect size, p-value, CI, n)
   - Performance comparisons (A vs B, metric, values)
   - Key thresholds or cutoffs mentioned

   Return as structured data."
```

### Firecrawl Structured Extraction

Firecrawl supports extraction schemas. Define:

```json
{
  "benchmark_results": [
    {"model": "string", "dataset": "string", "metric": "string", "value": "number"}
  ],
  "statistical_claims": [
    {"claim": "string", "effect_size": "number", "p_value": "number", "n": "number"}
  ],
  "comparisons": [
    {"item_a": "string", "item_b": "string", "metric": "string", "winner": "string", "margin": "string"}
  ]
}
```

### Numeric Confidence Rule

**Rule:** A numeric claim (benchmark, statistic, comparison) CANNOT be HIGH confidence unless:
- The number was extracted from FULLTEXT (not abstract)
- Context (table caption, methodology) was also extracted
- At least one corroborating source confirms the magnitude

### Integration Point

Structured extraction runs during EXTRACT phase for VERDICT and COMPARISON deliverables:

```
EXTRACT (for VERDICT/COMPARISON):
    1. Standard prose extraction → findings.md
    2. Structured numeric extraction → findings_structured.json
    3. Cross-reference numbers between sources
    4. Flag inconsistencies for synthesis
```

---

## Part 7: Grey Literature Access (BLUEPRINT Only)

### Trigger
Only enabled when `deliverable = BLUEPRINT`.

### Sources to Search

| Category | Sources | Search Method |
|----------|---------|---------------|
| Government | NIST, GAO, CBO, EPA | Exa with site filter |
| Standards | ISO, IEEE, W3C, IETF | Exa + direct site search |
| Think Tanks | RAND, Brookings, CSIS | Exa with site filter |
| Patents | USPTO, EPO, Google Patents | Exa or dedicated patent search |

### Search Queries

```yaml
Grey Literature Pass:
  trigger: deliverable == "BLUEPRINT"
  queries:
    - "{topic} site:nist.gov"
    - "{topic} site:rand.org"
    - "{topic} best practices filetype:pdf"
    - "{topic} implementation guide"
    - "{topic} standard specification"
  max_sources: 3 per unit
  tier: 2 or 3 (depending on source)
```

### Integration Point

Runs as additional pass in DISCOVER, only for BLUEPRINT:

```
DISCOVER (BLUEPRINT):
    1. Academic pass
    2. Practitioner pass
    3. Grey literature pass  ← NEW
    4. Counterevidence pass
```

---

## Part 8: Updated Workflow

### Phase 1: PARSE (unchanged + recency policy)

```yaml
Input: User query or SPEC.md
Output: STATE.json

Steps:
  1. Parse research question and units
  2. Auto-detect complexity → select preset
  3. Set contested_flag if VERDICT/COMPARISON or "vs/compare/which" in query
  4. Set recency_policy:
     - fast_moving (AI, security, markets): 18 months
     - scientific (general research): 5 years + foundational
     - historical (established topics): no limit
  5. Write STATE.json
```

### Phase 2: DISCOVER (enhanced)

```yaml
Input: STATE.json
Output: discovery/*.md

Steps:
  1. Academic Pass (OpenAlex + arXiv)
     - Keyword search with recency filter
     - Collect seed papers (top 5 per unit)

  2. Snowball Expansion (NEW)
     - Backward: references of seeds
     - Forward: citations of seeds
     - Max 2 rounds, 5 new sources per round

  3. Practitioner Pass (Exa)
     - Engineering blogs, docs, tutorials
     - Only for standard+ or BLUEPRINT/VERDICT

  4. Grey Literature Pass (NEW, BLUEPRINT only)
     - Government, standards, think tanks

  5. Counterevidence Pass
     - Always for standard+
     - Queries: limitations, failures, criticism
     - Max 2 sources per unit

Output: Raw candidate pool with source metadata
```

### Phase 3: CURATE (enhanced)

```yaml
Input: discovery/*.md
Output: SOURCES.md

Steps:
  1. Deduplication (NEW)
     - Compute canonical key (DOI or fingerprint)
     - Group duplicates, select best version

  2. Retraction Check (NEW)
     - Query Crossref for retraction/correction status
     - Flag retracted sources, exclude from candidates

  3. Tier Assignment
     - Apply tier rules (Tier 1/2/3)
     - Check tier targets, flag if unmet

  4. Full-Text Resolution (NEW)
     - For each candidate: resolve_fulltext(doi)
     - Assign extraction depth: FULLTEXT | ABSTRACT_ONLY | PAYWALLED

  5. Selection
     - Prioritize FULLTEXT sources
     - Meet min sources per unit
     - Respect tier targets (relax if necessary)

  6. Write SOURCES.md with metadata
```

### Phase 4: EXTRACT (enhanced)

```yaml
Input: SOURCES.md
Output: topics/*/findings.md, topics/*/findings_structured.json

Steps:
  1. For each source in SOURCES.md:

     a. Fetch content via resolved URL
        - FULLTEXT: fetch and extract all sections
        - ABSTRACT_ONLY: extract available metadata

     b. Prose Extraction (8 essential fields)
        - Citation, Type, Tier, Main claim, Key evidence
        - Limitations, Relevance, Notes
        - NEW: Extraction depth, Source URL, Sections extracted

     c. Structured Extraction (VERDICT/COMPARISON only)
        - Benchmark results
        - Statistical claims
        - Comparisons

  2. Write findings.md per research unit
  3. Write findings_structured.json if applicable
```

### Phase 5: COMPILE (enhanced)

```yaml
Input: topics/*/findings.md
Output: claims.md

Steps:
  1. Extract all claims from findings

  2. For each claim, compute confidence:
     - Count supporting sources
     - Check FULLTEXT requirement (Gate A)
     - Check for contradictions
     - Apply confidence rules:
       * HIGH: 3+ Tier-1 agree, ≥2 FULLTEXT
       * LOW: 1-2 sources OR Tier-2/3 only OR ABSTRACT_ONLY
       * CONTESTED: credible disagreement

  3. Flag numeric claims without FULLTEXT extraction

  4. Write claims.md with confidence labels and source citations
```

### Phase 6: SYNTHESIZE (automated agent)

```yaml
Input: claims.md, SPEC.md
Output: synthesis/final_deliverable.md

Agent Contract:
  - Reads ONLY: claims.md, SOURCES.md, STATE.json, SPEC.md
  - Never reads: raw tool output, discovery files
  - Writes: final_deliverable.md in requested format

Steps:
  1. Load claims.md and SPEC
  2. Select deliverable template (VERDICT/REPORT/COMPARISON/BLUEPRINT/BIBLIOGRAPHY)
  3. Generate synthesis following template
  4. Include confidence labels inline
  5. Flag CONTESTED claims with both perspectives
  6. Include limitations section
  7. Generate formatted source list
```

### Phase 7: CRITIQUE (automated agent)

```yaml
Input: synthesis/final_deliverable.md, claims.md, SOURCES.md
Output: synthesis/critique.md

Agent Contract:
  - Independent quality assessment
  - Max 1 page output

Checklist:
  [ ] Tier targets met (or justified relaxation)
  [ ] All HIGH claims have ≥2 FULLTEXT Tier-1/2 sources
  [ ] All LOW claims explicitly flagged
  [ ] CONTESTED claims present both sides
  [ ] No retracted sources in HIGH claims
  [ ] Numeric claims have extracted values + context
  [ ] Limitations section complete
  [ ] Deliverable matches SPEC request

Output: Pass/Fail for each check, overall assessment, improvement suggestions
```

---

## Part 9: Updated File Structure

```
research/{slug}/
├── SPEC.md                      # Input specification
├── STATE.json                   # Workflow state, config, flags
│
├── discovery/
│   ├── academic.md              # Keyword + snowball results
│   ├── practitioner.md          # Practitioner pass results
│   ├── grey_literature.md       # BLUEPRINT only
│   └── counterevidence.md       # Counter pass results
│
├── SOURCES.md                   # Curated, deduplicated, with access status
│
├── topics/
│   └── {unit}/
│       ├── findings.md          # Prose extraction
│       └── findings_structured.json  # Numeric extraction (VERDICT/COMPARISON)
│
├── claims.md                    # Evidence registry with confidence
│
├── synthesis/
│   ├── final_deliverable.md     # PRIMARY OUTPUT
│   ├── critique.md              # Quality assessment
│   └── contradictions.md        # If CONTESTED claims exist
│
└── logs/
    ├── runlog.ndjson            # Tool execution log
    ├── checkpoint.md            # Resume checkpoint
    ├── retraction_flags.json    # Flagged sources
    └── dedup_log.json           # Deduplication decisions
```

---

## Part 10: Updated STATE.json Schema

```json
{
  "slug": "project-name",
  "version": "2.0",
  "preset": "standard",
  "contested_flag": false,
  "deliverable": "REPORT",

  "config": {
    "min_sources_per_unit": 3,
    "extraction_depth": "medium",
    "recency_policy": "scientific",
    "recency_window_months": 60,
    "snowball_rounds": 2,
    "snowball_max_per_round": 5
  },

  "tier_targets": {
    "tier_1": 70,
    "tier_2": 25,
    "tier_3": 5
  },

  "gates": {
    "fulltext_required_for_high": true,
    "min_fulltext_for_high": 2,
    "retraction_check_enabled": true,
    "counterevidence_required": true
  },

  "research_units": ["unit1", "unit2", "unit3"],

  "phase": "parse",
  "started_at": "2024-01-01T00:00:00Z",
  "completed_at": null,

  "statistics": {
    "total_candidates": 0,
    "after_dedup": 0,
    "fulltext_resolved": 0,
    "abstract_only": 0,
    "paywalled": 0,
    "retracted_flagged": 0
  }
}
```

---

## Part 11: Skills

### /research {slug} [--preset]

Main entry point. Executes full 7-phase workflow.

```
Usage: /research {slug} [--quick|--standard|--thorough|--decision-support]

Examples:
  /research llm-evaluation --standard
  /research react-vs-vue --decision-support
  /research quantum-ml --thorough
```

### /research-validate {slug}

Pre-synthesis validation. Runs all gates and reports status.

```
Usage: /research-validate {slug}

Checks:
  - FULLTEXT coverage: X% of sources have full text
  - Tier targets: met/unmet with breakdown
  - Retraction flags: any flagged sources
  - HIGH claim validity: all have ≥2 FULLTEXT Tier-1/2
  - Dedup status: any remaining duplicates

Output: PASS/FAIL with details
```

### /research-status {slug}

Check progress of running or completed research.

```
Usage: /research-status {slug}

Output:
  - Current phase
  - Sources found/curated
  - Extraction progress
  - Any blockers or warnings
```

### /research-resume {slug}

Resume interrupted research from checkpoint.

```
Usage: /research-resume {slug}

Behavior:
  - Reads checkpoint.md
  - Resumes from last completed phase
  - Preserves all prior work
```

### /cite {DOI}

Quick citation utility.

```
Usage: /cite {DOI}

Output:
  - Formatted citation (APA)
  - OA availability (via Unpaywall)
  - Retraction status (via Crossref)
  - Best access URL
```

---

## Part 12: MCP Tools Required

### Existing (Keep)

| Tool | Purpose |
|------|---------|
| `mcp__openalex__search_works` | Academic paper search |
| `mcp__openalex__get_work` | Get paper details + references |
| `mcp__arxiv__search_papers` | Preprint search |
| `mcp__exa__web_search_exa` | Web/practitioner search |
| `mcp__firecrawl__firecrawl_scrape` | Content extraction |
| `mcp__crossref__getWorkByDOI` | DOI metadata + retraction check |

### New Required

| Tool | Purpose | Implementation |
|------|---------|----------------|
| Unpaywall resolver | OA URL lookup | WebFetch to API or new MCP server |
| Citation snowball | Get citing/cited works | OpenAlex filters (no new tool needed) |

### OpenAlex Queries for Snowballing

**Get works citing a paper:**
```
mcp__openalex__search_works with filter: cites:{work_id}
```

**Get referenced works:**
```
mcp__openalex__get_work → referenced_works field
```

No new MCP server needed for snowballing - existing OpenAlex tools suffice.

---

## Part 13: Implementation Priority

### Phase 1: Foundation (Do First)

| Item | Effort | Impact | Notes |
|------|--------|--------|-------|
| Unpaywall integration | Low | Critical | Unblocks FULLTEXT gate |
| Extraction depth tagging | Low | Critical | Required for Gate A |
| Deduplication logic | Medium | High | Prevents double-counting |
| Retraction check | Low | High | Uses existing Crossref |

### Phase 2: Discovery Enhancement

| Item | Effort | Impact | Notes |
|------|--------|--------|-------|
| Citation snowballing | Medium | High | Uses existing OpenAlex |
| Counterevidence always-on | Low | Medium | Config change |
| Recency policy | Low | Medium | Parse phase addition |

### Phase 3: Extraction Enhancement

| Item | Effort | Impact | Notes |
|------|--------|--------|-------|
| Structured numeric extraction | Medium | High | For VERDICT/COMPARISON |
| Section-aware extraction | Medium | Medium | Methods/Results/Discussion |

### Phase 4: Automation

| Item | Effort | Impact | Notes |
|------|--------|--------|-------|
| Synthesis agent | Medium | High | Dedicated sub-agent |
| Critique agent | Medium | High | Dedicated sub-agent |
| /research-validate skill | Low | Medium | Gate checking |

### Phase 5: Extensions

| Item | Effort | Impact | Notes |
|------|--------|--------|-------|
| Grey literature pass | Low | Medium | BLUEPRINT only |
| /cite utility | Low | Low | Convenience |

---

## Part 14: Success Criteria

The upgraded system succeeds when:

1. **Depth**: Every HIGH confidence claim is backed by ≥2 sources where we actually read the full paper

2. **Coverage**: Citation snowballing finds foundational/follow-on work that keyword search missed

3. **Trust**: No retracted papers in final output; corrections noted

4. **Accuracy**: Numeric claims have extracted values with context, not paraphrased abstracts

5. **Efficiency**: Deduplication prevents wasted extraction on duplicate sources

6. **Balance**: Counterevidence pass ensures limitations are always represented

7. **Automation**: Synthesis and critique run as agents without manual intervention

8. **Reproducibility**: All decisions logged; research can be audited and resumed

---

## Part 15: Design Principles (Preserved)

1. **Write to files, not context** - All outputs persist to `research/{slug}/`

2. **Quality over quantity** - Find RIGHT sources, not MOST sources

3. **Gates, not phases** - Add enforcement rules, not workflow steps

4. **Fail loudly** - If gates aren't met, report clearly; don't proceed silently

5. **One session completion** - Research completes autonomously in 7 phases

6. **SPEC-responsive** - Output format matches requested deliverable

7. **Explicit limitations** - Always document gaps, thin coverage, contested findings

---

## Appendix A: Unpaywall API Reference

**Endpoint:** `https://api.unpaywall.org/v2/{doi}?email={email}`

**Example Request:**
```
GET https://api.unpaywall.org/v2/10.1038/nature12373?email=research@example.com
```

**Key Response Fields:**
```json
{
  "doi": "10.1038/nature12373",
  "is_oa": true,
  "oa_status": "green",
  "best_oa_location": {
    "url_for_pdf": "https://europepmc.org/articles/pmc3814466?pdf=render",
    "url_for_landing_page": "https://europepmc.org/articles/pmc3814466",
    "version": "acceptedVersion",
    "host_type": "repository"
  }
}
```

**OA Status Values:**
- `gold`: Published OA in journal
- `green`: OA copy in repository
- `hybrid`: OA article in subscription journal
- `bronze`: Free to read but no license
- `closed`: No OA version found

---

## Appendix B: Crossref Retraction Check

**Endpoint:** `https://api.crossref.org/works/{doi}`

**Check for Retraction:**
```json
{
  "message": {
    "DOI": "10.1234/example",
    "relation": {
      "is-retracted-by": ["10.1234/retraction-notice"]
    },
    "update-to": [
      {
        "DOI": "10.1234/correction",
        "type": "correction"
      }
    ]
  }
}
```

**Flags to Check:**
- `relation.is-retracted-by` - Paper has been retracted
- `update-to[].type == "correction"` - Paper has corrections
- `update-to[].type == "retraction"` - Retraction notice

---

## Appendix C: OpenAlex Citation Queries

**Get papers citing a work:**
```
GET https://api.openalex.org/works?filter=cites:W2741809807&sort=cited_by_count:desc&per_page=10
```

**Get references from a work:**
```
GET https://api.openalex.org/works/W2741809807
→ response.referenced_works = ["W123...", "W456...", ...]
```

**Filter by quality:**
```
filter=cites:W2741809807,type:journal-article,cited_by_count:>10,publication_year:>2020
```

---

*Document Version: 2.0*
*Last Updated: 2025-02-03*
*Status: Final Implementation Plan*
