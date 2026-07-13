# 大数据+AI 领域论文日报

**日期**: 2026-07-13

**论文数量**: 3 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [A Sovereign, Open-Source Foundation...](https://arxiv.org/abs/2607.09424v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Graph Neural Networks for Scalable ...](https://arxiv.org/abs/2607.09372v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [SCOReD: Student-Aware CoT Optimizat...](https://arxiv.org/abs/2607.05734v2) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. A Sovereign, Open-Source Foundation Model for German and English

- **作者**: The Soofi-Team,  :, Benedikt Droste, David Fitzek, Ruben Härle
- **发布日期**: 2026-07-10
- **链接**: [arXiv:2607.09424v1](https://arxiv.org/abs/2607.09424v1) | [PDF](https://arxiv.org/pdf/2607.09424v1)
- **分类**: cs.CL, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

We present Soofi S 30B-A3B, a sovereign, open-source Mixture-of-Experts (MoE) hybrid Mamba Transformer foundation model for German and English.

Its hybrid design activates only 3B of 30B parameters per token and keeps the inference cache near-constant as context grows, giving it a decisive throughput advantage over dense models for long-context, high-concurrency deployment.

Pretrained on roughly 27 trillion tokens with deliberately up-weighted German, Soofi S matches dense 14 to 27B models on aggregate English and German benchmarks while achieving the best code aggregates in both languages amo

### AI 总结

总结生成失败

---

## 2. Graph Neural Networks for Scalable and Transferable Node Centrality Approximation

- **作者**: Samra Sana, Giorgio Mantica, Saul Imbrici
- **发布日期**: 2026-07-10
- **链接**: [arXiv:2607.09372v1](https://arxiv.org/abs/2607.09372v1) | [PDF](https://arxiv.org/pdf/2607.09372v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Graph Neural Networks (GNNs) provide a learning-based framework for approximating graph quantities that are expensive to compute exactly.

This paper investigates GNNs for scalable approximation of betweenness and closeness centrality, formulated as a node-ranking problem.

Exact centrality values are used as supervision, and ranking quality is evaluated using Kendall's tau rank correlation.

We study whether message-passing GNNs can learn transferable structural representations across different graph topologies rather than only fitting the distribution used during training.

On unseen Erdos renyi

### AI 总结

总结生成失败

---

## 3. SCOReD: Student-Aware CoT Optimization for Recommendation Distillation

- **作者**: Haz Sameen Shahgir, Yufei Li, Xiaohan Wei, Yunchen Pu, Fei Tian
- **发布日期**: 2026-07-07
- **链接**: [arXiv:2607.05734v2](https://arxiv.org/abs/2607.05734v2) | [PDF](https://arxiv.org/pdf/2607.05734v2)
- **分类**: cs.IR, cs.AI
- **含金量**: 20/43 分

### 摘要

Chain-of-thought (CoT) distillation in the recommendation domain is a necessary precursor to RL training, but raw teacher traces are ill-suited to this task.

Large teachers approach the recommendation task with unusually high reasoning uncertainty, repeatedly rechecking their answers without revising them; supervised fine-tuning on such traces produces verbose students that never revise their initial guess.

Furthermore, due to the novelty of the recommendation domain, the teacher's reasoning traces are highly out-of-distribution for the small student LLM.

We propose Student-Aware CoT Optimiz

### AI 总结

总结生成失败

---

