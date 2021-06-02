---
layout: project
title:  "Data and Learning Hub for Science (DLHub)"
image: "dlhub.png"
featured: false
teaser: "A simple way to find, share, publish, and run machine learning models and discover training data for science"
description: "A simple way to find, share, publish, and run machine learning models and discover training data for science"
---

While the Machine Learning (ML) landscape is evolving rapidly, there has been a relative lag in the development of the "learning systems" needed to enable broad adoption. Furthermore, few such systems are designed to support the specialized requirements of scientific ML. Here we present the Data and Learning Hub for science (DLHub), a multi-tenant system that provides both model repository and serving capabilities with a focus on science applications. DLHub addresses two significant shortcomings in current systems. First, its selfservice model repository allows users to share, publish, verify, reproduce, and reuse models, and addresses concerns related to model reproducibility by packaging and distributing models and all constituent components. Second, it implements scalable and low-latency serving capabilities that can leverage parallel and distributed computing resources to democratize access to published models through a simple web interface. Unlike other model serving frameworks, DLHub can store and serve any Python 3-compatible model or processing function, plus multiple-function pipelines. We show that relative to other model serving systems including TensorFlow Serving, SageMaker, and Clipper, DLHub provides greater capabilities, comparable performance without memoization and batching, and significantly better performance when the latter two techniques can be employed. We also describe early uses of DLHub for scientific applications.

Publications

- Li, Zhuozhao, Ryan Chard, Logan Ward, Kyle Chard, Tyler J. Skluzacek, Yadu Babuji, Anna Woodard et al. ["DLHub: Simplifying publication, discovery, and use of machine learning models in science."](../pubs/Li-DLHub-JPDC-2021.pdf) Journal of Parallel and Distributed Computing 147 (2021): 64-76

- Chard, Ryan, Zhuozhao Li, Kyle Chard, Logan Ward, Yadu Babuji, Anna Woodard, Steven Tuecke, Ben Blaiszik, Michael J. Franklin, and Ian Foster. ["DLHub: Model and data serving for science."](../pubs/Chard_DLHub_2019.pdf) In 2019 IEEE International Parallel and Distributed Processing Symposium (IPDPS), pp. 283-292. IEEE, 2019.

Other Links

- [Data and Learning Hub for Science (DLHub)](https://www.dlhub.org)

Support

This material is based upon work supported by Laboratory Directed Research and Development (LDRD) funding from Argonne National Laboratory, provided by the Director, Office of Science, of the U.S. Department of Energy under Contract No. DE-AC02-06CH11357.
