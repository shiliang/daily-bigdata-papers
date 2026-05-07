# 大数据+AI 领域论文日报

**日期**: 2026-05-07

**论文数量**: 8 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [On the Hardness of Junking LLMs](https://arxiv.org/abs/2605.05116v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Height-Guided Projection Reparamete...](https://arxiv.org/abs/2605.05072v1) | 待分析 | 评估失败 | [Code](https://github.com/Rayn-Wu/HiPR.) | 20/43 |
| 3 | [When Life Gives You BC, Make Q-func...](https://arxiv.org/abs/2605.05172v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Adaptive Learning Strategies for Ao...](https://arxiv.org/abs/2605.05055v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Online Nonstochastic Prediction: Lo...](https://arxiv.org/abs/2605.04364v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Topology-Aware Two-Stage Federated ...](https://arxiv.org/abs/2605.04512v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [CCL-D: A High-Precision Diagnostic ...](https://arxiv.org/abs/2605.04478v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [FASQ: Flexible Accelerated Subspace...](https://arxiv.org/abs/2605.04084v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. On the Hardness of Junking LLMs

- **作者**: Marco Rando, Samuel Vaiter
- **发布日期**: 2026-05-06
- **链接**: [arXiv:2605.05116v1](https://arxiv.org/abs/2605.05116v1) | [PDF](https://arxiv.org/pdf/2605.05116v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Large language models (LLMs) are known to be vulnerable to jailbreak attacks, which typically rely on carefully designed prompts containing explicit semantic structure.

These attacks generally operate by fixing an adversarial instruction and optimizing small adversarial components (e.g., suffixes or prefixes).

In this setting, prompt structure is fundamental for performance, and recent results show that even simple random search can achieve strong performance when combined with sophisticated prompt design.

Recently, it has been observed that harmful behaviors can be elicited even without the a

### AI 总结

总结生成失败

---

## 2. Height-Guided Projection Reparameterization for Camera-LiDAR Occupancy

- **作者**: Yuan Wu, Zhiqiang Yan, Jiawei Lian, Zhengxue Wang, Jian Yang
- **发布日期**: 2026-05-06
- **链接**: [arXiv:2605.05072v1](https://arxiv.org/abs/2605.05072v1) | [PDF](https://arxiv.org/pdf/2605.05072v1)
- **分类**: cs.CV
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/Rayn-Wu/HiPR.) ⭐ 0

### 摘要

3D occupancy prediction aims to infer dense, voxel-wise scene semantics from sensor observations, where the 2D-to-3D view transformation serves as a crucial step in bridging image features and volumetric representations.

Most previous methods rely on a fixed projection space, where 3D reference points are uniformly sampled along pillars.

However, such sampling struggles to capture the sparsity and height variations of real-world scenes, leading to ambiguous correspondences and unreliable feature aggregation.

To address these challenges, we propose HiPR, a camera-LiDAR occupancy framework with 

### AI 总结

总结生成失败

---

## 3. When Life Gives You BC, Make Q-functions: Extracting Q-values from Behavior Cloning for On-Robot Reinforcement Learning

- **作者**: Lakshita Dodeja, Ondrej Biza, Shivam Vats, Stephen Hart, Stefanie Tellex
- **发布日期**: 2026-05-06
- **链接**: [arXiv:2605.05172v1](https://arxiv.org/abs/2605.05172v1) | [PDF](https://arxiv.org/pdf/2605.05172v1)
- **分类**: cs.RO, cs.AI
- **含金量**: 20/43 分

### 摘要

Behavior Cloning (BC) has emerged as a highly effective paradigm for robot learning.

However, BC lacks a self-guided mechanism for online improvement after demonstrations have been collected.

Existing offline-to-online learning methods often cause policies to replace previously learned good actions due to a distribution mismatch between offline data and online learning.

In this work, we propose Q2RL, Q-Estimation and Q-Gating from BC for Reinforcement Learning, an algorithm for efficient offline-to-online learning.

Our method consists of two parts: (1) Q-Estimation extracts a Q-function from a

### AI 总结

总结生成失败

---

## 4. Adaptive Learning Strategies for AoA-Based Outdoor Localization: A Comprehensive Framework

- **作者**: Bac Trinh-Nguyen, Sara Berri, Sin G. Teo, Tram Truong-Huu, Arsenia Chorti
- **发布日期**: 2026-05-06
- **链接**: [arXiv:2605.05055v1](https://arxiv.org/abs/2605.05055v1) | [PDF](https://arxiv.org/pdf/2605.05055v1)
- **分类**: cs.LG, cs.AI, eess.SP
- **含金量**: 20/43 分

### 摘要

Localization in 5G and 6G networks is essential for important use cases such as intelligent transportation, smart factories, and smart cities.

Although deep learning has enabled improving localization accuracy, depending on the deployment scenario and the effort required for dataset collection campaigns on a given infrastructure, the training process for localization models can vary significantly.

Furthermore, with respect to feature selection, recent works have demonstrated the robustness of angle-of-arrival (AoA) based localization.

In view of these two points, we propose an adaptive framewo

### AI 总结

总结生成失败

---

## 5. Online Nonstochastic Prediction: Logarithmic Regret via Predictive Online Least Squares

- **作者**: Chih-Fan Pai, Yang Zheng
- **发布日期**: 2026-05-06
- **链接**: [arXiv:2605.04364v1](https://arxiv.org/abs/2605.04364v1) | [PDF](https://arxiv.org/pdf/2605.04364v1)
- **分类**: cs.LG, eess.SY, math.OC
- **含金量**: 20/43 分

### 摘要

We study online prediction for marginally stable, partially observed linear dynamical systems under nonstochastic disturbances.

Our objective is to minimize the cumulative squared prediction loss and compete with the best-in-hindsight Luenberger predictor.

Standard online learning methods typically rely on bounded domains/gradients, and thus their guarantees may fail to deal with potentially unbounded trajectories in marginally stable systems.

In this paper, we introduce an unconstrained online least squares method that stabilizes the learning process via tailored predictive hints.

With model 

### AI 总结

总结生成失败

---

## 6. Topology-Aware Two-Stage Federated Learning via Proxy Models for Sub-THz Heterogeneous LEO Communications

- **作者**: Jinhao Yi, Weijun Gao, Chong Han, Ozgur Gurbuz, Josep M. Jornet
- **发布日期**: 2026-05-06
- **链接**: [arXiv:2605.04512v1](https://arxiv.org/abs/2605.04512v1) | [PDF](https://arxiv.org/pdf/2605.04512v1)
- **分类**: eess.SP
- **含金量**: 20/43 分

### 摘要

Federated learning (FL) has emerged as a promising distributed training paradigm for Low Earth Orbit (LEO) networks by significantly reducing communication overhead.

However, its deployment faces critical challenges, e.g., topology-induced model staleness, short contact windows, and unaddressed computing heterogeneity.

To address these issues, a topology-aware two-stage FL framework is proposed in this paper.

First, a multi-layer physical architecture utilizing high-altitude platforms (HAPs) and Sub-THz communications is designed to extend satellite-ground contact windows and enlarge available

### AI 总结

总结生成失败

---

## 7. CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training

- **作者**: Yida Gu, Fakang Wang, Jianhao Fu, Zhenhang Sun, Qianyu Zhang
- **发布日期**: 2026-05-06
- **链接**: [arXiv:2605.04478v1](https://arxiv.org/abs/2605.04478v1) | [PDF](https://arxiv.org/pdf/2605.04478v1)
- **分类**: cs.DC, cs.AI
- **含金量**: 20/43 分

### 摘要

As training scales grow, collective communication libraries (CCL) increasingly face anomalies arising from complex interactions among hardware, software, and environmental factors.

These anomalies typically manifest as slow/hang communication, the most frequent and time-consuming category to diagnose.

However, traditional diagnostic methods remain inaccurate and inefficient, frequently requiring hours or even days for root cause analysis.

To address this, we propose CCL-D, a high-precision diagnostic system designed to detect and locate slow/hang anomalies in large-scale distributed training.



### AI 总结

总结生成失败

---

## 8. FASQ: Flexible Accelerated Subspace Quantization for Calibration-Free LLM Compression

- **作者**: Ye Qiao, Yian Wang, Zhiheng Chen, Hyoukjun Kwon, Sitao Huang
- **发布日期**: 2026-04-22
- **链接**: [arXiv:2605.04084v1](https://arxiv.org/abs/2605.04084v1) | [PDF](https://arxiv.org/pdf/2605.04084v1)
- **分类**: cs.LG, cs.AI, cs.AR
- **含金量**: 20/43 分

### 摘要

Compressing large language models (LLMs) for deployment on commodity GPUs remains challenging: conventional scalar quantization is limited to fixed bit-widths (e.g., 8/4/3-bit), offers only a few discrete compression points, and typically requires calibration data.

We present FASQ (Flexible Accelerated Subspace Quantization), a calibration-free framework that applies product quantization to LLM weight matrices.

By tuning two parameters, sub-vector size and codebook cardinality, FASQ exposes a continuous design space spanning 27-49% of the original FP16 model size, filling compression gaps that

### AI 总结

总结生成失败

---

