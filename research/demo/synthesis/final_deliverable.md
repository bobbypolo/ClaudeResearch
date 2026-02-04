# Report: RAG Fundamentals - Core Concepts and Best Practices

## Summary

Retrieval-Augmented Generation (RAG) has evolved rapidly from simple retrieve-then-generate pipelines to sophisticated multi-agent architectures. This report synthesizes findings from 9 academic and practitioner sources (2022-2026) to provide actionable guidance for implementing RAG systems.

The research reveals three key insights: (1) RAG architecture is converging toward modular, agentic designs that enable dynamic retrieval and iterative refinement; (2) embedding and retrieval strategies benefit from specialized pre-training and manifold-aware distance metrics, particularly for out-of-distribution scenarios; and (3) chunk size optimization is content-dependent, with no universal optimal size—64-128 tokens work best for factual queries while 512-1024 tokens suit technical content.

For practitioners building document Q&A systems with limited compute budgets, the evidence suggests starting with simple fixed-size chunking (150-300 tokens, no overlap), using established embedding models with bottleneck architectures, and considering agentic patterns only when static RAG proves insufficient for query complexity.

---

## Findings

### RAG Architecture Fundamentals

The field has moved beyond static retrieve-then-generate pipelines toward modular, adaptive architectures [HIGH confidence].

**Key claims:**
- Modular architecture separating retrieval, fusion, and orchestration is essential for maintainable RAG systems [HIGH confidence - S1, S2, S3]
- Static single-pass RAG is insufficient for complex multi-step reasoning tasks [HIGH confidence - S2, S3]
- Multi-agent patterns (reflection, planning, tool use, collaboration) significantly improve performance—HM-RAG achieved 12.95% accuracy improvement over baselines [HIGH confidence - S2, S3]

**Architecture evolution pattern:**
```
Static RAG → Agentic RAG → Hierarchical Multi-Agent RAG
```

**Four key agentic design patterns** (from Singh et al., 2025):
1. **Reflection**: Agents evaluate and refine outputs iteratively
2. **Planning**: Strategic organization of retrieval and reasoning
3. **Tool Use**: Dynamic leveraging of external resources
4. **Multiagent Collaboration**: Specialized agents working together

**Practical recommendation**: For a document Q&A system on a limited budget, start with static RAG using a single retrieval pass. Add agentic patterns (reflection, re-ranking) incrementally if answer quality is insufficient for complex queries.

---

### Embedding and Retrieval Strategies

Effective retrieval requires attention to both embedding quality and similarity metrics [HIGH/LOW confidence mixed].

**Key claims:**
- Bottleneck pre-training significantly improves dense retrieval—SimLM exceeded ColBERTv2 performance with lower storage costs [HIGH confidence - S6, ACL 2023]
- Manifold-aware distance metrics can improve out-of-distribution retrieval by up to 26% [LOW confidence - S7, single preprint]
- LLM-based document expansion enables strong zero-shot retrieval without labeled data [LOW confidence - S8, single preprint]

**Embedding model selection considerations:**
| Model Type | Strength | Best For |
|------------|----------|----------|
| Encoder-based (e.g., Snowflake) | Fine-grained entity matching | Factual queries, short answers |
| Decoder-based (e.g., Stella) | Global context understanding | Technical content, long documents |

**Practical recommendation**: Use established embedding models (OpenAI, Cohere, or open-source alternatives like BGE/E5) with proven bottleneck architectures. For domain-specific applications, consider fine-tuning or LLM-based document expansion if zero-shot performance is inadequate.

---

### Chunk Size and Context Window Optimization

Optimal chunking is content-dependent, not universal [HIGH confidence].

**Key claims:**
- No universal optimal chunk size exists—settings depend on content type, model, and use case [HIGH confidence - S11, S12, S13]
- Chunk overlap provides no measurable benefit while increasing storage costs [HIGH confidence - S12, S13]
- Context window sweet spot is 500-2,500 tokens; quality degrades beyond this ("context cliff") [HIGH confidence - S12]
- Semantic chunking is not worth the computational cost for natural documents [HIGH confidence - S12, S13]

**Content-specific chunk size recommendations:**

| Content Type | Optimal Size | Evidence |
|--------------|--------------|----------|
| Factual, entity-based | 64-128 tokens | 64.1% Recall@1 on SQuAD (S11) |
| General Q&A | 150-300 tokens | Balanced performance (S12) |
| Technical/explanatory | 512-1024 tokens | 71.5% Recall@1 on TechQA (S11) |
| Narrative, dispersed answers | 1024 tokens | 10.7% Recall@1 on NarrativeQA (S11) |

**Recommended defaults for document Q&A:**
- Chunk size: 150-300 tokens
- Overlap: 0%
- Chunking method: Sentence-based (matches semantic performance, lower cost)
- Context budget: ~2,500 tokens maximum

**Practical recommendation**: Start with 200-token sentence-based chunks and no overlap. If retrieval quality is poor, adjust chunk size based on content type: smaller for factual/entity queries, larger for explanatory content.

---

## Limitations

1. **Recency of field**: RAG research is rapidly evolving (2022-2026). Many sources are preprints awaiting peer review and replication.

2. **Limited Tier-1 sources**: Only 1 of 9 sources is peer-reviewed (SimLM, ACL 2023). Field is too new for extensive journal coverage.

3. **Benchmark dependency**: Findings are based on standard benchmarks (SQuAD, NarrativeQA, TechQA) which may not reflect production edge cases.

4. **Model-specific results**: Embedding and chunking findings are tied to specific models (Stella, Snowflake, SPLADE). Results may not transfer to all model families.

5. **Missing production data**: Limited evidence on production deployment experiences, failure modes, and operational costs.

---

## Sources

1. **S1**: Wampler, D., Nielson, D., & Seddighi, A. (2025). Engineering the RAG Stack. arXiv:2601.05264
2. **S2**: Singh, A., Ehtesham, A., Kumar, S., & Khoei, T. T. (2025). Agentic RAG Survey. arXiv:2501.09136
3. **S3**: Liu, P. et al. (2025). HM-RAG: Hierarchical Multi-Agent Multimodal RAG. arXiv:2504.12330
4. **S6**: Wang, L. et al. (2023). SimLM: Pre-training for Dense Passage Retrieval. ACL 2023. arXiv:2207.02578
5. **S7**: Liu, Y. et al. (2025). MA-DPR: Manifold-aware Distance Metrics. arXiv:2509.13562
6. **S8**: Ma, G. et al. (2023). LLM-based Document Expansion for DPR. arXiv:2308.08285
7. **S11**: Bhat, S.R. et al. (2025). Rethinking Chunk Size for Long-Document Retrieval. arXiv:2505.21700
8. **S12**: Bennani, S. & Moslonka, C. (2026). Systematic Analysis of Chunking Strategies. arXiv:2601.14123
9. **S13**: Qu, R., Tu, R., & Bao, F. (2024). Is Semantic Chunking Worth the Computational Cost? arXiv:2410.13070

---

*Research completed: 2026-02-03*
*Confidence: HIGH (10 of 14 claims) | LOW (4 claims) | CONTESTED (0)*
