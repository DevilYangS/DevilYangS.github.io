---
layout: paper
permalink: /papers/trainable-ea/
nav: false
paper_title: "Trainable Evolutionary Algorithms: A Reinforcement Learning Perspective on Algorithm Configuration"
authors:
  - name: Wenbiao Li
  - name: Shangshang Yang
    me: true
    star: true
  - name: Ye Tian
  - name: Zimo Sheng
affiliation: "The 8th International Conference on Data-driven Optimization of Complex Systems (DOCS), 2026"
venue: "DOCS 2026"
teaser: /assets/img/publication_preview/docs2026_best_paper.jpg
buttons:
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
award: Best Paper Award
abstract: >
  Trainable EAs have recently emerged as a promising paradigm for improving the adaptability of
  optimization algorithms. However, their effectiveness largely depends on how configurable
  algorithm components are parameterized. This paper studies algorithm configuration for trainable
  EAs and proposes an RL-based configuration framework for NeuroEA, a neural-network-like modular
  evolutionary algorithm. A Soft Actor-Critic (SAC) agent is employed to generate NeuroEA
  parameter configurations, while NeuroEA itself performs the optimization process. Both static
  and dynamic configuration paradigms are investigated under a unified framework. The former
  determines algorithm parameters before optimization starts, whereas the latter continuously
  updates parameters according to runtime search states. Experimental results on BBOB and SOP
  benchmark problems show that the proposed framework can effectively improve NeuroEA performance
  and achieve competitive results compared with representative optimization and configuration
  baselines. The study further provides insights into the advantages and limitations of static and
  dynamic configuration for trainable EAs.
bibtex: >-
  @inproceedings{li2026trainable,
    title   = {Trainable Evolutionary Algorithms: A Reinforcement Learning Perspective on Algorithm Configuration},
    author  = {Li, Wenbiao and Yang*, Shangshang and Tian, Ye and Sheng, Zimo},
    booktitle = {The 8th International Conference on Data-driven Optimization of Complex Systems (DOCS 2026)},
    year    = {2026},
  }
---

## Contributions

- Studies algorithm configuration for trainable evolutionary algorithms and proposes an RL-based configuration framework for NeuroEA.
- Employs a Soft Actor-Critic agent to generate NeuroEA parameter configurations under both static and dynamic paradigms.
- Provides insights into the advantages and limitations of static vs. dynamic configuration for trainable EAs.

## Method

A Soft Actor-Critic (SAC) agent generates parameter configurations for NeuroEA — a neural-network-like modular evolutionary algorithm — while NeuroEA performs the optimization; in the static paradigm parameters are fixed before optimization starts, whereas the dynamic paradigm continuously updates them according to runtime search states.

## Experimental Results

On BBOB and SOP benchmark problems the proposed framework effectively improves NeuroEA performance and achieves competitive results against representative optimization and configuration baselines.
