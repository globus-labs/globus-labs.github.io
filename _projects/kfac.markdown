---
layout: project
title:  "KAISA: a K-FAC-enabled, Adaptable, Improved, and ScAlable Second-Order Optimizer Framework"
image: "kfac.png"
teaser: "Deep Neural Network Training with Distributed K-FAC"
featured: false
description: "KAISA enables efficient and scalable second-order optimization for deep neural networks. Training with KAISA can reduce training time compared to conventional optimizers (e.g., SGD), and KAISA can adapt the memory footprint, communication, and computation given model and hardware characteristics to improve performance and increase scalability."
---

Kronecker-factored Approximate Curvature (K-FAC) has recently been shown to converge faster in deep neural network (DNN) training than stochastic gradient descent (SGD); however, K-FAC’s larger memory footprint hinders its applicability to large models.
We present **KAISA**, a **K**-FAC-enabled, **A**daptable, **I**mproved, and **S**c**A**lable second-order optimizer framework that adapts the memory footprint, communication, and computation given specific models and hardware to improve performance and increase scalability.
We quantify the tradeoffs between memory and communication cost and evaluate KAISA on large models, including ResNet-50, Mask R-CNN, U-Net, and BERT, on up to 128 NVIDIA A100 GPUs.
Compared to the original optimizers, KAISA converges 18.1–36.3% faster across applications with the same global batch size. 
Under a fixed memory budget, KAISA converges 32.5% and 41.6% faster in ResNet-50 and BERT-Large, respectively.
KAISA can balance memory and communication to achieve scaling efficiency equal to or better than the baseline optimizers.

Try it out on [GitHub](https://github.com/gpauloski/kfac_pytorch).

Publications:
- J. G. Pauloski, L. Huang, W. Xu, K. Chard, I. T. Foster and Z. Zhang, "[Deep Neural Network Training With Distributed K-FAC](https://ieeexplore.ieee.org/abstract/document/9739867)," in IEEE Transactions on Parallel and Distributed Systems, vol. 33, no. 12, pp. 3616-3627, 1 Dec. 2022, doi: 10.1109/TPDS.2022.3161187.
- J. Gregory Pauloski, Qi Huang, Lei Huang, Shivaram Venkataraman, Kyle Chard, Ian Foster, and Zhao Zhang. 2021. [KAISA: An Adaptive Second-order Optimizer Framework for Deep Neural Networks](https://dl.acm.org/doi/10.1145/3458817.3476152). In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC '21). Association for Computing Machinery, New York, NY, USA, Article 13, 1–14.
- J. Gregory Pauloski, Zhao Zhang, Lei Huang, Weijia Xu, and Ian T. Foster. 2020. [Convolutional neural network training with distributed K-FAC](https://dl.acm.org/doi/10.5555/3433701.3433826). In Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC ‘20). IEEE Press, Article 94, 1–14.
