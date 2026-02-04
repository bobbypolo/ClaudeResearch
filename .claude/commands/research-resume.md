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

If STATE.json doesn't exist but SPEC.md does:
- Resume from Phase 1 (Parse)

### Step 3: Determine Resume Point

Check existing files to find where to resume:

```
research/{slug}/
├── SPEC.md                         # Input
├── STATE.json                      # Phase 1 complete
├── discovery/
│   ├── academic.md                 # Phase 2 progress
│   ├── practitioner.md             # (optional)
│   └── counterevidence.md          # (optional)
├── SOURCES.md                      # Phase 3 complete
├── topics/
│   └── {unit}/findings.md          # Phase 4 progress
├── claims.md                       # Phase 5 complete
├── synthesis/
│   ├── final_deliverable.md        # Phase 6 complete
│   └── critique.md                 # Phase 7 complete
└── logs/
    └── checkpoint.md               # Resume checkpoint
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
3. Write STATE.json
4. Continue to Phase 2

#### STATE.json exists, no discovery/*.md
**Resume Phase 2: Discover**
1. Read STATE.json for config
2. Spawn discovery agents based on preset
3. Continue to Phase 3

#### discovery/*.md exists, no SOURCES.md
**Resume Phase 3: Curate**
1. Read all discovery files
2. Deduplicate and filter
3. Write SOURCES.md
4. Continue to Phase 4

#### SOURCES.md exists, no/partial topics/*/findings.md
**Resume Phase 4: Extract**
1. Read SOURCES.md
2. Check which units have findings.md
3. Extract remaining units
4. Continue to Phase 5

#### topics/*/findings.md complete, no claims.md
**Resume Phase 5: Compile**
1. Read all findings files
2. Build claims registry
3. Calculate confidence
4. Write claims.md
5. Continue to Phase 6

#### claims.md exists, no synthesis/final_deliverable.md
**Resume Phase 6: Synthesize**
1. Read SPEC.md for deliverable type
2. Read claims.md
3. Generate deliverable
4. Write synthesis/final_deliverable.md
5. Continue to Phase 7

#### synthesis/final_deliverable.md exists, no synthesis/critique.md
**Resume Phase 7: Critique**
1. Read deliverable
2. Assess quality
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

### Error Handling

**Missing sources:** Continue with available, flag in critique

**Partial extraction:** Check findings.md for completeness, resume from last unit

**Tool failures:** Try fallback, note in logs

### Checkpoint Writing

After each phase, write to `logs/checkpoint.md`:
```
## Checkpoint: {timestamp}
Phase: {N}
Status: {complete|partial}
Notes: {any issues}
```

### Progress Indicators

Report progress as you work:
```
[Phase 2/7] Running discovery...
  - Academic: 15 results
  - Practitioner: 8 results
[Phase 3/7] Curating sources...
  - SOURCES.md: 20 sources
[Phase 4/7] Extracting...
  - unit1: complete
  - unit2: in progress...
```
