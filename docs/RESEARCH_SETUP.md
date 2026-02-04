# Research ADE v5.0 - Setup Guide

## MCP Server Configuration

### Required Servers

Add to your Claude Code MCP configuration:

```json
{
  "mcpServers": {
    "openalex": {
      "command": "npx",
      "args": ["-y", "@anthropic/openalex-mcp"]
    },
    "arxiv": {
      "command": "npx",
      "args": ["-y", "@anthropic/arxiv-mcp"]
    },
    "exa": {
      "command": "npx",
      "args": ["-y", "@anthropic/exa-mcp"],
      "env": { "EXA_API_KEY": "your-exa-api-key" }
    },
    "firecrawl": {
      "command": "npx",
      "args": ["-y", "@anthropic/firecrawl-mcp"],
      "env": { "FIRECRAWL_API_KEY": "your-firecrawl-api-key" }
    },
    "crossref": {
      "command": "npx",
      "args": ["-y", "@anthropic/crossref-mcp"]
    }
  }
}
```

### API Keys

| Service | Cost | Get Key At |
|---------|------|------------|
| OpenAlex | Free | No key needed |
| arXiv | Free | No key needed |
| Crossref | Free | No key needed |
| Unpaywall | Free | No key needed (uses email for identification) |
| Exa | Paid | https://exa.ai |
| Firecrawl | Paid | https://firecrawl.dev |

### MCP Tools Used

| Phase | Tools |
|-------|-------|
| Discovery | `mcp__openalex__search_works`, `mcp__arxiv__search_papers`, `mcp__exa__web_search_exa` |
| Snowballing | `mcp__openalex__get_work_references`, `mcp__openalex__get_work_citations` |
| Full-Text | WebFetch to Unpaywall API, `mcp__firecrawl__firecrawl_scrape` |
| Extraction | `mcp__arxiv__read_paper`, `mcp__firecrawl__firecrawl_scrape` |
| Verification | `mcp__crossref__getWorkByDOI` (retraction check, metadata) |

---

## Quick Verification

After configuring MCP servers, verify they're working:

```
ToolSearch "+openalex"   # Should find mcp__openalex__search_works
ToolSearch "+arxiv"      # Should find mcp__arxiv__search_papers
ToolSearch "+exa"        # Should find mcp__exa__web_search_exa
```

Then run the demo:
```
/research-status demo    # Check existing demo
/research demo --quick   # Or run fresh with quick preset
```

---

## v5.0 Features Setup

### Mandatory Planning Phase (NEW)

No special configuration needed. The system automatically:
1. Creates `PLAN.md` before any discovery
2. Presents plan to user for approval
3. Blocks research until user approves

### Failure Analysis (Replaces Counterevidence)

The system searches for failed implementations and extracts lessons learned:
- Search patterns: `{method} failed`, `{method} pitfalls`, `{method} lessons learned`
- Output: `discovery/failure_analysis.md`
- Risk-mitigation pairs compiled in `synthesis/risk_mitigations.md`

### Completion Gate (NEW)

Enforces HIGH confidence on all recommendations OR explicit gap declarations:
- If recommendation has LOW confidence → must document gap in `synthesis/gaps.md`
- Research does not end with "feasible under narrow conditions"
- Either know how to do it, or document exactly what's missing

### Unpaywall Integration (Full-Text Access)

No configuration needed. The system uses WebFetch to query:
```
https://api.unpaywall.org/v2/{doi}?email=research@example.com
```

Returns OA status (gold/green/hybrid/bronze/closed) and PDF URLs when available.

### Citation Snowballing

Uses OpenAlex tools already configured:
- `mcp__openalex__get_work_references` - Backward snowball (what does this paper cite?)
- `mcp__openalex__get_work_citations` - Forward snowball (what papers cite this?)

### Retraction Checking

Uses Crossref API via `mcp__crossref__getWorkByDOI`:
- Checks `relation.is-retracted-by` field
- Checks `update-to` for corrections
- Results logged to `logs/retraction_flags.json`

---

## Performance Expectations

Based on actual workflow execution:

| Preset | Agents | Duration | Sources | Snowball | Failure Analysis |
|--------|--------|----------|---------|----------|------------------|
| `--quick` | 2 parallel | ~2-3 min | ~15-20 | No | No |
| `--standard` | 3 parallel | ~5-7 min | ~40-50 | Yes | Yes |
| `--thorough` | 4 parallel | ~8-12 min | ~60-80 | Yes | Yes |

