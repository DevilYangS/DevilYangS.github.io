---
layout: paper
permalink: /papers/peoat/
nav: false
paper_title: "PEOAT: Personalization-Guided Evolutionary Question Assembly for One-Shot Adaptive Testing"
authors:
  - name: Xiaoshan Yu
  - name: Ziwei Huang
  - name: Shangshang Yang
    me: true
    star: true
  - name: Ziwen Wang
  - name: Haiping Ma
  - name: Xingyi Zhang
affiliation: "Proceedings of the Fortieth AAAI Conference on Artificial Intelligence (AAAI), 2026"
venue: "AAAI 2026"
buttons:
  - label: Paper
    url: https://ojs.aaai.org/index.php/AAAI/article/view/40022
    icon: "fa fa-file-pdf pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  With the rapid advancement of intelligent education, Computerized Adaptive Testing (CAT) has
  attracted increasing attention by integrating educational psychology with deep learning
  technologies. Unlike traditional paper-and-pencil testing, CAT aims to efficiently and
  accurately assess examinee abilities by adaptively selecting the most suitable items during the
  assessment process. However, its real-time and sequential nature presents limitations in
  practical scenarios, particularly in large-scale assessments where interaction costs are high,
  or in sensitive domains such as psychological evaluations where minimizing noise and
  interference is essential. These challenges constrain the applicability of conventional CAT
  methods in time-sensitive or resourceconstrained environments. To this end, we first introduce a
  novel task called one-shot adaptive testing (OAT), which aims to select a fixed set of optimal
  items for each test-taker in a one-time selection. Meanwhile, we propose PEOAT, a
  Personalization-guided Evolutionary question assembly framework for One-shot Adaptive Testing
  from the perspective of combinatorial optimization. Specifically, we began by designing a
  personalization-aware initialization strategy that integrates differences between examinee
  ability and exercise difficulty, using multi-strategy sampling to construct a diverse and
  informative initial population. Building on this, we proposed a cognitive-enhanced evolutionary
  framework incorporating schema-preserving crossover and cognitively guided mutation to enable
  efficient exploration through informative signals. To maintain diversity without compromising
  fitness, we further introduced a diversity-aware environmental selection mechanism. The
  effectiveness of PEOAT is validated through extensive experiments on two datasets, complemented
  by case studies that uncovered valuable insights.
bibtex: >-
  @inproceedings{yu2026peoat,
    title   = {PEOAT: Personalization-Guided Evolutionary Question Assembly for One-Shot Adaptive Testing},
    author  = {Yu, Xiaoshan and Huang, Ziwei and Yang*, Shangshang and Wang, Ziwen and Ma, Haiping and Zhang, Xingyi},
    booktitle = {Proceedings of the Fortieth AAAI Conference on Artificial Intelligence},
    year    = {2026},
  }
---

## Contributions

- Introduces a novel task, One-shot Adaptive Testing (OAT), which selects a fixed subset of items in one shot instead of sequentially choosing items, suited for large-scale or noise-sensitive assessments.
- Proposes PEOAT, a personalization-guided evolutionary question assembly method to solve the OAT task.
- Demonstrates that a well-assembled fixed item set can approach the accuracy of fully adaptive testing at much lower interaction cost.

## Method

PEOAT formulates the selection of the fixed item set as an optimization problem and employs an evolutionary algorithm whose search is guided by personalization signals derived from examinee ability distributions, assembling a item set that covers diverse ability levels and maximizes overall assessment precision.

## Experimental Results

Experiments show that PEOAT delivers markedly better assessment accuracy than non-adaptive and random baselines, and remains competitive with sequential CAT while eliminating the need for real-time item selection.
