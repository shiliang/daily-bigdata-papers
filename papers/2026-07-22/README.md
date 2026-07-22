# 大数据+AI 领域论文日报

**日期**: 2026-07-22

**论文数量**: 4 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Vidu S1: A Real-Time Interactive Vi...](https://arxiv.org/abs/2607.03118v2) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Recti-Q: Feature-Space Rectificatio...](https://arxiv.org/abs/2607.18540v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Adaptive Two-Stage Online Learning ...](https://arxiv.org/abs/2607.18522v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [$\texttt{codesign-mcdp}$: A Python ...](https://arxiv.org/abs/2607.18415v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Vidu S1: A Real-Time Interactive Video Generation Model

- **作者**: Jintao Zhang, Kai Jiang, Jintao Chen, Xu Wang, Yang Luo
- **发布日期**: 2026-07-03
- **链接**: [arXiv:2607.03118v2](https://arxiv.org/abs/2607.03118v2) | [PDF](https://arxiv.org/pdf/2607.03118v2)
- **分类**: cs.CV, cs.LG
- **含金量**: 20/43 分

### 摘要

We introduce Vidu S1, a real-time interactive video generation model supporting voice control of digital characters.

Users can control video generation content at any moment through voice instructions.

Vidu S1 supports infinite-length real-time video generation without blurring, drift, or visual distortion.

Built with TurboDiffusion and TurboServe, Vidu S1 outputs 540p real-time videos at up to 42 FPS on regular consumer GPUs.

Users can upload custom images of real people, anime, and pets, and choose different voice tones for personalized experiences.

Experiments show that Vidu S1 achieves the

### AI 总结

总结生成失败

---

## 2. Recti-Q: Feature-Space Rectification for Out-of-Distribution-Robust Quantized Perception in Edge Robotics

- **作者**: Hamidreza Yaghoubi Araghi, Parastoo Pilevar, Ming C. Lin
- **发布日期**: 2026-07-20
- **链接**: [arXiv:2607.18540v1](https://arxiv.org/abs/2607.18540v1) | [PDF](https://arxiv.org/pdf/2607.18540v1)
- **分类**: cs.CV, cs.LG, cs.RO
- **含金量**: 20/43 分

### 摘要

Robotic perception pipelines increasingly rely on large vision backbones deployed on SWaP-constrained edge platforms, making post-training quantization (PTQ) attractive for real-time inference.

However, while PTQ often preserves clean in-distribution accuracy, we show that it can substantially degrade reliability under deployment-relevant distribution shifts (e.g., sensor noise, severe weather, and novel operating environments), creating a Quantization-Induced Robustness Gap.

Across foundational vision benchmarks (ImageNet-C and PACS), 4-bit PTQ models exhibit pronounced robustness degradation

### AI 总结

总结生成失败

---

## 3. Adaptive Two-Stage Online Learning for Service-Affecting Failure Detection in Mobile Core Networks

- **作者**: J. du Toit, G. Fita, J. Salzwedel, A. Stoltz, R. Wolhuter
- **发布日期**: 2026-07-20
- **链接**: [arXiv:2607.18522v1](https://arxiv.org/abs/2607.18522v1) | [PDF](https://arxiv.org/pdf/2607.18522v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Mobile network operators monitor aggregated traffic volumes to assess the operational health of core network infrastructure.

Reliable failure detection is challenging due to strong temporal structure, non-stationarity, measurement artefacts, and extreme class imbalance, which limit static threshold-based monitoring.

This paper proposes a two-stage online learning framework for traffic-based failure detection in mobile core networks.

Stage I incrementally models normal traffic dynamics using lightweight regression with time-aware features.

Stage II analyses prediction residuals together with co

### AI 总结

总结生成失败

---

## 4. $\texttt{codesign-mcdp}$: A Python Library for Monotone Co-Design Problems

- **作者**: Corentin Briat
- **发布日期**: 2026-07-20
- **链接**: [arXiv:2607.18415v1](https://arxiv.org/abs/2607.18415v1) | [PDF](https://arxiv.org/pdf/2607.18415v1)
- **分类**: math.OC, cs.MS, eess.SY
- **含金量**: 20/43 分

### 摘要

$\texttt{codesign-mcdp}$ is a Python library for formulating and solving $\textit{Monotone Co-Design Problems}$ (MCDPs) in the framework of Censi (2015).

A design problem is a relation between two posets, a functionality poset $F$ and a resource poset $R$; given a target functionality, the problem asks for the antichain of minimal resources needed to deliver it.

Design problems compose under three operators (series, parallel, feedback), and the resulting class is closed under composition.

The library implements the antichain calculus, six primitive design-problem types, the three composition o

### AI 总结

总结生成失败

---

