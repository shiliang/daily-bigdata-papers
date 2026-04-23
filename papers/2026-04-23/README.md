# 大数据+AI 领域论文日报

**日期**: 2026-04-23

**论文数量**: 8 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Surrogate modeling for interpreting...](https://arxiv.org/abs/2604.20331v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [LLM-guided phase diagram constructi...](https://arxiv.org/abs/2604.20304v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [TREX: Automating LLM Fine-tuning vi...](https://arxiv.org/abs/2604.14116v2) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Do We Still Need Humans in the Loop...](https://arxiv.org/abs/2604.13899v2) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [FSFM: A Biologically-Inspired Frame...](https://arxiv.org/abs/2604.20300v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [A GPU-Accelerated Framework for Mul...](https://arxiv.org/abs/2604.20121v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Online Survival Analysis: A Bandit ...](https://arxiv.org/abs/2604.20296v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Super Apriel: One Checkpoint, Many ...](https://arxiv.org/abs/2604.19877v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Surrogate modeling for interpreting black-box LLMs in medical predictions

- **作者**: Changho Han, Songsoo Kim, Dong Won Kim, Leo Anthony Celi, Jaewoong Kim
- **发布日期**: 2026-04-22
- **链接**: [arXiv:2604.20331v1](https://arxiv.org/abs/2604.20331v1) | [PDF](https://arxiv.org/pdf/2604.20331v1)
- **分类**: cs.CL, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

Large language models (LLMs), trained on vast datasets, encode extensive real-world knowledge within their parameters, yet their black-box nature obscures the mechanisms and extent of this encoding.

Surrogate modeling, which uses simplified models to approximate complex systems, can offer a path toward better interpretability of black-box models.

We propose a surrogate modeling framework that quantitatively explains LLM-encoded knowledge.

For a specific hypothesis derived from domain knowledge, this framework approximates the latent LLM knowledge space using observable elements (input-output p

### AI 总结

总结生成失败

---

## 2. LLM-guided phase diagram construction through high-throughput experimentation

- **作者**: Ryo Tamura, Haruhiko Morito, Yuna Oikawa, Guillaume Deffrennes, Shoichi Matsuda
- **发布日期**: 2026-04-22
- **链接**: [arXiv:2604.20304v1](https://arxiv.org/abs/2604.20304v1) | [PDF](https://arxiv.org/pdf/2604.20304v1)
- **分类**: cond-mat.mtrl-sci, cs.AI
- **含金量**: 20/43 分

### 摘要

Constructing phase diagrams for multicomponent alloys requires extensive experimental measurements and is a time-consuming task.

Here we investigate whether large language models (LLMs) can guide experimental planning for phase diagram construction.

In our framework, a general-purpose LLM serves as the experimental planner, suggesting compositions for measurement at each cycle in a closed loop with high-throughput synthesis and X-ray diffraction phase identification.

Using this framework, we experimentally constructed the ternary phase diagram of the Co-Al-Ge system at 900 degree C through ite

### AI 总结

总结生成失败

---

## 3. TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration

- **作者**: Zerun Ma, Guoqiang Wang, Xinchen Xie, Yicheng Chen, He Du
- **发布日期**: 2026-04-15
- **链接**: [arXiv:2604.14116v2](https://arxiv.org/abs/2604.14116v2) | [PDF](https://arxiv.org/pdf/2604.14116v2)
- **分类**: cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

While Large Language Models (LLMs) have empowered AI research agents to perform isolated scientific tasks, automating complex, real-world workflows, such as LLM training, remains a significant challenge.

In this paper, we introduce TREX, a multi-agent system that automates the entire LLM training life-cycle.

By orchestrating collaboration between two core modules-the Researcher and the Executor-the system seamlessly performs requirement analysis, open-domain literature and data research, formulation of training strategies, preparation of data recipes, and model training and evaluation.

The mul

### AI 总结

总结生成失败

---

## 4. Do We Still Need Humans in the Loop? Comparing Human and LLM Annotation in Active Learning for Hostility Detection

- **作者**: Ahmad Dawar Hakimi, Lea Hirlimann, Isabelle Augenstein, Hinrich Schütze
- **发布日期**: 2026-04-15
- **链接**: [arXiv:2604.13899v2](https://arxiv.org/abs/2604.13899v2) | [PDF](https://arxiv.org/pdf/2604.13899v2)
- **分类**: cs.CL, cs.AI
- **含金量**: 20/43 分

### 摘要

Instruction-tuned LLMs can annotate thousands of instances from a short prompt at negligible cost.

This raises two questions for active learning (AL): can LLM labels replace human labels within the AL loop, and does AL remain necessary when entire corpora can be labelled at once? We investigate both questions on a new dataset of 277,902 German political TikTok comments (25,974 LLM-labelled, 5,000 human-annotated), comparing seven annotation strategies across four encoders to detect anti-immigrant hostility.

A classifier trained on 25,974 GPT-5.2 labels (\$43) achieves comparable F1-Macro to on

### AI 总结

总结生成失败

---

## 5. FSFM: A Biologically-Inspired Framework for Selective Forgetting of Agent Memory

- **作者**: Yingjie Gu, Bo Xiong, Yijuan Guo, Chao Li, Xiaojing Zhang
- **发布日期**: 2026-04-22
- **链接**: [arXiv:2604.20300v1](https://arxiv.org/abs/2604.20300v1) | [PDF](https://arxiv.org/pdf/2604.20300v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

For LLM agents, memory management critically impacts efficiency, quality, and security.

While much research focuses on retention, selective forgetting--inspired by human cognitive processes (hippocampal indexing/consolidation theory and Ebbinghaus forgetting curve)--remains underexplored.

We argue that in resource-constrained environments, a well-designed forgetting mechanism is as crucial as remembering, delivering benefits across three dimensions: (1) efficiency via intelligent memory pruning, (2) quality by dynamically updating outdated preferences and context, and (3) security through acti

### AI 总结

总结生成失败

---

## 6. A GPU-Accelerated Framework for Multi-Attribute Range Filtered Approximate Nearest Neighbor Search

- **作者**: Zhonggen Li, Haoran Yu, Yifan Zhu, Yunjun Gao
- **发布日期**: 2026-04-22
- **链接**: [arXiv:2604.20121v1](https://arxiv.org/abs/2604.20121v1) | [PDF](https://arxiv.org/pdf/2604.20121v1)
- **分类**: cs.DB
- **含金量**: 20/43 分

### 摘要

Range-filtered approximate nearest neighbor search (RFANNS) is increasingly critical for modern vector databases.

However, existing solutions suffer from severe index inflation and construction overhead.

Furthermore, they rely exclusively on CPUs for the heavy indexing and query processing, failing to leverage the powerful computational capabilities of GPUs.

In this paper, we present Garfield, a GPU-accelerated framework for multi-attribute range filtered ANNS that overcomes these bottlenecks through designing a lightweight index structure and hardware-aware execution pipeline.

Garfield introd

### AI 总结

总结生成失败

---

## 7. Online Survival Analysis: A Bandit Approach under Cox PH Model

- **作者**: Yang Xu, Wenbin Lu, Rui Song
- **发布日期**: 2026-04-22
- **链接**: [arXiv:2604.20296v1](https://arxiv.org/abs/2604.20296v1) | [PDF](https://arxiv.org/pdf/2604.20296v1)
- **分类**: stat.ML, cs.LG
- **含金量**: 20/43 分

### 摘要

Survival analysis is a widely used statistical framework for modeling time-to-event data under censoring.

Classical methods, such as the Cox proportional hazards (Cox PH) model, offer a semiparametric approach to estimating the effects of covariates on the hazard function.

Despite its importance, survival analysis has been largely unexplored in online settings, particularly within the bandit framework, where decisions must be made sequentially to optimize treatments as new data arrive over time.

In this work, we take an initial step toward integrating survival analysis into a purely online lea

### AI 总结

总结生成失败

---

## 8. Super Apriel: One Checkpoint, Many Speeds

- **作者**: SLAM Labs, :, Oleksiy Ostapenko, Raymond Li, Torsten Scholak
- **发布日期**: 2026-04-21
- **链接**: [arXiv:2604.19877v1](https://arxiv.org/abs/2604.19877v1) | [PDF](https://arxiv.org/pdf/2604.19877v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

We release Super Apriel, a 15B-parameter supernet in which every decoder layer provides four trained mixer choices -- Full Attention (FA), Sliding Window Attention (SWA), Kimi Delta Attention (KDA), and Gated DeltaNet (GDN).

A placement selects one mixer per layer; placements can be switched between requests at serving time without reloading weights, enabling multiple speed presets from a single checkpoint.

The shared checkpoint also enables speculative decoding without a separate draft model.

The all-FA preset matches the Apriel 1.6 teacher on all reported benchmarks; recommended hybrid prese

### AI 总结

总结生成失败

---

