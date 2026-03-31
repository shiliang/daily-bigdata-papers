# 大数据+AI 领域论文日报

**日期**: 2026-03-31

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Temporal Credit Is Free](https://arxiv.org/abs/2603.28750v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [GPU-Accelerated Optimization of Tra...](https://arxiv.org/abs/2603.28708v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Sim-to-Real Fruit Detection Using S...](https://arxiv.org/abs/2603.28670v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [UniDA3D: A Unified Domain-Adaptive ...](https://arxiv.org/abs/2603.27995v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [OptINC: Optical In-Network-Computin...](https://arxiv.org/abs/2603.28290v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Pre-Deployment Complexity Estimatio...](https://arxiv.org/abs/2603.28282v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Heddle: A Distributed Orchestration...](https://arxiv.org/abs/2603.28101v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [RSR-core: A High-Performance Engine...](https://arxiv.org/abs/2603.27462v1) | 待分析 | 评估失败 | [Code](https://github.com/UIC-InDeXLab/RSR-core.) | 20/43 |
| 9 | [Demo-Pose: Depth-Monocular Modality...](https://arxiv.org/abs/2603.27533v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Debiasing Large Language Models tow...](https://arxiv.org/abs/2603.27057v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Temporal Credit Is Free

- **作者**: Aur Shalev Merin
- **发布日期**: 2026-03-30
- **链接**: [arXiv:2603.28750v1](https://arxiv.org/abs/2603.28750v1) | [PDF](https://arxiv.org/pdf/2603.28750v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Recurrent networks do not need Jacobian propagation to adapt online.

The hidden state already carries temporal credit through the forward pass; immediate derivatives suffice if you stop corrupting them with stale trace memory and normalize gradient scales across parameter groups.

An architectural rule predicts when normalization is needed: \b{eta}2 is required when gradients must pass through a nonlinear state update with no output bypass, and unnecessary otherwise.

Across ten architectures, real primate neural data, and streaming ML benchmarks, immediate derivatives with RMSprop match or exce

### AI 总结

总结生成失败

---

## 2. GPU-Accelerated Optimization of Transformer-Based Neural Networks for Real-Time Inference

- **作者**: Soutrik Mukherjee, Sangwhan Cha
- **发布日期**: 2026-03-30
- **链接**: [arXiv:2603.28708v1](https://arxiv.org/abs/2603.28708v1) | [PDF](https://arxiv.org/pdf/2603.28708v1)
- **分类**: cs.LG, cs.DC
- **含金量**: 20/43 分

### 摘要

This paper presents the design and evaluation of a GPU-accelerated inference pipeline for transformer models using NVIDIA TensorRT with mixed-precision optimization.

We evaluate BERT-base (110M parameters) and GPT-2 (124M parameters) across batch sizes from 1 to 32 and sequence lengths from 32 to 512.

The system achieves up to 64.4x speedup over CPU baselines, sub-10 ms latency for single-sample inference, and a 63 percent reduction in memory usage.

We introduce a hybrid precision strategy that preserves FP32 for numerically sensitive operations such as softmax and layer normalization, while a

### AI 总结

总结生成失败

---

## 3. Sim-to-Real Fruit Detection Using Synthetic Data: Quantitative Evaluation and Embedded Deployment with Isaac Sim

- **作者**: Martina Hutter-Mironovova
- **发布日期**: 2026-03-30
- **链接**: [arXiv:2603.28670v1](https://arxiv.org/abs/2603.28670v1) | [PDF](https://arxiv.org/pdf/2603.28670v1)
- **分类**: cs.CV, cs.RO
- **含金量**: 20/43 分

### 摘要

This study investigates the effectiveness of synthetic data for sim-to-real transfer in object detection under constrained data conditions and embedded deployment requirements.

Synthetic datasets were generated in NVIDIA Isaac Sim and combined with limited real-world fruit images to train YOLO-based detection models under real-only, synthetic-only, and hybrid regimes.

Performance was evaluated on two test datasets: an in-domain dataset with conditions matching the training data and a domain shift dataset containing real fruit and different background conditions.

Results show that models traine

### AI 总结

总结生成失败

---

## 4. UniDA3D: A Unified Domain-Adaptive Framework for Multi-View 3D Object Detection

- **作者**: Hongjing Wu, Cheng Chi, Jinlin Wu, Yanzhao Su, Zhen Lei
- **发布日期**: 2026-03-30
- **链接**: [arXiv:2603.27995v1](https://arxiv.org/abs/2603.27995v1) | [PDF](https://arxiv.org/pdf/2603.27995v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

Camera-only 3D object detection is critical for autonomous driving, offering a cost-effective alternative to LiDAR based methods.

In particular, multi-view 3D object detection has emerged as a promising direction due to its balanced trade-off between performance and cost.

However, existing methods often suffer significant performance degradation under complex environmental conditions such as nighttime, fog, and rain, primarily due to their reliance on training data collected mostly in ideal conditions.

To address this challenge, we propose UniDA3D, a unified domain-adaptive multi-view 3D objec

### AI 总结

总结生成失败

---

## 5. OptINC: Optical In-Network-Computing for Scalable Distributed Learning

- **作者**: Sijie Fei, Grace Li Zhang, Bing Li, Ulf Schlichtmann
- **发布日期**: 2026-03-30
- **链接**: [arXiv:2603.28290v1](https://arxiv.org/abs/2603.28290v1) | [PDF](https://arxiv.org/pdf/2603.28290v1)
- **分类**: cs.LG, cs.AR
- **含金量**: 20/43 分

### 摘要

Distributed learning is widely used for training large models on large datasets by distributing parts of the model or dataset across multiple devices and aggregating the computed results for subsequent computations or parameter updates.

Existing communication algorithms for distributed learning such as ring all-reduce result in heavy communication overhead between servers.

Since communication in large-scale systems uses optical fibers, we propose an Optical In-Network-Computing (OptINC) architecture to offload the computation in servers onto the optical interconnects.

To execute gradient avera

### AI 总结

总结生成失败

---

## 6. Pre-Deployment Complexity Estimation for Federated Perception Systems

- **作者**: KMA Solaiman, Shafkat Islam, Ruy de Oliveira, Bharat Bhargava
- **发布日期**: 2026-03-30
- **链接**: [arXiv:2603.28282v1](https://arxiv.org/abs/2603.28282v1) | [PDF](https://arxiv.org/pdf/2603.28282v1)
- **分类**: cs.LG, cs.AI, cs.DC
- **含金量**: 20/43 分

### 摘要

Edge AI systems increasingly rely on federated learning to train perception models in distributed, privacy-preserving, and resource-constrained environments.

Yet, before training begins, practitioners often lack practical tools to estimate how difficult a federated learning task will be in terms of achievable accuracy and communication cost.

This paper presents a classifier-agnostic, pre-deployment framework for estimating learning complexity in federated perception systems by jointly modeling intrinsic properties of the data and characteristics of the distributed environment.

The proposed com

### AI 总结

总结生成失败

---

## 7. Heddle: A Distributed Orchestration System for Agentic RL Rollout

- **作者**: Zili Zhang, Yinmin Zhong, Chengxu Yang, Chao Jin, Bingyang Wu
- **发布日期**: 2026-03-30
- **链接**: [arXiv:2603.28101v1](https://arxiv.org/abs/2603.28101v1) | [PDF](https://arxiv.org/pdf/2603.28101v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Agentic Reinforcement Learning (RL) enables LLMs to solve complex tasks by alternating between a data-collection rollout phase and a policy training phase.

During rollout, the agent generates trajectories, i.e., multi-step interactions between LLMs and external tools.

Yet, frequent tool calls induce long-tailed trajectory generation that bottlenecks rollouts.

This stems from step-centric designs that ignore trajectory context, triggering three system problems for long-tail trajectory generation: queueing delays, interference overhead, and inflated per-token time.

We propose Heddle, a trajector

### AI 总结

总结生成失败

---

## 8. RSR-core: A High-Performance Engine for Low-Bit Matrix-Vector Multiplication

- **作者**: Mohsen Dehghankar, Abolfazl Asudeh
- **发布日期**: 2026-03-29
- **链接**: [arXiv:2603.27462v1](https://arxiv.org/abs/2603.27462v1) | [PDF](https://arxiv.org/pdf/2603.27462v1)
- **分类**: cs.DS, cs.LG, cs.PF
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/UIC-InDeXLab/RSR-core.) ⭐ 0

### 摘要

Matrix-vector multiplication is a fundamental building block in neural networks, vector databases, and large language models, particularly during inference.

As a result, efficient matrix-vector multiplication engines directly translate into more efficient inference.

Recent work has explored low-bit quantization of model weights, where matrices are represented using binary (1-bit) or ternary (1.58-bit) values while activation is kept in higher precision.

These representations enable efficient hardware-level computation.

In parallel, algorithms such as Redundant Segment Reduction (RSR) provide t

### AI 总结

总结生成失败

---

## 9. Demo-Pose: Depth-Monocular Modality Fusion For Object Pose Estimation

- **作者**: Rachit Agarwal, Abhishek Joshi, Sathish Chalasani, Woo Jin Kim
- **发布日期**: 2026-03-29
- **链接**: [arXiv:2603.27533v1](https://arxiv.org/abs/2603.27533v1) | [PDF](https://arxiv.org/pdf/2603.27533v1)
- **分类**: cs.CV, cs.AI
- **含金量**: 20/43 分

### 摘要

Object pose estimation is a fundamental task in 3D vision with applications in robotics, AR/VR, and scene understanding.

We address the challenge of category-level 9-DoF pose estimation (6D pose + 3Dsize) from RGB-D input, without relying on CAD models during inference.

Existing depth-only methods achieve strong results but ignore semantic cues from RGB, while many RGB-D fusion models underperform due to suboptimal cross-modal fusion that fails to align semantic RGB cues with 3D geometric representations.

We propose DeMo-Pose, a hybrid architecture that fuses monocular semantic features with d

### AI 总结

总结生成失败

---

## 10. Debiasing Large Language Models toward Social Factors in Online Behavior Analytics through Prompt Knowledge Tuning

- **作者**: Hossein Salemi, Jitin Krishnan, Hemant Purohit
- **发布日期**: 2026-03-28
- **链接**: [arXiv:2603.27057v1](https://arxiv.org/abs/2603.27057v1) | [PDF](https://arxiv.org/pdf/2603.27057v1)
- **分类**: cs.CL, cs.AI
- **含金量**: 20/43 分

### 摘要

Attribution theory explains how individuals interpret and attribute others' behavior in a social context by employing personal (dispositional) and impersonal (situational) causality.

Large Language Models (LLMs), trained on human-generated corpora, may implicitly mimic this social attribution process in social contexts.

However, the extent to which LLMs utilize these causal attributions in their reasoning remains underexplored.

Although using reasoning paradigms, such as Chain-of-Thought (CoT), has shown promising results in various tasks, ignoring social attribution in reasoning could lead to

### AI 总结

总结生成失败

---

