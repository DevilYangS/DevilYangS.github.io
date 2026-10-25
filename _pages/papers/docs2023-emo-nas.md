---
layout: paper
permalink: /papers/docs2023-emo-nas/
nav: false
paper_title: "Evolutionary Multi-Objective Neural Architecture Search for Generalized Cognitive Diagnosis Models"
authors:
  - name: Shangshang Yang
    me: true
  - name: Cheng Zhen
  - name: Ye Tian
  - name: Haiping Ma
    star: true
  - name: Yuanchao Liu
  - name: Panpan Zhang
  - name: Xingyi Zhang
    star: true
affiliation: "2023 International Conference on Data-driven Optimization of Complex Systems (DOCS), 2023"
venue: "DOCS 2023"
teaser: /assets/img/publication_preview/docs2023.jpg
buttons:
  - label: Paper
    url: https://ieeexplore.ieee.org/abstract/document/10294588/
    icon: "fa fa-file-pdf pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
award: Best Paper
abstract: >
  Cognitive diagnosis models (CDMs) with high generalization are essential for intelligent
  education systems to reveal students' knowledge states in multiple datasets. However, existing
  CDMs' architectures are designed dependent on researcher expertise and experience from observing
  and summarizing partial students' learning behaviors, which makes handcrafted models not cover
  all learning behaviors well and thus limits their generalization. To develop generalized CDMs,
  this paper proposes an evolutionary neural architecture search to design CDMs' architectures
  effective on multiple datasets automatically. Specifically, we first formulate the search task
  as a multi-objective optimization problem (MOP), which maximizes model performance on multiple
  datasets containing learning behaviors as many as possible to ensure model generalization. Then,
  an expressive search space is devised to contain as many potential architectures as possible,
  where each architecture is denoted by a unified form, taking three given inputs and integrating
  them in a linear or no-linear manner for prediction. Finally, an evolutionary algorithm with a
  tailored deduplication strategy is employed to solve the MOP, where each architecture is further
  represented by a single-root computation tree for easy optimization. Experiments on multiple
  datasets demonstrate the generalization and effectiveness of the best architecture searched by
  the proposed approach, and the searched architecture also holds as good interpretability as
  handcrafted architectures.
bibtex: >-
  @inproceedings{yang2023generalized,
    title   = {Evolutionary Multi-Objective Neural Architecture Search for Generalized Cognitive Diagnosis Models},
    author  = {Yang, Shangshang and Zhen, Cheng and Tian, Ye and Ma*, Haiping and Liu, Yuanchao and Zhang, Panpan and Zhang*, Xingyi},
    booktitle = {2023 International Conference on Data-driven Optimization of Complex Systems (DOCS)},
    year    = {2023},
  }
---

## Contributions

- Formulates NAS for generalized cognitive diagnosis as a multi-objective optimization problem maximizing performance on multiple datasets.
- Devises an expressive search space covering diverse learning behaviors.
- Automatically designs CDM architectures with high generalization across datasets.

## Method

A multi-objective evolutionary algorithm searches the proposed space, evaluating each candidate architecture on several datasets with different learning behaviors; the aggregated performance objectives drive the search toward architectures that generalize beyond a single dataset.

## Experimental Results

The searched generalized CDMs achieve better cross-dataset performance than handcrafted models, winning the Best Paper Award of DOCS 2023.
