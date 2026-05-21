# 大数据+AI 领域论文日报

**日期**: 2026-05-21

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [High-speed Networking for Giga-Scal...](https://arxiv.org/abs/2605.21187v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [LiteViLNet: Lightweight Vision-LiDA...](https://arxiv.org/abs/2605.21007v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [ScenePilot: Controllable Boundary-D...](https://arxiv.org/abs/2605.21168v1) | 待分析 | 评估失败 | [Code](https://github.com/QiyuRuan/ScenePilot.) | 20/43 |
| 4 | [torchtune: PyTorch native post-trai...](https://arxiv.org/abs/2605.21442v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [DEL: Digit Entropy Loss for Numeric...](https://arxiv.org/abs/2605.20369v1) | 待分析 | 评估失败 | [Code](https://github.com/PolyU-VCLab/DEL) | 20/43 |
| 6 | [MixRea: Benchmarking Explicit-Impli...](https://arxiv.org/abs/2605.20128v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Neurosymbolic Learning for Inferenc...](https://arxiv.org/abs/2605.20098v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Introspective X Training: Feedback ...](https://arxiv.org/abs/2605.20285v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Charon: A Unified and Fine-Grained ...](https://arxiv.org/abs/2605.17164v2) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [STABLE: Simulation-Ready Tabletop L...](https://arxiv.org/abs/2605.16137v2) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. High-speed Networking for Giga-Scale AI Factories

- **作者**: Sajy Khashab, Albert Gran Alcoz, Alon Gal, Jacky Romano, Rani Abboud
- **发布日期**: 2026-05-20
- **链接**: [arXiv:2605.21187v1](https://arxiv.org/abs/2605.21187v1) | [PDF](https://arxiv.org/pdf/2605.21187v1)
- **分类**: cs.NI
- **含金量**: 20/43 分

### 摘要

As distributed model training scales to span hundreds of thousands of GPUs, scale-out networks face unprecedented performance and efficiency demands.

NVIDIA Spectrum-X Ethernet has been designed from the ground up to achieve predictable and stable network performance with high utilization and low latency.

This paper presents the Spectrum-X multiplane architecture, which replaces hierarchical depth with topological parallelism, and introduces hardware-accelerated load balancing in NICs and switches as the key architectural approach to provide fast reaction to highly dynamic network conditions a

### AI 总结

总结生成失败

---

## 2. LiteViLNet: Lightweight Vision-LiDAR Fusion Network for Efficient Road Segmentation

- **作者**: Daojie Peng, Bingtao Wang, Fulong Ma, Liang Zhang, Jun Ma
- **发布日期**: 2026-05-20
- **链接**: [arXiv:2605.21007v1](https://arxiv.org/abs/2605.21007v1) | [PDF](https://arxiv.org/pdf/2605.21007v1)
- **分类**: cs.CV, cs.RO
- **含金量**: 20/43 分

### 摘要

Road segmentation is a fundamental perception task for autonomous driving and intelligent robotic systems, requiring both high accuracy and real-time inference, especially for deployment on resource-constrained edge devices.

Existing multi-modal road segmentation methods often rely on heavy transformer-based encoders to achieve state-of-the-art performance, but their enormous computational cost prohibits real-time deployment on embedded platforms.

To address this dilemma, we propose \textbf{LiteViLNet}, a lightweight multi-modal network that fuses RGB texture information and LiDAR geometric in

### AI 总结

总结生成失败

---

## 3. ScenePilot: Controllable Boundary-Driven Critical Scenario Generation for Autonomous Driving

- **作者**: Qiyu Ruan, Yuxuan Wang, He Li, Zhenning Li, Cheng-zhong Xu
- **发布日期**: 2026-05-20
- **链接**: [arXiv:2605.21168v1](https://arxiv.org/abs/2605.21168v1) | [PDF](https://arxiv.org/pdf/2605.21168v1)
- **分类**: cs.AI
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/QiyuRuan/ScenePilot.) ⭐ 0

### 摘要

Safety-critical scenarios are central to evaluating autonomous driving systems, yet their rarity in naturalistic logs makes simulation-based stress testing indispensable.

Most scenario generation methods treat surrounding agents as adversaries, but they either (i) induce failures without explicitly modeling vehicle-road physical limits, yielding visually extreme yet physically unsolvable crashes, or (ii) enforce physical feasibility or policy feasibility in isolation, which can over-focus on aggressive maneuvers or remain tied to a controller-dependent capability boundary.

We propose ScenePilo

### AI 总结

总结生成失败

---

## 4. torchtune: PyTorch native post-training library

- **作者**: Mark Obozov, Maxime Griot, Joseph Cummings, Evan Smothers, Felipe Mello
- **发布日期**: 2026-05-20
- **链接**: [arXiv:2605.21442v1](https://arxiv.org/abs/2605.21442v1) | [PDF](https://arxiv.org/pdf/2605.21442v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

Modern LLMs typically require multistage training pipelines to achieve strong downstream performance, with post-training serving as the main interface for adapting open-weight models.

We introduce torchtune, a PyTorch-native library designed to streamline the post-training lifecycle of LLMs, enabling efficient fine-tuning, experimentation, and deployment-oriented workflows.

Unlike many existing fine-tuning frameworks, which often optimize for ease of use, specialized recipes, or hardware efficiency at the cost of transparency and extensibility, torchtune emphasizes modularity, hackability, and

### AI 总结

总结生成失败

---

## 5. DEL: Digit Entropy Loss for Numerical Learning of Large Language Models

- **作者**: Zhaohui Zheng, Chenhang He, Shihao Wang, Yuxuan Li, Ming-Ming Cheng
- **发布日期**: 2026-05-19
- **链接**: [arXiv:2605.20369v1](https://arxiv.org/abs/2605.20369v1) | [PDF](https://arxiv.org/pdf/2605.20369v1)
- **分类**: cs.CL, cs.AI, cs.LG
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/PolyU-VCLab/DEL) ⭐ 0

### 摘要

Number prediction stands as a fundamental capability of large language models (LLMs) in mathematical problem-solving and code generation.

The widely adopted maximum likelihood estimation (MLE) for LLM training is not tailored to number prediction.

Recently, penalty-driven approaches, e.g., Number Token Loss and Discretized Distance Loss, introduce an inductive bias of numerical distance but induce over-sharpened and over-flattened digit distributions, respectively.

In this paper, we make an in-depth analysis on LLM numerical learning, and show that existing numerical learning methods conceptua

### AI 总结

总结生成失败

---

## 6. MixRea: Benchmarking Explicit-Implicit Reasoning in Large Language Models

- **作者**: Yuanqing Cai, Ziyi Huang, Minhao Liu, Lixin Duan, Wen Li
- **发布日期**: 2026-05-19
- **链接**: [arXiv:2605.20128v1](https://arxiv.org/abs/2605.20128v1) | [PDF](https://arxiv.org/pdf/2605.20128v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

Large language models (LLMs) are increasingly integrated into high-stakes decision-making.

Inspired by the theory of \emph{inattentional blindness} in human cognition, we investigate whether LLMs, trained on human-preferred corpora that embed attentional biases, exhibit a similar limitation: \emph{failing to attend to subtle yet important contextual cues under explicit task instructions}.

To evaluate this, we introduce the task of \textbf{explicit-implicit reasoning} and present \textbf{MixRea}, a benchmark of 2,246 multiple-choice questions across 9 reasoning types with varying distributions 

### AI 总结

总结生成失败

---

## 7. Neurosymbolic Learning for Inference-Time Argumentation

- **作者**: Gabriel Freedman, Adam Dejl, Adam Gould,  Mansi, Lihu Chen
- **发布日期**: 2026-05-19
- **链接**: [arXiv:2605.20098v1](https://arxiv.org/abs/2605.20098v1) | [PDF](https://arxiv.org/pdf/2605.20098v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

Claim verification is an important problem in high-stakes settings, including health and finance.

When information underpinning claims is incomplete or conflicting, uncertain answers may be more appropriate than binary true or false classifications.

In all cases, faithful explanations of the considerations determining the final verdict are crucial.

We introduce inference-time argumentation (ITA), a trainable neurosymbolic framework for ternary claim verification in which a formal argumentation semantics giving the strength of claims is used both (i) to guide LLM training as models learn to gen

### AI 总结

总结生成失败

---

## 8. Introspective X Training: Feedback Conditioning Improves Scaling Across all LLM Training Stages

- **作者**: Brandon Cui, Ximing Lu, Jaehun Jung, Syeda Nahida Akter, Hyunwoo Kim
- **发布日期**: 2026-05-19
- **链接**: [arXiv:2605.20285v1](https://arxiv.org/abs/2605.20285v1) | [PDF](https://arxiv.org/pdf/2605.20285v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

We tackle the question of how to scale more efficiently across the many, ever-growing stages of current LLM training pipelines.

Our guiding intuition stems from the fact that the dynamics of later stages of the pipeline, e.g.

post-training, can be used to inform earlier stages such as pre-training.

To this end, we propose Introspective Training (or IXT), inspired by offline reward-conditioned reinforcement learning and applicable to any stage of training.

IXT uses a thinking reward model to annotate data with natural language critique based feedback, enabling quality aware training from the ea

### AI 总结

总结生成失败

---

## 9. Charon: A Unified and Fine-Grained Simulator for Large-Scale LLM Training and Inference

- **作者**: Mengtian Yang, Zhekun Zhang, Mingheng Wu, Jianwen Yan, Hanshi Sun
- **发布日期**: 2026-05-16
- **链接**: [arXiv:2605.17164v2](https://arxiv.org/abs/2605.17164v2) | [PDF](https://arxiv.org/pdf/2605.17164v2)
- **分类**: cs.DC, cs.AI, cs.LG, cs.PL
- **含金量**: 20/43 分

### 摘要

Deploying large-scale LLM training and inference with optimal performance is exceptionally challenging due to a complex design space of parallelism strategies, system optimizations, and hardware configurations.

Accurate and rapid performance simulation is critical for guiding optimization efforts and system studies by validating "what-if" Hooker Figure hypotheses.

To address this, we introduce Charon, a unified, modular, and fine-grained simulator for accurately predicting LLM performance.

Experiments show Charon achieves high accuracy across different models and configurations, with an overal

### AI 总结

总结生成失败

---

## 10. STABLE: Simulation-Ready Tabletop Layout Generation via a Semantics-Physics Dual System

- **作者**: Zhen Luo, Yixuan Yang, Xudong Xu, Jinkun Hao, Zhaoyang Lyu
- **发布日期**: 2026-05-15
- **链接**: [arXiv:2605.16137v2](https://arxiv.org/abs/2605.16137v2) | [PDF](https://arxiv.org/pdf/2605.16137v2)
- **分类**: cs.CV, cs.RO
- **含金量**: 20/43 分

### 摘要

Generating simulation-ready tabletop scenes from task instructions is an intriguing and promising research direction in the field of Embodied AI.

However, existing task-to-scene generation methods rely exclusively on large language models (LLMs) to predict scene layouts, inevitably yielding object collisions or floating due to LLMs' inherent limitations in 3D spatial reasoning.

In this paper, we present STABLE, a semantics-physics dual-system tailored for simulation-ready tabletop scene generation.

STABLE consists of two complementary modules: (i) a Semantic Reasoner, a fine-tuned LLM trained 

### AI 总结

总结生成失败

---

