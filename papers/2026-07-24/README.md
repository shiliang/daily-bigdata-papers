# 大数据+AI 领域论文日报

**日期**: 2026-07-24

**论文数量**: 8 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [VibeVoice-ASR-BitNet Technical Repo...](https://arxiv.org/abs/2607.21075v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [A Diffusion-Model Subpopulation Dig...](https://arxiv.org/abs/2607.21403v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Update the Unseen Only: Minimizing ...](https://arxiv.org/abs/2607.20967v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Controlled Periodic Synchronization...](https://arxiv.org/abs/2607.21224v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Demonstrating GenDB: Instance-Optim...](https://arxiv.org/abs/2607.20630v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [A Sovereign, Open-Source Foundation...](https://arxiv.org/abs/2607.09424v3) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [GaugeQuant: Online Learning of Quan...](https://arxiv.org/abs/2607.20757v1) | 待分析 | 评估失败 | [Code](https://github.com/MPedraBento/gauge-quant.) | 20/43 |
| 8 | [Pipelined Gradient Coding](https://arxiv.org/abs/2607.20739v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. VibeVoice-ASR-BitNet Technical Report

- **作者**: Songchen Xu, Ting Song, Shaohan Huang, Zhiliang Peng, Yan Xia
- **发布日期**: 2026-07-23
- **链接**: [arXiv:2607.21075v1](https://arxiv.org/abs/2607.21075v1) | [PDF](https://arxiv.org/pdf/2607.21075v1)
- **分类**: cs.SD, cs.CL, eess.AS
- **含金量**: 20/43 分

### 摘要

We present VibeVoice-ASR-BitNet, a compressed variant of VibeVoice-ASR optimized for real-time inference on edge CPUs.

We apply heterogeneous quantization tailored to the computational characteristics of each stage: the VAE acoustic tokenizer uses full-pipeline INT8 quantization (I8_S) with kernel fusion and SIMD optimization, while the autoregressive language model adopts BitNet-style ternary weights (I2_S).

To preserve accuracy under aggressive compression, we employ a progressive quantization-aware training strategy.

For inference, we implement custom SIMD kernels and fused operators within

### AI 总结

总结生成失败

---

## 2. A Diffusion-Model Subpopulation Digital Twin for Mobile Health Deployment: A Case Study on the HeartSteps Intervention

- **作者**: Ziping Xu, Yuyi Chang, Chenshun Ni, Nithin Sugavanam, Asim H. Gazi
- **发布日期**: 2026-07-23
- **链接**: [arXiv:2607.21403v1](https://arxiv.org/abs/2607.21403v1) | [PDF](https://arxiv.org/pdf/2607.21403v1)
- **分类**: cs.LG, stat.ME
- **含金量**: 20/43 分

### 摘要

Mobile-health interventions increasingly use online learning and decision making algorithms to personalize when to nudge users toward healthier behavior, but a poorly designed algorithm can burden and disengage participants.

New algorithm design decisions should therefore be vetted against realistic simulated users before each real-life deployment.

We propose a method to develop ``JITAI-Twins'': digital twins of a target subpopulation for comparing candidate online algorithms before a just-in-time adaptive intervention (JITAI) deployment.

The method builds on a conditional time-series diffusio

### AI 总结

总结生成失败

---

## 3. Update the Unseen Only: Minimizing AoI for Collaborative Perception through Online Learning

- **作者**: Yanan Ma, Zhuoyi Zhao, Zhengru Fang, Haonan An, Xianhao Chen
- **发布日期**: 2026-07-23
- **链接**: [arXiv:2607.20967v1](https://arxiv.org/abs/2607.20967v1) | [PDF](https://arxiv.org/pdf/2607.20967v1)
- **分类**: cs.NI
- **含金量**: 20/43 分

### 摘要

While collaborative perception (CP) enhances the safety of autonomous driving, limited bandwidth can cause severe shared data staleness in CP systems.

Existing age-of-information (AoI) minimization policies are not well-suited for CP, as they overlook the fact that a vehicle's AoI decreases not only through updates from the source (i.e., a base station) but also through the vehicle's local sensing.

To address this issue, we propose a mobility-aware AoI minimization framework for CP that explicitly accounts for vehicles' dynamic sensing ranges.

We first derive a closed-form expression for the l

### AI 总结

总结生成失败

---

## 4. Controlled Periodic Synchronization for Efficient Data-Parallel Training

- **作者**: Imane Ettifouri, Mostapha Zbakh, Claude Tadonki
- **发布日期**: 2026-07-23
- **链接**: [arXiv:2607.21224v1](https://arxiv.org/abs/2607.21224v1) | [PDF](https://arxiv.org/pdf/2607.21224v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Data-parallel training relies on frequent gradient synchronization across workers.

Standard DDP synchronizes gradients at every iteration, which is effective on fast local-area networks but increasingly sensitive to communication latency and network variability in geographically distributed environments.

Periodic methods such as LocalSGD reduce synchronization frequency but rely mainly on parameter averaging, which may be insufficient when worker trajectories diverge.

This paper studies synchronization frequency as a systems parameter for communication-constrained distributed training.

We eval

### AI 总结

总结生成失败

---

## 5. Demonstrating GenDB: Instance-Optimized and Customized Query Processing Code Generation via LLM Agents

- **作者**: Jiale Lao, Immanuel Trummer
- **发布日期**: 2026-07-22
- **链接**: [arXiv:2607.20630v1](https://arxiv.org/abs/2607.20630v1) | [PDF](https://arxiv.org/pdf/2607.20630v1)
- **分类**: cs.DB, cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

Traditional query processing engines require continuous development and extensions to support new techniques and user requirements, and in some cases, entirely new systems must be built from scratch.

However, these engines are difficult to extend due to their internal complexity, and building new systems demands significant engineering effort and cost.

To address this, we demonstrate GenDB, a generative query engine that shifts query processing from manually engineered systems to query processing code generation driven by Large Language Models (LLMs).

An early prototype of GenDB uses LLM agent

### AI 总结

总结生成失败

---

## 6. A Sovereign, Open-Source Foundation Model for German and English

- **作者**:  Soofi-Team,  :, Benedikt Droste, David Fitzek, Ruben Härle
- **发布日期**: 2026-07-10
- **链接**: [arXiv:2607.09424v3](https://arxiv.org/abs/2607.09424v3) | [PDF](https://arxiv.org/pdf/2607.09424v3)
- **分类**: cs.CL, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

We present Soofi S 30B-A3B, a sovereign, open-source Mixture-of-Experts (MoE) hybrid Mamba Transformer foundation model for German and English.

Its hybrid design activates only 3B of 30B parameters per token and keeps the inference cache near-constant as context grows, giving it a decisive throughput advantage over dense models for long-context, high-concurrency deployment.

Pretrained on roughly 27 trillion tokens with deliberately up-weighted German, Soofi S matches dense 14 to 27B models on aggregate English and German benchmarks while achieving the best code aggregates in both languages amo

### AI 总结

总结生成失败

---

## 7. GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries

- **作者**: Miguel P. Bento, João Seabra
- **发布日期**: 2026-07-22
- **链接**: [arXiv:2607.20757v1](https://arxiv.org/abs/2607.20757v1) | [PDF](https://arxiv.org/pdf/2607.20757v1)
- **分类**: cs.LG, cs.CL
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/MPedraBento/gauge-quant.) ⭐ 0

### 摘要

Transformers are known to have internal continuous symmetries that leave outputs invariant, while modifying quantization.

GaugeQuant leverages this in-training by introducing a LogSumExp term to the loss that breaks the symmetries, thus selecting a basis that minimizes activation outliers.

A stop-gradient operator ensures that only rotation matrices are updated, yielding the language modeling objective completely unaltered.

Our requires no specific calibration data, no quantization simulation, and adds negligible training overhead.

With the LLaMA-2 7B model under W4A4 quantization with group s

### AI 总结

总结生成失败

---

## 8. Pipelined Gradient Coding

- **作者**: Xian Su, Jun Li
- **发布日期**: 2026-07-22
- **链接**: [arXiv:2607.20739v1](https://arxiv.org/abs/2607.20739v1) | [PDF](https://arxiv.org/pdf/2607.20739v1)
- **分类**: cs.IT, cs.LG
- **含金量**: 20/43 分

### 摘要

In large-scale machine learning, distributed training commonly involves multiple workers evaluating the gradients of the model on different dataset partitions.

A common challenge is the presence of straggling workers, which may significantly slow down training.

Traditional gradient coding (GC) addresses this by duplicating dataset partitions across workers, allowing for the replacement of missing gradients from stragglers.

However, GC requires workers to evaluate gradients on multiple dataset partitions in each step, potentially increasing overall training time.

In this paper, we propose to pi

### AI 总结

总结生成失败

---

