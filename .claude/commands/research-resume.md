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
- Deliverable type
- Plan approval status
- Gate statuses

If STATE.json doesn't exist but SPEC.md does:
- Resume from Phase 0 (Plan)

### Step 3: Determine Resume Point (v5.0 - 8 Phases)

Check existing files to find where to resume:

```
research/{slug}/
├── PLAN.md                              # Phase 0 output (requires approval)
├── SPEC.md                              # Input
├── STATE.json                           # Phase 1 complete
├── discovery/
│   ├── academic.md                      # Phase 2 progress
│   ├── practitioner.md                  # (optional)
│   ├── failure_analysis.md              # (required for >=standard)
│   ├── grey_literature.md               # (BLUEPRINT only)
│   └── snowball.md                      # Citation snowball expansion
├── SOURCES.md                           # Phase 3 complete
├── topics/
│   └── {unit}/
│       ├── findings.md                  # Phase 3-4 progress (12 fields)
│       └── findings_structured.json     # Structured extraction
├── synthesis/
│   └── risk_mitigations.md              # Phase 4 complete
├── claims.md                            # Phase 5 complete
├── synthesis/
│   ├── gaps.md                          # Gap declarations (if any)
│   ├── final_deliverable.md             # Phase 6 complete
│   └── critique.md                      # Phase 7 complete
└── logs/
    ├── checkpoint.md                    # Resume checkpoint
    ├── runlog.ndjson                    # Tool execution log
    ├── dedup_log.json                   # Deduplication decisions
    └── retraction_flags.json            # Retraction check results
```

### Step 4: Print Status

```
## Resuming: {slug}

**Current State:**
| Phase | Status |
|-------|--------|
| 0. Plan | Complete (approved) |
| 1. Parse | Complete |
| 2. Survey | Complete |
| 3. Deep Dive | Complete |
| 4. Failure | Partial |
| 5. Compile | Pending |
| 6. Specify | Pending |
| 7. Validate | Pending |

**Additional Files:**
| File | Status |
|------|--------|
| PLAN.md | Present (approved) |
| failure_analysis.md | Present |
| risk_mitigations.md | Missing |
| gaps.md | N/A (no LOW claims yet) |

**Resuming from:** Phase 4 - Failure Analysis
```

### Step 5: Resume Logic

#### No SPEC.md
```
ERROR: No SPEC.md found for "{slug}"
Create research/{slug}/SPEC.md first.
```
**Stop.**

#### SPEC.md only (no PLAN.md)
**Resume Phase 0: Plan**
1. Read SPEC.md
2. Create research plan
3. Write PLAN.md
4. Present plan to user for approval
5. **STOP** - wait for user approval

#### PLAN.md exists but not approved (STATE.json missing or plan_approved=false)
**Resume Phase 0: Plan Approval**
1. Present PLAN.md to user
2. Ask for approval
3. **STOP** - wait for user approval

#### PLAN.md approved, no STATE.json
**Resume Phase 1: Parse**
1. Parse SPEC.md
2. Auto-detect complexity
3. Detect recency policy from topic
4. Write STATE.json (v3.0 schema)
5. Continue to Phase 2

#### STATE.json exists, no discovery/*.md
**Resume Phase 2: Survey**
1. Read STATE.json for config
2. Spawn discovery agents based on preset:
   - Academic (always)
   - Practitioner (if needed)
   - Failure Analysis (required for >=standard)
   - Grey literature (if BLUEPRINT)
   - Snowball expansion (if >=standard)
3. Continue to Phase 3

