---
layout: paper
permalink: /papers/eqnet/
nav: false
paper_title: "EQ-Net: Elastic Quantization Neural Networks"
authors:
  - name: Ke Xu
  - name: Lei Han
  - name: Ye Tian
  - name: Shangshang Yang
    me: true
    star: true
  - name: Xingyi Zhang
affiliation: "Proceedings of the 2023 IEEE/CVF International Conference on Computer Vision (ICCV), 2023"
venue: "ICCV 2023"
teaser: /assets/img/publication_preview/xu2023eqnet.jpg
buttons:
  - label: Paper
    url: https://ieeexplore.ieee.org/abstract/document/10378532
    icon: "fa fa-file-pdf pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  Current model quantization methods have shown their promising capability in reducing storage
  space and computation complexity. However, due to the diversity of quantization forms supported
  by different hardware, one limitation of existing solutions is that usually require repeated
  optimization for different scenarios. How to construct a model with flexible quantization forms
  has been less studied. In this paper, we explore a one-shot network quantization regime, named
  Elastic Quantization Neural Networks (EQ-Net), which aims to train a robust weight-sharing
  quantization supernet. First of all, we propose an elastic quantization space (including elastic
  bit-width, granularity, and symmetry) to adapt to various mainstream quantitative forms.
  Secondly, we propose the Weight Distribution Regularization Loss (WDR-Loss) and Group
  Progressive Guidance Loss (GPG-Loss) to bridge the inconsistency of the distribution for weights
  and output logits in the elastic quantization space gap. Lastly, we incorporate genetic
  algorithms and the proposed Conditional Quantization-Aware Accuracy Predictor (CQAP) as an
  estimator to quickly search mixed-precision quantized neural networks in supernet. Extensive
  experiments demonstrate that our EQ-Net is close to or even better than its static counterparts
  as well as state-of-the-art robust bit-width methods. Code can be available at
  https://github.com/xuke225/EQ-Net.
bibtex: >-
  @inproceedings{xu2023eqnet,
    title   = {EQ-Net: Elastic Quantization Neural Networks},
    author  = {Xu, Ke and Han, Lei and Tian, Ye and Yang*, Shangshang and Zhang, Xingyi},
    booktitle = {Proceedings of the 2023 International Conference on Computer Vision},
    year    = {2023},
  }
---

## Contributions

- Proposes EQ-Net, a one-shot quantization regime that trains a robust weight-sharing supernet supporting elastic quantization forms.
- Defines an elastic quantization space covering bit-width, granularity, and symmetry to adapt to diverse hardware.
- Introduces WDR-Loss and GPG-Loss to bridge the inconsistency between sub-networks and the supernet.

## Method

![Framework of the proposed method](/assets/img/publication_preview/xu2023eqnet.jpg){: .img-fluid .shadow-sm .rounded }

EQ-Net trains a single weight-sharing quantization supernet in which each sub-network can choose its own bit-width, quantization granularity, and symmetry; two regularization losses align the weight distributions and progressively guide sub-networks so that all quantization configurations remain accurate after a single training run.

## Experimental Results

![Main experimental results](/assets/img/paper_results/xu2023eqnet.jpg){: .img-fluid .shadow-sm .rounded }

Table 2 compares EQ-Net with state-of-the-art quantization approaches (LSQ, EdMIPS, RobustQ, AutoPress, MultiQuant, HAQ) on ResNet18/50, MobileNetV2, and EfficientNetB0 over ImageNet Top-1 accuracy. EQ-Net delivers the best or comparable accuracy at every bit-width with a single training run, e.g., 67.6% Top-1 at 2-bit on ResNet18.
