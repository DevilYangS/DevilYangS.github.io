---
layout: paper
permalink: /papers/emo-nas-cd/
nav: false
paper_title: "An Evolutionary Multi-Objective Neural Architecture Search Approach to Advancing Cognitive Diagnosis in Intelligent Education"
authors:
  - name: Shangshang Yang
    me: true
  - name: Haiping Ma
  - name: Ying Bi
  - name: Ye Tian
  - name: Limiao Zhang
    star: true
  - name: Yaochu Jin
  - name: Xingyi Zhang
    star: true
affiliation: "IEEE Transactions on Evolutionary Computation, 2024"
venue: "TEVC 2024"
teaser: /assets/img/publication_preview/EMO-NAS-CD.jpg
buttons:
  - label: Paper
    url: https://ieeexplore.ieee.org/abstract/document/10599558/
    icon: "fa fa-file-pdf pr-1"
  - label: Code
    url: https://github.com/DevilYangS/EMO-NAS-CD
    icon: "fab fa-github pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  As a pivotal technique in intelligent education systems, cognitive diagnosis (CD) serves to
  reveal students’ knowledge proficiency for better tackling subsequent tasks. Unfortunately, due
  to pursuing high model interpretability, existing manually designed models for CD often hold
  simplistic architectures, which cannot cope with intricate data in modern education platforms.
  Furthermore, the bias of human design limits the emergence of novel and effective CD models
  (CDMs). To develop interpretable and more effective models, thus this article proposes an
  evolutionary multiobjective neural architecture search (NAS) approach for CD. Specifically, we
  first adopt a comprehensive search space for the NAS task of CD: all candidate models can be
  encompassed by a general model that deals with three distinct types of inputs. Then, an
  innovative model interpretability objective is devised to formulate the architecture search task
  as a bi-objective optimization problem (BOP). To solve the BOP, we employ a multiobjective
  genetic programming (MOGP) as the search strategy to explore the search space. To make the
  employed MOGP search well, all architectures are first encoded by trees for easy optimization,
  and we devise a genetic operation and a population initialization strategy to expedite its
  convergence. Finally, the proposed approach is actually an MOGP-based NAS approach for CD.
  Extensive experiments show that CDMs searched by the proposed approach exhibit significantly
  better performance than existing models and hold as good interpretability as handcrafted models.
  Besides, the effectiveness of the proposed MOGP search strategy, the devised objective, and
  tailored strategies are validated.
bibtex: >-
  @article{yang2024emonascd,
    title   = {An Evolutionary Multi-Objective Neural Architecture Search Approach to Advancing Cognitive Diagnosis in Intelligent Education},
    author  = {Yang, Shangshang and Ma, Haiping and Bi, Ying and Tian, Ye and Zhang*, Limiao and Jin, Yaochu and Zhang*, Xingyi},
    journal = {IEEE Transactions on Evolutionary Computation},
    year    = {2024},
  }
---

## Contributions

- Adopts a comprehensive search space for CD in which all candidate models are encompassed by a general model handling three distinct input types.
- Devises an innovative model interpretability objective to formulate CD-NAS as a multi-objective problem.
- Searches interpretable and more effective CD models automatically, freeing design from human bias.

## Method

The search space is defined over a general cognitive diagnosis model that accepts three types of inputs; a multi-objective evolutionary algorithm jointly optimizes diagnosis accuracy and model interpretability, returning a Pareto set of architectures from which practitioners can choose.

## Experimental Results

The evolved CDMs outperform representative manually-designed models on multiple datasets while offering explicit interpretability, demonstrating that automated multi-objective search yields models better suited to intricate modern educational data.
