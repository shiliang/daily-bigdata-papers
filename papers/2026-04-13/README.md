# 大数据+AI 领域论文日报

**日期**: 2026-04-13

**论文数量**: 7 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Verbalizing LLMs' assumptions to ex...](https://arxiv.org/abs/2604.03058v2) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Evolutionary Optimization Trumps Ad...](https://arxiv.org/abs/2511.03913v2) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Matrix-Game 3.0: Real-Time and Stre...](https://arxiv.org/abs/2604.08995v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Online3R: Online Learning for Consi...](https://arxiv.org/abs/2604.09480v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Online Quantile Regression for Nonp...](https://arxiv.org/abs/2604.08969v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Demystifying the Silence of Correct...](https://arxiv.org/abs/2604.08720v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [RAMP: Hybrid DRL for Online Learnin...](https://arxiv.org/abs/2604.08685v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Verbalizing LLMs' assumptions to explain and control sycophancy

- **作者**: Myra Cheng, Isabel Sieh, Humishka Zope, Sunny Yu, Lujain Ibrahim
- **发布日期**: 2026-04-03
- **链接**: [arXiv:2604.03058v2](https://arxiv.org/abs/2604.03058v2) | [PDF](https://arxiv.org/pdf/2604.03058v2)
- **分类**: cs.CL, cs.AI, cs.CY
- **含金量**: 20/43 分

### 摘要

LLMs can be socially sycophantic, affirming users when they ask questions like "am I in the wrong?" rather than providing genuine assessment.

We hypothesize that this behavior arises from incorrect assumptions about the user, like underestimating how often users are seeking information over reassurance.

We present Verbalized Assumptions, a framework for eliciting these assumptions from LLMs.

Verbalized Assumptions provide insight into LLM sycophancy, delusion, and other safety issues, e.g., the top bigram in LLMs' assumptions on social sycophancy datasets is ``seeking validation.'' We provide 

### AI 总结

总结生成失败

---

## 2. Evolutionary Optimization Trumps Adam Optimization on Embedding Space Exploration

- **作者**: Domício Pereira Neto, João Correia, Penousal Machado
- **发布日期**: 2025-11-05
- **链接**: [arXiv:2511.03913v2](https://arxiv.org/abs/2511.03913v2) | [PDF](https://arxiv.org/pdf/2511.03913v2)
- **分类**: cs.NE, cs.AI
- **含金量**: 20/43 分

### 摘要

Deep diffusion models have revolutionized image generation by producing high-quality outputs.

However, achieving specific objectives with these models often requires costly adaptations such as fine-tuning, which can be resource-intensive and time-consuming.

An alternative approach is inference-time control, which involves optimizing the prompt embeddings to guide the generation process without altering the model weights.

We explore prompt-embedding search optimization for the Stable Diffusion XL Turbo model, comparing a gradient-free evolutionary approach, the Separable Covariance Matrix Adapt

### AI 总结

总结生成失败

---

## 3. Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory

- **作者**: Zile Wang, Zexiang Liu, Jaixing Li, Kaichen Huang, Baixin Xu
- **发布日期**: 2026-04-10
- **链接**: [arXiv:2604.08995v1](https://arxiv.org/abs/2604.08995v1) | [PDF](https://arxiv.org/pdf/2604.08995v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

With the advancement of interactive video generation, diffusion models have increasingly demonstrated their potential as world models.

However, existing approaches still struggle to simultaneously achieve memory-enabled long-term temporal consistency and high-resolution real-time generation, limiting their applicability in real-world scenarios.

To address this, we present Matrix-Game 3.0, a memory-augmented interactive world model designed for 720p real-time longform video generation.

Building upon Matrix-Game 2.0, we introduce systematic improvements across data, model, and inference.

First, 

### AI 总结

总结生成失败

---

## 4. Online3R: Online Learning for Consistent Sequential Reconstruction Based on Geometry Foundation Model

- **作者**: Shunkai Zhou, Zike Yan, Fei Xue, Dong Wu, Yuchen Deng
- **发布日期**: 2026-04-10
- **链接**: [arXiv:2604.09480v1](https://arxiv.org/abs/2604.09480v1) | [PDF](https://arxiv.org/pdf/2604.09480v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

We present Online3R, a new sequential reconstruction framework that is capable of adapting to new scenes through online learning, effectively resolving inconsistency issues.

Specifically, we introduce a set of learnable lightweight visual prompts into a pretrained, frozen geometry foundation model to capture the knowledge of new environments while preserving the fundamental capability of the foundation model for geometry prediction.

To solve the problems of missing groundtruth and the requirement of high efficiency when updating these visual prompts at test time, we introduce a local-global se

### AI 总结

总结生成失败

---

## 5. Online Quantile Regression for Nonparametric Additive Models

- **作者**: Haoran Zhan
- **发布日期**: 2026-04-10
- **链接**: [arXiv:2604.08969v1](https://arxiv.org/abs/2604.08969v1) | [PDF](https://arxiv.org/pdf/2604.08969v1)
- **分类**: stat.ML, cs.LG, math.ST
- **含金量**: 20/43 分

### 摘要

This paper introduces a projected functional gradient descent algorithm (P-FGD) for training nonparametric additive quantile regression models in online settings.

This algorithm extends the functional stochastic gradient descent framework to the pinball loss.

An advantage of P-FGD is that it does not need to store historical data while maintaining $O(J_t\ln J_t)$ computational complexity per step where $J_t$ denotes the number of basis functions.

Besides, we only need $O(J_t)$ computational time for quantile function prediction at time $t$.

These properties show that P-FGD is much better than 

### AI 总结

总结生成失败

---

## 6. Demystifying the Silence of Correctness Bugs in PyTorch Compiler

- **作者**: Meiziniu Li, Dongze Li, Jianmeng Liu, Shing-Chi Cheung
- **发布日期**: 2026-04-09
- **链接**: [arXiv:2604.08720v1](https://arxiv.org/abs/2604.08720v1) | [PDF](https://arxiv.org/pdf/2604.08720v1)
- **分类**: cs.SE, cs.AI
- **含金量**: 20/43 分

### 摘要

Performance optimization of AI infrastructure is key to the fast adoption of large language models (LLMs).

The PyTorch compiler (torch.compile), a core optimization tool for deep learning (DL) models (including LLMs), has received due attention.

However, torch.compile is prone to correctness bugs, which cause incorrect outputs of compiled DL models without triggering exceptions, crashes, or warnings.

These bugs pose a serious threat to the reliability of downstream LLM applications.

Data from the PyTorch community shows that 19.2% of high-priority issues are incorrect outputs of compiled DL mo

### AI 总结

总结生成失败

---

## 7. RAMP: Hybrid DRL for Online Learning of Numeric Action Models

- **作者**: Yarin Benyamin, Argaman Mordoch, Shahaf S. Shperberg, Roni Stern
- **发布日期**: 2026-04-09
- **链接**: [arXiv:2604.08685v1](https://arxiv.org/abs/2604.08685v1) | [PDF](https://arxiv.org/pdf/2604.08685v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

Automated planning algorithms require an action model specifying the preconditions and effects of each action, but obtaining such a model is often hard.

Learning action models from observations is feasible, but existing algorithms for numeric domains are offline, requiring expert traces as input.

We propose the Reinforcement learning, Action Model learning, and Planning (RAMP) strategy for learning numeric planning action models online via interactions with the environment.

RAMP simultaneously trains a Deep Reinforcement Learning (DRL) policy, learns a numeric action model from past interactio

### AI 总结

总结生成失败

---

