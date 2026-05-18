# 大数据+AI 领域论文日报

**日期**: 2026-05-18

**论文数量**: 7 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Runtime-Orchestrated Second-Order O...](https://arxiv.org/abs/2605.16184v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [DeltaPrompts: Escaping the Zero-Del...](https://arxiv.org/abs/2605.15532v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [On the Fragility of Data Attributio...](https://arxiv.org/abs/2605.15520v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [BatchWeave: A Consistent Object-Sto...](https://arxiv.org/abs/2605.09994v2) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Controlling Transient Amplification...](https://arxiv.org/abs/2605.08856v2) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Going Beyond the Edge: Distributed ...](https://arxiv.org/abs/2605.15694v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Tadpole: Autoencoders as Foundation...](https://arxiv.org/abs/2605.15284v1) | 待分析 | 评估失败 | [Code](https://github.com/tum-pbs/tadpole) | 20/43 |

---


## 1. Runtime-Orchestrated Second-Order Optimization for Scalable LLM Training

- **作者**: Yishun Lu, Junhao Zhang, Zeyu Yang, Wes Armour
- **发布日期**: 2026-05-15
- **链接**: [arXiv:2605.16184v1](https://arxiv.org/abs/2605.16184v1) | [PDF](https://arxiv.org/pdf/2605.16184v1)
- **分类**: cs.DC, cs.LG
- **含金量**: 20/43 分

### 摘要

Second-order methods offer an attractive path toward more sample-efficient LLM training, but their practical use is often blocked by the systems cost of maintaining and updating large matrix-based optimizer states.

We introduce \textbf{Asteria}, a runtime system designed to remove this bottleneck by separating second-order optimization logic from the critical GPU training path.

Rather than keeping all preconditioner state on the accelerator, Asteria dynamically distributes optimizer state across GPU memory, CPU memory, and optional NVMe storage according to architectural constraints and runtim

### AI 总结

总结生成失败

---

## 2. DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation

- **作者**: Jaehun Jung, Hyunwoo Kim, Brandon Cui, Ximing Lu, David Acuna
- **发布日期**: 2026-05-15
- **链接**: [arXiv:2605.15532v1](https://arxiv.org/abs/2605.15532v1) | [PDF](https://arxiv.org/pdf/2605.15532v1)
- **分类**: cs.LG, cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

Distillation enables compact Vision-Language Models (VLMs) to obtain strong reasoning capabilities, yet the prompts driving this process are typically chosen via simple heuristics or aggregated from off-the-shelf datasets.

We reveal a critical inefficiency in this approach: up to 69% of the prompts in standard chart / document reasoning datasets are effectively zero-delta, meaning the teacher and student already induce the exact same answer distribution.

Training on these prompts provides minimal learning signal, causing student improvement to rapidly saturate regardless of data scale.

To esca

### AI 总结

总结生成失败

---

## 3. On the Fragility of Data Attribution When Learning Is Distributed

- **作者**: Xian Gao, Bo Hui, Min-Te Sun, Wei-Shinn Ku
- **发布日期**: 2026-05-15
- **链接**: [arXiv:2605.15520v1](https://arxiv.org/abs/2605.15520v1) | [PDF](https://arxiv.org/pdf/2605.15520v1)
- **分类**: cs.LG, cs.AI, cs.DC
- **含金量**: 20/43 分

### 摘要

Data attribution has become an important component of pricing, auditing, and governance in machine learning pipelines, yet most attribution methods implicitly assume that attribution values faithfully reflect participants' contributions.

We show that this assumption can fail: a single participant in a standard distributed training workflow can substantially inflate its measured attribution value while preserving global utility.

Our attribution-first attack uses latent optimization to inject small synthetic batches that preserve utility while exploiting non-IID label coverage and evaluator sens

### AI 总结

总结生成失败

---

## 4. BatchWeave: A Consistent Object-Store-Native Data Plane for Large Foundation Model Training

- **作者**: Ting Sun, Junjie Zhang, Xiao Yan, Songxin Zhang, Zhuoyang Song
- **发布日期**: 2026-05-11
- **链接**: [arXiv:2605.09994v2](https://arxiv.org/abs/2605.09994v2) | [PDF](https://arxiv.org/pdf/2605.09994v2)
- **分类**: cs.DC, cs.LG
- **含金量**: 20/43 分

### 摘要

Modern Large Foundation Model (LFM) training has transformed the data pipeline from a static ingestion layer into a dynamic component that must co-evolve with the training process.

Existing systems are ill-equipped: colocated dataloaders offer no failure isolation, while message queue-based disaggregated dataloaders operate on a record/offset abstraction that cannot express the batch-level semantics required by distributed training.

We present BatchWeave, an object-store-native training data plane for distributed LFM training.

BatchWeave uses versioned manifests and conditional object writes t

### AI 总结

总结生成失败

---

## 5. Controlling Transient Amplification Improves Long-horizon Rollouts

- **作者**: Adeel Pervez, Francesco Locatello
- **发布日期**: 2026-05-09
- **链接**: [arXiv:2605.08856v2](https://arxiv.org/abs/2605.08856v2) | [PDF](https://arxiv.org/pdf/2605.08856v2)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Autoregressive neural simulators now match classical solvers on short-horizon prediction of physical systems, yet their accuracy degrades rapidly when rolled out over long horizons.

In this work, we identify transient amplification of perturbations around rollout trajectories as a structural mechanism driving rollout error.

Using a linearization analysis we show that when the Jacobians along an autoregressive trajectory are non-normal and non-commuting, the model amplifies errors transiently, resulting in model rollout drift even when the overall system is asymptotically stable.

Building on th

### AI 总结

总结生成失败

---

## 6. Going Beyond the Edge: Distributed Inference of Transformer Models on Ultra-Low-Power Wireless Devices

- **作者**: Alexander Gräfe, Ding Huo, Johannes Berger, Marco Zimmerling, Sebastian Trimpe
- **发布日期**: 2026-05-15
- **链接**: [arXiv:2605.15694v1](https://arxiv.org/abs/2605.15694v1) | [PDF](https://arxiv.org/pdf/2605.15694v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Transformer models are rapidly becoming a cornerstone of modern Internet of Things (IoT) applications, yet their computational and memory demands far exceed the capabilities of a single typical ultra-low-power IoT device.

We present CATS, a framework for distributed transformer inference on ultra-low-power wireless devices, enabling multiple devices to collaboratively execute models far larger than what a single device can sustain.

At its core, CATS is a communication-aware distributed transformer inference scheme co-designed across transformer partitioning, wireless communication and training

### AI 总结

总结生成失败

---

## 7. Tadpole: Autoencoders as Foundation Models for 3D PDEs with Online Learning

- **作者**: Qiang Liu, Felix Koehler, Benjamin Holzschuh, Nils Thuerey
- **发布日期**: 2026-05-14
- **链接**: [arXiv:2605.15284v1](https://arxiv.org/abs/2605.15284v1) | [PDF](https://arxiv.org/pdf/2605.15284v1)
- **分类**: cs.LG
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/tum-pbs/tadpole) ⭐ 0

### 摘要

We introduce Tadpole, a novel foundation model for three-dimensional partial differential equations (PDEs) that addresses key challenges in transferability, scalability to high dimensionality, and multi-functionality.

Tadpole is pre-trained as an autoencoder on synthetic 3D PDE data generated by an efficient online data-generation framework.

This enables large-scale, diverse training without storage or I/O overhead, demonstrated by scaling to an equivalent of hundreds of terabytes of training data.

By autoencoding single-channel spatial crops, Tadpole learns rich and transferable representatio

### AI 总结

总结生成失败

---

