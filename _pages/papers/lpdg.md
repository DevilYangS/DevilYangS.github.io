---
layout: paper
permalink: /papers/lpdg/
nav: false
paper_title: "Learning Patterns-Guided Data Generation for Knowledge Tracing"
authors:
  - name: Haiping Ma
  - name: Yu Yin
  - name: Ziwen Wang
  - name: Changqian Wang
  - name: Xiaoshan Yu
  - name: Shangshang Yang
    me: true
    star: true
  - name: Xingyi Zhang
affiliation: "ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD), 2025"
venue: "KDD 2025"
teaser: /assets/img/publication_preview/ma2025patterns.jpg
buttons:
  - label: Paper
    url: https://dl.acm.org/doi/10.1145/3711896.3737021
    icon: "fa fa-file-pdf pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  Knowledge tracing (KT), which is instrumental in monitoring and forecasting students' knowledge
  states throughout their learning trajectory in online learning environments, has over the past
  decade garnered widespread attention due to its pivotal role in facilitating personalized
  education. Existing KT approaches were mainly invented from the model-centric perspective to
  overcome the sequence modeling difficulty while not exploiting the potential information of
  sparsity, thereby limiting their performance. To make full use of the information in the
  dataset, this paper proposes a data-centric knowledge tracing paradigm, termed LPDG, aiming to
  generate interaction data between students and exercises by revealing students' Learning
  Patterns and facilitating the Generation of ideal training Data. Specifically, we propose a
  learning patterns-guided exercise sequence regenerator, which incorporates Transformer and a
  tailor-made pattern enhancer, thereby aiding in the extraction of valuable information for
  generating high-quality training data. Moreover, we devise a learning patterns-guided
  pseudo-label generator, which leverages the diffusion process to construct pseudo-labels for the
  regenerated sequences. Afterwards, the fully generated ideal data is incorporated into the
  training data, and we integrate this framework with various model-centric approaches in KT.
  Finally, experimental results across datasets clearly demonstrate the efficacy of our proposed
  LPDG framework.
bibtex: >-
  @inproceedings{ma2025patterns,
    title   = {Learning Patterns-Guided Data Generation for Knowledge Tracing},
    author  = {Ma, Haiping and Yin, Yu and Wang, Ziwen and Wang, Changqian and Yu, Xiaoshan and Yang*, Shangshang and Zhang, Xingyi},
    booktitle = {ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)},
    pages   = {2031--2041},
    year    = {2025},
    doi     = {10.1145/3711896.3737021}
  }
---

## Contributions

- Shifts knowledge tracing from a model-centric to a data-centric paradigm: generating ideal training data by revealing students' learning patterns.
- Proposes a learning-patterns-guided exercise sequence regenerator that produces high-quality interaction data.
- Substantially mitigates the sparsity problem of student–exercise interaction datasets.

## Method

![Framework of the proposed method](/assets/img/publication_preview/ma2025patterns.jpg){: .img-fluid .shadow-sm .rounded }

LPDG first mines recurrent learning patterns from historical interaction sequences, then uses these patterns to guide a sequence regeneration model that synthesizes plausible student–exercise interactions, augmenting sparse training data with pattern-consistent samples.

## Experimental Results

![Main experimental results](/assets/img/paper_results/ma2025patterns.jpg){: .img-fluid .shadow-sm .rounded }

**Compared algorithms:** Mainstream KT backbones each trained with and without LPDG, together with other data-augmentation strategies.

**Datasets:** Three real-world knowledge tracing datasets.

**Metrics:** Response-prediction accuracy (AUC/ACC).

**Overall results:** Plugging LPDG consistently improves prediction accuracy across all backbones and clearly outperforms other augmentation strategies.
