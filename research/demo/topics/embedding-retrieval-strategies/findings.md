# Embedding and Retrieval Strategies - Extracted Evidence

Research Unit: Embedding and retrieval strategies for RAG systems

---

## Source: SimLM: Pre-training with Representation Bottleneck for Dense Passage Retrieval

- **Citation**: Wang, L., Yang, N., Huang, X., Jiao, B., Yang, L., Jiang, D., Majumder, R., & Wei, F. (2023). SimLM: Pre-training with Representation Bottleneck for Dense Passage Retrieval. ACL 2023. arXiv:2207.02578
- **Type**: ACADEMIC
- **Tier**: 1 (ACL 2023 - top-tier NLP venue)
- **Main claim**: A bottleneck architecture with replaced language modeling pre-training objective significantly improves dense passage retrieval while maintaining computational efficiency.
- **Key evidence**: "SimLM achieved performance exceeding multi-vector approaches like ColBERTv2 while incurring significantly lower storage costs" (Experimental Results). The method uses "a replaced language modeling objective, inspired by ELECTRA, to improve sample efficiency and reduce the mismatch of input distribution between pre-training and fine-tuning."
- **Limitations**: Requires pre-training stage; evaluation primarily on standard benchmarks; may not address extreme domain shift scenarios.
- **Relevance**: Embedding and retrieval strategies - demonstrates effective pre-training approach for dense retrievers
- **Notes**: Key insight is that compressing passage information through a bottleneck architecture forces the model to learn better dense representations. Only requires unlabeled corpora for pre-training.

---

## Source: MA-DPR: Manifold-aware Distance Metrics for Dense Passage Retrieval

- **Citation**: Liu, Y., Wen, Q., Zhao, M., Liang, J., & Sanner, S. (2025). MA-DPR: Manifold-aware Distance Metrics for Dense Passage Retrieval. arXiv:2509.13562
- **Type**: ACADEMIC
- **Tier**: 2 (arXiv preprint)
- **Main claim**: Traditional Euclidean/cosine distance metrics underperform because embeddings occupy lower-dimensional non-linear manifolds; graph-based manifold-aware distances achieve up to 26% improvement on out-of-distribution retrieval.
- **Key evidence**: "Embeddings actually occupy lower-dimensional, non-linear manifolds, particularly in out-of-distribution scenarios where conventional distances underperform." The method achieves "up to 26% improvement on OOD passage retrieval" while maintaining comparable in-distribution performance. Manifold-aware metrics enable effective retrieval "even in the absence of direct semantic overlap" by exploiting neighborhood context.
- **Limitations**: Graph construction adds complexity; improvements most significant for OOD scenarios; may have higher memory requirements for large corpora.
- **Relevance**: Embedding and retrieval strategies - novel distance metric approach for improving retrieval robustness
- **Notes**: Uses shortest-path distances on nearest-neighbor graphs rather than direct vector distances. Query inference time increases only minimally. Generalizes across diverse embedding models.

---

## Source: Pre-training with Large Language Model-based Document Expansion for Dense Passage Retrieval

- **Citation**: Ma, G., Wu, X., Wang, P., Lin, Z., & Hu, S. (2023). Pre-training with Large Language Model-based Document Expansion for Dense Passage Retrieval. arXiv:2308.08285
- **Type**: ACADEMIC
- **Tier**: 2 (arXiv preprint)
- **Main claim**: LLM-based document expansion through query generation, combined with contrastive learning and curriculum learning, significantly improves dense retrieval performance especially for zero-shot and out-of-domain scenarios.
- **Key evidence**: The approach "significantly improves retrieval performance on large-scale web-search tasks" and "exhibits strong capabilities in zero-shot and out-of-domain retrieval, enabling practical deployment without requiring human-annotated training data initially." Uses curriculum learning to "progressively reduce reliance on expensive LLM computations."
- **Limitations**: Initial LLM inference cost for document expansion; curriculum learning adds training complexity; effectiveness may vary with LLM quality.
- **Relevance**: Embedding and retrieval strategies - demonstrates LLM augmentation for improving retrieval
- **Notes**: Combines three techniques: (1) LLM-based query generation for document expansion, (2) contrastive learning with bottlenecked query generation pre-training, (3) curriculum learning to reduce LLM dependency over time.

---

## Summary of Key Findings

### Embedding Optimization Techniques
1. **Bottleneck architectures** (SimLM): Force compression of passage information into dense vectors, improving representation quality
2. **Replaced language modeling** (SimLM): ELECTRA-style pre-training improves sample efficiency and reduces distribution mismatch

### Retrieval Approach Innovations
1. **Manifold-aware distances** (MA-DPR): Graph-based shortest-path metrics outperform Euclidean/cosine for OOD retrieval
2. **Document expansion** (LLM-based): Query generation augments documents to improve matching

### Cross-Cutting Themes
- **Out-of-distribution robustness**: Both MA-DPR and LLM-expansion specifically target OOD/zero-shot scenarios
- **Efficiency considerations**: SimLM achieves ColBERTv2-level performance with lower storage; curriculum learning reduces LLM costs
- **Pre-training importance**: All three papers emphasize specialized pre-training for retrieval tasks

### Confidence Assessment
- **HIGH**: Bottleneck pre-training improves dense retrieval (SimLM - peer-reviewed ACL 2023)
- **LOW**: Manifold-aware distances improve OOD retrieval (MA-DPR - single preprint, needs replication)
- **LOW**: LLM document expansion improves zero-shot retrieval (single preprint, needs replication)

---

*Extracted: 2026-02-03*
