# 大数据+AI 领域论文日报

**日期**: 2026-05-19

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [SGSoft: Learning Fused Semantic-Geo...](https://arxiv.org/abs/2605.18039v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Estimating Item Difficulty with Lar...](https://arxiv.org/abs/2605.18562v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Spiker-LL: An Energy-Efficient FPGA...](https://arxiv.org/abs/2605.18003v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [JanusPipe: Efficient Pipeline Paral...](https://arxiv.org/abs/2605.18404v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Going Beyond the Edge: Distributed ...](https://arxiv.org/abs/2605.15694v2) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Computational Challenges in Token E...](https://arxiv.org/abs/2605.17410v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [On the Complexity of Correlated Equ...](https://arxiv.org/abs/2605.17665v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [DepthPolyp: Pseudo-Depth Guided Lig...](https://arxiv.org/abs/2605.16519v1) | 待分析 | 评估失败 | [*1](https://github.com/ReaganWu/DepthPolyp) | 20/43 |
| 9 | [HPC-LLM: Practical Domain Adaptatio...](https://arxiv.org/abs/2605.16347v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Orth-Dion: Eliminating Geometric Mi...](https://arxiv.org/abs/2605.16341v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. SGSoft: Learning Fused Semantic-Geometric Features for 3D Shape Correspondence via Template-Guided Soft Signals

- **作者**: Soyeon Yoon, Chang Wook Seo, Hyunjung Shim
- **发布日期**: 2026-05-18
- **链接**: [arXiv:2605.18039v1](https://arxiv.org/abs/2605.18039v1) | [PDF](https://arxiv.org/pdf/2605.18039v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

Learning dense correspondences across deformable 3D shapes remains a long-standing challenge due to structural variability, non-isometric deformation, and inconsistent topology.

Existing methods typically trade off generalization, geometric fidelity, and efficiency.

We address this by proposing SGSoft, a unified intrinsic pipeline that (i) constructs a geodesic correspondence field on a canonical template, (ii) learns multimodal dense descriptors guided by pretrained semantic priors with this geodesic correspondence field supervision, (iii) retrieves dense correspondences in a single feed-forw

### AI 总结

总结生成失败

---

## 2. Estimating Item Difficulty with Large Language Models as Experts

- **作者**: Diana Kolesnikova, Kirill Fedyanin, Abe D. Hofman, Matthieu J. S. Brinkhuis, Maria Bolsinova
- **发布日期**: 2026-05-18
- **链接**: [arXiv:2605.18562v1](https://arxiv.org/abs/2605.18562v1) | [PDF](https://arxiv.org/pdf/2605.18562v1)
- **分类**: stat.ME, cs.AI, cs.LG, stat.AP
- **含金量**: 20/43 分

### 摘要

Accurate estimates of item difficulty are essential for valid assessment and effective adaptive learning.

However, for newly created tasks, response data are typically unavailable.

Pretesting and expert judgement can be costly and slow, while machine learning methods often require large labelled training datasets.

Recent work suggests that large language models (LLMs) may help.

However, there is limited evidence on the elicitation procedures and prompt configurations used to emulate experts for difficulty estimation.

This study addresses this gap by evaluating three off-the-shelf LLMs as diffi

### AI 总结

总结生成失败

---

## 3. Spiker-LL: An Energy-Efficient FPGA Accelerator Enabling Adaptive Local Learning in Spiking Neural Networks

- **作者**: Alessio Caviglia, Filippo Marostica, Alessandro Savino, Stefano Di Carlo
- **发布日期**: 2026-05-18
- **链接**: [arXiv:2605.18003v1](https://arxiv.org/abs/2605.18003v1) | [PDF](https://arxiv.org/pdf/2605.18003v1)
- **分类**: cs.NE, cs.AI
- **含金量**: 20/43 分

### 摘要

Deploying adaptive intelligence at the edge remains challenging due to the high computational and energy cost of training neural models.

Spiking Neural Networks (SNNs) offer a promising alternative, but enabling on-device learning requires hardware-algorithm co-design.

This paper presents SPIKER-LL, an FPGA-based SNN accelerator that extends the open-source Spiker+ inference architecture with efficient support for the STSF local learning rule.

Through targeted microarchitectural extensions, SPIKER-LL performs inference and online learning with minimal overhead.

Across MNIST, F-MNIST, and DIGIT

### AI 总结

总结生成失败

---

## 4. JanusPipe: Efficient Pipeline Parallel Training for Machine Learning Interatomic Potentials

- **作者**: Hongyu Wang, Weijian Liu, Hongtao Xu, Yan Wang, Mingzhen Li
- **发布日期**: 2026-05-18
- **链接**: [arXiv:2605.18404v1](https://arxiv.org/abs/2605.18404v1) | [PDF](https://arxiv.org/pdf/2605.18404v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Discovering atom-level phenomena requires molecular dynamics (MD) simulations with ab initio accuracy.

Machine learning interatomic potentials (MLIPs) enable stable, high-accuracy MD simulations, and their models exhibit scaling-law trends similar to large language models.

However, the lack of scalable and efficient distributed training systems for conservative MLIPs makes them difficult to scale.

This is because conservative MLIPs inherently follow a double-backward execution pattern, which involves computing gradients during the forward pass.

This pattern creates a mismatch with existing dis

### AI 总结

总结生成失败

---

## 5. Going Beyond the Edge: Distributed Inference of Transformer Models on Ultra-Low-Power Wireless Devices

- **作者**: Alexander Gräfe, Ding Huo, Vincent de Bakker, Johannes Berger, Marco Zimmerling
- **发布日期**: 2026-05-15
- **链接**: [arXiv:2605.15694v2](https://arxiv.org/abs/2605.15694v2) | [PDF](https://arxiv.org/pdf/2605.15694v2)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Transformer models are rapidly becoming a cornerstone of modern Internet of Things (IoT) applications, yet their computational and memory demands far exceed the capabilities of a single typical ultra-low-power IoT device.

We present CATS, a framework for distributed transformer inference on ultra-low-power wireless devices, enabling multiple devices to collaboratively execute models far larger than what a single device can sustain.

At its core, CATS is a communication-aware distributed transformer inference scheme co-designed across transformer partitioning, wireless communication and training

### AI 总结

总结生成失败

---

## 6. Computational Challenges in Token Economics: Bridging Economic Theory and AI System Design

- **作者**: Ou Wu, Yingjun Deng
- **发布日期**: 2026-05-17
- **链接**: [arXiv:2605.17410v1](https://arxiv.org/abs/2605.17410v1) | [PDF](https://arxiv.org/pdf/2605.17410v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

Token economics has emerged as a useful lens for understanding resource allocation, value creation, and pricing in large language model systems.

While recent work has increasingly treated tokens as economic primitives, there remains a substantial gap between high-level economic theory and the computational realities of modern AI infrastructure.

This paper identifies and analyzes the key computational challenges that arise when token-economic principles are implemented in real-time inference systems.

We argue that computational feasibility is not merely one dimension of token economics, but its

### AI 总结

总结生成失败

---

## 7. On the Complexity of Correlated Equilibria Beyond Normal-Form Games

- **作者**: Ioannis Anagnostides, Constantinos Daskalakis, Gabriele Farina, Noah Golowich, Tuomas Sandholm
- **发布日期**: 2026-05-17
- **链接**: [arXiv:2605.17665v1](https://arxiv.org/abs/2605.17665v1) | [PDF](https://arxiv.org/pdf/2605.17665v1)
- **分类**: cs.GT
- **含金量**: 20/43 分

### 摘要

Correlated equilibria are a fundamental solution concept in game theory.

However, despite decades of research, the complexity beyond games of polynomial type -- such as extensive-form games, congestion or routing games, and more broadly concave games -- has remained a major open problem, first highlighted by Papadimitriou and Roughgarden (JACM '08).

In this paper, we resolve several long-standing questions concerning the complexity of correlated equilibria and swap regret minimization.

First, we show that computing a correlated equilibrium in concave quadratic games is as hard as computing t

### AI 总结

总结生成失败

---

## 8. DepthPolyp: Pseudo-Depth Guided Lightweight Segmentation for Real-Time Colonoscopy

- **作者**: Zhuoyu Wu, Wenhui Ou, Lexi Zhang, Pei-Sze Tan, Dongjun Wu
- **发布日期**: 2026-05-15
- **链接**: [arXiv:2605.16519v1](https://arxiv.org/abs/2605.16519v1) | [PDF](https://arxiv.org/pdf/2605.16519v1)
- **分类**: cs.CV, eess.SP
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/ReaganWu/DepthPolyp) ⭐ 1 (Python)

### 摘要

Accurate polyp segmentation in colonoscopy is essential for early colorectal cancer detection, yet real-world clinical environments pose persistent challenges such as motion blur, specular reflections, and illumination instability.

Most existing methods are optimized on clean benchmark images and suffer noticeable performance degradation when deployed in authentic surgical scenarios.

We propose DepthPolyp, a lightweight and robust segmentation framework based on pseudo-depth-guided multi-task learning and efficient feature modulation.

The architecture combines hierarchical Ghost factorization 

### AI 总结

总结生成失败

---

## 9. HPC-LLM: Practical Domain Adaptation and Retrieval-Augmented Generation for HPC Support

- **作者**: Nourin Shahin, Izzat Alsmadi
- **发布日期**: 2026-05-08
- **链接**: [arXiv:2605.16347v1](https://arxiv.org/abs/2605.16347v1) | [PDF](https://arxiv.org/pdf/2605.16347v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Modern scientific research increasingly depends on High-Performance Computing (HPC) infrastructures, yet many researchers face significant operational barriers when interacting with cluster environments, job schedulers, GPU resources, and parallel computing frameworks.

General-purpose large language models (LLMs) provide useful coding assistance but often lack the domain-specific operational knowledge required for reliable HPC support.

This paper presents HPC-LLM, a retrieval augmented and domain-adapted assistant designed to support common HPC workflows including Slurm scheduling, MPI executi

### AI 总结

总结生成失败

---

## 10. Orth-Dion: Eliminating Geometric Mismatch in Distributed Low-Rank Spectral Optimization

- **作者**: Tatsuhiro Nakamori, Laura Gomezjurado Gonzalez, Ganesh Talluri, Ansh Tiwari, Hideyuki Kawashima
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.16341v1](https://arxiv.org/abs/2605.16341v1) | [PDF](https://arxiv.org/pdf/2605.16341v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Low-rank gradient compression reduces communication in distributed training by representing updates with rank-$r$ factors.

Dion is a recent method that approximates Muon, a spectral optimizer that orthogonalizes momentum, using one step of power iteration followed by column normalization (rescaling each column of the right factor to unit length).

This makes it compatible with fully sharded data parallel training, but it converges more slowly than full-rank spectral methods.

We show that this gap is geometric: column normalization does not yield the rank-$r$ polar factor that Muon implicitly ta

### AI 总结

总结生成失败

---

