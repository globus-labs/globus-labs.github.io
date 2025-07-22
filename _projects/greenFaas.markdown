---

[comment]: # Do not change the layout
layout: project

[comment]: # Project title
title: "GreenFaaS"

[comment]: # The image should be added to images/projects/
image: "greenfaas.png"

[comment]: # List of project members.
people: ["Alok Kamatar", "Valerie Hayot-Sasson", "Andre Bauer", "Kyle Chard", "Ian Foster"]

[comment]: # List of project tags. Remove all that do not apply
hashtags: [
    "Cloud and Edge Computing",
    "Compute Frameworks",
]

[comment]: # GitHub link or blank if not applicable
github: "https://github.com/AK2000/caws"

[comment]: # Website/homepage/docs or blank if not applicable
website:

[comment]: # One-line teaser/description for front page/project page
teaser: "A monitoring and scheduling framework to find the most energy-efficient endpoints for your application."

[comment]: # Set to false if the project is no longer maintained
active: false

---

Computational scientists have access to a variety of different types of machines distributed across many sites. Typically users run their applications only using a single (typically homogeneous) machine. We find that this could be detrimental for energy efficiency. When measuring the marginal energy consumption of different functions across machines, we see a tremendous variation. Not only does the most efficient function vary by machine, but the most efficient machine also depends on the function being run, and the occupancy of the machine. This complexity makes it extremely difficult for users to run applications in an energy efficient manner. To address these issues, we propose GreenFaaS, a framework built on top of Globus Compute that allows users to monitor their energy consumption and schedule tasks in an efficient manner.

Scientists are not typically concerned with the energy efficiency of their applications. In practice, users are driven by a mix of performance, availability (queue times) and funding (allocations). This leaves energy efficiency to an afterthought. To address this de-prioritization of efficiency, we study different incentives to make users more aware and concerned with their energy use. We propose 2 different allocation policies for HPC infrastructure that tie compute resources to either the energy used, or the total estimated carbon emissions. We then examine the effects of these policies using simulations, and by conducting a user study.

#### Publications
<!-- List the full citations for each paper here with links to where to find it. -->
A. Kamatar et al., "Enhancing Energy Efficiency with Multi-Site Scheduling Strategies," 2024 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW), San Francisco, CA, USA, 2024, pp. 1175-1177, doi: 10.1109/IPDPSW63119.2024.00197.

Kamatar, A., Hayot-Sasson, V., Babuji, Y., Bauer, A., Rattihalli, G., Hogade, N., Milojicic, D., Chard, K. and Foster, I., 2024. GreenFaaS: Maximizing Energy Efficiency of HPC Workloads with FaaS. arXiv preprint arXiv:2406.17710.

Kamatar, Alok, Maxime Gonthier, Valerie Hayot-Sasson, Andre Bauer, Marcin Copik, Torsten Hoefler, Raul Castro Fernandez, Kyle Chard, and Ian Foster. "Core Hours and Carbon Credits: Incentivizing Sustainability in HPC." arXiv preprint arXiv:2501.09557 (2025). (To Appear in SC' 25)


#### Funding and Acknowledgements
<!-- List any funding sources or other acknowledgements here otherwise remove -->
Available soon.
