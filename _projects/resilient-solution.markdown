---

[comment]: # Do not change the layout
layout: Resilient Solutions

[comment]: # Project title
title: ""

[comment]: # The image should be added to images/projects/
image: "reslient-solutions.png"

[comment]: # List of project members.
people: ["Hai Nguyen", "Kyle Chard", "Ian Foster"]

[comment]: # List of project tags. Remove all that do not apply
hashtags: [
    "Machine Learning",
    "Cloud and Edge Computing",
    "HPC",
    "Stream Processing",
    "Real-time",
    "Fault Tolerance",
    "Checkpoint",
]

[comment]: # GitHub link or blank if not applicable
github: "https://github.com/diaspora-project/aps-mini-app/tree/resilient"

[comment]: # Website/homepage/docs or blank if not applicable
website: ""

[comment]: # One-line teaser/description for front page/project page
teaser: "Resilience Solutions for Large-scale Computing"

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

Modern scientific and data-intensive applications operate at unprecedented scale to meet rapidly growing data volumes and computational demands. At these scales, failures and performance variability are no longer rare events but normal operating conditions. This project develops resilience solutions for this new challenge, enabling applications to run reliably across failure- and anomaly-prone large-scale infrastructures--from supercomputers to geographically distributed streaming environments--as if operating in a failure-free environment. Our solutions include (i) a non-blocking, asynchronous checkpointing mechanism that minimizes recovery cost while introducing negligible overhead during failure-free execution, and (ii) an adaptive dynamic load-balancing strategy that mitigates performance anomalies and stragglers by continuously redistributing work based on observed processing capability and progress.
Our solutions reduce the impact of failures on large-scale tomographic reconstruction workflows by up to 500x and enable scientific streaming applications to meet real-time deadlines across a wide range of failure rates and performance anomalies.

#### Publications
- H.D. Nguyen, T. Bicer, B. Nicolae, R. Kettimuthu, E.A. Huerta, and I.T. Foster: [Resilient execution of distributed X-ray image analysis workflows](https://www.frontiersin.org/journals/high-performance-computing/articles/10.3389/fhpcp.2025.1550855/full). Frontiers in High Performance Computing 3 (2025)

#### Funding and Acknowledgements
This work is supported by the U.S. Department of Energy (DOE) under Contract No. DE-AC02-06CH11357, including funding from the Office of Advanced Scientific Computing Research (ASCR)'s Diaspora project and the Laboratory Directed Research.
