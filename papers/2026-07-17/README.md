# 大数据+AI 领域论文日报

**日期**: 2026-07-17

**论文数量**: 5 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Don't Predict, Prioritize: Rethinki...](https://arxiv.org/abs/2607.15115v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Almost Navigable Graphs](https://arxiv.org/abs/2607.14564v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [BridgeFlow: Fast and Robust SE(2)-E...](https://arxiv.org/abs/2607.14725v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Long-History User Transformers for ...](https://arxiv.org/abs/2607.14331v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [DRIFT: Direct Reduced Fourier Trans...](https://arxiv.org/abs/2607.14394v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Don't Predict, Prioritize: Rethinking GPU Reliability Assessment

- **作者**: Difeng Ma, Changhua Pei, Yuanwei Lu, Quan Zhou, Zexin Wang
- **发布日期**: 2026-07-16
- **链接**: [arXiv:2607.15115v1](https://arxiv.org/abs/2607.15115v1) | [PDF](https://arxiv.org/pdf/2607.15115v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

The reliability of Graphics Processing Units (GPUs) is a criticalbottleneck for modern large-scale AI infrastructure, where a sin-gle node failure can disrupt synchronous training jobs and causesignificant financial losses.

While predictive maintenance is widelyused in other hardware domains, we demonstrate that accuratelypredicting the exact timing of GPU failures is inherently difficult.Through an in-depth analysis of telemetry data from a productioncluster, we find that major GPU failures, including Double Bit Er-rors (DBEs) and GPU Lost events, exhibit strong stochasticity andlow signal-to

### AI 总结

总结生成失败

---

## 2. Almost Navigable Graphs

- **作者**: Pratyush Avi, Christopher Musco
- **发布日期**: 2026-07-16
- **链接**: [arXiv:2607.14564v1](https://arxiv.org/abs/2607.14564v1) | [PDF](https://arxiv.org/pdf/2607.14564v1)
- **分类**: cs.DS
- **含金量**: 20/43 分

### 摘要

Graph-based methods like HNSW, DiskANN, NSG, and others have become an increasingly popular choice for implementing approximate nearest neighbor search (ANNS) in Vector Databases (VecDBs).

The success of these methods has motivated the study of how to best construct a search graph for a given dataset.

To that end, \emph{navigability} has been identified as a desirable graph property which ensures good ANNS performance when combined with greedy search.

However, for a dataset with $n$ vectors, the sparsest navigable graph requires $O(n\sqrt{n})$ edges in the worst-case, and we show empirically

### AI 总结

总结生成失败

---

## 3. BridgeFlow: Fast and Robust SE(2)-Equivariant Motion Planning with Flow Matching

- **作者**: Xinzhe Zhou, Xuyang Wang, Xiaoming Duan, Jianping He
- **发布日期**: 2026-07-16
- **链接**: [arXiv:2607.14725v1](https://arxiv.org/abs/2607.14725v1) | [PDF](https://arxiv.org/pdf/2607.14725v1)
- **分类**: cs.RO
- **含金量**: 20/43 分

### 摘要

In robotic motion planning, equivariance to rigid body transformations is crucial for robust spatial generalization.

However, current learning-based planners face a critical dilemma: they either lack inherent equivariance, treating transformed tasks as novel scenarios, or enforce it via computationally expensive specialized architectures that bottleneck real-time inference.

To break this trade-off, we propose BridgeFlow, a fast and strictly SE(2)-equivariant generative motion planning framework.

Rather than relying on heavy equivariant networks, BridgeFlow achieves exact spatial equivariance v

### AI 总结

总结生成失败

---

## 4. Long-History User Transformers for Real-Time Ad Ranking

- **作者**: Viacheslav Ovchinnikov, Georgii Smirnov, Nikolai Savushkin, Veronika Ivanova, Maksim Kuzin
- **发布日期**: 2026-07-15
- **链接**: [arXiv:2607.14331v1](https://arxiv.org/abs/2607.14331v1) | [PDF](https://arxiv.org/pdf/2607.14331v1)
- **分类**: cs.IR
- **含金量**: 20/43 分

### 摘要

Long interaction histories are among the most informative inputs for click-through rate (CTR) prediction, yet in online advertising they collide with a hard serving constraint: ads must be scored within a few hundred milliseconds to enter the auction, which rules out running a large sequence encoder at request time.

We describe how a production advertising system resolves this conflict by decoupling history encoding from real-time inference.

A high-capacity offline transformer asynchronously encodes the user's full cross-surface interaction history into a compact representation cached in a fea

### AI 总结

总结生成失败

---

## 5. DRIFT: Direct Reduced Fourier Transforms for Distributed Spectral Neural Operators

- **作者**: Sana Taghipour Anvari, David Kaeli
- **发布日期**: 2026-07-15
- **链接**: [arXiv:2607.14394v1](https://arxiv.org/abs/2607.14394v1) | [PDF](https://arxiv.org/pdf/2607.14394v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Fourier Neural Operators (FNOs) learn solution operators for partial differential equations and offer orders of magnitude speedup over traditional numerical solvers at inference time, which makes them attractive surrogates for high-resolution computational physics.

Scaling FNOs to high-resolution spatial grids requires distributing the data across GPUs, but the distributed FFT at the core of each spectral layer requires multiple dense all-to-all collectives that communicate the full spatial tensor, only for most coefficients to be discarded immediately.

We introduce the Distributed Truncated S

### AI 总结

总结生成失败

---

