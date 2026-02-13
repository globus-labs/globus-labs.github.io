---
layout: project
title:  "GLassBox"
teaser: "Interpretability Tools for Understanding ML models"
featured: false
image: "glassbox.png"
people: ["Jordan Pettyjohn", "Arham Khan", "Mansi Sakarvadia", "Aswathy Ajith", "Daniel Grzenda"]
description: "GLassBox is a suite of projects that facilitates a deeper understanding of complex AI models."
---

GLassBox is a collection of projects focusing on the interpretability and analysis of the behavior and internal mechanics of machine learning and AI models. It encompasses a suite of tools and analyses for making complex models more transparent, diagnosable, and scientifically grounded.

## Projects

### Mitigating Memorization In Language Models

Language models often unintentionally "memorize" data from their training set. During inference this data can be regurgitated verbatim via careful prompting. Training data memorization creates vulnerabilities in LLMs that can be exploited by so-called training data extraction attacks. These can enable attackers to extract sensitive data from language models. Additionally, memorization may reduce the generalization capacity of LLMs. We evaluate 17 strategies for mitigating memorization, including regularizer-based, fine-tuning-based, and machine-unlearning-based approaches. We find empirical evidence that unlearning methods, especially our proposed technique, BalancedSubnet, most effectively remove memorized information while preserving model performance.

<a href="https://mansisak.com/memorization/" class="btn btn-outline-secondary d-inline-flex align-items-center" target="_blank">Blog Post <i class="fas fa-pen-nib ms-2"></i></a>

**Further Reading:**
Mansi Sakarvadia, Aswathy Ajith, Arham Khan, Nathaniel Hudson, Caleb Geniesse, Kyle Chard, Yaoqing Yang, Ian Foster, and Michael W. Mahoney. "[Mitigating memorization in language models.](https://arxiv.org/abs/2410.02159)" arXiv preprint arXiv:2410.02159 (2024).

---

### Memory Injections: Correcting Multi-Hop Reasoning Failures during Inference in Transformer-Based Language Models

Transformer-based LLMs struggle with multi-hop reasoning due to their inability to recall intermediate facts that can "join" two claims together. The memory injections technique addresses this by inserting prompt-specific information into attention layers at inference time, significantly improving reasoning accuracy without retraining.

**Further Reading:**
Mansi Sakarvadia, Aswathy Ajith, Arham Khan, Daniel Grzenda, Nathaniel Hudson, André Bauer, Kyle Chard, and Ian Foster. "[Memory injections: Correcting multi-hop reasoning failures during inference in transformer-based language models.](https://arxiv.org/abs/2309.05605)" arXiv preprint arXiv:2309.05605 (2023).

---

### AttentionLens

Attention Lens is an interpretability tool that decodes the latent space of individual attention heads in LLMs. This offers a direct window for practitioners to inspect what LLMs are learning and retrieving during inference. By training head-specific transformations that map attention outputs to tokens in the vocabulary, we can identify the specialized role, such as knowledge retrieval or pattern matching, of each attention head. AttentionLens enables researchers to localize sources of bias, detect vulnerabilities to malicious prompts, and understand the mechanisms by which LLMs arrive at their predictions.

<a href="https://github.com/msakarvadia/AttentionLens" class="btn btn-outline-secondary d-inline-flex align-items-center" target="_blank">GitHub <i class="bi bi-github ms-2"></i></a>

**Further Reading:**
Mansi Sakarvadia, Arham Khan, Aswathy Ajith, Daniel Grzenda, Nathaniel Hudson, André Bauer, Kyle Chard, and Ian Foster. "[Attention lens: A tool for mechanistically interpreting the attention head information retrieval mechanism.](https://arxiv.org/abs/2310.16270)" arXiv preprint arXiv:2310.16270 (2023).

---

### Mind Your Manners: Detoxifying Language Models via Attention Head Intervention

Mind Your Manners extends AttentionLens to detect and mitigate toxicity in language models through targeted interventions on attention heads. We introduce DART (Degenerate Attention Response Tracking) to identify which attention heads upweight toxic tokens, and TOXIN (Toxicity Intervention) to surgically remove toxic latent tokens from attention heads. MYM enables interpretable, sparse, component-level detoxification while preserving overall model performance.

<a href="https://github.com/msakarvadia/AttentionLens" class="btn btn-outline-secondary d-inline-flex align-items-center" target="_blank">GitHub <i class="bi bi-github ms-2"></i></a>

**Further Reading:**
Jordan Nikolai Pettyjohn, Nathaniel C Hudson, Mansi Sakarvadia, Aswathy Ajith, Kyle Chard. "[Mind Your Manners: Detoxifying Language Models via Attention Head Intervention](https://openreview.net/pdf?id=UznBr4mxVr)"

---

### The False Promise of Zero-Shot Super-Resolution in Machine-Learned Operators 

Neural operators are powerful surrogates for solving complex partial differential equations. However, neural operators often struggle to model these systems at resolutions they weren't explicitly trained to represent. This inability to perform zero-shot super-resolution occurs because we fail to reliably extrapolate frequency information from Fourier space across resolution scales, leading to aliasing and degraded performance. A simple multi-resolution training strategy mitigates this issue, substantially improving cross-resolution generalization without changes to the model architecture.

<a href="https://mansisak.com/operator_aliasing/" class="btn btn-outline-secondary d-inline-flex align-items-center" target="_blank">Blog Post <i class="fas fa-pen-nib ms-2"></i></a>

**Further Reading:**
Mansi Sakarvadia, Kareem Hegazy, Amin Totounferoush, Kyle Chard, Yaoqing Yang, Ian Foster, and Michael W. Mahoney. "[The false promise of zero-shot super-resolution in machine-learned operators.](https://arxiv.org/abs/2510.06646)" arXiv preprint arXiv:2510.06646 (2025).

---

### Topology-Aware Knowledge Propagation in Decentralized Learning

Decentralized learning often fails to propagate rare information or features because standard gradient aggregation methods ignore the underlying network topology. In this work, we show that incorporating topology-aware weighting using graph features such as node connectivity and centrality improves knowledge diffusion and generalization in decentralized learning setups.

<a href="https://mansisak.com/topology_aware_learning/" class="btn btn-outline-secondary d-inline-flex align-items-center" target="_blank">Blog Post <i class="fas fa-pen-nib ms-2"></i></a>

**Further Reading:**
Mansi Sakarvadia, Nathaniel Hudson, Tian Li, Ian Foster, and Kyle Chard. "[Topology-Aware Knowledge Propagation in Decentralized Learning.](https://arxiv.org/abs/2505.11760)" arXiv preprint arXiv:2505.11760 (2025).

---


### LSHBloom: Memory-efficient, Extreme-scale Document Deduplication

Internet-scale pretraining datasets for LLMs are rife with exact or near-duplicate data points. These duplicate items make training more expensive, induce undesirable behaviors like memorization, and can limit model robustness. We develop an algorithm that is capable to deduplicating billions of documents using commodity hardware. 

<a href="/projects/lshbloom" class="btn btn-primary d-inline-flex align-items-center" role="button">Project Page <i class="fas fa-arrow-right ms-2"></i></a>

**Further Reading:**
Arham Khan, Robert Underwood, Carlo Siebenschuh, Yadu Babuji, Aswathy Ajith, Kyle Hippe, Ozan Gokdemir, Alexander Brace, Kyle Chard, Ian Foster. "[LSHBloom: Memory-efficient, Extreme-scale Document Deduplication.](https://arxiv.org/abs/2411.04257)" arXiv preprint arXiv:2411.04257 (2024).
