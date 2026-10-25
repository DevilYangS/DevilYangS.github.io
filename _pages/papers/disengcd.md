---
layout: paper
permalink: /papers/disengcd/
nav: false
paper_title: "DisenGCD: A Meta Multigraph-assisted Disentangled Graph Learning Framework for Cognitive Diagnosis"
authors:
  - name: Shangshang Yang
    me: true
  - name: Mingyang Chen
  - name: Ziwen Wang
  - name: Xiaoshan Yu
  - name: Panpan Zhang
  - name: Haiping Ma
    star: true
  - name: Xingyi Zhang
affiliation: "Advances in Neural Information Processing Systems 37 (NeurIPS), 2024"
venue: "NeurIPS 2024"
teaser: /assets/img/publication_preview/yang2024disengcd.jpg
buttons:
  - label: Paper
    url: https://proceedings.neurips.cc/paper_files/paper/2024/hash/a69d7f3a1340d55c720e572742439eaf-Abstract-Conference.html
    icon: "fa fa-file-pdf pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  Existing graph learning-based cognitive diagnosis (CD) methods have made relatively good
  results, but their student, exercise, and concept representations are learned and exchanged in
  an implicit unified graph, which makes the interaction-agnostic exercise and concept
  representations be learned poorly, failing to provide high robustness against noise in students'
  interactions. Besides, lower-order exercise latent representations obtained in shallow layers
  are not well explored when learning the student representation. To tackle the issues, this paper
  suggests a meta multigraph-assisted disentangled graph learning framework for CD (DisenGCD),
  which learns three types of representations on three disentangled graphs:
  student-exercise-concept interaction, exercise-concept relation, and concept dependency graphs,
  respectively. Specifically, the latter two graphs are first disentangled from the interaction
  graph. Then, the student representation is learned from the interaction graph by a devised meta
  multigraph learning module; multiple learnable propagation paths in this module enable current
  student latent representation to access lower-order exercise latent representations, which can
  lead to more effective nad robust student representations learned; the exercise and concept
  representations are learned on the relation and dependency graphs by graph attention modules.
  Finally, a novel diagnostic function is devised to handle three disentangled representations for
  prediction. Experiments show better performance and robustness of DisenGCD than state-of-the-art
  CD methods and demonstrate the effectiveness of the disentangled learning framework and meta
  multigraph module. The source code is available at
  https://github.com/BIMK/Intelligent-Education/tree/main/DisenGCD.
bibtex: >-
  @inproceedings{yang2024disengcd,
    title   = {DisenGCD: A Meta Multigraph-assisted Disentangled Graph Learning Framework for Cognitive Diagnosis},
    author  = {Yang, Shangshang and Chen, Mingyang and Wang, Ziwen and Yu, Xiaoshan and Zhang, Panpan and Ma*, Haiping and Zhang, Xingyi},
    booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},
    year    = {2024},
  }
---

## Contributions

- Proposes DisenGCD, which learns student, exercise, and concept representations on three disentangled graphs instead of one implicit unified graph.
- Introduces a meta multigraph-assisted learning mechanism that disentangles the exercise–concept relation graph and concept dependency graph from the interaction graph.
- Substantially improves robustness against noise in student interactions.

## Method

DisenGCD first separates the interaction graph into three task-specific graphs, learns representations on each with dedicated graph neural networks, and uses a meta-learning scheme to fuse the exercise/concept representations into the student representation, so that lower-order information is fully exploited and noise in interactions is filtered out.

## Experimental Results

DisenGCD achieves state-of-the-art diagnosis accuracy on multiple real-world datasets and shows markedly better robustness when interaction records are corrupted by noise.
