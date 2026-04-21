# 大数据+AI 领域论文日报

**日期**: 2026-04-21

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Semantic Step Prediction: Multi-Ste...](https://arxiv.org/abs/2604.18464v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Tensor Processing with Homodyne Pho...](https://arxiv.org/abs/2604.18496v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Toward Zero-Egress Psychiatric AI: ...](https://arxiv.org/abs/2604.18302v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Spectral bandits for smooth graph f...](https://arxiv.org/abs/2604.18420v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [ATANT: An Evaluation Framework for ...](https://arxiv.org/abs/2604.06710v2) | 待分析 | 评估失败 | [Code](https://github.com/Kenotic-Labs/ATANT.) | 20/43 |
| 6 | [Active Inference-Based Adaptive Rou...](https://arxiv.org/abs/2604.17373v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Federation over Text: Insight Shari...](https://arxiv.org/abs/2604.16778v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [POLAR: Online Learning for LoRA Ada...](https://arxiv.org/abs/2604.16583v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Scalable and Adaptive Parallel Trai...](https://arxiv.org/abs/2604.16715v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [A Lightweight Transformer for Pain ...](https://arxiv.org/abs/2604.16491v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Semantic Step Prediction: Multi-Step Latent Forecasting in LLM Reasoning Trajectories via Step Sampling

- **作者**: Yidi Yuan
- **发布日期**: 2026-04-20
- **链接**: [arXiv:2604.18464v1](https://arxiv.org/abs/2604.18464v1) | [PDF](https://arxiv.org/pdf/2604.18464v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Semantic Tube Prediction (STP) leverages representation geometric to regularize LLM hidden-state trajectories toward locally linear geodesics during fine-tuning, thereby greatly improving data efficiency.

The original STP recipe samples random token sub-spans, which is compatible with the base large language model (LLM) training architecture.

Inspired by STP, we are interested to investigate whether the sampling position can further enhance the semantic structure of multi-step reasoning, and hence affect its geometric impact.

We applied STP at consecutive semantic reasoning step boundaries and

### AI 总结

总结生成失败

---

## 2. Tensor Processing with Homodyne Photonic Integrated Circuits exceeds 1,000 TOPS

- **作者**: Lian Zhou, Kaiwen Xue, Yun-Jhu Lee, Chun-Ho Lee, Yuan Li
- **发布日期**: 2026-04-20
- **链接**: [arXiv:2604.18496v1](https://arxiv.org/abs/2604.18496v1) | [PDF](https://arxiv.org/pdf/2604.18496v1)
- **分类**: cs.ET
- **含金量**: 20/43 分

### 摘要

High-performance computing underpins modern artificial intelligence (AI), enabling foundation models, real-time inference and perception in autonomous systems, and data-intensive scientific simulations.

Recent advances in quantization techniques utilizing low-precision computation without degrading model accuracy, creates new opportunities for analog photonic computing characterized by ultra-high clock rates and low energy consumption.

Here we propose and demonstrate a coherent homodyne integrated circuit capable of general matrix multiplication(GEMM) with aggregate throughput that exceeds 1,0

### AI 总结

总结生成失败

---

## 3. Toward Zero-Egress Psychiatric AI: On-Device LLM Deployment for Privacy-Preserving Mental Health Decision Support

- **作者**: Eranga Bandara, Asanga Gunaratna, Ross Gore, Anita H. Clayton, Christopher K. Rhea
- **发布日期**: 2026-04-20
- **链接**: [arXiv:2604.18302v1](https://arxiv.org/abs/2604.18302v1) | [PDF](https://arxiv.org/pdf/2604.18302v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

Privacy represents one of the most critical yet underaddressed barriers to AI adoption in mental healthcare -- particularly in high-sensitivity operational environments such as military, correctional, and remote healthcare settings, where the risk of patient data exposure can deter help-seeking behavior entirely.

Existing AI-enabled psychiatric decision support systems predominantly rely on cloud-based inference pipelines, requiring sensitive patient data to leave the device and traverse external servers, creating unacceptable privacy and security risks in these contexts.

In this paper, we pro

### AI 总结

总结生成失败

---

## 4. Spectral bandits for smooth graph functions

- **作者**: Michal Valko, Rémi Munos, Branislav Kveton, Tomáš Kocák
- **发布日期**: 2026-04-20
- **链接**: [arXiv:2604.18420v1](https://arxiv.org/abs/2604.18420v1) | [PDF](https://arxiv.org/pdf/2604.18420v1)
- **分类**: stat.ML, cs.LG
- **含金量**: 20/43 分

### 摘要

Smooth functions on graphs have wide applications in manifold and semi-supervised learning.

In this paper, we study a bandit problem where the payoffs of arms are smooth on a graph.

This framework is suitable for solving online learning problems that involve graphs, such as content-based recommendation.

In this problem, each item we can recommend is a node and its expected rating is similar to its neighbors.

The goal is to recommend items that have high expected ratings.

We aim for the algorithms where the cumulative regret with respect to the optimal policy would not scale poorly with the num

### AI 总结

总结生成失败

---

## 5. ATANT: An Evaluation Framework for AI Continuity

- **作者**: Samuel Sameer Tanguturi
- **发布日期**: 2026-04-08
- **链接**: [arXiv:2604.06710v2](https://arxiv.org/abs/2604.06710v2) | [PDF](https://arxiv.org/pdf/2604.06710v2)
- **分类**: cs.AI, cs.IR
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/Kenotic-Labs/ATANT.) ⭐ 0

### 摘要

We present ATANT (Automated Test for Acceptance of Narrative Truth), an open evaluation framework for measuring continuity in AI systems: the ability to persist, update, disambiguate, and reconstruct meaningful context across time.

While the AI industry has produced memory components (RAG pipelines, vector databases, long context windows, profile layers), no published framework formally defines or measures whether these components produce genuine continuity.

We define continuity as a system property with 7 required properties, introduce a 10-checkpoint evaluation methodology that operates with

### AI 总结

总结生成失败

---

## 6. Active Inference-Based Adaptive Routing for Heterogeneous Edge AI Services

- **作者**: Zihang Wang, Boris Sedlak, Schahram Dustdar
- **发布日期**: 2026-04-19
- **链接**: [arXiv:2604.17373v1](https://arxiv.org/abs/2604.17373v1) | [PDF](https://arxiv.org/pdf/2604.17373v1)
- **分类**: cs.DC, cs.ET, cs.PF
- **含金量**: 20/43 分

### 摘要

Edge computing enables AI inference closer to data sources, reducing latency and bandwidth costs.

However, orchestrating AI services across the cloud-edge continuum remains challenging due to dynamic workloads and infrastructure variability.

We present AIF-Router, an Active Inference--based routing framework that autonomously learns to balance latency, throughput, and resource utilization across multi-tier AI services without offline training.

AIF-Router performs Bayesian state inference and expected free energy minimization to guide routing decisions based on observability-driven real-time me

### AI 总结

总结生成失败

---

## 7. Federation over Text: Insight Sharing for Multi-Agent Reasoning

- **作者**: Dixi Yao, Tahseen Rabbani, Tian Li
- **发布日期**: 2026-04-18
- **链接**: [arXiv:2604.16778v1](https://arxiv.org/abs/2604.16778v1) | [PDF](https://arxiv.org/pdf/2604.16778v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

LLM-powered agents often reason from scratch when presented with a new problem instance and lack automatic mechanisms to transfer learned skills to other agents.

We propose a federated learning-like framework, Federation over Text (FoT), that enables multiple agents solving different tasks to collectively generate a shared library of metacognitive insights by iteratively federating their local reasoning processes.

Instead of federation over gradients (e.g., as in distributed training), FoT operates at the semantic level without any gradient optimization or supervision signal.

Iteratively, each

### AI 总结

总结生成失败

---

## 8. POLAR: Online Learning for LoRA Adapter Caching and Routing in Edge LLM Serving

- **作者**: Shaoang Li, Jian Li
- **发布日期**: 2026-04-17
- **链接**: [arXiv:2604.16583v1](https://arxiv.org/abs/2604.16583v1) | [PDF](https://arxiv.org/pdf/2604.16583v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

Edge deployment of large language models (LLMs) increasingly relies on libraries of lightweight LoRA adapters, yet GPU/DRAM can keep only a small resident subset at a time.

Serving a request through a non-resident adapter requires paging its weights from storage, incurring measurable latency.

This creates a two-timescale online control problem: on a slow timescale, the system selects which adapters remain resident in fast memory, while on a fast timescale it routes each request to an adapter whose context-dependent utility is unknown a priori.

The two decisions are tightly coupled: the cache d

### AI 总结

总结生成失败

---

## 9. Scalable and Adaptive Parallel Training of Graph Transformer on Large Graphs

- **作者**: Jun-Liang Lin, Kamesh Madduri, Mahmut Taylan Kandemir
- **发布日期**: 2026-04-17
- **链接**: [arXiv:2604.16715v1](https://arxiv.org/abs/2604.16715v1) | [PDF](https://arxiv.org/pdf/2604.16715v1)
- **分类**: cs.DC, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

Graph foundation models have demonstrated remarkable adaptability across diverse downstream tasks through large-scale pretraining on graphs.

However, existing implementations of the backbone model, graph transformers, are typically limited to single-GPU systems, leading to long training times or out-of-memory issues on large graphs.

Moreover, parallelizing graph transformer training over the full graph is challenging, as efficiency depends heavily on both the graph structure and system characteristics, such as bandwidth and memory capacity.

In this work, we introduce a distributed training f

### AI 总结

总结生成失败

---

## 10. A Lightweight Transformer for Pain Recognition from Brain Activity

- **作者**: Stefanos Gkikas, Christian Arzate Cruz, Yu Fang, Lu Cao, Muhammad Umar Khan
- **发布日期**: 2026-04-13
- **链接**: [arXiv:2604.16491v1](https://arxiv.org/abs/2604.16491v1) | [PDF](https://arxiv.org/pdf/2604.16491v1)
- **分类**: cs.CV, cs.AI
- **含金量**: 20/43 分

### 摘要

Pain is a multifaceted and widespread phenomenon with substantial clinical and societal burden, making reliable automated assessment a critical objective.

This paper presents a lightweight transformer architecture that fuses multiple fNIRS representations through a unified tokenization mechanism, enabling joint modeling of complementary signal views without requiring modality-specific adaptations or increasing architectural complexity.

The proposed token-mixing strategy preserves spatial, temporal, and time-frequency characteristics by projecting heterogeneous inputs onto a shared latent repre

### AI 总结

总结生成失败

---

