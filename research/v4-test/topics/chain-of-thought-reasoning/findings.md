# Findings: Chain-of-Thought Reasoning

Extracted evidence from top sources on chain-of-thought reasoning mechanisms, approaches, and empirical findings.

---

## Source: Towards Reasoning Era: A Survey of Long Chain-of-Thought for Reasoning Large Language Models

- **Citation**: Chen, Q., Qin, L., Liu, J., Peng, D., Guan, J., Wang, P., Hu, M., Zhou, Y., Gao, T., & Che, W. (2025). Towards Reasoning Era: A Survey of Long Chain-of-Thought for Reasoning Large Language Models. arXiv preprint arXiv:2503.09567.

- **Type**: ACADEMIC

- **Tier**: 2

- **Extraction depth**: FULLTEXT

- **Source URL**: https://arxiv.org/abs/2503.09567

- **Sections extracted**: Abstract, Introduction, Long CoT Characteristics (Deep Reasoning, Extensive Exploration, Feasible Reflection), Empirical Phenomena, Evaluation Framework, Limitations, Future Directions

- **Main claim**: Long Chain-of-Thought (Long CoT) represents a fundamental paradigm shift in LLM reasoning, characterized by three key relaxations of traditional CoT constraints: deep reasoning (expanded logical node boundaries), extensive exploration (parallel investigation of multiple paths), and feasible reflection (ability to revisit and correct previous reasoning nodes).

- **Key evidence**:
  1. "Long CoT facilitates deeper reasoning across substantially more logical steps, incorporating reflective analysis and broader exploration of logical structures" compared to Short CoT which "employs shallow, linear reasoning with a limited number of logical nodes."

  2. On the overthinking phenomenon: "Performance initially improves with longer reasoning chains but subsequently declines beyond optimal thresholds... excessive exploration lengths beyond the RLLM's inherent reasoning boundary lead to performance decay."

  3. On test-time scaling: "For N samples, accuracy is proportional to m/(k/log N+b)^2, indicating fundamental limitations on parallel scaling effectiveness."

  4. On Long CoT emergence: "Modifying the decoding process or designing specific prompts can activate the Long CoT within pre-trained models." Models like Qwen exhibit verification, backtracking, and sub-target setting behaviors triggerable through rule-based reinforcement.

  5. On PRM vs ORM debate: "Reinforcement learning with outcome supervision is not statistically more challenging than process supervision, aside from polynomial factors."

- **Limitations**:
  - Survey paper synthesizing existing research rather than presenting new empirical results
  - Does not provide direct experimental comparisons between approaches
  - Limited coverage of multimodal reasoning contexts
  - Computational efficiency concerns with extended reasoning remain unresolved
  - Safety considerations for high-stakes applications need further investigation

- **Relevance**: chain-of-thought-reasoning

- **Notes**: Comprehensive survey covering 250+ references. Establishes taxonomical framework distinguishing Long CoT from traditional Short CoT. Identifies six critical phenomena: Long CoT emergence, reasoning boundaries, overthinking, test-time scaling, PRM vs ORM debate, and the "Aha moment." Key benchmarks identified include GSM8K, MATH, AIME for mathematics; Codeforces, SWEbench for coding; and BIG-Bench Hard for commonsense reasoning.

---

## Source: Chain-of-Thought Reasoning Without Prompting

- **Citation**: Wang, X., & Zhou, D. (2024). Chain-of-Thought Reasoning Without Prompting. In Advances in Neural Information Processing Systems 38 (NeurIPS 2024). arXiv preprint arXiv:2402.10200.

- **Type**: ACADEMIC

- **Tier**: 2

- **Extraction depth**: FULLTEXT

- **Source URL**: https://arxiv.org/abs/2402.10200

- **Sections extracted**: Abstract, Core Method (CoT-Decoding), Experimental Results, Confidence Mechanism, Discussion

- **Main claim**: Chain-of-thought reasoning capabilities are inherently present in pre-trained LLMs and can be elicited through modified decoding strategies (CoT-decoding) rather than explicit prompting, revealing that CoT reasoning paths exist among top-k alternative token sequences during generation.

- **Key evidence**:
  1. "CoT reasoning paths can be elicited from pre-trained LLMs by simply altering the decoding process" - the core finding that reasoning emerges from decoding rather than prompting.

  2. Benchmark performance: "On GSM8K, CoT-decoding consistently yields +10-30% absolute accuracy gains" over greedy decoding.

  3. Confidence correlation: "The presence of a CoT in the decoding path correlates with a higher confidence in the model's decoded answer, characterized by a significant probability disparity between the top and secondary tokens."

  4. Scale interaction: "On year parity, when using greedy decoding, the model's performance remains flat even after scaling up model sizes. In contrast, CoT-decoding significantly boosts the performance by recovering the CoT paths, achieving almost perfect accuracy at larger model scales."

  5. Why sampling fails: "CoT paths do not consistently outrank non-CoT ones in the model's probability assessment... The ineffectiveness of sampling stems from the model's strong tendency in providing a direct answer during decoding, hence the first token tends to have less diversity compared to CoT-decoding."

- **Limitations**:
  - Evaluated primarily on PaLM-2 model family; generalization to other architectures needs verification
  - Computational overhead of exploring top-k alternatives not fully characterized
  - Does not address whether CoT-decoding works for all reasoning task types
  - Confidence metric may not generalize across all problem domains

- **Relevance**: chain-of-thought-reasoning

- **Notes**: Published at NeurIPS 2024. Key insight is that reasoning capabilities are latent in models and don't require explicit prompting or additional training. The confidence-based selection mechanism provides a principled way to identify reasoning paths. This challenges the assumption that CoT requires careful prompt engineering and suggests inference-time strategies can unlock hidden capabilities. Implementations available in OptiLLM library.

---

## Cross-Source Analysis

### Convergent Findings

1. **Decoding modifications can elicit CoT**: Both papers support that CoT reasoning can emerge through inference-time interventions rather than training or prompting alone.

2. **Reasoning boundaries exist**: S13 documents the "overthinking phenomenon" while S14 shows that greedy decoding masks reasoning capabilities, suggesting models have inherent reasoning bounds affected by generation strategy.

3. **Model scale matters**: Both papers note interactions between model scale and CoT effectiveness, with larger models showing different reasoning emergence patterns.

### Complementary Insights

- S13 provides the theoretical taxonomy (Deep Reasoning, Exploration, Reflection) while S14 provides empirical evidence that reasoning paths exist in model weights.
- S13 covers training-time approaches (RL, SFT) while S14 focuses on inference-time solutions.
- S13 documents the "Aha moment" debate while S14 demonstrates that confidence metrics can identify reasoning paths.

### Key Takeaway for Research Unit

Chain-of-thought reasoning in LLMs operates through multiple mechanisms: it can be trained via imitation learning or reinforcement learning (S13), and it can also be surfaced through decoding modifications without additional training (S14). The presence of CoT correlates with answer confidence, and there are fundamental boundaries to reasoning depth beyond which performance degrades.
