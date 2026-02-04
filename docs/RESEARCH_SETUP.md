# Research ADE v4.0 - Setup Guide

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

A working demo is included at `research/demo/` showing complete output.

---

## v4.0 Features Setup

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

| Preset | Agents | Duration | Sources | Snowball |
|--------|--------|----------|---------|----------|
| `--quick` | 2 parallel | ~2-3 min | ~15-20 | No |
| `--standard` | 3 parallel | ~5-7 min | ~40-50 | Yes |
| `--thorough` | 4 parallel | ~8-12 min | ~60-80 | Yes |

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

## File Structure

After running `/research {slug}`:

```
research/{slug}/
├── SPEC.md                     # Your input
├── STATE.json                  # Workflow state and config
│
├── discovery/
│   ├── academic.md             # OpenAlex + arXiv
│   ├── practitioner.md         # Exa web sources
│   ├── counterevidence.md      # Critiques (standard+ presets)
│   ├── grey_literature.md      # BLUEPRINT only (v4.0)
│   └── snowball.md             # Citation snowballing (v4.0)
│
├── SOURCES.md                  # Curated list with access tags
│
├── topics/
│   └── {unit}/
│       ├── findings.md         # Extracted evidence
│       └── findings_structured.json  # Structured data (v4.0)
│
├── claims.md                   # Evidence registry with gate checks
│
├── synthesis/
│   ├── final_deliverable.md    # PRIMARY OUTPUT
│   ├── critique.md             # Limitations
│   └── contradictions.md       # If contested
│
└── logs/
    ├── runlog.ndjson           # Tool execution log
    ├── checkpoint.md           # Resume checkpoint
    ├── dedup_log.json          # Deduplication decisions (v4.0)
    └── retraction_flags.json   # Retraction check results (v4.0)
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

---

## Example: Demo Output

The included `research/demo/` contains a complete example:

| File | Content |
|------|---------|
| `SPEC.md` | RAG Fundamentals research spec |
| `STATE.json` | Preset: standard, 3 units |
| `discovery/academic.md` | 25 sources from OpenAlex/arXiv |
| `discovery/practitioner.md` | 26 sources from Exa |
| `SOURCES.md` | 15 curated sources |
| `topics/*/findings.md` | Extracted evidence |
| `claims.md` | 14 claims (10 HIGH, 4 LOW) |
| `synthesis/final_deliverable.md` | REPORT deliverable |
| `synthesis/critique.md` | Quality assessment |

---

## Commands Reference

| Command | Description |
|---------|-------------|
| `/research {slug}` | Execute full 7-phase workflow |
| `/research {slug} --quick` | Fast mode (2 sources/unit) |
| `/research {slug} --standard` | Default (3 sources/unit + snowball) |
| `/research {slug} --thorough` | Deep (5 sources/unit + all gates) |
| `/research-status {slug}` | Check progress and statistics |
| `/research-resume {slug}` | Continue interrupted research |
| `/research-validate {slug}` | Check gates before synthesis |
| `/cite {DOI}` | Quick citation lookup with OA status |

---

## Version 4.0

Enhanced from v3.0 with:
- Full-text access via Unpaywall integration
- Citation snowballing (forward + backward)
- Enforcement gates (Depth, Safety, Retraction)
- Structured data extraction for VERDICT/COMPARISON
- Grey literature pass for BLUEPRINT
- Domain-aware recency policies
- Enhanced deduplication pipeline
