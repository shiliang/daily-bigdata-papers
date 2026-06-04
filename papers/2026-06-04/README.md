# 大数据+AI 领域论文日报

**日期**: 2026-06-04

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Fine-grained Fragment Retrieval in ...](https://arxiv.org/abs/2606.04591v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Reconstructing Unobservable Tempera...](https://arxiv.org/abs/2606.04582v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Mean-based algorithms: A lower boun...](https://arxiv.org/abs/2606.04931v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Offline-to-Online Learning in Linea...](https://arxiv.org/abs/2606.04305v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [RL Excursions during Pre-Training: ...](https://arxiv.org/abs/2606.04272v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [EvoTrainer: Co-Evolving LLM Policie...](https://arxiv.org/abs/2606.03108v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [ACRONYM: Accelerated Approximate Ne...](https://arxiv.org/abs/2606.03151v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Online Learning with Gradient-Varia...](https://arxiv.org/abs/2606.03831v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [AUGUSTE: Online-Learning dApp for P...](https://arxiv.org/abs/2606.03664v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [E2LLM: Towards Efficient LLM Servin...](https://arxiv.org/abs/2606.03770v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Fine-grained Fragment Retrieval in Multi-modal Long-form Dialogues

- **作者**: Hanbo Bi, Zhiqiang Yuan, Chongyang Li, Qiwei Yan, Zexi Jia
- **发布日期**: 2026-06-03
- **链接**: [arXiv:2606.04591v1](https://arxiv.org/abs/2606.04591v1) | [PDF](https://arxiv.org/pdf/2606.04591v1)
- **分类**: cs.CL, cs.CV
- **含金量**: 20/43 分

### 摘要

With the widespread adoption of multi-modal communication platforms, long-form dialogues interleaving text and images have become increasingly common.

Users often need to retrieve coherent dialogue fragments related to specific topics, rather than isolated utterances.

We propose Fine-grained Fragment Retrieval (FFR), which locates semantically relevant multi-utterance, multi-image fragments in multi-modal long-form dialogues.

We explore two settings: (1) FFR within Single-Dialogue, retrieving fragments from a given dialogue; and (2) FFR within Dialogue Corpus, retrieving from a large-scale cor

### AI 总结

总结生成失败

---

## 2. Reconstructing Unobservable Temperature Fields via Simulation-Aided Intelligent Sensing

- **作者**: Monika Stipsitz, Hèlios Sanchis-Alepuz, Jacob Reynvaan, Silvester Sabathiel
- **发布日期**: 2026-06-03
- **链接**: [arXiv:2606.04582v1](https://arxiv.org/abs/2606.04582v1) | [PDF](https://arxiv.org/pdf/2606.04582v1)
- **分类**: physics.comp-ph, cs.LG, physics.app-ph
- **含金量**: 20/43 分

### 摘要

Real-time monitoring of the temperature distribution within components and sub-structures is a challenging topic in many systems due to restrictions on feasible sensor locations.

While machine learning (ML) proves a versatile tool in many applications, its adoption for high-resolution thermal monitoring is hindered by the availability of high-quality datasets for training.

In this work, we propose a novel approach for generating datasets for industrial applications based on randomized physics-based simulations.

We demonstrate the approach in a proof-of-concept hardware setup: A neural network 

### AI 总结

总结生成失败

---

## 3. Mean-based algorithms: A lower bound and regret

- **作者**: Julius Durmann, Amelie Kleber
- **发布日期**: 2026-06-03
- **链接**: [arXiv:2606.04931v1](https://arxiv.org/abs/2606.04931v1) | [PDF](https://arxiv.org/pdf/2606.04931v1)
- **分类**: cs.LG, cs.GT
- **含金量**: 20/43 分

### 摘要

Mean-based algorithms are a class of online learning algorithms that assign low probability to actions with low average rewards.

Recent work indicates these algorithms converge favorably to serially undominated actions, which approximate Nash equilibria in economic games.

However, empirical studies also show slower convergence compared to established algorithms in bandit-feedback scenarios.

We study mean-based algorithms when the time horizon is unknown and only bandit feedback is available.

In this setting, we provide the first lower bound on the algorithm-defining sequence $γ_t$ that forma

### AI 总结

总结生成失败

---

## 4. Offline-to-Online Learning in Linear Bandits

- **作者**: Kushagra Chandak, Toshinori Kitamura, Xiaoqi Tan
- **发布日期**: 2026-06-03
- **链接**: [arXiv:2606.04305v1](https://arxiv.org/abs/2606.04305v1) | [PDF](https://arxiv.org/pdf/2606.04305v1)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

We study online learning with an additional offline dataset in the stochastic linear bandit setting.

Although this problem arises frequently in practice, the offline-to-online tradeoff remains poorly understood in structured environments.

We propose a linear bandit algorithm that balances this tradeoff: it relies on offline data during early rounds, and increasingly favors exploration as the horizon grows.

We establish regret bounds showing that our method is simultaneously competitive with both purely online and purely offline solutions.

In particular, it achieves sublinear regret relative to

### AI 总结

总结生成失败

---

## 5. RL Excursions during Pre-Training: Re-examining Policy Optimization for LLM training

- **作者**: Rachit Bansal, Clara Mohri, Tian Qin, David Alvarez-Melis, Sham Kakade
- **发布日期**: 2026-06-02
- **链接**: [arXiv:2606.04272v1](https://arxiv.org/abs/2606.04272v1) | [PDF](https://arxiv.org/pdf/2606.04272v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

The standard LLM training pipeline applies reinforcement learning (RL) only after pre-training and supervised fine-tuning (SFT).

We question this status quo by training a LLM from scratch and applying RL, SFT, and SFT followed by RL directly to intermediate pre-training checkpoints.

We find that RL is effective very early, and often matches the full SFT$\to$RL pipeline early as well.

Through experiments on harder problems, we find that targeted pre-training data composition is a strong lever for RL effectiveness, even more so than model scale.

Beyond reasoning accuracy, applying RL directly to

### AI 总结

总结生成失败

---

## 6. EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agentic Reinforcement Learning

- **作者**: Guhong Chen, Yingcheng Shi, Yongbin Li, Binhua Li, Xander Xu
- **发布日期**: 2026-06-02
- **链接**: [arXiv:2606.03108v1](https://arxiv.org/abs/2606.03108v1) | [PDF](https://arxiv.org/pdf/2606.03108v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

Autonomous LLM training is often framed as recipe search, which leaves the training harness largely static.

This limitation sharpens in agentic RL, where shifting bottlenecks and scalar rewards mask diverse failure modes.

We introduce EvoTrainer, an autonomous training framework that co-evolves LLM policies and training-side harnesses through empirical feedback: it diagnoses rollout-level evidence, revises diagnostics, backtests interventions, and accumulates reusable skills.

Evaluated on mathematical reasoning, competitive-programming code generation, and repository-level software engineering

### AI 总结

总结生成失败

---

## 7. ACRONYM: Accelerated Approximate Nearest Neighbor Search in Memory for Dynamic Vector Databases

- **作者**: Md Mizanur Rahaman Nayan, Tianqi Zhang, Flavio Ponzina, Tajana Rosing, Azad J Naeemi
- **发布日期**: 2026-06-02
- **链接**: [arXiv:2606.03151v1](https://arxiv.org/abs/2606.03151v1) | [PDF](https://arxiv.org/pdf/2606.03151v1)
- **分类**: cs.AR, cs.DB, cs.ET
- **含金量**: 20/43 分

### 摘要

Vector database search with frequent updates is increasingly critical in applications such as retrieval augmented generation, recommendation systems, and large-scale embedding retrieval.

Existing solutions, such as graph-based and partition-based approximate nearest neighbor search (ANNS), suffer from frequent index rebuilding due to data distribution-dependent indexing that impacts continuous deployment and causes long rebuilding latency.

This paper proposes an algorithm-hardware co-designed platform, ACRONYM, that addresses key problems with state of the art database search.

Algorithmically,

### AI 总结

总结生成失败

---

## 8. Online Learning with Gradient-Variation Interval Regret

- **作者**: Yan-Feng Xie, Shuche Wang, Peng Zhao, Zhi-Hua Zhou
- **发布日期**: 2026-06-02
- **链接**: [arXiv:2606.03831v1](https://arxiv.org/abs/2606.03831v1) | [PDF](https://arxiv.org/pdf/2606.03831v1)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

This paper investigates non-stationary online learning using the metric of interval regret, which requires an online algorithm to perform well over every time interval.

We propose the first online learning algorithm that achieves an interval regret bound scaling with gradient variation, a fundamental measure of the cumulative change in online function gradients, which relates to various problem-dependent quantities and is closely connected to stochastic optimization and other problems.

Our method employs a simple and efficient two-layer online ensemble structure that achieves strong theoretica

### AI 总结

总结生成失败

---

## 9. AUGUSTE: Online-Learning dApp for Predictive URLLC Scheduling

- **作者**: Maxime Elkael, Michele Polese, Yunseong Lee, Koichiro Furueda, Tommaso Melodia
- **发布日期**: 2026-06-02
- **链接**: [arXiv:2606.03664v1](https://arxiv.org/abs/2606.03664v1) | [PDF](https://arxiv.org/pdf/2606.03664v1)
- **分类**: cs.NI, cs.AI
- **含金量**: 20/43 分

### 摘要

Ultra Reliable and Low Latency Communications (URLLC) was one of the main motivations behind 5G, with 3GPP advertising 1-10 ms latency targets for applications such as industrial automation, Vehicle-To-Everything (V2X), tactical edge networking, and unmanned-system control.

Years on, real 5G Time Division Duplexing (TDD) networks still show median Uplink (UL) round-trip times in the 50-70 ms range, largely because of the Scheduling Request (SR) procedure that a User Equipment (UE) must complete before transmitting UL data.

Existing remedies, primarily Configured Grant (CG) scheduling, only eli

### AI 总结

总结生成失败

---

## 10. E2LLM: Towards Efficient LLM Serving in Heterogeneous Edge/Fog Environments

- **作者**: Truong-Thanh Le, Amir Taherkordi, Hoang-Loc La, Frank Eliassen, Phuong Hoai Ha
- **发布日期**: 2026-06-02
- **链接**: [arXiv:2606.03770v1](https://arxiv.org/abs/2606.03770v1) | [PDF](https://arxiv.org/pdf/2606.03770v1)
- **分类**: cs.DC, cs.AI
- **含金量**: 20/43 分

### 摘要

Large Language Models (LLMs) have become integral to modern applications, yet their deployment remains challenging.

Beyond executing the models themselves, practical deployment must address cost efficiency, low latency, and optimal resource utilization.

Conventional approaches typically assume that an entire model can be hosted on a single device, which does not hold in many real-world scenarios, particularly in Edge and Fog environments where device resources are constrained.

In this paper, we introduce E2LLM, a framework designed to enable efficient LLM deployment in such resource limited se

### AI 总结

总结生成失败

---