*Duration depends on MCP server response times, snowball depth, and extraction complexity.*

---

## Permissions (Optional)

To reduce approval prompts during research:

### Option 1: Scoped Permissions

```
/permissions add Write research/**
/permissions add Read research/**
```

### Option 2: Session Approval

When prompted, approve tools for the session:
- `mcp__openalex__*` - Academic searches + snowballing
- `mcp__arxiv__*` - Preprint searches
- `mcp__exa__*` - Web searches
- `mcp__firecrawl__*` - Content extraction
- `mcp__crossref__*` - DOI validation + retraction check

---

## File Structure (v5.0)

After running `/research {slug}`:

```
research/{slug}/
├── PLAN.md                     # Research plan (requires approval) [NEW]
├── SPEC.md                     # Your input (Goal, not Question)
├── STATE.json                  # Workflow state and config (v3.0 schema)
│
├── discovery/
│   ├── academic.md             # OpenAlex + arXiv
│   ├── practitioner.md         # Exa web sources
│   ├── failure_analysis.md     # Failure studies (was counterevidence)
│   ├── grey_literature.md      # BLUEPRINT only
│   └── snowball.md             # Citation snowballing
│
├── SOURCES.md                  # Curated list with access tags
│
├── topics/
│   └── {unit}/
│       ├── findings.md         # Extracted evidence (12 fields)
│       └── findings_structured.json  # Structured data
│
├── claims.md                   # Evidence registry with gate checks
│
├── synthesis/
│   ├── final_deliverable.md    # PRIMARY OUTPUT
│   ├── critique.md             # Limitations + gate compliance
│   ├── risk_mitigations.md     # Compiled risk-mitigation pairs [NEW]
│   └── gaps.md                 # Gap declarations (if any) [NEW]
│
└── logs/
    ├── runlog.ndjson           # Tool execution log
    ├── checkpoint.md           # Resume checkpoint
    ├── dedup_log.json          # Deduplication decisions
    └── retraction_flags.json   # Retraction check results
```

---

## Troubleshooting

### "Tool not found"

MCP server not loaded. Restart Claude Code or check config:
```
/mcp status
```

### "No sources found"

1. Check key terms for typos
2. Broaden search terms (less specific)
3. Verify MCP servers are responding

### "Extraction failed"

Firecrawl may be rate-limited or URL inaccessible:
- System tries Unpaywall for OA version first
- Falls back to abstract if no full-text available
- Marks source as "ABSTRACT_ONLY" or "PAYWALLED"
- Documents gap in `synthesis/critique.md`

### "Retracted paper found"

System auto-excludes retracted papers:
- Logged in `logs/retraction_flags.json`
- Removed from SOURCES.md
- Cannot support HIGH confidence claims

### "Research interrupted"

Resume from last checkpoint:
```
/research-resume {slug}
```

STATE.json tracks current phase; workflow continues from there.

### "Plan not approved"

Research cannot proceed until user approves the plan:
1. Review `PLAN.md` for accuracy
2. Modify if needed
3. Run `/research {slug}` again and approve

### "Completion Gate failed"

LOW confidence recommendations need gap declarations:
1. Check which claims have LOW confidence in `claims.md`
2. Document gaps in `synthesis/gaps.md`
3. Run `/research-validate {slug}` to verify

---

## Commands Reference

| Command | Description |
|---------|-------------|
| `/research {slug}` | Execute full 8-phase workflow |
| `/research {slug} --quick` | Fast mode (2 sources/unit, no failure analysis) |
| `/research {slug} --standard` | Default (3 sources/unit + failure analysis) |
| `/research {slug} --thorough` | Deep (5 sources/unit + all gates) |
| `/research-status {slug}` | Check progress and statistics |
| `/research-resume {slug}` | Continue interrupted research |
| `/research-validate {slug}` | Check gates before synthesis |
| `/cite {DOI}` | Quick citation lookup with OA status |

---

## Version 5.0

Enhanced from v4.0 with:
- **Mandatory planning phase** - User approves research plan before execution
- **Optimistic-empirical posture** - "Solutions exist until proven otherwise"
- **Failure analysis** - Extracts lessons from failed implementations
- **Risk-mitigation pairs** - Every risk paired with evidence-based mitigation
- **Completion Gate** - HIGH confidence required or explicit gaps declared
- **SPECIFICATION deliverable** - Implementation-focused output (new default)
- **8-phase workflow** - Plan → Parse → Survey → Deep Dive → Failure → Compile → Specify → Validate
