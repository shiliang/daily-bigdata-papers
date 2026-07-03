# 大数据+AI 领域论文日报

**日期**: 2026-07-03

**论文数量**: 8 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Unlocking Speech-Text Compositional...](https://arxiv.org/abs/2607.02214v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [SCAPE: Accurate and Efficient LLM T...](https://arxiv.org/abs/2607.01678v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [DeadPool: Resilient LLM Training wi...](https://arxiv.org/abs/2607.01646v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [LMPAN: A Lightweight Multi-Path Ali...](https://arxiv.org/abs/2607.02062v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Dendritic In-Context Learning in a ...](https://arxiv.org/abs/2607.02283v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [A Memory Efficient Unified Algorith...](https://arxiv.org/abs/2607.02050v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Single-Channel EEG-Based Cognitive ...](https://arxiv.org/abs/2607.01795v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [The Rising Unsustainability of AI G...](https://arxiv.org/abs/2607.01258v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Unlocking Speech-Text Compositional Powers: Instruction-Following Speech Language Models without Instruction Tuning

- **作者**: Congrui Du, Yang Zhang, Kaizhi Qian, Shiyu Chang
- **发布日期**: 2026-07-02
- **链接**: [arXiv:2607.02214v1](https://arxiv.org/abs/2607.02214v1) | [PDF](https://arxiv.org/pdf/2607.02214v1)
- **分类**: cs.CL, eess.AS
- **含金量**: 20/43 分

### 摘要

Instruction tuning for speech language models (SLMs) is substantially more challenging than for text-based large language models (LLMs), as it requires learning a new modality and a wide range of speech-specific instructions in addition to those supported by text LLMs.

Existing SLM training approaches largely replicate the text LLM training paradigm by synthesizing large-scale speech pre-training and instruction-tuning datasets.

However, this strategy is difficult to scale, since speech sequences are significantly longer than text sequences.

In this paper, we propose SpeechCombine, an instruct

### AI 总结

总结生成失败

---

## 2. SCAPE: Accurate and Efficient LLM Training with Extreme Sparse Communication

- **作者**: Mingkai Zheng, Junlin Chen, Haotian Xie, Zhao Zhang
- **发布日期**: 2026-07-02
- **链接**: [arXiv:2607.01678v1](https://arxiv.org/abs/2607.01678v1) | [PDF](https://arxiv.org/pdf/2607.01678v1)
- **分类**: cs.LG, cs.DC
- **含金量**: 20/43 分

### 摘要

Communication increasingly dominates the cost of Large Language Model (LLM) pre-training, especially under data-parallel and sharded training schemes, where gradient synchronization and parameter reconstruction overhead increase with model size and system scale.

Existing communication-reduction methods either sparsify raw gradients, which can be unstable for modern Adam-style optimizers at high sparsity, or quantize communication, whose savings are fundamentally bounded by bit width and often incur additional runtime overhead.

We present SCAPE, a communication-efficient distributed optimizer f

### AI 总结

总结生成失败

---

## 3. DeadPool: Resilient LLM Training with Hot-Swapping via Zero-Overhead Checkpoint

- **作者**: Haotian Xie, Junlin Chen, Mingkai Zheng, Lishan Yang, Zhao Zhang
- **发布日期**: 2026-07-02
- **链接**: [arXiv:2607.01646v1](https://arxiv.org/abs/2607.01646v1) | [PDF](https://arxiv.org/pdf/2607.01646v1)
- **分类**: cs.LG, cs.DC
- **含金量**: 20/43 分

### 摘要

State-of-the-art large language model (LLM) training takes tens of thousands of graphics processing units (GPUs) for months and encounters failures across the software and hardware stack.

Existing fault-tolerance mechanisms either impose non-trivial overhead during failure-free execution or suffer from prolonged recovery latency, particularly under scenarios where a small subset of compute nodes experience permanent failures.

%The tradeoff between failure-free overhead and recovery latency forms a space forms a Pareto frontier We present DeadPool to simultaneously address both optimization obj

### AI 总结

总结生成失败

---

## 4. LMPAN: A Lightweight Multi-Path Alignment Network for Joint Full-Duplex Acoustic Echo Cancellation and Noise Suppression

- **作者**: Chengwei Liu, Shaofei Xue, Haoyin Yan, Xiaotao Liang, Zheng Xue
- **发布日期**: 2026-07-02
- **链接**: [arXiv:2607.02062v1](https://arxiv.org/abs/2607.02062v1) | [PDF](https://arxiv.org/pdf/2607.02062v1)
- **分类**: eess.AS
- **含金量**: 20/43 分

### 摘要

We propose a lightweight multi-path alignment network (LMPAN) for on-device joint acoustic echo cancellation (AEC) and noise suppression (NS) in full-duplex spoken dialogue systems.

To address hardware-induced distortions and dynamic acoustic conditions, we introduce three core innovations: (1) a multi-path alignment stage correcting temporal and energy mismatches across reference, linear AEC (LAEC) output, and microphone signals; (2) an attention-based mechanism that dynamically integrates enhanced LAEC and microphone features under varying acoustic scenarios; (3) a post-filtering module with

### AI 总结

总结生成失败

---

## 5. Dendritic In-Context Learning in a Single-Layer Spiking Neural Network

- **作者**: Juwei Shen, Yujie Wu, Changwen Chen
- **发布日期**: 2026-07-02
- **链接**: [arXiv:2607.02283v1](https://arxiv.org/abs/2607.02283v1) | [PDF](https://arxiv.org/pdf/2607.02283v1)
- **分类**: cs.NE, cs.LG
- **含金量**: 20/43 分

### 摘要

In-context learning (ICL) operates via implicit gradient descent embedded in the forward pass of modern AI architectures -- Transformers, Mamba, state-space models, and MLPs.

Capturing this capability in biologically plausible Spiking Neural Networks (SNNs) has remained an open challenge: existing SNNs fail the Garg-2022 benchmark at non-trivial task dimensions.

We trace this failure to a structural assumption: prior SNN designs route adaptation through inference-time synaptic plasticity, viewing the dendritic compartment as a passive conduit for error or teacher signals.

We challenge this ass

### AI 总结

总结生成失败

---

## 6. A Memory Efficient Unified Algorithm for Online Learning of Linear Dynamical Systems

- **作者**: Yuval Ran-Milo, Angelos Assos, Elad Hazan
- **发布日期**: 2026-07-02
- **链接**: [arXiv:2607.02050v1](https://arxiv.org/abs/2607.02050v1) | [PDF](https://arxiv.org/pdf/2607.02050v1)
- **分类**: cs.LG, eess.SY
- **含金量**: 20/43 分

### 摘要

Motivated by the challenge of stabilizing a general unknown linear dynamical system (LDS) from observations, we study the natural prerequisite of online prediction.

Our goal is to achieve sublinear regret with a memory footprint that adapts to the intrinsic complexity of the dynamics rather than the full hidden -- state dimension.

We focus on the practically central regime of systems with low instability complexity -- eigenvalues outside the real stable interval that do not decay rapidly, together with non-semisimple modes-potentially embedded in an otherwise stable real spectrum of much highe

### AI 总结

总结生成失败

---

## 7. Single-Channel EEG-Based Cognitive Load Assessment in Online Learning: A Hybrid Deep Learning Approach

- **作者**: Rowan Hussein, Mohamed Ouf
- **发布日期**: 2026-07-02
- **链接**: [arXiv:2607.01795v1](https://arxiv.org/abs/2607.01795v1) | [PDF](https://arxiv.org/pdf/2607.01795v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

Monitoring cognitive load during online learning could help instructors identify content that learners find difficult, but remote settings remove the visual cues that support this judgement in a classroom.

We study whether a single-channel, consumer-grade EEG device (the NeuroSky MindWave Mobile 2) can distinguish easy from difficult educational-video content, using the publicly available dataset of Wang et al.

[24] (ten learners, one excluded for excessive noise, leaving nine).

We implement a hybrid CNN+LSTM+Attention model that combines the raw waveform with band-power features.

In a within-

### AI 总结

总结生成失败

---

## 8. The Rising Unsustainability of AI Graphics Cards Production

- **作者**: Clément Morand, Aurélie Névéol, Anne-Laure Ligozat
- **发布日期**: 2026-06-05
- **链接**: [arXiv:2607.01258v1](https://arxiv.org/abs/2607.01258v1) | [PDF](https://arxiv.org/pdf/2607.01258v1)
- **分类**: cs.CY, cs.AI
- **含金量**: 20/43 分

### 摘要

The rapid advancement of Artificial Intelligence (AI) has been accompanied by significant increases in computational and environmental costs, driven by large-scale investments in AI infrastructure, hardware, and software.

In particular, graphics cards have become central to AI training, with frequent hardware updates required to meet escalating computational demands.

However, the environmental damages of graphics cards production remain understudied.

This study addresses this gap by estimating the environmental damages associated with graphics cards production over the past decade (2013-2025

### AI 总结

总结生成失败

---

