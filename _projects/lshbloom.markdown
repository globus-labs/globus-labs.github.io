---
layout: project

title: "LSHBloom: Memory-efficient, Extreme-scale Document Deduplication"

image: "lshbloom.png"

people: ["Arham Khan", "Robert Underwood", "Carlo Siebenschuh", "Yadu Babuji", "Aswathy Ajith", "Kyle Hippe", "Ozan Gokdemir", "Alexander Brace", "Kyle Chard", "Ian Foster"]

hashtags: [
    "Deduplication",
    "LLM",
    "Big Data",
    "Machine Learning"
]

github: "https://github.com/ekzhu/datasketch"

teaser: "Memory-efficient, extreme-scale document deduplication using Bloom filters"

active: true

---

<!--
Add your project description below according to these guidelines.

 - Use Markdown syntax everywhere, not HTML!
 - Use active voice ("we")
 - Limit the intro paragraph to 3 sentences or less.
 - Keep the overall length under 3 paragraphs.
 - Bullet points are helpful for quickly understanding key points.
 - Add figures and additional links if relevant.
-->

Deduplicating training datasets is a critical step in training Large Language Models (LLMs). Duplicate documents in training data can degrade model performance and lead to memorization. However, deduplication at the scale of modern datasets (billions of documents) is computationally expensive and memory-intensive.

We introduce LSHBloom, a novel approach that extends MinHashLSH by replacing the traditional LSH index with a memory-efficient Bloom filter index. This approach significantly reduces memory usage and enhances throughput while maintaining high deduplication accuracy.

Our experiments show that LSHBloom achieves a 12x speedup and reduces disk space usage by 18x compared to MinHash LSH, making it feasible to deduplicate extreme-scale datasets on commodity hardware.

#### Publications
<!-- List the full citations for each paper here with links to where to find it. -->
- Arham Khan, Robert Underwood, Carlo Siebenschuh, Yadu Babuji, Aswathy Ajith, Kyle Hippe, Ozan Gokdemir, Alexander Brace, Kyle Chard, Ian Foster. "[LSHBloom: Memory-efficient, Extreme-scale Document Deduplication.](https://arxiv.org/abs/2411.04257)" arXiv preprint arXiv:2411.04257 (2024).

#### Funding and Acknowledgements
This research used resources of the Argonne Leadership
Computing Facility, a U.S. Department of Energy (DOE)
Office of Science user facility at Argonne National Laboratory (ANL) and is based on research supported by the
DOE Office of Science–Advanced Scientific Computing
Research Program and by Laboratory Directed Research
and Development (LDRD) funding from ANL, provided by
the Director, DOE Office of Science, both under Contract
No. DE-AC02-06CH11357.
