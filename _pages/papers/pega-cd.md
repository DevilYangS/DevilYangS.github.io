---
layout: paper
permalink: /papers/pega-cd/
nav: false
paper_title: "Cognitive Diagnosis-Based Personalized Exercise Group Assembly via a Multi-Objective Evolutionary Algorithm"
authors:
  - name: Shangshang Yang
    me: true
  - name: Haoyu Wei
  - name: Haiping Ma
    star: true
  - name: Ye Tian
  - name: Xingyi Zhang
  - name: Yunbo Cao
  - name: Yaochu Jin
affiliation: "IEEE Transactions on Emerging Topics in Computational Intelligence, 2023"
venue: "TETCI 2023"
teaser: /assets/img/publication_preview/yang2023assembly.jpg
buttons:
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  Exercise group recommendation plays an important role in many intelligent education tasks.
  However, existing approaches make recommendations based on the intrinsic features of exercises
  without considering students' learning abilities, or make selections from several pre-built
  exercise groups at the expense of flexibility. Furthermore, although many cognitive diagnosis
  approaches have successfully revealed students' abilities, how to leverage the diagnosis results
  for exercise group recommendation is hardly explored. To flexibly recommend suitable exercise
  groups to students, this paper proposes to assemble personalized exercises as a group based on
  students' abilities, called Personalized Exercise Group Assembly (PEGA). To solve the PEGA task,
  we first formulate it as a constrained multi-objective problem (CMOP), where three objectives
  are designed for enabling the assembled exercises to enhance students' abilities on both weak
  and new knowledge concepts. Then, we devise an extended neural cognitive diagnosis model to
  learn student's ability/proficiency on all knowledge concepts to compute the weakness
  consolidation objective. Besides, we propose a dual-encoding and dual-population based
  co-evolutionary algorithm to tackle the CMOP, where the main population with binary encoding is
  used to search which exercises are selected, and the auxiliary population with integer encoding
  is responsible for accelerating the convergence of the main population via guiding offspring
  generation of the main population. Experiments on three popular datasets demonstrate the
  effectiveness of exercises assembled by the proposed algorithm compared to state-of-the-art
  exercise group recommendation approaches, where our assembled exercises can enhance students'
  proficiency on both poorly mastered and new knowledge concepts.
bibtex: >-
  @article{yang2023assembly,
    title   = {Cognitive Diagnosis-Based Personalized Exercise Group Assembly via a Multi-Objective Evolutionary Algorithm},
    author  = {Yang, Shangshang and Wei, Haoyu and Ma*, Haiping and Tian, Ye and Zhang, Xingyi and Cao, Yunbo and Jin, Yaochu},
    journal = {IEEE Transactions on Emerging Topics in Computational Intelligence},
    volume   = {7},
    number   = {3},
    pages   = {829--844},
    year    = {2023},
  }
---

## Contributions

- Formulates personalized exercise group assembly (PEGA) as a constrained multi-objective optimization problem driven by cognitive diagnosis results.
- Designs three objectives so that the assembled group matches the student's ability, covers target concepts, and controls redundancy.
- Solves the problem with a constrained multi-objective evolutionary algorithm with repair-based constraint handling.

## Method

Based on the diagnosed ability of each student, PEGA encodes candidate exercise groups as individuals and evolves them under constraints on group size and concept coverage; the evolutionary search returns a set of non-dominated exercise groups adapted to the student's proficiency.

## Experimental Results

Compared with rule-based and single-objective baselines, PEGA assembles exercise groups whose difficulty better matches each student's ability, leading to improved learning efficiency in simulated practice.
