---
layout: paper
permalink: /papers/hashcat/
nav: false
paper_title: "Reconciling Efficiency and Effectiveness of Exercise Retrieval: An Uncertainty Reduction Hashing Approach for Computerized Adaptive Testing"
authors:
  - name: Haiping Ma
  - name: Yang Zhou
  - name: Xiaoshan Yu
  - name: Changqian Wang
  - name: Shangshang Yang
    me: true
    star: true
  - name: Limiao Zhang
  - name: Xingyi Zhang
affiliation: "ACM SIGIR Conference on Research and Development in Information Retrieval, 2025"
venue: "SIGIR 2025"
teaser: /assets/img/publication_preview/ma2025reconciling.jpg
buttons:
  - label: PDF
    url: /assets/pdf/ma2025reconciling.pdf
    icon: "fa fa-file-pdf pr-1"
  - label: Paper
    url: https://dl.acm.org/doi/10.1145/3726302.3730072
    icon: "fa fa-file-pdf pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  With the rapid development of intelligent education, Computerized Adaptive Testing(CAT) has
  garnered significant attention for its ability to tailor exercises to individual examinees. The
  adaptability of CAT is primarily achieved through the alternating optimization of two core
  components: the cognitive diagnosis model and the exercise selection module. However, existing
  CAT approaches, de- spite their remarkable achievements, often come at the expense of high time
  costs. Statistical-based approaches incur increased time overhead due to complex computations,
  while data-driven approaches further exacerbate time inefficiency because of the iter- ative
  processes in reinforcement learning, making it challenging to balance evaluation effectiveness
  and time efficiency. To this end, in this paper, we propose HashCAT, an efficient CAT approach
  based on learning to hash, aiming to balance efficiency and evalu- ation effectiveness. Our
  approach comprises two stages: the hash representation generation and the exercise selection. In
  the first ∗Corresponding author Permission to make digital or hard copies of all or part of this
  work for personal or classroom use is granted without fee provided that copies are not made or
  distributed for profit or commercial advantage and that copies bear this notice and the full
  citation on the first page. Copyrights for components of this work owned by others than the
  author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
  republish, to post on servers or to redistribute to lists, requires prior specific permission
  and/or a fee. Request permissions from permissions@acm.org. SIGIR ’25, Padua, Italy © 2025
  Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN
  979-8-4007-1592-1/2025/07 https://doi.org/10.1145/3726302.3730072 stage, we design an
  information alignment module and a novel cognitive diagnosis function to model the interaction
  between ex- aminees and exercises, generating hash representations with clear physical
  significance. In the second stage, we propose an uncer- tainty reduction-based algorithm that
  utilize information entropy to quantify the uncertainty in student ability estimation and
  selects exercises that most effectively reduce this uncertainty. Experimen- tal results on four
  real-world datasets demonstrate that the pro- posed method significantly improves question
  selection efficiency while maintaining competitive evaluation performance. The code exists
  anonymously in https://github.com/sherklock/Intelligent- Education/tree/main/HashCAT-main.
bibtex: >-
  @inproceedings{ma2025reconciling,
    title   = {Reconciling Efficiency and Effectiveness of Exercise Retrieval: An Uncertainty Reduction Hashing Approach for Computerized Adaptive Testing},
    author  = {Ma, Haiping and Zhou, Yang and Yu, Xiaoshan and Wang, Changqian and Yang*, Shangshang and Zhang, Limiao and Zhang, Xingyi},
    booktitle = {ACM SIGIR Conference on Research and Development in Information Retrieval},
    pages   = {1044--1054},
    year    = {2025},
    doi     = {10.1145/3726302.3730072}
  }
---

## Contributions

- Proposes HashCAT, an efficient CAT approach based on learning to hash, reconciling evaluation effectiveness with time efficiency.
- Encodes exercises and examinees into compact hash codes so that exercise selection reduces to fast hashing-based retrieval.
- Removes the heavy iterative computation of statistical and reinforcement-learning-based selection modules.

## Method

![Framework of the proposed method](/assets/img/paper_method/ma2025reconciling.jpg){: .img-fluid .shadow-sm .rounded }

An uncertainty-reduction hashing objective trains binary representations under which the expected information gain of candidate exercises is preserved; at test time the next exercise is retrieved via Hamming-distance lookup instead of exhaustively scoring the item bank.

## Experimental Results

![Main experimental results](/assets/img/paper_results/ma2025reconciling.jpg){: .img-fluid .shadow-sm .rounded }

**Compared algorithms:** Statistical selectors (MKLI, MAAT, BECAT) and data-driven selectors (GMOCAT, BOCAT, NCAT, UATS).

**Datasets:** NIPS-2020, JUNYI, ASSIST2012, and PTADISC.

**Metrics:** ACC, AUC, and per-exercise selection latency.

**Overall results:** HashCAT keeps accuracy close to the best baselines while cutting selection time by an order of magnitude; several baselines are even too slow to record at step-20.
