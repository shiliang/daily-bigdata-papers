# 大数据+AI 领域论文日报

**日期**: 2026-04-20

**论文数量**: 6 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [CHOP: Chunkwise Context-Preserving ...](https://arxiv.org/abs/2604.15802v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Adapting in the Dark: Efficient and...](https://arxiv.org/abs/2604.15609v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [MoshiRAG: Asynchronous Knowledge Re...](https://arxiv.org/abs/2604.12928v2) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Training Time Prediction for Mixed ...](https://arxiv.org/abs/2604.16145v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Breaking the Training Barrier of Bi...](https://arxiv.org/abs/2604.15821v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [StoSignSGD: Unbiased Structural Sto...](https://arxiv.org/abs/2604.15416v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. CHOP: Chunkwise Context-Preserving Framework for RAG on Multi Documents

- **作者**: Hyunseok Park, Jihyeon Kim, Jongeun Kim, Dongsik Yoon
- **发布日期**: 2026-04-17
- **链接**: [arXiv:2604.15802v1](https://arxiv.org/abs/2604.15802v1) | [PDF](https://arxiv.org/pdf/2604.15802v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

Retrieval-Augmented Generation (RAG) systems lose retrieval accuracy when similar documents coexist in the vector database, causing unnecessary information, hallucinations, and factual errors.

To alleviate this issue, we propose CHOP, a framework that iteratively evaluates chunk relevance with Large Language Models (LLMs) and progressively reconstructs documents by determining their association with specific topics or query types.

CHOP integrates two key components: the CNM-Extractor, which generates compact per-chunk signatures capturing categories, key nouns, and model names, and the Continu

### AI 总结

总结生成失败

---

## 2. Adapting in the Dark: Efficient and Stable Test-Time Adaptation for Black-Box Models

- **作者**: Yunbei Zhang, Shuaicheng Niu, Chengyi Cai, Feng Liu, Jihun Hamm
- **发布日期**: 2026-04-17
- **链接**: [arXiv:2604.15609v1](https://arxiv.org/abs/2604.15609v1) | [PDF](https://arxiv.org/pdf/2604.15609v1)
- **分类**: cs.LG, cs.CV
- **含金量**: 20/43 分

### 摘要

Test-Time Adaptation (TTA) for black-box models accessible only via APIs remains a largely unexplored challenge.

Existing approaches such as post-hoc output refinement offer limited adaptive capacity, while Zeroth-Order Optimization (ZOO) enables input-space adaptation but faces high query costs and optimization challenges in the unsupervised TTA setting.

We introduce BETA (Black-box Efficient Test-time Adaptation), a framework that addresses these limitations by employing a lightweight, local white-box steering model to create a tractable gradient pathway.

Through a prediction harmonization t

### AI 总结

总结生成失败

---

## 3. MoshiRAG: Asynchronous Knowledge Retrieval for Full-Duplex Speech Language Models

- **作者**: Chung-Ming Chien, Manu Orsini, Eugene Kharitonov, Neil Zeghidour, Karen Livescu
- **发布日期**: 2026-04-14
- **链接**: [arXiv:2604.12928v2](https://arxiv.org/abs/2604.12928v2) | [PDF](https://arxiv.org/pdf/2604.12928v2)
- **分类**: cs.CL, eess.AS
- **含金量**: 20/43 分

### 摘要

Speech-to-speech language models have recently emerged to enhance the naturalness of conversational AI.

In particular, full-duplex models are distinguished by their real-time interactivity, including handling of pauses, interruptions, and backchannels.

However, improving their factuality remains an open challenge.

While scaling the model size could address this gap, it would make real-time inference prohibitively expensive.

In this work, we propose MoshiRAG, a modular approach that combines a compact full-duplex interface with selective retrieval to access more powerful knowledge sources.

Our 

### AI 总结

总结生成失败

---

## 4. Training Time Prediction for Mixed Precision-based Distributed Training

- **作者**: Minchul Kang, Changyong Shin, Jinwoo Jeong, Hyunho Lee, Younghun Go
- **发布日期**: 2026-04-17
- **链接**: [arXiv:2604.16145v1](https://arxiv.org/abs/2604.16145v1) | [PDF](https://arxiv.org/pdf/2604.16145v1)
- **分类**: cs.LG, cs.AI, cs.DC, cs.PF
- **含金量**: 20/43 分

### 摘要

Accurate prediction of training time in distributed deep learning is crucial for resource allocation, cost estimation, and job scheduling.

We observe that the floating-point precision setting is a key determinant of training time, leading to training time variations of ~2.4x over its minimum.

However, existing studies on distributed training time prediction rely on static model computation graphs that do not capture precision variations, including mixed precision.

According to our experiments, training time prediction without considering precision results in significant prediction errors - rea

### AI 总结

总结生成失败

---

## 5. Breaking the Training Barrier of Billion-Parameter Universal Machine Learning Interatomic Potentials

- **作者**: Yuanchang Zhou, Hongyu Wang, Yiming Du, Yan Wang, Mingzhen Li
- **发布日期**: 2026-04-17
- **链接**: [arXiv:2604.15821v1](https://arxiv.org/abs/2604.15821v1) | [PDF](https://arxiv.org/pdf/2604.15821v1)
- **分类**: cs.DC, cs.LG
- **含金量**: 20/43 分

### 摘要

Universal Machine Learning Interatomic Potentials (uMLIPs), pre-trained on massively diverse datasets encompassing inorganic materials and organic molecules across the entire periodic table, serve as foundational models for quantum-accurate physical simulations.

However, uMLIP training requires second-order derivatives, which lack corresponding parallel training frameworks; moreover, scaling to the billion-parameter regime causes explosive growth in computation and communication overhead, making its training a tremendous challenge.

We introduce MatRIS-MoE, a billion-parameter Mixture-of-Expert

### AI 总结

总结生成失败

---

## 6. StoSignSGD: Unbiased Structural Stochasticity Fixes SignSGD for Training Large Language Models

- **作者**: Dingzhi Yu, Rui Pan, Yuxing Liu, Tong Zhang
- **发布日期**: 2026-04-16
- **链接**: [arXiv:2604.15416v1](https://arxiv.org/abs/2604.15416v1) | [PDF](https://arxiv.org/pdf/2604.15416v1)
- **分类**: cs.LG, cs.AI, math.OC
- **含金量**: 20/43 分

### 摘要

Sign-based optimization algorithms, such as SignSGD, have garnered significant attention for their remarkable performance in distributed learning and training large foundation models.

Despite their empirical superiority, SignSGD is known to diverge on non-smooth objectives, which are ubiquitous in modern machine learning due to ReLUs, max-pools, and mixture-of-experts.

To overcome this fundamental limitation, we propose \textbf{StoSignSGD}, an algorithm that injects structural stochasticity into the sign operator while maintaining an unbiased update step.

In the regime of (online) convex optim

### AI 总结

总结生成失败

---

