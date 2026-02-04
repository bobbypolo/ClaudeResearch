# Research ADE - Setup Guide

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
| Exa | Paid | https://exa.ai |
| Firecrawl | Paid | https://firecrawl.dev |

### MCP Tools Used

| Phase | Tools |
|-------|-------|
| Discovery | `mcp__openalex__search_works`, `mcp__arxiv__search_papers`, `mcp__exa__web_search_exa` |
| Extraction | `mcp__arxiv__read_paper`, `mcp__firecrawl__firecrawl_scrape` |
| Verification | `mcp__crossref__getWorkByDOI` (sparingly) |

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

## Performance Expectations

Based on actual workflow execution:

| Preset | Agents | Duration | Sources |
|--------|--------|----------|---------|
| `--quick` | 2 parallel | ~2-3 min | ~15-20 |
| `--standard` | 2 parallel | ~4-5 min | ~40-50 |
| `--thorough` | 3 parallel | ~6-8 min | ~60-80 |

*Duration depends on MCP server response times and extraction complexity.*

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
- `mcp__openalex__*` - Academic searches
- `mcp__arxiv__*` - Preprint searches
- `mcp__exa__*` - Web searches
- `mcp__firecrawl__*` - Content extraction

---

## File Structure

After running `/research {slug}`:

```
research/{slug}/
├── SPEC.md                     # Your input
├── STATE.json                  # Workflow config
│
├── discovery/
│   ├── academic.md             # OpenAlex + arXiv
│   └── practitioner.md         # Exa web sources
│
├── SOURCES.md                  # Curated list
│
├── topics/
│   └── {unit}/
│       └── findings.md         # Extracted evidence
│
├── claims.md                   # Evidence registry
│
└── synthesis/
    ├── final_deliverable.md    # PRIMARY OUTPUT
    └── critique.md             # Limitations
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
- System marks source as "Abstract only"
- Continues with available content
- Documents gap in `synthesis/critique.md`

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

## Version 3.0

Simplified from v2.0:
- 7 phases (was 10)
- 3 confidence levels (was 4)
- 8-field extraction (was 20+)
- No Core/Supporting classification
- Auto-complexity detection
