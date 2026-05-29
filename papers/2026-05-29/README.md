# 大数据+AI 领域论文日报

**日期**: 2026-05-29

**论文数量**: 6 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Demystifying Data Organization for ...](https://arxiv.org/abs/2605.30334v1) | 待分析 | 评估失败 | [*46](https://github.com/microsoft/data-efficacy) | 20/43 |
| 2 | [On the Optimizer Dependence of Neur...](https://arxiv.org/abs/2605.29387v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [minWM: A Full-Stack Open-Source Fra...](https://arxiv.org/abs/2605.30263v1) | 待分析 | 评估失败 | [*192](https://github.com/shengshu-ai/minWM) | 20/43 |
| 4 | [FPLIER: Federated Pathway-Level Inf...](https://arxiv.org/abs/2605.29587v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Protecting On-Device AI Inference: ...](https://arxiv.org/abs/2605.29450v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Does Distributed Training Undermine...](https://arxiv.org/abs/2605.29359v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Demystifying Data Organization for Enhanced LLM Training

- **作者**: Yalun Dai, Yangyu Huang, Tongshen Yang, Yonghan Wang, Xin Zhang
- **发布日期**: 2026-05-28
- **链接**: [arXiv:2605.30334v1](https://arxiv.org/abs/2605.30334v1) | [PDF](https://arxiv.org/pdf/2605.30334v1)
- **分类**: cs.AI, cs.CL
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/microsoft/data-efficacy) ⭐ 46 (Python)

### 摘要

Large Language Models (LLMs) have revolutionized various fields, yet their training efficiency is heavily reliant on effective data curation.

While data selection has been widely studied, the strategic data organization for enhanced training remains an underexplored area, particularly since current LLMs are often trained for only one or a few epochs.

This paper systematically explores the influence of data organization on LLM training by reusing pre-computed sample-level scores originally generated for data efficiency, thereby incurring minimal additional computational overhead.

We identify an

### AI 总结

总结生成失败

---

## 2. On the Optimizer Dependence of Neural Scaling Laws

- **作者**: Vansh Ramani, Shourya Vir Jain
- **发布日期**: 2026-05-28
- **链接**: [arXiv:2605.29387v1](https://arxiv.org/abs/2605.29387v1) | [PDF](https://arxiv.org/pdf/2605.29387v1)
- **分类**: cs.LG, cs.AI, stat.ML
- **含金量**: 20/43 分

### 摘要

The scaling exponent $α$ in neural scaling laws $L(N) \propto N^{-α}$ is commonly treated as a fixed constant set by architecture and data.

We present evidence that $α$ depends systematically on the optimizer.

In controlled random-feature regression experiments -- the canonical theoretical framework for neural scaling -- we measure $α$ across five optimizer variants and six spectral conditions.

Preconditioned optimizers consistently yield steeper scaling (larger $α$), with the $α$-shift increasing across most of the tested spectral range, peaking near $s = 1.5$, and remaining large at $s = 2.0

### AI 总结

总结生成失败

---

## 3. minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models

- **作者**: Min Zhao, Hongzhou Zhu, Bokai Yan, Zihan Zhou, Yimin Chen
- **发布日期**: 2026-05-28
- **链接**: [arXiv:2605.30263v1](https://arxiv.org/abs/2605.30263v1) | [PDF](https://arxiv.org/pdf/2605.30263v1)
- **分类**: cs.CV
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/shengshu-ai/minWM) ⭐ 192 (Python)

### 摘要

Recent video diffusion foundation models have achieved remarkable progress in high-quality video generation, yet turning them into real-time interactive video world models remains challenging.

Interactive world models require controllable, causal, and low-latency rollout, which in practice demands a full pipeline spanning data construction, controllable fine-tuning, autoregressive training, few-step distillation, and streaming inference.

In this work, we present minWM, a full-stack open-source framework for building real-time interactive video world models.

minWM provides an end-to-end pipelin

### AI 总结

总结生成失败

---

## 4. FPLIER: Federated Pathway-Level Information Extractor

- **作者**: Daniele Malpetti, Christian Berchtold, Francesco Gualdi, Marco Scutari, Laura Azzimonti
- **发布日期**: 2026-05-28
- **链接**: [arXiv:2605.29587v1](https://arxiv.org/abs/2605.29587v1) | [PDF](https://arxiv.org/pdf/2605.29587v1)
- **分类**: q-bio.QM, cs.LG
- **含金量**: 20/43 分

### 摘要

In transcriptomics, gene-set-aware factorization methods such as the Pathway Level Information Extractor (PLIER) are most effective when trained on large, heterogeneous expression compendia.

Yet, many clinically relevant cohorts cannot be pooled into a single dataset due to privacy and governance constraints.

We present FPLIER, a federated extension of PLIER that enables distributed training across multiple data holders while incorporating publicly available datasets.

Through secure aggregation, FPLIER produces training updates algebraically equivalent to those of a centralized pooled-data app

### AI 总结

总结生成失败

---

## 5. Protecting On-Device AI Inference: A Systematic Review of Attacks and Defence Mechanisms

- **作者**: Zisis Tsiatsikas, Alexandros Fakis, Georgios Karopoulos, Vasileios Kouliaridis, Marios Anagnostopoulos
- **发布日期**: 2026-05-28
- **链接**: [arXiv:2605.29450v1](https://arxiv.org/abs/2605.29450v1) | [PDF](https://arxiv.org/pdf/2605.29450v1)
- **分类**: cs.CR
- **含金量**: 20/43 分

### 摘要

The need for secure and private Artificial Intelligence (AI) and Machine Learning (ML) on edge and mobile devices has increased the necessity of protecting the architecture of these systems from threats to both security and privacy.

With an ever-increasing number of pre-trained AI models being used on mobile platforms for client-side inference, there are rising concerns about the risks associated with the theft/extraction of AI models, adversarial attacks on AI models, and data breaches.

As a result of this trend, a variety of defence mechanisms have been proposed to protect against these thre

### AI 总结

总结生成失败

---

## 6. Does Distributed Training Undermine Compute Governance?

- **作者**: Robi Rahman
- **发布日期**: 2026-05-28
- **链接**: [arXiv:2605.29359v1](https://arxiv.org/abs/2605.29359v1) | [PDF](https://arxiv.org/pdf/2605.29359v1)
- **分类**: cs.CY, cs.AI
- **含金量**: 20/43 分

### 摘要

Compute governance proposals often rely on the assumption that frontier AI training requires large, detectable computing clusters.

However, recent advances in distributed training algorithms could allow developers to conduct frontier-scale training on distributed agglomerations of hardware, rather than needing large datacenter facilities.

Developers who prefer not to be constrained by regulations may structure their hardware in a manner that evades the registration and monitoring requirements associated with compute governance.

Therefore, regulations must be designed to detect and prevent illi

### AI 总结

总结生成失败

---

