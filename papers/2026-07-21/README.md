# 大数据+AI 领域论文日报

**日期**: 2026-07-21

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [A domain decomposition online-learn...](https://arxiv.org/abs/2607.17723v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Online learning of neural state-spa...](https://arxiv.org/abs/2607.17614v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Mobius Learning: Cyclic Depth Foldi...](https://arxiv.org/abs/2607.17843v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [FlashRT: Agent Harness for Guiding ...](https://arxiv.org/abs/2607.18171v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Adaptive Incident Prioritization fo...](https://arxiv.org/abs/2607.16963v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Learning to Fold: prizewinning solu...](https://arxiv.org/abs/2606.27163v2) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [AoA: Theorem Proving Agent over Abs...](https://arxiv.org/abs/2607.16372v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Retrieval is Enough: Training-Free ...](https://arxiv.org/abs/2607.16448v1) | 待分析 | 评估失败 | [Code](https://github.com/SriramB-98/HARP) | 20/43 |
| 9 | [Compositional Diffusion with Guided...](https://arxiv.org/abs/2601.00126v3) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Deep Learning-based Filtering for V...](https://arxiv.org/abs/2607.16319v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. A domain decomposition online-learning-enhanced nonlinear elimination preconditioner

- **作者**: Pai Zhang, Linyan Gu, Li Luo
- **发布日期**: 2026-07-20
- **链接**: [arXiv:2607.17723v1](https://arxiv.org/abs/2607.17723v1) | [PDF](https://arxiv.org/pdf/2607.17723v1)
- **分类**: math.NA
- **含金量**: 20/43 分

### 摘要

Nonlinearly preconditioned inexact Newton methods form an effective class of solvers for large-scale nonlinear algebraic systems arising from the discretization of partial differential equations.

A central challenge in nonlinear elimination (NE) preconditioning is the reliable identification of the slowly converging components to be eliminated.

Existing selection strategies often rely on problem-specific physical information or user-tuned thresholds applied directly to the raw nonlinear residual, which may contain irregular oscillatory structures near stagnation regions, making the selected ba

### AI 总结

总结生成失败

---

## 2. Online learning of neural state-space models

- **作者**: Bendegúz Györök, Tamás Péni, Maarten Schoukens, Roland Tóth
- **发布日期**: 2026-07-20
- **链接**: [arXiv:2607.17614v1](https://arxiv.org/abs/2607.17614v1) | [PDF](https://arxiv.org/pdf/2607.17614v1)
- **分类**: eess.SY, cs.LG
- **含金量**: 20/43 分

### 摘要

Recent advances in deep-learning-based nonlinear system identification have led to encoder-based estimation of neural state-space (ANN-SS) models that achieve state-of-the-art performance in offline settings by estimating initial model states from past input-output data.

These methods are typically used in multiple-shooting-based offline identification, and online learning of these models remains largely unexplored.

This paper presents a batch-wise learning pipeline and a direct recursive identification algorithm for subspace encoder-based ANN-SS models.

We provide convergence analysis of the 

### AI 总结

总结生成失败

---

## 3. Mobius Learning: Cyclic Depth Folding in Transformers

- **作者**: Tongtian Zhu
- **发布日期**: 2026-07-20
- **链接**: [arXiv:2607.17843v1](https://arxiv.org/abs/2607.17843v1) | [PDF](https://arxiv.org/pdf/2607.17843v1)
- **分类**: cs.LG, cs.CL, cs.DC
- **含金量**: 20/43 分

### 摘要

Transformer-based language models organize computation along an ordered depth axis, where shallow and deep blocks often develop distinct representational roles.

We challenge the conventional view that these roles must remain tied to a block's position in the ordered sequence.

We introduce Mobius Learning, a training architecture based on cyclic depth folding, in which different data streams follow cyclically shifted block orders.

The same block group is therefore applied early in the block sequence for some data streams and late for others, so it is optimized in both shallow and deep roles, a 

### AI 总结

总结生成失败

---

## 4. FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications

- **作者**: Krish Agarwal, Zhuoming Chen, Yanyuan Qin, Zhenyu Gu, Atri Rudra
- **发布日期**: 2026-07-20
- **链接**: [arXiv:2607.18171v1](https://arxiv.org/abs/2607.18171v1) | [PDF](https://arxiv.org/pdf/2607.18171v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Real-time multimodal applications, including voice agents and interactive video generation, compose heterogeneous models into pipelines whose efficient deployment requires application-specific decisions about placement, streaming, and intra-model parallelism.

Existing serving systems and auto-parallelism compilers commit to limited transformations and fixed workload assumptions, so achieving high performance on a new application requires hand-crafting an efficient implementation.

We present FlashRT, an agent harness that guides coding agents to lift simple developer-written reference implement

### AI 总结

总结生成失败

---

## 5. Adaptive Incident Prioritization for Security Operations at Scale

- **作者**: Scott Freitas, Amir Gharib, Maayan Magenheim
- **发布日期**: 2026-07-18
- **链接**: [arXiv:2607.16963v1](https://arxiv.org/abs/2607.16963v1) | [PDF](https://arxiv.org/pdf/2607.16963v1)
- **分类**: cs.CR, cs.IR
- **含金量**: 20/43 分

### 摘要

Large security operations centers (SOCs) often face hundreds of active incidents per day, creating substantial cognitive and operational demands for analysts.

Analysts must quickly decide which incidents deserve attention within long, constantly changing queues, yet incidents are commonly ordered by arrival time, coarse severity, or product-specific heuristics that leave their relative priority unclear.

We introduce Adaptive Incident Prioritization (AIP), the ranking algorithm behind Microsoft Defender Queue Assistant, which continuously prioritizes security incidents for analyst investigation

### AI 总结

总结生成失败

---

## 6. Learning to Fold: prizewinning solution at LeHome Challenge 2026 (1st place online, 2nd offline)

- **作者**: Ilia Larchenko
- **发布日期**: 2026-06-25
- **链接**: [arXiv:2606.27163v2](https://arxiv.org/abs/2606.27163v2) | [PDF](https://arxiv.org/pdf/2606.27163v2)
- **分类**: cs.RO, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

I describe my solution to the LeHome Challenge 2026, an ICRA 2026 competition on bimanual garment folding.

The system placed 1st of 62 teams in the online (simulation) round and 2nd in the real-world final.

It improves a vision-language-action (VLA) policy with a reinforcement-learning loop.

The policy is its own value function: the same network that predicts actions also predicts success, progress, and a few task-relevant future quantities, and those predictions drive advantage estimation, live failure detection, and candidate selection.

The work mostly recombines existing RL ideas with engin

### AI 总结

总结生成失败

---

## 7. AoA: Theorem Proving Agent over Abstract Syntax Tree of Redesigned Language

- **作者**: Qiyuan Xu, Joshua Ong Jun Leang, Renxi Wang, Wenda Li, Haonan Li
- **发布日期**: 2026-07-17
- **链接**: [arXiv:2607.16372v1](https://arxiv.org/abs/2607.16372v1) | [PDF](https://arxiv.org/pdf/2607.16372v1)
- **分类**: cs.SE, cs.AI, cs.LG, cs.PL
- **含金量**: 20/43 分

### 摘要

Interactive theorem proving (ITP) underpins program verification and formalized mathematics, but its manual effort limits scalability.

LLM-based proof agents promise to ease this effort, but their heavy token consumption and API cost remain a major obstacle.

We trace this cost to a shared root: current agents operate on serialized concrete syntax, emitting proofs as source text and recovering proof states through separate, line-number-based queries, so every edit shifts later lines and forces repeated relocation of errors and states.

This same dependence on concrete syntax also blocks adoption

### AI 总结

总结生成失败

---

## 8. Retrieval is Enough: Training-Free Interpretability with a Tool-Using Agent

- **作者**: Sriram Balasubramanian, Soheil Feizi
- **发布日期**: 2026-07-17
- **链接**: [arXiv:2607.16448v1](https://arxiv.org/abs/2607.16448v1) | [PDF](https://arxiv.org/pdf/2607.16448v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/SriramB-98/HARP) ⭐ 0 (Python)

### 摘要

Interpretability methods for neural network activations span a wide cost spectrum, from cheap, training-free techniques (such as linear probes, PCA, SVD) to more expensive training-based ones (such as SAEs and activation oracles).

Training-based methods are typically more powerful, in part because they leverage large activation datasets during training.

This raises a natural question - do they actually surface insights that go beyond what is recoverable from the training dataset itself? To address this, we equip an LLM agent with a vector database of activations paired with their textual conte

### AI 总结

总结生成失败

---

## 9. Compositional Diffusion with Guided Search for Long-Horizon Planning

- **作者**: Utkarsh A Mishra, David He, Yongxin Chen, Danfei Xu
- **发布日期**: 2025-12-31
- **链接**: [arXiv:2601.00126v3](https://arxiv.org/abs/2601.00126v3) | [PDF](https://arxiv.org/pdf/2601.00126v3)
- **分类**: cs.RO
- **含金量**: 20/43 分

### 摘要

Generative models have emerged as powerful tools for planning, with compositional approaches offering particular promise for modeling long-horizon task distributions by composing together local, modular generative models.

This compositional paradigm spans diverse domains, from multi-step manipulation planning to panoramic image synthesis to long video generation.

However, compositional generative models face a critical challenge: when local distributions are multimodal, existing composition methods average incompatible modes, producing plans that are neither locally feasible nor globally coher

### AI 总结

总结生成失败

---

## 10. Deep Learning-based Filtering for Video Coding: A Survey on Architectures, Algorithms, and Complexity Analysis

- **作者**: Young-Woon Lee, Byung-Gyu Kim
- **发布日期**: 2026-07-15
- **链接**: [arXiv:2607.16319v1](https://arxiv.org/abs/2607.16319v1) | [PDF](https://arxiv.org/pdf/2607.16319v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

As Ultra-High-Definition (UHD) displays and immersive media services become ubiquitous in the Internet of Things (IoT) and Consumer Electronics (CE) sectors, including 8K display and mobile devices, the demand for high-efficiency video coding is unprecedented.

While Deep Learning-based Filtering (DLF) has emerged as a promising solution to mitigate compression artifacts inherent in standards like High Efficiency Video Coding (HEVC/H.265) and Versatile Video Coding (VVC/H.266), its deployment in CE devices is severely constrained by computational complexity, memory bandwidth, and power consumpt

### AI 总结

总结生成失败

---

