# 大数据+AI 领域论文日报

**日期**: 2026-06-09

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Powering the Future of AI: Navigati...](https://arxiv.org/abs/2606.09617v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [When More Cores Hurts: The Vector D...](https://arxiv.org/abs/2606.08950v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Online Learning with Recency: Algor...](https://arxiv.org/abs/2606.08977v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Flexible Online Representation Lear...](https://arxiv.org/abs/2606.01546v2) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Resource-aware Computation-Communic...](https://arxiv.org/abs/2606.09200v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [FlashCP: Load-Balanced Communicatio...](https://arxiv.org/abs/2606.08476v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [The Strongest Teacher Is Not Always...](https://arxiv.org/abs/2605.26872v2) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [MB-Loc: Multi-planar Bird's-eye-vie...](https://arxiv.org/abs/2606.08744v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Sound Field Interpolation Using Phy...](https://arxiv.org/abs/2606.08435v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Semantic Quorum Assurance: Collecti...](https://arxiv.org/abs/2606.08021v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Powering the Future of AI: Navigating the Trade-offs for Europe's Energy Transition and Net-Zero Goals

- **作者**: Mohammad Hemmati, Gbemi Oluleye, Vassilis M. Charitopoulos
- **发布日期**: 2026-06-08
- **链接**: [arXiv:2606.09617v1](https://arxiv.org/abs/2606.09617v1) | [PDF](https://arxiv.org/pdf/2606.09617v1)
- **分类**: math.OC, cs.AI, cs.CY, eess.SY
- **含金量**: 20/43 分

### 摘要

The rapid expansion of AI globally has led to the proliferation of energy-intensive hyperscale data centres (DCs), making them as a structurally challenging component in power system planning and operation.

Using a spatially explicit optimisation model of Europe across 21 AI growth scenarios, we systematically quantify additional demand, capacity requirements, emissions, and operational impacts of DCs.

Results indicate that AI could drive 73-723 TWh of extra demand by 2050, risking cumulative emissions overshoots of 67-181 MtCO2 between 2030 and 2050.

Our analysis indicates that after 2030, th

### AI 总结

总结生成失败

---

## 2. When More Cores Hurts: The Vector Database Scaling Paradox in HPC

- **作者**: Seth Ockerman, Song Young Oh, Amal Gueroudji, Rochana Chaturvedi, Philip Carns
- **发布日期**: 2026-06-08
- **链接**: [arXiv:2606.08950v1](https://arxiv.org/abs/2606.08950v1) | [PDF](https://arxiv.org/pdf/2606.08950v1)
- **分类**: cs.DC, cs.DB
- **含金量**: 20/43 分

### 摘要

Vector databases have been designed and optimized for cloud environments; however, emerging scientific AI workloads (e.g., molecular search, meteorological trajectory detection, and literature-driven hypothesis generation) demand efficient, scalable execution on HPC systems.

We present a large-scale evaluation of three state-of-the-art vector databases -- Qdrant, Milvus, and Weaviate -- on two production supercomputers, scaling to 256 distributed workers across 64 compute nodes.

We evaluate representative workload patterns -- mixed read/write and write-then-read -- using popular benchmarks, mu

### AI 总结

总结生成失败

---

## 3. Online Learning with Recency: Algorithms for Sliding-window Streaming Multi-armed Bandits

- **作者**: Vladimir Braverman, Chen Wang, Liudeng Wang, Samson Zhou
- **发布日期**: 2026-06-08
- **链接**: [arXiv:2606.08977v1](https://arxiv.org/abs/2606.08977v1) | [PDF](https://arxiv.org/pdf/2606.08977v1)
- **分类**: cs.LG, cs.DS
- **含金量**: 20/43 分

### 摘要

Motivated by the recency effect in online learning, we study algorithms for single-pass *sliding-window streaming multi-armed bandits (MABs)* in this paper.

In this setting, we are given $n$ arms with unknown sub-Gaussian reward distributions and a parameter $W$.

The arms arrive in a single-pass stream, and only the most recent $W$ arms are considered valid.

The algorithm is required to perform pure exploration and regret minimization with limited memory, defined as the number of stored arms.

The model is a natural extension of the streaming multi-armed bandits model (without the sliding windo

### AI 总结

总结生成失败

---

## 4. Flexible Online Representation Learning Based on Similarity Matching

- **作者**: Shagesh Sridharan, Yanis Bahroun, Anirvan M. Sengupta
- **发布日期**: 2026-06-01
- **链接**: [arXiv:2606.01546v2](https://arxiv.org/abs/2606.01546v2) | [PDF](https://arxiv.org/pdf/2606.01546v2)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Sparse high-dimensional representations are conducive to uncovering nontrivial structures in unsupervised exploration of data.

Such a representation can deal with the dense connectivity in graphs relevant to community detection problems.

However, sparse high-dimensional representations are capable of doing more, including manifold tiling and feature learning.

Conventional algorithms optimize in the space of computationally intractable completely positive matrices or relax the problem to the space of doubly nonnegative matrices that scale with sample size in a way rendering them impractical for

### AI 总结

总结生成失败

---

## 5. Resource-aware Computation-Communication Overlap for multi-GPU ML Workloads

- **作者**: Minyu Cui, Miquel Pericas
- **发布日期**: 2026-06-08
- **链接**: [arXiv:2606.09200v1](https://arxiv.org/abs/2606.09200v1) | [PDF](https://arxiv.org/pdf/2606.09200v1)
- **分类**: cs.DC, cs.AI
- **含金量**: 20/43 分

### 摘要

The rapid growth of large-scale machine learning (ML) has made distributed training across multiple GPUs a fundamental component of modern ML systems.

As model sizes and computational throughput continue to increase, communication overhead has become a dominant bottleneck in multi-GPU training, particularly when computation and communication are executed sequentially.

This work explores concurrent execution of computation and collective communication using two portable runtime controls: shared-memory-driven occupancy shaping for computation kernels and elevated scheduling priority for communic

### AI 总结

总结生成失败

---

## 6. FlashCP: Load-Balanced Communication-Efficient Context Parallelism for LLM Training

- **作者**: Zheng Wang, Eric Liu, Linan Jiang, Zhongkai Yu, Zaifeng Pan
- **发布日期**: 2026-06-07
- **链接**: [arXiv:2606.08476v1](https://arxiv.org/abs/2606.08476v1) | [PDF](https://arxiv.org/pdf/2606.08476v1)
- **分类**: cs.DC, cs.AI
- **含金量**: 20/43 分

### 摘要

Context parallelism (CP) is essential for training large-scale, long-context language models, as it partitions sequences to reduce memory overhead.

However, existing CP methods suffer from workload imbalance, inefficient kernels, and redundant communication due to static sequence sharding and key-value (KV) tensor communication.

We present FlashCP, a load-balanced and communication-efficient framework for CP training.

FlashCP introduces a sharding-aware communication mechanism to eliminate redundant KV communication and proposes a novel Whole-Doc sharding strategy that maximizes communication 

### AI 总结

总结生成失败

---

## 7. The Strongest Teacher Is Not Always the Best Teacher: Student-Centric Answer Selection

- **作者**: Zhengyu Hu, Zheyuan Xiao, Linxin Song, Fengqing Jiang, Yuetai Li
- **发布日期**: 2026-05-26
- **链接**: [arXiv:2605.26872v2](https://arxiv.org/abs/2605.26872v2) | [PDF](https://arxiv.org/pdf/2605.26872v2)
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

## 8. MB-Loc: Multi-planar Bird's-eye-view Localization in outdoor LiDAR scenes

- **作者**: Ayaan Choudhury, Preet Savalia, Anirudh Pydah, Avinash Sharma
- **发布日期**: 2026-06-07
- **链接**: [arXiv:2606.08744v1](https://arxiv.org/abs/2606.08744v1) | [PDF](https://arxiv.org/pdf/2606.08744v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

Global LiDAR localization is a fundamental task for autonomous navigation systems.

Recent methods perform Scene Coordinate Regression (SCR) and achieve superior accuracy over Absolute Pose Regression (APR) solutions by predicting dense 3D world coordinates.

However, SCR approaches introduce two major bottlenecks: severe computational inefficiency from processing raw 3D geometries and significant performance degradation under varying sensor viewpoints.

To address these limitations, we present MB-Loc, a lightweight and viewpoint-robust SCR framework.

Instead of relying on heavy 3D convolutions, 

### AI 总结

总结生成失败

---

## 9. Sound Field Interpolation Using Physics-Informed Extreme Learning Machine with Pre-Training

- **作者**: Hayato Komaba, Gen Sato, Ken Kurata, Yusuke Ikeda
- **发布日期**: 2026-06-07
- **链接**: [arXiv:2606.08435v1](https://arxiv.org/abs/2606.08435v1) | [PDF](https://arxiv.org/pdf/2606.08435v1)
- **分类**: eess.AS
- **含金量**: 20/43 分

### 摘要

Numerous machine learning-based sound field interpolation methods have been proposed.

In particular, physics-informed neural networks (PINNs) can accurately interpolate sound fields from a small number of microphones.

However, their high computational cost and long training time pose practical challenges for applications requiring real-time processing or online learning.

To address this, we propose a hybrid framework that combines PINN-based pre-training with a physics-informed extreme learning machine (PIELM) tailored for acoustic fields.

By replacing iterative PINN fine-tuning for each targe

### AI 总结

总结生成失败

---

## 10. Semantic Quorum Assurance: Collective Certification for Non-Deterministic AI Infrastructure

- **作者**: Jun He, Deying Yu
- **发布日期**: 2026-06-06
- **链接**: [arXiv:2606.08021v1](https://arxiv.org/abs/2606.08021v1) | [PDF](https://arxiv.org/pdf/2606.08021v1)
- **分类**: cs.LG, cs.AI, cs.MA
- **含金量**: 20/43 分

### 摘要

As large language model (LLM) agents are integrated into autonomous cloud operations, distributed systems face a semantic reliability problem: proposer agents can generate production mutations, such as modifying IAM policies, opening firewall security groups, or executing data exports, that are syntactically valid and statically authorized but operationally unsafe.

Classical distributed consensus protocols replicate deterministic state transitions but do not evaluate the safety of the proposed intent.

To address this gap, we introduce Semantic Quorum Assurance (SQA), a control-plane primitive 

### AI 总结

总结生成失败

---

