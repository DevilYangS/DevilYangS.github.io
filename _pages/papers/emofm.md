---
layout: paper
permalink: /papers/emofm/
nav: false
paper_title: "An Evolutionary Multiobjective Optimization Based Fuzzy Method for Overlapping Community Detection"
authors:
  - name: Ye Tian
  - name: Shangshang Yang
    me: true
  - name: Xingyi Zhang
    star: true
affiliation: "IEEE Transactions on Fuzzy Systems, 2019"
venue: "TFS 2019"
buttons:
  - label: Paper
    url: https://ieeexplore.ieee.org/abstract/document/8855008
    icon: "fa fa-file-pdf pr-1"
  - label: Code
    url: https://github.com/DevilYangS/EMOFM
    icon: "fab fa-github pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  In the last decade, the detection of overlapping communities has received increasing attention
  in network science. Among various clustering techniques, the fuzzy clustering has been widely
  adopted in overlapping community detection, since the soft assignment provided by it naturally
  meets the overlapping between multiple communities. The crucial step of fuzzy-clustering-based
  overlapping community detection is to find the optimal community centers, so that the
  overlapping communities can be obtained according to the membership degrees between nodes and
  community centers. In this article, we propose an evolutionary multiobjective optimization-based
  fuzzy method for overlapping community detection. In contrast to traditional fuzzy clustering
  methods, the proposed method optimizes the community centers by using a specially tailored
  multiobjective evolutionary algorithm. Moreover, it can also find an appropriate fuzzy threshold
  for each node, so that diverse overlapping community structures can be uncovered. In the
  experiments, we compare the proposed method with six state-of-the-art overlapping community
  detection approaches on synthetic and real-world networks with different scales and
  characteristics. The statistical results demonstrate that the proposed method can obtain the
  best results on most test instances.
bibtex: >-
  @article{tian2019evolutionary,
    title   = {An Evolutionary Multiobjective Optimization Based Fuzzy Method for Overlapping Community Detection},
    author  = {Tian, Ye and Yang, Shangshang and Zhang*, Xingyi},
    journal = {IEEE Transactions on Fuzzy Systems},
    volume   = {28},
    number   = {11},
    pages   = {2841--2855},
    year    = {2019},
  }
---

## Contributions

- Proposes an evolutionary multiobjective optimization-based fuzzy method (EMOFM) for overlapping community detection.
- Optimizes community centers with a specially tailored multiobjective EA instead of traditional fuzzy clustering update rules.
- Automatically finds an appropriate fuzzy threshold for each node, uncovering diverse overlapping community structures.

## Method

EMOFM encodes community centers as individuals and evolves them under multiple objectives that trade off cohesion and separation of fuzzy partitions; membership degrees between nodes and the evolved centers then yield overlapping communities, with per-node thresholds adapted during the search.

## Experimental Results

**Compared algorithms:** Six state-of-the-art overlapping community detection approaches.

**Datasets:** Synthetic and real-world networks of different scales.

**Metrics:** Overlapping community detection quality.

**Overall results:** EMOFM obtains the best results on most test instances (code at github.com/DevilYangS/EMOFM).
