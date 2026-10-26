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

<h3>Fundings</h3>

<ul>
  <li>The National Natural Science Foundation of China (General Project), 2027&ndash;2030, 500K RMB</li>
  <li>The National Natural Science Foundation of China (Youth Project), No. 62302019, "Efficient Evolutionary Neural Architecture Search Methods for Student Cognitive Diagnosis Models in Intelligent Education", 2024&ndash;2026, 300K RMB</li>
  <li>The Postdoctoral Fellowship Program (Grade B), China Postdoctoral Science Foundation, No. GZB20240002, 2024&ndash;2026, 360K RMB</li>
  <li>2025 Postdoctoral Research Performance Assessment (Tier 2), China Postdoctoral Science Foundation, No. YJB20250190, 2025&ndash;2026, 60K RMB</li>
  <li>The China Postdoctoral Science Foundation (74th Batch of General Funding), 2023&ndash;2025, 80K RMB</li>
  <li>Anhui Province Key Laboratory of Intelligent Computing and Applications, No. AFZNJS2024KF01, 2024&ndash;2025, 50K RMB</li>
</ul>

<h3>Patents</h3>

<ul>
  <li>CN 118070884A, "A Multi-objective Based Neural Architecture Search Method" (一种基于多目标的神经架构搜索方法), filed Apr. 2024, published May 2024</li>
  <li>CN 118297130A, "A Knowledge Tracing Method Based on Transformer Neural Architecture Search" (一种基于Transformer神经架构搜索的知识追踪方法), filed Apr. 2024, published Jul. 2024</li>
</ul>

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
