---
name: research-resume
description: Resume interrupted research project
user_prompt: true
---

# /research-resume {slug}

Resume an interrupted research project from where it left off.

## Instructions

### Step 1: Validate Project

Check if `research/{slug}/` exists.

If no slug provided:
- List available projects in `research/`
- Ask user which to resume

If project doesn't exist:
- Report error and stop

### Step 2: Check STATE.json

Read `research/{slug}/STATE.json` to get:
- Last completed phase
- Preset configuration
- Research units
- Deliverable type (for v2.0 conditional files)

If STATE.json doesn't exist but SPEC.md does:
- Resume from Phase 1 (Parse)

### Step 3: Determine Resume Point

Check existing files to find where to resume:

```
research/{slug}/
├── SPEC.md                              # Input
├── STATE.json                           # Phase 1 complete
├── discovery/
│   ├── academic.md                      # Phase 2 progress
│   ├── practitioner.md                  # (optional)
│   ├── counterevidence.md               # (required for >=standard)
│   ├── grey_literature.md               # (BLUEPRINT only)
│   └── snowball.md                      # Citation snowball expansion
├── SOURCES.md                           # Phase 3 complete
├── topics/
│   └── {unit}/
│       ├── findings.md                  # Phase 4 progress
│       └── findings_structured.json     # (VERDICT/COMPARISON only)
├── claims.md                            # Phase 5 complete
├── synthesis/
│   ├── final_deliverable.md             # Phase 6 complete
│   ├── critique.md                      # Phase 7 complete
│   └── contradictions.md                # (if contested)
└── logs/
    ├── checkpoint.md                    # Resume checkpoint
    ├── runlog.ndjson                    # Tool execution log
    ├── dedup_log.json                   # Deduplication decisions
    ├── retraction_flags.json            # Retraction check results
    └── validation.json                  # Pre-synthesis validation
```

### Step 4: Print Status

```
## Resuming: {slug}

**Current State:**
| Phase | Status |
|-------|--------|
| 1. Parse | Complete |
| 2. Discover | Complete |
| 3. Curate | Complete |
| 4. Extract | Partial (2/4 units) |
| 5. Compile | Pending |
| 6. Synthesize | Pending |
| 7. Critique | Pending |

**v2.0 Files:**
| File | Status |
|------|--------|
| dedup_log.json | Present |
| retraction_flags.json | Missing |
| grey_literature.md | N/A (not BLUEPRINT) |
| findings_structured.json | Required (VERDICT) |

**Resuming from:** Phase 4 - Extract
```

### Step 5: Resume Logic

#### No SPEC.md
```
ERROR: No SPEC.md found for "{slug}"
Create research/{slug}/SPEC.md first.
```
**Stop.**

#### SPEC.md only (no STATE.json)
**Resume Phase 1: Parse**
1. Parse SPEC.md
2. Auto-detect complexity
3. Detect recency policy from topic
4. Write STATE.json (v2.0 schema)
5. Continue to Phase 2

#### STATE.json exists, no discovery/*.md
**Resume Phase 2: Discover**
1. Read STATE.json for config
2. Spawn discovery agents based on preset:
   - Academic (always)
   - Practitioner (if needed)
   - Counterevidence (required for >=standard)
   - Grey literature (if BLUEPRINT)
   - Snowball expansion (if >=standard)
3. Continue to Phase 3

#### discovery/*.md exists, no SOURCES.md
**Resume Phase 3: Curate**
1. Read all discovery files
2. Run deduplication pipeline
3. Write `logs/dedup_log.json`
4. Run retraction check on DOIs
5. Write `logs/retraction_flags.json`
6. Resolve full-text access via Unpaywall
7. Filter and organize sources
8. Write SOURCES.md
9. Continue to Phase 4

#### discovery complete, dedup_log.json missing
**Resume at Deduplication** (v2.0 sub-phase)
1. Read all discovery files
2. Run deduplication pipeline
3. Write `logs/dedup_log.json`
4. Continue with retraction check

#### SOURCES.md exists, retraction_flags.json missing
**Resume at Retraction Check** (v2.0 sub-phase)
1. Read SOURCES.md
2. Query Crossref for retraction status of all DOIs
3. Flag retracted papers and expressions of concern
4. Write `logs/retraction_flags.json`
5. Continue to Phase 4

