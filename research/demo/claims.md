# Claims Registry: demo

## Research Unit: RAG Architecture Fundamentals

### Claim 1: Modular architecture is essential for RAG systems
- **Confidence**: HIGH
- **Sources**: S1, S2, S3
- **Evidence**: All three sources emphasize modularity - RAG Stack for fusion/retrieval/orchestration (S1), Agentic RAG for agent patterns (S2), HM-RAG for plug-and-play retrieval modules (S3)

### Claim 2: Static single-pass RAG is insufficient for complex tasks
- **Confidence**: HIGH
- **Sources**: S2, S3
- **Evidence**: "Traditional RAG approaches employ static workflows and lack the adaptability required for multistep reasoning" (S2); HM-RAG shows 12.95% accuracy improvement with multi-agent approach (S3)

### Claim 3: Multi-agent patterns improve RAG performance
- **Confidence**: HIGH
- **Sources**: S2, S3
- **Evidence**: Four agentic patterns (reflection, planning, tool use, multiagent) enable dynamic workflow adaptation (S2); HM-RAG achieves SOTA with three-tier agent architecture (S3)

### Claim 4: RAG evolution follows: Static → Agentic → Hierarchical Multi-Agent
- **Confidence**: LOW
- **Sources**: S2
- **Evidence**: Survey identifies progression but single source; pattern is implied across literature

---

## Research Unit: Embedding and Retrieval Strategies

### Claim 5: Bottleneck pre-training improves dense retrieval representations
- **Confidence**: HIGH
- **Sources**: S6 (Tier 1)
- **Evidence**: "SimLM achieved performance exceeding multi-vector approaches like ColBERTv2 while incurring significantly lower storage costs" (ACL 2023)

### Claim 6: Manifold-aware distance metrics outperform Euclidean/cosine for OOD retrieval
- **Confidence**: LOW
- **Sources**: S7
- **Evidence**: "Up to 26% improvement on OOD passage retrieval" - single preprint, awaits replication

### Claim 7: LLM-based document expansion improves zero-shot retrieval
- **Confidence**: LOW
- **Sources**: S8
- **Evidence**: "Exhibits strong capabilities in zero-shot and out-of-domain retrieval" - single preprint, awaits replication

### Claim 8: Out-of-distribution robustness requires specialized techniques
- **Confidence**: LOW
- **Sources**: S7, S8
- **Evidence**: Both papers specifically target OOD scenarios; converging theme but limited replication

---

## Research Unit: Chunk Size and Context Window Optimization

### Claim 9: No universal optimal chunk size exists
- **Confidence**: HIGH
- **Sources**: S11, S12, S13
- **Evidence**: All three sources agree optimal settings depend on content type, model architecture, and use case

### Claim 10: Chunk overlap provides no measurable benefit
- **Confidence**: HIGH
- **Sources**: S12, S13
- **Evidence**: "Adding 10-20% overlap did not improve BERTScore or EM" (S12); fixed-size (non-overlapping) performs comparably or better (S13)

### Claim 11: Context window sweet spot is 500-2,500 tokens
- **Confidence**: HIGH
- **Sources**: S12
- **Evidence**: "BERTScore was stable between 0.5k-2.5k tokens and then declined by ~4-5% at 10k tokens" - context cliff phenomenon

### Claim 12: Small chunks (64-128 tokens) optimal for fact-based queries
- **Confidence**: HIGH
- **Sources**: S11
- **Evidence**: "SQuAD: 64-token chunks achieved 64.1% Recall@1; performance degrades 10-15% with larger chunks"

### Claim 13: Large chunks (512-1024 tokens) optimal for technical/dispersed content
- **Confidence**: HIGH
- **Sources**: S11
- **Evidence**: "TechQA: Recall@1 improved from 4.8% (64 tokens) to 71.5% (1024 tokens)"

### Claim 14: Semantic chunking not worth computational cost for natural documents
- **Confidence**: HIGH
- **Sources**: S12, S13
- **Evidence**: "Fixed-size chunking often performed better or comparably (90.59% vs 87.37%)" (S13); "Sentence and semantic methods performed comparably up to ~5K tokens" (S12)

---

## Confidence Summary

| Level | Count | Claims |
|-------|-------|--------|
| HIGH | 10 | 1, 2, 3, 5, 9, 10, 11, 12, 13, 14 |
| LOW | 4 | 4, 6, 7, 8 |
| CONTESTED | 0 | - |

---

## Contradictions

No major contradictions detected. Minor variations exist in optimal chunk size recommendations, but these are context-dependent rather than contradictory:
- S11: 64-128 for facts, 512-1024 for technical
- S12: 150-300 general default
- Both are reconciled by content-type dependency (Claim 9)
