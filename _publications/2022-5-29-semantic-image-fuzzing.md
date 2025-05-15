---
title: "Semantic Image Fuzzing of AI Perception Systems"
collection: publications
permalink: /publication/2022-5-29-semantic-image-fuzzing
excerpt: 'Perception systems enable autonomous systems to interpret raw sensor readings of the physical world. Testing of perception systems aims to reveal misinterpretations that could cause system failures. Current testing methods, however, are inadequate. The cost of human interpretation and annotation of real-world input data is high, so manual test suites tend to be small. The simulation-reality gap reduces the validity of test results based on simulated worlds. And methods for synthesizing test inputs do not provide corresponding expected interpretations. To address these limitations, we developed 𝑠𝑒𝑚𝑆𝑒𝑛𝑠𝐹𝑢𝑧𝑧, a new approach to fuzz testing of perception systems based on semantic mutation of test cases that pair real-world sensor readings with their ground-truth interpretations. We implemented our approach to assess its feasibility and potential to improve software testing for perception systems. We used it to generate 150,000 semantically mutated image inputs for five state-of-the-art perception systems. We found that it synthesized tests with novel and subjectively realistic image inputs, and that it discovered inputs that revealed significant inconsistencies between the specified and computed interpretations. We also found that it produced such test cases at a cost that was very low compared to that of manual semantic annotation of real-world images.'
date: 2022-5-29
venue: '44th International Conference on Software Engineering (ICSE 2022)'
paperurl: 'https://github.com/less-lab-uva/perception_fuzzing/blob/main/Semantic%20Image%20Fuzzing%20of%20AI%20Perception%20Systems.pdf'
citation: 'Trey Woodlief, Sebastian Elbaum, and Kevin Sullivan. 2022. Semantic Image Fuzzing of AI Perception Systems. In 44th International Conference on Software Engineering (ICSE ’22), May 21–29, 2022, Pittsburgh, PA, USA. ACM, New York, NY, USA, 12 pages. https://doi.org/10.1145/3510003.3510212'
bibtex: '@inproceedings{woodlief2022semantic,  title={Semantic image fuzzing of AI perception systems},  author={Woodlief, Trey and Elbaum, Sebastian and Sullivan, Kevin},  booktitle={Proceedings of the 44th International Conference on Software Engineering}, pages={1958--1969}, year={2022}}'
image: '/images/semSensFuzz.png'
github: 'https://github.com/less-lab-uva/perception_fuzzing'
paper_type: 'FULL'
journal: false
short_venue: "ICSE'22"
series: ICSE
short_year: "'22"
---

<a href='https://github.com/less-lab-uva/perception_fuzzing/blob/main/Semantic%20Image%20Fuzzing%20of%20AI%20Perception%20Systems.pdf'>Download paper here</a>&nbsp;&nbsp;
<a href="https://github.com/less-lab-uva/perception_fuzzing"><i class="fab fa-fw fa-github" aria-hidden="true"></i> Github</a>

Perception systems enable autonomous systems to interpret raw sensor readings of the physical world. Testing of perception systems aims to reveal misinterpretations that could cause system failures. Current testing methods, however, are inadequate. The cost of human interpretation and annotation of real-world input data is high, so manual test suites tend to be small. The simulation-reality gap reduces the validity of test results based on simulated worlds. And methods for synthesizing test inputs do not provide corresponding expected interpretations. To address these limitations, we developed 𝑠𝑒𝑚𝑆𝑒𝑛𝑠𝐹𝑢𝑧𝑧, a new approach to fuzz testing of perception systems based on semantic mutation of test cases that pair real-world sensor readings with their ground-truth interpretations. We implemented our approach to assess its feasibility and potential to improve software testing for perception systems. We used it to generate 150,000 semantically mutated image inputs for five state-of-the-art perception systems. We found that it synthesized tests with novel and subjectively realistic image inputs, and that it discovered inputs that revealed significant inconsistencies between the specified and computed interpretations. We also found that it produced such test cases at a cost that was very low compared to that of manual semantic annotation of real-world images.
