# Findings: Zero-Shot and Few-Shot Prompting

## Source: A Survey on In-context Learning

- **Citation**: Dong, Q., Li, L., Dai, D., Zheng, C., Ma, J., Li, R., Xia, H., Xu, J., Wu, Z., Chang, B., Sun, X., Li, L., & Sui, Z. (2024). A Survey on In-context Learning. In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing* (pp. 1107-1128). Association for Computational Linguistics. DOI: 10.18653/v1/2024.emnlp-main.64

- **Type**: ACADEMIC

- **Tier**: 1

- **Extraction depth**: FULLTEXT

- **Source URL**: https://aclanthology.org/2024.emnlp-main.64/

- **Sections extracted**: Abstract, Introduction, Definition and Formulation, Model Training (Pretraining, Warmup), Prompt Designing (Demonstration Organization, Instruction Formatting, Scoring Function), Analysis (Influencing Factors, Learning Mechanism), Application, Challenges and Future Directions

- **Main claim**: In-context learning (ICL) is a paradigm that allows LLMs to learn tasks from a few demonstration examples without parameter updates, where the key idea is "learning from analogy" - models infer patterns from demonstrations to make predictions on new queries.

- **Key evidence**:
  - "In-context learning is a paradigm that allows language models to learn tasks given only a few examples in the form of demonstration." (Section 2, Definition)
  - "The key idea of in-context learning is to learn from analogy... ICL requires a few demonstration examples to form a prompt context. These examples are usually written in natural language templates." (Section 1, Introduction)
  - "Different from supervised learning, which requires a training stage that uses backward gradients to update model parameters, ICL does not perform parameter updates." (Section 1)
  - "The performance of ICL is sensitive to specific settings, including the prompt template, the selection and order of demonstration examples, and other factors." (Section 1)
  - On few-shot vs zero-shot: "Tuning the 137B LaMDA-PT on over 60 datasets verbalized via natural language instruction templates, FLAN improves the ability of LLMs to follow instructions, boosting both the zero-shot and few-shot ICL performance." (Section 3.2)
  - On demonstration selection: "A straightforward approach to selecting ICL examples is to choose the nearest neighbors of input instances based on their similarities." (Section 4.1.1)
  - On ordering effects: "Lu et al. (2022) have proven that order sensitivity is a common problem and always exists for various models." (Section 4.1.3)

- **Limitations**: The survey acknowledges that "many papers covered by this survey did not utilize the most up-to-date models while running experiments." The theoretical analysis sections focus primarily on simple tasks and small models, noting that "extending analysis on extensive tasks and large models may be the next step to be considered." The survey does not provide detailed empirical benchmarks comparing specific zero-shot vs few-shot performance gaps.

- **Relevance**: zero-shot-few-shot-prompting

- **Notes**: This comprehensive survey provides the foundational framework for understanding ICL as a prompting paradigm. Key distinctions are made between ICL and related concepts: (1) Prompt Learning - ICL is a subclass where demonstrations are part of the prompt; (2) Few-shot Learning - traditional few-shot learning requires parameter updates, while ICL does not. The survey identifies three key aspects of demonstration organization: selection (which examples to use), formatting (how to present them), and ordering (sequence arrangement). The paper also provides a taxonomy of training-time enhancements (pretraining, warmup/instruction tuning) that improve both zero-shot and few-shot ICL capabilities.

---

## Source: The Impact of Role Design in In-Context Learning for Large Language Models

- **Citation**: Rouzegar, H., & Makrehchi, M. (2025). The Impact of Role Design in In-Context Learning for Large Language Models. arXiv preprint arXiv:2509.23501. https://arxiv.org/abs/2509.23501

- **Type**: ACADEMIC

- **Tier**: 2

- **Extraction depth**: FULLTEXT

- **Source URL**: https://arxiv.org/abs/2509.23501

- **Sections extracted**: Abstract, Introduction, Related Works, Methodology and Experimental Setup, Prompt Designs, Experimental Setup, Results (General NLP Task Performance, Mathematical Reasoning Task Performance), Limitations and Future Works, Conclusion

- **Main claim**: Role-based prompt structuring (using system, user, and assistant role distinctions) significantly enhances LLM performance in both zero-shot and few-shot learning scenarios, with the FewSUA (Few-shot System, User, and Assistant) configuration generally achieving the best results across NLP tasks.

- **Key evidence**:
  - "In most cases, the few-shot system, user, and assistant prompt (FewSUA) configuration exhibited a superior F1 score across the experiments, indicating that incorporating clear role distinctions and examples significantly enhances model performance." (Section 5.1)
  - Performance data (Table 3): On commonsense_qa with GPT-3.5, FewSUA achieved 73% F1 vs 68% for ZeroU and ZeroSU. On ai2_arc with GPT-3.5, FewSUA achieved 85% F1 vs 76% for ZeroU.
  - "For Llama models, the use of few-shot user (FewU) and few-shot system and user (FewSU) commands led to a noticeable decrease in F1 scores. This suggests that embedding few-shot examples within user prompts may cause these models to produce more incorrect answers and hallucinations." (Section 5.1)
  - "A standout finding is that the FewSUA prompt configuration helped the Llama models generate outputs in the desired structure, making it potentially useful for applications like chatbots where maintaining a specific structure is crucial." (Section 5.1)
  - On math reasoning: "In mathematical reasoning, we found that configurations allowing for explanations often outperformed those strictly adhering to structural accuracy." (Conclusion)
  - "The success of the Reasoning-First approach in mathematical tasks indicates that encouraging models to articulate their thought processes can lead to more accurate outputs." (Conclusion)

- **Limitations**: The study focused on a limited range of tasks (sentiment analysis, text classification, QA, math reasoning) and specific model families (GPT-3.5, GPT-4o, Llama2-7b, Llama2-13b). The authors note they "were unable to experiment with larger Llama models" due to resource constraints. The study used pre-defined roles for instruction-tuned LLMs only and did not explore non-instruction-tuned models. Mathematical reasoning results were based on relatively small sample sizes.

- **Relevance**: zero-shot-few-shot-prompting

- **Notes**: This paper introduces a systematic framework for evaluating role-based prompt design with five configurations: ZeroU (zero-shot user-only), ZeroSU (zero-shot system+user), FewU (few-shot user-only), FewSU (few-shot system+user), and FewSUA (few-shot system+user+assistant). Key insight: the distinction between simply providing examples (few-shot) and structuring them with explicit role assignments can significantly impact performance. The study also introduces "Structural Accuracy" as a secondary metric measuring output format compliance. For complex reasoning tasks, the paper found that allowing models to explain reasoning before answering (Reasoning-First approach) improved accuracy, even at the cost of structural compliance - suggesting a trade-off between output formatting and task performance. Code available at: https://github.com/hrouzegar/Role_Based-In-Context-Learning
