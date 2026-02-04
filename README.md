# Research ADE

**Autonomous Research System for Claude Code**

Research ADE executes comprehensive, evidence-based research in a single session using MCP tools to access academic databases (OpenAlex, arXiv) and web sources (Exa). Provide a SPEC, get a confidence-graded synthesis with full source traceability.

---

## What's New in v4.0

### Full-Text Access via Unpaywall
- Automatically retrieves open-access PDFs when available
- Falls back to abstracts with clear "Abstract only" notation
- No API key required (free service)

### Enforcement Gates
- **Depth Gate**: Validates extraction depth meets preset requirements
- **Safety Gate**: Blocks sources without proper attribution or dates
- **Retraction Gate**: Checks for retracted papers via Crossref API

### Citation Snowballing
- Forward snowballing: Finds papers citing key sources
- Backward snowballing: Examines reference lists
- Discovers high-impact sources missed by keyword search

### Enhanced Deduplication Pipeline
- DOI-based exact matching
- Title similarity (>90% threshold)
- Author/year cross-validation
- Prefers peer-reviewed over preprints over web sources

### Structured Data Extraction
- Standardized JSON output for claims
- Machine-readable source metadata
- Cross-reference tracking between claims and sources

### Grey Literature Access
- Government reports (via gov domain filtering)
- Technical standards documents
- Conference proceedings beyond major venues

---

## Features

- **7-Phase Workflow**: Parse -> Discover -> Curate -> Extract -> Compile -> Synthesize -> Critique
- **MCP-Powered Discovery**: OpenAlex (250M+ papers), arXiv (preprints), Exa (web)
- **Full-Text Access**: Unpaywall integration for open-access papers
- **Parallel Agents**: Discovery agents run simultaneously for speed
- **Auto-Complexity Detection**: Presets adjust based on deliverable type
- **Robust Confidence**: HIGH (3+ T1 sources + 2+ full-text) / LOW (1-2 sources) / CONTESTED
- **Full Traceability**: Every claim links to sources with DOIs and tiers
- **Resumable**: STATE.json tracks progress; continue from any checkpoint

## Example Output

See `research/demo/` for a complete example:
- **Topic**: RAG Fundamentals
- **Sources**: 15 curated from 51 discovered
- **Claims**: 14 (10 HIGH, 4 LOW confidence)
- **Output**: `synthesis/final_deliverable.md`

---

## Quick Start

### 1. Create SPEC

```bash
mkdir -p research/my-topic
```

Create `research/my-topic/SPEC.md`:

```markdown
# Research Specification: My Topic

## Research Question
What are the best practices for [topic]?

## Research Units
1. [Area 1]
2. [Area 2]
3. [Area 3]

## Deliverables
REPORT

## User Context
- Use case: [what you're building]
- Constraints: [limits]
- Expertise: [your background]
```

### 2. Run Research

```
/research my-topic
```

Or with preset:
```
/research my-topic --quick       # 2 sources/unit, fast
/research my-topic --standard    # 3 sources/unit, default
/research my-topic --thorough    # 5 sources/unit, comprehensive
```

### 3. Monitor (Optional)

```
/research-status my-topic
```

### 4. Review Results

Primary outputs:
- `synthesis/final_deliverable.md` - Main research deliverable
- `synthesis/critique.md` - Limitations and confidence assessment
- `claims.md` - Evidence registry with confidence levels
- `SOURCES.md` - Curated source list with tiers

---

## Commands

| Command | Description |
|---------|-------------|
| `/research {slug}` | Execute 7-phase workflow |
| `/research {slug} --quick` | Fast mode (2 sources/unit, 2 passes) |
| `/research {slug} --standard` | Default (3 sources/unit, 2-3 passes) |
| `/research {slug} --thorough` | Deep (5 sources/unit, 3 passes + counterevidence) |
| `/research-status {slug}` | Check progress and statistics |
| `/research-resume {slug}` | Continue interrupted research |
| `/research-validate {slug}` | Validate sources and check for retractions |
| `/cite {DOI or title}` | Quick citation lookup and formatting |

---

## Presets

| Preset | Sources/Unit | Passes | Counterevidence | Use When |
|--------|--------------|--------|-----------------|----------|
| `--quick` | 2 | 2 | No | Exploration, time-sensitive |
| `--standard` | 3 | 2-3 | If contested | Default |
| `--thorough` | 5 | 3 | Yes | Critical decisions |
| `--decision-support` | 4 | 3 | Yes | VERDICT/COMPARISON |

---

## How It Works

### Phase 1: Parse
- Reads SPEC.md, validates required sections
- Auto-detects complexity and recency policy
- Writes STATE.json with configuration
- Creates directory structure

### Phase 2: Discover
- Spawns parallel agents (Academic + Practitioner)
- Academic: OpenAlex + arXiv for peer-reviewed/preprints
- Practitioner: Exa for tutorials, docs, case studies
- Counterevidence pass (if --thorough or contested topic)
- **NEW**: Citation snowballing for key sources

### Phase 3: Curate
- Merges discovery results with enhanced deduplication
- **NEW**: Retraction checking via Crossref
- Filters by tier targets and relevance
- Writes SOURCES.md with curated list

