# 大数据+AI 领域论文日报

**日期**: 2026-06-10

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Flaws in the LLM Automation Narrati...](https://arxiv.org/abs/2606.11166v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Unifying Local Communications and L...](https://arxiv.org/abs/2606.11081v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Dep-LLM: Training-Free Depression D...](https://arxiv.org/abs/2606.10796v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Unifying Data, Memory, and Compute ...](https://arxiv.org/abs/2606.10706v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Divide and Cooperate: Role-Decompos...](https://arxiv.org/abs/2606.10684v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [RATrain: A Resource-Aware Training ...](https://arxiv.org/abs/2606.10415v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [From Stacks to Circuits: A Regenera...](https://arxiv.org/abs/2606.10544v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [TacForeSight: Force-Guided Tactile ...](https://arxiv.org/abs/2606.11184v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Lip Forcing: Few-Step Autoregressiv...](https://arxiv.org/abs/2606.11180v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Piper: A Programmable Distributed T...](https://arxiv.org/abs/2606.11169v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Flaws in the LLM Automation Narrative

- **作者**: George Perrett, Javae Elliott, Jennifer Hill, Marc Scott
- **发布日期**: 2026-06-09
- **链接**: [arXiv:2606.11166v1](https://arxiv.org/abs/2606.11166v1) | [PDF](https://arxiv.org/pdf/2606.11166v1)
- **分类**: stat.OT, cs.AI
- **含金量**: 20/43 分

### 摘要

Large Language Models (LLMs) are increasingly described as performing at the level of human experts on knowledge economy tasks.

These claims are primarily based on how LLMs perform on benchmarking tasks that measure average performance across standardized datasets.

Primary limitations of many benchmarking tasks are that they often measure performance based on content directly included in LLM training data, and they frequently do not assess the reliability of LLM performance or the magnitude of LLM errors.

However, in high stakes contexts, these qualities are critically important.

Through a nov

### AI 总结

总结生成失败

---

## 2. Unifying Local Communications and Local Updates for LLM Pretraining

- **作者**: Pietro Cagnasso, Eugene Belilovsky, Edouard Oyallon
- **发布日期**: 2026-06-09
- **链接**: [arXiv:2606.11081v1](https://arxiv.org/abs/2606.11081v1) | [PDF](https://arxiv.org/pdf/2606.11081v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

Communication-efficient pre-training of LLMs is increasingly important as training draws on compute distributed across clusters, data centers, and lower-bandwidth links.

Many practical methods reduce communication frequency but still rely on synchronous All-Reduce operations that maintain identical model states and tie progress to global collectives.

This can become a bottleneck when bandwidth or worker speed is heterogeneous.

We introduce GASLoC, a novel decentralized pre-training algorithm that generalizes the notion of communication acceleration to the recently popular "outer optimizer" to 

### AI 总结

总结生成失败

---

## 3. Dep-LLM: Training-Free Depression Diagnosis via Evidence-Guided Structured Multi-factor with Reliable LLM Reasoning

- **作者**: Yiqing Lyu, Xianbing Zhao, Buzhou Tang, Ronghuan Jiang
- **发布日期**: 2026-06-09
- **链接**: [arXiv:2606.10796v1](https://arxiv.org/abs/2606.10796v1) | [PDF](https://arxiv.org/pdf/2606.10796v1)
- **分类**: cs.CL, cs.AI
- **含金量**: 20/43 分

### 摘要

Automatic Depression Detection (ADD) from clinical interviews is a pivotal task in computational mental health, yet it remains challenging due to two critical obstacles: 1) difficulty in modeling complex but sparsely distributed depression clues within lengthy, multi-topic clinical interviews, leading to superficial and unreliable reasoning; 2) scarcity of labeled data due to clinical privacy, together with high cost of training and fine-tuning, limiting the deployment of supervised ADD systems.

To jointly address these challenges, we propose Dep-LLM, a training-free framework that mirrors the

### AI 总结

总结生成失败

---

## 4. Unifying Data, Memory, and Compute Efficiency in LLM training: A Survey

- **作者**: Vanessa Schmidt, Huy Hoang Nguyen, Cédric Jung, Shirin Salehi, Anke Schmeink
- **发布日期**: 2026-06-09
- **链接**: [arXiv:2606.10706v1](https://arxiv.org/abs/2606.10706v1) | [PDF](https://arxiv.org/pdf/2606.10706v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

Resource constraints increasingly determine what can be trained, fine-tuned, and deployed in large language models (LLMs), yet efficiency is often studied through isolated techniques rather than as an interacting system of limits.

This survey adopts a constraint-centric perspective and organizes recent progress around three coupled bottlenecks: data efficiency (what to train on), memory efficiency (how to fit training), and compute budget awareness (when and where to spend FLOPs).

On the data axis, we review selection and pruning methods that maximize learning per token, ranging from scalable 

### AI 总结

总结生成失败

---

## 5. Divide and Cooperate: Role-Decomposed Multi-Agent LLM Training with Cross-Agent Learning Signals

- **作者**: Jaewan Park, Solbee Cho, Jay-Yoon Lee
- **发布日期**: 2026-06-09
- **链接**: [arXiv:2606.10684v1](https://arxiv.org/abs/2606.10684v1) | [PDF](https://arxiv.org/pdf/2606.10684v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

Modern language agents which perform multi-step reasoning have shown strong performance in knowledge-intensive question answering.

However, existing approaches typically couple evidence acquisition and answer generation within a single policy.

This forces a single model to play multiple potentially conflicting roles, inducing a combinatorial explosion in the policy space and hindering efficient exploration.

It also introduces a credit assignment problem during training: a search action that retrieves sufficient evidence may still be penalized when generation fails, and vice versa.

We propose D

### AI 总结

总结生成失败

---

## 6. RATrain: A Resource-Aware Training Runtime for Large Language Models on Bandwidth-Constrained Heterogeneous Supercomputing Platforms

- **作者**: Yao Lu, Shiqing Ma, Zhongzhi Luan, Gen Li, Jiaxing Qi
- **发布日期**: 2026-06-09
- **链接**: [arXiv:2606.10415v1](https://arxiv.org/abs/2606.10415v1) | [PDF](https://arxiv.org/pdf/2606.10415v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Production heterogeneous supercomputing platforms are increasingly used to host large language model (LLM) training workloads.

However, existing GPU-oriented training runtimes typically rely on high-bandwidth device memory, fast interconnects, and mature collective communication libraries, making them difficult to directly adapt to MT-3000, a platform with an explicit memory hierarchy, limited usable DDR capacity, and constrained inter-cluster communication.

This paper presents RATrain, a resource-aware training runtime for dense LLMs on bandwidth-constrained heterogeneous supercomputing platf

### AI 总结

总结生成失败

---

## 7. From Stacks to Circuits: A Regenerative Socio-Technical Roadmap for AI Infrastructure within Planetary Boundaries

- **作者**: Han-Teng Liao, Karen Ang
- **发布日期**: 2026-06-09
- **链接**: [arXiv:2606.10544v1](https://arxiv.org/abs/2606.10544v1) | [PDF](https://arxiv.org/pdf/2606.10544v1)
- **分类**: cs.SI, cs.CY, cs.NI, econ.GN, eess.SY
- **含金量**: 20/43 分

### 摘要

Current scaling trajectories for Generative AI, typified by linear supply-side "stacks," prioritize performance density while externalizing significant thermodynamic and material costs.

As the "Twin Transition" of green and digital transformation accelerates, the industry faces technology gaps - including Scope 3 emissions and e-waste recycling - that impede sustainable scaling and lead to social tensions.

This study proposes a Regenerative Socio-Technical roadmap that repurposes the Sustainable Production and Consumption system map to reframe artificial intelligence infrastructure as a system

### AI 总结

总结生成失败

---

## 8. TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation

- **作者**: Yujie Zang, Yuhang Zheng, Xian Nie, Yupeng Zheng, Shuai Tian
- **发布日期**: 2026-06-09
- **链接**: [arXiv:2606.11184v1](https://arxiv.org/abs/2606.11184v1) | [PDF](https://arxiv.org/pdf/2606.11184v1)
- **分类**: cs.RO
- **含金量**: 20/43 分

### 摘要

Contact-rich manipulation requires robots to continuously perceive and regulate evolving physical interactions under dynamic contact transitions or complex surface geometries.

Recent imitation learning methods improve contact-aware control by incorporating tactile or force feedback, but they rarely model the asymmetric spatiotemporal roles of global force and local tactile sensing.

To address this, we propose TacForeSight, a lightweight force-conditioned tactile foresight framework for real-time manipulation.

The core component is TacForceWM, a tactile world model that predicts short-horizon t

### AI 总结

总结生成失败

---

## 9. Lip Forcing: Few-Step Autoregressive Diffusion for Real-time Lip Synchronization

- **作者**: Paul Hyunbin Cho, Jinhyuk Jang, SeokYoung Lee, Joungbin Lee, Siyoon Jin
- **发布日期**: 2026-06-09
- **链接**: [arXiv:2606.11180v1](https://arxiv.org/abs/2606.11180v1) | [PDF](https://arxiv.org/pdf/2606.11180v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

Diffusion-based lip synchronization models achieve strong visual quality and audio-visual alignment, but full-sequence bidirectional attention and many denoising steps make them impractical for real-time inference.

We present Lip Forcing, to our knowledge the first autoregressive diffusion method for video-to-video (V2V) lip synchronization, which distills a 14B audio-conditioned bidirectional video diffusion teacher into causal students.

At inference, the students generate each chunk in only two denoising steps without inference-time CFG, enabling real-time lip synchronization.

A lip-sync-spe

### AI 总结

总结生成失败

---

## 10. Piper: A Programmable Distributed Training System

- **作者**: Megan Frisella, Shubham Tiwari, Andy Ruan, Yi Pan, Parker Gustafson
- **发布日期**: 2026-06-09
- **链接**: [arXiv:2606.11169v1](https://arxiv.org/abs/2606.11169v1) | [PDF](https://arxiv.org/pdf/2606.11169v1)
- **分类**: cs.DC, cs.AI
- **含金量**: 20/43 分

### 摘要

Large-scale model training increasingly relies on composing multiple parallelism strategies, such as data, pipeline, and expert parallelism, together with memory-saving optimizations like ZeRO.

Deployed systems for foundation model pretraining often rely on human experts to manually design a high-level parallelism strategy then implement the corresponding low-level execution strategy, making it difficult to adapt the system to new strategies.

Meanwhile, many general-purpose frameworks are more flexible but their implementations are still tied to a fixed set of common parallelism strategies, ma

### AI 总结

总结生成失败

---

