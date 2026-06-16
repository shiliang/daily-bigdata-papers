# 大数据+AI 领域论文日报

**日期**: 2026-06-16

**论文数量**: 7 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Tangram: Hiding GPU Heterogeneity f...](https://arxiv.org/abs/2606.16907v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Binary Decompilation LLM with Feedb...](https://arxiv.org/abs/2606.16162v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [PVminerLLM2: Improving Structured E...](https://arxiv.org/abs/2606.16074v1) | 待分析 | 评估失败 | [Code](https://github.com/Data-Mining-Lab-Yale/PVminerLLM2) | 20/43 |
| 4 | [Directory-Aware Query and Maintenan...](https://arxiv.org/abs/2606.16903v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Modeling Nonlinear Ability Trajecto...](https://arxiv.org/abs/2606.15525v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [NEURON-Fabric: CXL-Side Low-Bit Gra...](https://arxiv.org/abs/2606.15045v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Policy Regret for Embedding Model R...](https://arxiv.org/abs/2606.14929v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Tangram: Hiding GPU Heterogeneity for Efficient LLM Parallelization

- **作者**: Yanda Tao, Pedro F. Silvestre, Marcel Wagenländer, Peter Pietzuch
- **发布日期**: 2026-06-15
- **链接**: [arXiv:2606.16907v1](https://arxiv.org/abs/2606.16907v1) | [PDF](https://arxiv.org/pdf/2606.16907v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

The scale of LLM training jobs requires parallelization planning over large GPU clusters.

Due to different GPU types and interconnects added over time, these GPU clusters are increasingly heterogeneous.

Automatic LLM parallelizers can search for parallelization plans but face an exploding search space with heterogeneous GPUs.

To make search tractable in heterogeneous GPU clusters, parallelizers often omit types of parallelism (e.g., expert parallelism) or memory-saving techniques (e.g., ZeRO), which results in worse plans.

We describe Tangram, a system that enables the use of existing hetero

### AI 总结

总结生成失败

---

## 2. Binary Decompilation LLM with Feedback-Driven Multi-Turn Refinement

- **作者**: Peipei Liu, Jian Sun, Mingzhe Xing, Yicheng Zeng, Zhaoteng Yan
- **发布日期**: 2026-06-15
- **链接**: [arXiv:2606.16162v1](https://arxiv.org/abs/2606.16162v1) | [PDF](https://arxiv.org/pdf/2606.16162v1)
- **分类**: cs.SE
- **含金量**: 20/43 分

### 摘要

Binary decompilation is fundamental to security tasks such as vulnerability discovery, malware inspection, and executable-only program understanding.

Recent LLM-based decompilation methods have shown promising results, but most still follow a single-turn generation paradigm: given assembly code or decompiler-produced pseudo-code, the model generates one output and stops.

Consequently, the generated code may appear readable or even compile successfully, yet still deviate from the behavior of the original binary and mislead downstream analysis.

This paper presents AutoDecompiler, a decompilati

### AI 总结

总结生成失败

---

## 3. PVminerLLM2: Improving Structured Extraction of Patient Voice via Preference Optimization

- **作者**: Samah Fodeh, Linhai Ma, Ganesh Puthiaraju, Srivani Talakokkul, Afshan Khan
- **发布日期**: 2026-06-15
- **链接**: [arXiv:2606.16074v1](https://arxiv.org/abs/2606.16074v1) | [PDF](https://arxiv.org/pdf/2606.16074v1)
- **分类**: cs.CL, cs.AI
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/Data-Mining-Lab-Yale/PVminerLLM2) ⭐ 0 (Python)

### 摘要

Motivation: Patient-generated text contains critical information on patients' lived experiences, social context, and care engagement, but remains largely unstructured, limiting its use in patient-centered outcomes research.

Prior work introduced the PV-Miner benchmark and PVMinerLLM models for structured extraction.

However, supervised fine-tuning (SFT) alone struggles with rare, fine-grained, and unevenly distributed errors, particularly in token-critical structured outputs.

Results: We present PVminerLLM2, an improved set of LLMs for structured patient voice extraction that applies prefere

### AI 总结

总结生成失败

---

## 4. Directory-Aware Query and Maintenance in Vector Databases

- **作者**: Mengzhao Wang, Zheng Gong, Jingpei Hu, Jiajie Fu, Maojia Sheng
- **发布日期**: 2026-06-15
- **链接**: [arXiv:2606.16903v1](https://arxiv.org/abs/2606.16903v1) | [PDF](https://arxiv.org/pdf/2606.16903v1)
- **分类**: cs.DB
- **含金量**: 20/43 分

### 摘要

Vector databases typically manage metadata as flat scalar attributes, which limits their ability to express hierarchical directory semantics commonly used to organize code repositories, enterprise documents, and agent memories.

As a result, directory-scoped retrieval and structural updates are often implemented as application-layer workarounds, making recursive scope resolution expensive and directory maintenance difficult to keep consistent.

This paper studies native directory semantics as a first-class capability for vector databases.

We formalize two core operators: Directory-Semantic Query

### AI 总结

总结生成失败

---

## 5. Modeling Nonlinear Ability Trajectories and Learner Heterogeneity in Online Learning: A Bayesian Nonparametric Dynamic IRT Framework

- **作者**: Zhihua Ma, Alice Xu, Icy Zhang, Guanyu Hu
- **发布日期**: 2026-06-14
- **链接**: [arXiv:2606.15525v1](https://arxiv.org/abs/2606.15525v1) | [PDF](https://arxiv.org/pdf/2606.15525v1)
- **分类**: stat.AP, stat.ME
- **含金量**: 20/43 分

### 摘要

Online learning has amplified the need to understand how student engagement patterns influence learning outcomes, particularly given the flexibility of technology-mediated environments.

To address this, we propose a Bayesian nonparametric dynamic item response theory (IRT) framework that tracks within-individual ability trajectories across instructional units.

The proposed model integrates B-spline basis expansions to capture nonlinear effects of engagement behaviors on ability drift, alongside a Mixture-of-Finite-Mixtures (MFM) prior to automatically determine the number of latent learner clu

### AI 总结

总结生成失败

---

## 6. NEURON-Fabric: CXL-Side Low-Bit Gradient Aggregation for Distributed Training

- **作者**: Ziqiang Wang, Changcheng Huang, Chung-Horng Lung
- **发布日期**: 2026-06-13
- **链接**: [arXiv:2606.15045v1](https://arxiv.org/abs/2606.15045v1) | [PDF](https://arxiv.org/pdf/2606.15045v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

In large-model distributed training, especially large language model workloads, gradient All-Reduce increasingly stresses the memory and communication path.

This paper asks whether a Compute Express Link (CXL) memory controller can aggregate low-bit gradient signals as gradient cache lines pass through it, while preserving a 32-bit floating-point (FP32) path for workloads, layers, or phases that should not use low-bit approximation.

We present NEURON-Fabric, a CXL-side controller architecture that performs packed gradient-binary (G-Binary) sign-count aggregation and gradient-ternary (G-Ternary

### AI 总结

总结生成失败

---

## 7. Policy Regret for Embedding Model Routing: Contextual Bandits with Low-Rank Experts

- **作者**: Yan Dai, Negin Golrezaei, Patrick Jaillet
- **发布日期**: 2026-06-12
- **链接**: [arXiv:2606.14929v1](https://arxiv.org/abs/2606.14929v1) | [PDF](https://arxiv.org/pdf/2606.14929v1)
- **分类**: cs.LG, cs.AI, stat.ML
- **含金量**: 20/43 分

### 摘要

Modern recommendation systems increasingly rely on dynamically routing diverse queries to multiple embedding models.

Despite its practical significance, this problem remains poorly understood under realistic conditions like adversarial queries, bandit feedback, and limited observability of models.

We formalize embedding model routing as an adversarial contextual linear bandit with low-rank experts, where contexts are queries, actions are items, and experts are the embedding models working on low-rank latent representation spaces.

We first establish that standard regret notions suffer from stru

### AI 总结

总结生成失败

---

