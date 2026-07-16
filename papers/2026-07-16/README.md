# 大数据+AI 领域论文日报

**日期**: 2026-07-16

**论文数量**: 8 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [The Environmental Cost of Digital S...](https://arxiv.org/abs/2607.13443v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [LiteTopK: Exploiting the Curse of D...](https://arxiv.org/abs/2607.11976v2) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [WAVE-Stereo: Warp-Aligned Volume En...](https://arxiv.org/abs/2607.13674v1) | 待分析 | 评估失败 | [Code](https://github.com/yamanoko-do/WAVE-Stereo.) | 20/43 |
| 4 | [Structured Reinforcement Learning f...](https://arxiv.org/abs/2607.13576v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [From Novice to Expert: Cost-Aware B...](https://arxiv.org/abs/2607.13546v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Reverse to Advance: Teleoperation-C...](https://arxiv.org/abs/2607.13455v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Change-Aware Self-Adaptive AI-Aided...](https://arxiv.org/abs/2607.13387v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Agora: Collective and Permissionles...](https://arxiv.org/abs/2607.13332v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. The Environmental Cost of Digital Sovereignty: Water, Energy, and Emissions Impacts of Sovereign AI Infrastructure in the Global South

- **作者**: Muntaser Syed, Marius C. Silaghi, Sheikh Abujar, Sharun Akter Khushbu, Amal El Ahmad
- **发布日期**: 2026-07-15
- **链接**: [arXiv:2607.13443v1](https://arxiv.org/abs/2607.13443v1) | [PDF](https://arxiv.org/pdf/2607.13443v1)
- **分类**: cs.CY, cs.DC
- **含金量**: 20/43 分

### 摘要

Sovereign AI has become a strategic priority across the Global South, with over \$200 billion in state-led commitments announced between 2024 and 2026.

Yet the physical infrastructure that compute sovereignty demands, above all data centers, imposes water, energy, and carbon costs that fall hardest on countries least equipped to absorb them.

This paper presents a comparative environmental stress analysis across four cases: the United Arab Emirates, Bangladesh, India, and Africa (with a focus on Kenya).

Using publicly available water stress data, grid carbon intensity factors, and GPU power spe

### AI 总结

总结生成失败

---

## 2. LiteTopK: Exploiting the Curse of Dimensionality for a Fused Indexer-TopK Kernel in Long-Context Sparse Attention

- **作者**: Ziqi Yin, Jianyang Gao, Peiqi Yin, Jiangneng Li, Gao Cong
- **发布日期**: 2026-07-13
- **链接**: [arXiv:2607.11976v2](https://arxiv.org/abs/2607.11976v2) | [PDF](https://arxiv.org/pdf/2607.11976v2)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Indexer-TopK, the operation to compute the scores and select the top-k candidates, is widely used by sparse attention kernels in large language models and vector retrieval in recommendation systems and vector databases.

However, existing GPU-based Indexer-TopK kernels like DeepSeek Sparse Attention (DSA) remain inefficient due to excessive global memory traffic, costly synchronization, and prohibitive memory overhead.

In this work, we exploit the curse of dimensionality in high-dimensional spaces, where distances between high-dimensional vectors tend to concentrate within a narrow range, to de

### AI 总结

总结生成失败

---

## 3. WAVE-Stereo: Warp-Aligned Volume Encoding for Stereo Matching

- **作者**: Zehan Liu, Yage He, Xianwu Gong
- **发布日期**: 2026-07-15
- **链接**: [arXiv:2607.13674v1](https://arxiv.org/abs/2607.13674v1) | [PDF](https://arxiv.org/pdf/2607.13674v1)
- **分类**: cs.CV, cs.RO
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/yamanoko-do/WAVE-Stereo.) ⭐ 0

### 摘要

Existing iterative stereo matching methods primarily adopt two types of correspondence representation: explicit matching search via correlation volumes and local residual refinement via warped features, yet the two remain separately modeled.

We propose WAVE-Stereo, built on a core insight: correlation volumes and feature warping provide complementary matching cues.

\textbf{GeoWarp Correspondence Encoder (GWCE)} encodes matching search, residual alignment, and disparity prior in parallel at the ConvGRU input.

To mitigate matching degradation in textureless regions, we propose \textbf{Periodic G

### AI 总结

总结生成失败

---

## 4. Structured Reinforcement Learning for Bayesian Persuasion : Application to Intelligent Interactive Driving

- **作者**: Merlin Paul, Anup Aprem
- **发布日期**: 2026-07-15
- **链接**: [arXiv:2607.13576v1](https://arxiv.org/abs/2607.13576v1) | [PDF](https://arxiv.org/pdf/2607.13576v1)
- **分类**: cs.LG, eess.SP
- **含金量**: 20/43 分

### 摘要

Interactive driving, wherein an intelligent lead vehicle equipped with real-time traffic data coordinates route choices of connected vehicles, offers a promising approach to dynamic traffic management.

To address the challenge of harmonising decisions, this paper considers the strategic information revealing framework of Bayesian persuasion.

Here, the principal (lead vehicle) aims to guide the agent's (connected vehicle) partially observable sequential decision making towards its own objectives by selectively revealing information, such as real-time traffic ahead, using signals.

However, the a

### AI 总结

总结生成失败

---

## 5. From Novice to Expert: Cost-Aware Bandits for Evolving Worker Performance in Crowdsensing

- **作者**: Yin Huang, Qingsong Liu, Jie Xu
- **发布日期**: 2026-07-15
- **链接**: [arXiv:2607.13546v1](https://arxiv.org/abs/2607.13546v1) | [PDF](https://arxiv.org/pdf/2607.13546v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Mobile crowdsensing (MC) recruits mobile users to perform sensing tasks using their smartphones, enabling large-scale applications such as traffic monitoring and environmental sensing.

A fundamental challenge is online worker recruitment under uncertainty, where the platform must learn workers' sensing performance while operating with a limited budget.

Existing learning-based MC recruitment methods typically assume that each worker's sensing quality is stationary with a fixed mean over time.

In practice, however, worker performance often improves with experience and eventually stabilizes, whil

### AI 总结

总结生成失败

---

## 6. Reverse to Advance: Teleoperation-Cost Effective Hard Policy Learning from Reversed Easy Tasks

- **作者**: Qiyuan Qiao, Ge Yuan, Can Wang, Dong Xu
- **发布日期**: 2026-07-15
- **链接**: [arXiv:2607.13455v1](https://arxiv.org/abs/2607.13455v1) | [PDF](https://arxiv.org/pdf/2607.13455v1)
- **分类**: cs.RO
- **含金量**: 20/43 分

### 摘要

High-quality teleoperation datasets are costly to collect, particularly for hard tasks.

We observe that many tasks exhibit directional asymmetry: completing the forward hard task is difficult, whereas reversing it by relaxing or disrupting the environment is comparatively easy.

This suggests that reversed easy-task trajectories can serve as a scalable supervision signal for the hard task, reducing the cost of manual demonstration collection.

However, reversed data can be noisy, and directly training on it may yield suboptimal policies.

To enable largely automated acquisition and effective use 

### AI 总结

总结生成失败

---

## 7. Change-Aware Self-Adaptive AI-Aided Kalman Filters With Neural Change Point Detection

- **作者**: Wenyi Zhang, Xiaoyong Ni, Nir Shlezinger, Zengfu Wang
- **发布日期**: 2026-07-15
- **链接**: [arXiv:2607.13387v1](https://arxiv.org/abs/2607.13387v1) | [PDF](https://arxiv.org/pdf/2607.13387v1)
- **分类**: eess.SY
- **含金量**: 20/43 分

### 摘要

Reliable state estimation in dynamical systems is often challenged by model mismatches, unknown noise statistics, and temporal variations.

While AI-aided Kalman filters such as KalmanNet leverage deep learning to enhance classical estimation, they remain vulnerable to distribution shifts and lack mechanisms for autonomous adaptation.

This work introduces Change-Aware Self-Adaptive KalmanNet (CASA-KalmanNet), an online adaptation framework that integrates a dedicated neural module, termed CPDNet, to monitor the interpretable internal features of KalmanNet and provide soft indicators of reliabil

### AI 总结

总结生成失败

---

## 8. Agora: Collective and Permissionless Internet-Scale Pretraining of Large Language Models

- **作者**: Gil Avraham, Violetta Shevchenko, Hadi Mohaghegh Dolatabadi, Karol Pajak, James Snewin
- **发布日期**: 2026-07-14
- **链接**: [arXiv:2607.13332v1](https://arxiv.org/abs/2607.13332v1) | [PDF](https://arxiv.org/pdf/2607.13332v1)
- **分类**: cs.LG, cs.DC
- **含金量**: 20/43 分

### 摘要

Training large language models at the multi-billion to trillion parameter scale is confined to datacenters, where data-parallel (DP) and model-parallel (MP) techniques presume homogeneous accelerators, high-speed interconnects, and a single orchestrating entity.

Frontier model development is thereby concentrated among the few groups able to assemble such clusters.

Meanwhile, an enormous pool of compute remains unusable for training: consumer and professional GPUs that are heterogeneous, preemptible, individually owned, and connected only by the internet.

We present Agora, a system that makes e

### AI 总结

总结生成失败

---

