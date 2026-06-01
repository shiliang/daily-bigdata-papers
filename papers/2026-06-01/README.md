# 大数据+AI 领域论文日报

**日期**: 2026-06-01

**论文数量**: 9 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Vector Linking via Cross-Model Loca...](https://arxiv.org/abs/2605.31100v1) | 待分析 | 评估失败 | [Code](https://github.com/DBgroup-Edinburgh/VecLinking.) | 20/43 |
| 2 | [Practical Cross-Band Channel Predic...](https://arxiv.org/abs/2605.31279v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [LiteViLNet: Lightweight Vision-LiDA...](https://arxiv.org/abs/2605.21007v2) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Learning to Bid in FCR Markets: A B...](https://arxiv.org/abs/2605.31070v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [OrcaRouter: A Production-Oriented L...](https://arxiv.org/abs/2605.30736v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Universal Decision Learners](https://arxiv.org/abs/2605.30694v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Self-Supervised Online Robot-Agnost...](https://arxiv.org/abs/2605.28442v2) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [The Fundamental Limits of Fraud Det...](https://arxiv.org/abs/2605.27557v2) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Universal Multiclass Transductive O...](https://arxiv.org/abs/2605.30479v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Vector Linking via Cross-Model Local Isometric Consistency

- **作者**: Ziying Chen, Yang Cao, He Sun, Beining Yang, Tianjian Yang
- **发布日期**: 2026-05-29
- **链接**: [arXiv:2605.31100v1](https://arxiv.org/abs/2605.31100v1) | [PDF](https://arxiv.org/pdf/2605.31100v1)
- **分类**: cs.AI, cs.DB, cs.IR
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/DBgroup-Edinburgh/VecLinking.) ⭐ 0

### 摘要

We study Vector Linking: given two embedding clouds produced by different black-box encoders over partially overlapping datasets, recover cross-model object correspondences using only vectors.

Empirically and theoretically, we show that independently trained contrastive encoders exhibit local geometric consistency: short-range distances are approximately preserved up to a scale factor, while long-range distances are not due to model-specific distortion.

Building on this, we propose an iterative, reference-based geometric embedding hashing that recovers vector links from a tiny seed set of pair

### AI 总结

总结生成失败

---

## 2. Practical Cross-Band Channel Prediction for AI-RAN via Physics-Guided Deep Unfolding

- **作者**: Ruiqi Kong, He Chen, Xiaojun Lin
- **发布日期**: 2026-05-29
- **链接**: [arXiv:2605.31279v1](https://arxiv.org/abs/2605.31279v1) | [PDF](https://arxiv.org/pdf/2605.31279v1)
- **分类**: eess.SP, cs.AI, cs.NI
- **含金量**: 20/43 分

### 摘要

To make cross-band channel prediction practical for AI-native RAN, algorithms must generalize across diverse environments and support real-time inference.

Existing approaches achieve one but not both.

To bridge this gap, we introduce GUIDE, a physics-guided deep unfolding framework that embeds wireless channel physics into differentiable layers.

Without retraining in unseen environments, GUIDE achieves 2.75x beamforming gain than the deep learning-based baseline FIRE with only a slight increase in inference time, and 1.39x beamforming gain than the strongest model-based baseline R2F2 while run

### AI 总结

总结生成失败

---

## 3. LiteViLNet: Lightweight Vision-LiDAR Fusion Network for Efficient Road Segmentation

- **作者**: Daojie Peng, Bingtao Wang, Fulong Ma, Liang Zhang, Jun Ma
- **发布日期**: 2026-05-20
- **链接**: [arXiv:2605.21007v2](https://arxiv.org/abs/2605.21007v2) | [PDF](https://arxiv.org/pdf/2605.21007v2)
- **分类**: cs.CV, cs.RO
- **含金量**: 20/43 分

### 摘要

Road segmentation is a fundamental perception task for autonomous driving and intelligent robotic systems, requiring both high accuracy and real-time inference, especially for deployment on resource-constrained edge devices.

Existing multi-modal road segmentation methods often rely on heavy transformer-based encoders to achieve state-of-the-art performance, but their enormous computational cost prohibits real-time deployment on embedded platforms.

To address this dilemma, we propose LiteViLNet, a lightweight multi-modal network that fuses RGB texture information and LiDAR geometric information

### AI 总结

总结生成失败

---

## 4. Learning to Bid in FCR Markets: A Best-of-Both-Worlds Approach

- **作者**: Marius Potfer, Cheng Wan, Pierre Gruet
- **发布日期**: 2026-05-29
- **链接**: [arXiv:2605.31070v1](https://arxiv.org/abs/2605.31070v1) | [PDF](https://arxiv.org/pdf/2605.31070v1)
- **分类**: cs.LG, cs.GT
- **含金量**: 20/43 分

### 摘要

Bidding in the European Frequency Containment Reserve (FCR) market is challenging for flexibility providers because competing offers are hidden and bidders observe only partial feedback form the market, such as, clearing price and awarded quantity.

For a participant active in a single country, we show that the multi-country FCR clearing problem can be recast as a repeated multi-unit uniform-price auction against an endogenous vector of opposing bids.

This reformulation yields an online learning problem and allows us to adapt a Best-of-Both-Worlds combinatorial semi-bandit algorithm implementab

### AI 总结

总结生成失败

---

## 5. OrcaRouter: A Production-Oriented LLM Router with Hybrid Offline-Online Learning

- **作者**: Zhenghua Bao, Fengya Tian, Chris Zhang, Zhenjun Chen, Xile Ma
- **发布日期**: 2026-05-29
- **链接**: [arXiv:2605.30736v1](https://arxiv.org/abs/2605.30736v1) | [PDF](https://arxiv.org/pdf/2605.30736v1)
- **分类**: cs.LG, cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

The rapid development of large language models, each with distinct capabilities and inference costs, raises a practical deployment question: given an incoming request, which model should handle it? We present OrcaRouter, a production-oriented LLM router that combines a LinUCB-based contextual bandit over lexical and sentence-embedding features with a hybrid offline-online learning protocol.

Offline, OrcaRouter obtains full-information feedback by evaluating each candidate model on a curated set of routing prompts, yielding a reward matrix used to fit one ridge regressor per arm.

At deployment 

### AI 总结

总结生成失败

---

## 6. Universal Decision Learners

- **作者**: Sridhar Mahadevan
- **发布日期**: 2026-05-29
- **链接**: [arXiv:2605.30694v1](https://arxiv.org/abs/2605.30694v1) | [PDF](https://arxiv.org/pdf/2605.30694v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Many theories of decision making -- planning, reinforcement learning, causal intervention, online learning, and game-theoretic equilibrium -- turn local information into globally coherent behavior.

This paper proposes a common categorical formulation: a Universal Decision Learner (UDL) extends a partially specified decision functor from observed contexts to new contexts by a pair of universal constructions.

Left Kan extensions express rollout, aggregation, and candidate generation; right Kan extensions express consistency, constraint satisfaction, and fixed-point semantics.

The central claim i

### AI 总结

总结生成失败

---

## 7. Self-Supervised Online Robot-Agnostic Traversability Estimation for Open-World Environments

- **作者**: Julia Hindel, Simon Bultmann, Houman Masnavi, Daniele Cattaneo, Abhinav Valada
- **发布日期**: 2026-05-27
- **链接**: [arXiv:2605.28442v2](https://arxiv.org/abs/2605.28442v2) | [PDF](https://arxiv.org/pdf/2605.28442v2)
- **分类**: cs.RO, cs.CV
- **含金量**: 20/43 分

### 摘要

Self-supervised online traversability estimation enables robots to continuously learn from unlabeled open-world experiences and adapt their navigation behavior toward safe and efficient trajectories.

Existing approaches either rely on handcrafted proprioceptive traversability scores, limiting robot-agnosticism, or cluster prior data, preventing online learning.

Moreover, many continual learning methods incur substantial memory and computational costs, hindering onboard deployment.

We introduce COTRATE, an online learning framework for continuous traversability estimation from multimodal, unlab

### AI 总结

总结生成失败

---

## 8. The Fundamental Limits of Fraud Detection in Card Payment Networks

- **作者**: Gaurav Dhama
- **发布日期**: 2026-05-26
- **链接**: [arXiv:2605.27557v2](https://arxiv.org/abs/2605.27557v2) | [PDF](https://arxiv.org/pdf/2605.27557v2)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

Card payment fraud detection is usually framed as a supervised classification problem.

Although this approach has generated practical progress, improvement has remained incremental despite major advances in model architecture.

We argue that this is not mainly a failure of function approximation or optimization, but a consequence of structural information impairments inherent to the payment ecosystem.

We formalize card authorization as a sequential decision problem with delayed, censored, corrupted, and counterfactually missing feedback.

We derive a minimax regret lower bound showing that the

### AI 总结

总结生成失败

---

## 9. Universal Multiclass Transductive Online Learning

- **作者**: Steve Hanneke, Hongao Wang
- **发布日期**: 2026-05-28
- **链接**: [arXiv:2605.30479v1](https://arxiv.org/abs/2605.30479v1) | [PDF](https://arxiv.org/pdf/2605.30479v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

We consider the problem of universal transductive online classification with a possibly unbounded label space.

This setting considers online learning, with the sequence of instances (without labels) known to the learner in advance.

We say a concept class $\mathcal{H}$ is learnable if there is a learning algorithm $\mathcal{A}$, such that for every realizable sequence, the number of mistakes made by $\mathcal{A}$ grows at most sublinearly with the number of predictions.

We characterize the learnability of this setting and show that there are only two possible optimal rates for the learnable cla

### AI 总结

总结生成失败

---

