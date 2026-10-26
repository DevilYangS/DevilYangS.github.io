---
layout: paper
permalink: /papers/mfeas-nas/
nav: false
paper_title: "Accelerating Evolutionary Neural Architecture Search via Multi-Fidelity Evaluation"
authors:
  - name: Shangshang Yang
    me: true
  - name: Ye Tian
  - name: Xiaoshu Xiang
    star: true
  - name: Shicheng Peng
  - name: Xingyi Zhang
    star: true
affiliation: "IEEE Transactions on Cognitive and Developmental Systems, 2022"
venue: "TCDS 2022"
teaser: /assets/img/publication_preview/yang2022accelerating.jpg
buttons:
  - label: PDF
    url: /assets/pdf/yang2022accelerating.pdf
    icon: "fa fa-file-pdf pr-1"
  - label: Paper
    url: https://ieeexplore.ieee.org/abstract/document/9786036
    icon: "fa fa-file-pdf pr-1"
  - label: Code
    url: https://github.com/DevilYangS/MFENAS
    icon: "fab fa-github pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
award: Best Poster Paper
award_img: /assets/img/awards/ahsai2022_poster.jpg
abstract: >
  Evolutionary neural architecture search (ENAS) has recently received increasing attention by
  effectively ﬁnd- ing high-quality neural architectures, which however consumes high
  computational cost by training the architecture encoded by each individual for complete epochs
  in individual evalua- tion. Numerous ENAS approaches have been developed to reduce the
  evaluation cost, but it is often difﬁcult for most of these approaches to achieve high
  evaluation accuracy. To address this issue, in this article, we propose an accelerated ENAS via
  multiﬁdelity evaluation termed MFENAS, where the individual evaluation cost is signiﬁcantly
  reduced by training the archi- tecture encoded by each individual for only a small number of
  epochs. The balance between evaluation cost and evaluation accuracy is well maintained by
  suggesting a multiﬁdelity evalua- tion, which identiﬁes the potentially good individuals that
  cannot survive from previous generations by integrating multiple eval- uations under different
  numbers of training epochs. Besides, a population initialization strategy is devised to produce
  diverse neural architectures varying from ResNet-like architectures to Inception-like ones. As
  shown by experiments, the proposed MFENAS takes only 0.6 GPU days to ﬁnd the best archi- tecture
  holding a 2.39% test error rate, which is superior to most state-of-the-art neural architecture
  search approaches. And the architectures transferred to CIFAR-100 and ImageNet also exhibit
  competitive performance.
bibtex: >-
  @article{yang2022accelerating,
    title   = {Accelerating Evolutionary Neural Architecture Search via Multi-Fidelity Evaluation},
    author  = {Yang, Shangshang and Tian, Ye and Xiang*, Xiaoshu and Peng, Shicheng and Zhang*, Xingyi},
    journal = {IEEE Transactions on Cognitive and Developmental Systems},
    volume   = {14},
    number   = {4},
    pages   = {1778--1792},
    year    = {2022},
  }
---

## Contributions

- Proposes MFENAS, which accelerates evolutionary NAS by training each architecture for only a small number of epochs.
- Designs a multi-fidelity evaluation strategy that identifies potentially good individuals from low-fidelity evaluations.
- Well maintains the balance between evaluation cost and evaluation accuracy.

## Method

![Framework of the proposed method](/assets/img/paper_method/yang2022accelerating.jpg){: .img-fluid .shadow-sm .rounded }

Instead of fully training every individual, MFENAS evaluates architectures at low fidelity (few epochs) and uses a selection mechanism that promotes individuals whose early-training performance indicates high final quality; only the most promising architectures are trained at higher fidelity.

## Experimental Results

![Main experimental results](/assets/img/paper_results/yang2022accelerating.jpg){: .img-fluid .shadow-sm .rounded }

**Compared algorithms:** 22 peer competitors: manual designs, RL-based (NASNet-A, NASBOT), gradient-based (DARTS, SNAS), and evolutionary (AmoebaNet-A, Genetic-CNN, AE-CNN) approaches.

**Datasets:** CIFAR-10.

**Metrics:** Test error, number of parameters, and search cost (GPU-days).

**Overall results:** MFENAS attains the lowest test error (2.39%) with only 0.6 GPU-days of search cost.
