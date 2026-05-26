# 大数据+AI 领域论文日报

**日期**: 2026-05-26

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [PowLU: An Activation Function for S...](https://arxiv.org/abs/2605.25704v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [How Should LLMs Consume High-Qualit...](https://arxiv.org/abs/2605.25698v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [BigMac: Breaking the Pareto Frontie...](https://arxiv.org/abs/2605.25451v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Bandwidth-Aware and Cost-Efficient ...](https://arxiv.org/abs/2605.25375v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [SAM3-Assisted Training of Lightweig...](https://arxiv.org/abs/2605.25860v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Bridging the Gap: Enabling Soft Act...](https://arxiv.org/abs/2605.24975v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [NEST: Network- and Memory-Aware Dev...](https://arxiv.org/abs/2603.06798v2) | 待分析 | 评估失败 | [*4](https://github.com/scai-tech/Nest) | 20/43 |
| 8 | [Summoning the Oracle to Slay It: Mi...](https://arxiv.org/abs/2605.24564v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Streaming Reinforcement Learning un...](https://arxiv.org/abs/2605.24709v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Batch Normalization Amplifies Memor...](https://arxiv.org/abs/2605.24420v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. PowLU: An Activation Function for Stable Pre-Training of LLMs

- **作者**: Peijie Jiang, Yuqi Feng, Cunyin Peng, Qian Zhao, Jia Liu
- **发布日期**: 2026-05-25
- **链接**: [arXiv:2605.25704v1](https://arxiv.org/abs/2605.25704v1) | [PDF](https://arxiv.org/pdf/2605.25704v1)
- **分类**: cs.CL, cs.LG
- **含金量**: 20/43 分

### 摘要

In contemporary large language models (LLMs), the swish-gated linear unit (SwiGLU) activation function is widely adopted to regulate the information flow and introduce non-linearity.

For large positive inputs, SwiGLU approximates the quadratic function $x^2$, providing strong nonlinearity and expressive capacity.

However, this property also causes numerical instability as the input or model scale increases, particularly in low-precision LLM training.

The main reason is its approximate quadratic amplification, which enlarges the output range and exacerbates outliers.

To address this issue, we p

### AI 总结

总结生成失败

---

## 2. How Should LLMs Consume High-Quality Data? Optimal Data Scheduling via Quality-Aware Functional Scaling Laws

- **作者**: Zhitao Zhu, Xili Wang, Shizhe Wu, Jiawei Fu, Xiaoqing Liu
- **发布日期**: 2026-05-25
- **链接**: [arXiv:2605.25698v1](https://arxiv.org/abs/2605.25698v1) | [PDF](https://arxiv.org/pdf/2605.25698v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

High-quality data is scarce in large language model (LLM) training, yet how to schedule its use jointly with training dynamics lacks theoretical guidance.

We extend functional scaling laws by incorporating a data-quality dimension, and solve the joint data-quality and batch-size scheduling problem in asymptotic closed form.

The solution reveals two regimes and a dual role of high-quality data.

In the noise-limited regime, high-quality data should be used as a signal amplifier: lowering the batch size converts cleaner data into more signal without amplifying noise.

In the signal-limited regime,

### AI 总结

总结生成失败

---

## 3. BigMac: Breaking the Pareto Frontier of Compute and Memory in Multimodal LLM Training

- **作者**: Zili Zhang, Chengxu Yang, Shenglong Zhang, Chenyu Wang, Yufan Zhang
- **发布日期**: 2026-05-25
- **链接**: [arXiv:2605.25451v1](https://arxiv.org/abs/2605.25451v1) | [PDF](https://arxiv.org/pdf/2605.25451v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Training multimodal large language models (MLLMs) is challenged by both model and data heterogeneity.

Existing systems redesign the training pipeline to address these challenges, but remain bound by a Pareto frontier between compute and memory efficiency, improving one only at the expense of the other.

We present BigMac, a new training pipeline for multimodal LLMs.

The core idea of BigMac is to elegantly nest the encoder and generator computation into the original LLM pipeline, forming a dependency-safe nested pipeline structure.

With this design, BigMac reduces the activation memory complexit

### AI 总结

总结生成失败

---

## 4. Bandwidth-Aware and Cost-Efficient Pipeline Parallel Scheduling in Geo-Distributed LLM Training

- **作者**: Han Zhang, Jianchun Liu, Hongli Xu
- **发布日期**: 2026-05-25
- **链接**: [arXiv:2605.25375v1](https://arxiv.org/abs/2605.25375v1) | [PDF](https://arxiv.org/pdf/2605.25375v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

The rapid evolution of large language models (LLMs) has made geographically distributed training necessary due to GPU scarcity within a single cloud region.

In such cross-region settings, Pipeline Parallelism (PP) is communication-efficient, yet scheduling PP remains challenging under heterogeneous inter-region bandwidth and regional electricity prices.

Existing schedulers are either delay-first, incurring high electricity cost, or cost-first, relying on rigid resource allocation that prolongs Job Completion Time (JCT).

They are also ineffective at optimizing execution order in multi-tenant en

### AI 总结

总结生成失败

---

## 5. SAM3-Assisted Training of Lightweight YOLO Models for Precision Pig Farming

- **作者**: Marcos Vinicius Mendes Faria, Thiago Borges Pereira, Isabella C. F. S. Condotta, Thiago Meireles Paixão, Francisco de Assis Boldt
- **发布日期**: 2026-05-25
- **链接**: [arXiv:2605.25860v1](https://arxiv.org/abs/2605.25860v1) | [PDF](https://arxiv.org/pdf/2605.25860v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

Deep learning-based object detection has revolutionized Precision Livestock Farming (PLF), yet a critical barrier remains: high-performance Foundation Models (such as SAM 3) are too computationally intensive for edge deployment, while lightweight models (like YOLO) require prohibitive manual annotation efforts.

This work proposes a fully automated knowledge distillation pipeline that leverages the Segment Anything Model 3 (SAM 3) to generate zero-shot pseudo-labels for training efficient YOLOv8 detectors.

By treating SAM 3 as an offline auto-annotator, we eliminate the manual labeling bottlene

### AI 总结

总结生成失败

---

## 6. Bridging the Gap: Enabling Soft Actor Critic for High Performance Legged Locomotion

- **作者**: Gianluca Sabatini, Chenhao Li, Marco Hutter
- **发布日期**: 2026-05-24
- **链接**: [arXiv:2605.24975v1](https://arxiv.org/abs/2605.24975v1) | [PDF](https://arxiv.org/pdf/2605.24975v1)
- **分类**: cs.RO, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

Proximal Policy Optimization (PPO) has become the de facto standard for training legged robots, thanks to its robustness and scalability in massively parallel simulation environments like IsaacLab.

However, its on-policy nature makes it inherently sample-inefficient, preventing its use for continuous adaptation and fine-tuning on real hardware.

Soft Actor-Critic (SAC), by contrast, is an off-policy algorithm that can reuse past experience, making it a natural candidate for sim-to-real transfer workflows where the same algorithm can be used both in simulation and for online learning on the real

### AI 总结

总结生成失败

---

## 7. NEST: Network- and Memory-Aware Device Placement For Distributed Deep Learning

- **作者**: Irene Wang, Vishnu Varma Venkata, Arvind Krishnamurthy, Divya Mahajan
- **发布日期**: 2026-03-06
- **链接**: [arXiv:2603.06798v2](https://arxiv.org/abs/2603.06798v2) | [PDF](https://arxiv.org/pdf/2603.06798v2)
- **分类**: cs.LG, cs.DC, stat.ML
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/scai-tech/Nest) ⭐ 4 (Python)

### 摘要

The growing scale of deep learning demands distributed training frameworks that jointly reason about parallelism, memory, and network topology.

Prior works often rely on heuristic or topology-agnostic search, handling communication and memory separately.

Without per-device memory awareness, these methods typically ensure feasibility post hoc by sharding parameters and activations across many devices, increasing synchronization, inflating communication, and underutilizing compute-limiting scalability and efficiency on real datacenter networks.

We present NEST, a network-, compute-, and memory-a

### AI 总结

总结生成失败

---

## 8. Summoning the Oracle to Slay It: Mitigating Look-Ahead Bias in Financial Backtesting with Large Language Models

- **作者**: Weixian Waylon Li, Mengyu Wang, Tiejun Ma
- **发布日期**: 2026-05-23
- **链接**: [arXiv:2605.24564v1](https://arxiv.org/abs/2605.24564v1) | [PDF](https://arxiv.org/pdf/2605.24564v1)
- **分类**: cs.AI, cs.CE, cs.LG
- **含金量**: 20/43 分

### 摘要

Backtesting large language models (LLMs) on historical financial data is unreliable because pre-training cuts off after the events happened.

An LLM trained in 2024 already "knows" which way 2018-2020 stocks moved.

We name this failure parametric look-ahead bias and propose FinCAD, an inference-time adaptation of Context-Aware Decoding that suppresses an LLM's memory of historical outcomes without retraining.

FinCAD pairs an adversarial bias-discovery pipeline that learns a model-specific memory-activating prior prompt with an entity- and date-adaptive rule that scales the CAD strength to per-(

### AI 总结

总结生成失败

---

## 9. Streaming Reinforcement Learning under Partial Observability with Real-Time Recurrent Learning

- **作者**: Noah Farr, Aryaman Reddi, Carlo D'Eramo, Jan Peters
- **发布日期**: 2026-05-23
- **链接**: [arXiv:2605.24709v1](https://arxiv.org/abs/2605.24709v1) | [PDF](https://arxiv.org/pdf/2605.24709v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Streaming reinforcement learning has emerged as an online learning paradigm that conforms to the restrictions of natural learning agents that process data incrementally, i.e.

with a batch size of 1 and no replay buffer.

While streaming RL has recently been shown to scale with deep function approximation with full observability, partially observable settings have remained out of reach.

Truncated backpropagation through time collapses to a one-step gradient horizon under the streaming setting, and exact real-time recurrent learning is prohibitively expensive.

We close this gap using recurrent tr

### AI 总结

总结生成失败

---

## 10. Batch Normalization Amplifies Memorization and Privacy Risks

- **作者**: Ngoc Phu Doan, Chongyan Gu, Ihsen Alouani
- **发布日期**: 2026-05-23
- **链接**: [arXiv:2605.24420v1](https://arxiv.org/abs/2605.24420v1) | [PDF](https://arxiv.org/pdf/2605.24420v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

Batch Normalization (BN) is widely adopted to enable faster convergence and more stable training of deep neural networks.

However, its impact on privacy and memorization has remained largely unexplored.

In this work, we investigate the effect of BN layers on the memorization of atypical or outlier samples and its implications for privacy leakage.

We conduct an extensive empirical study using three complementary approaches: (i) unintended memorization of out-of-distribution training samples, (ii) per-sample influence measured via gradient norms, and (iii) susceptibility to membership inference 

### AI 总结

总结生成失败

---

