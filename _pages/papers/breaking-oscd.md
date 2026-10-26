---
layout: paper
permalink: /papers/breaking-oscd/
nav: false
paper_title: "Breaking Robustness Barriers in Cognitive Diagnosis: A One-Shot Neural Architecture Search Perspective"
authors:
  - name: Ziwen Wang
  - name: Shangshang Yang
    me: true
    star: true
  - name: Xiaoshan Yu
  - name: Haiping Ma
  - name: Xingyi Zhang
affiliation: "ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2026"
venue: "KDD 2026"
teaser: /assets/img/publication_preview/wang2026breaking.jpg
buttons:
  - label: PDF
    url: /assets/pdf/wang2026breaking.pdf
    icon: "fa fa-file-pdf pr-1"
  - label: Paper
    url: https://dl.acm.org/doi/abs/10.1145/3770854.3780159
    icon: "fa fa-file-pdf pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  With the advancement of network technologies, intelligent tutor- ing systems (ITS) have emerged
  to deliver increasingly precise and tailored personalized learning services. Cognitive diagnosis
  (CD) has emerged as a core research task in ITS, aiming to infer learn- ers’ mastery of specific
  knowledge concepts by modeling the map- ping between learning behavior data and knowledge
  states. How- ever, existing research prioritizes model performance enhancement while neglecting
  the pervasive noise contamination in observed response data, significantly hindering practical
  deployment. Fur- thermore, current cognitive diagnosis models (CDMs) rely heav- ily on
  researchers’ domain expertise for structural design, which fails to exhaustively explore
  architectural possibilities, thus leav- ing model architectures’ full potential untapped. To
  address this issue, we propose OSCD, an evolutionary multi-objective One- Shot neural
  architecture search method for Cognitive Diagnosis, designed to efficiently and robustly improve
  the model’s capabil- ity in assessing learner proficiency. Specifically, OSCD operates through
  two distinct stages: training and searching. During the training stage, we construct a search
  space encompassing diverse architectural combinations and train a weight-sharing supernet
  ∗Corresponding author. This work is licensed under a Creative Commons Attribution 4.0
  International License. KDD ’26, Jeju Island, Republic of Korea © 2026 Copyright held by the
  owner/author(s). ACM ISBN 979-8-4007-2258-5/2026/08 https://doi.org/10.1145/3770854.3780159
  represented via the complete binary tree topology, enabling com- prehensive exploration of
  potential architectures beyond manual design priors. In the searching stage, we formulate the
  optimal architecture search under heterogeneous noise scenarios as a multi- objective
  optimization problem (MOP), and develop an optimization framework integrating a Pareto-optimal
  solution search strategy with cross-scenario performance evaluation for resolution. Exten- sive
  experiments on real-world educational datasets validate the effectiveness and robustness of the
  optimal architectures discovered by our OSCD model for CD tasks.
bibtex: >-
  @inproceedings{wang2026breaking,
    title   = {Breaking Robustness Barriers in Cognitive Diagnosis: A One-Shot Neural Architecture Search Perspective},
    author  = {Wang, Ziwen and Yang*, Shangshang and Yu, Xiaoshan and Ma, Haiping and Zhang, Xingyi},
    booktitle = {ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)},
    year    = {2026},
    doi     = {10.1145/3770854.3780159}
  }
---

## Contributions

- Identifies two long-neglected issues in cognitive diagnosis: pervasive noise contamination in observed response data, and the reliance of existing CDM architectures on manual expert design.
- Proposes OSCD, an evolutionary multi-objective one-shot neural architecture search framework that automatically designs noise-robust cognitive diagnosis models.
- Achieves a much better robustness–accuracy trade-off than handcrafted CDMs at a fraction of the search cost thanks to the one-shot paradigm.

## Method

![Framework of the proposed method](/assets/img/paper_method/wang2026breaking.jpg){: .img-fluid .shadow-sm .rounded }

OSCD trains a weight-sharing supernet of cognitive diagnosis models once, and then applies an evolutionary multi-objective search over the supernet to discover architectures that jointly optimize diagnosis accuracy and robustness against noisy response data.

## Experimental Results

![Main experimental results](/assets/img/paper_results/wang2026breaking.jpg){: .img-fluid .shadow-sm .rounded }

**Compared algorithms:** Ten handcrafted CDMs (DINA, IRT, MIRT, MF, NCD, RCD, KSCD, KaNCD, ReCD, ORCDF) and the EMO-NAS-CD search baseline.

**Datasets:** ASSIST09 and SLP-Math under four train/val/test splits (50/20/30 – 80/10/10).

**Metrics:** ACC, AUC, and RMSE.

**Overall results:** The architectures found by OSCD rank first on nearly every split and shrink the least as training data decreases; on SLP-Math OSCD variants take the best ACC/AUC in all four settings.
