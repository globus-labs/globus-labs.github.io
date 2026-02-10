---

[comment]: # Do not change the layout
layout: project

[comment]: # Project title
title: "Octopus Event Fabric"

[comment]: # The image should be added to images/projects/
image: "octopus.svg"

[comment]: # List of project members.
people: ["Haochen Pan","Ryan Chard", "Alok Kamatar", "Rafael Vescovi", "Valerie Hayot-Sasson", "Andre Bauer", "Maxime Gonthier", "Kyle Chard", "Ian Foster"]

[comment]: # List of project tags. Remove all that do not apply
hashtags: [
    "Distributed Systems",
    "Cloud and Edge Computing",
]

[comment]: # GitHub link or blank if not applicable
github: "https://haochenpan.github.io/diaspora-service/main/"

[comment]: # Website/homepage/docs or blank if not applicable
website: "https://diaspora-project.github.io/"

[comment]: # One-line teaser/description for front page/project page
teaser: "Cloud-to-edge event fabric that handles millions of events securely at scale."

[comment]: # Set to false if the project is no longer maintained
active: true

---

Modern science relies on a distributed research infrastructure that generates large volumes of events. As applications span sites, scientists need to consume and act on events from many sources. We introduce **Octopus**, a hybrid cloud-edge event fabric designed for scalable, flexible scientific event-driven architecture (EDA). Benchmarks and real-world studies show Octopus meets the demands of scientific applications for throughput, latency, and resilience. Our experience suggests EDA maps naturally to scientific workflows.

- **Global reach**: A cloud-hosted Amazon MSK (Kafka) cluster accessible from edge and HPC sites.
- **Secure access**: Per-topic authentication and authorization via Globus Auth and AWS IAM.
- **Managed triggers**: Users can deploy filterable, auto-scaling Lambda functions to invoke arbitrary web services on matching events.
- **Scalable and resilient**:  Brokers, web services, and triggers scale independently; supports at-least-once delivery, producer acks, and consumer commits.

Together with [**Mofka**](https://www.frontiersin.org/journals/high-performance-computing/articles/10.3389/fhpcp.2025.1638203/full), which provides high-throughput data and metadata exchange within HPC environments, cloud-hosted Octopus forms a high-performance, hierarchical event bus that bridges HPC systems, edge resources, and cloud services. In [WRATH](https://doi.org/10.1109/CCGRID64434.2025.00058), Octopus serves as a cross-facility streaming fabric for  task metrics, heartbeats, and failure logs from task-based parallel programming frameworks (e.g., Parsl), enabling real-time failure categorization and informed termination or hierarchical retry actions. In Icicle (to be released), Octopus, combined with Apache Flink, provides an event-driven substrate for ingesting, transporting, and processing high-volume file system metadata events, supporting scalable real-time monitoring and continuous metadata index maintenance across HPC file systems.

#### Publications
- Pan, Haochen, Ryan Chard, Sicheng Zhou, Alok Kamatar, Rafael Vescovi, Valérie Hayot-Sasson, André Bauer, Maxime Gonthier, Kyle Chard, and Ian Foster. [Octopus: Experiences with a hybrid event-driven architecture for distributed scientific computing.](https://arxiv.org/abs/2407.11432) In SC24-W: Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis, pp. 496-507. IEEE, 2024.
- Zhou, Sicheng, Zhuozhao Li, Valérie Hayot-Sasson, Haochen Pan, Maxime Gonthier, J. Gregory Pauloski, Ryan Chard, Kyle Chard, and Ian Foster. [Wrath: Workload Resilience Across Task Hierarchies in Task-Based Parallel Programming Frameworks](https://doi.org/10.1109/CCGRID64434.2025.00058). In 2025 IEEE 25th International Symposium on Cluster, Cloud and Internet Computing (CCGrid), pp. 1–11. IEEE, 2025.
- Pan, Haochen, Ryan Chard, Reid Mello, Christopher Grams, Tanjin He, Alexander Brace, Owen Price Skelly, Will Engler, Hayden Holbrook, Song Young Oh, Maxime Gonthier, Michael Papka, Ben Blaiszik, Kyle Chard, and Ian Foster. [Experiences with Model Context Protocol Servers for Science and High Performance Computing.](https://arxiv.org/abs/2508.18489) arXiv preprint arXiv:2508.18489, 2025.

#### Funding and Acknowledgements
We thank the entire team of the Diaspora Project for their
helpful comments and feedback. This material is based upon
work supported by the U.S. Department of Energy (DOE),
Office of Science, Office of Advanced Scientific Computing
Research, under Contract DE-AC02-06CH11357.

