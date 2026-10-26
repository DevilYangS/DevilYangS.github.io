---
layout: paper
permalink: /papers/samoea-tpm/
nav: false
paper_title: "A Surrogate-Assisted Multiobjective Evolutionary Algorithm for Large-Scale Task-Oriented Pattern Mining"
authors:
  - name: Ye Tian
  - name: Shangshang Yang
    me: true
  - name: Lei Zhang
  - name: Fuchen Duan
  - name: Xingyi Zhang
    star: true
affiliation: "IEEE Transactions on Emerging Topics in Computational Intelligence, 2019"
venue: "TETCI 2019"
teaser: /assets/img/publication_preview/tian2019surrogate.jpg
buttons:
  - label: Paper
    url: https://ieeexplore.ieee.org/abstract/document/8482477
    icon: "fa fa-file-pdf pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  As a branch of frequent pattern mining, the task-oriented pattern mining has received increasing
  attention due to its broad application scenarios. The lexicographic subset tree based algorithm
  and the multiobjective evolutionary algorithm are two effective approaches for finding the most
  frequent and complete pattern in task-oriented applications. However, both suffer from heavy
  computational cost since their runtime increases rapidly as the transaction dataset is scaled
  up. To address this issue, this paper regards the task-oriented pattern mining as a data-driven
  optimization problem and solves it by using a surrogate-assisted multiobjective evolutionary
  algorithm. Based on the framework of our previous multiobjective evolutionary algorithm for
  task-oriented pattern mining, the proposed algorithm estimates the objective values of most
  solutions using an ensemble of surrogates instead of the real objective functions, thereby
  highly improving the efficiency of the algorithm. Experimental results on three task-oriented
  applications indicate that the proposed algorithm has better efficiency than state-of-the-art
  algorithms.
bibtex: >-
  @article{tian2019surrogate,
    title   = {A Surrogate-Assisted Multiobjective Evolutionary Algorithm for Large-Scale Task-Oriented Pattern Mining},
    author  = {Tian, Ye and Yang, Shangshang and Zhang, Lei and Duan, Fuchen and Zhang*, Xingyi},
    journal = {IEEE Transactions on Emerging Topics in Computational Intelligence},
    volume   = {3},
    number   = {2},
    pages   = {106--116},
    year    = {2019},
  }
---

## Contributions

- Formulates large-scale task-oriented pattern mining as a data-driven optimization problem.
- Proposes a surrogate-assisted multiobjective evolutionary algorithm (SMOEA) whose objective values of most solutions are estimated by an ensemble of surrogates.
- Reduces the heavy computational cost of lexicographic subset tree algorithms and plain MOEAs on large transaction datasets.

## Method

![Framework of the proposed method](/assets/img/publication_preview/tian2019surrogate.jpg){: .img-fluid .shadow-sm .rounded }

Building on the framework of the previous multiobjective EA for task-oriented pattern mining, SMOEA trains an ensemble of RBF surrogate models to estimate the objectives of most offspring, and evaluates only a few selected solutions with the real objective function to update the surrogates.

## Experimental Results

![Main experimental results](/assets/img/paper_results/tian2019surrogate.jpg){: .img-fluid .shadow-sm .rounded }

Fig. 4 shows the HV convergence profiles of the plain MOEA (MOPM) and its surrogate-assisted versions (SA-MOPM) on the transaction dataset with 500,000 records. The surrogate assistance accelerates convergence substantially and reaches higher final HV with far fewer real function evaluations.
