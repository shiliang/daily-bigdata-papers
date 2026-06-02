# 大数据+AI 领域论文日报

**日期**: 2026-06-02

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [CHIMERA: A Flexible and Scalable 3....](https://arxiv.org/abs/2606.02358v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Unveiling the Entropy Dynamics of C...](https://arxiv.org/abs/2606.02020v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Flexible Online Representation Lear...](https://arxiv.org/abs/2606.01546v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Learning from Saturated Data: Signa...](https://arxiv.org/abs/2606.01436v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Training-Free Imitation Learning wi...](https://arxiv.org/abs/2606.01238v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Large Language Models in Transporta...](https://arxiv.org/abs/2606.00991v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Lodestar: An Online-Learning LLM In...](https://arxiv.org/abs/2606.00946v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Memory-Efficient LLM Training with ...](https://arxiv.org/abs/2606.00888v1) | 待分析 | 评估失败 | [Code](https://github.com/QiaoXiao7282/SMET.) | 20/43 |
| 9 | [EMA: Approximate Nearest Neighbor S...](https://arxiv.org/abs/2606.00734v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Benchmarking Recursive-Collapse War...](https://arxiv.org/abs/2606.00329v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. CHIMERA: A Flexible and Scalable 3.1 TOPS/W AI-MCU with Transformer Accelerator and 563 Gb/s Shared-L2 Memory Subsystem with QoS Guarantees

- **作者**: Lorenzo Leone, Philip Wiese, Gamze İslamoğlu, Michael Rogenmoser, Davide Rossi
- **发布日期**: 2026-06-01
- **链接**: [arXiv:2606.02358v1](https://arxiv.org/abs/2606.02358v1) | [PDF](https://arxiv.org/pdf/2606.02358v1)
- **分类**: cs.AR
- **含金量**: 20/43 分

### 摘要

We present Chimera, a flexible and scalable Microcontroller Unit (MCU) designed to accelerate real-time inference of rapidly evolving transformer-based models at the ultra-low-power edge (hundred of mW).

The chip, implemented in 22 nm FDX technology, integrates a transformer accelerator tightly coupled within a compute cluster featuring nine general-purpose RV32IMA cores.

Scalability extends to the memory hierarchy through a novel L2 memory island subsystem, which enables data sharing across multiple clusters while delivering 563 Gb/s aggregate bandwidth.

The L2 subsystem enforces quality-of-s

### AI 总结

总结生成失败

---

## 2. Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning

- **作者**: Ting Xu, Xu He, Yupu Lu, Jiankai Sun, Dong Li
- **发布日期**: 2026-06-01
- **链接**: [arXiv:2606.02020v1](https://arxiv.org/abs/2606.02020v1) | [PDF](https://arxiv.org/pdf/2606.02020v1)
- **分类**: cs.CL, cs.LG
- **含金量**: 20/43 分

### 摘要

This paper investigates the entropy dynamics of Chain-of-Thought (CoT) and uncovers a consistent two-phase structure: an Uncertainty Region of exploration transitioning sharply to a Confidence Region of convergence.

We demonstrate that the Confidence Region possesses two critical properties: 1) High Reliability -- answers in the confidence region become highly accurate and stable, and 2) High Redundancy -- models generate unnecessary tokens long after reaching the correct answer.

These properties unlock more efficient and reliable inference strategies: 1) Early Exit leverages reliability and r

### AI 总结

总结生成失败

---

## 3. Flexible Online Representation Learning Based on Similarity Matching

- **作者**: Shagesh Sridharan, Yanis Bahroun, Anirvan M. Sengupta
- **发布日期**: 2026-06-01
- **链接**: [arXiv:2606.01546v1](https://arxiv.org/abs/2606.01546v1) | [PDF](https://arxiv.org/pdf/2606.01546v1)
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

## 4. Learning from Saturated Data: Signals Beyond Correctness for LLM Training

- **作者**: Hanno Hiss, Jasper Dekoninck, Martin Vechev
- **发布日期**: 2026-05-31
- **链接**: [arXiv:2606.01436v1](https://arxiv.org/abs/2606.01436v1) | [PDF](https://arxiv.org/pdf/2606.01436v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

The growing capabilities of large language models (LLMs) have led to the saturation of many benchmarks and training datasets used to improve them.

Motivated by this, we investigate whether questions solved with perfect empirical accuracy can nevertheless be used to improve downstream performance.

To do so, we replace binary correctness with two sources of more fine-grained quality signals: (1) pairwise LLM self-judgments, in which the model evaluates the relative quality of its own solutions, and (2) token-level entropy, where token-level uncertainty is used as a proxy for solution quality.

We

### AI 总结

总结生成失败

---

## 5. Training-Free Imitation Learning with Closed-Form Diffusion Policies

- **作者**: Raghav Mishra, Ian R. Manchester
- **发布日期**: 2026-05-31
- **链接**: [arXiv:2606.01238v1](https://arxiv.org/abs/2606.01238v1) | [PDF](https://arxiv.org/pdf/2606.01238v1)
- **分类**: cs.RO, cs.LG
- **含金量**: 20/43 分

### 摘要

While diffusion-based policies have impressive performance and expressivity, their long offline training slows down the data collection and policy deployment loop.

We introduce Closed-Form Diffusion Policies, a class of training-free diffusion-based policies for imitation learning using the closed-form score derived from the demonstration dataset.

We deploy CFDP with real-time inference with a mobile CPU in hardware experiments, showing it can successfully perform imitation directly from the dataset in milliseconds and with faster inference than neural diffusion policies.

In experiments on imi

### AI 总结

总结生成失败

---

## 6. Large Language Models in Transportation Systems Management and Operations: From Text Reasoning to Multi-modal Decision Support

- **作者**: Siyan Li, Zehao Wang, Jiachen Li, Kanok Boriboonsomsin, Matthew J. Barth
- **发布日期**: 2026-05-31
- **链接**: [arXiv:2606.00991v1](https://arxiv.org/abs/2606.00991v1) | [PDF](https://arxiv.org/pdf/2606.00991v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

Transportation systems management and operations (TSMO) increasingly depends on timely interpretation of heterogeneous data, from various sensor streams, incident reports, traveler feedback, and visual observations.

Large language models (LLMs), including emerging multi-modal large language models (MM-LLMs), provide a new mechanism for integrating these structured and unstructured inputs into operator-facing decision support.

This survey paper reviews LLM- and MM-LLM-based applications in TSMO across three domains: transportation operations & services (supply), mobility & fleet services (deman

### AI 总结

总结生成失败

---

## 7. Lodestar: An Online-Learning LLM Inference Router

- **作者**: Gangmuk Lim, Wanyu Zhao, Brighten Godfrey, Jiaxin Shan, Le Xu
- **发布日期**: 2026-05-31
- **链接**: [arXiv:2606.00946v1](https://arxiv.org/abs/2606.00946v1) | [PDF](https://arxiv.org/pdf/2606.00946v1)
- **分类**: cs.DC, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

Efficiently serving large language model (LLM) inference tasks is crucial both for user-perceived latency such as time-to-first-token (TTFT) and for GPU utilization.

However, LLM request routing, that is, assigning each inference request to a GPU instance, is particularly challenging: execution is highly input-dependent; batching and KV-cache reuse create strong cross-request coupling; and latency responds nonlinearly to context length, model/engine settings, and heterogeneous accelerators.

As a result, simple traditional load balancing algorithms, and even heuristics tailored for LLM inferenc

### AI 总结

总结生成失败

---

## 8. Memory-Efficient LLM Training with Dynamic Sparsity: From Stability to Practical Scaling

- **作者**: Qiao Xiao, Boqian Wu, Patrik Okanovic, Tomasz Sternal, Maurice van Keulen
- **发布日期**: 2026-05-30
- **链接**: [arXiv:2606.00888v1](https://arxiv.org/abs/2606.00888v1) | [PDF](https://arxiv.org/pdf/2606.00888v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/QiaoXiao7282/SMET.) ⭐ 0

### 摘要

Dynamic Sparse Training (DST) offers a promising paradigm for improving the training and inference efficiency of deep neural networks; however, we find that in large language model training, DST can suffer from optimization instability, manifested as loss spikes after topology updates.

In this work, we show that the naive use of standard Adam-based optimizers leads to a cold-start issue for newly regrown parameters, resulting in excessively large updates and disrupted training dynamics.

To address this issue, we propose Sparse Memory-Efficient Training (SMET), which stabilizes DST with optimiz

### AI 总结

总结生成失败

---

## 9. EMA: Approximate Nearest Neighbor Search with General Attribute Filtering and Dynamic Updates

- **作者**: Mocheng Li, Baotong Lu, James Cheng, Chenhao Ma
- **发布日期**: 2026-05-30
- **链接**: [arXiv:2606.00734v1](https://arxiv.org/abs/2606.00734v1) | [PDF](https://arxiv.org/pdf/2606.00734v1)
- **分类**: cs.DB
- **含金量**: 20/43 分

### 摘要

Filtering Approximate Nearest Neighbor (FANN) search is a critical and emerging task for strengthening the query capability of vector databases, supporting applications such as recommendation systems, retrieval-augmented generation (RAG), and agent memory.

However, most existing methods are limited to range or label filtering, often incurring unacceptable index construction time and memory overhead.

Predicate-agnostic approaches further struggle to handle a wide range of predicate selectivities effectively.

In this paper, we propose EMA, a filtering ANN algorithm that supports multi-predicate 

### AI 总结

总结生成失败

---

## 10. Benchmarking Recursive-Collapse Warning Claims Under Matched False-Positive Control

- **作者**: David Mullett
- **发布日期**: 2026-05-29
- **链接**: [arXiv:2606.00329v1](https://arxiv.org/abs/2606.00329v1) | [PDF](https://arxiv.org/pdf/2606.00329v1)
- **分类**: eess.SY, cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

Recursive systems can enter collapse-like regimes -- self-reinforcing amplification, persistent recursion, and narrowing diversity that mask accelerating internal degradation -- before overt failure becomes visible.

We introduce Loopzero, a claim-bounded benchmark framework for testing whether recursive failures follow a directional telemetry pattern: rising gain (G), recursive persistence (p), and declining diversity ($δ$).

The claim boundary is specified in Lean; the Lean artifact does not verify real telemetry, benchmark validity, or detector performance.

We evaluate the bridge on two fro

### AI 总结

总结生成失败

---

