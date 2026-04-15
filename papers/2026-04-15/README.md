# 大数据+AI 领域论文日报

**日期**: 2026-04-15

**论文数量**: 7 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [MoshiRAG: Asynchronous Knowledge Re...](https://arxiv.org/abs/2604.12928v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [LightTune: Lightweight Forward-Only...](https://arxiv.org/abs/2604.12406v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Aethon: A Reference-Based Replicati...](https://arxiv.org/abs/2604.12129v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Offline-Online Reinforcement Learni...](https://arxiv.org/abs/2604.11994v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Predictive Bayesian Arbitration: A ...](https://arxiv.org/abs/2604.11989v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Evaluating Cross-Architecture Perfo...](https://arxiv.org/abs/2604.12090v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [GRACE: A Dynamic Coreset Selection ...](https://arxiv.org/abs/2604.11810v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. MoshiRAG: Asynchronous Knowledge Retrieval for Full-Duplex Speech Language Models

- **作者**: Chung-Ming Chien, Manu Orsini, Eugene Kharitonov, Neil Zeghidour, Karen Livescu
- **发布日期**: 2026-04-14
- **链接**: [arXiv:2604.12928v1](https://arxiv.org/abs/2604.12928v1) | [PDF](https://arxiv.org/pdf/2604.12928v1)
- **分类**: cs.CL, eess.AS
- **含金量**: 20/43 分

### 摘要

Speech-to-speech language models have recently emerged to enhance the naturalness of conversational AI.

In particular, full-duplex models are distinguished by their real-time interactivity, including handling of pauses, interruptions, and backchannels.

However, improving their factuality remains an open challenge.

While scaling the model size could address this gap, it would make real-time inference prohibitively expensive.

In this work, we propose MoshiRAG, a modular approach that combines a compact full-duplex interface with selective retrieval to access more powerful knowledge sources.

Our 

### AI 总结

总结生成失败

---

## 2. LightTune: Lightweight Forward-Only Online Fine-Tuning with Applications to Link Adaptation

- **作者**: Ramy E. Ali, Federico Penna
- **发布日期**: 2026-04-14
- **链接**: [arXiv:2604.12406v1](https://arxiv.org/abs/2604.12406v1) | [PDF](https://arxiv.org/pdf/2604.12406v1)
- **分类**: cs.NI
- **含金量**: 20/43 分

### 摘要

Deploying machine learning (ML) algorithms on mobile phones is bottlenecked by performance degradation under dynamic, real-world conditions that differ from the offline training conditions.

While continual learning and adaptation are essential to mitigate this distributional shift, conventional online learning methods are often computationally prohibitive for resource-constrained devices.

In this paper, we propose LightTune, a lightweight, backpropagation-free online fine-tuning framework with provable convergence guarantees.

LightTune opportunistically refines ML models using live test-time d

### AI 总结

总结生成失败

---

## 3. Aethon: A Reference-Based Replication Primitive for Constant-Time Instantiation of Stateful AI Agents

- **作者**: Swanand Rao, Kiran Kashalkar, Parvathi Somashekar, Priya Krishnan
- **发布日期**: 2026-04-13
- **链接**: [arXiv:2604.12129v1](https://arxiv.org/abs/2604.12129v1) | [PDF](https://arxiv.org/pdf/2604.12129v1)
- **分类**: cs.AI, cs.AR, cs.DC, cs.MA
- **含金量**: 20/43 分

### 摘要

The transition from stateless model inference to stateful agentic execution is reshaping the systems assumptions underlying modern AI infrastructure.

While large language models have made persistent, tool-using, and collaborative agents technically viable, existing runtime architectures remain constrained by materialization-heavy instantiation models that impose significant latency and memory overhead.

This paper introduces Aethon, a reference-based replication primitive for near-constant-time instantiation of stateful AI agents.

Rather than reconstructing agents as fully materialized object

### AI 总结

总结生成失败

---

## 4. Offline-Online Reinforcement Learning for Linear Mixture MDPs

- **作者**: Zhongjun Zhang, Sean R. Sinclair
- **发布日期**: 2026-04-13
- **链接**: [arXiv:2604.11994v1](https://arxiv.org/abs/2604.11994v1) | [PDF](https://arxiv.org/pdf/2604.11994v1)
- **分类**: cs.LG, math.OC, stat.ML
- **含金量**: 20/43 分

### 摘要

We study offline-online reinforcement learning in linear mixture Markov decision processes (MDPs) under environment shift.

In the offline phase, data are collected by an unknown behavior policy and may come from a mismatched environment, while in the online phase the learner interacts with the target environment.

We propose an algorithm that adaptively leverages offline data.

When the offline data are informative, either due to sufficient coverage or small environment shift, the algorithm provably improves over purely online learning.

When the offline data are uninformative, it safely ignores 

### AI 总结

总结生成失败

---

## 5. Predictive Bayesian Arbitration: A Scalable Noisy-OR Model with Service Criticality Awareness

- **作者**: Anil Jangam, Ganesh Karthick Rajendran, Roy Kantharajah
- **发布日期**: 2026-04-13
- **链接**: [arXiv:2604.11989v1](https://arxiv.org/abs/2604.11989v1) | [PDF](https://arxiv.org/pdf/2604.11989v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Geographically High-Available (Geo-HA) cluster systems are essential for service continuity in distributed cloud-native environments.

However, traditional arbitration mechanisms, which are often predicated on deterministic node-level heartbeats, are resource-intensive and inherently reactive.

This necessitates a dedicated arbiter per deployment and leads to reactive switchovers that incur unavoidable downtime, occurring only after a failure has already compromised the system.

This paper presents a novel predictive arbitration framework that utilizes a shared, microservice-based architecture to

### AI 总结

总结生成失败

---

## 6. Evaluating Cross-Architecture Performance Modeling of Distributed ML Workloads Using StableHLO

- **作者**: Jonas Svedas, Nathan Laubeuf, Ryan Harvey, Arjun Singh, Changhai Man
- **发布日期**: 2026-04-13
- **链接**: [arXiv:2604.12090v1](https://arxiv.org/abs/2604.12090v1) | [PDF](https://arxiv.org/pdf/2604.12090v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Predicting the performance of large-scale distributed machine learning (ML) workloads across multiple accelerator architectures remains a central challenge in ML system design.

Existing GPU and TPU focused simulators are typically architecture-specific, while distributed training simulators rely on workload-specific analytical models or costly post-execution traces, limiting portability and cross-platform comparison.

This work evaluates whether MLIR's StableHLO dialect can serve as a unified workload representation for cross-architecture and cross-fidelity performance modeling of distributed M

### AI 总结

总结生成失败

---

## 7. GRACE: A Dynamic Coreset Selection Framework for Large Language Model Optimization

- **作者**: Tianhao Tang, Haoyang Li, Lei Chen
- **发布日期**: 2026-04-09
- **链接**: [arXiv:2604.11810v1](https://arxiv.org/abs/2604.11810v1) | [PDF](https://arxiv.org/pdf/2604.11810v1)
- **分类**: cs.DB, cs.AI
- **含金量**: 20/43 分

### 摘要

Large Language Models (LLMs) have demonstrated remarkable capabilities in natural language understanding and generation.

However, their immense number of parameters and complex transformer-based architectures result in significant resource demands and computational complexity during training, making it challenging to optimize them efficiently on large datasets.

To reduce training costs while preserving performance, researchers have investigated coreset selection techniques, which aim to identify small, representative subsets of the entire training dataset to accelerate LLM training.

However, e

### AI 总结

总结生成失败

---

