# 大数据+AI 领域论文日报

**日期**: 2026-07-14

**论文数量**: 8 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [A Sovereign, Open-Source Foundation...](https://arxiv.org/abs/2607.09424v2) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [NeuralActuator: Neural Actuation Mo...](https://arxiv.org/abs/2607.11734v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Efficient Online Proportional Sampl...](https://arxiv.org/abs/2607.10963v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Unlocking Parallelism in Autoregres...](https://arxiv.org/abs/2607.10661v1) | 待分析 | 评估失败 | [Code](https://github.com/MINE-USTC/PTD.) | 20/43 |
| 5 | [A Knowledge-Based Multi-Agent Frame...](https://arxiv.org/abs/2607.09954v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Implicit Midpoint Gradient Descent:...](https://arxiv.org/abs/2607.09950v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Dynamics and Convergences for Marko...](https://arxiv.org/abs/2607.05580v2) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [JEPA for AI-Native 6G: Predictive R...](https://arxiv.org/abs/2607.09798v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. A Sovereign, Open-Source Foundation Model for German and English

- **作者**: The Soofi-Team,  :, Benedikt Droste, David Fitzek, Ruben Härle
- **发布日期**: 2026-07-10
- **链接**: [arXiv:2607.09424v2](https://arxiv.org/abs/2607.09424v2) | [PDF](https://arxiv.org/pdf/2607.09424v2)
- **分类**: cs.CL, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

We present Soofi S 30B-A3B, a sovereign, open-source Mixture-of-Experts (MoE) hybrid Mamba Transformer foundation model for German and English.

Its hybrid design activates only 3B of 30B parameters per token and keeps the inference cache near-constant as context grows, giving it a decisive throughput advantage over dense models for long-context, high-concurrency deployment.

Pretrained on roughly 27 trillion tokens with deliberately up-weighted German, Soofi S matches dense 14 to 27B models on aggregate English and German benchmarks while achieving the best code aggregates in both languages amo

### AI 总结

总结生成失败

---

## 2. NeuralActuator: Neural Actuation Modeling for Robot Dynamics and External Force Perception

- **作者**: Zhiyang Dou, John U. Onyemelukwe, Hangxing Zhang, Heng Zhang, Minghao Guo
- **发布日期**: 2026-07-13
- **链接**: [arXiv:2607.11734v1](https://arxiv.org/abs/2607.11734v1) | [PDF](https://arxiv.org/pdf/2607.11734v1)
- **分类**: cs.RO, cs.CV, cs.GR, cs.LG
- **含金量**: 20/43 分

### 摘要

Differentiable simulators have advanced policy learning and model-based control, yet actuator dynamics remain an important source of sim-to-real error.

This is particularly acute on low-cost platforms, where the linear current-to-torque relation $τ= K_tI$ becomes unreliable during commanded-target tracking because of friction, hysteresis, backlash, and thermal effects.

We present NeuralActuator, a neural actuator model that jointly predicts (i) a simulator-equivalent generalized-effort surrogate for trajectory propagation on low-cost servo platforms, (ii) external force with a contact-probabil

### AI 总结

总结生成失败

---

## 3. Efficient Online Proportional Sampling with Applications to Smoothed Online Learning

- **作者**: Amirmahdi Mirfakhar, Maria-Florina Balcan, Hedyeh Beyhaghi
- **发布日期**: 2026-07-13
- **链接**: [arXiv:2607.10963v1](https://arxiv.org/abs/2607.10963v1) | [PDF](https://arxiv.org/pdf/2607.10963v1)
- **分类**: cs.LG, cs.AI, cs.CG, cs.GT, econ.TH
- **含金量**: 20/43 分

### 摘要

We study the problem of efficient online proportional sampling from a high-dimensional domain under a $σ$-smoothed adversary, where the sampling distribution is induced by a dynamically evolving weight function defined over a sequence of piecewise-structured partitions.

This setting captures a broad range of applications, including principal-agent games (e.g., pricing and contract design), and algorithm configuration and parameter tuning.

The central challenge is maintaining an efficient data structure as the induced partition grows increasingly complex over time -- naively, the number of subr

### AI 总结

总结生成失败

---

## 4. Unlocking Parallelism in Autoregressive Language Models via Speculative Decoding with Progressive Tree Drafting

- **作者**: Zipeng Gao, Zhi Zheng, Qingrong Xia, Junda Lin, Ziwei Zhao
- **发布日期**: 2026-07-12
- **链接**: [arXiv:2607.10661v1](https://arxiv.org/abs/2607.10661v1) | [PDF](https://arxiv.org/pdf/2607.10661v1)
- **分类**: cs.CL, cs.AI
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/MINE-USTC/PTD.) ⭐ 0

### 摘要

Speculative decoding has significantly accelerated Large Language Model (LLM) inference by alleviating memory-bound bottlenecks.

However, traditional speculative decoding typically relies on auxiliary draft modules, incurring significant training and communication overhead.

Although recent methods attempt to generate drafts within the target model itself, they often fail to fully exploit its latent parallel capacity due to a lack of structural coordination.

In this paper, we propose \textbf{Progressive Tree Drafting (PTD)}, which employs a structured, guided parallel drafting strategy to harne

### AI 总结

总结生成失败

---

## 5. A Knowledge-Based Multi-Agent Framework for Security Control Recommendation

- **作者**: Carolina Fernández-Martínez, Shuaib Siddiqui, Vanesa Daza
- **发布日期**: 2026-07-10
- **链接**: [arXiv:2607.09954v1](https://arxiv.org/abs/2607.09954v1) | [PDF](https://arxiv.org/pdf/2607.09954v1)
- **分类**: cs.GT, cs.AI, cs.CR, cs.LG, cs.MA
- **含金量**: 20/43 分

### 摘要

Hardening IT on-premises environments can be a daunting task for teams without access to adequate cybersecurity expertise.

In this regard, Decision Support Systems (DSS) with embedded expert knowledge can assist users by guiding them with security recommendations to meet their objectives.

This work proposes a Security DSS that recommends security control sub-families given minimal user requirements indicating coverage of different security dimensions.

It leverages a curated, unified dataset from both well-known Information Security (InfoSec) and academic sources.

This DSS is defined as a non-z

### AI 总结

总结生成失败

---

## 6. Implicit Midpoint Gradient Descent: Fast and Learning rate free convergence for Zero-Sum Games

- **作者**: Gaoqi Xue, James P. Bailey
- **发布日期**: 2026-07-10
- **链接**: [arXiv:2607.09950v1](https://arxiv.org/abs/2607.09950v1) | [PDF](https://arxiv.org/pdf/2607.09950v1)
- **分类**: cs.GT, math.OC
- **含金量**: 20/43 分

### 摘要

We study unconstrained bilinear zero-sum games, a fundamental model in online learning, adversarial optimization, and multi-agent decision-making.

We introduce the implicit midpoint gradient descent rule, which we derive from continuous-time follow-the-regularized leader dynamics via symplectic integration methods.

We prove that implicit midpoint gradient descent inherits several powerful properties from the continuous-time dynamics, including bounded orbits, fast ergodic convergence to Nash equilibria, and learning-rate-independent stability guarantees.

This is the first traditional online op

### AI 总结

总结生成失败

---

## 7. Dynamics and Convergences for Markov Coevolutionary Opinion Formation Games in Dynamic Social Networks

- **作者**: Po-An Chen, Chi-Jen Lu, Chuang-Chieh Lin, Jim Shi, Chih-Chieh Hung
- **发布日期**: 2026-07-06
- **链接**: [arXiv:2607.05580v2](https://arxiv.org/abs/2607.05580v2) | [PDF](https://arxiv.org/pdf/2607.05580v2)
- **分类**: cs.GT
- **含金量**: 20/43 分

### 摘要

While deterministic variants of the coevolutionary opinion formation games such as the K-Nearest Neighbor (K-NN) game, e.g., in Bhawalkar et al., in a dynamic social network can sometimes be shown to stabilize using potential functions or localized smoothness arguments, introducing stochasticity fundamentally changes the mathematical landscape.

In the "K-NN Markov game", network topologies evolve via a time-varying, randomized selection process.

Proving whether such a system, as a special case of general-sum Markov games, converges to an equilibrium is a profoundly non-obvious and challenging 

### AI 总结

总结生成失败

---

## 8. JEPA for AI-Native 6G: Predictive Representations and Open Challenges

- **作者**: Sheikh Salman Hassan, Irshad A. Meer, Almoatssimbillah Saifaldawla, Yan Kyaw Tun, Mustafa Ozger
- **发布日期**: 2026-07-09
- **链接**: [arXiv:2607.09798v1](https://arxiv.org/abs/2607.09798v1) | [PDF](https://arxiv.org/pdf/2607.09798v1)
- **分类**: cs.LG, cs.AI, cs.NI
- **含金量**: 20/43 分

### 摘要

Sixth-generation (6G) networks are moving toward AI-native operation, where learning modules are embedded across the radio access network (RAN), edge, and core.

This transition requires learning from limited labels, heterogeneous wireless and network data, partial observations, non-stationary propagation, and latency-constrained control loops.

Joint-embedding predictive architecture (JEPA) is a promising self-supervised paradigm for this setting because it predicts missing or future representations in latent space instead of reconstructing raw measurements or using contrastive negative samples

### AI 总结

总结生成失败

---

