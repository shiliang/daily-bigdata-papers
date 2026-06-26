# 大数据+AI 领域论文日报

**日期**: 2026-06-26

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [DMuon: Efficient Distributed Muon T...](https://arxiv.org/abs/2606.27153v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Simulating Unified Tensor Reshardin...](https://arxiv.org/abs/2606.26633v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Mask to Concept: Auto-Promptable SA...](https://arxiv.org/abs/2606.26711v1) | 待分析 | 评估失败 | [Code](https://github.com/Huster-Hq/M2C.) | 20/43 |
| 4 | [Does AI Reviewer See the Full Pictu...](https://arxiv.org/abs/2606.12716v2) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Simulation-based inference for rapi...](https://arxiv.org/abs/2606.27286v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Blackwell Approachability and Gradi...](https://arxiv.org/abs/2606.27315v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Jailbreaking for the Average Jane: ...](https://arxiv.org/abs/2606.26936v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Asymptotically Optimal Learning for...](https://arxiv.org/abs/2606.26893v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Learning to Fold: prizewinning solu...](https://arxiv.org/abs/2606.27163v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Hybrid privacy-aware semantic searc...](https://arxiv.org/abs/2606.26373v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. DMuon: Efficient Distributed Muon Training with Near-Adam Overhead

- **作者**: Vincent Chen, Starrick Liu, Regis Cheng, Dance Yang, Shalfun Li
- **发布日期**: 2026-06-25
- **链接**: [arXiv:2606.27153v1](https://arxiv.org/abs/2606.27153v1) | [PDF](https://arxiv.org/pdf/2606.27153v1)
- **分类**: cs.DC, cs.LG
- **含金量**: 20/43 分

### 摘要

Matrix-orthogonalization-based optimizers, exemplified by Muon, have demonstrated strong convergence behavior across a wide range of modern deep learning workloads.

The matrix-aware updates offer a compelling alternative to conventional element-wise optimization, particularly as model architectures continue to grow in scale and heterogeneity.

Yet contemporary distributed training infrastructure built around the assumption of element-wise optimizers is poorly matched to matrix-level optimizers such as Muon, whose updates couple entire weight matrices and require costly Newton-Schulz iterations.

### AI 总结

总结生成失败

---

## 2. Simulating Unified Tensor Resharding in heterogeneous AI systems

- **作者**: Sumit Kumar, Sayantan Dasgupta, Kushal Mitra, Meet Dadhania, Rohan Sudhir Basugade
- **发布日期**: 2026-06-25
- **链接**: [arXiv:2606.26633v1](https://arxiv.org/abs/2606.26633v1) | [PDF](https://arxiv.org/pdf/2606.26633v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

State-of-the-art AI training simulators assume homogeneous compute and network infrastructure.

However, real-world training infrastructure is becoming increasingly heterogeneous since: (a) Model architectures such as multimodal and MoE exploit heterogeneity to improve device utilization, (b) Public cloud platforms often provide limited availability of homogeneous hardware due to fast hardware evolution, and (c) Large enterprises frequently deploy geographically distributed infrastructure that is both diverse and heterogeneous.

In this paper, we present Xsim, a heterogeneity-aware simulator for

### AI 总结

总结生成失败

---

## 3. Mask to Concept: Auto-Promptable SAM3 via Efficient Test-Time Concept Embedding Search for Few-Shot Annotation

- **作者**: Quan Zhou, Shaoqing Zhai, Qiang Hu Jia Chen, Qiang Li, Zhiwei Wang
- **发布日期**: 2026-06-25
- **链接**: [arXiv:2606.26711v1](https://arxiv.org/abs/2606.26711v1) | [PDF](https://arxiv.org/pdf/2606.26711v1)
- **分类**: cs.CV
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/Huster-Hq/M2C.) ⭐ 0

### 摘要

Transforming foundation segmentation models from human-prompted tools into auto-promptable annotators is critical for scalable medical data annotation.

Current methods commonly depend on external feature matchers or auxiliary networks to automate geometric prompting, but introducing architectural overhead and limiting performance scalability.

Although SAM3 natively supports concept segmentation via reusable text prompts, its direct use in medical imaging is hindered by a lack of fine-grained clinical knowledge and the ambiguity of human-written descriptions.

In this work, we propose Mask to Co

### AI 总结

总结生成失败

---

## 4. Does AI Reviewer See the Full Picture? Attacking and Defending Multimodal Peer Review

- **作者**: Xinyu Zhao, Rana Muhammad Shahroz Khan, Zhen Xu, Zhen Tan, Tianlong Chen
- **发布日期**: 2026-06-10
- **链接**: [arXiv:2606.12716v2](https://arxiv.org/abs/2606.12716v2) | [PDF](https://arxiv.org/pdf/2606.12716v2)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

The integration of Large Language Models (LLMs) and Multimodal LLMs (MLLMs) into scientific peer-review workflows introduces novel and significant risks for adversarial manipulation, especially given the multimodal nature of scientific papers where figures, not just text, convey core evidence.

This creates a significant gap: current robustness studies on AI peer-review are overwhelmingly text-only.

Moreover, the problem is distinct from standard jailbreaking, as a peer-review attack seeks to induce a domain-specific, targeted failure (e.g., "inflate this score") rather than a general safety po

### AI 总结

总结生成失败

---

## 5. Simulation-based inference for rapid Bayesian parameter estimation in epidemiological models: a comparison with MCMC

- **作者**: Alina Bazarova, Johann Fredrik Jadebeck, Henrik Zunker, Carolina J. Klett-Tammen, Torben Heinsohn
- **发布日期**: 2026-06-25
- **链接**: [arXiv:2606.27286v1](https://arxiv.org/abs/2606.27286v1) | [PDF](https://arxiv.org/pdf/2606.27286v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

Mechanistic epidemiological models are widely used to support infectious disease forecasting and public-health decision making.

Bayesian calibration of such models is commonly performed using Markov chain Monte Carlo (MCMC), which can become computationally expensive for high-dimensional nonlinear systems and repeated near-real-time analyses.

Here, we investigate simulation-based inference (SBI) using neural posterior estimation as a scalable alternative for Bayesian calibration of a mechanistic SECIR epidemiological model using COVID-19 intensive care unit (ICU) occupancy data from Germany du

### AI 总结

总结生成失败

---

## 6. Blackwell Approachability and Gradient Equilibrium are Equivalent

- **作者**: Brian W. Lee, Nika Haghtalab, Michael I. Jordan, Ryan J. Tibshirani
- **发布日期**: 2026-06-25
- **链接**: [arXiv:2606.27315v1](https://arxiv.org/abs/2606.27315v1) | [PDF](https://arxiv.org/pdf/2606.27315v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Gradient equilibrium (GEQ) is a recently introduced online optimization framework that generalizes first-order stationarity from offline optimization and abstracts problems like online conformal prediction.

While GEQ has curious similarities with known online learning frameworks, namely regret minimization, prior work has shown that GEQ error and regret are incomparable objectives, leaving open a precise understanding of how GEQ fits into the broader online learning landscape.

In this work, we show that GEQ is equivalent to Blackwell approachability in the algorithmic sense.

That is, a Blackwe

### AI 总结

总结生成失败

---

## 7. Jailbreaking for the Average Jane: Choosing Optimal Jailbreaks via Bandit Algorithms for Automatically Enhanced Queries

- **作者**: Prarabdh Shukla,  Ritik, Suhas Rao, Arpit Agarwal, Arjun Bhagoji
- **发布日期**: 2026-06-25
- **链接**: [arXiv:2606.26936v1](https://arxiv.org/abs/2606.26936v1) | [PDF](https://arxiv.org/pdf/2606.26936v1)
- **分类**: cs.CR, cs.CL, cs.LG
- **含金量**: 20/43 分

### 摘要

With a profusion of jailbreaks for LLMs now widely known, a growing concern is that non-expert malicious actors ("the average Jane") could elicit actionable responses to malicious requests.

In this work, we examine whether this concern is justified.

A non-expert malicious actor requires two ingredients for a successful attack: a powerful jailbreak for their target model, acting on an effective malicious query.

For the former, we propose a novel attack strategy based on the multi-armed bandit framework.

This allows efficient online learning of the optimal jailbreak from a large choice set via n

### AI 总结

总结生成失败

---

## 8. Asymptotically Optimal Learning for Parametric Prophet Inequalities

- **作者**: Jung-hun Kim, Anna Grebennikova, Vianney Perchet
- **发布日期**: 2026-06-25
- **链接**: [arXiv:2606.26893v1](https://arxiv.org/abs/2606.26893v1) | [PDF](https://arxiv.org/pdf/2606.26893v1)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

We study learning in prophet inequalities with i.i.d.

rewards drawn from an exponential-type parametric family with an unknown parameter $θ$, a class that includes exponential, Pareto, and bounded-support power-family distributions.

We first characterize the optimal full-information asymptotic competitive ratio for this family.

In the unbounded-support case, the limit is $ {\left(θ/({θ-c_+})\right)^{c_+/θ}}/ {Γ(1-c_+/θ)},$ while in the bounded-support case, the limit is $1$.

We then propose a confidence-based dynamic-programming policy for online learning.

By exploiting the explicit parametric

### AI 总结

总结生成失败

---

## 9. Learning to Fold: prizewinning solution at LeHome Challenge 2026 (1st place online, 2nd offline)

- **作者**: Ilia Larchenko
- **发布日期**: 2026-06-25
- **链接**: [arXiv:2606.27163v1](https://arxiv.org/abs/2606.27163v1) | [PDF](https://arxiv.org/pdf/2606.27163v1)
- **分类**: cs.RO, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

I describe my solution to the LeHome Challenge 2026, an ICRA 2026 competition on bimanual garment folding.

The system placed 1st of 62 teams in the online (simulation) round and 2nd in the real-world final.

It improves a vision-language-action (VLA) policy with a reinforcement-learning loop.

The policy is its own value function: the same network that predicts actions also predicts success, progress, and a few task-relevant future quantities, and those predictions drive advantage estimation, live failure detection, and candidate selection.

The work mostly recombines existing RL ideas with engin

### AI 总结

总结生成失败

---

## 10. Hybrid privacy-aware semantic search: SVD-truncated document geometry and CKKS-encrypted query reranking under a restricted threat model

- **作者**: Sergey Kurilenko
- **发布日期**: 2026-06-24
- **链接**: [arXiv:2606.26373v1](https://arxiv.org/abs/2606.26373v1) | [PDF](https://arxiv.org/pdf/2606.26373v1)
- **分类**: cs.CR, cs.AI, cs.IR
- **含金量**: 20/43 分

### 摘要

Dense embeddings power semantic search and retrieval-augmented generation, but embedding-inversion attacks can reconstruct source text from a vector: when a vector database leaks, the documents behind it leak too.

The textbook defences are extremes - encrypting the whole search homomorphically is sound but too slow at million-document scale, while privacy noise degrades ranking long before it protects.

We study a middle path exploiting the asymmetry between the static collection and the dynamic query.

The collection is protected geometrically: each vector is truncated onto a lower-dimensional 

### AI 总结

总结生成失败

---

