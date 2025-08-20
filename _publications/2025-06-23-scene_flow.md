---
title: "Scene Flow Specifications: Encoding and Monitoring Rich Temporal Safety Properties of Autonomous Systems"
collection: publications
permalink: /publication/2025-06-23-scene_flow
excerpt: 'To ensure the safety of autonomous systems, it is imperative for them to abide by their safety properties. The specification of such safety properties is challenging because of the gap between the input sensor space (e.g., pixels, point clouds) and the semantic space over which safety properties are specified (e.g. people, vehicles, road). Recent work utilized scene graphs to overcome portions of that gap, enabling the specification and synthesis of monitors targeting many safe driving properties for autonomous vehicles. However, scene graphs are not rich enough to express the many driving properties that include temporal elements (i.e., when two vehicles enter an intersection at the same time, the vehicle on the left shall yield...), fundamentally limiting the types of specifications that can be monitored. In this work, we characterize the expressiveness required to specify a large body of driving properties, identify property types that cannot be specified with current approaches, which we name scene flow properties, and construct an enhanced domain-specific language that utilizes symbolic entities across time to enable the encoding of the rich temporal properties required for autonomous system safety. In analyzing a set of 114 specifications, we find that our approach can successfully encode 110 (96%) specifications as compared to 87 (76%) under prior approaches, an improvement of 20 percentage points. We implement the specifications in the form of a runtime monitoring framework to check the compliance of 3 state-of-the-art autonomous vehicles finding that they violated scene flow properties over 40 times in 30 test executions, including 34 violations for failing to yield properly at intersections. Empirical results demonstrate the implementation is suitably efficient for runtime monitoring applications.'
date: 2025-06-23
venue: '2025 ACM International Conference on the Foundations of Software Engineering'
paperurl: '/files/fse_scene_flow.pdf'
citation: 'Trey Woodlief, Felipe Toledo, Matthew Dwyer, and Sebastian Elbaum. 2025. Scene Flow Specifications: Encoding and Monitoring Rich Temporal Safety Properties of Autonomous Systems. Proc. ACM Softw. Eng. 2, FSE,
Article FSE112 (July 2025), 24 pages. https://doi.org/10.1145/3729382'
bibtex: '@article{woodlief2025scene,
  title={Scene Flow Specifications: Encoding and Monitoring Rich Temporal Safety Properties of Autonomous Systems},
  author={Woodlief, Trey and Toledo, Felipe and Dwyer, Matthew and Elbaum, Sebastian},
  journal={Proceedings of the ACM on Software Engineering},
  volume={2},
  number={FSE},
  pages={2524--2547},
  year={2025},
  publisher={ACM New York, NY, USA}
}'
image: '/images/Scene_Flow.png'
github: 'https://github.com/less-lab-uva/SceneFlowLang'
paper_type: 'FULL'
journal: false
short_venue: "FSE'25"
series: FSE
short_year: "'25"
---

<a href='/files/fse_scene_flow.pdf'>Download paper here</a>&nbsp;&nbsp;
<a href="https://github.com/less-lab-uva/SceneFlowLang"><i class="fab fa-fw fa-github" aria-hidden="true"></i> Github</a>

To ensure the safety of autonomous systems, it is imperative for them to abide by their safety properties. The specification of such safety properties is challenging because of the gap between the input sensor space (e.g., pixels, point clouds) and the semantic space over which safety properties are specified (e.g. people, vehicles, road). Recent work utilized scene graphs to overcome portions of that gap, enabling the specification and synthesis of monitors targeting many safe driving properties for autonomous vehicles. However, scene graphs are not rich enough to express the many driving properties that include temporal elements (i.e., when two vehicles enter an intersection at the same time, the vehicle on the left shall yield...), fundamentally limiting the types of specifications that can be monitored. In this work, we characterize the expressiveness required to specify a large body of driving properties, identify property types that cannot be specified with current approaches, which we name scene flow properties, and construct an enhanced domain-specific language that utilizes symbolic entities across time to enable the encoding of the rich temporal properties required for autonomous system safety. In analyzing a set of 114 specifications, we find that our approach can successfully encode 110 (96%) specifications as compared to 87 (76%) under prior approaches, an improvement of 20 percentage points. We implement the specifications in the form of a runtime monitoring framework to check the compliance of 3 state-of-the-art autonomous vehicles finding that they violated scene flow properties over 40 times in 30 test executions, including 34 violations for failing to yield properly at intersections. Empirical results demonstrate the implementation is suitably efficient for runtime monitoring applications.
