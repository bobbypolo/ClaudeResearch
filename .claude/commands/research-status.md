---
name: research-status
description: Check research project progress
user_prompt: true
---

# /research-status {slug}

Check the progress and status of a research project.

## Instructions

### Step 1: Validate Project

Check if `research/{slug}/` exists. If not:
- List available research projects in `research/`
- Report that the requested project does not exist

### Step 2: Read STATE.json

If `research/{slug}/STATE.json` exists, read it to get:
- Current phase
- Preset configuration
- Research units
- Min sources per unit

### Step 3: Check File Existence

Scan for these files:

| File | Phase | Purpose |
|------|-------|---------|
| `SPEC.md` | Input | Research specification |
| `STATE.json` | 1 | Workflow state |
| `discovery/academic.md` | 2 | Academic sources |
| `discovery/practitioner.md` | 2 | Practitioner sources (optional) |
| `discovery/counterevidence.md` | 2 | Counterevidence (optional) |
| `SOURCES.md` | 3 | Curated source list |
| `topics/*/findings.md` | 4 | Extracted evidence |
| `claims.md` | 5 | Evidence registry |
| `synthesis/final_deliverable.md` | 6 | Main output |
| `synthesis/critique.md` | 7 | Quality assessment |

### Step 4: Determine Current Phase

| Files Present | Phase | Status |
|---------------|-------|--------|
| None | - | Not started |
| SPEC.md only | 1 | Ready to start |
| STATE.json exists | 1 | Parse complete |
| discovery/*.md files | 2 | Discovery complete |
| SOURCES.md exists | 3 | Curation complete |
| topics/*/findings.md | 4 | Extraction complete |
| claims.md exists | 5 | Compilation complete |
| synthesis/final_deliverable.md | 6 | Synthesis complete |
| synthesis/critique.md | 7 | COMPLETE |

### Step 5: Gather Statistics

If SOURCES.md exists:
- Count sources by type (ACADEMIC, PRACTITIONER, OTHER)
- Count by tier (1, 2, 3)
- Check coverage per research unit

If claims.md exists:
- Count claims by confidence (HIGH, LOW, CONTESTED)
- Identify any gaps

### Step 6: Output Status Report

```
## Research Status: {slug}

### Current Phase
Phase [N]/7: [Phase Name]
Status: [NOT STARTED | IN PROGRESS | COMPLETE]

### Progress
- [x] Phase 1: Parse (SPEC.md -> STATE.json)
- [x] Phase 2: Discover (discovery/*.md)
- [x] Phase 3: Curate (SOURCES.md)
- [ ] Phase 4: Extract (topics/*/findings.md)
- [ ] Phase 5: Compile (claims.md)
- [ ] Phase 6: Synthesize (synthesis/final_deliverable.md)
- [ ] Phase 7: Critique (synthesis/critique.md)

### Configuration
- Preset: {preset}
- Min sources/unit: {min}
- Extraction depth: {depth}
- Contested: {yes/no}

### Sources
| Type | Count | Target |
|------|-------|--------|
| Academic | N | 70% |
| Practitioner | N | 25% |
| Other | N | 5% |

### Claims
| Confidence | Count |
|------------|-------|
| HIGH | N |
| LOW | N |
| CONTESTED | N |

### Coverage
| Research Unit | Sources | Status |
|---------------|---------|--------|
| {unit1} | N | [OK|GAP] |

### Next Steps
- [Action based on current phase]
```

### Step 7: Recommendations

**If not started:** Create SPEC.md, then run `/research {slug}`

**If in progress:** Run `/research-resume {slug}`

**If complete:** Review `synthesis/final_deliverable.md` and `synthesis/critique.md`
