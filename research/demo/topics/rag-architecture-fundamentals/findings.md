# RAG Architecture Fundamentals - Evidence Extraction

**Extraction Date:** 2026-02-03
**Research Unit:** RAG architecture fundamentals
**Sources Processed:** 3

---

## Source: Engineering the RAG Stack

- **Citation**: Wampler, D., Nielson, D., & Seddighi, A. (2025). Engineering the RAG Stack: A Comprehensive Review of the Architecture and Trust Frameworks for Retrieval-Augmented Generation Systems. arXiv:2601.05264
- **Type**: ACADEMIC
- **Tier**: 2
- **Main claim**: RAG provides a modular approach for integrating external knowledge without increasing model capacity, but research and engineering practices have been fragmented due to the diversity of RAG methodologies spanning fusion mechanisms, retrieval strategies, and orchestration approaches.
- **Key evidence**: "Research and engineering practices have been fragmented as a result of the increasing diversity of RAG methodologies, which encompasses a variety of fusion mechanisms, retrieval strategies, and orchestration approaches." (Abstract)
- **Limitations**: Comprehensive 86-page survey spanning 2018-2025; may be too broad for specific implementation guidance; focuses on taxonomy and assessment frameworks rather than benchmarks
- **Relevance**: RAG architecture fundamentals - provides unified taxonomy of RAG techniques
- **Notes**: Includes 37 tables synthesizing RAG approaches; addresses trust and alignment implications; covers both academic studies and industrial applications

### Key Architecture Claims

1. **Modular Architecture**: RAG enables external knowledge integration without expanding model parameters
2. **Taxonomy Consolidation**: Unifies diverse RAG techniques (fusion mechanisms, retrieval strategies, orchestration)
3. **Trust Frameworks**: Provides assessment frameworks for deploying secure, domain-adaptable RAG systems
4. **Historical Scope**: Synthesizes developments from 2018-2025 across academic and industrial contexts

---

## Source: Agentic Retrieval-Augmented Generation Survey

- **Citation**: Singh, A., Ehtesham, A., Kumar, S., & Khoei, T. T. (2025). Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG. arXiv:2501.09136
- **Type**: ACADEMIC
- **Tier**: 2
- **Main claim**: Traditional RAG employs static workflows lacking adaptability for multistep reasoning and complex task management; Agentic RAG addresses this through autonomous agents using reflection, planning, tool use, and multiagent collaboration patterns.
- **Key evidence**: "Traditional RAG approaches employ static workflows and lack the adaptability required for multistep reasoning and complex task management." Agentic RAG enables "dynamic management of retrieval strategies, iteratively refine contextual understanding, and adapt workflows to meet complex task requirements." (Abstract)
- **Limitations**: Survey paper - provides overview rather than implementation details; covers healthcare, finance, education but may not generalize to all domains
- **Relevance**: RAG architecture fundamentals - defines evolution from static to agentic RAG patterns
- **Notes**: Identifies four key agentic design patterns; documents frameworks and implementation tools

### Key Architecture Patterns (Agentic RAG)

1. **Reflection**: Agents evaluate and refine their outputs iteratively
2. **Planning**: Strategic organization of retrieval and reasoning tasks
3. **Tool Use**: Dynamic leveraging of external resources and APIs
4. **Multiagent Collaboration**: Coordinated problem-solving across specialized agents

### Core Capability Improvements

- Dynamic retrieval strategy management
- Iterative contextual understanding refinement
- Adaptive workflow modification for complex tasks

---

## Source: HM-RAG - Hierarchical Multi-Agent Multimodal RAG

- **Citation**: Liu, P., Liu, X., Yao, R., Liu, J., Meng, S., Wang, D., & Ma, J. (2025). HM-RAG: Hierarchical Multi-Agent Multimodal Retrieval Augmented Generation. arXiv:2504.12330
- **Type**: ACADEMIC
- **Tier**: 2
- **Main claim**: Single-agent RAG systems have limitations that can be addressed through hierarchical multi-agent architecture enabling collaborative intelligence for dynamic knowledge synthesis across structured, unstructured, and graph-based data sources.
- **Key evidence**: "Achieves 12.95% improvement in answer accuracy and a 3.56% boost in question classification accuracy compared to baseline systems on ScienceQA and CrisisMMD benchmarks." "Establishes state-of-the-art results in zero-shot settings on both datasets." (Results)
- **Limitations**: Benchmarked on ScienceQA and CrisisMMD only; multimodal focus may not apply to text-only use cases
- **Relevance**: RAG architecture fundamentals - concrete multi-agent RAG architecture with quantitative results
- **Notes**: Open source code available; modular design for adding new data modalities

### Three-Tier Agent Architecture

1. **Decomposition Agent**
   - Semantic-aware query rewriting
   - Schema-guided context augmentation
   - Breaks complex queries into manageable sub-queries

2. **Multi-source Retrieval Agents**
   - Parallel, modality-specific retrieval
   - Plug-and-play modules for different data sources:
     - Vector databases (unstructured)
     - Graph databases (structured relationships)
     - Web-based databases (live information)

3. **Decision Agent**
   - Consistency voting mechanism
   - Multi-source answer integration
   - Discrepancy resolution in retrieval results

### Performance Metrics

| Metric | Improvement |
|--------|-------------|
| Answer Accuracy | +12.95% |
| Question Classification | +3.56% |
| Setting | Zero-shot SOTA |

---

## Cross-Source Synthesis

### Converging Claims [HIGH Confidence - 3 sources agree]

1. **Modular Architecture is Essential**: All three sources emphasize modularity - RAG Stack for fusion/retrieval/orchestration, Agentic RAG for agent patterns, HM-RAG for plug-and-play retrieval modules

2. **Static RAG is Insufficient**: Both Agentic RAG and HM-RAG identify limitations of single-pass, static retrieval approaches

3. **Multi-Agent Patterns Improve Performance**: Agentic RAG and HM-RAG both advocate for multiple specialized agents over monolithic designs

### Architecture Evolution Pattern

```
Traditional RAG (Static)
    |
    v
Agentic RAG (Dynamic, Single-Agent)
    |
    v
Hierarchical Multi-Agent RAG (Specialized Agent Tiers)
```

### Key Design Principles Extracted

1. **Separation of Concerns**: Query processing, retrieval, and answer synthesis as distinct components
2. **Iterative Refinement**: Reflection and feedback loops for output quality
3. **Multi-Source Integration**: Combining vector, graph, and web retrieval
4. **Adaptive Orchestration**: Dynamic workflow management based on query complexity

---

## Evidence Quality Assessment

| Source | Tier | Recency | Methodology | Confidence |
|--------|------|---------|-------------|------------|
| RAG Stack Survey | 2 | 2025 | Literature review | HIGH |
| Agentic RAG Survey | 2 | 2025 | Literature review | HIGH |
| HM-RAG | 2 | 2025 | Empirical (benchmarks) | HIGH |

**Overall Confidence for RAG Architecture Claims: HIGH**
- 3 Tier-2 academic sources from 2025
- Converging findings on modularity and multi-agent patterns
- One source (HM-RAG) provides quantitative validation
