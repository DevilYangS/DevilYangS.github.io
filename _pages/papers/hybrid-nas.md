---
layout: paper
permalink: /papers/hybrid-nas/
nav: false
paper_title: "Hybrid Architecture-based Evolutionary Robust Neural Architecture Search"
authors:
  - name: Shangshang Yang
    me: true
  - name: Xiangkun Sun
  - name: Ke Xu
  - name: Yuanchao Liu
  - name: Ye Tian
    star: true
  - name: Xingyi Zhang
    star: true
affiliation: "IEEE Transactions on Emerging Topics in Computational Intelligence, 2024"
venue: "TETCI 2024"
teaser: /assets/img/publication_preview/yang2024hybrid.jpg
buttons:
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  The robustness of neural networks in image classification is important to resist adversarial
  attacks. Although many researchers proposed to enhance the network robustness by inventing
  network training paradigms or designing network architectures, existing approaches are mainly
  based on a single type of networks, e.g., convolution neural networks (CNNs) or vision
  Transformer (ViT). Considering a recently revealed fact that CNNs and ViT can effectively defend
  against adversarial attacks transferred from each other, this paper aims to enhance network
  robustness by designing robust hybrid architecture networks containing different types of
  networks. To this end, we propose a hybrid architecture-based evolutionary neural architecture
  search approach for robust architecture design, termed HA-ENAS. Specifically, to combine or
  aggregate different types of networks in the same network framework, a multi-stage block-wise
  hybrid architecture network is first devised as the supernet, where three types of blocks
  (called convolution blocks, Transformer blocks, multi-layer perception blocks) are further
  designed as each block's candidate, and thus a hybrid architecture-based search space is
  established for HA-ENAS; then, the robust hybrid architecture search is formulated as an
  optimization problem maximizing both clean and adversarial accuracy of architectures, and an
  efficient multi-objective evolutionary algorithm is employed to solve the problem, where a
  supernet-based retraining evaluation and a surrogate model are used to mitigate coupled weight
  influence and reduce the whole search cost. Experimental results show that the hybrid
  architectures found by the proposed HA-ENAS outperform state-of-the-art single-type
  architectures in terms of clean accuracy and adversarial accuracy under a variety of common
  attacks.
bibtex: >-
  @article{yang2024hybrid,
    title   = {Hybrid Architecture-based Evolutionary Robust Neural Architecture Search},
    author  = {Yang, Shangshang and Sun, Xiangkun and Xu, Ke and Liu, Yuanchao and Tian*, Ye and Zhang*, Xingyi},
    journal = {IEEE Transactions on Emerging Topics in Computational Intelligence},
    year    = {2024},
  }
---

## Contributions

- Proposes HA-ENAS, an evolutionary NAS approach that designs robust hybrid architectures combining CNNs and Vision Transformers.
- Exploits the fact that CNNs and ViTs effectively defend against adversarial attacks transferred from each other.
- Designs hybrid encoding and crossover/mutation operators that handle heterogeneous network blocks.

## Method

HA-ENAS defines a search space in which a single network may contain both convolutional and self-attention blocks; a multi-objective evolutionary algorithm searches for architectures balancing clean accuracy and robustness under adversarial attacks.

## Experimental Results

The evolved hybrid networks are significantly more robust than single-type CNN or ViT architectures against both white-box and transferred adversarial attacks, without sacrificing clean accuracy.
