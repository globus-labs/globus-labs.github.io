---

[comment]: # Do not change the layout
layout: project

[comment]: # Project title
title: "MPI-LLM"

[comment]: # The image should be added to images/projects/
image: "mpi-llm.png"

[comment]: # List of project members.
people: ["Shu Shi", "Wenyi Wang", "Yadu Nand Babuji", "Maxime Gonthier", "Kyle Chard", "Ian Foster"]

[comment]: # List of project tags. Remove all that do not apply
hashtags: [
    "Machine Learning Systems",
    "LLM Serving"
]

[comment]: # GitHub link or blank if not applicable
github: 

[comment]: # Website/homepage/docs or blank if not applicable
website:

[comment]: # One-line teaser/description for front page/project page
teaser: "An MPI-based multi-model serving system for HPC with fast model switching."

[comment]: # Set to false if the project is no longer maintained
active: true

---
MPI-LLM is an HPC-oriented serving system for Large Language Models that helps institutions run many LLMs on a limited GPU pool. Built on top of vLLM, it replaces the Ray backend with a Message Passing Interface (MPI) control plane and a master-side scheduler that manages long-lived GPU workers across multiple nodes. This design improves compatibility with HPC infrastructure and reduces the overheads of deployment and coordination. MPI-LLM supports hosting multiple models simultaneously and enables rapid model switching, allowing users to move between models with different GPU requirements without repeatedly tearing down and restarting jobs. Our implementation demonstrates lower startup and switching overheads on multi-node GPU clusters while preserving strong inference throughput for multi-model workloads.

MPI-LLM provides:

- MPI runtime integration: Provides an MPI-native runtime layer for coordination across nodes.

- Request-level scheduling: Schedules and routes requests to coordinate multi-model execution.

- GPU allocation policies: Dynamically assigns GPU resources to support efficient model switching on a shared pool.