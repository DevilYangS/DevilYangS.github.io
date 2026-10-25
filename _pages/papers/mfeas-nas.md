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
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
award: Best Poster Paper
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
  competitive performance. Manuscript received 7 November 2021; revised 17 February 2022 and 13
  April 2022; accepted 28 May 2022. Date of publication 1 June 2022; date of current version 9
  December 2022. This work was supported in part by the National Key Research and Development
  Project under Grant 2018AAA0100105 and Grant 2018AAA0100100; in part by the National Natural
  Science Foundation of China under Grant 61822301, Grant 61876123, Grant 61906001, Grant
  62136008, Grant U21A20512, and Grant U1804262; in part by the Hong Kong Scholars Program under
  Grant XJ2019035; in part by the Anhui Provincial Natural Science Foundation under Grant
  1808085J06 and Grant 1908085QF271; in part by the Collaborative Innovation Program of
  Universities in Anhui Province under Grant GXXT-2020-013; and in part by the State Key
  Laboratory of Synthetical Automation for Process Industries under Grant PAL-N201805.
  (Corresponding authors: Xiaoshu Xiang; Xingyi Zhang). Shangshang Yang, Shichen Peng, and Xingyi
  Zhang are with the Key Laboratory of Intelligent Computing and Signal Processing of Ministry of
  Education, School of Artiﬁcial Intelligence, Anhui University, Hefei 230039, China (e-mail:
  yangshang0308@gmail.com; severus.peng@gmail.com; xyzhanghust@gmail.com). Ye Tian and Xiaoshu
  Xiang are with the Key Laboratory of Intelligent Computing and Signal Processing of Ministry of
  Education, Institute of Physical Science and Information Technology, Anhui University, Hefei
  230601, China (e-mail: ﬁeld910921@gmail.com; 94xxs13@gmail.com). This article has supplementary
  material provided by the authors and color versions of one or more ﬁgures available at
  https://doi.org/10.1109/TCDS.2022.3179482. Digital Object Identiﬁer 10.1109/TCDS.2022.3179482
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

Instead of fully training every individual, MFENAS evaluates architectures at low fidelity (few epochs) and uses a selection mechanism that promotes individuals whose early-training performance indicates high final quality; only the most promising architectures are trained at higher fidelity.

## Experimental Results

MFENAS finds architectures of comparable or better quality than full-evaluation ENAS at a significantly lower total computational cost on standard NAS benchmarks.
