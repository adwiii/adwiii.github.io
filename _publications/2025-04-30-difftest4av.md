---
title: "A Differential Testing Framework to Identify Critical AV Failures Leveraging Arbitrary Inputs"
collection: publications
permalink: /publication/2025-04-30-difftest4av
excerpt: 'The proliferation of autonomous vehicles (AVs) has made their failures increasingly evident. Testing efforts aimed at identifying the inputs leading to those failures are challenged by the input’s long-tail distribution, whose area under the curve is dominated by rare scenarios. We hypothesize that leveraging emerging open-access datasets can accelerate the exploration of long-tail inputs. Having access to diverse inputs, however, is not sufficient to expose failures; an effective test also requires an oracle to distinguish between correct and incorrect behaviors. Current datasets lack such oracles and developing them is notoriously difficult. In response, we propose DIFFTEST4AV, a differential testing framework designed to address the unique challenges of testing AV systems: 1) for any given input, many outputs may be considered acceptable, 2) the long-tail contains an insurmountable number of inputs to explore, and 3) the AV’s continuous execution loop requires for failures to persist in order to affect the system. DIFFTEST4AV integrates statistical analysis to identify meaningful behavioral variations, judges their importance in terms of the severity of these differences, and incorporates sequential analysis to detect persistent errors indicative of potential system-level failures. Our study on 5 versions of the commercially-available, road-deployed comma.ai OpenPilot system, using 3 available image datasets, demonstrates the capabilities of the framework to detect high-severity, high-confidence, long-running test failures.'
date: 2025-04-30
venue: '47th International Conference on Software Engineering (ICSE 2025)'
paperurl: '/files/Differential_Testing_ICSE_2025.pdf'
citation: 'Coming Soon'
bibtex: 'Coming Soon'
image: '/images/difftest4av_splash.png'
journal: false
short_venue: "ICSE'25"
series: ICSE
short_year: "'25"
---

<a href='/files/Differential_Testing_ICSE_2025.pdf'>Download paper here</a>

The proliferation of autonomous vehicles (AVs) has made their failures increasingly evident. Testing efforts aimed at identifying the inputs leading to those failures are challenged by the input’s long-tail distribution, whose area under the curve is dominated by rare scenarios. We hypothesize that leveraging emerging open-access datasets can accelerate the exploration of long-tail inputs. Having access to diverse inputs, however, is not sufficient to expose failures; an effective test also requires an oracle to distinguish between correct and incorrect behaviors. Current datasets lack such oracles and developing them is notoriously difficult. In response, we propose DIFFTEST4AV, a differential testing framework designed to address the unique challenges of testing AV systems: 1) for any given input, many outputs may be considered acceptable, 2) the long-tail contains an insurmountable number of inputs to explore, and 3) the AV’s continuous execution loop requires for failures to persist in order to affect the system. DIFFTEST4AV integrates statistical analysis to identify meaningful behavioral variations, judges their importance in terms of the severity of these differences, and incorporates sequential analysis to detect persistent errors indicative of potential system-level failures. Our study on 5 versions of the commercially-available, road-deployed comma.ai OpenPilot system, using 3 available image datasets, demonstrates the capabilities of the framework to detect high-severity, high-confidence, long-running test failures.
