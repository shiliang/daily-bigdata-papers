# 大数据+AI 领域论文日报

**日期**: 2026-05-27

**论文数量**: 9 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [The Strongest Teacher Is Not Always...](https://arxiv.org/abs/2605.26872v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [MuCon: Clipped Muon Updates for LLM...](https://arxiv.org/abs/2605.26459v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Resolving the Correct Library: A Lo...](https://arxiv.org/abs/2605.26665v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Birkhoff Decompositions and Photoni...](https://arxiv.org/abs/2605.26845v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Towards Generalization-Oriented Mod...](https://arxiv.org/abs/2605.26776v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [MinT: Managed Infrastructure for Tr...](https://arxiv.org/abs/2605.13779v2) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Online Learning on Hidden-Convex Lo...](https://arxiv.org/abs/2605.26373v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Scaling World-Model Reinforcement L...](https://arxiv.org/abs/2605.26282v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [ScenePilot: Controllable Boundary-D...](https://arxiv.org/abs/2605.21168v2) | 待分析 | 评估失败 | [Code](https://github.com/QiyuRuan/ScenePilot.) | 20/43 |

---


## 1. The Strongest Teacher Is Not Always the Best Teacher: Student-Centric Answer Selection

- **作者**: Zhengyu Hu, Zheyuan Xiao, Linxin Song, Fengqing Jiang, Yutai Li
- **发布日期**: 2026-05-26
- **链接**: [arXiv:2605.26872v1](https://arxiv.org/abs/2605.26872v1) | [PDF](https://arxiv.org/pdf/2605.26872v1)
- **分类**: cs.LG, cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

LLM training increasingly relies on teacher-generated supervision, from synthetic responses to reasoning traces and tool-use demonstrations.

Current practice often chooses the highest-performing teacher to generate student training data, implicitly treating teacher test performance as a proxy for teaching quality.

We show that this assumption can fail: even when multiple teachers provide correct answers to the same question, the answer from the strongest teacher is not necessarily the best supervision for a given student.

To address this gap, we propose Student-Centric Answer Sampling (SCAS), 

### AI 总结

总结生成失败

---

## 2. MuCon: Clipped Muon Updates for LLM Training

- **作者**: Albert Yi
- **发布日期**: 2026-05-26
- **链接**: [arXiv:2605.26459v1](https://arxiv.org/abs/2605.26459v1) | [PDF](https://arxiv.org/pdf/2605.26459v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Muon-style optimizers take a matrix-valued momentum or preconditioned update $B = U \operatorname{diag}(σ_1,\ldots,σ_r) V^\top$ and replace it with its canonical partial polar factor $\operatorname{Pol}(B) = U V^\top$.

This maps every nonzero singular value to one.

MuCon is the clipped-Muon variant studied here: it applies singular-value clipping to the same Muon matrix, $D^{\mathrm{MuCon}}\_τ(B) = \operatorname{MClip}\_τ(B) = U \operatorname{diag}\bigl(\min\{σ\_i,τ\}\bigr) V^\top, \qquad τ> 0$.

Thus, $\operatorname{MClip}\_τ$ denotes the mathematical clipping operator, while MuCon denotes the

### AI 总结

总结生成失败

---

## 3. Resolving the Correct Library: A Loader-Level Defense Solution Against Shared Object Hijacking

- **作者**: Can Ozkan, Dave Singelee
- **发布日期**: 2026-05-26
- **链接**: [arXiv:2605.26665v1](https://arxiv.org/abs/2605.26665v1) | [PDF](https://arxiv.org/pdf/2605.26665v1)
- **分类**: cs.CR
- **含金量**: 20/43 分

### 摘要

Shared library hijacking attacks in the Linux ecosystem, including embedded Linux, are a significant concern.

It fundamentally exploits the dynamic linker's library-resolution semantics rather than modifying trusted libraries directly.

Prior research has extensively analyzed attack vectors exploiting environment variables, embedded search paths, and dynamic loader internals, demonstrating that hijacking is rooted in fundamental loader behavior rather than isolated misconfigurations.

Existing defenses either harden or replace the loader, enforce control-flow integrity after libraries are loaded

### AI 总结

总结生成失败

---

## 4. Birkhoff Decompositions and Photonic Interconnects Wait! Don't Forget the Compute!

- **作者**: Eliezer Amponsah, Vamsi Addanki
- **发布日期**: 2026-05-26
- **链接**: [arXiv:2605.26845v1](https://arxiv.org/abs/2605.26845v1) | [PDF](https://arxiv.org/pdf/2605.26845v1)
- **分类**: cs.NI
- **含金量**: 20/43 分

### 摘要

The growing demand for efficient communication in distributed training and inference has sparked significant interest in reconfigurable photonic interconnects across both academia and industry.

Mixture-of-Experts (MoE) models, with their highly skewed communication patterns, present a natural opportunity for such circuit-switched fabrics.

However, existing approaches largely optimize communication in isolation, overlooking the interaction between communication and the expert computation that follows.

In this paper, we revisit circuit scheduling for all-to-all communication in MoE execution.



### AI 总结

总结生成失败

---

## 5. Towards Generalization-Oriented Models for Vehicle Routing Problems with Mixture-of-Experts

- **作者**: Changhao Miao, Yuntian Zhang, Tongyu Wu, Fang Deng, Chen Chen
- **发布日期**: 2026-05-26
- **链接**: [arXiv:2605.26776v1](https://arxiv.org/abs/2605.26776v1) | [PDF](https://arxiv.org/pdf/2605.26776v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

In recent years, Deep Reinforcement Learning (DRL) has achieved substantial progress on Vehicle Routing Problems (VRPs).

However, existing DRL-based methods are typically trained on instances generated from a uniform distribution, which limits their performance under real-world distribution shifts.

In this paper, we aim to develop a generalization-oriented model that partitions the policy network into multiple modules and adaptively recombines modules to form specific policies during inference.

Specifically, we propose Residual Refined Experts with Instance-level Gating (R2E-IG) to improve cro

### AI 总结

总结生成失败

---

## 6. MinT: Managed Infrastructure for Training and Serving Millions of LLMs

- **作者**: Mind Lab,  :, Song Cao, Vic Cao, Andrew Chen
- **发布日期**: 2026-05-13
- **链接**: [arXiv:2605.13779v2](https://arxiv.org/abs/2605.13779v2) | [PDF](https://arxiv.org/pdf/2605.13779v2)
- **分类**: cs.LG, cs.AI, cs.DC
- **含金量**: 20/43 分

### 摘要

We present MindLab Toolkit (MinT), a managed infrastructure system for Low-Rank Adaptation (LoRA) post-training and online serving.

MinT targets a setting where many trained policies are produced over a small number of expensive base-model deployments.

Instead of materializing each policy as a merged full checkpoint, MinT keeps the base model resident and moves exported LoRA adapter revisions through rollout, update, export, evaluation, serving, and rollback, hiding distributed training, serving, scheduling, and data movement behind a service interface.

MinT scales this path along three axes.



### AI 总结

总结生成失败

---

## 7. Online Learning on Hidden-Convex Losses via Algorithmic Equivalence: Optimal Regret, Geometric Barrier, and Bandit Feedback

- **作者**: Anas Barakat, Andreas Kontogiannis, Vasilis Pollatos, Ioannis Panageas, Antonios Varvitsiotis
- **发布日期**: 2026-05-25
- **链接**: [arXiv:2605.26373v1](https://arxiv.org/abs/2605.26373v1) | [PDF](https://arxiv.org/pdf/2605.26373v1)
- **分类**: cs.LG, math.OC, stat.ML
- **含金量**: 20/43 分

### 摘要

We study adversarial online learning with hidden-convex losses, i.e., nonconvex losses that become convex after a nonlinear reparameterization.

Ghai, Lu and Hazan (2022) proved that, under geometric and smoothness assumptions, online gradient descent (OGD) on such nonconvex losses approximately simulates online mirror descent (OMD) on the underlying convex losses with a suitable regularizer, yielding $\mathcal{O}(T^{2/3})$ regret.

They left open whether the optimal $Θ(\sqrt{T})$ regret from online convex optimization can be recovered in this hidden-convex setting.

We answer this question affir

### AI 总结

总结生成失败

---

## 8. Scaling World-Model Reinforcement Learning Through Diffusion Policy Optimization

- **作者**: Xiaoyuan Cheng, Wenxuan Yuan, Zhancun Mu, Yuanzhao Zhang, Yiming Yang
- **发布日期**: 2026-05-25
- **链接**: [arXiv:2605.26282v1](https://arxiv.org/abs/2605.26282v1) | [PDF](https://arxiv.org/pdf/2605.26282v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Model-based reinforcement learning (RL) can be effectively supported at scale through the use of world models.

However, in practice, scaling such approaches remains fundamentally limited.

A commonly recognized challenge is model bias and error compounding, which degrade long-horizon predictions.

Beyond these issues, we identify a more critical yet underexplored bottleneck: a structural misalignment between search and value learning in existing world model approaches.

In particular, policy improvement often relies on value functions induced by a separate, non-search policy, resulting in trainin

### AI 总结

总结生成失败

---

## 9. ScenePilot: Controllable Boundary-Driven Critical Scenario Generation for Autonomous Driving

- **作者**: Qiyu Ruan, Yuxuan Wang, He Li, Zhenning Li, Cheng-zhong Xu
- **发布日期**: 2026-05-20
- **链接**: [arXiv:2605.21168v2](https://arxiv.org/abs/2605.21168v2) | [PDF](https://arxiv.org/pdf/2605.21168v2)
- **分类**: cs.AI
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/QiyuRuan/ScenePilot.) ⭐ 0

### 摘要

Safety-critical scenarios are central to evaluating autonomous driving systems, yet their rarity in naturalistic logs makes simulation-based stress testing indispensable.

Most scenario generation methods treat surrounding agents as adversaries, but they either (i) induce failures without explicitly modeling vehicle-road physical limits, yielding visually extreme yet physically unsolvable crashes, or (ii) enforce physical feasibility or policy feasibility in isolation, which can over-focus on aggressive maneuvers or remain tied to a controller-dependent capability boundary.

We propose ScenePilo

### AI 总结

总结生成失败

---

