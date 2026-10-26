---
layout: paper
permalink: /papers/gemonn/
nav: false
paper_title: "A Gradient-Guided Evolutionary Approach to Training Deep Neural Networks"
authors:
  - name: Shangshang Yang
    me: true
  - name: Ye Tian
    star: true
  - name: Cheng He
  - name: Xingyi Zhang
    star: true
  - name: Kan Chen Tan
  - name: Yaochu Jin
affiliation: "IEEE Transactions on Neural Networks and Learning Systems, 2021"
venue: "TNNLS 2021"
teaser: /assets/img/publication_preview/yang2021gradient.jpg
buttons:
  - label: Paper
    url: https://ieeexplore.ieee.org/abstract/document/9369973
    icon: "fa fa-file-pdf pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  It has been widely recognized that the efficient training of neural networks (NNs) is crucial to
  classification performance. While a series of gradient-based approaches have been extensively
  developed, they are criticized for the ease of trapping into local optima and sensitivity to
  hyperparameters. Due to the high robustness and wide applicability, evolutionary algorithms
  (EAs) have been regarded as a promising alternative for training NNs in recent years. However,
  EAs suffer from the curse of dimensionality and are inefficient in training deep NNs (DNNs). By
  inheriting the advantages of both the gradient-based approaches and EAs, this article proposes a
  gradient-guided evolutionary approach to train DNNs. The proposed approach suggests a novel
  genetic operator to optimize the weights in the search space, where the search direction is
  determined by the gradient of weights. Moreover, the network sparsity is considered in the
  proposed approach, which highly reduces the network complexity and alleviates overfitting.
  Experimental results on single-layer NNs, deep-layer NNs, recurrent NNs, and convolutional NNs
  (CNNs) demonstrate the effectiveness of the proposed approach. In short, this work not only
  introduces a novel approach for training DNNs but also enhances the performance of EAs in
  solving large-scale optimization problems.
bibtex: >-
  @article{yang2021gradient,
    title   = {A Gradient-Guided Evolutionary Approach to Training Deep Neural Networks},
    author  = {Yang, Shangshang and Tian*, Ye and He, Cheng and Zhang*, Xingyi and Tan, Kan Chen and Jin, Yaochu},
    journal = {IEEE Transactions on Neural Networks and Learning Systems},
    volume   = {33},
    number   = {9},
    pages   = {4861--4875},
    year    = {2021},
  }
---

## Contributions

- Proposes GEMONN, a gradient-guided evolutionary approach for training deep neural networks that inherits the robustness of EAs and the efficiency of gradients.
- Designs a novel genetic operator whose search direction is determined by the gradient of the weights.
- Avoids the local optima and hyperparameter sensitivity of pure gradient descent, as well as the curse of dimensionality of pure EAs.

## Method

![Framework of the proposed method](/assets/img/publication_preview/yang2021gradient.jpg){: .img-fluid .shadow-sm .rounded }

GEMONN maintains a population of weight vectors and, at each generation, uses back-propagated gradients to bias the variation operator: offspring weights are perturbed along gradient-informed directions while the population mechanism preserves diversity to escape local optima.

## Experimental Results

![Main experimental results](/assets/img/paper_results/yang2021gradient.jpg){: .img-fluid .shadow-sm .rounded }

**Compared algorithms:** Four SAE trainers (EUDNN, SSAE, SCAE, SDAE) for stacked autoencoders, and SGD/Adam-trained LSTMs.

**Datasets:** Ten image benchmarks (MNIST variants, Rectangles, Convex, Cifar10-bw).

**Metrics:** Correct classification rate (CCR).

**Overall results:** GEMONN obtains the best CCR on nearly all ten SAE benchmarks and the largest average CCR on four of six LSTM datasets, validating the gradient-guided genetic operator.
