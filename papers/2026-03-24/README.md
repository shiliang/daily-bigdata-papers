# 大数据+AI 领域论文日报

**日期**: 2026-03-24

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Counterfactual Credit Policy Optimi...](https://arxiv.org/abs/2603.21563v1) | 待分析 | 评估失败 | [Code](https://github.com/bhai114/ccpo.) | 20/43 |
| 2 | [FGIM: a Fast Graph-based Indexes Me...](https://arxiv.org/abs/2603.21710v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Calibeating Made Simple](https://arxiv.org/abs/2603.22167v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Constrained Online Convex Optimizat...](https://arxiv.org/abs/2603.21375v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [CLT-Forge: A Scalable Library for C...](https://arxiv.org/abs/2603.21014v1) | 待分析 | 评估失败 | [Code](https://github.com/LLM-Interp/CLT-Forge.) | 20/43 |
| 6 | [Optimal low-rank stochastic gradien...](https://arxiv.org/abs/2603.20632v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [High-dimensional online learning vi...](https://arxiv.org/abs/2603.20696v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Revenue-Sharing as Infrastructure: ...](https://arxiv.org/abs/2603.20533v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [A cellular automaton model for ther...](https://arxiv.org/abs/2603.20522v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Articulated-Body Dynamics Network: ...](https://arxiv.org/abs/2603.19078v2) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Counterfactual Credit Policy Optimization for Multi-Agent Collaboration

- **作者**: Zhongyi Li, Wan Tian, Yikun Ban, Jinju Chen, Huiming Zhang
- **发布日期**: 2026-03-23
- **链接**: [arXiv:2603.21563v1](https://arxiv.org/abs/2603.21563v1) | [PDF](https://arxiv.org/pdf/2603.21563v1)
- **分类**: cs.AI
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/bhai114/ccpo.) ⭐ 0

### 摘要

Collaborative multi-agent large language models (LLMs) can solve complex reasoning tasks by decomposing roles and aggregating diverse hypotheses.

Yet, reinforcement learning (RL) for such systems is often undermined by credit assignment: a shared global reward obscures individual contributions, inflating update variance and encouraging free-riding.

We introduce Counterfactual Credit Policy Optimization (CCPO), a framework that assigns agent-specific learning signals by estimating each agent's marginal contribution through counterfactual trajectories.

CCPO builds dynamic counterfactual baseline

### AI 总结

总结生成失败

---

## 2. FGIM: a Fast Graph-based Indexes Merging Framework for Approximate Nearest Neighbor Search

- **作者**: Zekai Wu, Jiabao Jin, Peng Cheng, Xiaoyao Zhong, Lei Chen
- **发布日期**: 2026-03-23
- **链接**: [arXiv:2603.21710v1](https://arxiv.org/abs/2603.21710v1) | [PDF](https://arxiv.org/pdf/2603.21710v1)
- **分类**: cs.DB
- **含金量**: 20/43 分

### 摘要

As the state-of-the-art methods for high-dimensional data retrieval, Approximate Nearest Neighbor Search (ANNS) approaches with graph-based indexes have attracted increasing attention and play a crucial role in many real-world applications, e.g., retrieval-augmented generation (RAG) and recommendation systems.

Unlike the extensive works focused on designing efficient graph-based ANNS methods, this paper delves into merging multiple existing graph-based indexes into a single one, which is also crucial in many real-world scenarios (e.g., cluster consolidation in distributed systems and read-writ

### AI 总结

总结生成失败

---

## 3. Calibeating Made Simple

- **作者**: Yurong Chen, Zhiyi Huang, Michael I. Jordan, Haipeng Luo
- **发布日期**: 2026-03-23
- **链接**: [arXiv:2603.22167v1](https://arxiv.org/abs/2603.22167v1) | [PDF](https://arxiv.org/pdf/2603.22167v1)
- **分类**: cs.LG, cs.AI, cs.GT, econ.TH
- **含金量**: 20/43 分

### 摘要

We study calibeating, the problem of post-processing external forecasts online to minimize cumulative losses and match an informativeness-based benchmark.

Unlike prior work, which analyzed calibeating for specific losses with specific arguments, we reduce calibeating to existing online learning techniques and obtain results for general proper losses.

More concretely, we first show that calibeating is minimax-equivalent to regret minimization.

This recovers the $O(\log T)$ calibeating rate of Foster and Hart [FH23] for the Brier and log losses and its optimality, and yields new optimal calibeat

### AI 总结

总结生成失败

---

## 4. Constrained Online Convex Optimization with Memory and Predictions

- **作者**: Mohammed Abdullah, George Iosifidis, Salah Eddine Elayoubi, Tijani Chahed
- **发布日期**: 2026-03-22
- **链接**: [arXiv:2603.21375v1](https://arxiv.org/abs/2603.21375v1) | [PDF](https://arxiv.org/pdf/2603.21375v1)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

We study Constrained Online Convex Optimization with Memory (COCO-M), where both the loss and the constraints depend on a finite window of past decisions made by the learner.

This setting extends the previously studied unconstrained online optimization with memory framework and captures practical problems such as the control of constrained dynamical systems and scheduling with reconfiguration budgets.

For this problem, we propose the first algorithms that achieve sublinear regret and sublinear cumulative constraint violation under time-varying constraints, both with and without predictions of 

### AI 总结

总结生成失败

---

## 5. CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs

- **作者**: Florent Draye, Abir Harrasse, Vedant Palit, Tung-Yu Wu, Jiarui Liu
- **发布日期**: 2026-03-22
- **链接**: [arXiv:2603.21014v1](https://arxiv.org/abs/2603.21014v1) | [PDF](https://arxiv.org/pdf/2603.21014v1)
- **分类**: cs.LG, cs.CL
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/LLM-Interp/CLT-Forge.) ⭐ 0

### 摘要

Mechanistic interpretability seeks to understand how Large Language Models (LLMs) represent and process information.

Recent approaches based on dictionary learning and transcoders enable representing model computation in terms of sparse, interpretable features and their interactions, giving rise to feature attribution graphs.

However, these graphs are often large and redundant, limiting their interpretability in practice.

Cross-Layer Transcoders (CLTs) address this issue by sharing features across layers while preserving layer-specific decoding, yielding more compact representations, but remai

### AI 总结

总结生成失败

---

## 6. Optimal low-rank stochastic gradient estimation for LLM training

- **作者**: Zehao Li, Tao Ren, Zishi Zhang, Xi Chen, Yijie Peng
- **发布日期**: 2026-03-21
- **链接**: [arXiv:2603.20632v1](https://arxiv.org/abs/2603.20632v1) | [PDF](https://arxiv.org/pdf/2603.20632v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Large language model (LLM) training is often bottlenecked by memory constraints and stochastic gradient noise in extremely high-dimensional parameter spaces.

Motivated by empirical evidence that many LLM gradient matrices are effectively low-rank during training, we present an unbiased, memory-efficient, low-rank matrix estimator with the lowest variance that is applicable across common stochastic gradient estimation paradigms.

The core idea is to project a high-dimensional stochastic gradient estimator onto a random low-dimensional subspace and lift it back, reducing memory while keeping the 

### AI 总结

总结生成失败

---

## 7. High-dimensional online learning via asynchronous decomposition: Non-divergent results, dynamic regularization, and beyond

- **作者**: Shixiang Liu, Zhifan Li, Hanming Yang, Jianxin Yin
- **发布日期**: 2026-03-21
- **链接**: [arXiv:2603.20696v1](https://arxiv.org/abs/2603.20696v1) | [PDF](https://arxiv.org/pdf/2603.20696v1)
- **分类**: stat.ML, cs.LG
- **含金量**: 20/43 分

### 摘要

Existing high-dimensional online learning methods often face the challenge that their error bounds, or per-batch sample sizes, diverge as the number of data batches increases.

To address this issue, we propose an asynchronous decomposition framework that leverages summary statistics to construct a surrogate score function for current-batch learning.

This framework is implemented via a dynamic-regularized iterative hard thresholding algorithm, providing a computationally and memory-efficient solution for sparse online optimization.

We provide a unified theoretical analysis that accounts for bot

### AI 总结

总结生成失败

---

## 8. Revenue-Sharing as Infrastructure: A Distributed Business Model for Generative AI Platforms

- **作者**: Ghislain Dorian Tchuente Mondjo
- **发布日期**: 2026-03-20
- **链接**: [arXiv:2603.20533v1](https://arxiv.org/abs/2603.20533v1) | [PDF](https://arxiv.org/pdf/2603.20533v1)
- **分类**: cs.CY, cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

Generative AI platforms (Google AI Studio, OpenAI, Anthropic) provide infrastructures (APIs, models) that are transforming the application development ecosystem.

Recent literature distinguishes three generations of business models: a first generation modeled on cloud computing (pay-per-use), a second characterized by diversification (freemium, subscriptions), and a third, emerging generation exploring multi-layer market architectures with revenue-sharing mechanisms.

Despite these advances, current models impose a financial barrier to entry for developers, limiting innovation and excluding acto

### AI 总结

总结生成失败

---

## 9. A cellular automaton model for thermal transport in low-dimensional systems

- **作者**: Alejandra León
- **发布日期**: 2026-03-20
- **链接**: [arXiv:2603.20522v1](https://arxiv.org/abs/2603.20522v1) | [PDF](https://arxiv.org/pdf/2603.20522v1)
- **分类**: cond-mat.mes-hall
- **含金量**: 20/43 分

### 摘要

In this work, we formulate a theoretical model based on a cellular automaton (CA) to study thermal transport in low-dimensional nanostructures across ballistic, diffusive, and transition regimes.

Unlike computationally intensive methods such as the Boltzmann Transport Equation (BTE), our model stands out for its geometrical robustness, allowing the seamless integration of substitutional impurities, vacancies, and irregular edges.

We validated the model using graphene nanoribbons (AGNRs), successfully replicating the dependence of thermal conductivity on ribbon width and temperature.

Results de

### AI 总结

总结生成失败

---

## 10. Articulated-Body Dynamics Network: Dynamics-Grounded Prior for Robot Learning

- **作者**: Sangwoo Shin, Kunzhao Ren, Xiaobin Xiong, Josiah P. Hanna
- **发布日期**: 2026-03-19
- **链接**: [arXiv:2603.19078v2](https://arxiv.org/abs/2603.19078v2) | [PDF](https://arxiv.org/pdf/2603.19078v2)
- **分类**: cs.RO
- **含金量**: 20/43 分

### 摘要

Recent work in reinforcement learning has shown that incorporating structural priors for articulated robots, such as link connectivity, into policy networks improves learning efficiency.

However, dynamics properties, despite their fundamental role in determining how forces and motion propagate through the body, remain largely underexplored as an inductive bias for policy learning.

To address this gap, we present the Articulated-Body Dynamics Network (ABD-Net), a novel graph neural network architecture grounded in the computational structure of forward dynamics.

Specifically, we adapt the inert

### AI 总结

总结生成失败

---

