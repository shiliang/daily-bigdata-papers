# 大数据+AI 领域论文日报

**日期**: 2026-06-24

**论文数量**: 7 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Natural Identifiers for Privacy and...](https://arxiv.org/abs/2606.24408v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Holistic Data Scheduler for LLM Pre...](https://arxiv.org/abs/2606.24133v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [REDI-Match: Rotation-Equivariant Di...](https://arxiv.org/abs/2606.24330v1) | 待分析 | 评估失败 | [Code](https://github.com/YinjiGe/REDI-Match.) | 20/43 |
| 4 | [BRAVR: An AP-Assisted Online DRL Me...](https://arxiv.org/abs/2606.24389v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Quantum ring all-reduce: communicat...](https://arxiv.org/abs/2606.20344v2) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [A Comparative Study of Bayesian Con...](https://arxiv.org/abs/2606.23977v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Topological Online Learning for Dis...](https://arxiv.org/abs/2606.23901v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Natural Identifiers for Privacy and Data Audits in Large Language Models

- **作者**: Lorenzo Rossi, Bartłomiej Marek, Franziska Boenisch, Adam Dziedzic
- **发布日期**: 2026-06-23
- **链接**: [arXiv:2606.24408v1](https://arxiv.org/abs/2606.24408v1) | [PDF](https://arxiv.org/pdf/2606.24408v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Assessing the privacy of large language models (LLMs) presents significant challenges.

In particular, most existing methods for auditing differential privacy require the insertion of specially crafted canary data during training, making them impractical for auditing already-trained models without costly retraining.

Additionally, dataset inference, which audits whether a suspect dataset was used to train a model, is infeasible without access to a private non-member held-out dataset.

Yet, such held-out datasets are often unavailable or difficult to construct for real-world cases since they have 

### AI 总结

总结生成失败

---

## 2. Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement Learning

- **作者**: Chenhao Dang, Jing Ma, Mingjie Liao
- **发布日期**: 2026-06-23
- **链接**: [arXiv:2606.24133v1](https://arxiv.org/abs/2606.24133v1) | [PDF](https://arxiv.org/pdf/2606.24133v1)
- **分类**: cs.LG, cs.CL
- **含金量**: 20/43 分

### 摘要

The composition of training data, governed by the diversity of sources and their mixing strategy, is a cornerstone of Large Language Model (LLM) pre-training.

Online Data Mixing (ODM), the technique of adaptively adjusting data mixtures during training, has emerged as a promising direction to improve efficiency.

However, existing methods are constrained by their reliance on a singular optimization perspective, which fundamentally overlooks the need for complex LLM pre-training to consider the dynamic data composition from multiple dimensions.

To overcome this limitation, we introduce the Holis

### AI 总结

总结生成失败

---

## 3. REDI-Match: Rotation-Equivariant Distillation for Efficient and Robust Dense Matching

- **作者**: Yinji Ge, Guixu Zheng, Wulong Guo, Qian Feng, Xu Wu
- **发布日期**: 2026-06-23
- **链接**: [arXiv:2606.24330v1](https://arxiv.org/abs/2606.24330v1) | [PDF](https://arxiv.org/pdf/2606.24330v1)
- **分类**: cs.CV
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/YinjiGe/REDI-Match.) ⭐ 0

### 摘要

Vision Foundation Models (VFMs) have significantly advanced dense feature matching, yet severe in-plane rotation remains a critical challenge.

Existing solutions face a fundamental dilemma: data-driven methods require inefficient parameter scaling to implicitly learn rotations, whereas strictly equivariant networks lack the semantic capacity of modern VFMs.

Consequently, current frameworks typically freeze VFMs and shift the entire burden of rotation generalization to the downstream decoder.

To break this architectural bottleneck, we propose REDI-Match, an efficient framework driven by a novel

### AI 总结

总结生成失败

---

## 4. BRAVR: An AP-Assisted Online DRL Mechanism for Interactive VR Bitrate Adaptation over Wi-Fi

- **作者**: Miguel Casasnovas, Francesc Wilhelmi, Boris Bellalta
- **发布日期**: 2026-06-23
- **链接**: [arXiv:2606.24389v1](https://arxiv.org/abs/2606.24389v1) | [PDF](https://arxiv.org/pdf/2606.24389v1)
- **分类**: cs.NI
- **含金量**: 20/43 分

### 摘要

Interactive virtual reality (VR) streaming over Wi-Fi requires stringent latency and reliability guarantees, which become increasingly difficult to achieve under dynamic channel conditions and shared medium contention.

These challenges make real-time bitrate adaptation a critical yet fundamentally difficult control problem, particularly under limited visibility of the underlying network conditions.

This paper formulates VR bitrate adaptation as a network-aware, online decision-making problem and proposes BRAVR, a decentralized deep reinforcement learning (DRL) mechanism designed to optimize vi

### AI 总结

总结生成失败

---

## 5. Quantum ring all-reduce: communication and privacy advantages for distributed learning

- **作者**: María Gragera Garcés, Lirandë Pira
- **发布日期**: 2026-06-18
- **链接**: [arXiv:2606.20344v2](https://arxiv.org/abs/2606.20344v2) | [PDF](https://arxiv.org/pdf/2606.20344v2)
- **分类**: quant-ph, cs.DC, cs.LG
- **含金量**: 20/43 分

### 摘要

Machine learning models have scaled to unprecedented sizes, making training across distributed devices the de facto standard in the field.

In this work, we explore how quantum communications can make distributed training both more communication-efficient and information-theoretically private, for both classical and quantum learning models.

Ring all-reduce is the foundational communication primitive for large-scale distributed training.

We present a quantum version that reduces per-link online communication by a provably optimal factor of two using pre-shared entanglement and superdense coding,

### AI 总结

总结生成失败

---

## 6. A Comparative Study of Bayesian Contextual Bandits for Real-Time Warehouse Sorter Optimization

- **作者**: Tina Dongxu Li, Mouhacine Benosman, Ken Meszaros, Trevor Dardik
- **发布日期**: 2026-06-22
- **链接**: [arXiv:2606.23977v1](https://arxiv.org/abs/2606.23977v1) | [PDF](https://arxiv.org/pdf/2606.23977v1)
- **分类**: cs.LG, eess.SY
- **含金量**: 20/43 分

### 摘要

Efficient sorter diversion control of automated material handling systems (MHS) is critical for optimizing operational efficiency in large-scale warehouse environments.

In this study, we use an inbound receiving sorter at a high-volume e-commerce warehouse as our primary use case, where the sorter diversion system relies on cost functions with static weight configurations that fail to adapt to highly dynamic system contexts, such as volume mode, congestion level, equipment physical status, and upstream/downstream dependencies.

To address this real-time sorter diversion optimization challenge, 

### AI 总结

总结生成失败

---

## 7. Topological Online Learning for Displacement-based Formation Control

- **作者**: Saksham Sharma, Shubhankar Gupta, Sumant A Gunagi, Suresh Sundaram
- **发布日期**: 2026-06-22
- **链接**: [arXiv:2606.23901v1](https://arxiv.org/abs/2606.23901v1) | [PDF](https://arxiv.org/pdf/2606.23901v1)
- **分类**: cs.RO, eess.SY
- **含金量**: 20/43 分

### 摘要

This paper addresses the problem of robust formation control by introducing Topological Online Learning for Displacement-based (TOLD) formation control, a real-time edge-level adaptation framework.

Unlike conventional node-level robust controllers that regulate individual robot inputs without modifying the interaction topology, TOLD updates the interaction topology weights online to directly minimize formation distortion.

Two strategies are proposed under the TOLD formation control framework: Online Gradient Flow (OGF) with unconstrained weights and Online Exponential Gradient Flow (OExpGF) wi

### AI 总结

总结生成失败

---

