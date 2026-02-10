---

[comment]: # Do not change the layout
layout: project

[comment]: # Project title
title: "BRISKNet"

[comment]: # The image should be added to images/projects/
image: "brisknet.png"

[comment]: # List of project members.
people: ["Rachel Gordon", "Kyle Chard", "Ian Foster"]

[comment]: # List of project tags. Remove all that do not apply
hashtags: [
    "Machine Learning"
]

[comment]: # GitHub link or blank if not applicable
github: 

[comment]: # Website/homepage/docs or blank if not applicable
website: 

[comment]: # One-line teaser/description for front page/project page
teaser: "Breast Rapid Imaging via Self-Supervised Kinetics"

[comment]: # Set to false if the project is no longer maintained
active: true

---

<!--
Add your project description below according to these guidelines.

 - Use Markdown syntax everywhere, not HTML!
 - Use active voice ("we")
 - Limit the intro paragraph to 3 sentences or less.
 - Keep the overall length under 3 paragraphs.
 - Bullet points are helpful for quickly understanding key points.
 - Add figures and additional links if relevant.

An example first paragraph:

 1. Sentence giving overall context, hinting at the problem we solve.
      "Most humans don't like to read long paragraphs and writing short
      ones takes thought."
 2. An explanation of how we fix it.
      "We made a simple template that you can follow for how to write one."
 3. A statement of impact.
      "Any Globus Labs member need only edit this template to make their
      science more accessible."
-->


Dynamic contrast-enhanced (DCE) MRI plays a central role in breast cancer diagnosis and staging by measuring how contrast agents enter and wash out of tissue. These contrast kinetics reflect vascular architecture and tumor biology, and emerging evidence suggests that contrast kinetics within the first two seconds after contrast injection encode previously inaccessible physiological biomarkers relevant to cancer risk and treatment response prediction. However, current breast DCE-MRI acquisition methods are fundamentally limited by a trade-off between spatial and temporal resolution, leaving the early sub-2-second window of contrast dynamics unresolved. 

BRISKNet is a self-supervised, physics-informed framework for reconstructing highly undersampled breast DCE-MRI with improved spatiotemporal resolution. The framework integrates principles from compressed sensing, parallel imaging, and non-Cartesian sampling with deep learning-based MRI reconstruction. By avoiding reliance on fully sampled ground-truth data, which is infeasible to obtain in DCE-MRI due to frame rates that inherently require undersampling, BRISKNet enables robust reconstruction at high temporal resolutions. This framework achieves reconstruction quality comparable to iterative methods while enabling faster reconstruction and improved visualization of rapid contrast kinetics. This work provides a foundation for discovering new kinetic biomarkers for personalized breast cancer risk stratification. 

#### Funding and Acknowledgements

This work is partially supported by the University of Chicago’s AI+Science Research Initiative through the Margot and Tom Pritzker Foundation.