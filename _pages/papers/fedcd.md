---
layout: paper
permalink: /papers/fedcd/
nav: false
paper_title: "FedCD: A Fairness-aware Federated Cognitive Diagnosis Framework"
authors:
  - name: Shangshang Yang
    me: true
  - name: Jialin Han
  - name: Xiaoshan Yu
  - name: Ziwen Wang
  - name: Hao Jiang
  - name: Haiping Ma
    star: true
  - name: Xingyi Zhang
  - name: Geyong Min
affiliation: "ACM Transactions on Information Systems, 2026"
venue: "TOIS 2026"
teaser: /assets/img/publication_preview/yang2026fedcd.jpg
buttons:
  - label: PDF
    url: /assets/pdf/yang2026fedcd.pdf
    icon: "fa fa-file-pdf pr-1"
  - label: Paper
    url: https://doi.org/10.1145/3860629
    icon: "fa fa-file-pdf pr-1"
  - label: arXiv
    url: https://arxiv.org/abs/2508.01296
    icon: "ai ai-arxiv pr-1"
  - label: Code
    url: https://github.com/MamboAuto/FedCD
    icon: "fab fa-github pr-1"
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  With the rapid development of Internet technologies, online intelligent education platforms
  have generated a vast amount of distributed student learning data. This influx of data
  presents opportunities for cognitive diagnosis (CD) to assess students' mastery of knowledge
  concepts while also raising significant data privacy and security challenges. To cope with
  this issue, federated learning (FL) becomes a promising solution by jointly training models
  across multiple local clients without sharing their original data. However, the data quality
  problem, caused by the ability differences and educational context differences between
  different groups/schools of students, further poses a challenge to the client fairness of
  models. To address this challenge, this paper proposes a fairness-aware federated cognitive
  diagnosis framework (FedCD) to jointly train CD models built upon a novel parameter
  decoupling-based personalization strategy, preserving privacy of data and achieving precise
  and fair diagnosis of students on each client. As an FL paradigm, FedCD trains a local CD
  model for the students in each client based on its local student learning data, and each
  client uploads its partial model parameters to the central server for parameter aggregation
  according to the devised innovative personalization strategy. The main idea of this strategy
  is to decouple model parameters into two parts: the first is used as locally personalized
  parameters, containing diagnostic function-related model parameters, to diagnose each
  client's students fairly; the second is the globally shared parameters across clients and
  the server, containing exercise embedding parameters, which are updated via fairness-aware
  aggregation, to alleviate inter-school unfairness. Experiments on three real-world datasets
  demonstrate the effectiveness of the proposed FedCD framework and the personalization
  strategy compared to five FL approaches under three CD models.
bibtex: >-
  @article{yang2026fedcd,
    title   = {FedCD: A Fairness-aware Federated Cognitive Diagnosis Framework},
    author  = {Yang, Shangshang and Han, Jialin and Yu, Xiaoshan and Wang, Ziwen and Jiang, Hao and Ma*, Haiping and Zhang, Xingyi and Min, Geyong},
    journal = {ACM Transactions on Information Systems},
    year    = {2026},
    doi     = {10.1145/3860629}
  }
---

## Contributions

- Proposes **FedCD**, a fairness-aware federated cognitive diagnosis framework that jointly trains CD models across schools/clients without sharing raw student learning data.
- Devises a **parameter decoupling-based personalization strategy**: student embeddings and the diagnostic function stay locally personalized, while exercise embeddings are globally shared across clients and the server.
- Designs a **fairness-aware aggregation** mechanism that weights clients by their local prediction loss, alleviating inter-school unfairness caused by data-quality differences.
- Validates the framework on three real-world datasets under three base CD models against five FL baselines, showing superior accuracy and fairness.

## Method

![Overview of FedCD](/assets/img/paper_method/yang2026fedcd.jpg){: .img-fluid .shadow-sm .rounded }

Each communication round consists of four steps: ① each school/client trains its own CD model, initializing its local exercise embedding with the globally shared embeddings, and computes the predicted loss on local students; ② each client uploads only its exercise embedding to the central server; ③ the server determines aggregation weights in a fairness-aware manner (loss-based weighting) and aggregates the local exercise embeddings into a global exercise embedding; ④ the server distributes the global exercise embedding back to all clients, while student embeddings and the diagnostic function never leave the client.

## Experimental Results

![Performance comparison on ASSIST2009](/assets/img/paper_results/yang2026fedcd.jpg){: .img-fluid .shadow-sm .rounded }

**Compared algorithms:** Five federated learning approaches &mdash; FedAvg, FedAtt, LoAdaBoost, F2MF, and PFedRec &mdash; under three base CD models (DINA, NCD, and KaNCD), plus GUM with HPFL.

**Datasets:** Three real-world datasets &mdash; ASSIST2009, ASSIST2012, and SLP-Math &mdash; under 60%/40%, 70%/30%, and 80%/20% train/test ratios.

**Metrics:** Diagnosis ACC, RMSE, and AUC, together with group fairness (GF) and degree of agreement (DOA) for fairness evaluation.

**Overall results:** FedCD achieves the best ACC/RMSE/AUC in most settings (e.g., it wins 27 out of 30 comparisons against FedAvg on ASSIST2009), and substantially reduces the performance disparity across schools with different data qualities, confirming both the diagnosis precision and the client fairness of the framework.
