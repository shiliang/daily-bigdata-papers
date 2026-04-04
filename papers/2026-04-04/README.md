# 大数据+AI 领域论文日报

**日期**: 2026-04-04

**论文数量**: 3 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Combating Data Laundering in LLM Tr...](https://arxiv.org/abs/2604.01904v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Does Your Optimizer Care How You No...](https://arxiv.org/abs/2604.01563v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [ByteRover: Agent-Native Memory Thro...](https://arxiv.org/abs/2604.01599v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Combating Data Laundering in LLM Training

- **作者**: Muxing Li, Zesheng Ye, Sharon Li, Feng Liu
- **发布日期**: 2026-04-02
- **链接**: [arXiv:2604.01904v1](https://arxiv.org/abs/2604.01904v1) | [PDF](https://arxiv.org/pdf/2604.01904v1)
- **分类**: cs.CR, cs.AI
- **含金量**: 20/43 分

### 摘要

Data rights owners can detect unauthorized data use in large language model (LLM) training by querying with proprietary samples.

Often, superior performance (e.g., higher confidence or lower loss) on a sample relative to the untrained data implies it was part of the training corpus, as LLMs tend to perform better on data they have seen during training.

However, this detection becomes fragile under data laundering, a practice of transforming the stylistic form of proprietary data, while preserving critical information to obfuscate data provenance.

When an LLM is trained exclusively on such laun

### AI 总结

总结生成失败

---

## 2. Does Your Optimizer Care How You Normalize? Normalization-Optimizer Coupling in LLM Training

- **作者**: Abdelrahman Abouzeid
- **发布日期**: 2026-04-02
- **链接**: [arXiv:2604.01563v1](https://arxiv.org/abs/2604.01563v1) | [PDF](https://arxiv.org/pdf/2604.01563v1)
- **分类**: cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

In LLM training, normalization layers and optimizers are typically treated as independent design choices.

In a 3x2 factorial at 1B parameters and 1000 training steps, we show this assumption can fail: Dynamic Erf (Derf; Chen & Liu, 2025) suffers a large negative interaction with Muon (Jordan, 2024), with its gap to RMSNorm growing from +0.31 nats under AdamW to +0.97 under Muon, approximately three times larger.

Dynamic Tanh (DyT; Zhu et al., 2025), included as a bounded-normalizer control, shows no such penalty.

Our evidence points to two failure modes of erf under Muon's faster spectral-norm

### AI 总结

总结生成失败

---

## 3. ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context

- **作者**: Andy Nguyen, Danh Doan, Hoang Pham, Bao Ha, Dat Pham
- **发布日期**: 2026-04-02
- **链接**: [arXiv:2604.01599v1](https://arxiv.org/abs/2604.01599v1) | [PDF](https://arxiv.org/pdf/2604.01599v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

Memory-Augmented Generation (MAG) extends large language models with external memory to support long-context reasoning, but existing approaches universally treat memory as an external service that agents call into, delegating storage to separate pipelines of chunking, embedding, and graph extraction.

This architectural separation means the system that stores knowledge does not understand it, leading to semantic drift between what the agent intended to remember and what the pipeline actually captured, loss of coordination context across agents, and fragile recovery after failures.

In this paper

### AI 总结

总结生成失败

---

