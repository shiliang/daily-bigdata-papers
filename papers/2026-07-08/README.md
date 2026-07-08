# 大数据+AI 领域论文日报

**日期**: 2026-07-08

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Unified Audio Intelligence Without ...](https://arxiv.org/abs/2607.05196v2) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Not All Refusals Are Equal: How Saf...](https://arxiv.org/abs/2607.02714v2) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [GORIO: GPU-Centered Remote I/O for ...](https://arxiv.org/abs/2607.04415v2) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Prior-First, Condition-Second: Scal...](https://arxiv.org/abs/2607.05938v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Adaptive and Neural Operator Contro...](https://arxiv.org/abs/2607.06425v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Scalable Perturbation Learning for ...](https://arxiv.org/abs/2607.06079v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [SCOReD: Student-Aware CoT Optimizat...](https://arxiv.org/abs/2607.05734v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [SpanUQ: Span-Level Uncertainty Quan...](https://arxiv.org/abs/2607.05721v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [PHOENIX: Resilient LLM Training wit...](https://arxiv.org/abs/2607.01646v2) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Patch Knowledge Transfer for Effici...](https://arxiv.org/abs/2607.05605v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Unified Audio Intelligence Without Regressing on Text Intelligence

- **作者**: Zhifeng Kong, Sang-gil Lee, Jaehyeon Kim, Boxin Wang, Zihan Liu
- **发布日期**: 2026-07-06
- **链接**: [arXiv:2607.05196v2](https://arxiv.org/abs/2607.05196v2) | [PDF](https://arxiv.org/pdf/2607.05196v2)
- **分类**: cs.CL, cs.AI, cs.LG, cs.SD, eess.AS
- **含金量**: 20/43 分

### 摘要

Audio intelligence involves understanding, reasoning about, and generating both audio and speech.

In this work, we introduce Nemotron-Labs-Audex-30B-A3B (Audex), a unified audio-text LLM built on Nemotron-Cascade-2-30B-A3B, a strong text-only MoE LLM.

Audex adopts a simple unified design with a single Transformer decoder: audio inputs are encoded and projected into the text embedding space, while text tokens and quantized audio output tokens are treated uniformly during generation.

This architecture enables strong audio-text fusion, seamless multimodal generation, and compatibility with standa

### AI 总结

总结生成失败

---

## 2. Not All Refusals Are Equal: How Safety Alignment Fails Cybersecurity at Scale

- **作者**: Vadym Hadetskyi, Dario Pasquini, Artem Sorokin
- **发布日期**: 2026-07-02
- **链接**: [arXiv:2607.02714v2](https://arxiv.org/abs/2607.02714v2) | [PDF](https://arxiv.org/pdf/2607.02714v2)
- **分类**: cs.CR, cs.AI
- **含金量**: 20/43 分

### 摘要

There is no doubt that safety alignment is an essential step in LLM training.

However, conceptually it does not distinguish between various domains and the level of potential harm of a query, which creates significant complications in the fields like cyber security, where a model should not be constrained by its safety circuits to accomplish the goals of legitimate, authorized operations.

In this work, we share our findings from a large scale abliteration experiment on 24 open-source LLMs and show that domain-specific abliteration is achievable with standard methodology on the example of a 1T-

### AI 总结

总结生成失败

---

## 3. GORIO: GPU-Centered Remote I/O for Graph ANNS over NVMe-oF

- **作者**: Gen Zhang, Wenhao Gu, Shan Huang, Xinhai Chen
- **发布日期**: 2026-07-05
- **链接**: [arXiv:2607.04415v2](https://arxiv.org/abs/2607.04415v2) | [PDF](https://arxiv.org/pdf/2607.04415v2)
- **分类**: cs.DC, cs.DB
- **含金量**: 20/43 分

### 摘要

Graph-based approximate nearest neighbor search (ANNS) is increasingly used in vector databases and retrieval-augmented generation services, but large vector indexes often exceed the memory capacity of a single GPU server.

NVMe over Fabrics (NVMe-oF) provides an attractive storage-disaggregation substrate, yet existing remote storage paths are still largely CPU-centered: the CPU forms I/O requests, drives transport progress, and determines when GPU computation can resume.

This organization is poorly matched to graph ANNS, where the next data access is discovered inside GPU graph traversal.

T

### AI 总结

总结生成失败

---

## 4. Prior-First, Condition-Second: Scalable and Controllable Hand Motion Completion

- **作者**: Mingyi Shi, Xuelin Chen, Taku Komura
- **发布日期**: 2026-07-07
- **链接**: [arXiv:2607.05938v1](https://arxiv.org/abs/2607.05938v1) | [PDF](https://arxiv.org/pdf/2607.05938v1)
- **分类**: cs.GR, cs.RO
- **含金量**: 20/43 分

### 摘要

Synthesizing hand motion that matches the full body motion and the semantic labels is a difficult task due to their high degrees of freedom and the lack of semantic labels.

To cope with this issue, we propose a prior-first, condition-second framework for body-conditioned hand motion completion.

Our framework first learns a generic body-hand kinematic prior from large-scale unstructured and unlabeled motion data, capturing the intrinsic coordination between global body dynamics and hand articulation.

Semantic control is then introduced through lightweight adaptation on top of the frozen prior, 

### AI 总结

总结生成失败

---

## 5. Adaptive and Neural Operator Control of Nonlinear Volterra Hyperbolic PDEs

- **作者**: Miroslav Krstic
- **发布日期**: 2026-07-07
- **链接**: [arXiv:2607.06425v1](https://arxiv.org/abs/2607.06425v1) | [PDF](https://arxiv.org/pdf/2607.06425v1)
- **分类**: eess.SY, math.OC
- **含金量**: 20/43 分

### 摘要

Adaptive control learns the plant online; neural-operator control learns the control gains offline.

We bring the two together for a class of nonlinear hyperbolic PDEs whose dynamics are governed by an unknown Volterra series of arbitrarily many kernels.

An observer-based passive identifier learns a truncation of this series online.

The infinite-dimensional map that synthesizes the backstepping kernels from the parameter estimates -- a cascade of PDEs on simplex domains of increasing dimension, prohibitive to solve in real time -- is approximated once, offline, by a neural operator.

The closed 

### AI 总结

总结生成失败

---

## 6. Scalable Perturbation Learning for Online Self-Supervised Echo State Networks

- **作者**: Taiki Yamada, Kantaro Fujiwara
- **发布日期**: 2026-07-07
- **链接**: [arXiv:2607.06079v1](https://arxiv.org/abs/2607.06079v1) | [PDF](https://arxiv.org/pdf/2607.06079v1)
- **分类**: cs.LG, cs.NE
- **含金量**: 20/43 分

### 摘要

Intelligent systems should not only solve tasks but also adapt under real-world constraints.

Autonomous adaptation via self-supervised learning, sequential adaptation via online learning, and memory-efficient implementation via perturbation-based learning are important requirements for such systems.

However, these requirements are generally in tension for high-dimensional systems, because perturbation-based learning suffers from variance that grows with the dimension of the perturbed variables.

In this study, we focus on echo state networks (ESNs), where this tension naturally arises in larg

### AI 总结

总结生成失败

---

## 7. SCOReD: Student-Aware CoT Optimization for Recommendation Distillation

- **作者**: Haz Sameen Shahgir, Yufei Li, Frank Shyu, Luke Simon, Sandeep Pandey
- **发布日期**: 2026-07-07
- **链接**: [arXiv:2607.05734v1](https://arxiv.org/abs/2607.05734v1) | [PDF](https://arxiv.org/pdf/2607.05734v1)
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

## 8. SpanUQ: Span-Level Uncertainty Quantification for Large Language Model Generation

- **作者**: Yimeng Zhang, Yingying Zhuang, Ziyi Wang, Yuxuan Lu, Pei Chen
- **发布日期**: 2026-07-07
- **链接**: [arXiv:2607.05721v1](https://arxiv.org/abs/2607.05721v1) | [PDF](https://arxiv.org/pdf/2607.05721v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

Uncertainty estimation is essential not only for the trustworthy deployment of large language models (LLMs) but also as a foundation for self-refinement in LLM generation.

However, existing approaches operate at suboptimal granularities: token-level scores lack semantic coherence, while sequence-level scores fail to localize errors.

We formalize Span-Level Uncertainty Estimation (SLUE), a new task that targets the natural granularity for uncertainty: semantically coherent text spans, each conveying a single assessable unit of meaning.

To address this task, we introduce SPANUQ, a lightweight pr

### AI 总结

总结生成失败

---

## 9. PHOENIX: Resilient LLM Training with Hot-Swapping via Zero-Overhead Checkpoint

- **作者**: Haotian Xie, Junlin Chen, Mingkai Zheng, Lishan Yang, Zhao Zhang
- **发布日期**: 2026-07-02
- **链接**: [arXiv:2607.01646v2](https://arxiv.org/abs/2607.01646v2) | [PDF](https://arxiv.org/pdf/2607.01646v2)
- **分类**: cs.LG, cs.DC
- **含金量**: 20/43 分

### 摘要

State-of-the-art large language model (LLM) training takes tens of thousands of graphics processing units (GPUs) for months and encounters failures across the software and hardware stack.

Existing fault-tolerance mechanisms either impose non-trivial overhead during failure-free execution or suffer from prolonged recovery latency, particularly under scenarios where a small subset of compute nodes experience permanent failures.

%The tradeoff between failure-free overhead and recovery latency forms a space forms a Pareto frontier We present PHOENIX to simultaneously address both optimization obje

### AI 总结

总结生成失败

---

## 10. Patch Knowledge Transfer for Efficient AI-Generated Image Quality Assessment

- **作者**: Jiquan Yuan
- **发布日期**: 2026-07-06
- **链接**: [arXiv:2607.05605v1](https://arxiv.org/abs/2607.05605v1) | [PDF](https://arxiv.org/pdf/2607.05605v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

With the rapid advancement of image generation technologies, perceptual quality assessment of AI-generated images has emerged as a crucial research direction in computer vision.

The core challenge of this task lies in achieving efficient quality assessment for massive generated images.

Current mainstream approaches exhibit two key limitations: 1) Methods employing complex feature extraction strategies, while improving performance, incur prohibitive computational costs that hinder real-time inference; 2) Simple image scaling-based solutions, despite their computational efficiency, demonstrate s

### AI 总结

总结生成失败

---

