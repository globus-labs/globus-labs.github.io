---
layout: project
title:  "Colmena"
image: "colmena.svg"
teaser: "Machine Learning-Based Steering of Ensemble Simulations"
featured: false
description: "Colmena is a Python library for building applications that combine AI and simulation workflows on HPC. Its core feature is a communication library that simplifies tools for intelligently steering large ensemble simulations."
github: "https://github.com/exalean/colmena"
website: "https://colmena.readthedocs.io"
---

The core concept of Colmena is a “thinker” application.
The Thinker application is responsible for intelligently responding to new data, such as by updating a machine learning model or selecting a new simulation with Bayesian optimization.

Colmena provides a few main components to enable building thinker applications:

- A “Task Server” that provides a simplified interface to HPC-ready workflow systems.
- A high-performance queuing system for interacting with method server(s) from thinking applications.
- An extensible base class for building thinking applications with a dataflow programming model.

Try it out at:
[https://colmena.readthedocs.io](https://colmena.readthedocs.io)

#### Publications

- Logan Ward, Ganesh Sivaraman, J. Gregory Pauloski, Yadu Babuji, Ryan Chard, Naveen Dandu, Paul C. Redfern, Rajeev S. Assary, Kyle Chard, Larry A. Curtiss, Rajeev Thakur, and Ian Foster. ["Colmena: Scalable machine-learning-based steering of ensemble simulations for high performance computing."](https://arxiv.org/abs/2110.02827) In IEEE/ACM Workshop on Machine Learning in High Performance Computing Environments. IEEE, 2021.
- Logan Ward, J. Gregory Pauloski, Valerie Hayot-Sasson, Ryan Chard, Yadu Babuji, Ganesh Sivaraman, Sutanay Choudhury, Kyle Chard, Rajeev Thakur, and Ian Foster. ["Cloud Services Enable Efficient AI-Guided Simulation Workflows across Heterogeneous Resources."](https://arxiv.org/abs/2303.08803) In Proceedings of Heterogeneity in Computing Workshop of the International Parallel and Distributed Processing Symposium. IEEE, 2023.
