# 大数据+AI 领域论文日报

**日期**: 2026-06-18

**论文数量**: 9 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [BLADE: Scalable Bi-level Adaptive D...](https://arxiv.org/abs/2606.18650v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [On the Memorization Behavior of LLM...](https://arxiv.org/abs/2606.17276v2) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [PYPILINE: Malicious PyPI Package De...](https://arxiv.org/abs/2606.19063v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [A Mixed-Reality Testbed for Autonom...](https://arxiv.org/abs/2606.19267v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Online Distributional Prediction vi...](https://arxiv.org/abs/2606.18778v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Splaxel: Efficient Distributed Trai...](https://arxiv.org/abs/2606.18588v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [ReMP: Low-Downtime Runtime Model-Pa...](https://arxiv.org/abs/2606.18741v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Ghost Vectors: Soft-Deleted Embeddi...](https://arxiv.org/abs/2606.18497v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [A Critical Discourse Analysis of Ge...](https://arxiv.org/abs/2606.18423v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training

- **作者**: Jiaxing Wang, Deping Xiang, Jin Xu, Zirui Liu, Zicheng Zhang
- **发布日期**: 2026-06-17
- **链接**: [arXiv:2606.18650v1](https://arxiv.org/abs/2606.18650v1) | [PDF](https://arxiv.org/pdf/2606.18650v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

As Large Language Model (LLM) datasets scale to trillions of tokens, data selection has emerged as a critical frontier to filter out uninformative noise and construct adaptive learning trajectories.

Beyond static heuristic filtering, advanced data selection methods for LLM training largely follow two paradigms, each with fundamental limitations.

Influence-based methods provide principled bi-level objectives but require intractable inverse-Hessian computations, while excess-loss methods are computationally efficient but rely on a static reference model that becomes misaligned with the evolving 

### AI 总结

总结生成失败

---

## 2. On the Memorization Behavior of LLMs in Generative Recommendation: Observations, Implications, and Training Strategies

- **作者**: Sunwoo Kim, Sunkyung Lee, Clark Mingxuan Ju, Donald Loveland, Bhuvesh Kumar
- **发布日期**: 2026-06-15
- **链接**: [arXiv:2606.17276v2](https://arxiv.org/abs/2606.17276v2) | [PDF](https://arxiv.org/pdf/2606.17276v2)
- **分类**: cs.IR, cs.LG
- **含金量**: 20/43 分

### 摘要

Generative recommendation (GR) has emerged as a promising direction for recommender systems.

Recently, large language models (LLMs) have been increasingly adopted for GR, as their rich pretrained knowledge is expected to help them generalize beyond common user behavior patterns that traditional memorization-oriented baselines can capture.

However, existing LLM-based GR works largely ignore LLMs' well-known tendency to memorize, which, if present in LLMs fine-tuned for GR, would restrict their utilization of pretrained knowledge.

In this work, we investigate this concern by examining one-hop me

### AI 总结

总结生成失败

---

## 3. PYPILINE: Malicious PyPI Package Detection via Suspicious API Knowledge and Agent Workflow

- **作者**: Siyuan Pang, Zhengwei Jiang, Yepeng Yao, Zijing Fan, Haozhe Li
- **发布日期**: 2026-06-17
- **链接**: [arXiv:2606.19063v1](https://arxiv.org/abs/2606.19063v1) | [PDF](https://arxiv.org/pdf/2606.19063v1)
- **分类**: cs.CR
- **含金量**: 20/43 分

### 摘要

The detection of malicious PyPI packages is crucial for maintaining the security of the open source software supply chain.

Existing methods, which primarily rely on rules or traditional machine learning, suffer from poor interpretability and difficulty in adapting to novel attacks.

To address this, we propose PYPILINE, a novel detection method that combines a suspicious API knowledge base with an Agent workflow.

PYPILINE first conducts static analysis on known malicious packages, extracting abstract syntax trees and generating API call graphs, from which it automatically extracts and construct

### AI 总结

总结生成失败

---

## 4. A Mixed-Reality Testbed for Autonomous Vehicles

- **作者**: H. M. Sabbir Ahmad, Ehsan Sabouni, Emrullah Celik, Zean Wan, Damola Ajeyemi
- **发布日期**: 2026-06-17
- **链接**: [arXiv:2606.19267v1](https://arxiv.org/abs/2606.19267v1) | [PDF](https://arxiv.org/pdf/2606.19267v1)
- **分类**: cs.RO, eess.SY
- **含金量**: 20/43 分

### 摘要

We propose a mixed-reality, hardware-in-the-loop (HIL) testbed for autonomous vehicles that seamlessly integrates a physical testbed of mobile robots with a high-fidelity simulation environment.

The virtual simulation enables the creation of diverse, safety-critical driving scenarios to validate state-of-the-art perception, planning, and control algorithms, while augmenting simulations with physical robots equipped with multimodal sensors in photorealistic virtual environments further facilitating rigorous validation.

Our testbed also features vehicular connectivity using wireless communicatio

### AI 总结

总结生成失败

---

## 5. Online Distributional Prediction via Latent Cluster Geometry Under Drift and Corruption

- **作者**: Navyansh Mahla, Prateek Chanda, Ganesh Ramakrishnan
- **发布日期**: 2026-06-17
- **链接**: [arXiv:2606.18778v1](https://arxiv.org/abs/2606.18778v1) | [PDF](https://arxiv.org/pdf/2606.18778v1)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

Online learning in non-stationary streams is often formulated as tracking a point estimate, but many applications require predicting the full data-generating distribution.

We study online distributional prediction under drift and adversarial corruption.

Our approach represents each candidate law through a latent cluster geometry: a variable-size configuration of centers that organizes probability mass and induces a predictive distribution.

A Gibbs quasi-posterior over these configurations yields an online predictor by posterior averaging, and the resulting variable-dimensional posterior can be

### AI 总结

总结生成失败

---

## 6. Splaxel: Efficient Distributed Training of 3D Gaussian Splatting for Large-scale Scene Reconstruction via Pixel-level Communication

- **作者**: Wenqi Jia, Zhewen Hu, Ying Huang, Yu Gong, Stavros Kalafatis
- **发布日期**: 2026-06-17
- **链接**: [arXiv:2606.18588v1](https://arxiv.org/abs/2606.18588v1) | [PDF](https://arxiv.org/pdf/2606.18588v1)
- **分类**: cs.DC, cs.CV
- **含金量**: 20/43 分

### 摘要

3D Gaussian Splatting (3DGS) enables high-fidelity and real-time 3D scene reconstruction, but scaling training to large-scale scenes requires optimizing hundreds of millions of Gaussians across multiple GPUs.

Existing distributed approaches either partition scenes into isolated regions, causing global inconsistency, or rely on global Gaussian-level exchanges, which lead to substantial growth in inter-GPU communication and quickly dominate iteration time.

We propose Splaxel, a communication-efficient distributed 3DGS training framework based on pixel-level local rendering and global compositi

### AI 总结

总结生成失败

---

## 7. ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving

- **作者**: Haipeng Yuan, Kaining Zheng, Yongshu Bai, Yuchen Zhang, Yunquan Zhang
- **发布日期**: 2026-06-17
- **链接**: [arXiv:2606.18741v1](https://arxiv.org/abs/2606.18741v1) | [PDF](https://arxiv.org/pdf/2606.18741v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Current large language model (LLM) inference systems universally deploy ultra-large-scale models using a combination of Tensor Parallelism (TP) and Pipeline Parallelism (PP).

However, existing systems treat the model parallelism topology as a static configuration that cannot be flexibly adjusted at runtime.

This rigid design creates a fundamental contradiction with the dynamically changing inference workloads in real-world scenarios.

State-of-the-art systems lack online reconfiguration capabilities and can only switch configurations by restarting the service, resulting in several minutes of se

### AI 总结

总结生成失败

---

## 8. Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases

- **作者**: Chandranil Chakraborttii, Jackeline García Alvarado, Sitora Abdulofizova, Shivanshu Dwivedi
- **发布日期**: 2026-06-16
- **链接**: [arXiv:2606.18497v1](https://arxiv.org/abs/2606.18497v1) | [PDF](https://arxiv.org/pdf/2606.18497v1)
- **分类**: cs.CR
- **含金量**: 20/43 分

### 摘要

Retrieval-augmented generation (RAG) allows large language models to access external and private corpora for factual, domain-specific responses.

Modern RAG pipelines use hierarchical navigable small world (HNSW) vector databases for efficient similarity search.

When a user requests data deletion, the systems typically only mark the record as deleted, leaving the embedding on disk physically unchanged.

This soft-delete operation raises compliance concerns under data-erasure and retention requirements such as GDPR Article 17 and HIPAA.

Analysis on three HNSW implementations confirms that deleted

### AI 总结

总结生成失败

---

## 9. A Critical Discourse Analysis of Gender Representation in Software Engineering Education Videos on YouTube

- **作者**: Isabella Graßl, Alexander Serebrenik, Giuseppe Destefanis
- **发布日期**: 2026-06-16
- **链接**: [arXiv:2606.18423v1](https://arxiv.org/abs/2606.18423v1) | [PDF](https://arxiv.org/pdf/2606.18423v1)
- **分类**: cs.SE
- **含金量**: 20/43 分

### 摘要

Educational resources may frame students' perceptions of who belongs in software engineering, which is relevant given the field's ongoing gender gap.

However, we know little about the hidden curriculum regarding gender in online learning spaces.

This study presents a critical discourse analysis of 200 manually analysed English and German software engineering tutorials on YouTube, examining gender representation through contextual domains and linguistic identity markers.

Our results show that male characters and masculine linguistic defaults dominate the tutorials.

We identified an agency gap, 

### AI 总结

总结生成失败

---

