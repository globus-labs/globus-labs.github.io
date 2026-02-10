---

[comment]: # Do not change the layout
layout: project

[comment]: # Project title
title: "Flight"

[comment]: # The image should be added to images/projects/
image: "flight.png"

[comment]: # List of project members.
people: ["Nathaniel Hudson", "Matt Baughman", "Yadu Babuji", "Kyle Chard", "Ian Foster"]

[comment]: # List of project tags. Remove all that do not apply
hashtags: [
    "Machine Learning",
    "Cloud and Edge Computing",
    "Compute Frameworks",
]

[comment]: # GitHub link or blank if not applicable
github: "https://github.com/globus-labs/flight"

[comment]: # Website/homepage/docs or blank if not applicable
website: 

[comment]: # One-line teaser/description for front page/project page
teaser: "Hierarchical Federated Learning across the Computing Continuum."

[comment]: # Set to false if the project is no longer maintained
active: true

---

Flight is a unique *Federated Learning* (FL) framework, built on top of Globus Compute, to enable research and
deployment of FL pipelines across hierarchical network topologies. While most FL frameworks are limited to simple topologies
of devices with a topmost aggregator and a flat layer of devices to train the model, Flight drops this assumption.
Instead, Flight is able to facilitate FL processes in more complex topologies with multiple aggregators.

Flight's goals are to:
- **Empower Rapid Prototyping.** 
    There are countless research questions surrounding FL. We want FL to be a powerful tool in researcher's toolbox to rapidly develop novel FL algorithms across the computing continuum (i.e., from the edge to super computers).
- **Streamline Deployment.** 
    Flight is meant to simplify the process meant to run FL processes. Ideally, anything that is able to run with Globus Compute and train a deep neural network will be able to participate in an FL process with Flight.


#### Publications
<!-- List the full citations for each paper here with links to where to find it. -->

- Nathaniel Hudson, Valerie Hayot-Sasson, Yadu Babuji, Matt Baughman, J. Gregory Pauloski, Ryan Chard, Ian Foster, and Kyle Chard. [Flight: A FaaS-based framework for complex and Hierarchical Federated Learning,
](https://www.sciencedirect.com/science/article/pii/S0167739X25002936). Future Generation Computer Systems. 2025.

- Nikita Kotsehub, Matt Baughman, Ryan Chard, Nathaniel Hudson, Panos Patros, Omer Rana, Ian Foster, and Kyle Chard. 2022. [FLoX: Federated learning with FaaS at the edge](https://ieeexplore.ieee.org/abstract/document/9973578/). IEEE 18th International Conference on e-Science (e-Science). IEEE, 2022. 

- Nathaniel Hudson, Valerie Hayot-Sasson, Yadu Babuji, Matt Baughman, J. Gregory Pauloski, Ryan Chard, Ian Foster, and Kyle Chard. 2025. [Flight: A FaaS-Based Framework for Complex and Hierarchical Federated Learning](https://arxiv.org/pdf/2409.16495). Future Generation Computer Systems, 2025.

#### Funding and Acknowledgements
<!-- List any funding sources or other acknowledgements here otherwise remove -->
This research was supported in part by DOE contract DE-AC02-06CH11357 and by NSF grants 1816611, 2004894, and 1550588.
