# 大数据+AI 领域论文日报

**日期**: 2026-03-28

**论文数量**: 3 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [DFLOP: A Data-driven Framework for ...](https://arxiv.org/abs/2603.25120v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [PRISM: Dynamic Primitive-Based Fore...](https://arxiv.org/abs/2603.25378v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [TAMI-MPC:Trusted Acceleration of Mi...](https://arxiv.org/abs/2603.24861v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. DFLOP: A Data-driven Framework for Multimodal LLM Training Pipeline Optimization

- **作者**: Hyeonjun An, Sihyun Kim, Chaerim Lim, Hyunjoon Kim, Rathijit Sen
- **发布日期**: 2026-03-26
- **链接**: [arXiv:2603.25120v1](https://arxiv.org/abs/2603.25120v1) | [PDF](https://arxiv.org/pdf/2603.25120v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Multimodal Large Language Models (MLLMs) have achieved remarkable advances by integrating text, image, and audio understanding within a unified architecture.

However, existing distributed training frameworks remain fundamentally data-blind: they parallelize computation without accounting for variations in input data characteristics.

This data unawareness leads to severe computation skew across stages and microbatches, where heterogeneous multimodal inputs incur different processing costs.

Consequently, GPU resources are unevenly utilized, synchronization delays accumulate, and overall training

### AI 总结

总结生成失败

---

## 2. PRISM: Dynamic Primitive-Based Forecasting for Large-Scale GPU Cluster Workloads

- **作者**: Xin Wu, Fei Teng, Xingwang Li, Bin Zheng, Qiang Duan
- **发布日期**: 2026-03-26
- **链接**: [arXiv:2603.25378v1](https://arxiv.org/abs/2603.25378v1) | [PDF](https://arxiv.org/pdf/2603.25378v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Accurately forecasting GPU workloads is essential for AI infrastructure, enabling efficient scheduling, resource allocation, and power management.

Modern workloads are highly volatile, multiple periodicity, and heterogeneous, making them challenging for traditional predictors.

We propose PRISM, a primitive-based compositional forecasting framework combining dictionary-driven temporal decomposition with adaptive spectral refinement.

This dual representation extracts stable, interpretable workload signatures across diverse GPU jobs.

Evaluated on large-scale production traces, PRISM achieves stat

### AI 总结

总结生成失败

---

## 3. TAMI-MPC:Trusted Acceleration of Minimal-Interaction MPC for Efficient Nonlinear Inference

- **作者**: Zhuoran Li, Hanieh Totonchi Asl, Yifei Cai, Ebrahim Nouri, Danella Zhao
- **发布日期**: 2026-03-25
- **链接**: [arXiv:2603.24861v1](https://arxiv.org/abs/2603.24861v1) | [PDF](https://arxiv.org/pdf/2603.24861v1)
- **分类**: cs.AR
- **含金量**: 20/43 分

### 摘要

Secure multi-party computation (MPC) offers a practical foundation for privacy-preserving machine learning at the edge.

However, current MPC systems rely heavily on communication and computation-intensive primitives-such as secure comparison for nonlinear inference, which are often impractical on resource-constrained platforms.

To enable real-time inference under a resource-constrained platform, we introduce a Trusted Acceleration of Minimal-Interaction MPC framework, TAMI-MPC, for nonlinear evaluation.

Specifically, we reduce communication cost by redesigning the core primitives, leaf compari

### AI 总结

总结生成失败

---