#### SOURCES.md exists, no/partial topics/*/findings.md
**Resume Phase 4: Extract**
1. Read SOURCES.md
2. Check which units have findings.md
3. Extract remaining units
4. If VERDICT/COMPARISON: Generate findings_structured.json
5. Continue to Phase 5

#### topics/*/findings.md complete, no claims.md
**Resume Phase 5: Compile**
1. Read all findings files
2. If VERDICT/COMPARISON: Read findings_structured.json
3. Build claims registry
4. Calculate confidence with v2.0 gates:
   - Gate A: Depth (HIGH needs 2+ FULLTEXT Tier-1/2)
   - Gate B: Safety (counterevidence pass ran)
   - Gate C: Retraction (no retracted in HIGH claims)
5. Write claims.md
6. Recommend `/research-validate {slug}` before continuing
7. Continue to Phase 6

#### claims.md exists, no synthesis/final_deliverable.md
**Resume Phase 6: Synthesize**
1. Check if `/research-validate` was run (logs/validation.json)
2. If not run or FAIL, warn user but continue
3. Read SPEC.md for deliverable type
4. Read claims.md
5. Generate deliverable
6. Write synthesis/final_deliverable.md
7. Continue to Phase 7

#### synthesis/final_deliverable.md exists, no synthesis/critique.md
**Resume Phase 7: Critique**
1. Read deliverable
2. Assess quality including v2.0 checks:
   - Access depth coverage
   - Gate compliance
   - Retraction status
3. Write synthesis/critique.md
4. Update STATE.json to complete

#### All files exist
```
## Research Complete: {slug}

All 7 phases completed.

**Outputs:**
- synthesis/final_deliverable.md - Main deliverable
- synthesis/critique.md - Quality assessment
- claims.md - Evidence registry
- SOURCES.md - Source list

**v2.0 Quality:**
- FULLTEXT coverage: X%
- Retracted sources: N
- Duplicates removed: N

**Key Findings:**
[3-5 bullets from deliverable]

**Confidence:** [From critique]
```
**Do not modify files.**

### Step 6: Continue Execution

After resuming, continue all subsequent phases until:
- All phases complete
- Error requires user input
- Rate limits pause execution
- Validation fails (recommend fix before synthesis)

### Error Handling

**Missing sources:** Continue with available, flag in critique

**Partial extraction:** Check findings.md for completeness, resume from last unit

**Tool failures:** Try fallback, note in logs

**Retracted sources found:** Flag in retraction_flags.json, exclude from HIGH claims

**Dedup log missing:** Regenerate from discovery files

### Checkpoint Writing

After each phase, write to `logs/checkpoint.md`:
```
## Checkpoint: {timestamp}
Phase: {N}
Status: {complete|partial}
v2.0 Checks:
  - Dedup: {complete|pending}
  - Retraction: {complete|pending}
  - Validation: {pass|warn|fail|pending}
Notes: {any issues}
```

### Progress Indicators

Report progress as you work:
```
[Phase 2/7] Running discovery...
  - Academic: 15 results
  - Practitioner: 8 results
  - Counterevidence: 5 results
  - Snowball: 12 additional sources
[Phase 3/7] Curating sources...
  - Deduplication: 4 duplicates removed
  - Retraction check: 0 flagged
  - Full-text resolved: 18 FULLTEXT, 5 ABSTRACT_ONLY
  - SOURCES.md: 23 sources
[Phase 4/7] Extracting...
  - unit1: complete (FULLTEXT: 4, ABSTRACT: 1)
  - unit2: in progress...
[Phase 5/7] Pre-synthesis validation recommended
  - Run: /research-validate {slug}
```

### v2.0 Resume Decision Tree

```
discovery complete?
├── No → Resume Phase 2: Discover
└── Yes → dedup_log.json exists?
    ├── No → Resume at Deduplication
    └── Yes → SOURCES.md exists?
        ├── No → Resume Phase 3: Curate (post-dedup)
        └── Yes → retraction_flags.json exists?
            ├── No → Resume at Retraction Check
            └── Yes → findings complete?
                ├── No → Resume Phase 4: Extract
                └── Yes → claims.md exists?
                    ├── No → Resume Phase 5: Compile
                    └── Yes → final_deliverable.md exists?
                        ├── No → Resume Phase 6: Synthesize
                        └── Yes → critique.md exists?
                            ├── No → Resume Phase 7: Critique
                            └── Yes → COMPLETE
```
