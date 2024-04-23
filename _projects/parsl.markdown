---
layout: project
title:  "Parsl"
image: "parsl-logo.png"
teaser: "Parallel programming library for Python"
featured: true
description: "Parsl is a parallel programming library for Python. It provides a model by which complex workflows can be represented in an intuitive Python-based control application. It facilitates transparent parallel execution of workflow components (apps) on any distributed or parallel computing system."
---

Parsl is a Python-based parallel programming library that supports development and execution of asynchronous and parallel data-oriented workflows (dataflows). These workflows glue together existing executables (called Apps) and Python functions with control logic written in Python. Parsl brings implicit parallel execution to standard Python scripts. Rather than explicitly defining a graph and/or modifying data structures, instead developers simply annotate Python functions and Apps. Parsl constructs a dynamic, parallel execution graph derived from the implicit linkage between Apps based on shared input/output data objects. Parsl then executes these components when dependencies are met. Parsl is resource-independent, that is, the same Parsl script can be executed on your laptop through to clusters, clouds, and supercomputers. Parsl also supports different executors including local threads, pilot jobs, and extreme-scale execution with Swift/T.

Parsl can be used to realize a variety of workflows:

- Parallel task-based workflows in which tasks are executed when their dependencies are met.
- Interactive and dynamic workflows in which the workflow is dynamically expanded during execution by users or the workflow itself.
- Procedural workflows in which serial execution of tasks are managed by Parsl.
- Workflows with many short duration tasks where no task-level fault tolerance is required
- Workflows with long running tasks with fault tolerance

Try it out at:
[https://parsl-project.org](https://parsl-project.org)

Further reading
- Yadu Babuji, Anna Woodard, Zhuozhao Li, Daniel S. Katz, Ben Clifford, Rohan Kumar, Luksaz Lacinski, Ryan Chard, Justin M. Wozniak, Ian Foster, Michael Wilde and Kyle Chard. "Parsl: Pervasive Parallel Programming in Python." 28th ACM International Symposium on High-Performance Parallel and Distributed Computing (HPDC). 2019. 10.1145/3307681.3325400
- Babuji, Yadu, Woodard, Anna, Li, Zhuozhao, Katz, Daniel S., Clifford, Ben, Foster, Ian, Wilde, Michael and Chard, Kyle. "Scalable Parallel Programming in Python with Parsl." Proceedings of the Practice and Experience in Advanced Research Computing on Rise of the Machines (Learning). pp 22:1--22:8. 2019.
- Yadu Babuji, Kyle Chard, Ian Foster, Daniel S. Katz, Michael Wilde, Anna Woodard and Justin Wozniak. "Parsl: Scalable Parallel Scripting in Python." 10th International Workshop on Science Gateways (IWSG). 2018.
- Babuji, Y., Brizius, A., Chard, K., Foster, I., Katz, D.S., Wilde, M., & Wozniak, J.. (2017, August 30). 
[Introducing Parsl: A Python Parallel Scripting Library](http://doi.org/10.5281/zenodo.853491). Zenodo. http://doi.org/10.5281/zenodo.853491.

Funding

- NSF 1550588
