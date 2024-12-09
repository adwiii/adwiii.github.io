---
title: "The SGSM framework: Enabling the specification and monitor synthesis of safe driving properties through scene graphs"
collection: publications
permalink: /publication/2024-11-26-sgsm-framework
excerpt: 'As autonomous vehicles (AVs) become mainstream, assuring that they operate in accordance with safe driving properties becomes paramount. The ability to specify and monitor driving properties is at the center of such assurance. Yet, the mismatch between the semantic space over which typical driving properties are asserted (e.g., vehicles, pedestrians) and the sensed inputs of AVs (e.g., images, point clouds) poses a significant assurance gap. Related efforts bypass this gap by either assuming that data at the right semantic level is available, or they develop bespoke methods for capturing such data. Our recent Scene Graph Safety Monitoring (SGSM) framework addresses this challenge by extracting scene graphs (SGs) from sensor inputs to capture the entities related to the AV, specifying driving properties using a domain-specific language that enables building propositions over those graphs and composing them through temporal logic, and synthesizing monitors to detect property violations. Through this paper we further explain, formalize, analyze, and extend the SGSM framework, producing SGSM++. This extension is significant in that it incorporates the ability for the framework to encode the semantics of resetting a property violation, enabling the framework to count the quantity and duration of violations. We implemented SGSM++ to monitor for violations of 9 properties of 3 AVs from the CARLA Autonomous Driving Leaderboard, confirming the viability of the framework, which found that the AVs violated 71% of properties during at least one test including almost 1400 unique violations over 30 total test executions, with violations lasting up to 9.25 minutes. Artifact available at https://github.com/less-lab-uva/ExtendingSGSM.'
date: 2024-11-26
venue: 'Science of Computer Programming'
paperurl: 'https://authors.elsevier.com/a/1kEgNc7X5A%7EFU'
citation: 'Trey Woodlief, Felipe Toledo, Sebastian Elbaum, Matthew B. Dwyer, The SGSM framework: Enabling the specification and monitor synthesis of safe driving properties through scene graphs, Science of Computer Programming, Volume 242, 2025, 103252, ISSN 0167-6423, https://doi.org/10.1016/j.scico.2024.103252.'
bibtex: '@article{WOODLIEF2025103252,
title = {The SGSM framework: Enabling the specification and monitor synthesis of safe driving properties through scene graphs},
journal = {Science of Computer Programming},
volume = {242},
pages = {103252},
year = {2025},
issn = {0167-6423},
doi = {https://doi.org/10.1016/j.scico.2024.103252},
url = {https://www.sciencedirect.com/science/article/pii/S0167642324001758},
author = {Trey Woodlief and Felipe Toledo and Sebastian Elbaum and Matthew B. Dwyer},
keywords = {Runtime verification, Autonomous vehicles, Safe driving properties, Scene graphs},
}'
image: '/images/extending_sgsm.png'
github: 'https://github.com/less-lab-uva/ExtendingSGSM'
journal: true
year: 2024
---

<a href='https://authors.elsevier.com/a/1kEgNc7X5A%7EFU'>Download paper here</a>&nbsp;&nbsp;<a href="https://github.com/less-lab-uva/ExtendingSGSM"><i class="fab fa-fw fa-github" aria-hidden="true"></i> Github</a>

As autonomous vehicles (AVs) become mainstream, assuring that they operate in accordance with safe driving properties becomes paramount. The ability to specify and monitor driving properties is at the center of such assurance. Yet, the mismatch between the semantic space over which typical driving properties are asserted (e.g., vehicles, pedestrians) and the sensed inputs of AVs (e.g., images, point clouds) poses a significant assurance gap. Related efforts bypass this gap by either assuming that data at the right semantic level is available, or they develop bespoke methods for capturing such data. Our recent Scene Graph Safety Monitoring (SGSM) framework addresses this challenge by extracting scene graphs (SGs) from sensor inputs to capture the entities related to the AV, specifying driving properties using a domain-specific language that enables building propositions over those graphs and composing them through temporal logic, and synthesizing monitors to detect property violations. Through this paper we further explain, formalize, analyze, and extend the SGSM framework, producing SGSM++. This extension is significant in that it incorporates the ability for the framework to encode the semantics of resetting a property violation, enabling the framework to count the quantity and duration of violations. We implemented SGSM++ to monitor for violations of 9 properties of 3 AVs from the CARLA Autonomous Driving Leaderboard, confirming the viability of the framework, which found that the AVs violated 71% of properties during at least one test including almost 1400 unique violations over 30 total test executions, with violations lasting up to 9.25 minutes. Artifact available at https://github.com/less-lab-uva/ExtendingSGSM.
