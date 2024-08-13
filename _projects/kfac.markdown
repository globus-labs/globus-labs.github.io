---
layout: project
title: "KAISA: Scalable Second-Order Deep Neural Network Training"
image: "kfac.png"
people: ["Greg Pauloski", "Zhao Zhang", "Kyle Chard", "Ian Foster"]
hashtags: [
    "Machine Learning",
]
github: "https://github.com/gpauloski/kfac-pytorch"
website: 
teaser: "KAISA is a novel distributed framework for training large models with K-FAC at scale."
active: false
---

KAISA is a PyTorch preconditioner that enables efficient and scalable second-order optimization for deep neural networks.
Training with KAISA can reduce training time compared to conventional optimizers (e.g., SGD), and KAISA can adapt the memory footprint, communication, and computation given model and hardware characteristics to improve performance and increase scalability.

We have shown across a variety of computing hardware and scales that, compared to the original optimizers, KAISA converges 18.1–36.3% faster across applications with the same global batch size.
Under a fixed memory budget, KAISA converges 32.5% and 41.6% faster in ResNet-50 and BERT-Large, respectively.
KAISA can balance memory and communication to achieve scaling efficiency equal to or better than the baseline optimizers.

#### KAISA Features
- Compatible with PyTorch, DeepSpeed, and NVIDIA Apex distributed training.
- Data and model parallel training.
- K-FAC preconditioning for Linear and Conv2D layers.
- Supports mixed precision and gradient accumulation training.
- Only takes two lines of code to get started!

#### Publications
- J. G. Pauloski, L. Huang, W. Xu, K. Chard, I. T. Foster and Z. Zhang, "[Deep Neural Network Training With Distributed K-FAC](https://ieeexplore.ieee.org/abstract/document/9739867)," in IEEE Transactions on Parallel and Distributed Systems, vol. 33, no. 12, pp. 3616-3627, 1 Dec. 2022, doi: 10.1109/TPDS.2022.3161187.
- J. Gregory Pauloski, Qi Huang, Lei Huang, Shivaram Venkataraman, Kyle Chard, Ian Foster, and Zhao Zhang. 2021. [KAISA: An Adaptive Second-order Optimizer Framework for Deep Neural Networks](https://dl.acm.org/doi/10.1145/3458817.3476152). In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC '21). Association for Computing Machinery, New York, NY, USA, Article 13, 1–14.
- J. Gregory Pauloski, Zhao Zhang, Lei Huang, Weijia Xu, and Ian T. Foster. 2020. [Convolutional neural network training with distributed K-FAC](https://dl.acm.org/doi/10.5555/3433701.3433826). In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC ‘20). IEEE Press, Article 94, 1–14.

#### Funding and Acknowledgements
This work was supported in part by the U.S. Department of Energy, Office of Science, Advanced Scientific Computing Research, Contract DE-AC02-06CH11357; the Exascale Computing Project, Project 17-SC-20-SC; and NSF OAC-1931354,  OAC-1818253, OAC-2106661, and OAC-2107511.
