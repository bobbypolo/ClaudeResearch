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
- Deliverable type (for v2.0 conditional files)

### Step 3: Check File Existence

Scan for these files:

| File | Phase | Purpose |
|------|-------|---------|
| `SPEC.md` | Input | Research specification |
| `STATE.json` | 1 | Workflow state |
| `discovery/academic.md` | 2 | Academic sources |
| `discovery/practitioner.md` | 2 | Practitioner sources (optional) |
| `discovery/counterevidence.md` | 2 | Counterevidence (required for >=standard) |
| `discovery/grey_literature.md` | 2 | Grey literature (BLUEPRINT only) |
| `discovery/snowball.md` | 2 | Citation snowball expansion |
| `SOURCES.md` | 3 | Curated source list |
| `topics/*/findings.md` | 4 | Extracted evidence |
| `topics/*/findings_structured.json` | 4 | Structured extraction (VERDICT/COMPARISON) |
| `claims.md` | 5 | Evidence registry |
| `synthesis/final_deliverable.md` | 6 | Main output |
| `synthesis/critique.md` | 7 | Quality assessment |
| `logs/retraction_flags.json` | 3 | Retraction check results |
| `logs/dedup_log.json` | 3 | Deduplication decisions |
| `logs/validation.json` | 5 | Pre-synthesis validation |

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

**v2.0 Statistics:**

If findings files exist, count by access depth:
- FULLTEXT: Sources with full text extracted
- ABSTRACT_ONLY: Sources with only abstract available
- PAYWALLED: Sources behind paywall with no OA version

If `logs/retraction_flags.json` exists:
- Count retracted sources flagged
- Count expressions of concern

If `logs/dedup_log.json` exists:
- Count duplicates removed
- Count potential duplicates remaining

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
- Deliverable: {VERDICT|REPORT|COMPARISON|BLUEPRINT|BIBLIOGRAPHY}

### Sources
| Type | Count | Target |
|------|-------|--------|
| Academic | N | 70% |
| Practitioner | N | 25% |
| Other | N | 5% |

### v2.0 Access Depth
| Access Level | Count | Percentage |
|--------------|-------|------------|
| FULLTEXT | N | X% |
| ABSTRACT_ONLY | N | X% |
| PAYWALLED | N | X% |

### v2.0 Quality Checks
| Check | Status |
|-------|--------|
| Retracted flagged | N sources |
| Duplicates removed | N sources |
| Potential duplicates | N remaining |

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

### v2.0 Conditional Files
| File | Required For | Status |
|------|--------------|--------|
| grey_literature.md | BLUEPRINT | [Present|Missing|N/A] |
| findings_structured.json | VERDICT/COMPARISON | [Present|Missing|N/A] |
| snowball.md | >=standard | [Present|Missing|N/A] |
| retraction_flags.json | All | [Present|Missing] |
| dedup_log.json | All | [Present|Missing] |

### Next Steps
- [Action based on current phase]
```

### Step 7: Recommendations

**If not started:** Create SPEC.md, then run `/research {slug}`

**If in progress:** Run `/research-resume {slug}`

**If pre-synthesis:** Run `/research-validate {slug}` to check quality gates

**If complete:** Review `synthesis/final_deliverable.md` and `synthesis/critique.md`

### Step 8: v2.0 Validation Summary

If `logs/validation.json` exists, display last validation result:

```
### Last Validation
- Date: {timestamp}
- Overall: [PASS|PASS WITH WARNINGS|FAIL]
- Checks:
  - FULLTEXT coverage: {X}% ({status})
  - Tier targets: {status}
  - Retraction flags: {status}
  - HIGH claim validity: {status}
  - Deduplication: {status}
```

If validation failed, highlight:
```
⚠️ Validation FAILED - Address issues before synthesis
Run `/research-validate {slug}` for details
```
