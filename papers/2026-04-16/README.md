# 大数据+AI 领域论文日报

**日期**: 2026-04-16

**论文数量**: 8 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [TREX: Automating LLM Fine-tuning vi...](https://arxiv.org/abs/2604.14116v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Do We Still Need Humans in the Loop...](https://arxiv.org/abs/2604.13899v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [SparseBalance: Load-Balanced Long C...](https://arxiv.org/abs/2604.13847v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [SAKURAONE: An Open Ethernet-Based A...](https://arxiv.org/abs/2604.13600v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Rag Performance Prediction for Ques...](https://arxiv.org/abs/2604.07985v2) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Online learning with noisy side obs...](https://arxiv.org/abs/2604.13740v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [SemiFA: An Agentic Multi-Modal Fram...](https://arxiv.org/abs/2604.13236v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [LPM 1.0: Video-based Character Perf...](https://arxiv.org/abs/2604.07823v2) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration

- **作者**: Zerun Ma, Guoqiang Wang, Xinchen Xie, Yicheng Chen, He Du
- **发布日期**: 2026-04-15
- **链接**: [arXiv:2604.14116v1](https://arxiv.org/abs/2604.14116v1) | [PDF](https://arxiv.org/pdf/2604.14116v1)
- **分类**: cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

While Large Language Models (LLMs) have empowered AI research agents to perform isolated scientific tasks, automating complex, real-world workflows, such as LLM training, remains a significant challenge.

In this paper, we introduce TREX, a multi-agent system that automates the entire LLM training life-cycle.

By orchestrating collaboration between two core modules-the Researcher and the Executor-the system seamlessly performs requirement analysis, open-domain literature and data research, formulation of training strategies, preparation of data recipes, and model training and evaluation.

The mul

### AI 总结

总结生成失败

---

## 2. Do We Still Need Humans in the Loop? Comparing Human and LLM Annotation in Active Learning for Hostility Detection

- **作者**: Ahmad Dawar Hakimi, Lea Hirlimann, Isabelle Augenstein, Hinrich Schütze
- **发布日期**: 2026-04-15
- **链接**: [arXiv:2604.13899v1](https://arxiv.org/abs/2604.13899v1) | [PDF](https://arxiv.org/pdf/2604.13899v1)
- **分类**: cs.CL, cs.AI
- **含金量**: 20/43 分

### 摘要

Instruction-tuned LLMs can annotate thousands of instances from a short prompt at negligible cost.

This raises two questions for active learning (AL): can LLM labels replace human labels within the AL loop, and does AL remain necessary when entire corpora can be labelled at once? We investigate both questions on a new dataset of 277,902 German political TikTok comments (25,974 LLM-labelled, 5,000 human-annotated), comparing seven annotation strategies across four encoders to detect anti-immigrant hostility.

A classifier trained on 25,974 GPT-5.2 labels (\$43) achieves comparable F1-Macro to on

### AI 总结

总结生成失败

---

## 3. SparseBalance: Load-Balanced Long Context Training with Dynamic Sparse Attention

- **作者**: Hongtao Xu, Jianchao Tan, Yuxuan Hu, Pengju Lu, Hongyu Wang
- **发布日期**: 2026-04-15
- **链接**: [arXiv:2604.13847v1](https://arxiv.org/abs/2604.13847v1) | [PDF](https://arxiv.org/pdf/2604.13847v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

While sparse attention mitigates the computational bottleneck of long-context LLM training, its distributed training process exhibits extreme heterogeneity in both \textit{1)} sequence length and \textit{2)} sparsity sensitivity, leading to a severe imbalance problem and sub-optimal model accuracy.

Existing algorithms and training frameworks typically focus on single issue, failing to systematically co-optimize these two problems.

Therefore, we propose SparseBalance, a novel algorithm-system co-design framework, which exploits the sparsity and sequence heterogeneity to optimize model accuracy 

### AI 总结

总结生成失败

---

## 4. SAKURAONE: An Open Ethernet-Based AI HPC System and Its Observed Workload Dynamics in a Single-Tenant LLM Development Environment

- **作者**: Fumikazu Konishi, Yuuki Tsubouchi, Hirofumi Tsuruta
- **发布日期**: 2026-04-15
- **链接**: [arXiv:2604.13600v1](https://arxiv.org/abs/2604.13600v1) | [PDF](https://arxiv.org/pdf/2604.13600v1)
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

## 5. Rag Performance Prediction for Question Answering

- **作者**: Or Dado, David Carmel, Oren Kurland
- **发布日期**: 2026-04-09
- **链接**: [arXiv:2604.07985v2](https://arxiv.org/abs/2604.07985v2) | [PDF](https://arxiv.org/pdf/2604.07985v2)
- **分类**: cs.CL, cs.IR
- **含金量**: 20/43 分

### 摘要

We address the task of predicting the gain of using RAG (retrieval augmented generation) for question answering with respect to not using it.

We study the performance of a few pre-retrieval and post-retrieval predictors originally devised for ad hoc retrieval.

We also study a few post-generation predictors, one of which is novel to this study and posts the best prediction quality.

Our results show that the most effective prediction approach is a novel supervised predictor that explicitly models the semantic relationships among the question, retrieved passages, and the generated answer.

### AI 总结

总结生成失败

---

## 6. Online learning with noisy side observations

- **作者**: Tomáš Kocák, Gergely Neu, Michal Valko
- **发布日期**: 2026-04-15
- **链接**: [arXiv:2604.13740v1](https://arxiv.org/abs/2604.13740v1) | [PDF](https://arxiv.org/pdf/2604.13740v1)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

We propose a new partial-observability model for online learning problems where the learner, besides its own loss, also observes some noisy feedback about the other actions, depending on the underlying structure of the problem.

We represent this structure by a weighted directed graph, where the edge weights are related to the quality of the feedback shared by the connected nodes.

Our main contribution is an efficient algorithm that guarantees a regret of $\widetilde{O}(\sqrt{α^* T})$ after $T$ rounds, where $α^*$ is a novel graph property that we call the effective independence number.

Our alg

### AI 总结

总结生成失败

---

## 7. SemiFA: An Agentic Multi-Modal Framework for Autonomous Semiconductor Failure Analysis Report Generation

- **作者**: Shivam Chand Kaushik
- **发布日期**: 2026-04-14
- **链接**: [arXiv:2604.13236v1](https://arxiv.org/abs/2604.13236v1) | [PDF](https://arxiv.org/pdf/2604.13236v1)
- **分类**: cs.CV, cs.AI, eess.IV
- **含金量**: 20/43 分

### 摘要

Semiconductor failure analysis (FA) requires engineers to examine inspection images, correlate equipment telemetry, consult historical defect records, and write structured reports, a process that can consume several hours of expert time per case.

We present SemiFA, an agentic multi-modal framework that autonomously generates structured FA reports from semiconductor inspection images in under one minute.

SemiFA decomposes FA into a four-agent LangGraph pipeline: a DefectDescriber that classifies and narrates defect morphology using DINOv2 and LLaVA-1.6, a RootCauseAnalyzer that fuses SECS/GEM e

### AI 总结

总结生成失败

---

## 8. LPM 1.0: Video-based Character Performance Model

- **作者**: Ailing Zeng, Casper Yang, Chauncey Ge, Eddie Zhang, Garvey Xu
- **发布日期**: 2026-04-09
- **链接**: [arXiv:2604.07823v2](https://arxiv.org/abs/2604.07823v2) | [PDF](https://arxiv.org/pdf/2604.07823v2)
- **分类**: cs.CV, cs.AI, cs.MM
- **含金量**: 20/43 分

### 摘要

Performance, the externalization of intent, emotion, and personality through visual, vocal, and temporal behavior, is what makes a character alive.

Learning such performance from video is a promising alternative to traditional 3D pipelines.

However, existing video models struggle to jointly achieve high expressiveness, real-time inference, and long-horizon identity stability, a tension we call the performance trilemma.

Conversation is the most comprehensive performance scenario, as characters simultaneously speak, listen, react, and emote while maintaining identity over time.

To address this, 

### AI 总结

总结生成失败

---

