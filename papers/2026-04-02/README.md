# 大数据+AI 领域论文日报

**日期**: 2026-04-02

**论文数量**: 5 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [LLM REgression with a Latent Iterat...](https://arxiv.org/abs/2604.01206v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Exploring Silent Data Corruption as...](https://arxiv.org/abs/2604.00726v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Ontology-Constrained Neural Reasoni...](https://arxiv.org/abs/2604.00555v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Learning Humanoid Navigation from H...](https://arxiv.org/abs/2604.00416v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [EmbedPart: Embedding-Driven Graph P...](https://arxiv.org/abs/2604.01000v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. LLM REgression with a Latent Iterative State Head

- **作者**: Yiheng Su, Matthew Lease
- **发布日期**: 2026-04-01
- **链接**: [arXiv:2604.01206v1](https://arxiv.org/abs/2604.01206v1) | [PDF](https://arxiv.org/pdf/2604.01206v1)
- **分类**: cs.CL, cs.LG
- **含金量**: 20/43 分

### 摘要

We present RELISH (REgression with a Latent Iterative State Head), a novel, lightweight architecture designed for text regression with large language models.

Rather than decoding numeric targets as text or aggregating multiple generated outputs, RELISH predicts scalar values directly from frozen LLM representations by iteratively refining a learned latent state through cross-attention over token-level representations, and then mapping the final state to a point estimate with a linear regressor.

Across five datasets, four LLM backbones, and two LLM training regimes, RELISH consistently outperfo

### AI 总结

总结生成失败

---

## 2. Exploring Silent Data Corruption as a Reliability Challenge in LLM Training

- **作者**: Anton Altenbernd, Philipp Wiesner, Odej Kao
- **发布日期**: 2026-04-01
- **链接**: [arXiv:2604.00726v1](https://arxiv.org/abs/2604.00726v1) | [PDF](https://arxiv.org/pdf/2604.00726v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

As Large Language Models (LLMs) scale in size and complexity, the consequences of failures during training become increasingly severe.

A major challenge arises from Silent Data Corruption (SDC): hardware-induced faults that bypass system-level detection mechanisms.

SDC may behave like benign numerical noise, but can also cause harmful gradient corruption that leads to loss spikes, divergence, or stalled progress.

This work provides a controlled study of how intermittent SDC affects LLM pretraining.

Using targeted fault injection at the level of GPU matrix-multiply instructions, we characteri

### AI 总结

总结生成失败

---

## 3. Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents

- **作者**: Thanh Luong Tuan
- **发布日期**: 2026-04-01
- **链接**: [arXiv:2604.00555v1](https://arxiv.org/abs/2604.00555v1) | [PDF](https://arxiv.org/pdf/2604.00555v1)
- **分类**: cs.AI, cs.CL, cs.SE
- **含金量**: 20/43 分

### 摘要

Enterprise adoption of Large Language Models (LLMs) is constrained by hallucination, domain drift, and the inability to enforce regulatory compliance at the reasoning level.

We present a neurosymbolic architecture implemented within the Foundation AgenticOS (FAOS) platform that addresses these limitations through ontology-constrained neural reasoning.

Our approach introduces a three-layer ontological framework--Role, Domain, and Interaction ontologies--that provides formal semantic grounding for LLM-based enterprise agents.

We formalize the concept of asymmetric neurosymbolic coupling, wherein

### AI 总结

总结生成失败

---

## 4. Learning Humanoid Navigation from Human Data

- **作者**: Weizhuo Wang, Yanjie Ze, C. Karen Liu, Monroe Kennedy
- **发布日期**: 2026-04-01
- **链接**: [arXiv:2604.00416v1](https://arxiv.org/abs/2604.00416v1) | [PDF](https://arxiv.org/pdf/2604.00416v1)
- **分类**: cs.RO, cs.AI, cs.CV, cs.LG
- **含金量**: 20/43 分

### 摘要

We present EgoNav, a system that enables a humanoid robot to traverse diverse, unseen environments by learning entirely from 5 hours of human walking data, with no robot data or finetuning.

A diffusion model predicts distributions of plausible future trajectories conditioned on past trajectory, a 360 deg visual memory fusing color, depth, and semantics, and video features from a frozen DINOv3 backbone that capture appearance cues invisible to depth sensors.

A hybrid sampling scheme achieves real-time inference in 10 denoising steps, and a receding-horizon controller selects paths from the pred

### AI 总结

总结生成失败

---

## 5. EmbedPart: Embedding-Driven Graph Partitioning for Scalable Graph Neural Network Training

- **作者**: Nikolai Merkel, Ruben Mayer, Volker Markl, Hans-Arno Jacobsen
- **发布日期**: 2026-04-01
- **链接**: [arXiv:2604.01000v1](https://arxiv.org/abs/2604.01000v1) | [PDF](https://arxiv.org/pdf/2604.01000v1)
- **分类**: cs.LG, cs.DB, cs.DC
- **含金量**: 20/43 分

### 摘要

Graph Neural Networks (GNNs) are widely used for learning on graph-structured data, but scaling GNN training to massive graphs remains challenging.

To enable scalable distributed training, graphs are divided into smaller partitions that are distributed across multiple machines such that inter-machine communication is minimized and computational load is balanced.

In practice, existing partitioning approaches face a fundamental trade-off between partitioning overhead and partitioning quality.

We propose EmbedPart, an embedding-driven partitioning approach that achieves both speed and quality.

In

### AI 总结

总结生成失败

---

