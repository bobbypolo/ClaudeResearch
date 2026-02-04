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
- Deliverable type
- Plan approval status
- Gate statuses

### Step 3: Check File Existence

Scan for these files (v5.0 structure):

| File | Phase | Purpose |
|------|-------|---------|
| `PLAN.md` | 0 | Research plan (requires approval) |
| `SPEC.md` | Input | Research specification (Goal, not Question) |
| `STATE.json` | 1 | Workflow state (v3.0 schema) |
| `discovery/academic.md` | 2 | Academic sources |
| `discovery/practitioner.md` | 2 | Practitioner sources (optional) |
| `discovery/failure_analysis.md` | 2 | Failure studies (required for >=standard) |
| `discovery/grey_literature.md` | 2 | Grey literature (BLUEPRINT only) |
| `discovery/snowball.md` | 2 | Citation snowball expansion |
| `SOURCES.md` | 3 | Curated source list with impl detail flags |
| `topics/*/findings.md` | 3-4 | Extracted evidence (12 fields) |
| `topics/*/findings_structured.json` | 3-4 | Structured extraction |
| `synthesis/risk_mitigations.md` | 4 | Risk-mitigation pairs |
| `claims.md` | 5 | Evidence registry with gate checks |
| `synthesis/gaps.md` | 5 | Gap declarations (if any) |
| `synthesis/final_deliverable.md` | 6 | Main output |
| `synthesis/critique.md` | 7 | Quality assessment |
| `logs/retraction_flags.json` | 3 | Retraction check results |
| `logs/dedup_log.json` | 3 | Deduplication decisions |

### Step 4: Determine Current Phase (v5.0 - 8 Phases)

| Files Present | Phase | Status |
|---------------|-------|--------|
| None | - | Not started |
| SPEC.md only | 0 | Ready to plan |
| PLAN.md exists (not approved) | 0 | Awaiting plan approval |
| PLAN.md + STATE.json | 1 | Parse complete |
| discovery/*.md files | 2 | Survey complete |
| SOURCES.md + topics/*/findings.md | 3 | Deep dive complete |
| synthesis/risk_mitigations.md | 4 | Failure analysis complete |
| claims.md exists | 5 | Compilation complete |
| synthesis/final_deliverable.md | 6 | Specification complete |
| synthesis/critique.md | 7 | COMPLETE |

### Step 5: Gather Statistics

If SOURCES.md exists:
- Count sources by type (ACADEMIC, PRACTITIONER, OTHER)
- Count by tier (1, 2, 3)
- Count sources with implementation detail
- Check coverage per research unit

If claims.md exists:
- Count claims by confidence (HIGH, LOW, CONTESTED)
- Count recommendations vs findings
- Identify declared gaps

**Access Depth Statistics:**

If findings files exist, count by access depth:
- FULLTEXT: Sources with full text extracted
- ABSTRACT_ONLY: Sources with only abstract available
- PAYWALLED: Sources behind paywall with no OA version

**Gate Statistics:**

If STATE.json gates exist:
- Depth Gate: status, claims downgraded
- Completion Gate: status, gaps declared
- Retraction Gate: status, sources removed

If `synthesis/risk_mitigations.md` exists:
- Count risk-mitigation pairs

### Step 6: Output Status Report

```
## Research Status: {slug}

### Current Phase
Phase [N]/8: [Phase Name]
Status: [NOT STARTED | AWAITING APPROVAL | IN PROGRESS | COMPLETE]

### Progress
- [ ] Phase 0: Plan (PLAN.md - awaiting approval)
- [x] Phase 1: Parse (SPEC.md -> STATE.json)
- [x] Phase 2: Survey (discovery/*.md)
- [x] Phase 3: Deep Dive (SOURCES.md, topics/*/findings.md)
- [ ] Phase 4: Failure (synthesis/risk_mitigations.md)
- [ ] Phase 5: Compile (claims.md)
- [ ] Phase 6: Specify (synthesis/final_deliverable.md)
- [ ] Phase 7: Validate (synthesis/critique.md)

### Configuration
- Preset: {preset}
- Posture: optimistic-empirical
- Min sources/unit: {min}
- Extraction depth: {depth}
- Deliverable: {SPECIFICATION|VERDICT|REPORT|COMPARISON|BLUEPRINT|BIBLIOGRAPHY}
- Plan approved: {yes/no}

### Sources
| Type | Count | Target |
|------|-------|--------|
| Academic | N | 70% |
| Practitioner | N | 25% |
| Other | N | 5% |

### Implementation Detail
| Category | Count |
|----------|-------|
| With impl detail | N |
| Without impl detail | N |

### Access Depth
| Access Level | Count | Percentage |
|--------------|-------|------------|
| FULLTEXT | N | X% |
| ABSTRACT_ONLY | N | X% |
| PAYWALLED | N | X% |

### Gates (v5.0)
| Gate | Status | Details |
|------|--------|---------|
| Depth (A) | PASSED/PENDING | N claims downgraded |
| Completion (B) | PASSED/PENDING | N gaps declared |
| Retraction (C) | PASSED/PENDING | N sources removed |

### Claims
| Confidence | Count |
|------------|-------|
| HIGH | N |
| LOW (with gaps) | N |
| CONTESTED | N |

### Risk-Mitigation Pairs
| Count | Source |
|-------|--------|
| N | failure_analysis.md |

### Coverage
| Research Unit | Sources | Impl Detail | Status |
|---------------|---------|-------------|--------|
| {unit1} | N | N | [OK|GAP] |

### Conditional Files (v5.0)
| File | Required For | Status |
|------|--------------|--------|
| PLAN.md | All | [Present|Missing] |
| failure_analysis.md | >=standard | [Present|Missing|N/A] |
| risk_mitigations.md | >=standard | [Present|Missing|N/A] |
| gaps.md | If LOW claims | [Present|Missing|N/A] |
| grey_literature.md | BLUEPRINT | [Present|Missing|N/A] |
| findings_structured.json | SPECIFICATION/VERDICT/COMPARISON | [Present|Missing|N/A] |
| snowball.md | >=standard | [Present|Missing|N/A] |

### Next Steps
- [Action based on current phase]
```

### Step 7: Recommendations

**If not started:** Create SPEC.md, then run `/research {slug}`

**If plan awaiting approval:** Review PLAN.md and approve to continue

**If in progress:** Run `/research-resume {slug}`

**If pre-synthesis:** Run `/research-validate {slug}` to check quality gates

**If complete:** Review `synthesis/final_deliverable.md` and `synthesis/critique.md`

### Step 8: Gate Summary

Display gate compliance summary:

```
### Gate Compliance
| Gate | Requirement | Status |
|------|-------------|--------|
| Depth (A) | 2+ FULLTEXT T1/T2 for HIGH | {PASSED/FAILED} |
| Completion (B) | HIGH confidence or gaps declared | {PASSED/FAILED} |
| Retraction (C) | No retracted papers in claims | {PASSED/FAILED} |

**Overall:** [ALL PASSED | N FAILED]
```

If Completion Gate has gaps:
```
### Declared Gaps
- Gap 1: {description}
- Gap 2: {description}
```
