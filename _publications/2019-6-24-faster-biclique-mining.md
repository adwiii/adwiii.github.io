---
title: "Faster Biclique Mining in Near-Bipartite Graphs"
collection: publications
permalink: /publication/2019-6-24-faster-biclique-mining
excerpt: 'Identifying dense bipartite subgraphs is a common graph data mining task. Many applications focus on the enumeration of all maximal bicliques (MBs), though sometimes the stricter variant of maximal induced bicliques (MIBs) is of interest. Recent work of Kloster et al. introduced a MIB-enumeration approach designed for “near-bipartite” graphs, where the runtime is parameterized by the size k of an odd cycle transversal (OCT), a vertex set whose deletion results in a bipartite graph. Their algorithm was shown to outperform the previously best known algorithm even when k was logarithmic in <code>|V|</code>. In this paper, we introduce two new algorithms optimized for near-bipartite graphs - one which enumerates MIBs in time <code>O(M<sub>I</sub>|V||E|k)</code>, and another based on the approach of Alexe et al. which enumerates MBs in time <code>O(M<sub>B</sub>|V||E|k)</code>, where <code>M<sub>I</sub></code> and <code>M<sub>B</sub></code> denote the number of MIBs and MBs in the graph, respectively. We implement all of our algorithms in open-source C++ code and experimentally verify that the OCT-based approaches are faster in practice than the previously existing algorithms on graphs with a wide variety of sizes, densities, and OCT decompositions.'
date: 2019-6-24
venue: 'International Symposium on Experimental Algorithms'
paperurl: 'https://link.springer.com/chapter/10.1007/978-3-030-34029-2_28'
citation: 'Sullivan, Blair D., Andrew van der Poel, and Trey Woodlief. &quot;Faster Biclique Mining in Near-Bipartite Graphs.&quot; <i>International Symposium on Experimental Algorithms</i>. Springer, Cham, 2019.'
bibtex: '@inproceedings{sullivan2019faster,  title={Faster Biclique Mining in Near-Bipartite Graphs},  author={Sullivan, Blair D and Poel, Andrew van der and Woodlief, Trey},  booktitle={International Symposium on Experimental Algorithms},  pages={424--453},  year={2019},  organization={Springer}}'
journal: false
short_venue: "SEA^2'19"
series: SEA^2
short_year: "'19"
---

<a href='https://link.springer.com/chapter/10.1007/978-3-030-34029-2_28'>Download paper here</a>

Identifying dense bipartite subgraphs is a common graph data mining task. Many applications focus on the enumeration of all maximal bicliques (MBs), though sometimes the stricter variant of maximal induced bicliques (MIBs) is of interest. Recent work of Kloster et al. introduced a MIB-enumeration approach designed for “near-bipartite” graphs, where the runtime is parameterized by the size k of an odd cycle transversal (OCT), a vertex set whose deletion results in a bipartite graph. Their algorithm was shown to outperform the previously best known algorithm even when k was logarithmic in <code>|V|</code>. In this paper, we introduce two new algorithms optimized for near-bipartite graphs - one which enumerates MIBs in time <code>O(M<sub>I</sub>|V||E|k)</code>, and another based on the approach of Alexe et al. which enumerates MBs in time <code>O(M<sub>B</sub>|V||E|k)</code>, where <code>M<sub>I</sub></code> and <code>M<sub>B</sub></code> denote the number of MIBs and MBs in the graph, respectively. We implement all of our algorithms in open-source C++ code and experimentally verify that the OCT-based approaches are faster in practice than the previously existing algorithms on graphs with a wide variety of sizes, densities, and OCT decompositions.
