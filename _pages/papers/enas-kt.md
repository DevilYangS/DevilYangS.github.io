---
layout: paper
permalink: /papers/enas-kt/
nav: false
paper_title: "Evolutionary Neural Architecture Search for Transformer in Knowledge Tracing"
authors:
  - name: Shangshang Yang
    me: true
  - name: Xiaoshan Yu
  - name: Ye Tian
  - name: Xueming Yan
  - name: Haiping Ma
    star: true
  - name: Xingyi Zhang
    star: true
affiliation: "Advances in Neural Information Processing Systems 36 (NeurIPS), 2023"
venue: "NeurIPS 2023"
teaser: /assets/img/publication_preview/yang2023transformer.jpg
buttons:
  - label: Paper
    url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/3e53d82a1113e3d240059a9195668edc-Abstract-Conference.html
    icon: "fa fa-file-pdf pr-1"
  - label: Code
    url: https://github.com/DevilYangS/ENAS-KT
    icon: "fab fa-github pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  Knowledge tracing (KT) aims to trace students' knowledge states by predicting whether students
  answer correctly on exercises. Despite the excellent performance of existing Transformer-based
  KT approaches, they are criticized for the manually selected input features for fusion and the
  defect of single global context modelling to directly capture students' forgetting behavior in
  KT, when the related records are distant from the current record in terms of time. To address
  the issues, this paper first considers adding convolution operations to the Transformer to
  enhance its local context modelling ability used for students' forgetting behavior, then
  proposes an evolutionary neural architecture search approach to automate the input feature
  selection and automatically determine where to apply which operation for achieving the balancing
  of the local/global context modelling. In the search space, the original global path containing
  the attention module in Transformer is replaced with the sum of a global path and a local path
  that could contain different convolutions, and the selection of input features is also
  considered. To search the best architecture, we employ an effective evolutionary algorithm to
  explore the search space and also suggest a search space reduction strategy to accelerate the
  convergence of the algorithm. Experimental results on the two largest and most challenging
  education datasets demonstrate the effectiveness of the architecture found by the proposed
  approach.
bibtex: >-
  @inproceedings{yang2023transformer,
    title   = {Evolutionary Neural Architecture Search for Transformer in Knowledge Tracing},
    author  = {Yang, Shangshang and Yu, Xiaoshan and Tian, Ye and Yan, Xueming and Ma*, Haiping and Zhang*, Xingyi},
    booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},
    year    = {2023},
  }
---

## Contributions

- Enhances Transformer-based knowledge tracing with convolution operations to better model students' forgetting behavior in the local context.
- Proposes an evolutionary NAS approach that automates input feature fusion and decides where to apply which operation.
- Balances local and global context modeling automatically instead of manual feature selection.

## Method

![Framework of the proposed method](/assets/img/publication_preview/yang2023transformer.jpg){: .img-fluid .shadow-sm .rounded }

A tailored search space treats input feature selection, convolution placement, and attention configuration as genes; an evolutionary algorithm searches over this space for KT architectures whose global attention captures long-term patterns while local convolutions capture recency/forgetting effects.

## Experimental Results

![Main experimental results](/assets/img/paper_results/yang2023transformer.jpg){: .img-fluid .shadow-sm .rounded }

**Compared algorithms:** CT-NCM, SAKT, AKT, SAINT/SAINT+, and the NAS-Cell baseline.

**Datasets:** EdNet.

**Metrics:** AUC and model size (number of parameters).

**Overall results:** The searched models reach 0.8021–0.8059 AUC, consistently above all handcrafted baselines, while using far fewer parameters than SAINT+ (more) (e.g., 2.5M vs. 4.9M).
