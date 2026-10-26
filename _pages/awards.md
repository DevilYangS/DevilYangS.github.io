---
layout: page
title: awards
permalink: /awards/
nav: true
nav_order: 6
---

<style>
.award-group { margin-bottom: 1.2rem; }
.award-year {
  font-size: 1.02rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  color: var(--global-theme-color);
  margin-bottom: 0.35rem;
  padding-bottom: 0.15rem;
  border-bottom: 1px solid var(--global-divider-color);
}
ul.award-list { list-style: none; padding-left: 0; margin: 0; }
ul.award-list > li { position: relative; padding: 0.24rem 0 0.24rem 1rem; line-height: 1.55; }
ul.award-list > li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0.75rem;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--global-theme-color);
  opacity: 0.65;
}
/* 奖项等级：标红 + 加粗 */
.award-rank { font-weight: 700; color: var(--global-highlight-color); }
/* 授予单位 / 赛事：加粗 */
.award-org { font-weight: 600; }
/* 补充说明：弱化 */
.award-note { color: var(--global-text-color-light); font-size: 0.92em; }
/* 级别标注：加粗 + 下划线 */
.award-level {
  font-weight: 700;
  text-decoration: underline;
  text-underline-offset: 2px;
  text-decoration-thickness: 1px;
}
.award-level.national { color: var(--global-highlight-color); }
.award-level.provincial { color: #2c7be5; }
.award-level.regional { color: #1a9c6b; }
/* 证书提示角标 */
li.award-item.has-cert { cursor: pointer; border-radius: 6px; transition: background 0.15s; }
li.award-item.has-cert:hover { background: var(--global-code-background-color); }
li.award-item.has-cert:hover .award-tag { filter: brightness(1.1); }
.cert-hint {
  font-size: 0.72rem;
  color: var(--global-text-color-light);
  margin-left: 0.35rem;
  white-space: nowrap;
}
.cert-hint i { font-size: 0.74rem; }
li.award-item.has-cert:hover .cert-hint { color: var(--global-theme-color); }
/* 证书预览浮层 */
.award-preview {
  display: none;
  position: fixed;
  z-index: 9999;
  max-width: min(720px, 92vw);
  background: #fff;
  padding: 10px;
  border-radius: 12px;
  box-shadow: 0 12px 40px rgba(0,0,0,0.28);
  border: 1px solid var(--global-divider-color);
}
.award-preview img {
  display: block;
  max-width: 100%;
  max-height: 70vh;
  width: auto;
  height: auto;
  border-radius: 8px;
}
/* ===== 区块标题（字距展开，类似 F U N D I N G） ===== */
.section-title {
  font-size: 0.92rem;
  font-weight: 700;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--global-theme-color);
  border-bottom: 2px solid var(--global-divider-color);
  padding-bottom: 0.32rem;
  margin: 2.4rem 0 1.1rem;
}
/* ===== 基金卡片 ===== */
.fund-list, .patent-list { display: grid; gap: 0.55rem; }
.fund-item, .patent-item {
  background: var(--global-code-bg-color);
  border-left: 3px solid var(--global-theme-color);
  border-radius: 0 6px 6px 0;
  padding: 0.62rem 0.88rem;
  transition: box-shadow 0.16s ease, transform 0.16s ease;
}
.fund-item:hover, .patent-item:hover {
  box-shadow: 0 3px 12px rgba(0, 0, 0, 0.10);
  transform: translateY(-1px);
}
.fund-head, .patent-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 0.9rem;
  flex-wrap: wrap;
}
.fund-name, .patent-title { font-weight: 600; line-height: 1.4; }
.fund-amount {
  font-weight: 700;
  color: var(--global-highlight-color);
  white-space: nowrap;
  font-variant-numeric: tabular-nums;
}
.fund-project {
  margin-top: 0.26rem;
  font-size: 0.92em;
  font-style: italic;
  color: var(--global-text-color-light);
  line-height: 1.45;
}
.fund-meta, .patent-meta {
  margin-top: 0.38rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.45rem;
  font-size: 0.82rem;
  color: var(--global-text-color-light);
}
.fund-badge, .patent-badge {
  padding: 0.04rem 0.46rem;
  border-radius: 0.7rem;
  border: 1px solid currentColor;
  font-size: 0.70rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  white-space: nowrap;
}
.fund-badge.national { color: var(--global-highlight-color); }
.fund-badge.postdoc { color: #2c7be5; }
.fund-badge.provincial { color: #1a9c6b; }
.patent-badge.granted { color: #1a9c6b; }
.patent-badge.published { color: #2c7be5; }
.fund-grant, .patent-no {
  font-weight: 600;
  color: var(--global-theme-color);
  white-space: nowrap;
  font-variant-numeric: tabular-nums;
}
.fund-note { font-size: 0.80rem; }
.fund-note::before { content: "\00b7  "; }
.patent-inventors b { color: var(--global-text-color); }
/* 奖项类别小标签 */
.award-tag {
  display: inline-block;
  margin-left: 0.45rem;
  padding: 0.02rem 0.42rem;
  font-size: 0.70rem;
  font-weight: 600;
  line-height: 1.5;
  border-radius: 0.7rem;
  border: 1px solid currentColor;
  vertical-align: 0.06rem;
  white-space: nowrap;
}
.award-tag.paper { color: var(--global-highlight-color); }
.award-tag.comp { color: #2c7be5; }
.award-tag.advisor { color: #1a9c6b; }
.award-tag.fund { color: #8a6d3b; }
</style>

<div class="post">

<h3>Honors and Awards</h3>

<div class="award-group">
  <div class="award-year">2026</div>
  <ul class="award-list">
    <li class="award-item has-cert" data-img="/assets/img/awards/docs2026_best_paper.jpg"><span class="award-rank">Best Paper Award</span> &mdash; <span class="award-org">DOCS 2026</span><span class="award-tag paper">Paper Award</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
    <li><span class="award-rank">Best Reviewer Award</span> &mdash; <span class="award-org">KDD 2026</span><span class="award-tag paper">Reviewer Award</span></li>
    <li><span class="award-rank">Gold Reviewer Award</span> &mdash; <span class="award-org">ICML 2026</span><span class="award-tag paper">Reviewer Award</span></li>
    <li class="award-item has-cert" data-img="/assets/img/awards/wcci2026_gnbg.jpg"><span class="award-rank">Joint First Winner</span> &mdash; <span class="award-org">GNBG-III Numerical Global Optimization Competition</span>, IEEE WCCI 2026<span class="award-tag comp">Competition</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
    <li class="award-item has-cert" data-img="/assets/img/awards/wcci2026_hdmmo.jpg"><span class="award-rank">Winner</span> &mdash; <span class="award-org">Competition on Higher Dimension Multimodal Multiobjective Optimization</span>, IEEE WCCI 2026<span class="award-tag comp">Competition</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
    <li class="award-item has-cert" data-img="/assets/img/awards/wcci2026_mixedvar.jpg"><span class="award-rank">Second Place</span> &mdash; <span class="award-org">Competition on Evolutionary Expensive Optimization for Mixed-Variable Problems (Learning to Optimize)</span>, IEEE WCCI 2026<span class="award-tag comp">Competition</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
  </ul>
</div>

<div class="award-group">
  <div class="award-year">2025</div>
  <ul class="award-list">
    <li class="award-item has-cert" data-img="/assets/img/awards/postdoc2025_assessment.jpg"><span class="award-rank">Tier 2, Top 5%</span> &mdash; <span class="award-org">2025 Postdoctoral Research Performance Assessment</span>, China Postdoctoral Science Foundation<span class="award-tag fund">Assessment</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
    <li class="award-item has-cert" data-img="/assets/img/awards/cec2025_c04.jpg"><span class="award-rank">Winner</span> &mdash; <span class="award-org">IEEE CEC 2025 Competition C04</span>: EMAP Dataset Challenge<span class="award-tag comp">Competition</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
    <li class="award-item has-cert" data-img="/assets/img/awards/cec2025_c07.jpg"><span class="award-rank">Winner</span> &mdash; <span class="award-org">IEEE CEC 2025 Competition C07</span>: Large-scale Multiobjective Optimization for Status Assessment of Measuring Equipment<span class="award-tag comp">Competition</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
    <li class="award-item has-cert" data-img="/assets/img/awards/cec2025_c06.jpg"><span class="award-rank">Second Runner-Up</span> &mdash; <span class="award-org">IEEE CEC 2025 Competition C06</span>: Constrained Single and Multiobjective Numerical Optimization<span class="award-tag comp">Competition</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
    <li class="award-item has-cert" data-img="/assets/img/awards/cec2025_c10.jpg"><span class="award-rank">Second Runner-Up</span> &mdash; <span class="award-org">IEEE CEC 2025 Competition C10</span>: Dynamic Optimization Problems<span class="award-tag comp">Competition</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
  </ul>
</div>

<div class="award-group">
  <div class="award-year">2024</div>
  <ul class="award-list">
    <li class="award-item has-cert" data-img="/assets/img/awards/wcci2024_winner.jpg"><span class="award-rank">Winner</span> &mdash; <span class="award-org">Large-scale Multiobjective Optimization for Status Assessment of Measuring Equipment</span>, IEEE WCCI 2024<span class="award-tag comp">Competition</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
    <li class="award-item has-cert" data-img="/assets/img/awards/cicisc2024_bronze.jpg"><span class="award-rank">Bronze Award</span> &mdash; <span class="award-org">China International College Students&rsquo; Innovation Competition</span> <span class="award-level national">National Level</span> <span class="award-note">(as advisor)</span><span class="award-tag advisor">Student Competition</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
    <li class="award-item has-cert" data-img="/assets/img/awards/anhui2024_gold.jpg"><span class="award-rank">Gold Award</span> &mdash; <span class="award-org">Final of Anhui Province College Students&rsquo; Innovation Competition</span> <span class="award-level provincial">Provincial Level</span> <span class="award-note">(as advisor)</span><span class="award-tag advisor">Student Competition</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
    <li class="award-item has-cert" data-img="/assets/img/awards/fuwu2024_third.jpg"><span class="award-rank">Third Prize</span> &mdash; <span class="award-org">China Students Service Outsourcing Innovation and Entrepreneurship Competition</span>, Eastern Region <span class="award-level regional">Regional Level</span> <span class="award-note">(as advisor)</span><span class="award-tag advisor">Student Competition</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
    <li class="award-item has-cert" data-img="/assets/img/awards/postdoc2024_fellowship.jpg"><span class="award-rank">Grade B</span> &mdash; <span class="award-org">Postdoctoral Fellowship Program</span>, China Postdoctoral Science Foundation<span class="award-tag fund">Fellowship</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
  </ul>
</div>

<div class="award-group">
  <div class="award-year">2023</div>
  <ul class="award-list">
    <li class="award-item has-cert" data-img="/assets/img/awards/docs2023_best_paper.jpg"><span class="award-rank">Best Paper</span> &mdash; <span class="award-org">DOCS 2023</span><span class="award-tag paper">Paper Award</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
    <li class="award-item has-cert" data-img="/assets/img/awards/cec2023_winner.jpg"><span class="award-rank">Winner</span> &mdash; <span class="award-org">Large-scale Continuous Optimization for Non-contact Measurement (MO Optimization)</span>, IEEE CEC 2023<span class="award-tag comp">Competition</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
  </ul>
</div>

<div class="award-group">
  <div class="award-year">2022</div>
  <ul class="award-list">
    <li class="award-item has-cert" data-img="/assets/img/awards/ahsai2022_poster.jpg"><span class="award-rank">Best Poster Paper</span> &mdash; <span class="award-org">2022 Annual Conference of Anhui Artificial Intelligence Society</span><span class="award-tag paper">Paper Award</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
    <li class="award-item has-cert" data-img="/assets/img/awards/anhui2022_silver.jpg"><span class="award-rank">Silver Award</span> &mdash; <span class="award-org">8th Anhui Province &ldquo;Internet+&rdquo; College Students&rsquo; Innovation and Entrepreneurship Competition</span> <span class="award-level provincial">Provincial Level</span> <span class="award-note">(as advisor)</span><span class="award-tag advisor">Student Competition</span><span class="cert-hint"><i class="far fa-images"></i></span></li>
  </ul>
</div>

<div class="award-group">
  <div class="award-year">2019</div>
  <ul class="award-list">
    <li><span class="award-rank">National Scholarship for Postgraduate</span> &mdash; <span class="award-org">Ministry of Education, China</span> <span class="award-level national">National Level</span><span class="award-tag fund">Scholarship</span></li>
  </ul>
</div>

<h3 class="section-title">Fundings</h3>

<div class="fund-list">

  <div class="fund-item">
    <div class="fund-head">
      <span class="fund-name">National Natural Science Foundation of China &middot; General Project</span>
      <span class="fund-amount">¥500K</span>
    </div>
    <div class="fund-meta">
      <span class="fund-badge national">National</span>
      <span class="fund-period">2027 &ndash; 2030</span>
      <span>Principal Investigator</span>
    </div>
  </div>

  <div class="fund-item">
    <div class="fund-head">
      <span class="fund-name">National Natural Science Foundation of China &middot; Youth Project</span>
      <span class="fund-amount">¥300K</span>
    </div>
    <div class="fund-project">&ldquo;Efficient Evolutionary Neural Architecture Search Methods for Student Cognitive Diagnosis Models in Intelligent Education&rdquo;</div>
    <div class="fund-meta">
      <span class="fund-badge national">National</span>
      <span class="fund-grant">No. 62302019</span>
      <span class="fund-period">2024 &ndash; 2026</span>
    </div>
  </div>

  <div class="fund-item">
    <div class="fund-head">
      <span class="fund-name">Postdoctoral Fellowship Program (Grade B) &middot; China Postdoctoral Science Foundation</span>
      <span class="fund-amount">¥360K</span>
    </div>
    <div class="fund-meta">
      <span class="fund-badge postdoc">Postdoctoral</span>
      <span class="fund-grant">No. GZB20240002</span>
      <span class="fund-period">2024 &ndash; 2026</span>
      <span class="fund-note">≈1000 awardees nationwide (≈500 Grade A)</span>
    </div>
  </div>

  <div class="fund-item">
    <div class="fund-head">
      <span class="fund-name">China Postdoctoral Science Foundation &middot; 74th Batch of General Funding</span>
      <span class="fund-amount">¥80K</span>
    </div>
    <div class="fund-meta">
      <span class="fund-badge postdoc">Postdoctoral</span>
      <span class="fund-period">2023 &ndash; 2025</span>
      <span class="fund-note">success rate ≈17%</span>
    </div>
  </div>

  <div class="fund-item">
    <div class="fund-head">
      <span class="fund-name">2025 Postdoctoral Research Performance Assessment (Tier 2, Top 5%) &middot; China Postdoctoral Science Foundation</span>
      <span class="fund-amount">¥60K</span>
    </div>
    <div class="fund-meta">
      <span class="fund-badge postdoc">Postdoctoral</span>
      <span class="fund-grant">No. YJB20250190</span>
      <span class="fund-period">2025 &ndash; 2026</span>
    </div>
  </div>

  <div class="fund-item">
    <div class="fund-head">
      <span class="fund-name">Anhui Province Key Laboratory of Intelligent Computing and Applications</span>
      <span class="fund-amount">¥50K</span>
    </div>
    <div class="fund-meta">
      <span class="fund-badge provincial">Provincial</span>
      <span class="fund-grant">No. AFZNJS2024KF01</span>
      <span class="fund-period">2024 &ndash; 2025</span>
    </div>
  </div>

</div>

<h3 class="section-title">Patents</h3>

<div class="patent-list">

  <div class="patent-item">
    <div class="patent-head">
      <span class="patent-title">A Multi-objective Based Neural Architecture Search Method <span class="fund-note">(一种基于多目标的神经架构搜索方法)</span></span>
      <span class="patent-no">CN 118070884 A</span>
    </div>
    <div class="patent-meta">
      <span class="patent-badge published">Published</span>
      <span class="patent-inventors"><b>S. Yang</b>, M. Chen, X. Yu, H. Ma, Y. Tian</span>
      <span>filed Apr. 2024 &middot; published May 2024</span>
    </div>
  </div>

  <div class="patent-item">
    <div class="patent-head">
      <span class="patent-title">A Knowledge Tracing Method Based on Transformer Neural Architecture Search <span class="fund-note">(一种基于Transformer神经架构搜索的知识追踪方法)</span></span>
      <span class="patent-no">CN 118297130 A</span>
    </div>
    <div class="patent-meta">
      <span class="patent-badge published">Published</span>
      <span class="patent-inventors"><b>S. Yang</b>, L. Qin, X. Yu, H. Ma, Y. Tian</span>
      <span>filed Apr. 2024 &middot; published Jul. 2024</span>
    </div>
  </div>

  <div class="patent-item">
    <div class="patent-head">
      <span class="patent-title">An Image Recognition Method Based on a Gradient-Guided Evolutionary Algorithm <span class="fund-note">(一种基于梯度引导进化算法的图像识别方法)</span></span>
      <span class="patent-no">ZL 202111639517.1</span>
    </div>
    <div class="patent-meta">
      <span class="patent-badge granted">Granted</span>
      <span class="patent-inventors">Y. Tian, Z. Shi, <b>S. Yang</b>, X. Zhang</span>
    </div>
  </div>

  <div class="patent-item">
    <div class="patent-head">
      <span class="patent-title">A Cognitive Diagnosis Method for Heterogeneous Graph Learning Based on Imbalance Perception <span class="fund-note">(一种基于不平衡感知的异构图学习认知诊断方法)</span></span>
      <span class="patent-no">CN 120144950 A</span>
    </div>
    <div class="patent-meta">
      <span class="patent-badge published">Published</span>
      <span class="patent-inventors">X. Zhang, J. Li, <b>S. Yang</b>, X. Yu, H. Ma</span>
    </div>
  </div>

  <div class="patent-item">
    <div class="patent-head">
      <span class="patent-title">Distance-Aware Knowledge Tracing <span class="fund-note">(一种距离感知的知识追踪方法)</span></span>
      <span class="patent-no">CN 117933301 A</span>
    </div>
    <div class="patent-meta">
      <span class="patent-badge published">Published</span>
      <span class="patent-inventors">M. Cao, H. Ma, <b>S. Yang</b>, X. Zhang</span>
    </div>
  </div>

</div>

<div id="award-preview" class="award-preview"><img src="" alt="Award certificate"></div>

<script>
(function () {
  var pv = document.getElementById("award-preview");
  var pvImg = pv.querySelector("img");
  var hideTimer = null;
  var current = null;

  function hide() {
    clearTimeout(hideTimer);
    hideTimer = null;
    current = null;
    pv.style.display = "none";
  }

  function showFor(li) {
    var src = li.getAttribute("data-img");
    if (!src) return;
    current = li;
    pvImg.src = src;
    pv.style.display = "block";
    // position below the item, clamped to viewport
    var r = li.getBoundingClientRect();
    var pw = pv.offsetWidth, ph = pv.offsetHeight;
    var top = r.bottom + 8;
    if (top + ph > window.innerHeight - 10) top = Math.max(10, r.top - ph - 8);
    var left = Math.min(r.left, window.innerWidth - pw - 12);
    left = Math.max(12, left);
    pv.style.top = top + "px";
    pv.style.left = left + "px";
  }

  document.querySelectorAll("li.award-item.has-cert").forEach(function (li) {
    li.addEventListener("click", function (e) {
      e.stopPropagation();
      if (current === li) { hide(); return; }
      showFor(li);
    });
    li.addEventListener("mouseleave", function () {
      clearTimeout(hideTimer);
      hideTimer = setTimeout(function () {
        if (current === li) hide();
      }, 300);
    });
    li.addEventListener("mouseenter", function () {
      clearTimeout(hideTimer);
    });
  });

  pv.addEventListener("mouseenter", function () { clearTimeout(hideTimer); });
  pv.addEventListener("mouseleave", hide);
  document.addEventListener("click", function (e) {
    if (pv.style.display === "block" && !pv.contains(e.target)) hide();
  });
  window.addEventListener("scroll", hide, { passive: true });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") hide();
  });
})();
</script>

</div>