### Phase 4: Extract
- Reads top N sources per unit (based on preset)
- **NEW**: Unpaywall integration for full-text access
- Uses arXiv API for preprints, Firecrawl for web
- **NEW**: Depth gate validates extraction completeness
- Writes findings to `topics/{unit}/findings.md`

### Phase 5: Compile
- Builds claims registry from extracted evidence
- **NEW**: Enhanced confidence requires 2+ full-text sources for HIGH
- Calculates confidence: HIGH (3+ T1 + 2+ FULLTEXT) / LOW (1-2) / CONTESTED
- Writes claims.md

### Phase 6: Synthesize
- Generates deliverable matching SPEC type
- REPORT, VERDICT, COMPARISON, BLUEPRINT, or BIBLIOGRAPHY
- Writes `synthesis/final_deliverable.md`

### Phase 7: Critique
- Self-assesses source quality and coverage
- **NEW**: Reports full-text vs abstract-only ratio
- Documents limitations and what could invalidate conclusions
- Writes `synthesis/critique.md`

---

## Output Files

```
research/{slug}/
├── SPEC.md                     # Your specification (input)
├── STATE.json                  # Workflow state and config
├── discovery/
│   ├── academic.md             # OpenAlex + arXiv results
│   ├── practitioner.md         # Exa results
│   ├── counterevidence.md      # Critiques (if run)
│   └── snowball.md             # Citation snowballing results (NEW)
├── SOURCES.md                  # Curated source list
├── topics/
│   └── {unit}/
│       ├── findings.md         # Extracted evidence per unit
│       └── findings.json       # Structured extraction (NEW)
├── claims.md                   # Evidence registry
├── claims.json                 # Machine-readable claims (NEW)
├── validation/
│   └── retraction_check.md     # Retraction scan results (NEW)
└── synthesis/
    ├── final_deliverable.md    # PRIMARY OUTPUT
    ├── critique.md             # Quality assessment
    └── contradictions.md       # If contested
```

---

## Deliverable Types

| Type | Use When | Output Format |
|------|----------|---------------|
| **REPORT** | "What is X?" | Findings by research unit |
| **VERDICT** | "Which should I use?" | Recommendation + comparison matrix |
| **COMPARISON** | "Compare A vs B" | Neutral side-by-side analysis |
| **BLUEPRINT** | "How to design X?" | Architecture + implementation steps |
| **BIBLIOGRAPHY** | "What sources exist?" | Annotated source list |

---

## Confidence Levels

| Level | Requirement | Display |
|-------|-------------|---------|
| **HIGH** | 3+ Tier-1 sources agree AND 2+ full-text accessed | Stated with confidence |
| **LOW** | 1-2 sources only OR abstract-only extraction | Flagged as tentative |
| **CONTESTED** | Sources disagree | Both positions presented |

---

## Source Tiers

| Tier | Examples | Target |
|------|----------|--------|
| **1** | Peer-reviewed journals, major conferences (ACL, NeurIPS) | 70% |
| **2** | arXiv preprints, patents, tech reports, authoritative docs | 25% |
| **3** | Blogs, tutorials, whitepapers | 5% |

*Tier targets auto-adjust for emerging fields with limited peer review.*

---

## Prerequisites

### Required MCP Servers

| Server | Purpose | API Key |
|--------|---------|---------|
| **OpenAlex** | Academic papers (250M+) | Free |
| **arXiv** | Preprints | Free |
| **Exa** | Web search | Required |
| **Firecrawl** | Content extraction | Required |
| **Crossref** | DOI validation, retraction checking | Free |

### Optional Services

| Service | Purpose | API Key |
|---------|---------|---------|
| **Unpaywall** | Full-text PDF access | Free (no key needed) |

### Configuration

See `docs/RESEARCH_SETUP.md` for:
- MCP server configuration
- API key setup
- Permission/sandbox settings

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No sources found | Broaden key terms, verify MCP servers running |
| Extraction failing | Firecrawl rate-limited; wait and `/research-resume` |
| Low Tier-1 percentage | Field may be too new; document as limitation |
| Research interrupted | Use `/research-resume {slug}` to continue |
| Retracted paper found | System auto-excludes and logs in validation/ |

---

## Documentation

| File | Content |
|------|---------|
| `docs/RESEARCH_SETUP.md` | MCP setup, permissions, hooks |
| `.claude/CLAUDE.md` | System constitution (7 principles) |
| `.claude/rules/research.md` | Schemas and rubrics |
| `templates/SPEC.md` | SPEC template |
| `research/demo/` | Working example output |

---

## Comparison: Research ADE vs Standard Claude Research

| Aspect | Standard Mode | Research ADE |
|--------|---------------|--------------|
| Sources | Web search snippets | OpenAlex, arXiv, Exa, Unpaywall |
| Full-text access | Rare | Systematic via Unpaywall |
| Traceability | Weak | DOI, citations, tiers |
| Confidence | Implicit | Explicit HIGH/LOW/CONTESTED |
| Retraction checking | None | Automatic via Crossref |
| Persistence | None | Full file structure |
| Reproducibility | None | STATE.json + artifacts |
| Best for | Quick questions | Rigorous research |

---

**Version 4.0** | Enhanced with Full-Text Access, Enforcement Gates, and Citation Snowballing
