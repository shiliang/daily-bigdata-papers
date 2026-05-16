# 大数据+AI 领域论文日报

**日期**: 2026-05-16

**论文数量**: 5 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Efficient Online Conformal Selectio...](https://arxiv.org/abs/2605.14953v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [In-Context Learning for Data-Driven...](https://arxiv.org/abs/2605.14840v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Peng's Q($λ$) for Conservative Valu...](https://arxiv.org/abs/2605.14779v1) | 待分析 | 评估失败 | [Code](https://github.com/oh-lab/CPQL.) | 20/43 |
| 4 | [Sample-Mean Anchored Thompson Sampl...](https://arxiv.org/abs/2605.10289v2) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Bringing Order to Asynchronous SGD:...](https://arxiv.org/abs/2605.02043v2) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Efficient Online Conformal Selection with Limited Feedback

- **作者**: Sreenivas Gollapudi, Kostas Kollias, Kamesh Munagala, Ali Sinop
- **发布日期**: 2026-05-14
- **链接**: [arXiv:2605.14953v1](https://arxiv.org/abs/2605.14953v1) | [PDF](https://arxiv.org/pdf/2605.14953v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

We address the problem of conformal selection, where an agent must select a minimal subset of options to ensure that at least one ``success'' is identified with a pre-specified target probability $φ$.

While traditional online conformal prediction focuses on maintaining validity for the observed sequence, minimizing the resource cost (efficiency) of such selections, especially under limited feedback, remains a significant challenge.

In this work, we consider settings with the most limited ``bandit'' feedback, and demonstrate that the simple Adaptive Conformal Inference (ACI) update rule, when a

### AI 总结

总结生成失败

---

## 2. In-Context Learning for Data-Driven Censored Inventory Control

- **作者**: Sohom Mukherjee, Anh-Duy Pham, Richard Pibernik, Yunbei Xu
- **发布日期**: 2026-05-14
- **链接**: [arXiv:2605.14840v1](https://arxiv.org/abs/2605.14840v1) | [PDF](https://arxiv.org/pdf/2605.14840v1)
- **分类**: cs.LG, math.OC, stat.ML
- **含金量**: 20/43 分

### 摘要

We study inventory control with decision-dependent censoring, focusing on the censored or repeated newsvendor (R-NV), where each order quantity determines whether demand is fully observed or censored by sales.

Existing approaches based on parametric Thompson sampling (TS) can be brittle under prior mismatch, while offline imputation methods need not transfer to online learning.

Motivated by the predictive view of decision making, we combine these ideas by taking oracle actions on learned completions of latent demand.

We propose in-context generative posterior sampling (ICGPS), which uses moder

### AI 总结

总结生成失败

---

## 3. Peng's Q($λ$) for Conservative Value Estimation in Offline Reinforcement Learning

- **作者**: Byeongchan Kim, Min-hwan Oh
- **发布日期**: 2026-05-14
- **链接**: [arXiv:2605.14779v1](https://arxiv.org/abs/2605.14779v1) | [PDF](https://arxiv.org/pdf/2605.14779v1)
- **分类**: cs.LG
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/oh-lab/CPQL.) ⭐ 0

### 摘要

We propose a model-free offline multi-step reinforcement learning (RL) algorithm, Conservative Peng's Q($λ$) (CPQL).

Our algorithm adapts the Peng's Q($λ$) (PQL) operator for conservative value estimation as an alternative to the Bellman operator.

To the best of our knowledge, this is the first work in offline RL to theoretically and empirically demonstrate the effectiveness of conservative value estimation with a \textit{multi-step} operator by fully leveraging offline trajectories.

The fixed point of the PQL operator in offline RL lies closer to the value function of the behavior policy, the

### AI 总结

总结生成失败

---

## 4. Sample-Mean Anchored Thompson Sampling for Offline-to-Online Learning with Distribution Shift

- **作者**: Bochao Li, Yao Fu, Wei Chen, Fang Kong
- **发布日期**: 2026-05-11
- **链接**: [arXiv:2605.10289v2](https://arxiv.org/abs/2605.10289v2) | [PDF](https://arxiv.org/pdf/2605.10289v2)
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

## 5. Bringing Order to Asynchronous SGD: Towards Optimality under Data-Dependent Delays with Momentum

- **作者**: Tehila Dahan, Roie Reshef, Sharon Goldstein, Kfir Y. Levy
- **发布日期**: 2026-05-03
- **链接**: [arXiv:2605.02043v2](https://arxiv.org/abs/2605.02043v2) | [PDF](https://arxiv.org/pdf/2605.02043v2)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Asynchronous stochastic gradient descent (SGD) enables scalable distributed training but suffers from gradient staleness.

Existing mitigation strategies, such as delay-adaptive learning rates and staleness-aware filtering, typically attenuate or discard delayed gradients, introducing systematic bias: updates from simpler or faster-to-process samples are overrepresented, while gradients from more complex samples are delayed or suppressed.

In contrast, prior approaches to data-dependent delays rely on a Lipschitz assumption that yields suboptimal rates or leave the smooth, convex case unaddresse

### AI 总结

总结生成失败

---

