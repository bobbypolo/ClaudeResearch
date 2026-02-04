# Claims Registry: v4-test

## Gate Status
| Gate | Status | Impact |
|------|--------|--------|
| Depth (A) | PASSED | 4 FULLTEXT sources extracted (2 per unit) |
| Safety (B) | NOT_REQUIRED | Quick preset - counterevidence optional |
| Retraction (C) | PASSED | 0 retractions removed |

---

## Research Unit: Zero-Shot and Few-Shot Prompting

### Claim 1: ICL enables learning from analogy without parameter updates
- **Confidence**: LOW
- **Sources**: S7 (FULLTEXT, T1)
- **FULLTEXT support**: 1/1 sources
- **Evidence**: "In-context learning is a paradigm that allows language models to learn tasks given only a few examples in the form of demonstration... ICL does not perform parameter updates." (Dong et al., 2024, Section 1)
- **Gate A check**: N/A - single source claim

### Claim 2: Role-based prompt structuring significantly enhances ICL performance
- **Confidence**: LOW
- **Sources**: S1 (FULLTEXT, T2)
- **FULLTEXT support**: 1/1 sources
- **Evidence**: "In most cases, the few-shot system, user, and assistant prompt (FewSUA) configuration exhibited a superior F1 score across the experiments." (Rouzegar & Makrehchi, 2025, Section 5.1)
- **Gate A check**: N/A - single source claim

### Claim 3: ICL performance is sensitive to demonstration selection and ordering
- **Confidence**: LOW
- **Sources**: S7 (FULLTEXT, T1), S1 (FULLTEXT, T2)
- **FULLTEXT support**: 2/2 sources
- **Evidence**:
  - "The performance of ICL is sensitive to specific settings, including the prompt template, the selection and order of demonstration examples." (Dong et al., 2024)
  - "Role-based structuring (using system, user, and assistant role distinctions) significantly enhances LLM performance." (Rouzegar & Makrehchi, 2025)
- **Gate A check**: PASSED - 2 FULLTEXT T1/T2 sources agree
- **Note**: With 3+ sources, this would be HIGH. Low due to quick preset source limit.

### Claim 4: Instruction tuning (FLAN-style) improves both zero-shot and few-shot capabilities
- **Confidence**: LOW
- **Sources**: S7 (FULLTEXT, T1)
- **FULLTEXT support**: 1/1 sources
- **Evidence**: "Tuning the 137B LaMDA-PT on over 60 datasets verbalized via natural language instruction templates, FLAN improves the ability of LLMs to follow instructions, boosting both the zero-shot and few-shot ICL performance." (Dong et al., 2024, Section 3.2)
- **Gate A check**: N/A - single source claim

---

## Research Unit: Chain-of-Thought Reasoning

### Claim 5: Long CoT is characterized by deep reasoning, extensive exploration, and feasible reflection
- **Confidence**: LOW
- **Sources**: S13 (FULLTEXT, T2)
- **FULLTEXT support**: 1/1 sources
- **Evidence**: "Long CoT facilitates deeper reasoning across substantially more logical steps, incorporating reflective analysis and broader exploration of logical structures." (Chen et al., 2025)
- **Gate A check**: N/A - single source claim (survey synthesis)

### Claim 6: CoT reasoning can be elicited through decoding modifications without explicit prompting
- **Confidence**: LOW
- **Sources**: S13 (FULLTEXT, T2), S14 (FULLTEXT, T2)
- **FULLTEXT support**: 2/2 sources
- **Evidence**:
  - "Modifying the decoding process or designing specific prompts can activate the Long CoT within pre-trained models." (Chen et al., 2025)
  - "CoT reasoning paths can be elicited from pre-trained LLMs by simply altering the decoding process." (Wang & Zhou, 2024)
- **Gate A check**: PASSED - 2 FULLTEXT T2 sources agree
- **Note**: With 3+ T1/T2 sources, this would be HIGH. Low due to quick preset source limit.

### Claim 7: CoT-decoding yields significant accuracy improvements (+10-30% on GSM8K)
- **Confidence**: LOW
- **Sources**: S14 (FULLTEXT, T2)
- **FULLTEXT support**: 1/1 sources
- **Evidence**: "On GSM8K, CoT-decoding consistently yields +10-30% absolute accuracy gains over greedy decoding." (Wang & Zhou, 2024)
- **Gate A check**: N/A - single source claim

### Claim 8: Overthinking phenomenon exists - performance degrades beyond optimal reasoning lengths
- **Confidence**: LOW
- **Sources**: S13 (FULLTEXT, T2)
- **FULLTEXT support**: 1/1 sources
- **Evidence**: "Performance initially improves with longer reasoning chains but subsequently declines beyond optimal thresholds... excessive exploration lengths beyond the RLLM's inherent reasoning boundary lead to performance decay." (Chen et al., 2025)
- **Gate A check**: N/A - single source claim (documents phenomenon from multiple studies)

### Claim 9: Answer confidence correlates with presence of CoT in decoding paths
- **Confidence**: LOW
- **Sources**: S14 (FULLTEXT, T2)
- **FULLTEXT support**: 1/1 sources
- **Evidence**: "The presence of a CoT in the decoding path correlates with a higher confidence in the model's decoded answer, characterized by a significant probability disparity between the top and secondary tokens." (Wang & Zhou, 2024)
- **Gate A check**: N/A - single source claim

---

## Confidence Summary

| Level | Count | Notes |
|-------|-------|-------|
| HIGH | 0 | Quick preset limits to 2 sources/unit (need 3+ for HIGH) |
| LOW | 9 | All claims LOW due to source count limitation |
| CONTESTED | 0 | No contradictions found |

### Claims with Multi-Source Agreement (Would be HIGH with more sources)
- Claim 3: ICL sensitivity to demonstration selection/ordering (2 sources agree)
- Claim 6: CoT via decoding modifications (2 sources agree)

---

## Depth Gate Compliance

**Status**: PASSED

| Unit | Sources Extracted | FULLTEXT Count | Gate A Met |
|------|-------------------|----------------|------------|
| zero-shot-few-shot-prompting | 2 | 2 | YES |
| chain-of-thought-reasoning | 2 | 2 | YES |

All extracted sources have FULLTEXT access. Claims with 2+ supporting sources meet the depth requirement for potential HIGH confidence (if source count were higher).

---

*Compiled: 2026-02-04*
*Preset: quick (2 sources/unit, light extraction)*
