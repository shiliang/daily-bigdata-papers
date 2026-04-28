# 大数据+AI 领域论文日报

**日期**: 2026-04-28

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [TACO: Efficient Communication Compr...](https://arxiv.org/abs/2604.24088v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [FlashOverlap: Minimizing Tail Laten...](https://arxiv.org/abs/2604.24013v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [MatchRDMA: A Segmented and Rate-Mat...](https://arxiv.org/abs/2604.23932v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [BoomHQ: Learning to Boost Multiple ...](https://arxiv.org/abs/2604.24552v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Geometric Analysis of Self-Supervis...](https://arxiv.org/abs/2604.24469v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Characterizing Vision-Language-Acti...](https://arxiv.org/abs/2604.24447v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Efficient learning by implicit expl...](https://arxiv.org/abs/2604.24555v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Learning is Revelation in Disguise:...](https://arxiv.org/abs/2604.24093v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Geometry-Aware Offline-to-Online Le...](https://arxiv.org/abs/2604.24016v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [FreeScale: Distributed Training for...](https://arxiv.org/abs/2604.24073v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. TACO: Efficient Communication Compression of Intermediate Tensors for Scalable Tensor-Parallel LLM Training

- **作者**: Man Liu, Xingchen Liu, Xingjian Tian, Bing Lu, Shengkay Lyu
- **发布日期**: 2026-04-27
- **链接**: [arXiv:2604.24088v1](https://arxiv.org/abs/2604.24088v1) | [PDF](https://arxiv.org/pdf/2604.24088v1)
- **分类**: cs.DC, cs.AI
- **含金量**: 20/43 分

### 摘要

Handling communication overhead in large-scale tensor-parallel training remains a critical challenge due to the dense, near-zero distributions of intermediate tensors, which exacerbate errors under frequent communication and introduce significant computational overhead during compression.

To this end, we propose TACO (Tensor-parallel Adaptive COmmunication compression), a robust FP8-based framework for compressing TP intermediate tensors.

First, we employ a data-driven reshaping strategy combined with an Adaptive Scale-Hadamard Transform to enable high-fidelity FP8 quantization, while its Dual

### AI 总结

总结生成失败

---

## 2. FlashOverlap: Minimizing Tail Latency in Communication Overlap for Distributed LLM Training

- **作者**: Rezaul Karim, Austin Wen, Wang Zongzuo, Weiwei Zhang, Yang Liu
- **发布日期**: 2026-04-27
- **链接**: [arXiv:2604.24013v1](https://arxiv.org/abs/2604.24013v1) | [PDF](https://arxiv.org/pdf/2604.24013v1)
- **分类**: cs.LG, cs.CV, cs.DC
- **含金量**: 20/43 分

### 摘要

The rapid growth in the size of large language models has necessitated the partitioning of computational workloads across accelerators such as GPUs, TPUs, and NPUs.

However, these parallelization strategies incur substantial data communication overhead significantly hindering computational efficiency.

While communication-computation overlap presents a promising direction, existing data slicing based solutions suffer from tail latency.

To overcome this limitation, this research introduces a novel communication-computation overlap technique to eliminate this tail latency in state of the art over

### AI 总结

总结生成失败

---

## 3. MatchRDMA: A Segmented and Rate-Matched Long-Haul RDMA Scheme for Geo-distributed LLM Training over OTN

- **作者**: Jun Dai, Xiaorun Wang, Xingde Li, Zheng Yang, Kexiong Fang
- **发布日期**: 2026-04-27
- **链接**: [arXiv:2604.23932v1](https://arxiv.org/abs/2604.23932v1) | [PDF](https://arxiv.org/pdf/2604.23932v1)
- **分类**: cs.NI
- **含金量**: 20/43 分

### 摘要

We propose MatchRDMA, a proactive, segmented, and rate-matched long-haul RDMA scheme for geo-distributed LLM training over OTN.

By coordinating source and destination OTN rates, it improves inter-DC throughput by up to 20x compared with conventional RDMA, and reduces destination-OTN buffer occupancy by up to 62.7%.

### AI 总结

总结生成失败

---

## 4. BoomHQ: Learning to Boost Multiple Hybrid Queries on Vector DBMSs

- **作者**: Ermu Qiu, Tianyi Chen, Jun Gao, Xing Wei, Yaofeng Tu
- **发布日期**: 2026-04-27
- **链接**: [arXiv:2604.24552v1](https://arxiv.org/abs/2604.24552v1) | [PDF](https://arxiv.org/pdf/2604.24552v1)
- **分类**: cs.DB
- **含金量**: 20/43 分

### 摘要

Hybrid queries, which combine vector nearest neighbor searches with scalar predicates, represent a fundamental challenge in managing vector databases.

Existing methods often restrict the number of vector columns involved or the complexity of scalar predicates, thereby limiting their flexibility in handling diverse query patterns.

Moreover, these approaches typically do not fully leverage the correlations between scalar and vector attributes, or the distributional patterns observed from query vector neighborhoods.

To address these limitations, we introduce BoomHQ, a learning-based framework to 

### AI 总结

总结生成失败

---

## 5. Geometric Analysis of Self-Supervised Vision Representations for Semantic Image Retrieval

- **作者**: Esteban Rodríguez-Betancourt, Edgar Casasola-Murillo
- **发布日期**: 2026-04-27
- **链接**: [arXiv:2604.24469v1](https://arxiv.org/abs/2604.24469v1) | [PDF](https://arxiv.org/pdf/2604.24469v1)
- **分类**: cs.IR, cs.CV
- **含金量**: 20/43 分

### 摘要

Content-based image retrieval (CBIR) systems enable users to search images based on visual content instead of relying on metadata.

The text domain has benefited from vector search of representations created with unsupervised methods such as BERT.

However, modern self-supervised learning methods for vision are mostly not reported in CBIR-related literature, instead relying on supervised models or multi-modal methods that align text and vision.

We evaluate how the representations learned by modern self-supervised learning methods for vision perform under typical retrieval stacks that leverage 

### AI 总结

总结生成失败

---

## 6. Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment

- **作者**: Kaijun Zhou, Qiwei Chen, Da Peng, Zhiyang Li, Xijun Li
- **发布日期**: 2026-04-27
- **链接**: [arXiv:2604.24447v1](https://arxiv.org/abs/2604.24447v1) | [PDF](https://arxiv.org/pdf/2604.24447v1)
- **分类**: cs.RO, cs.AI
- **含金量**: 20/43 分

### 摘要

Vision-Language-Action (VLA) models are promising for generalist robot control, but on-robot deployment is bottlenecked by real-time inference under tight cost and energy budgets.

Most prior evaluations rely on desktop-grade GPUs, obscuring the trade-offs and opportunities offered by heterogeneous edge accelerators (GPUs/XPUs/NPUs).

We present a systematic analysis for low-cost VLA deployment via model-hardware co-characterization.

First, we build a cross-accelerator leaderboard and evaluate model-hardware pairs under CET (Cost, Energy, Time), showing that right-sized edge devices can be more 

### AI 总结

总结生成失败

---

## 7. Efficient learning by implicit exploration in bandit problems with side observations

- **作者**: Tomas Kocak, Gergely Neu, Michal Valko, Remi Munos
- **发布日期**: 2026-04-27
- **链接**: [arXiv:2604.24555v1](https://arxiv.org/abs/2604.24555v1) | [PDF](https://arxiv.org/pdf/2604.24555v1)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

We consider online learning problems under a partial observability model capturing situations where the information conveyed to the learner is between full information and bandit feedback.

In the simplest variant, we assume that in addition to its own loss, the learner also gets to observe losses of some other actions.

The revealed losses depend on the learner's action and a directed observation system chosen by the environment.

For this setting, we propose the first algorithm that enjoys near-optimal regret guarantees without having to know the observation system before selecting its actions.

### AI 总结

总结生成失败

---

## 8. Learning is Revelation in Disguise: Improved Regret and Equivalence Results for Dynamic Pricing

- **作者**: Shiliang Zuo
- **发布日期**: 2026-04-27
- **链接**: [arXiv:2604.24093v1](https://arxiv.org/abs/2604.24093v1) | [PDF](https://arxiv.org/pdf/2604.24093v1)
- **分类**: cs.GT
- **含金量**: 20/43 分

### 摘要

We study dynamic pricing where a seller repeatedly interacts with a strategic, non-myopic buyer who has a fixed private valuation and discounts future utility.

Prior work focused exclusively on posted-price mechanisms, which only extract binary accept/reject signals.

For our first result, we show that menu mechanisms-offering allocation-payment contracts are able to achieve $O(T_γ\log T_γ)$ regret, where $T_γ$ is the buyer's effective discounted time horizon, improving all prior bounds.

Our second contribution is more conceptual in nature.

The problem of dynamic pricing sits at the intersectio

### AI 总结

总结生成失败

---

## 9. Geometry-Aware Offline-to-Online Learning in Linear Contextual Bandits

- **作者**: Zean Han, Ruihan Lin, Zezhen Ding, Jiheng Zhang
- **发布日期**: 2026-04-27
- **链接**: [arXiv:2604.24016v1](https://arxiv.org/abs/2604.24016v1) | [PDF](https://arxiv.org/pdf/2604.24016v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

We study offline-to-online learning in linear contextual bandits with biased offline regression data: the offline parameter need not match the online one, so history should not be treated as a single warm start.

We model directional transfer with a shift certificate $(M_{\mathrm{shift}},ρ)$ and offline ridge estimation, yielding a geometry-aware confidence region for the online parameter rather than an isotropic radius.

We propose \emph{Ellipsoidal-MINUCB}, which combines a standard online branch with an offline-informed pooled branch and uses offline information only when it tightens uncertai

### AI 总结

总结生成失败

---

## 10. FreeScale: Distributed Training for Sequence Recommendation Models with Minimal Scaling Cost

- **作者**: Chenhao Feng, Haoli Zhang, Shakhzod Ali-Zade, Yanli Zhao, Liang Luo
- **发布日期**: 2026-04-27
- **链接**: [arXiv:2604.24073v1](https://arxiv.org/abs/2604.24073v1) | [PDF](https://arxiv.org/pdf/2604.24073v1)
- **分类**: cs.LG, cs.AI, cs.DC, cs.IR
- **含金量**: 20/43 分

### 摘要

Modern industrial Deep Learning Recommendation Models typically extract user preferences through the analysis of sequential interaction histories, subsequently generating predictions based on these derived interests.

The inherent heterogeneity in data characteristics frequently result in substantial under-utilization of computational resources during large-scale training, primarily due to computational bubbles caused by severe stragglers and slow blocking communications.

This paper introduces FreeScale, a solution designed to (1) mitigate the straggler problem through meticulously load balance

### AI 总结

总结生成失败

---