#### discovery/*.md exists, no SOURCES.md
**Resume Phase 3: Deep Dive**
1. Read all discovery files
2. Run deduplication pipeline
3. Write `logs/dedup_log.json`
4. Run retraction check on DOIs
5. Write `logs/retraction_flags.json`
6. Resolve full-text access via Unpaywall
7. Detect implementation detail in sources
8. Filter and organize sources
9. Write SOURCES.md with impl detail flags
10. Extract findings to topics/*/findings.md
11. Continue to Phase 4

#### discovery complete, dedup_log.json missing
**Resume at Deduplication**
1. Read all discovery files
2. Run deduplication pipeline
3. Write `logs/dedup_log.json`
4. Continue with retraction check

#### SOURCES.md exists, retraction_flags.json missing
**Resume at Retraction Check**
1. Read SOURCES.md
2. Query Crossref for retraction status of all DOIs
3. Flag retracted papers
4. Write `logs/retraction_flags.json`
5. Continue to Phase 4

#### SOURCES.md + findings exist, no risk_mitigations.md
**Resume Phase 4: Failure**
1. Read discovery/failure_analysis.md
2. Extract failure studies
3. Compile risk-mitigation pairs
4. Write synthesis/risk_mitigations.md
5. Continue to Phase 5

#### risk_mitigations.md exists, no claims.md
**Resume Phase 5: Compile**
1. Read all findings files
2. Read risk_mitigations.md
3. Build claims registry
4. Calculate confidence with implementation detail check
5. Enforce gates:
   - Gate A: Depth (HIGH needs 2+ FULLTEXT Tier-1/2)
   - Gate B: Completion (HIGH or gaps declared)
   - Gate C: Retraction (no retracted in HIGH claims)
6. If LOW confidence recommendations: write gaps.md
7. Write claims.md
8. Continue to Phase 6

#### claims.md exists, no synthesis/final_deliverable.md
**Resume Phase 6: Specify**
1. Verify Completion Gate passed (or gaps declared)
2. Read SPEC.md for deliverable type (default: SPECIFICATION)
3. Read claims.md
4. Read risk_mitigations.md
5. Generate deliverable with method selections
6. Write synthesis/final_deliverable.md
7. Continue to Phase 7

#### synthesis/final_deliverable.md exists, no synthesis/critique.md
**Resume Phase 7: Validate**
1. Read deliverable
2. Assess quality including gate checks
3. Verify all gates passed
4. Write synthesis/critique.md
5. Update STATE.json to complete

#### All files exist
```
## Research Complete: {slug}

All 8 phases completed.

**Outputs:**
- PLAN.md - Approved research plan
- synthesis/final_deliverable.md - Implementation specification
- synthesis/risk_mitigations.md - Risk-mitigation pairs
- synthesis/critique.md - Quality assessment
- claims.md - Evidence registry

**Quality:**
- FULLTEXT coverage: X%
- Implementation detail: X sources
- Risk-mitigation pairs: N
- Gaps declared: N

**Key Recommendations:**
[3-5 bullets from deliverable]

**Confidence:** [From critique]
```
**Do not modify files.**

### Step 6: Continue Execution

After resuming, continue all subsequent phases until:
- All phases complete
- Error requires user input
- Plan approval required
- Rate limits pause execution
- Completion Gate fails (need to document gaps)

### Error Handling

**Plan not approved:** Present PLAN.md to user, wait for approval

**Missing sources:** Continue with available, flag in critique

**Partial extraction:** Check findings.md for completeness, resume from last unit

**Tool failures:** Try fallback, note in logs

**Retracted sources found:** Flag in retraction_flags.json, exclude from HIGH claims

**Completion Gate fail:** Write gaps.md before continuing to synthesis

### Checkpoint Writing

After each phase, write to `logs/checkpoint.md`:
```
## Checkpoint: {timestamp}
Phase: {N}/8
Status: {complete|partial}
Gate Checks:
  - Depth: {complete|pending}
  - Completion: {complete|pending}
  - Retraction: {complete|pending}
Notes: {any issues}
```

### Progress Indicators

Report progress as you work:
```
[Phase 0/8] Plan created, awaiting approval...
[Phase 1/8] Parsing SPEC...
[Phase 2/8] Running survey...
  - Academic: 15 results
  - Practitioner: 8 results
  - Failure Analysis: 5 failure studies
  - Snowball: 12 additional sources
[Phase 3/8] Deep dive...
  - Deduplication: 4 duplicates removed
  - Retraction check: 0 flagged
  - Full-text resolved: 18 FULLTEXT, 5 ABSTRACT_ONLY
  - Implementation detail: 12 sources
  - SOURCES.md: 23 sources
[Phase 4/8] Failure analysis...
  - Failure studies extracted: 5
  - Risk-mitigation pairs: 7
[Phase 5/8] Compiling claims...
  - HIGH confidence: 8
  - LOW confidence (with gaps): 2
  - Completion Gate: PASSED (gaps declared)
[Phase 6/8] Generating specification...
[Phase 7/8] Validating...
```

### Resume Decision Tree (v5.0)

```
PLAN.md exists?
├── No → Resume Phase 0: Plan
└── Yes → Plan approved (STATE.json.plan_approved)?
    ├── No → Resume Phase 0: Await Approval
    └── Yes → discovery complete?
        ├── No → Resume Phase 2: Survey
        └── Yes → dedup_log.json exists?
            ├── No → Resume at Deduplication
            └── Yes → SOURCES.md exists?
                ├── No → Resume Phase 3: Deep Dive (post-dedup)
                └── Yes → retraction_flags.json exists?
                    ├── No → Resume at Retraction Check
                    └── Yes → risk_mitigations.md exists?
                        ├── No → Resume Phase 4: Failure
                        └── Yes → claims.md exists?
                            ├── No → Resume Phase 5: Compile
                            └── Yes → final_deliverable.md exists?
                                ├── No → Resume Phase 6: Specify
                                └── Yes → critique.md exists?
                                    ├── No → Resume Phase 7: Validate
                                    └── Yes → COMPLETE
```
