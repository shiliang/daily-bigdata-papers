# 大数据+AI 领域论文日报

**日期**: 2026-04-17

**论文数量**: 5 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [CoTEvol: Self-Evolving Chain-of-Tho...](https://arxiv.org/abs/2604.14768v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Switching Efficiency: A Novel Frame...](https://arxiv.org/abs/2604.14690v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [SAKURAONE: An Open Ethernet-Based A...](https://arxiv.org/abs/2604.13600v2) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Mistake gating leads to energy and ...](https://arxiv.org/abs/2604.14336v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Doubly Outlier-Robust Online Infini...](https://arxiv.org/abs/2604.14322v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning

- **作者**: Zhuo Wang, Zhuo Zhang, Yafu Li, Yu Cheng, Lizhen Qu
- **发布日期**: 2026-04-16
- **链接**: [arXiv:2604.14768v1](https://arxiv.org/abs/2604.14768v1) | [PDF](https://arxiv.org/pdf/2604.14768v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

Large Language Models (LLMs) exhibit strong mathematical reasoning when trained on high-quality Chain-of-Thought (CoT) that articulates intermediate steps, yet costly CoT curation hinders further progress.

While existing remedies such as distillation from stronger LLMs and self-synthesis based on test-time search alleviate this issue, they often suffer from diminishing returns or high computing overhead.In this work, we propose CoTEvol, a genetic evolutionary framework that casts CoT generation as a population-based search over reasoning trajectories.Candidate trajectories are iteratively evol

### AI 总结

总结生成失败

---

## 2. Switching Efficiency: A Novel Framework for Dissecting AI Data Center Network Efficiency

- **作者**: Niangen Ye, Jiawen Zhu, Baojun Chen, Dong Wang, Jiang Sun
- **发布日期**: 2026-04-16
- **链接**: [arXiv:2604.14690v1](https://arxiv.org/abs/2604.14690v1) | [PDF](https://arxiv.org/pdf/2604.14690v1)
- **分类**: cs.NI
- **含金量**: 20/43 分

### 摘要

Communication is pivotal in LLM training, and a thorough analysis of the communication efficiency of AI data center (AIDC) network is essential for guiding the design of these capital-intensive clusters.

However, conventional metrics are inadequate for such analysis, as they do not directly link network activity to computational progress and lack granularity to diagnose the impact of different network design patterns.

To address this, we introduce a metric framework, the Switching Efficiency Framework, whose core metric - Switching Efficiency ($η$) - quantifies computationally effective data t

### AI 总结

总结生成失败

---

## 3. SAKURAONE: An Open Ethernet-Based AI HPC System and Its Observed Workload Dynamics in a Single-Tenant LLM Development Environment

- **作者**: Fumikazu Konishi, Yuuki Tsubouchi, Hirofumi Tsuruta
- **发布日期**: 2026-04-15
- **链接**: [arXiv:2604.13600v2](https://arxiv.org/abs/2604.13600v2) | [PDF](https://arxiv.org/pdf/2604.13600v2)
- **分类**: cs.DC, cs.NI
- **含金量**: 20/43 分

### 摘要

SAKURAONE is a managed high performance computing (HPC) cluster developed and operated by the SAKURA Internet Research Center.

It builds on the KOKARYOKU PHY bare metal GPU platform and is optimized for advanced workloads, including large language model (LLM) training.

In ISC 2025 TOP500, SAKURAONE is ranked 49th by HPL and is the only top 100 system that uses a fully open networking stack - 800 GbE with SONiC - demonstrating the scalability of vendor-neutral technology.

Measured performance is 33.95 PFLOP/s (HPL Rmax), 396.295 TFLOP/s (HPCG), and 339.86 PFLOP/s on HPL-MxP with FP8.

The system

### AI 总结

总结生成失败

---

## 4. Mistake gating leads to energy and memory efficient continual learning

- **作者**: Aaron Pache, Mark CW van Rossum
- **发布日期**: 2026-04-15
- **链接**: [arXiv:2604.14336v1](https://arxiv.org/abs/2604.14336v1) | [PDF](https://arxiv.org/pdf/2604.14336v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

Synaptic plasticity is metabolically expensive, yet animals continuously update their internal models without exhausting energy reserves.

However, when artificial neural networks are trained, the network parameters are typically updated on every sample that is presented, even if the sample was classified correctly.

Inspired by the human negativity bias and error-related negativity, we propose 'memorized mistake-gated learning' -- a biologically plausible plasticity rule where synaptic updates are strictly gated by current and past classification errors.

This reduces the number of updates the n

### AI 总结

总结生成失败

---

## 5. Doubly Outlier-Robust Online Infinite Hidden Markov Model

- **作者**: Horace Yiu, Leandro Sánchez-Betancourt, Álvaro Cartea, Gerardo Duran-Martin
- **发布日期**: 2026-04-15
- **链接**: [arXiv:2604.14322v1](https://arxiv.org/abs/2604.14322v1) | [PDF](https://arxiv.org/pdf/2604.14322v1)
- **分类**: stat.ML, cs.LG
- **含金量**: 20/43 分

### 摘要

We derive a robust update rule for the online infinite hidden Markov model (iHMM) for when the streaming data contains outliers and the model is misspecified.

Leveraging recent advances in generalised Bayesian inference, we define robustness via the posterior influence function (PIF), and provide conditions under which the online iHMM has bounded PIF.

Imposing robustness inevitably induces an adaptation lag for regime switching.

Our method, which is called Batched Robust iHMM (BR-iHMM), balances adaptivity and robustness with two additional tunable parameters.

Across limit order book data, hou

### AI 总结

总结生成失败

---

