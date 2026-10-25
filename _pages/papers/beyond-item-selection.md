---
layout: paper
permalink: /papers/beyond-item-selection/
nav: false
paper_title: "Beyond Item Selection: Rethinking Ability Evolution in Computerized Adaptive Testing"
authors:
  - name: Xiaoshan Yu
  - name: Jing Li
  - name: Shangshang Yang
    me: true
    star: true
  - name: Ziwen Wang
  - name: Haiping Ma
  - name: Xingyi Zhang
affiliation: "ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2026"
venue: "KDD 2026"
teaser: /assets/img/publication_preview/yu2026beyond.jpg
buttons:
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  Computerized Adaptive Testing (CAT), as a core assessment technique in intelligent education,
  aims to enhance the efficiency and precision of learner evaluation by adaptively selecting
  questions that best align with the examinee's current knowledge state. Indeed, recent years have
  witnessed substantial progress in the design and refinement of the fundamental cognitive
  diagnosis models and the question selection strategies, leading to promising results. However,
  the evolutionary dynamics of examinee abilities and the underlying updating mechanisms
  throughout the adaptive testing process have received limited attention. To this end, this paper
  investigates the impact of update mechanisms with varying granularities on the accuracy of
  ability estimation, with a particular focus on step-based and batch-based strategies in the
  context of assessment diagnosis. Specifically, we begin by conducting an approximation analysis
  to compare the changes in ability estimates induced by the two strategies, followed by a
  theoretical analysis of their update trajectories through the lens of error bounds. To trade-off
  the adaptability and stability during the assessment process, we propose SUAT, a Smooth-step
  Updating strategy for more effective Adaptive Testing. Finally, we conduct extensive experiments
  on two real-world educational datasets of varying scales, and provide a detailed analysis and
  discussion of the differences among the different update mechanisms, and their potential
  applications.
bibtex: >-
  @inproceedings{yu2026beyond,
    title   = {Beyond Item Selection: Rethinking Ability Evolution in Computerized Adaptive Testing},
    author  = {Yu, Xiaoshan and Li, Jing and Yang*, Shangshang and Wang, Ziwen and Ma, Haiping and Zhang, Xingyi},
    booktitle = {ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)},
    year    = {2026},
  }
---

## Contributions

- Reveals that the granularity of ability update mechanisms (step-based vs. batch-based) has a substantial impact on ability estimation accuracy in CAT.
- Systematically analyzes the evolutionary dynamics of examinee abilities throughout the adaptive testing process.
- Provides practical guidelines for selecting update mechanisms in real-world CAT deployments.

## Method

The paper models ability estimation as a continuously evolving process during adaptive testing, and compares update mechanisms of varying granularity — updating the ability estimate after each answered item (step-based) versus after a batch of items (batch-based) — analyzing how each strategy affects the convergence and precision of ability estimation.

## Experimental Results

Experiments on assessment diagnosis tasks show that the choice of update mechanism significantly influences estimation accuracy, and the proposed analysis yields concrete recommendations that improve precision, particularly in the early stages of testing.
