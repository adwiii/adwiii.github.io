---
title: "Specifying and Monitoring Safe Driving Properties with Scene Graphs"
collection: publications
permalink: /publication/2024-5-17-sg-monitoring
excerpt: 'With the proliferation of autonomous vehicles (AVs)  comes the need to ensure they abide to safe driving  properties. Specifying and monitoring such properties, however, is challenging because of the mismatch between the semantic space over which typical driving properties are asserted (e.g., vehicles,   pedestrians, intersections) and the sensed inputs of AVs. Existing efforts either assume for such sematic data  to be available or develop bespoke methods for capturing it. Instead, this work introduces a framework that can extract scene graphs  from sensor inputs to capture the entities related to the AV, and a domain-specific language  that enables   building propositions over those  graphs and composing them through temporal logic. We implemented the framework to monitor for specification violations of 3 top AVs from the CARLA Autonomous Driving Leaderboard, and found that on average the AVs violated 71% of properties during at least one test.'
date: 2024-5-17
venue: '2024 IEEE International Conference on
Robotics and Automation'
paperurl: 'https://github.com/less-lab-uva/ExtendingSGSM/blob/master/ICRA24_Specifying_and_Monitoring_with_Scene_Graphs.pdf'
citation: 'Toledo, Felipe, Trey Woodlief, Sebastian Elbaum, and Matthew B. Dwyer. &quot;Specifying and Monitoring Safe Driving Properties with Scene Graphs.&quot; In 2024 IEEE International Conference on Robotics and Automation (ICRA), pp. 15577-15584. IEEE, 2024.'
bibtex: '@inproceedings{toledo2024specifying,title={Specifying and Monitoring Safe Driving Properties with Scene Graphs},author={Toledo, Felipe and Woodlief, Trey and Elbaum, Sebastian and Dwyer, Matthew B},booktitle={2024 IEEE International Conference on Robotics and Automation (ICRA)},pages={15577--15584},year={2024},organization={IEEE}}'
image: '/images/icra24.png'
github: 'https://github.com/less-lab-uva/sgsm'
short_venue: "ICRA'24"
series: ICRA
short_year: "'24"
---

<a href='https://github.com/less-lab-uva/ExtendingSGSM/blob/master/ICRA24_Specifying_and_Monitoring_with_Scene_Graphs.pdf'>Download paper here</a>&nbsp;&nbsp;<a href="https://github.com/less-lab-uva/sgsm"><i class="fab fa-fw fa-github" aria-hidden="true"></i> Github</a>

With the proliferation of autonomous vehicles (AVs)  comes the need to ensure they abide to safe driving  properties. Specifying and monitoring such properties, however, is challenging because of the mismatch between the semantic space over which typical driving properties are asserted (e.g., vehicles,   pedestrians, intersections) and the sensed inputs of AVs. Existing efforts either assume for such sematic data  to be available or develop bespoke methods for capturing it. Instead, this work introduces a framework that can extract scene graphs  from sensor inputs to capture the entities related to the AV, and a domain-specific language  that enables   building propositions over those  graphs and composing them through temporal logic. We implemented the framework to monitor for specification violations of 3 top AVs from the CARLA Autonomous Driving Leaderboard, and found that on average the AVs violated 71% of properties during at least one test.
