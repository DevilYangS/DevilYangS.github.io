---
layout: paper
permalink: /papers/kan-ncd/
nav: false
paper_title: "Endowing Interpretability for Neural Cognitive Diagnosis by Efficient Kolmogorov-Arnold Networks"
authors:
  - name: Shangshang Yang
    me: true
  - name: Linrui Qin
  - name: Xiaoshan Yu
  - name: Ziwen Wang
  - name: Xueming Yan
  - name: Haiping Ma
  - name: Ye Tian
affiliation: "Proceedings of the 34th International Joint Conference on Artificial Intelligence (IJCAI), 2025"
venue: "IJCAI 2025"
teaser: /assets/img/publication_preview/yang2025kan.jpg
buttons:
  - label: Paper
    url: https://www.ijcai.org/proceedings/2025/878
    icon: "fa fa-file-pdf pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  Cognitive diagnosis is crucial for intelligent education because of its ability to reveal
  students' proficiency in knowledge concepts. Although neural network-based neural cognitive
  diagnosis models (CDMs) have exhibited significantly better performance than traditional models,
  neural cognitive diagnosis is criticized for the poor model interpretability due to the
  multi-layer perceptron(MLP) employed, even with the monotonicity assumption. Therefore, this
  paper proposes to empower the interpretability of neural cognitive diagnosis models through
  efficient Kolmogorov-Arnold networks (KANs), named KAN2CD, where KANs are used to enhance
  interpretability in two manners. Specifically, in the first manner, KANs are directly used to
  replace the used MLPs in existing neural CDMs; while in the second manner, the student
  embedding, exercise embedding, and concept embedding are directly processed by several KANs, and
  then their outputs are further combined and learned in a unified KAN to get final predictions.
  Besides, the implementation of original KANs is modified without affecting the interpretability
  to overcome the problem of training KANs slowly. Extensive experiments show KAN2CD outperforms
  traditional CDMs and slightly surpasses existing neural CDMs, and its learned structures ensure
  interpretability on par with traditional CDMs and better than neural CDMs. The datasets,
  associated code, and more experimental results are available at
  https://github.com/null233QAQ/KAN2CD.
bibtex: >-
  @inproceedings{yang2025kan,
    title   = {Endowing Interpretability for Neural Cognitive Diagnosis by Efficient Kolmogorov-Arnold Networks},
    author  = {Yang, Shangshang and Qin, Linrui and Yu, Xiaoshan and Wang, Ziwen and Yan, Xueming and Ma, Haiping and Tian, Ye},
    booktitle = {Proceedings of the 34th International Joint Conference on Artificial Intelligence},
    year    = {2025},
  }
---

## Contributions

- Proposes KAN2CD, which empowers the interpretability of neural cognitive diagnosis models via efficient Kolmogorov–Arnold Networks (KANs).
- Explores two complementary manners: directly replacing MLPs in existing neural CDMs, and processing student/exercise/concept embeddings with KANs.
- Retains the monotonicity assumption while making the diagnosis process visually interpretable.

## Method

![Framework of the proposed method](/assets/img/publication_preview/yang2025kan.jpg){: .img-fluid .shadow-sm .rounded }

KANs replace the black-box MLPs in neural CDMs with learnable activation functions on edges, so that the contribution of each knowledge concept to the predicted response can be read off directly from the learned functions; two integration schemes cover both drop-in replacement and embedding-level processing.

## Experimental Results

![Main experimental results](/assets/img/paper_results/yang2025kan.jpg){: .img-fluid .shadow-sm .rounded }

Table 1 reports overall comparison against four traditional models (IRT, MIRT, DINA, MF) and eight neural CDMs (NCD/NCD+, KaNCD/KaNCD+, RCD/RCD+, KSCD/KSCD+) on four datasets (Assistments, SLP, JunYi, FreSub) in AUC/ACC. KAN2CD-e ranks best or second-best on nearly all datasets while keeping the diagnosis process interpretable.
