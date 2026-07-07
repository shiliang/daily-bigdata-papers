# 大数据+AI 领域论文日报

**日期**: 2026-07-07

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Unified Audio Intelligence Without ...](https://arxiv.org/abs/2607.05196v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Train Smarter, Not Longer: Memoriza...](https://arxiv.org/abs/2607.04969v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Direct Model State Migration for El...](https://arxiv.org/abs/2607.04749v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Exploiting Structural Properties fo...](https://arxiv.org/abs/2607.04630v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Hybrid privacy-aware semantic searc...](https://arxiv.org/abs/2606.26373v3) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [CausticFlow: An Efficient Machine L...](https://arxiv.org/abs/2607.04955v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [GORIO: GPU-Centered Remote I/O for ...](https://arxiv.org/abs/2607.04415v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [ViPo-MLLM: Visual-Pose Multimodal L...](https://arxiv.org/abs/2607.03657v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Enactive Drift Regulation and the E...](https://arxiv.org/abs/2607.03834v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [A Memory Efficient Unified Algorith...](https://arxiv.org/abs/2607.02050v2) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Unified Audio Intelligence Without Regressing on Text Intelligence

- **作者**: Zhifeng Kong, Sang-gil Lee, Jaehyeon Kim, Boxin Wang, Zihan Liu
- **发布日期**: 2026-07-06
- **链接**: [arXiv:2607.05196v1](https://arxiv.org/abs/2607.05196v1) | [PDF](https://arxiv.org/pdf/2607.05196v1)
- **分类**: cs.CL, cs.AI, cs.LG, cs.SD, eess.AS
- **含金量**: 20/43 分

### 摘要

Audio intelligence involves understanding, reasoning about, and generating both audio and speech.

In this work, we introduce Nemotron-Labs-Audex-30B-A3B (Audex), a unified audio-text LLM built on Nemotron-Cascade-2-30B-A3B, a strong text-only MoE LLM.

Audex adopts a simple unified design with a single Transformer decoder: audio inputs are encoded and projected into the text embedding space, while text tokens and quantized audio output tokens are treated uniformly during generation.

This architecture enables strong audio-text fusion, seamless multimodal generation, and compatibility with standa

### AI 总结

总结生成失败

---

## 2. Train Smarter, Not Longer: Memorization-Guided Data Reuse for Efficient LLM Training

- **作者**: Jingwei Zuo, Cong Zeng, Ilyas Chahed, Maksim Velikanov, Dhia Eddine Rhaiem
- **发布日期**: 2026-07-06
- **链接**: [arXiv:2607.04969v1](https://arxiv.org/abs/2607.04969v1) | [PDF](https://arxiv.org/pdf/2607.04969v1)
- **分类**: cs.LG, cs.CL
- **含金量**: 20/43 分

### 摘要

The training paradigm of large language models has shifted from traditional one-pass training to multi-epoch training, as reasonable reuse of limited high-quality data can improve both model performance and sample efficiency.

Meanwhile, excessive repetition introduces the risk of overfitting and diminishing returns.

Determining when and how to reuse data effectively thus emerges as a natural but under-explored question.

Through a novel observation of model's "Memorization Window" signals derived from loss retention dynamics and downstream evaluation scores, we propose "Memorization-guided Data

### AI 总结

总结生成失败

---

## 3. Direct Model State Migration for Elastic Training of Large Language Models

- **作者**: Weijian Liu, Mingzhen Li, Rui Kang, Chen Sun, Guangming Tan
- **发布日期**: 2026-07-06
- **链接**: [arXiv:2607.04749v1](https://arxiv.org/abs/2607.04749v1) | [PDF](https://arxiv.org/pdf/2607.04749v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Large language model (LLM) training shall adapt to dynamic resources in shared clusters to tackle the elasticity, including passive preemption and optimistic scaling.

State migration across device sets is required when altering the hybrid-parallel configuration due to dynamic resources.

Existing solutions rely on checkpoint-based mechanisms, which persist complete states to storage for resuming with re-assigned resources, forcing all GPUs to stall when transferring model states.

Despite optimization efforts, checkpoint-based solutions incur prohibitive latency due to data movement across memor

### AI 总结

总结生成失败

---

## 4. Exploiting Structural Properties for Efficient Constraint-Aware HNSW Hyperparameter Tuning

- **作者**: Geon Choi, Hoeun Lee, Jaeyoung Do
- **发布日期**: 2026-07-06
- **链接**: [arXiv:2607.04630v1](https://arxiv.org/abs/2607.04630v1) | [PDF](https://arxiv.org/pdf/2607.04630v1)
- **分类**: cs.DB
- **含金量**: 20/43 分

### 摘要

Vector databases (VectorDBs) are a core component of modern retrieval systems, including Retrieval-Augmented Generation (RAG), where efficient Approximate Nearest Neighbor Search (ANNS) is critical.

Among ANNS algorithms, Hierarchical Navigable Small World (HNSW) graphs are widely adopted for their strong recalllatency trade-off.

However, configuring HNSW remains challenging: its hyperparameters jointly affect search quality, latency, build time, and index size in nonlinear ways, while production deployments impose strict resource and tuning-time constraints.We study HNSW hyperparameter tuning

### AI 总结

总结生成失败

---

## 5. Hybrid privacy-aware semantic search: SVD-truncated document geometry and CKKS-encrypted query reranking under a restricted threat model

- **作者**: Sergey Kurilenko
- **发布日期**: 2026-06-24
- **链接**: [arXiv:2606.26373v3](https://arxiv.org/abs/2606.26373v3) | [PDF](https://arxiv.org/pdf/2606.26373v3)
- **分类**: cs.CR, cs.AI, cs.IR
- **含金量**: 20/43 分

### 摘要

Dense embeddings power semantic search and Retrieval-Augmented Generation, yet a leaked vector database leaks the text behind it, since embeddings invert with high fidelity.

The textbook defences are extreme--homomorphic search is sound but far too slow at million-document scale, while privacy noise degrades ranking before it protects.

We study a middle path built on an asymmetry: each static document vector is SVD-truncated and then rotated by a secret orthogonal transform held only by the data owner, while the dynamic query is protected cryptographically under CKKS, so an honest-but-curious 

### AI 总结

总结生成失败

---

## 6. CausticFlow: An Efficient Machine Learning Framework Combining Neural Differential Equations and Normalizing Flows for Binary Microlensing Parameter Inference

- **作者**: Haibin Ren, Wei Zhu
- **发布日期**: 2026-07-06
- **链接**: [arXiv:2607.04955v1](https://arxiv.org/abs/2607.04955v1) | [PDF](https://arxiv.org/pdf/2607.04955v1)
- **分类**: astro-ph.IM, astro-ph.EP, astro-ph.GA, astro-ph.SR
- **含金量**: 20/43 分

### 摘要

We introduce CausticFlow, a machine learning framework that combines neural controlled differential equations with normalizing flows to infer binary microlensing parameters.

This architecture naturally handles irregularly sampled time series and data gaps while flexibly capturing strongly correlated and multimodal posterior distributions.

Trained on simulated KMTNet-like light curves, CausticFlow generates posterior samples in a fraction of a second, with maximum-a-posteriori estimates achieving typical precisions of $\sim17\%$ for the mass ratio $q$ and $\sim3\%$ for the projected separation 

### AI 总结

总结生成失败

---

## 7. GORIO: GPU-Centered Remote I/O for Graph ANNS over NVMe-oF

- **作者**: Gen Zhang, Wenhao Gu
- **发布日期**: 2026-07-05
- **链接**: [arXiv:2607.04415v1](https://arxiv.org/abs/2607.04415v1) | [PDF](https://arxiv.org/pdf/2607.04415v1)
- **分类**: cs.DC, cs.DB
- **含金量**: 20/43 分

### 摘要

Graph-based approximate nearest neighbor search (ANNS) is increasingly used in vector databases and retrieval-augmented generation services, but large vector indexes often exceed the memory capacity of a single GPU server.

NVMe over Fabrics (NVMe-oF) provides an attractive storage-disaggregation substrate, yet existing remote storage paths are still largely CPU-centered: the CPU forms I/O requests, drives transport progress, and determines when GPU computation can resume.

This organization is poorly matched to graph ANNS, where the next data access is discovered inside GPU graph traversal.

T

### AI 总结

总结生成失败

---

## 8. ViPo-MLLM: Visual-Pose Multimodal LLM for Gloss-Free Sign Language Translation

- **作者**: Ahmed Abul Hasanaath, Bicheng Xu, Mir Rayat Imtiaz Hossain, Leonid Sigal, Hamzah Luqman
- **发布日期**: 2026-07-04
- **链接**: [arXiv:2607.03657v1](https://arxiv.org/abs/2607.03657v1) | [PDF](https://arxiv.org/pdf/2607.03657v1)
- **分类**: cs.CV, cs.AI
- **含金量**: 20/43 分

### 摘要

Gloss-free Sign Language Translation (SLT) translates sign language videos into spoken-language sentences without gloss annotations, avoiding costly labeling but requiring fine-grained modeling of hands, body, and facial cues.

Existing methods often use single-modality or weakly fused features, limiting performance.

We propose ViPo-MLLM, a framework that integrates spatio-temporal RGB and human pose features.

Dedicated encoders model intra-modal dynamics and cross-modal attention captures long-range dependencies.

The fused representation is conditioned with a structured prompt and processed by

### AI 总结

总结生成失败

---

## 9. Enactive Drift Regulation and the Emergence Machine: A Framework for Coherent Adaptation Through Regulated Interaction

- **作者**: Nicholas Davis
- **发布日期**: 2026-07-04
- **链接**: [arXiv:2607.03834v1](https://arxiv.org/abs/2607.03834v1) | [PDF](https://arxiv.org/pdf/2607.03834v1)
- **分类**: cs.HC
- **含金量**: 20/43 分

### 摘要

Adaptive systems increasingly operate in environments characterized by persistent non-stationarity, where patterns reorganize rather than merely vary.

While existing approaches such as online learning, continual learning, and adaptive filtering address performance degradation under changing data distributions, they typically treat drift as noise, error, or distribution shift to be corrected.

This paper argues that such framings miss a more fundamental challenge: the loss of organizational coherence over time.

We introduce Enactive Drift Regulation (EDR) as a general adaptive principle that tre

### AI 总结

总结生成失败

---

## 10. A Memory Efficient Unified Algorithm for Online Learning of Linear Dynamical Systems

- **作者**: Yuval Ran-Milo, Angelos Assos, Elad Hazan
- **发布日期**: 2026-07-02
- **链接**: [arXiv:2607.02050v2](https://arxiv.org/abs/2607.02050v2) | [PDF](https://arxiv.org/pdf/2607.02050v2)
- **分类**: cs.LG, eess.SY
- **含金量**: 20/43 分

### 摘要

Motivated by the challenge of stabilizing a general unknown linear dynamical system (LDS) from observations, we study the natural prerequisite of online prediction.

Our goal is to achieve sublinear regret with a memory footprint that adapts to the intrinsic complexity of the dynamics rather than the full hidden-state dimension.

We focus on the practically central regime of systems with low instability complexity -- eigenvalues outside the real stable interval that do not decay rapidly, together with non-semisimple modes -- potentially embedded in an otherwise stable real spectrum of much highe

### AI 总结

总结生成失败

---

