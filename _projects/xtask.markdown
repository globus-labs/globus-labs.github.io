---

[comment]: # Do not change the layout
layout: project

[comment]: # Project title
title: "XTask"

[comment]: # The image should be added to images/projects/
image: "xtask.png"

[comment]: # List of project members.
people: ["Wenyi Wang", "Ioan Raicu", "Ian Foster", "Kyle Chard"]

# [comment]: # List of project tags. Remove all that do not apply
# hashtags: [
#   "Parallel Computing",
#   "High-performance Runtime",
#   "OpenMP"
# ]

# [comment]: # GitHub link or blank if not applicable
# github: "TODO"

# [comment]: # Website/homepage/docs or blank if not applicable
# website: "TODO"

[comment]: # One-line teaser/description for front page/project page
teaser: "Optimizing Fine-Grained Parallelism on OpenMP with NUMA awareness."

[comment]: # Set to false if the project is no longer maintained
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

An example first paragraph:

 1. Sentence giving overall context, hinting at the problem we solve.
      "Most humans don't like to read long paragraphs and writing short
      ones takes thought."
 2. An explanation of how we fix it.
      "We made a simple template that you can follow for how to write one."
 3. A statement of impact.
      "Any Globus Labs member need only edit this template to make their
      science more accessible."
-->

<!-- TODO: add your project description here. -->
High synchronization overhead in frameworks like GNU OpenMP impedes fine-grained task parallelism on many-core architectures. We introduce three advances to GNU OpenMP: a lock-less concurrent queue (XQueue), a scalable distributed tree barrier, and two NUMA-aware, lock-less load-balancing strategies.

Evaluated with Barcelona OpenMP Task Suite (BOTS) benchmarks, our XQueue and tree barrier improve performance by up to 1522.8× over the original GNU OpenMP. The load-balancing strategies provide an additional performance improvement of up to 4×.

#### Publications
<!-- List the full citations for each paper here with links to where to find it. -->

- W. Wang, M. Gonthier, H. Lai, P. Nookala, H. Pan, I. Foster, I. Raicu, K. Chard: [Exploring Fine-Grained Parallelism in Data-flow Runtime Systems on Many-Core Systems](https://sc25.supercomputing.org/proceedings/posters/poster_pages/post147.html). Proceedings of the SC '25 Research Posters of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC Posters'25)
- W. Wang, M. Gonthier, P. Nookala, H. Pan, I. Foster, I. Raicu, K. Chard: [Optimizing Fine-Grained Parallelism Through Dynamic Load Balancing on Multi-Socket Many-Core Systems](https://doi.ieeecomputersociety.org/10.1109/IPDPS64566.2025.00016). 2025 IEEE International Parallel and Distributed Processing Symposium (IPDPS25)

<!-- #### Funding and Acknowledgements -->
<!-- List any funding sources or other acknowledgements here otherwise remove -->
