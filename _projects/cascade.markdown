---
layout: project
title:  "Cascade"
image: "cascade.png"
teaser: "Distributed on-the-fly learning for ML surrogates"
featured: false
description: "Cascade is a continual-learning tool for scientific simulations. 
It uses distributed agents to run scientific simulations with ML surrogates, detect when these surrogates are likely to be unreliable, 
generate new training data, fine-tune models, and rerun untrusted simulation segments with updated models"
---

Machine learning (ML) surrogates can accelerate scientific simulations by orders of magnitude by replacing expensive numerical subroutines with comparably cost-effective ML model evaluations, but concerns about their reliability remain active among scientists. 
Of particular concern is the possibility that a simulation will enter a state outside of the ML surrogate's training domain, leading to innacurate predictions. 
On-the-fly learning, wherein ML surrogates are continually monitored for accuracy and updated when inaccuracy is suspected, increases the reliability of ML-driven simulations. 
Recent work from our group, Proxima, uses control-theory to ensure that simulation error meets a user-defined bound. 
Cascade extends Proxima to a distributed setting to take full advantage of HPC resources.


Implementations of Proxima and cascade can be found here
[https://github.com/globus-labs/cascade](https://github.com/globus-labs/cascade)

Further reading on proxima
- Yuliana Zamora, Logan Ward, Ganesh Sivaraman, Ian Foster, Henry Hoffmann. ICS '21: Proceedings of the 35th ACM International Conference on Supercomputing
[https://doi.org/10.1145/3447818.34603](https://doi.org/10.1145/3447818.34603)
- Michael Tynes, Logan Ward, Kyle Chard, Ian Foster. Will It Blend? Mixing Numerical and Machine-Learned Physics Quantities for Accurate on-the-Fly Surrogate Modeling. ICCS 2025: 25th International Conference on Computational Science. [https://doi.org/10.1007/978-3-031-97632-2_19](https://doi.org/10.1007/978-3-031-97632-2_19)
