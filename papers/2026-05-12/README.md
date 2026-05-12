# 大数据+AI 领域论文日报

**日期**: 2026-05-12

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Accelerating Compound LLM Training ...](https://arxiv.org/abs/2605.10501v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [ResiHP: Taming LLM Training Failure...](https://arxiv.org/abs/2605.06374v2) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Height-Guided Projection Reparamete...](https://arxiv.org/abs/2605.05072v2) | 待分析 | 评估失败 | [Code](https://github.com/yanzq95/HiPR.) | 20/43 |
| 4 | [AsymTalker: Identity-Consistent Lon...](https://arxiv.org/abs/2605.02948v3) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Online Sharp-Calibrated Bayesian Op...](https://arxiv.org/abs/2605.10572v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Fast Training of Mixture-of-Experts...](https://arxiv.org/abs/2605.10330v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Sample-Mean Anchored Thompson Sampl...](https://arxiv.org/abs/2605.10289v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Online Learning-Based Control with ...](https://arxiv.org/abs/2605.10152v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Continuous Latent Contexts Enable E...](https://arxiv.org/abs/2605.09867v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Filtering Memorization from Paramet...](https://arxiv.org/abs/2605.10439v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Accelerating Compound LLM Training Workloads with Maestro

- **作者**: Xiulong Yuan, Hongqing Chen, Jiaxuan Peng, Fan Zhou, Zhixiang Ruan
- **发布日期**: 2026-05-11
- **链接**: [arXiv:2605.10501v1](https://arxiv.org/abs/2605.10501v1) | [PDF](https://arxiv.org/pdf/2605.10501v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Compound LLM training workloads-such as knowledge distillation and multimodal LLM (MLLM) training-are gaining prominence.

These typically comprise heterogeneous components differing in parameter scale, execution mode (forward-only or full forward-backward), and sequence length.

Besides, component activation can be data-dependent: in MLLM training, modality-specific parts activate only when inputs contain corresponding modalities, causing dynamic computational paths and irregular runtime workloads.

Conventional frameworks, designed for monolithic models, cannot handle the dual heterogeneity-sta

### AI 总结

总结生成失败

---

## 2. ResiHP: Taming LLM Training Failures with Dynamic Hybrid Parallelism

- **作者**: Tenghui Ma, Jihu Guo, Wei Gao, Sitian Lu, Zhisheng Ye
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.06374v2](https://arxiv.org/abs/2605.06374v2) | [PDF](https://arxiv.org/pdf/2605.06374v2)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Hybrid parallelism underpins large-scale LLM training across tens of thousands of GPUs.

At such scale, hardware failures on individual devices lead to performance skew across devices, diminishing overall training efficiency.

Existing resilient systems overlook sequence length variability in datasets and device performance skew under hybrid parallelism.

As a result, (1) iteration time fluctuations induced by sequence length variability can trigger spurious fail-slow detections, and (2) failures are mitigated through individual adaptations in hybrid parallelism, leading to unnecessary detection 

### AI 总结

总结生成失败

---

## 3. Height-Guided Projection Reparameterization for Camera-LiDAR Occupancy

- **作者**: Yuan Wu, Zhiqiang Yan, Jiawei Lian, Zhengxue Wang, Jian Yang
- **发布日期**: 2026-05-06
- **链接**: [arXiv:2605.05072v2](https://arxiv.org/abs/2605.05072v2) | [PDF](https://arxiv.org/pdf/2605.05072v2)
- **分类**: cs.CV
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/yanzq95/HiPR.) ⭐ 0

### 摘要

3D occupancy prediction aims to infer dense, voxel-wise scene semantics from sensor observations, where the 2D-to-3D view transformation serves as a crucial step in bridging image features and volumetric representations.

Most previous methods rely on a fixed projection space, where 3D reference points are uniformly sampled along pillars.

However, such sampling struggles to capture the sparsity and height variations of real-world scenes, leading to ambiguous correspondences and unreliable feature aggregation.

To address these challenges, we propose HiPR, a camera-LiDAR occupancy framework with 

### AI 总结

总结生成失败

---

## 4. AsymTalker: Identity-Consistent Long-Term Talking Head Generation via Asymmetric Distillation

- **作者**: Yuxin Lu, Jiayang Sun, Guibo Zhu, Min Cao
- **发布日期**: 2026-05-01
- **链接**: [arXiv:2605.02948v3](https://arxiv.org/abs/2605.02948v3) | [PDF](https://arxiv.org/pdf/2605.02948v3)
- **分类**: cs.LG, cs.AI, cs.SD
- **含金量**: 20/43 分

### 摘要

Diffusion-based talking head generation has achieved remarkable visual quality, yet scaling it to long-term videos remains challenging.

The widely adopted chunk-wise paradigm introduces two fundamental failures: (1) temporal-spatial misalignment between static identity references and dynamic audio streams, and (2) cascading identity drift propagated through self-generated continuity references across chunks.

To address both issues, we propose AsymTalker, a novel diffusion-based talking head generation method comprising Temporal Reference Encoding (TRE) and Asymmetric Knowledge Distillation (AK

### AI 总结

总结生成失败

---

## 5. Online Sharp-Calibrated Bayesian Optimization

- **作者**: Marshal Arijona Sinaga, Julien Martinelli, Teemu Turpeinen, Samuel Kaski
- **发布日期**: 2026-05-11
- **链接**: [arXiv:2605.10572v1](https://arxiv.org/abs/2605.10572v1) | [PDF](https://arxiv.org/pdf/2605.10572v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Bayesian optimization (BO) is a widely used framework for optimizing expensive black-box functions, commonly based on Gaussian process (GP) surrogate models.

Its effectiveness relies on uncertainty quantification that is both sharp (informative) and well-calibrated along the BO trajectory.

In practice, GP kernel hyperparameters are unknown and are refit online from sequentially collected (non-i.i.d.) data, which can yield miscalibrated or overly conservative uncertainty and lies outside the fixed-kernel assumptions of standard BO regret theory.

We propose Online Sharp-Calibrated Bayesian Optim

### AI 总结

总结生成失败

---

## 6. Fast Training of Mixture-of-Experts for Time Series Forecasting via Expert Loss Integration

- **作者**: Btissame El Mahtout, Florian Ziel
- **发布日期**: 2026-05-11
- **链接**: [arXiv:2605.10330v1](https://arxiv.org/abs/2605.10330v1) | [PDF](https://arxiv.org/pdf/2605.10330v1)
- **分类**: stat.ML, cs.LG, stat.ME
- **含金量**: 20/43 分

### 摘要

We propose a novel adaptive Mixture-of-Experts (MoE) framework for time series forecasting that enhances expert specialization by incorporating expert-specific loss information directly into the training process.

Notably, the overall objective comprises the base forecasting loss and expert-specific losses, allowing expert-level prediction errors to jointly shape training alongside the global forecasting loss.

This framework is further combined with a partial online learning strategy, enabling incremental updates of both the gating mechanism and expert parameters.

This approach significantly re

### AI 总结

总结生成失败

---

## 7. Sample-Mean Anchored Thompson Sampling for Offline-to-Online Learning with Distribution Shift

- **作者**: Bochao Li, Yao Fu, Wei Chen, Fang Kong
- **发布日期**: 2026-05-11
- **链接**: [arXiv:2605.10289v1](https://arxiv.org/abs/2605.10289v1) | [PDF](https://arxiv.org/pdf/2605.10289v1)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

Offline-to-online learning aims to improve online decision-making by leveraging offline logged data.

A central challenge in this setting is the distribution shift between offline and online environments.

While some existing works attempt to leverage shifted offline data, they largely rely on UCB-type algorithms.

Thompson sampling (TS) represents another canonical class of bandit algorithms, well known for its strong empirical performance and naturally suited to offline-to-online learning through its Bayesian formulation.

However, unlike UCB indices, posterior samples in TS are not guaranteed t

### AI 总结

总结生成失败

---

## 8. Online Learning-Based Control with Guaranteed Error Bounds for a Class of Nonlinear Systems

- **作者**: Ricus Husmann, Sven Weishaupt, Malin Lotta Husmann, Harald Aschemann
- **发布日期**: 2026-05-11
- **链接**: [arXiv:2605.10152v1](https://arxiv.org/abs/2605.10152v1) | [PDF](https://arxiv.org/pdf/2605.10152v1)
- **分类**: eess.SY
- **含金量**: 20/43 分

### 摘要

In this paper, we present a learning-based control for a class of nonlinear systems that guarantees exponential stability as well as bounded output errors.

The control is based on the Gaussian Process Submodel Online Learning (GPSOL) algorithm and the Disturbance Error Rate Limiting (DERL) algorithm, both of which were developed in previous work.

The GPSOL algorithm provides a method to learn Gaussian Process (GP) models for subsystems online, whereas the DERL algorithm allows to limit the rate of the prediction error of these GP models.

The focus of this paper is the utilization of the GP mod

### AI 总结

总结生成失败

---

## 9. Continuous Latent Contexts Enable Efficient Online Learning in Transformers

- **作者**: Emile Anand, Abdullah Ateyeh, Xinyuan Cao, Max Dabagia
- **发布日期**: 2026-05-11
- **链接**: [arXiv:2605.09867v1](https://arxiv.org/abs/2605.09867v1) | [PDF](https://arxiv.org/pdf/2605.09867v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

Large language models (LLMs) exhibit a strong capacity for in-context learning: Given labeled examples, they can generate good predictions without parameter updates.

However, many interactive settings go beyond static prediction to online decision-making, in which effective behavior demands adaptation over long multi-turn horizons in response to feedback, and efficient algorithms in these domains must use compact representations of what they have learned.

Recently, continuous transformer architectures with latent chain of thought have shown promise for offline iterative tasks such as directed 

### AI 总结

总结生成失败

---

## 10. Filtering Memorization from Parameter-Space in Diffusion Models

- **作者**: Yu Zhe, Yang Jiayan, Wei Junhao, Yu-Lin Tsai, Wang Chen
- **发布日期**: 2026-05-11
- **链接**: [arXiv:2605.10439v1](https://arxiv.org/abs/2605.10439v1) | [PDF](https://arxiv.org/pdf/2605.10439v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

Low-Rank Adaptation (LoRA) has become a widely used mechanism for customizing diffusion models, enabling users to inject new visual concepts or styles through lightweight parameter updates.

However, LoRAs can memorize training images, causing generated outputs to reproduce copyrighted or sensitive content.

This risk is particularly concerning in LoRA-sharing ecosystems, where users distribute trained LoRAs without releasing the underlying training data.

Existing approaches for mitigating memorization rely on access to the training pipeline, training data, or control over the inference process,

### AI 总结

总结生成失败

---

