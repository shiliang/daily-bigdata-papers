# 大数据+AI 领域论文日报

**日期**: 2026-05-06

**论文数量**: 8 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Carbon-Aware Compute--Power Schedul...](https://arxiv.org/abs/2605.03751v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Optimal Posterior Sampling for Poli...](https://arxiv.org/abs/2605.03921v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Enwar 3.0: An Agentic Multi-Modal L...](https://arxiv.org/abs/2605.03215v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Human-Provenance Verification shoul...](https://arxiv.org/abs/2605.03210v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Sim-FA: A GPGPU Simulator Framework...](https://arxiv.org/abs/2605.00555v2) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [OCRR: A Benchmark for Online Correc...](https://arxiv.org/abs/2605.03153v1) | 待分析 | 评估失败 | [Code](https://github.com/adriangrassi/ocrr-benchmark.) | 20/43 |
| 7 | [The Buy-or-Build Decision, Revisite...](https://arxiv.org/abs/2604.26482v2) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [AsymK-Talker: Real-Time and Long-Ho...](https://arxiv.org/abs/2605.02948v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Carbon-Aware Compute--Power Scheduling for AI Data Centers with Microgrid Prosumer Operations

- **作者**: Johnny R. Zhang, Gaoyuan Du, Qianyi Sun, Shiqi Wang, Jiaxuan Li
- **发布日期**: 2026-05-05
- **链接**: [arXiv:2605.03751v1](https://arxiv.org/abs/2605.03751v1) | [PDF](https://arxiv.org/pdf/2605.03751v1)
- **分类**: cs.CE
- **含金量**: 20/43 分

### 摘要

AI data centers are increasingly becoming tightly coupled compute--energy systems, where workload placement, cooling demand, electricity procurement, storage operation, and carbon emissions interact over time.

This paper studies carbon-aware compute--power scheduling for geographically distributed AI data centers with microgrid prosumer capabilities.

We propose a mixed-integer linear programming (MILP) framework that jointly schedules rigid training jobs, routes elastic inference workloads, dispatches local generation and battery storage, and manages bidirectional grid interaction under latenc

### AI 总结

总结生成失败

---

## 2. Optimal Posterior Sampling for Policy Identification in Tabular Markov Decision Processes

- **作者**: Cyrille Kone, Kevin Jamieson
- **发布日期**: 2026-05-05
- **链接**: [arXiv:2605.03921v1](https://arxiv.org/abs/2605.03921v1) | [PDF](https://arxiv.org/pdf/2605.03921v1)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

We study the $(\varepsilon, δ)$-PAC policy identification problem in finite-horizon episodic Markov Decision Processes.

Existing approaches provide finite-time guarantees for approximate settings ($\varepsilon>0$) but suffer from high computational cost, rendering them hard to implement, and also suffer from suboptimal dependence on $\log(1/δ)$.

We propose a randomized and computationally efficient algorithm for best policy identification that combines posterior sampling with an online learning algorithm to guide exploration in the MDP.

Our method achieves asymptotic optimality in sample compl

### AI 总结

总结生成失败

---

## 3. Enwar 3.0: An Agentic Multi-Modal LLM Orchestrator for Situation-Aware Beamforming, Blockage Prediction, and Handover Management

- **作者**: Ahmad M. Nazar, Abdulkadir Celik, Asmaa Abdallah, Mohamed Y. Selim, Daji Qiao
- **发布日期**: 2026-05-04
- **链接**: [arXiv:2605.03215v1](https://arxiv.org/abs/2605.03215v1) | [PDF](https://arxiv.org/pdf/2605.03215v1)
- **分类**: cs.MA
- **含金量**: 20/43 分

### 摘要

Maintaining robust millimeter-wave (mmWave) connectivity in vehicular networks requires real-time adaptation to environmental dynamics, sensor degradation, and link variability.

This paper presents Enwar 3.0, an environment-aware reasoning framework that unifies multi-modal sensing, agentic large language models (LLMs), and context-driven model selection for predictive beamforming, blockage detection, and handover management.

Building upon prior iterations of Enwar, the proposed architecture integrates a classifier-driven assessment of sensor health with a primed LLM that orchestrates multiple

### AI 总结

总结生成失败

---

## 4. Human-Provenance Verification should be Treated as Labor Infrastructure in AI-Saturated Markets

- **作者**: Erin McGurk, David Khachaturov
- **发布日期**: 2026-05-04
- **链接**: [arXiv:2605.03210v1](https://arxiv.org/abs/2605.03210v1) | [PDF](https://arxiv.org/pdf/2605.03210v1)
- **分类**: cs.CY, cs.AI, econ.GN
- **含金量**: 20/43 分

### 摘要

We argue that AI-saturated markets are likely to create Veblen-good premiums, which we term human-provenance premiums, for verified human presence, and hence AI governance should treat human-provenance verification as labor infrastructure.

Generative and agentic AI systems lower the cost of many standardized cognitive, creative, and coordination tasks, weakening the scarcity premiums that have supported much middle-tier knowledge work.

We argue that this pressure may produce an asymmetric barbell-shaped structure of value capture in advanced economies: high-volume synthetic production controll

### AI 总结

总结生成失败

---

## 5. Sim-FA: A GPGPU Simulator Framework for Fine-Grained FlashAttention Pipeline Analysis

- **作者**: Zhongchun Zhou, Yuhang Gu, Chengtao Lai, Ya Wang, Wei Zhang
- **发布日期**: 2026-05-01
- **链接**: [arXiv:2605.00555v2](https://arxiv.org/abs/2605.00555v2) | [PDF](https://arxiv.org/pdf/2605.00555v2)
- **分类**: cs.AR
- **含金量**: 20/43 分

### 摘要

To efficiently support Large Language Models (LLMs), modern GPGPU architectures have introduced new features and programming paradigms, such as warp specialization.

These features enable temporal overlap between the producer and consumer, as well as between matrix multiplication and activation function operations, substantially improving performance.

To conduct effective AI infrastructure and computer architecture research, cycle-accurate simulators that support these new features, together with analytical models that faithfully capture workload characteristics, are essential.

However, exist

### AI 总结

总结生成失败

---

## 6. OCRR: A Benchmark for Online Correction Recovery under Distribution Shift

- **作者**: Adrian Grassi
- **发布日期**: 2026-05-04
- **链接**: [arXiv:2605.03153v1](https://arxiv.org/abs/2605.03153v1) | [PDF](https://arxiv.org/pdf/2605.03153v1)
- **分类**: cs.LG, cs.CL
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/adriangrassi/ocrr-benchmark.) ⭐ 0

### 摘要

Static benchmarks measure a model frozen at training time.

Real systems face distribution shift: new categories, paraphrased queries, drift: and must recover online via user corrections.

No existing benchmark measures recovery speed under correction streams.

We introduce OCRR (Online Correction Recovery Rate): a benchmark that streams a corpus through a classification system, applies oracle or stochastic corrections to wrong predictions, and reports two curves: novel-class accuracy and original-distribution accuracy versus correction count.

We evaluate the substrate alongside nine baseline alg

### AI 总结

总结生成失败

---

## 7. The Buy-or-Build Decision, Revisited: How Agentic AI Changes the Economics of Enterprise Software

- **作者**: David Klotz
- **发布日期**: 2026-04-29
- **链接**: [arXiv:2604.26482v2](https://arxiv.org/abs/2604.26482v2) | [PDF](https://arxiv.org/pdf/2604.26482v2)
- **分类**: cs.CY
- **含金量**: 20/43 分

### 摘要

Advances in generative artificial intelligence, particularly agentic coding systems capable of autonomous software development, are disrupting the economics of the make-or-buy decision for enterprise applications.

The "SaaSocalypse" narrative predicts that AI will render large segments of the Software-as-a-Service market obsolete by enabling firms to build software in-house at a fraction of historical cost.

This paper adopts a conceptual research approach, combining transaction cost economics and the resource-based view with an assessment of current AI capabilities, to systematically re-evalua

### AI 总结

总结生成失败

---

## 8. AsymK-Talker: Real-Time and Long-Horizon Talking Head Generation via Asymmetric Kernel Distillation

- **作者**: Yuxin Lu, Qian Qiao, Jiayang Sun, Min Cao, Guibo Zhu
- **发布日期**: 2026-05-01
- **链接**: [arXiv:2605.02948v1](https://arxiv.org/abs/2605.02948v1) | [PDF](https://arxiv.org/pdf/2605.02948v1)
- **分类**: cs.LG, cs.AI, cs.SD
- **含金量**: 20/43 分

### 摘要

Recent advances in diffusion models have markedly enhanced the visual fidelity of audio-driven talking head generation.

Nevertheless, existing methods are constrained by three critical limitations: causal inefficiency that impedes real-time inference, incompatibility with temporally coherent conditioning, and progressive drift over long-horizon generation, collectively hindering their deployment in real-time applications.

To overcome these challenges, we introduce AsymK-Talker, a novel diffusion-distillation method designed for real-time and long-horizon talking head generation.

AsymK-Talker c

### AI 总结

总结生成失败

---

