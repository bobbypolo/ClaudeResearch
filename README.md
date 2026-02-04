# Research ADE

**Autonomous Research System for Claude Code**

Research ADE executes comprehensive, evidence-based research in a single session using MCP tools to access academic databases (OpenAlex, arXiv) and web sources (Exa). Provide a SPEC, get a confidence-graded synthesis with full source traceability.

## Features

- **7-Phase Workflow**: Parse → Discover → Curate → Extract → Compile → Synthesize → Critique
- **MCP-Powered Discovery**: OpenAlex (250M+ papers), arXiv (preprints), Exa (web)
- **Parallel Agents**: Discovery agents run simultaneously for speed
- **Auto-Complexity Detection**: Presets adjust based on deliverable type
- **Simple Confidence**: HIGH (3+ sources) / LOW (1-2 sources) / CONTESTED
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
- Auto-detects complexity, sets preset if not specified
- Writes STATE.json with configuration
- Creates directory structure

### Phase 2: Discover
- Spawns parallel agents (Academic + Practitioner)
- Academic: OpenAlex + arXiv for peer-reviewed/preprints
- Practitioner: Exa for tutorials, docs, case studies
- Counterevidence pass (if --thorough or contested topic)

### Phase 3: Curate
- Merges discovery results, deduplicates by DOI/title
- Filters by tier targets and relevance
- Writes SOURCES.md with curated list

### Phase 4: Extract
- Reads top N sources per unit (based on preset)
- Uses arXiv API for preprints, Firecrawl for web
- Writes findings to `topics/{unit}/findings.md`

### Phase 5: Compile
- Builds claims registry from extracted evidence
- Calculates confidence: HIGH (3+ T1) / LOW (1-2) / CONTESTED
- Writes claims.md

### Phase 6: Synthesize
- Generates deliverable matching SPEC type
- REPORT, VERDICT, COMPARISON, BLUEPRINT, or BIBLIOGRAPHY
- Writes `synthesis/final_deliverable.md`

### Phase 7: Critique
- Self-assesses source quality and coverage
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
│   └── practitioner.md         # Exa results
├── SOURCES.md                  # Curated source list
├── topics/
│   └── {unit}/findings.md      # Extracted evidence per unit
├── claims.md                   # Evidence registry
└── synthesis/
    ├── final_deliverable.md    # PRIMARY OUTPUT
    └── critique.md             # Quality assessment
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
| **HIGH** | 3+ Tier-1/2 sources agree | Stated with confidence |
| **LOW** | 1-2 sources only | Flagged as tentative |
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
| **Crossref** | DOI validation | Free |

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
| Sources | Web search snippets | OpenAlex, arXiv, Exa |
| Traceability | Weak | DOI, citations, tiers |
| Confidence | Implicit | Explicit HIGH/LOW/CONTESTED |
| Persistence | None | Full file structure |
| Reproducibility | None | STATE.json + artifacts |
| Best for | Quick questions | Rigorous research |

---

**Version 3.0** | Simplified 7-Phase Workflow
