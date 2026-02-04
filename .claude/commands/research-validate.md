---
name: research-validate
description: Validate research quality gates before synthesis
user_prompt: true
---

# /research-validate {slug}

Validate research quality gates before proceeding to synthesis phase. This command performs pre-synthesis checks to ensure evidence quality meets thresholds.

## Instructions

### Step 1: Validate Project Exists

Check if `research/{slug}/` exists.

If not:
- List available research projects in `research/`
- Report that the requested project does not exist
- **Stop.**

### Step 2: Read Required Files

Read the following files:
- `research/{slug}/STATE.json` - Configuration and targets
- `research/{slug}/SOURCES.md` - Source list with tier/type info
- `research/{slug}/topics/*/findings.md` - Extracted evidence
- `research/{slug}/logs/retraction_flags.json` - Retracted sources (if exists)
- `research/{slug}/logs/dedup_log.json` - Deduplication log (if exists)
- `research/{slug}/claims.md` - Claims registry (if exists)
- `research/{slug}/synthesis/gaps.md` - Gap declarations (if exists, for Completion Gate)

### Step 3: Run Quality Gate Checks

Perform these validation checks:

#### Check 1: FULLTEXT Coverage

Count sources by access level in findings files:
- **FULLTEXT**: Full text was accessed and extracted
- **ABSTRACT_ONLY**: Only abstract available
- **PAYWALLED**: Could not access content

Calculate coverage percentage:
```
FULLTEXT_COVERAGE = (FULLTEXT_COUNT / TOTAL_SOURCES) * 100
```

**PASS**: FULLTEXT coverage >= 50%
**WARN**: FULLTEXT coverage >= 30% but < 50%
**FAIL**: FULLTEXT coverage < 30%

#### Check 2: Tier Targets

Read tier_targets from STATE.json and compare to actual distribution in SOURCES.md:

| Tier | Target | Actual | Status |
|------|--------|--------|--------|
| Academic (T1) | {target}% | {actual}% | PASS/FAIL |
| Practitioner (T2) | {target}% | {actual}% | PASS/FAIL |
| Other (T3) | {target}% | {actual}% | PASS/FAIL |

**PASS**: All tiers within 15% of target
**WARN**: One tier off by 15-25%
**FAIL**: Any tier off by >25%

#### Check 3: Retraction Flags

If `logs/retraction_flags.json` exists, check for flagged sources:

```json
{
  "flagged": [
    {"doi": "10.xxx", "reason": "retracted", "source": "S3"}
  ]
}
```

**PASS**: No retracted sources
**WARN**: Sources with expressions of concern
**FAIL**: Retracted sources still in SOURCES.md

#### Check 4: HIGH Claim Validity

For each claim marked HIGH confidence in claims.md:
- Check supporting sources have access_level = FULLTEXT
- Check supporting sources are Tier 1 or Tier 2
- Require at least 2 FULLTEXT Tier-1/2 sources per HIGH claim

**PASS**: All HIGH claims meet requirements
**WARN**: 1-2 HIGH claims have only 1 FULLTEXT Tier-1/2 source
**FAIL**: Any HIGH claim has 0 FULLTEXT Tier-1/2 sources

#### Check 5: Deduplication Status

If `logs/dedup_log.json` exists, check for remaining duplicates:

```json
{
  "removed": [...],
  "potential_duplicates": [
    {"source1": "S1", "source2": "S5", "similarity": 0.85}
  ]
}
```

**PASS**: No potential duplicates with similarity > 0.9
**WARN**: 1-3 potential duplicates with similarity 0.85-0.9
**FAIL**: >3 potential duplicates OR any with similarity > 0.95

#### Check 6: Completion Gate (v5.0)

For each recommendation claim in claims.md:
- If confidence = HIGH: PASS (no gap needed)
- If confidence = LOW: Check if gap is declared in `synthesis/gaps.md`
- If confidence = LOW and no gap declared: FAIL

**PASS**: All recommendations have HIGH confidence OR declared gaps
**WARN**: All gaps declared but >30% of recommendations are LOW
**FAIL**: Any LOW confidence recommendation without gap declaration

### Step 4: Calculate Overall Assessment

| Result | Criteria |
|--------|----------|
| **PASS** | All checks PASS |
| **PASS WITH WARNINGS** | All checks PASS or WARN, no FAIL |
| **FAIL** | Any check FAIL |

