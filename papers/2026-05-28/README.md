# 大数据+AI 领域论文日报

**日期**: 2026-05-28

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [How Far Can Disaggregation Go? A De...](https://arxiv.org/abs/2605.28302v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [CaMBRAIN: Real-time, Continuous EEG...](https://arxiv.org/abs/2605.28792v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [SARAD: LLM-Based Safety-Aware Hybri...](https://arxiv.org/abs/2605.28583v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [History-aware adaptive reduced-orde...](https://arxiv.org/abs/2605.28684v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Online Irregular Multivariate Time ...](https://arxiv.org/abs/2605.28603v1) | 待分析 | 评估失败 | [Code](https://github.com/HaonanWen/Under-Cali.) | 20/43 |
| 6 | [Self-Supervised Online Robot-Agnost...](https://arxiv.org/abs/2605.28442v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Exploratory Experience Shapes the G...](https://arxiv.org/abs/2605.27929v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Decentralized Parameter-Free Online...](https://arxiv.org/abs/2605.27831v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Learning to target with network int...](https://arxiv.org/abs/2605.27794v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [SiDP: Memory-Efficient Data Paralle...](https://arxiv.org/abs/2605.28095v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. How Far Can Disaggregation Go? A Design-Space Exploration of Attention-FFN Disaggregation for Efficient MoE LLM Serving

- **作者**: Hanjiang Wu, Abhimanyu Rajeshkumar Bambhaniya, Sarbartha Banerjee, Tuhin Khare, Sudarshan Srinivasan
- **发布日期**: 2026-05-27
- **链接**: [arXiv:2605.28302v1](https://arxiv.org/abs/2605.28302v1) | [PDF](https://arxiv.org/pdf/2605.28302v1)
- **分类**: cs.LG, cs.AI, cs.DC
- **含金量**: 20/43 分

### 摘要

Modern large language model (LLM) inference has progressively disaggregated to keep pace with growing model sizes and tight TTFT and TPOT service-level objectives: from chunked-prefill aggregation, to prefill-decode (P/D) disaggregation, and most recently to operator-level Attention-FFN Disaggregation (AFD).

This trend is especially important for mixture-of-experts (MoE) models, where memory-bound attention, compute-intensive expert FFNs, and MoE dispatch/combine communication create distinct resource demands.

AFD further exposes this heterogeneity by placing attention and MoE-FFN execution on

### AI 总结

总结生成失败

---

## 2. CaMBRAIN: Real-time, Continuous EEG Inference with Causal State Space Models

- **作者**: Abhilash Durgam, Nyle Siddiqui, Jeffrey A. Chan-Santiago, Qiushi Fu, Elakkat D. Gireesh
- **发布日期**: 2026-05-27
- **链接**: [arXiv:2605.28792v1](https://arxiv.org/abs/2605.28792v1) | [PDF](https://arxiv.org/pdf/2605.28792v1)
- **分类**: cs.AI, cs.HC, cs.LG
- **含金量**: 20/43 分

### 摘要

Electroencephalography (EEG) is a critical, non-invasive method to monitor electrical brain activity.

EEGs can span anywhere from a couple seconds to multiple hours, posing a major hurdle for existing deep learning methods due to two major factors: (1) existing EEG models are predominantly built upon the attention mechanism, incurring quadratic scaling as the sequence length increases, and (2) raw EEG signals must be processed in a sliding-window fashion due to fixed-length input requirements, preventing global understanding of the entire signal.

To this extent, we propose CaMBRAIN - the first

### AI 总结

总结生成失败

---

## 3. SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving

- **作者**: Kangyu Wu, Peng Cui, Guoxi Chen, Ya Zhang
- **发布日期**: 2026-05-27
- **链接**: [arXiv:2605.28583v1](https://arxiv.org/abs/2605.28583v1) | [PDF](https://arxiv.org/pdf/2605.28583v1)
- **分类**: cs.RO, cs.AI, cs.LG, eess.SY
- **含金量**: 20/43 分

### 摘要

Ensuring both safety and efficiency in decision-making for autonomous driving systems remains a fundamental challenge.

Traditional Deep Reinforcement Learning (DRL) suffers from unsafe random exploration and slow convergence, while Large Language Models (LLMs) demonstrate inherent latency in real-time inference operations.

To address these limitations, this paper proposes SARAD, a novel safety-aware hybrid framework that synergizes LLMs and DRL for autonomous driving.

SARAD substitutes the random exploration of DRL with Retrieval-Augmented Generation (RAG)-enhanced, LLM-guided decisions source

### AI 总结

总结生成失败

---

## 4. History-aware adaptive reduced-order models via incremental singular value decomposition

- **作者**: Amirpasha Hedayat, Ali Mohaghegh, Laura Balzano, Cheng Huang, Karthik Duraisamy
- **发布日期**: 2026-05-27
- **链接**: [arXiv:2605.28684v1](https://arxiv.org/abs/2605.28684v1) | [PDF](https://arxiv.org/pdf/2605.28684v1)
- **分类**: cs.LG, cs.CE, math.NA, physics.comp-ph
- **含金量**: 20/43 分

### 摘要

Reduced-order models (ROMs) can accelerate high-dimensional dynamical simulations, but their accuracy often deteriorates when online dynamics leave the regime represented by offline training data.

We develop a projection-based adaptive ROM framework based on incremental singular value decomposition (iSVD), in which occasional full-order operator evaluations provide correction snapshots for online basis updates.

The intrusive ROMs considered here are fully parameterized by the basis, so each update naturally propagates to reduced operators and hyper-reduction machinery.

Through its evolving sin

### AI 总结

总结生成失败

---

## 5. Online Irregular Multivariate Time Series Forecasting via Uncertainty-Driven Dual-Expert Calibration

- **作者**: Haonan Wen, Hanyang Chen, Songhe Feng
- **发布日期**: 2026-05-27
- **链接**: [arXiv:2605.28603v1](https://arxiv.org/abs/2605.28603v1) | [PDF](https://arxiv.org/pdf/2605.28603v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/HaonanWen/Under-Cali.) ⭐ 0

### 摘要

Irregular multivariate time series forecasting is critical in many real-world applications, where time series are irregularly sampled and exhibit dynamically evolving missingness patterns.

Although existing methods perform well in offline settings, they often suffer from significant performance degradation when deployed online due to dynamic shifts in data distribution.

Maintaining forecasting capability in such dynamic scenarios typically necessitates online adaptation techniques.

Since irregular sampling fundamentally undermines temporal continuity and periodicity, we cannot leverage these w

### AI 总结

总结生成失败

---

## 6. Self-Supervised Online Robot-Agnostic Traversability Estimation for Open-World Environments

- **作者**: Julia Hindel, Simon Bultmann, Houman Masnavi, Daniele Cattaneo, Abhinav Valada
- **发布日期**: 2026-05-27
- **链接**: [arXiv:2605.28442v1](https://arxiv.org/abs/2605.28442v1) | [PDF](https://arxiv.org/pdf/2605.28442v1)
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

## 7. Exploratory Experience Shapes the Geometry of Predictive Representations

- **作者**: Kseniia Shilova, Abdelrahman Sharafeldin, Advay Balakrishnan, Hannah Choi
- **发布日期**: 2026-05-27
- **链接**: [arXiv:2605.27929v1](https://arxiv.org/abs/2605.27929v1) | [PDF](https://arxiv.org/pdf/2605.27929v1)
- **分类**: q-bio.NC, cs.LG
- **含金量**: 20/43 分

### 摘要

Active sensing links behavior and learning through an action-perception loop: actions determine the observations used to update internal predictive models of perception, which subsequently guide the next actions.

Predictive-coding frameworks provide a natural way to model this process, since internal representations are continuously updated to predict future observations.

Here, we ask how exploratory and exploitative behavioral strategies shape these internal predictive representations.

We build an online learning agent in a tree-like maze with a controllable parameter regulating the balance b

### AI 总结

总结生成失败

---

## 8. Decentralized Parameter-Free Online Learning with Compressed Gossip

- **作者**: Tomas Ortega, Hamid Jafarkhani
- **发布日期**: 2026-05-27
- **链接**: [arXiv:2605.27831v1](https://arxiv.org/abs/2605.27831v1) | [PDF](https://arxiv.org/pdf/2605.27831v1)
- **分类**: cs.LG, eess.SP, math.OC
- **含金量**: 20/43 分

### 摘要

We study decentralized online convex optimization when agents communicate over a graph and messages may be compressed.

Classical decentralized online methods typically require learning-rate choices that depend on the horizon, comparator scale, or other problem parameters, while compressed communication introduces additional disagreement that must be controlled.

We propose DECO-EF (DEcentralized COin-betting with Error Feedback), a decentralized parameter-free online learning algorithm that combines coin-betting predictions with compressed difference-based gossip.

Each agent maintains a clean a

### AI 总结

总结生成失败

---

## 9. Learning to target with network interference

- **作者**: Xiaomeng Wang, Hamsa Bastani, Osbert Bastani, Zhimei Ren
- **发布日期**: 2026-05-27
- **链接**: [arXiv:2605.27794v1](https://arxiv.org/abs/2605.27794v1) | [PDF](https://arxiv.org/pdf/2605.27794v1)
- **分类**: stat.ML, cs.LG, stat.ME
- **含金量**: 20/43 分

### 摘要

This paper studies adaptive targeting under network interference in a bandit setting, where treatments applied to one individual may affect others through spillover effects.

We consider a linear model in a sparse regime, where each individual's outcome can be affected by at most a few others.

We first establish a regret lower bound showing that ignoring the network structure and reducing the problem to a standard linear bandit inevitably leads to inefficient learning, particularly in large populations.

To understand how structural information can be leveraged, we analyze regimes with varying l

### AI 总结

总结生成失败

---

## 10. SiDP: Memory-Efficient Data Parallelism for Offline LLM Inference

- **作者**: Alan Zhao, Cyril Y. He
- **发布日期**: 2026-05-27
- **链接**: [arXiv:2605.28095v1](https://arxiv.org/abs/2605.28095v1) | [PDF](https://arxiv.org/pdf/2605.28095v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

The rapid adoption of large language models (LLMs) has shifted a substantial portion of inference workloads into throughput-oriented offline regimes, where fully utilizing GPU compute requires large batch sizes.

However, existing deployments face a structural tension.

Data parallelism (DP) scales throughput well but replicates model weights, leaving limited GPU memory for key-value (KV) cache and constraining batch size.

Model parallelism reduces per-device weights, but requires fine-grained synchronization that erodes DP's independence and scheduling flexibility.

We present SiDP, a memory-eff

### AI 总结

总结生成失败

---

