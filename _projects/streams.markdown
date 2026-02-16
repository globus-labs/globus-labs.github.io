---

layout: project
title: "Streams"
image: "streams_logo.png"
people: ["Seena VazifeDunn", "Kyle Chard", "Ian Foster"]
hashtags: [
    "Scientific Data Streaming",
    "Memory-to-memory data streaming",
    "Secure data transfer", 
    "Real-time data processing",
    "High-performance networking",
]
github: 
website: 
teaser: "Secure, High-performance Memory-to-Memory Data Streaming"
active: true

---

Scientific data streaming enables the real-time transfer, processing, and analysis of high-throughput experimental data as they are generated. The streaming paradigm is crucial for data-intensive domains such as high-energy physics, climate modeling, and synchrotron-based imaging, where low-latency insight is essential to dynamically adjust experimental parameters and support adaptive data collection. Modern data streaming architectures enable continuous data transfer and in-transit processing across distributed systems, leveraging advanced networking, efficient serialization protocols, and memory-to-memory data transfer. To support this functionality, streaming systems must operate within isolated and secure environments, supporting robust authentication and access control across various institutions, and ensuring end-to-end data integrity under the principles of zero-trust architecture.

This project is motivated by the deployment and operational limitations of current frameworks in real scientific environments, such as lack of federated authentication, manual intervention, network policy modification, admin level access to independently administered facilities, etc. We addressed this limitations by focusing on the following goals:
 - Automated and managed orchestration: Eliminate manual proxy setup, certificate distribution, and system-level tuning through on-demand, programmatic orchestration of streaming components.
 - Federated security model: Enable secure cross-site streaming without requiring shared administrative control or prior trust relationships.
 - Scalability and flexibility: Support diverse deployment environments, including scientific instruments, edge devices, and HPC facilities with firewalls, without requiring custom modifications to each site.
 - Portability: Operate entirely in user space using standard tools, avoiding the need for kernel modules, root privileges, or site-specific system dependencies.
 - Usability: Abstract configuration complexity and provide a simple interface for launching and managing secure, high-performance data streams.
 - Practicality: Establish streaming channels with minimal overhead, ensuring efficient and cost-effective operation.


#### Publications
- S. VazifeDunn, F. Castro, R. Kettimuthu, K. Chard, I. Foster: [StreamHub: High-performance Managed SciStream as a Service](https://dl.acm.org/doi/pdf/10.1145/3731599.3767459). in Proceedings of the SC ’25 Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis, ser. SC Workshops ’25. New York, NY, USA: Association for Computing Machinery, 2025, p. 929–938.

#### Funding and Acknowledgements
This work is supported by the National Science Foundation and the US Department of Energy, including by the Office of Advanced Scientific Computing Research’s Diaspora project.
