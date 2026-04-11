# 大数据+AI 领域论文日报

**日期**: 2026-04-11

**论文数量**: 8 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Rethinking Data Mixing from the Per...](https://arxiv.org/abs/2604.07963v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Rag Performance Prediction for Ques...](https://arxiv.org/abs/2604.07985v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [LPM 1.0: Video-based Character Perf...](https://arxiv.org/abs/2604.07823v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Adversarial Label Invariant Graph D...](https://arxiv.org/abs/2604.08404v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [STQuant: Spatio-Temporal Adaptive F...](https://arxiv.org/abs/2604.06836v2) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [LegoDiffusion: Micro-Serving Text-t...](https://arxiv.org/abs/2604.08123v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Learning is Forgetting: LLM Trainin...](https://arxiv.org/abs/2604.07569v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [A Bayesian Information-Theoretic Ap...](https://arxiv.org/abs/2604.03858v2) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Rethinking Data Mixing from the Perspective of Large Language Models

- **作者**: Yuanjian Xu, Tianze Sun, Changwei Xu, XinLong Zhao, Jianing Hao
- **发布日期**: 2026-04-09
- **链接**: [arXiv:2604.07963v1](https://arxiv.org/abs/2604.07963v1) | [PDF](https://arxiv.org/pdf/2604.07963v1)
- **分类**: cs.CL, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

Data mixing strategy is essential for large language model (LLM) training.

Empirical evidence shows that inappropriate strategies can significantly reduce generalization.

Although recent methods have improved empirical performance, several fundamental questions remain open: what constitutes a domain, whether human and model perceptions of domains are aligned, and how domain weighting influences generalization.

We address these questions by establishing formal connections between gradient dynamics and domain distributions, offering a theoretical framework that clarifies the role of domains in t

### AI 总结

总结生成失败

---

## 2. Rag Performance Prediction for Question Answering

- **作者**: Or Dado, David Carmel. Oren Kurland
- **发布日期**: 2026-04-09
- **链接**: [arXiv:2604.07985v1](https://arxiv.org/abs/2604.07985v1) | [PDF](https://arxiv.org/pdf/2604.07985v1)
- **分类**: cs.CL, cs.IR
- **含金量**: 20/43 分

### 摘要

We address the task of predicting the gain of using RAG (retrieval augmented generation) for question answering with respect to not using it.

We study the performance of a few pre-retrieval and post-retrieval predictors originally devised for ad hoc retrieval.

We also study a few post-generation predictors, one of which is novel to this study and posts the best prediction quality.

Our results show that the most effective prediction approach is a novel supervised predictor that explicitly models the semantic relationships among the question, retrieved passages, and the generated answer.

### AI 总结

总结生成失败

---

## 3. LPM 1.0: Video-based Character Performance Model

- **作者**: Ailing Zeng, Casper Yang, Chauncey Ge, Eddie Zhang, Garvey Xu
- **发布日期**: 2026-04-09
- **链接**: [arXiv:2604.07823v1](https://arxiv.org/abs/2604.07823v1) | [PDF](https://arxiv.org/pdf/2604.07823v1)
- **分类**: cs.CV, cs.AI, cs.MM
- **含金量**: 20/43 分

### 摘要

Performance, the externalization of intent, emotion, and personality through visual, vocal, and temporal behavior, is what makes a character alive.

Learning such performance from video is a promising alternative to traditional 3D pipelines.

However, existing video models struggle to jointly achieve high expressiveness, real-time inference, and long-horizon identity stability, a tension we call the performance trilemma.

Conversation is the most comprehensive performance scenario, as characters simultaneously speak, listen, react, and emote while maintaining identity over time.

To address this, 

### AI 总结

总结生成失败

---

## 4. Adversarial Label Invariant Graph Data Augmentations for Out-of-Distribution Generalization

- **作者**: Simon Zhang, Ryan P. DeMilt, Kun Jin, Cathy H. Xia
- **发布日期**: 2026-04-09
- **链接**: [arXiv:2604.08404v1](https://arxiv.org/abs/2604.08404v1) | [PDF](https://arxiv.org/pdf/2604.08404v1)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

Out-of-distribution (OoD) generalization occurs when representation learning encounters a distribution shift.

This occurs frequently in practice when training and testing data come from different environments.

Covariate shift is a type of distribution shift that occurs only in the input data, while the concept distribution stays invariant.

We propose RIA - Regularization for Invariance with Adversarial training, a new method for OoD generalization under convariate shift.

Motivated by an analogy to $Q$-learning, it performs an adversarial exploration for training data environments.

These new en

### AI 总结

总结生成失败

---

## 5. STQuant: Spatio-Temporal Adaptive Framework for Optimizer Quantization in Large Multimodal Model Training

- **作者**: Minglu Liu, Cunchen Hu, Liangliang Xu, Fengming Tang, Ruijia Wang
- **发布日期**: 2026-04-08
- **链接**: [arXiv:2604.06836v2](https://arxiv.org/abs/2604.06836v2) | [PDF](https://arxiv.org/pdf/2604.06836v2)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Quantization is an effective way to reduce the memory cost of large-scale model training.

However, most existing methods adopt fixed-precision policies, which ignore the fact that optimizer-state distributions vary significantly across layers and training steps.

Such uniform designs often introduce noticeable accuracy degradation.

To move beyond fixed quantization, we propose STQuant, a distributed training framework that reduces the memory footprint of optimizer states via dynamic precision allocation across layers, state variables, and training steps, while maintaining model quality.

Naively

### AI 总结

总结生成失败

---

## 6. LegoDiffusion: Micro-Serving Text-to-Image Diffusion Workflows

- **作者**: Lingyun Yang, Suyi Li, Tianyu Feng, Xiaoxiao Jiang, Zhipeng Di
- **发布日期**: 2026-04-09
- **链接**: [arXiv:2604.08123v1](https://arxiv.org/abs/2604.08123v1) | [PDF](https://arxiv.org/pdf/2604.08123v1)
- **分类**: cs.DC, cs.AI
- **含金量**: 20/43 分

### 摘要

Text-to-image generation executes a diffusion workflow comprising multiple models centered on a base diffusion model.

Existing serving systems treat each workflow as an opaque monolith, provisioning, placing, and scaling all constituent models together, which obscures internal dataflow, prevents model sharing, and enforces coarse-grained resource management.

In this paper, we make a case for micro-serving diffusion workflows with LegoDiffusion, a system that decomposes a workflow into loosely coupled model-execution nodes that can be independently managed and scheduled.

By explicitly managing 

### AI 总结

总结生成失败

---

## 7. Learning is Forgetting: LLM Training As Lossy Compression

- **作者**: Henry C. Conklin, Tom Hosking, Tan Yi-Chern, Julian Gold, Jonathan D. Cohen
- **发布日期**: 2026-04-08
- **链接**: [arXiv:2604.07569v1](https://arxiv.org/abs/2604.07569v1) | [PDF](https://arxiv.org/pdf/2604.07569v1)
- **分类**: cs.LG, cs.AI, cs.CL, cs.IT
- **含金量**: 20/43 分

### 摘要

Despite the increasing prevalence of large language models (LLMs), we still have a limited understanding of how their representational spaces are structured.

This limits our ability to interpret how and what they learn or relate them to learning in humans.

We argue LLMs are best seen as an instance of lossy compression, where over training they learn by retaining only information in their training data relevant to their objective(s).

We show pre-training results in models that are optimally compressed for next-sequence prediction, approaching the Information Bottleneck bound on compression.

Ac

### AI 总结

总结生成失败

---

## 8. A Bayesian Information-Theoretic Approach to Data Attribution

- **作者**: Dharmesh Tailor, Nicolò Felicioni, Kamil Ciosek
- **发布日期**: 2026-04-04
- **链接**: [arXiv:2604.03858v2](https://arxiv.org/abs/2604.03858v2) | [PDF](https://arxiv.org/pdf/2604.03858v2)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

Training Data Attribution (TDA) seeks to trace model predictions back to influential training examples, enhancing interpretability and safety.

We formulate TDA as a Bayesian information-theoretic problem: subsets are scored by the information loss they induce - the entropy increase at a query when removed.

This criterion credits examples for resolving predictive uncertainty rather than label noise.

To scale to modern networks, we approximate information loss using a Gaussian Process surrogate built from tangent features.

We show this aligns with classical influence scores for single-example at

### AI 总结

总结生成失败

---

