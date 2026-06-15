# 大数据+AI 领域论文日报

**日期**: 2026-06-15

**论文数量**: 6 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Be My Tutor: On-Policy Co-Distillat...](https://arxiv.org/abs/2606.14368v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [OdysSim: Building Foundation Models...](https://arxiv.org/abs/2606.14199v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Observing Teachers' Instrumental Pe...](https://arxiv.org/abs/2606.14358v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [A Programmer's Guide to Cascaded Ad...](https://arxiv.org/abs/2606.14146v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Natively Unlearnable Large Language...](https://arxiv.org/abs/2606.13873v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [TA-RAG: Tone-Aware Retrieval-Augmen...](https://arxiv.org/abs/2606.06794v2) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Be My Tutor: On-Policy Co-Distillation for Mutual LLM Improvement via Peer Feedback

- **作者**: Woohyeon Byeon, Jiwon Jeon, Jeonghye Kim, Youngchul Sung
- **发布日期**: 2026-06-12
- **链接**: [arXiv:2606.14368v1](https://arxiv.org/abs/2606.14368v1) | [PDF](https://arxiv.org/pdf/2606.14368v1)
- **分类**: cs.LG, cs.CL
- **含金量**: 20/43 分

### 摘要

We study multi-domain LLM training in which two models, each stronger in a different domain, co-evolve by tutoring each other through on-policy feedback.

Unlike one-way distillation or single-model fine-tuning, our goal is mutual Pareto improvement: each model improves across domains without losing its original strength.

To this end, we propose On-Policy Co-Distillation (OPCoD), where each student's self-distillation is conditioned on its own correct rollout and feedback from its peer.

To make feedback exchange effective, OPCoD uses cognizance-based gating to decide when to give feedback and f

### AI 总结

总结生成失败

---

## 2. OdysSim: Building Foundation Models for Human Behavior Simulation

- **作者**: Xuhui Zhou, Weiwei Sun, Weihua Du, Jiarui Liu, Haojia Sun
- **发布日期**: 2026-06-12
- **链接**: [arXiv:2606.14199v1](https://arxiv.org/abs/2606.14199v1) | [PDF](https://arxiv.org/pdf/2606.14199v1)
- **分类**: cs.CL, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

Large language models are increasingly deployed as human simulators for interactive evaluation and social simulation.

Yet helpfulness-driven post-training pulls them toward a homogeneous, overly agreeable assistant register, creating a behavioral Sim2Real gap.

We present OdysSim, the largest open systematic investigation of behavioral foundation models, i.e., models trained to simulate human behavior at scale.

We propose SOUL, a taxonomy of five capability axes (CONV, SS, COG, ROLE, EVAL) that unifies 62 datasets and 23 benchmark tasks under one framework.

Specifically, we curate the OdysSim c

### AI 总结

总结生成失败

---

## 3. Observing Teachers' Instrumental Pedagogical Orchestration in Synchronous Online Learning: A Multimodal Grid Based on Videoconferencing Traces

- **作者**: Intissar Bamou, Christine Michel, Hassina El Kechai
- **发布日期**: 2026-06-12
- **链接**: [arXiv:2606.14358v1](https://arxiv.org/abs/2606.14358v1) | [PDF](https://arxiv.org/pdf/2606.14358v1)
- **分类**: cs.CY
- **含金量**: 20/43 分

### 摘要

Synchronous online teaching environments pose specific challenges for the analysis of pedagogical activity as teaching takes place via videoconferencing platforms and interactions are multimodal.

While pedagogical orchestration has been extensively studied in the context of face-to-face courses and at the level of instructional design, the analysis of teaching in videoconferencing environments remains under-explored and insufficiently instrumented in terms of methodology.

This article proposes a multimodal observation grid designed to analyze the instrumentalised pedagogical orchestration of t

### AI 总结

总结生成失败

---

## 4. A Programmer's Guide to Cascaded Adaptive Combiners: Online Learning by Biologically Accurate Models of Multilayer Neuron Networks

- **作者**: Martin Nilsson, Denis Kleyko
- **发布日期**: 2026-06-12
- **链接**: [arXiv:2606.14146v1](https://arxiv.org/abs/2606.14146v1) | [PDF](https://arxiv.org/pdf/2606.14146v1)
- **分类**: cs.NE
- **含金量**: 20/43 分

### 摘要

Learning in biological multilayer neuronal networks offers insights that extend beyond the classical weighted-sum neuron model commonly used in artificial neural networks.

This article presents an accessible guide to a mechanistic neuronal network model that more accurately captures aspects of biological computation while enabling a simple yet powerful mechanism for learning in multilayer neural networks.

The proposed approach supports efficient online streamed learning and provides a practical alternative to backpropagation.

We demonstrate its potential in an image classification task, achiev

### AI 总结

总结生成失败

---

## 5. Natively Unlearnable Large Language Models

- **作者**: Gaurav R. Ghosal, Pratyush Maini, Aditi Raghunathan
- **发布日期**: 2026-06-11
- **链接**: [arXiv:2606.13873v1](https://arxiv.org/abs/2606.13873v1) | [PDF](https://arxiv.org/pdf/2606.13873v1)
- **分类**: cs.LG, cs.CL
- **含金量**: 20/43 分

### 摘要

Unlearning aims to remove the influence of specific training data sources, but this has proved challenging because the contributions of different sources are entangled within the model.

Isolating source contributions to disjoint parameters makes removal easier, though it obstructs joint learning across sources.

We propose NULLs (Natively Unlearnable LLMs), a model class that satisfies the two opposing goals of isolating source-specific contributions and learning jointly across sources, by training a set of shared backbone neurons alongside a pool of sparsely activated sinks.

During training, i

### AI 总结

总结生成失败

---

## 6. TA-RAG: Tone-Aware Retrieval-Augmented Generation for Peer-Support Health Communication

- **作者**: Yong-Bin Kang, Anthony McCosker
- **发布日期**: 2026-06-05
- **链接**: [arXiv:2606.06794v2](https://arxiv.org/abs/2606.06794v2) | [PDF](https://arxiv.org/pdf/2606.06794v2)
- **分类**: cs.CL, cs.IR
- **含金量**: 20/43 分

### 摘要

Retrieval-augmented generation (RAG) successfully grounds large language model (LLM) outputs in trusted documents, but factual grounding alone is insufficient for sensitive peer-support health communication.

In domains such as HIV peer support, responses must also be accessible, stigma-free, empathetic, and tailored to the recipient.

This paper presents TA-RAG, a lightweight, prompt-based tone-aware RAG framework that embeds explicit tone control into a RAG pipeline without requiring model fine-tuning.

We operationalise tone across four core components: stigma-free rewriting, readability adjus

### AI 总结

总结生成失败

---

