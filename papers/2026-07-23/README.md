# 大数据+AI 领域论文日报

**日期**: 2026-07-23

**论文数量**: 5 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [SLAI T-Rex: Full-Parameter Post-tra...](https://arxiv.org/abs/2607.20145v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [GaussianSeed: Hierarchical Gaussian...](https://arxiv.org/abs/2607.20071v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Adaptive Bayesian Online Learning v...](https://arxiv.org/abs/2607.20239v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Odin: Primitive-Level Synchronizati...](https://arxiv.org/abs/2607.19893v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Learning to Transmit: Volatility-Aw...](https://arxiv.org/abs/2607.19590v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. SLAI T-Rex: Full-Parameter Post-training of the DeepSeek-V4 Family on Ascend SuperPOD

- **作者**: Dongfang Li, Xiaodong Luo, Ruoyu Sun, Xuhui Chen, Linyuan Qiu
- **发布日期**: 2026-07-22
- **链接**: [arXiv:2607.20145v1](https://arxiv.org/abs/2607.20145v1) | [PDF](https://arxiv.org/pdf/2607.20145v1)
- **分类**: cs.CL, cs.AI
- **含金量**: 20/43 分

### 摘要

Full-parameter post-training of trillion-parameter-scale MoE models introduces substantial system-level challenges for large-scale distributed training, including severe memory pressure, non-overlapped communication overhead, and inefficient kernel execution.

While most large-scale LLM training systems are built around GPU-based clusters, this report presents an end-to-end optimization practice on the Ascend NPU SuperPOD.

Using the DeepSeek-V4 model family as the target workload, we develop a hierarchical optimization framework spanning model-level parallelism, computation-communication orches

### AI 总结

总结生成失败

---

## 2. GaussianSeed: Hierarchical Gaussian Seeding for High-Resolution 3D Occupancy Prediction

- **作者**: Xinzhuo Li, Xianghui Pan, Jiayuan Du, Wei Wei, Liuyi Wang
- **发布日期**: 2026-07-22
- **链接**: [arXiv:2607.20071v1](https://arxiv.org/abs/2607.20071v1) | [PDF](https://arxiv.org/pdf/2607.20071v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

Vision-centric 3D occupancy prediction provides dense scene representations essential for autonomous driving and robotic navigation, yet existing methods struggle to scale to high voxel resolutions due to prohibitive computational costs.

To address this, we introduce GaussianSeed, a progressive multi-scale Gaussian occupancy prediction framework that organizes primitives into a coarse-to-fine hierarchy.

Benefiting from this hierarchical design, GaussianSeed effectively circumvents the memory bottlenecks inherent in dense representations, successfully scaling to a $0.1\text{m}$ spatial resoluti

### AI 总结

总结生成失败

---

## 3. Adaptive Bayesian Online Learning via Expert Aggregation

- **作者**: Jungbin Jun, Ilsang Ohn
- **发布日期**: 2026-07-22
- **链接**: [arXiv:2607.20239v1](https://arxiv.org/abs/2607.20239v1) | [PDF](https://arxiv.org/pdf/2607.20239v1)
- **分类**: stat.ML, cs.LG
- **含金量**: 20/43 分

### 摘要

Bayesian online learning promises uncertainty-aware prediction on data streams, but its performance hinges on inferential choices, including learning rates, prior distributions and variational families, which are usually fixed before seeing the stream.

We address this by treating Bayesian update rules as experts and aggregating the Bayesian experts according to sequential predictive losses.

We prove that the resulting aggregate competes with the best expert in hindsight at an aggregation cost determined by how each expert's per-round performance is evaluated.

We instantiate the framework in on

### AI 总结

总结生成失败

---

## 4. Odin: Primitive-Level Synchronization for Distributed Point-Based Neural Rendering

- **作者**: Zhenxiang Ma, Zeyu He, Yuanzhen Zhou, Zhenyu Yang, Yuchang Zhang
- **发布日期**: 2026-07-22
- **链接**: [arXiv:2607.19893v1](https://arxiv.org/abs/2607.19893v1) | [PDF](https://arxiv.org/pdf/2607.19893v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Point-based neural rendering (PBNR) represents 3D scenes as explicit, trainable primitives and underpins high-quality reconstruction and emerging embodied AI and world-model pipelines.

Unlike layer-structured neural networks, PBNR has primitive-indexed dependencies: each view reads and updates only a sparse, view-dependent subset of mutable scene state.

As large scenes require distributed training and optimized renderers reduce per-view computation, global task- or iteration-level barriers increasingly place synchronization, rather than rendering, on the critical path.

We present Odin, a distr

### AI 总结

总结生成失败

---

## 5. Learning to Transmit: Volatility-Aware Predictive Communication for Energy-Efficient IoT Networks

- **作者**: John Kangethe, Ifrat Ikhtear Uddin, Longwei Wang
- **发布日期**: 2026-07-21
- **链接**: [arXiv:2607.19590v1](https://arxiv.org/abs/2607.19590v1) | [PDF](https://arxiv.org/pdf/2607.19590v1)
- **分类**: cs.IT
- **含金量**: 20/43 分

### 摘要

Communication is the dominant source of energy consumption in Internet-of-Things (IoT) networks, yet many sensed measurements exhibit strong temporal correlations and provide little new information to the receiver.

This paper introduces \textsc{ADAPTIVEML}, a volatility-aware predictive communication framework that enables IoT devices to intelligently decide when communication is necessary.

Each sensor maintains a lightweight machine learning predictor and transmits only when the prediction residual exceeds an adaptive threshold proportional to the local signal volatility.

By normalizing predi

### AI 总结

总结生成失败

---

