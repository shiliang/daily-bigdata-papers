# 大数据+AI 领域论文日报

**日期**: 2026-06-23

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Have You Ever Seen Them? Entity-lev...](https://arxiv.org/abs/2606.23030v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [FORGE: Fused On-Register Gradient E...](https://arxiv.org/abs/2606.22932v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [RLM-Cascade: Response-Level Specula...](https://arxiv.org/abs/2606.22840v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Cross-lingual Retrieval-Augmented C...](https://arxiv.org/abs/2606.22910v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [GitOfThoughts: Version-Controlled R...](https://arxiv.org/abs/2606.14470v2) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [RT-DocLayout: Real-Time End-to-End ...](https://arxiv.org/abs/2606.23344v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Flow6D: Discrete-to-Continuous Flow...](https://arxiv.org/abs/2606.23293v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Leveraging Similarities in Multi-Ar...](https://arxiv.org/abs/2606.23414v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [DT-GOL: Dual-Track Geometric Online...](https://arxiv.org/abs/2606.22950v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [FlowTrain: Flow-Based Decoupled Tra...](https://arxiv.org/abs/2606.23087v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Have You Ever Seen Them? Entity-level Membership Inference through Interrogating Large Language Models

- **作者**: Yiran Zhu, Ziqi Yang
- **发布日期**: 2026-06-22
- **链接**: [arXiv:2606.23030v1](https://arxiv.org/abs/2606.23030v1) | [PDF](https://arxiv.org/pdf/2606.23030v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

Large Language Models (LLMs) raise growing concerns about privacy leakage and copyright compliance.

Membership inference is a key tool for assessing such risks, but existing studies mainly focus on whether specific samples or sample-based data units are used for training.

We argue that LLMs exhibit a human-memory-like behavior: an LLM may not memorize a specific sample verbatim, yet it can accumulate and reveal knowledge about a real-world entity from scattered mentions.

This analogy motivates us to examine whether an LLM can be interrogated like a human interviewee to reveal its exposure to e

### AI 总结

总结生成失败

---

## 2. FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training

- **作者**: Dikshant Kukreja, Kritarth Prasad, Avinash Anand, Zhengkui Wang, Erik Cambria
- **发布日期**: 2026-06-22
- **链接**: [arXiv:2606.22932v1](https://arxiv.org/abs/2606.22932v1) | [PDF](https://arxiv.org/pdf/2606.22932v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Reverse-mode differentiation computes every weight gradient, writes it to memory, and only then lets the optimizer read it back.

This two-phase schedule sets the memory ceiling of modern training: at the seam between the phases, every layer's gradient is live at once.

We argue that this materialized gradient is an artifact of how differentiation is staged, not a quantity that learning requires -- and we eliminate it.

FORGE folds the optimizer step into the backward pass and applies it one tile at a time, entirely in registers, so each gradient tile is consumed the instant it is produced and ne

### AI 总结

总结生成失败

---

## 3. RLM-Cascade: Response-Level Speculative Decoding for Cost-Efficient LLM API Serving

- **作者**: Haifeng Wu, Srinivasan Manoharan, Fangbo Tu, Junhua Zhao, Jian Wan
- **发布日期**: 2026-06-22
- **链接**: [arXiv:2606.22840v1](https://arxiv.org/abs/2606.22840v1) | [PDF](https://arxiv.org/pdf/2606.22840v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

We present RLM-Cascade, a proxy-layer system that applies speculative decoding at the response level to reduce LLM API costs without requiring model architecture access or a shared vocabulary.

A fast, inexpensive draft model generates a candidate response; a capable verify model accepts, enhances, or is bypassed entirely depending on a lightweight complexity router.

On a real-world agentic coding workload (Claude Code), RLM-Cascade achieves a draft-use rate of 88.8% across 125 production requests, reducing API cost by 45.8% relative to a direct Opus baseline.

Counter-intuitively, the proxy als

### AI 总结

总结生成失败

---

## 4. Cross-lingual Retrieval-Augmented Classification for Dysarthria Severity Assessment

- **作者**: Taeyoung Jeong, Insung Lee, Du-Seong Chang, Myoung-Wan Koo
- **发布日期**: 2026-06-22
- **链接**: [arXiv:2606.22910v1](https://arxiv.org/abs/2606.22910v1) | [PDF](https://arxiv.org/pdf/2606.22910v1)
- **分类**: cs.SD, cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

Automatic dysarthria severity assessment is limited by the scarcity of labeled pathological speech data.

To address this, we propose Cross-lingual Retrieval-Augmented Classification (CRAC), which leverages speech from a different language via an align-retrieve-fuse pipeline.

Supervised contrastive learning first shapes a severity-focused embedding space, then a vector database is built from the opposite-language corpus.

During both training and inference, the classifier retrieves top-k references from the aligned space and fuses them with the input via cross-attention.

Evaluated on Korean post

### AI 总结

总结生成失败

---

## 5. GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge

- **作者**: Pavan C Shekar, Abhishek H S, Aswanth Krishnan
- **发布日期**: 2026-06-12
- **链接**: [arXiv:2606.14470v2](https://arxiv.org/abs/2606.14470v2) | [PDF](https://arxiv.org/pdf/2606.14470v2)
- **分类**: cs.AI, cs.CL, cs.LG
- **含金量**: 20/43 分

### 摘要

Large language model reasoning leaves no trace once it is done.

The steps of a chain of thought disappear when the context window closes, a pruned search branch is just gone, and memory buffers cannot be diffed, merged, or audited.

Code, infrastructure, and experiments are all version-controlled.

Reasoning is not.

GitOfThoughts stores an agent's reasoning tree as a git repository.

Every scored thought becomes a commit, scores become notes, outcomes become tags, and retrieval is just git log over the agent's own history.

We use this to test something simple.

Does giving an agent memory from pas

### AI 总结

总结生成失败

---

## 6. RT-DocLayout: Real-Time End-to-End Document Layout Analysis with Reading Order in the Wild

- **作者**: Cheng Cui, Tingquan Gao, Xueqing Wang, Changda Zhou, Hongen Liu
- **发布日期**: 2026-06-22
- **链接**: [arXiv:2606.23344v1](https://arxiv.org/abs/2606.23344v1) | [PDF](https://arxiv.org/pdf/2606.23344v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

Accurate document layout analysis remains a critical bottleneck for document parsing systems, due to the intricate coupling among heterogeneous document layout elements, geometric distortions (\eg, paper warping and bending, perspective variations), and reading order within diverse layout structures.

Existing approaches typically rely on fragmented multi-stage pipelines or computationally heavy generative Transformer architectures, leading to error propagation and limited efficiency.

In this paper, we present RT-DocLayout, a highly efficient end-to-end framework for document layout analysis,

### AI 总结

总结生成失败

---

## 7. Flow6D: Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-Level 6D Pose Estimation

- **作者**: Mingyu Mei, Li Zhang, Zibo Dai, Han Sun, Xinyue Zhao
- **发布日期**: 2026-06-22
- **链接**: [arXiv:2606.23293v1](https://arxiv.org/abs/2606.23293v1) | [PDF](https://arxiv.org/pdf/2606.23293v1)
- **分类**: cs.CV, cs.RO
- **含金量**: 20/43 分

### 摘要

6D pose estimation is a key task in computer vision and embodied AI, widely used in robotic manipulation, augmented reality, etc.

Existing methods directly regress in a high-dimensional continuous space, facing two key challenges in category-level pose estimation: limited accuracy due to noise and local optima, and inefficient search over an infinite space that hinders real-time performance.

This paper proposes Flow6D, a hierarchical flow matching framework with a two-stage discrete latent space localization-continuous pose regression strategy.

Rotation and translation parameters are first dis

### AI 总结

总结生成失败

---

## 8. Leveraging Similarities in Multi-Armed Bandits

- **作者**: Khaled Eldowa, Thibaud Rahier, Augustin Cablant, Panayotis Mertikopoulos, Pierre Gaillard
- **发布日期**: 2026-06-22
- **链接**: [arXiv:2606.23414v1](https://arxiv.org/abs/2606.23414v1) | [PDF](https://arxiv.org/pdf/2606.23414v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

In many online learning and bandit problems, the actions we consider possess inherent similarities--for instance because they share latent traits, tags, or hierarchical structure.

We study online learning with a similarity-structured action set, encoded by a rooted tree whose leaves are the actions and whose levels quantify how closely two actions are related.

The loss sequence is assumed tree-compatible: losses of similar actions are constrained to be close.

We establish an impossibility result showing that usual one-point bandit feedback cannot, in general, leverage range or tree-induced sim

### AI 总结

总结生成失败

---

## 9. DT-GOL: Dual-Track Geometric Online Learning in Nonstationary Environment with Label Delay

- **作者**: Yulin Wang, Yi He, Dianlong You, Di Wu
- **发布日期**: 2026-06-22
- **链接**: [arXiv:2606.22950v1](https://arxiv.org/abs/2606.22950v1) | [PDF](https://arxiv.org/pdf/2606.22950v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Online learning is crucial for handling complex data streams in big data applications.

Recent research has begun to focus on dynamic scenarios, i.e., non-stationary environments.

However, a crucial yet often overlooked aspect is label latency, where new data may not receive labels in time due to the slow and expensive labeling process, thus hindering rapid adaptation to dynamic environments.

To resolve this impasse, we propose Dual-Track Geometry Online Learning (DT-GOL), a novel framework that shifts from temporal compensation to spatial reasoning to bridge the supervised latency gap.

By mo

### AI 总结

总结生成失败

---

## 10. FlowTrain: Flow-Based Decoupled Training for Industrial-Grade Vision-Language Models

- **作者**: Zhida Jiang, Zhaolong Xing, Yang Pei, Xiaolong Chen, Yuanhang Xiao
- **发布日期**: 2026-06-22
- **链接**: [arXiv:2606.23087v1](https://arxiv.org/abs/2606.23087v1) | [PDF](https://arxiv.org/pdf/2606.23087v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Industrial-grade distributed training of vision-language models (VLMs) remains far less efficient than that of unimodal LLMs.

Existing solutions either follow a monolithic design that assigns uniform parallelism to heterogeneous modules or adopt a disaggregated deployment that separates modules while executing them as a batch-synchronized pipeline.

In this paper, we highlight that the above solutions are still not sufficient, and VLM training can be further decoupled.

To this end, we present FlowTrain, a flow-based decoupled training framework that reformulates VLM training as a producer-consu

### AI 总结

总结生成失败

---

