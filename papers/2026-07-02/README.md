# 大数据+AI 领域论文日报

**日期**: 2026-07-02

**论文数量**: 8 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [CausalMix: Data Mixture as Causal I...](https://arxiv.org/abs/2607.01104v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Understanding Large Language Models](https://arxiv.org/abs/2607.01006v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [MultiSynt/MT: Trillion-Token Multi-...](https://arxiv.org/abs/2607.00890v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Rise From The Ashes: LLM-based Stat...](https://arxiv.org/abs/2607.00555v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Approximate Nearest Neighbor Search...](https://arxiv.org/abs/2607.00727v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [NoPA: Non-Parametric Online 3D Scen...](https://arxiv.org/abs/2607.00529v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [DriveVer: Lightweight Trajectory Ev...](https://arxiv.org/abs/2607.00399v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [When Classic Cache Policies Fail: L...](https://arxiv.org/abs/2607.00394v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. CausalMix: Data Mixture as Causal Inference for Language Model Training

- **作者**: Zinan Tang, Yukun Zhang, Shaomian Zheng, Zhuoshi Pan, Qizhi Pei
- **发布日期**: 2026-07-01
- **链接**: [arXiv:2607.01104v1](https://arxiv.org/abs/2607.01104v1) | [PDF](https://arxiv.org/pdf/2607.01104v1)
- **分类**: cs.LG, cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

In Large Language Model (LLM) training, data mixing plays a pivotal role in determining model performance.

Recent methods optimize mixture weights via proxy models, but they rely on the assumption of static data distributions.

As a result, when the underlying data pool shifts, these methods require costly retraining from scratch.

This limitation restricts their ability to scale seamlessly from small settings to larger data pools and model sizes.

In this paper, we propose CausalMix to address this limitation by casting data mixture optimization as a causal inference problem.

We formulate the st

### AI 总结

总结生成失败

---

## 2. Understanding Large Language Models

- **作者**: Yannik Keller, Thomas Eisenmann
- **发布日期**: 2026-07-01
- **链接**: [arXiv:2607.01006v1](https://arxiv.org/abs/2607.01006v1) | [PDF](https://arxiv.org/pdf/2607.01006v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

Large Language Models (LLMs) represent one of the most significant advances in AI and natural language processing in recent years.

Still, many pressing questions about their mechanisms, capabilities, and relationship to human cognition remain highly debated.

This chapter aims to outline our current understanding of LLMs by discussing recent evidence on emerging capabilities and their mechanistic implementation within processing layers.

We begin with a concise overview of the Transformer architecture, emphasizing how the attention mechanism enables training on massive datasets, allowing LLMs to

### AI 总结

总结生成失败

---

## 3. MultiSynt/MT: Trillion-Token Multi-Parallel Pre-Training Data Translated Across 36 Languages

- **作者**: Maximilian Idahl, Jörg Tiedemann, Sampo Pyysalo, David Salinas, Tomasz Galica
- **发布日期**: 2026-07-01
- **链接**: [arXiv:2607.00890v1](https://arxiv.org/abs/2607.00890v1) | [PDF](https://arxiv.org/pdf/2607.00890v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

Open web-scale pre-training corpora remain concentrated in English, limiting multilingual LLM development.

We introduce MultiSynt/MT, an open synthetic parallel corpus with approximately 4.8 trillion target-language tokens across 36 European languages, produced by translating 100 billion high-quality Nemotron-CC tokens with Tower+ and OPUS-MT/HPLT-MT systems.

For many medium- and lower-resource European languages, this is the largest openly available pre-training resource.

On a broad multilingual benchmark suite, reference LLMs trained on MultiSynt/MT reach the final score of HPLT 2.0, a nativ

### AI 总结

总结生成失败

---

## 4. Rise From The Ashes: LLM-based Static Analysis for Deep Learning Framework Bugs

- **作者**: Shaoyu Yang, Haifeng Lin, Chunrong Fang, Xiang Chen, Wei Cheng
- **发布日期**: 2026-07-01
- **链接**: [arXiv:2607.00555v1](https://arxiv.org/abs/2607.00555v1) | [PDF](https://arxiv.org/pdf/2607.00555v1)
- **分类**: cs.SE
- **含金量**: 20/43 分

### 摘要

Deep learning (DL) frameworks are critical AI infrastructures that often hide bugs with serious security implications.

While dynamic approaches such as fuzzing are effective in uncovering these bugs, they require real test execution and incur high computational costs.

Static analysis is a natural complement because it can detect bugs without runtime execution, offering fast and scalable testing.

Unfortunately, there is still limited work targeting static analysis for DL frameworks due to their multilingual architectures and tensor-related program state.

We present Phoenix, the first LLM-base

### AI 总结

总结生成失败

---

## 5. Approximate Nearest Neighbor Search with Graph Range Filters

- **作者**: Qian Tao, Yuntao Jiang, Yongxin Tong, Yu Sun
- **发布日期**: 2026-07-01
- **链接**: [arXiv:2607.00727v1](https://arxiv.org/abs/2607.00727v1) | [PDF](https://arxiv.org/pdf/2607.00727v1)
- **分类**: cs.DB
- **含金量**: 20/43 分

### 摘要

Vector databases have become a fundamental component for high-dimensional vector retrieval in artificial intelligence applications.

Recent research has focused on filtered approximate nearest neighbor search (filtered ANN), which involves retrieving the nearest vectors that satisfy a given attribute-based filter.

However, existing filters are generally limited to numerical range constraints or categorical existence checks, which restricts their applicability in more complex, real-world scenarios.

In this paper, we investigate filtered ANN using graph range filters, where the retrieved vectors 

### AI 总结

总结生成失败

---

## 6. NoPA: Non-Parametric Online 3D Scene Graph Generation

- **作者**: Qi Xun Yeo, Seungjun Lee, Yan Li, Gim Hee Lee
- **发布日期**: 2026-07-01
- **链接**: [arXiv:2607.00529v1](https://arxiv.org/abs/2607.00529v1) | [PDF](https://arxiv.org/pdf/2607.00529v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

Classic 3D scene graph generation approaches fail to work in real-time due to the heavy computational cost of environment mapping and the need to generate intermediate point-cloud representations.

To alleviate this issue, a recent work eschews point clouds in favor of a lightweight Gaussian distribution for each object.

This approximation drastically speeds up inference and enables real-time 3D scene graph generation.

However, the representation has two key weaknesses.

\textbf{1)} Each object is approximated by a single 3D Gaussian, which causes a severe loss of 3D geometric detail.

\textbf{2)

### AI 总结

总结生成失败

---

## 7. DriveVer: Lightweight Trajectory Evaluator as Test-Time Verifier for Autonomous Driving

- **作者**: Chong He, Yuechen Luo, Fang Li, Shaoqing Xu, Fuxi Wen
- **发布日期**: 2026-07-01
- **链接**: [arXiv:2607.00399v1](https://arxiv.org/abs/2607.00399v1) | [PDF](https://arxiv.org/pdf/2607.00399v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

End-to-end autonomous driving models often encounter performance bottlenecks, as training-time scaling leads to high computational costs and diminishing marginal returns.

Existing planners typically adopt a one-shot generation paradigm, lacking secondary validation and active correction mechanisms to detect and revise suboptimal or unsafe trajectories during inference.

To address this issue, we propose DriveVer, a lightweight, plug-and-play Test-Time Verifier that leverages the test-time scaling paradigm to enable autonomous driving systems to validate and refine trajectories without costly an

### AI 总结

总结生成失败

---

## 8. When Classic Cache Policies Fail: Learning-Augmented Replacement for Semantic Retrieval Buffers

- **作者**: Yushi Sun, Bowen Cao, Wai Lam
- **发布日期**: 2026-07-01
- **链接**: [arXiv:2607.00394v1](https://arxiv.org/abs/2607.00394v1) | [PDF](https://arxiv.org/pdf/2607.00394v1)
- **分类**: cs.DB, cs.CL
- **含金量**: 20/43 分

### 摘要

LLM agents increasingly rely on retrieval buffers to store and reuse past experience, yet the cache management policies governing these buffers remain largely ad-hoc.

We formalize this as an online semantic cache replacement problem with switching costs, where items are matched by embedding similarity and hit quality is continuous rather than binary.

Through experiments on two datasets from MemoryBench-Full (LoCoMo, DialSim) with 8 replacement policies, we reveal a surprising finding: classic heuristics (LRU, LFU) \emph{consistently underperform} the naive FIFO baseline on semantic workloads, 

### AI 总结

总结生成失败

---

