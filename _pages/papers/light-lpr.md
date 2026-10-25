---
layout: paper
permalink: /papers/light-lpr/
nav: false
paper_title: "Enhancing Learning Path Recommendation via Knowledge Topology-Aware Sequence Optimization"
authors:
  - name: Xiaoshan Yu
  - name: Shangshang Yang
    me: true
    star: true
  - name: Ziwen Wang
  - name: Shuang Song
  - name: Haiping Ma
  - name: Zhen Cao
  - name: Xingyi Zhang
affiliation: "ACM SIGIR Conference on Research and Development in Information Retrieval, 2025"
venue: "SIGIR 2025"
teaser: /assets/img/publication_preview/yu2025enhancing.jpg
buttons:
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  Learning path recommendation (LPR) aims to provide individualized and effective learning item
  routes by modeling learners' learning histories and goals, which has been widely considered a
  essential task in the field of personalized education. Indeed, considerable research efforts
  have been dedicated to this direction in recent years, focusing on step-based and sequence-based
  modeling approaches. However, most of existing studies overlook the complementarity between
  explicit and implicit relationships among knowledge concepts, while failing to harmonize static
  knowledge structures with dynamic path generation. To this end, in this paper, we propose LIGHT,
  a knowLedge topology-aware sequence optImization model for enhancing learninG patH
  recommendaTion. Specifically, we first construct a composite concept graph that incorporates
  explicit prerequisite relationships and implicit collaborative relationships, achieved by mining
  interaction statistics and collaborative signals from learners' learning processes. Next, we
  design a complementary contrastive fusion module to fully capture the interplay between the two
  relational views of concepts through graph structure learning and contrastive constraints, which
  enhances the effectiveness of the learned representations. Following this, we introduce a
  knowledge topology-aware modeling module that integrates structural semantics clustering with
  candidate path sampling. Finally, we develop a bidirectional sensing path optimization network
  to deeply model and optimize the sampled paths from a sequential perspective, thereby enhancing
  modeling efficiency while preserving structural semantics. Extensive experiments on three
  real-world educational datasets clearly demonstrate the effectiveness of the proposed LIGHT
  model in the LPR task.
bibtex: >-
  @inproceedings{yu2025enhancing,
    title   = {Enhancing Learning Path Recommendation via Knowledge Topology-Aware Sequence Optimization},
    author  = {Yu, Xiaoshan and Yang*, Shangshang and Wang, Ziwen and Song, Shuang and Ma, Haiping and Cao, Zhen and Zhang, Xingyi},
    booktitle = {ACM SIGIR Conference on Research and Development in Information Retrieval},
    pages   = {306--315},
    year    = {2025},
  }
---

## Contributions

- Proposes LIGHT, a knowledge topology-aware sequence optimization model for learning path recommendation.
- Constructs a composite concept graph that fuses explicit prerequisite relations with implicit collaborative signals.
- Harmonizes the static knowledge structure with dynamic path generation during recommendation.

## Method

LIGHT first builds a composite concept graph combining prerequisite edges mined from curricula and collaborative edges learned from learner behaviors, then optimizes generated learning sequences against this topology so that recommended paths respect both conceptual dependencies and observed learning regularities.

## Experimental Results

On real-world learning datasets LIGHT outperforms state-of-the-art learning path recommendation baselines in both recommendation effectiveness and post-learning performance of simulated learners.
