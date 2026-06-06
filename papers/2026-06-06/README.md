# 大数据+AI 领域论文日报

**日期**: 2026-06-06

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [PC Layer: Polynomial Weight Precond...](https://arxiv.org/abs/2606.06470v1) | 待分析 | 评估失败 | [Code](https://github.com/Empath-aln/PC-layer.) | 20/43 |
| 2 | [Better Literary Translation: A Mult...](https://arxiv.org/abs/2606.05924v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [RedKnot: Efficient Long-Context LLM...](https://arxiv.org/abs/2606.06256v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [The Dignity-Centric Stack: A Common...](https://arxiv.org/abs/2606.06083v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [CLEAR: Cognition and Latent Evaluat...](https://arxiv.org/abs/2606.06219v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Regret Minimization with Adaptive O...](https://arxiv.org/abs/2606.06486v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Adaptive Learning Rates with Surrog...](https://arxiv.org/abs/2606.06043v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Continual Learning Bench: Evaluatin...](https://arxiv.org/abs/2606.05661v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [CLaaS: Continual learning as a serv...](https://arxiv.org/abs/2606.05559v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [LLM-Guided ANN Index Optimization f...](https://arxiv.org/abs/2606.05489v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. PC Layer: Polynomial Weight Preconditioning for Improving LLM Pre-Training

- **作者**: Senmiao Wang, Tiantian Fang, Haoran Zhang, Yushun Zhang, Kunxiang Zhao
- **发布日期**: 2026-06-04
- **链接**: [arXiv:2606.06470v1](https://arxiv.org/abs/2606.06470v1) | [PDF](https://arxiv.org/pdf/2606.06470v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/Empath-aln/PC-layer.) ⭐ 0

### 摘要

We propose a preconditioning (PC) layer, a weight parameterization via polynomial preconditioner that ensures stable weight conditioning throughout LLM training.

The PC module reshapes the singular-value spectrum of weight matrices via low-degree polynomial preconditioning.

After training, the preconditioned weights can be merged back into the original architecture, incurring no inference overhead.

We demonstrate the advantage of the proposed PC layer over standard transformers in Llama-1B pre-training, for both the AdamW and Muon optimizers.

Theoretically, we justify this spectrum-control pri

### AI 总结

总结生成失败

---

## 2. Better Literary Translation: A Multi-Aspect Data Generation and LLM Training Approach

- **作者**: Zhihao Lin, Ziqi Zhu, Hao Huang, Guanghui Wang, Peiyang He
- **发布日期**: 2026-06-04
- **链接**: [arXiv:2606.05924v1](https://arxiv.org/abs/2606.05924v1) | [PDF](https://arxiv.org/pdf/2606.05924v1)
- **分类**: cs.CL, cs.AI
- **含金量**: 20/43 分

### 摘要

Literary translation poses unique challenges due to the scarcity of high-quality annotated data and the need to balance expression fluency with literary effect.

We present a multi-aspect iterative refinement framework that generates high-quality translation references and preference data through specialized LLM translators, each targeting a distinct quality dimension.

We leverage the generated data for supervised fine-tuning and reinforcement learning.

Experiments show that our generated references outperform the original ground truth for SFT by 8.65 CEA100 points.

For reinforcement learning, 

### AI 总结

总结生成失败

---

## 3. RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention

- **作者**: Yang Liu, ZhaoKai Luo, HuaYi Jin, ZhiYong Wang, RuoZhou He
- **发布日期**: 2026-06-04
- **链接**: [arXiv:2606.06256v1](https://arxiv.org/abs/2606.06256v1) | [PDF](https://arxiv.org/pdf/2606.06256v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

As the input length of large language model (LLM) serving continues to grow, the KV cache has become a dominant bottleneck in AI infrastructure.

It limits GPU memory capacity, serving concurrency, cache reuse, and distributed scalability.

Several important problems, including position-independent KV cache, prefix KV cache compression, hot/cold KV cache separation, and distributed KV cache management, all depend on how the KV cache is represented and managed.

However, existing serving systems largely rely on a monolithic KV cache abstraction, where the KV cache is treated as a homogeneous seque

### AI 总结

总结生成失败

---

## 4. The Dignity-Centric Stack: A Commons-Governed, Horizontally Federated Architecture for Human-Dignity AI

- **作者**: Eduardo C. Garrido-Merchán
- **发布日期**: 2026-06-04
- **链接**: [arXiv:2606.06083v1](https://arxiv.org/abs/2606.06083v1) | [PDF](https://arxiv.org/pdf/2606.06083v1)
- **分类**: cs.CY
- **含金量**: 20/43 分

### 摘要

The human-dignity-centric digital social contract grounds personal data in human dignity, data personalism, and data sovereignty, and articulates six dimensions of data governance: technological oversight, automation limits, economic justice, political legitimacy, social cohesion, and legal guarantees.

It presupposes, however, that enforcement falls to State regulators, licensed fiduciaries, and multi-stakeholder bodies embedded in existing legal systems.

This paper asks whether its normative content can instead be realized not as rules imposed on the owners of the AI stack from without, but a

### AI 总结

总结生成失败

---

## 5. CLEAR: Cognition and Latent Evaluation for Adaptive Routing in End-to-End Autonomous Driving

- **作者**: Yining Xing, Zehong Ke, Zhiyuan Liu, Yanbo Jiang, Wenhao Yu
- **发布日期**: 2026-06-04
- **链接**: [arXiv:2606.06219v1](https://arxiv.org/abs/2606.06219v1) | [PDF](https://arxiv.org/pdf/2606.06219v1)
- **分类**: cs.RO, cs.AI
- **含金量**: 20/43 分

### 摘要

End-to-end autonomous driving models often struggle to balance multi-modal maneuver generation with real-time inference constraints.

While diffusion models successfully capture diverse driving behaviors, their iterative denoising process incurs unacceptable latency for safety-critical deployment.

To address this, we propose CLEAR (Cognition and Latent Evaluation for Adaptive Routing), a framework that combines ultra-fast generative planning with deep semantic reasoning.

CLEAR employs Drive-JEPA as the visual encoder and replaces the multi-step denoising chain with a single-step conditional dri

### AI 总结

总结生成失败

---

## 6. Regret Minimization with Adaptive Opponents in Repeated Games

- **作者**: Mingyang Liu, Asuman Ozdaglar, Tiancheng Yu, Kaiqing Zhang
- **发布日期**: 2026-06-04
- **链接**: [arXiv:2606.06486v1](https://arxiv.org/abs/2606.06486v1) | [PDF](https://arxiv.org/pdf/2606.06486v1)
- **分类**: cs.LG, cs.AI, cs.GT
- **含金量**: 20/43 分

### 摘要

In this paper, we study regret minimization in repeated games with \emph{adaptive} opponents who can respond based on histories of play.

The standard metric of \emph{external regret} in online learning is known to fail to capture such adaptivity.

To account for players' counterfactual reasoning, we introduce {\tt Repeated Policy Regret (RP-Regret)}, a game-theoretic metric that measures the difference between the \emph{realized} and the \emph{best-in-hindsight} accumulated utility when all players can \emph{respond} to the history of play.

Compared to existing regret notions in this setting, o

### AI 总结

总结生成失败

---

## 7. Adaptive Learning Rates with Surrogate Probability for Follow-the-Perturbed-Leader

- **作者**: Jongyeong Lee, Junya Honda, Shinji Ito, Chansoo Kim
- **发布日期**: 2026-06-04
- **链接**: [arXiv:2606.06043v1](https://arxiv.org/abs/2606.06043v1) | [PDF](https://arxiv.org/pdf/2606.06043v1)
- **分类**: stat.ML, cs.LG
- **含金量**: 20/43 分

### 摘要

Follow-the-regularized-leader framework has shown effectiveness and flexibility in online learning problems, where the choice of learning rates are known to be crucial.

Recently, adaptive learning rates defined in terms of the arm-selection probabilities, obtained by solving convex optimization, have achieved improved best-of-both-worlds (BOBW) guarantees in various bandit problems.

In contrast, BOBW guarantees for its computationally efficient alternative, follow-the-perturbed-leader (FTPL), remain relatively limited since its optimization-free nature ironically makes the design of adaptive, 

### AI 总结

总结生成失败

---

## 8. Continual Learning Bench: Evaluating Frontier AI Systems in Real-World Stateful Environments

- **作者**: Parth Asawa, Christopher M. Glaze, Gabriel Orlanski, Ramya Ramakrishnan, Benji Xu
- **发布日期**: 2026-06-04
- **链接**: [arXiv:2606.05661v1](https://arxiv.org/abs/2606.05661v1) | [PDF](https://arxiv.org/pdf/2606.05661v1)
- **分类**: cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

Continual learning, the ability of AI systems to improve through sequential experience, has attracted substantial interest, but no high-quality benchmark exists to evaluate it.

We introduce Continual Learning Bench (CL-Bench), the first difficult, expert-validated benchmark designed to measure whether LLM-based systems genuinely improve with experience.

CL-Bench spans six diverse domains (software engineering, signal processing, disease outbreak forecasting, database querying, strategic game-playing, and demand forecasting), each validated by domain experts and designed so that tasks share a l

### AI 总结

总结生成失败

---

## 9. CLaaS: Continual learning as a service for sample efficient online learning

- **作者**: Kion Fallah, Silen Naihin, Barak Widawsky, Qingqing Mao
- **发布日期**: 2026-06-04
- **链接**: [arXiv:2606.05559v1](https://arxiv.org/abs/2606.05559v1) | [PDF](https://arxiv.org/pdf/2606.05559v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Deployed large language model agents must adapt to distribution shift in dynamic environments.

Ideally, adaptation can be performed from accumulated agent experiences and retain prior capabilities while transferring to future tasks.

However, agent actions and environmental transitions can only be sampled once per scenario, as real-world environments cannot be trivially reset.

To this end, we investigate an experiential and online continual learning setting in which agents learn from a stream of scenarios.

We propose continual learning as-a-service (CLaaS), a system which enables agents to impr

### AI 总结

总结生成失败

---

## 10. LLM-Guided ANN Index Optimization for Human-Object Interaction Retrieval

- **作者**: Shahrzad Esmat, Chaunte W. Lacewell, Sameh Gobriel, Nilesh Jain, Ali Jannesari
- **发布日期**: 2026-06-03
- **链接**: [arXiv:2606.05489v1](https://arxiv.org/abs/2606.05489v1) | [PDF](https://arxiv.org/pdf/2606.05489v1)
- **分类**: cs.CV, cs.DB
- **含金量**: 20/43 分

### 摘要

Retrieval systems underpin modern AI applications -- spanning visual search, recommendation engines, and multi-modal question answering.

Modern multi-stage retrieval systems require the joint optimization of highly coupled parameters, yet traditional hyperparameter optimization (HPO) methods -- including Tree-structured Parzen Estimators (TPE) and Gaussian Process Bayesian Optimization -- rely on an independence assumption that fundamentally prevents them from navigating these coupled configuration spaces.

We address this limitation with a phase-aware large language model (LLM) agent that cond

### AI 总结

总结生成失败

---

