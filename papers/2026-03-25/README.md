# 大数据+AI 领域论文日报

**日期**: 2026-03-25

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Off-Policy Value-Based Reinforcemen...](https://arxiv.org/abs/2603.23355v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Can an LLM Detect Instances of Micr...](https://arxiv.org/abs/2603.23073v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [KALAVAI: Predicting When Independen...](https://arxiv.org/abs/2603.22755v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Detecting Non-Membership in LLM Tra...](https://arxiv.org/abs/2603.22707v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Edge Radar Material Classification ...](https://arxiv.org/abs/2603.23342v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [AI Lifecycle-Aware Feasibility Fram...](https://arxiv.org/abs/2603.23252v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Rao-Blackwellized Stein Gradient De...](https://arxiv.org/abs/2603.23039v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Concept-based explanations of Segme...](https://arxiv.org/abs/2603.23020v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [DAK-UCB: Diversity-Aware Prompt Rou...](https://arxiv.org/abs/2603.23140v1) | 待分析 | 评估失败 | [Code](https://github.com/Donya-Jafari/DAK-UCB.) | 20/43 |
| 10 | [COMPASS-Hedge: Learning Safely With...](https://arxiv.org/abs/2603.22348v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Off-Policy Value-Based Reinforcement Learning for Large Language Models

- **作者**: Peng-Yuan Wang, Ziniu Li, Tian Xu, Bohan Yang, Tian-Shuo Liu
- **发布日期**: 2026-03-24
- **链接**: [arXiv:2603.23355v1](https://arxiv.org/abs/2603.23355v1) | [PDF](https://arxiv.org/pdf/2603.23355v1)
- **分类**: cs.LG, cs.CL
- **含金量**: 20/43 分

### 摘要

Improving data utilization efficiency is critical for scaling reinforcement learning (RL) for long-horizon tasks where generating trajectories is expensive.

However, the dominant RL methods for LLMs are largely on-policy: they update each batch of data only once, discard it, and then collect fresh samples, resulting in poor sample efficiency.

In this work, we explore an alternative value-based RL framework for LLMs that naturally enables off-policy learning.

We propose ReVal, a Bellman-update-based method that combines stepwise signals capturing internal consistency with trajectory-level signa

### AI 总结

总结生成失败

---

## 2. Can an LLM Detect Instances of Microservice Infrastructure Patterns?

- **作者**: Carlos Eduardo Duarte, Neil B. Harrison, Filipe Figueiredo Correia, Ademar Aguiar, Pavlína Gonçalves
- **发布日期**: 2026-03-24
- **链接**: [arXiv:2603.23073v1](https://arxiv.org/abs/2603.23073v1) | [PDF](https://arxiv.org/pdf/2603.23073v1)
- **分类**: cs.SE, cs.AI
- **含金量**: 20/43 分

### 摘要

Architectural patterns are frequently found in various software artifacts.

The wide variety of patterns and their implementations makes detection challenging with current tools, especially since they often only support detecting patterns in artifacts written in a single language.

Large Language Models (LLMs), trained on a diverse range of software artifacts and knowledge, might overcome the limitations of existing approaches.

However, their true effectiveness and the factors influencing their performance have not yet been thoroughly examined.

To better understand this, we developed MicroPAD.

T

### AI 总结

总结生成失败

---

## 3. KALAVAI: Predicting When Independent Specialist Fusion Works -- A Quantitative Model for Post-Hoc Cooperative LLM Training

- **作者**: Ramchand Kumaresan
- **发布日期**: 2026-03-24
- **链接**: [arXiv:2603.22755v1](https://arxiv.org/abs/2603.22755v1) | [PDF](https://arxiv.org/pdf/2603.22755v1)
- **分类**: cs.CL, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

Independently trained domain specialists can be fused post-hoc into a single model that outperforms any individual specialist, and the gain is predictable: gain = 0.82 x divergence - 2.72 (R^2 = 0.856, n=6, 3-26% divergence).

This enables practitioners to estimate cooperative value before committing compute.

Below ~3.3% divergence, gains approach zero.In the KALAVAI protocol, contributors fine-tune copies of a shared checkpoint independently, then submit for lightweight MoE routing (500 steps).

Gains are consistent: +7.72% at 410M (+/-0.02%, 3 seeds), +7.49% at 1B (+/-0.01%, 3 seeds), +6.53% a

### AI 总结

总结生成失败

---

## 4. Detecting Non-Membership in LLM Training Data via Rank Correlations

- **作者**: Pranav Shetty, Mirazul Haque, Zhiqiang Ma, Xiaomo Liu
- **发布日期**: 2026-03-24
- **链接**: [arXiv:2603.22707v1](https://arxiv.org/abs/2603.22707v1) | [PDF](https://arxiv.org/pdf/2603.22707v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

As large language models (LLMs) are trained on increasingly vast and opaque text corpora, determining which data contributed to training has become essential for copyright enforcement, compliance auditing, and user trust.

While prior work focuses on detecting whether a dataset was used in training (membership inference), the complementary problem -- verifying that a dataset was not used -- has received little attention.

We address this gap by introducing PRISM, a test that detects dataset-level non-membership using only grey-box access to model logits.

Our key insight is that two models that h

### AI 总结

总结生成失败

---

## 5. Edge Radar Material Classification Under Geometry Shifts

- **作者**: Jannik Hohmann, Dong Wang, Andreas Nüchter
- **发布日期**: 2026-03-24
- **链接**: [arXiv:2603.23342v1](https://arxiv.org/abs/2603.23342v1) | [PDF](https://arxiv.org/pdf/2603.23342v1)
- **分类**: cs.RO, cs.AI
- **含金量**: 20/43 分

### 摘要

Material awareness can improve robotic navigation and interaction, particularly in conditions where cameras and LiDAR degrade.

We present a lightweight mmWave radar material classification pipeline designed for ultra-low-power edge devices (TI IWRL6432), using compact range-bin intensity descriptors and a Multilayer Perceptron (MLP) for real-time inference.

While the classifier reaches a macro-F1 of 94.2\% under the nominal training geometry, we observe a pronounced performance drop under realistic geometry shifts, including sensor height changes and small tilt angles.

These perturbations indu

### AI 总结

总结生成失败

---

## 6. AI Lifecycle-Aware Feasibility Framework for Split-RIC Orchestration in NTN O-RAN

- **作者**: Daniele Tarchi
- **发布日期**: 2026-03-24
- **链接**: [arXiv:2603.23252v1](https://arxiv.org/abs/2603.23252v1) | [PDF](https://arxiv.org/pdf/2603.23252v1)
- **分类**: cs.NI, cs.AI
- **含金量**: 20/43 分

### 摘要

Integrating Artificial Intelligence (AI) into Non-Terrestrial Networks (NTN) is constrained by the joint limits of satellite SWaP and feeder-link capacity, which directly impact O-RAN closed-loop control and model lifecycle management.

This paper studies the feasibility of distributing the O-RAN control hierarchy across Ground, LEO, and GEO segments through a Split-RIC architecture.

We compare three deployment scenarios: (i) ground-centric control with telemetry streaming, (ii) ground--LEO Split-RIC with on-board inference and store-and-forward learning, and (iii) GEO--LEO multi-layer control 

### AI 总结

总结生成失败

---

## 7. Rao-Blackwellized Stein Gradient Descent for Joint State-Parameter Estimation

- **作者**: Milad Banitalebi Dehkordi, Manas Mejari, Dario Piga
- **发布日期**: 2026-03-24
- **链接**: [arXiv:2603.23039v1](https://arxiv.org/abs/2603.23039v1) | [PDF](https://arxiv.org/pdf/2603.23039v1)
- **分类**: eess.SY
- **含金量**: 20/43 分

### 摘要

We present a filtering framework for online joint state estimation and parameter identification in nonlinear, time-varying systems.

The algorithm uses Rao-Blackwellization technique to infer joint state-parameter posteriors efficiently.

In particular, conditional state distributions are computed analytically via Kalman filtering, while model parameters including process and measurement noise covariances are approximated using particle-based Stein Variational Gradient Descent (SVGD), enabling stable real-time inference.

We prove a theoretical consistency result by bounding the impact of the SVG

### AI 总结

总结生成失败

---

## 8. Concept-based explanations of Segmentation and Detection models in Natural Disaster Management

- **作者**: Samar Heydari, Jawher Said, Galip Ümit Yolcu, Evgenii Kortukov, Elena Golimblevskaia
- **发布日期**: 2026-03-24
- **链接**: [arXiv:2603.23020v1](https://arxiv.org/abs/2603.23020v1) | [PDF](https://arxiv.org/pdf/2603.23020v1)
- **分类**: cs.CV, cs.AI
- **含金量**: 20/43 分

### 摘要

Deep learning models for flood and wildfire segmentation and object detection enable precise, real-time disaster localization when deployed on embedded drone platforms.

However, in natural disaster management, the lack of transparency in their decision-making process hinders human trust required for emergency response.

To address this, we present an explainability framework for understanding flood segmentation and car detection predictions on the widely used PIDNet and YOLO architectures.

More specifically, we introduce a novel redistribution strategy that extends Layer-wise Relevance Propagat

### AI 总结

总结生成失败

---

## 9. DAK-UCB: Diversity-Aware Prompt Routing for LLMs and Generative Models

- **作者**: Donya Jafari, Farzan Farnia
- **发布日期**: 2026-03-24
- **链接**: [arXiv:2603.23140v1](https://arxiv.org/abs/2603.23140v1) | [PDF](https://arxiv.org/pdf/2603.23140v1)
- **分类**: cs.LG
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/Donya-Jafari/DAK-UCB.) ⭐ 0

### 摘要

The expansion of generative AI and LLM services underscores the growing need for adaptive mechanisms to select an appropriate available model to respond to a user's prompts.

Recent works have proposed offline and online learning formulations to identify the optimal generative AI model for an input prompt, based solely on maximizing prompt-based fidelity evaluation scores, e.g., CLIP-Score in text-to-image generation.

However, such fidelity-based selection methods overlook the diversity of generated outputs, and hence, they can fail to address potential diversity shortcomings in the generated r

### AI 总结

总结生成失败

---

## 10. COMPASS-Hedge: Learning Safely Without Knowing the World

- **作者**: Ting Hu, Luanda Cai, Manolis Vlatakis
- **发布日期**: 2026-03-22
- **链接**: [arXiv:2603.22348v1](https://arxiv.org/abs/2603.22348v1) | [PDF](https://arxiv.org/pdf/2603.22348v1)
- **分类**: cs.LG, cs.GT
- **含金量**: 20/43 分

### 摘要

Online learning algorithms often faces a fundamental trilemma: balancing regret guarantees between adversarial and stochastic settings and providing baseline safety against a fixed comparator.

While existing methods excel in one or two of these regimes, they typically fail to unify all three without sacrificing optimal rates or requiring oracle access to problem-dependent parameters.

In this work, we bridge this gap by introducing COMPASS-Hedge.

Our algorithm is the first full-information method to simultaneously achieve: i) Minimax-optimal regret in adversarial environments; ii) Instance-op

### AI 总结

总结生成失败

---

