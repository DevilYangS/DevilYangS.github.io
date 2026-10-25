---
layout: paper
permalink: /papers/isr-moea/
nav: false
paper_title: "An indexed set representation based multi-objective evolutionary approach for mining diversified top-k high utility patterns"
authors:
  - name: Lei Zhang
  - name: Shangshang Yang
    me: true
  - name: Xinpeng Wu
  - name: Fan Cheng
    star: true
  - name: Ying Xie
  - name: Zhiting Lin
affiliation: "Engineering Applications of Artificial Intelligence, 2019"
venue: "EAAI 2019"
teaser: /assets/img/publication_preview/zhang2019indexed.jpg
buttons:
  - label: Homepage
    url: /
    icon: "fa fa-home pr-1"
abstract: >
  How to discover top-k patterns with the largest utility values, namely, mining top-k high
  utility patterns, is a hot topic in data mining. However, most of the existing works for mining
  top-k high utility patterns consider each pattern separately during the mining process, thus
  many mined patterns are highly similar and lack diversity. In this paper, we propose to mine
  top-k high utility patterns with high diversity for enhancing users satisfaction in
  recommendation. Specifically, we first introduce a simple measure of coverage to quantify the
  diversity of the whole set, that is, the top-k patterns as a complete entity. Then we propose an
  indexed set representation based multi-objective evolutionary approach named ISR-MOEA to mine
  diversified top-k high utility patterns, due to the fact that the two measures utility and
  coverage are conflicting. In ISR-MOEA, an indexed set individual representation scheme is
  suggested for fast encoding and decoding the top-k pattern set. Experimental results on six
  real-world and two synthetic datasets demonstrate the effectiveness of the proposed approach.
  The proposed approach can obtain several groups of top-k pattern set with different trade-offs
  between utility and diversity in only one run, which would further enhance the satisfaction of
  users.
bibtex: >-
  @article{zhang2019indexed,
    title   = {An indexed set representation based multi-objective evolutionary approach for mining diversified top-k high utility patterns},
    author  = {Zhang, Lei and Yang, Shangshang and Wu, Xinpeng and Cheng*, Fan and Xie, Ying and Lin, Zhiting},
    journal = {Engineering Applications of Artificial Intelligence},
    volume   = {77},
    pages   = {9--20},
    year    = {2019},
  }
---

## Contributions

- Introduces mining of diversified top-k high utility patterns, adding a coverage measure that quantifies the diversity of the whole top-k set.
- Proposes ISR-MOEA, a bi-objective (utility vs. coverage) evolutionary approach with an indexed set individual representation for fast encoding/decoding.
- Obtains multiple trade-off pattern sets with different utility–diversity balances in a single run.

## Method

ISR-MOEA encodes a complete top-k pattern set as one individual using an indexed set representation, and evolves a population under the conflicting objectives of total utility and coverage, returning a Pareto front of diversified recommendation sets.

## Experimental Results

On six real-world and two synthetic datasets, ISR-MOEA mines pattern sets with clearly higher diversity at comparable utility than single-objective top-k miners, improving user satisfaction in recommendation.