### Step 5: Output Validation Report

```
## Validation Report: {slug}

### Overall Assessment: [PASS | PASS WITH WARNINGS | FAIL]

---

### Check 1: FULLTEXT Coverage
**Status**: [PASS | WARN | FAIL]
- FULLTEXT: N sources ({X}%)
- ABSTRACT_ONLY: N sources ({X}%)
- PAYWALLED: N sources ({X}%)
- Coverage: {X}% (threshold: 50%)

### Check 2: Tier Targets
**Status**: [PASS | WARN | FAIL]
| Tier | Target | Actual | Delta | Status |
|------|--------|--------|-------|--------|
| Academic (T1) | {X}% | {Y}% | {Z}% | [OK|WARN|FAIL] |
| Practitioner (T2) | {X}% | {Y}% | {Z}% | [OK|WARN|FAIL] |
| Other (T3) | {X}% | {Y}% | {Z}% | [OK|WARN|FAIL] |

### Check 3: Retraction Flags
**Status**: [PASS | WARN | FAIL]
- Retracted: N sources
- Expressions of concern: N sources
- Flagged sources: [list if any]

### Check 4: HIGH Claim Validity
**Status**: [PASS | WARN | FAIL]
| Claim | FULLTEXT T1/2 Sources | Required | Status |
|-------|------------------------|----------|--------|
| {claim1} | N | 2 | [OK|WARN|FAIL] |

### Check 5: Deduplication Status
**Status**: [PASS | WARN | FAIL]
- Duplicates removed: N
- Potential duplicates remaining: N
- Flagged pairs: [list if any]

### Check 6: Completion Gate (v5.0)
**Status**: [PASS | WARN | FAIL]
- HIGH confidence recommendations: N
- LOW confidence with gaps declared: N
- LOW confidence without gaps: N (must be 0 to pass)

---

### Recommendations

**If PASS:**
- Ready to proceed to synthesis phase
- Run `/research {slug}` to continue

**If PASS WITH WARNINGS:**
- Review warnings before proceeding
- Consider addressing issues for higher quality output
- Proceed with caution: `/research {slug}`

**If FAIL:**
- Must address failures before synthesis
- Retracted sources: Remove from SOURCES.md
- LOW coverage: Run additional extraction
- Invalid HIGH claims: Downgrade to LOW or find more sources
- Completion Gate failed: Declare gaps for LOW confidence recommendations in `synthesis/gaps.md`
- Run `/research-validate {slug}` again after fixes
```

### Step 6: Write Validation Log

Write results to `research/{slug}/logs/validation.json`:

```json
{
  "timestamp": "2024-01-01T12:00:00Z",
  "overall": "PASS|WARN|FAIL",
  "checks": {
    "fulltext_coverage": {
      "status": "PASS",
      "value": 65,
      "threshold": 50
    },
    "tier_targets": {
      "status": "PASS",
      "academic": {"target": 70, "actual": 68},
      "practitioner": {"target": 25, "actual": 27},
      "other": {"target": 5, "actual": 5}
    },
    "retraction_flags": {
      "status": "PASS",
      "retracted": 0,
      "concern": 0
    },
    "high_claim_validity": {
      "status": "PASS",
      "valid": 5,
      "invalid": 0
    },
    "deduplication": {
      "status": "PASS",
      "removed": 3,
      "potential": 0
    },
    "completion_gate": {
      "status": "PASS",
      "high_confidence": 5,
      "low_with_gaps": 2,
      "low_without_gaps": 0
    }
  }
}
```

---

## Error Handling

**Missing STATE.json**: Cannot validate without configuration. Run `/research {slug}` first to parse SPEC.

**Missing SOURCES.md**: Discovery/curation not complete. Run `/research-resume {slug}` to continue workflow.

**Missing findings files**: Extraction not complete. Cannot validate HIGH claims without evidence.

**Missing log files**: Create empty log files and note in report:
```
Note: retraction_flags.json not found - retraction check skipped
Note: dedup_log.json not found - deduplication check skipped
```

---

## Integration with Workflow

This command should be run:
1. After Phase 5 (Compile) completes
2. Before Phase 6 (Specify) begins
3. Optionally: manually at any point to check quality

If validation fails, the user should:
1. Address the failures
2. Re-run `/research-validate {slug}`
3. Only proceed to synthesis when PASS or PASS WITH WARNINGS
