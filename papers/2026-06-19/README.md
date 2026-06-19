# 大数据+AI 领域论文日报

**日期**: 2026-06-19

**论文数量**: 9 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [ARGUS: Production-Scale Tracing and...](https://arxiv.org/abs/2606.20374v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [StreamKL: Fast and Memory-Efficient...](https://arxiv.org/abs/2606.20005v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Online Dynamic Batching with Formal...](https://arxiv.org/abs/2606.19989v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [IHUBERT: Vector-Based Semantic Dedu...](https://arxiv.org/abs/2606.20089v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Query-aware Routing for Filtered Ap...](https://arxiv.org/abs/2606.19898v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Policy-aware Vector Search: A Visio...](https://arxiv.org/abs/2606.19803v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Library-Aware Doubles and Iterative...](https://arxiv.org/abs/2606.19725v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Finetuning Vision-Language-Action M...](https://arxiv.org/abs/2606.20246v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Quantum ring all-reduce: communicat...](https://arxiv.org/abs/2606.20344v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. ARGUS: Production-Scale Tracing and Performance Diagnosis for over 10,000-GPU Clusters

- **作者**: Jiasheng Zhou, Longbin Zeng, Clavis Chen, Ruiming Lu, Qinwei Yang
- **发布日期**: 2026-06-18
- **链接**: [arXiv:2606.20374v1](https://arxiv.org/abs/2606.20374v1) | [PDF](https://arxiv.org/pdf/2606.20374v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Large-scale LLM training requires always-on, fine-grained observability for effective performance diagnosis at scale.

Coarse resource monitors alone cannot localize root causes, and fine-grained profilers incur prohibitive (5%-30%) overheads and massive trace volumes, making always-on deployment impractical in large production clusters.

We propose ARGUS, a low-overhead, fine-grained, always-on tracing and real-time analysis system for training workloads in 10,000+ GPU-scale production clusters.

ARGUS decomposes observation along the training call hierarchy into CPU call stacks, framework sem

### AI 总结

总结生成失败

---

## 2. StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation

- **作者**: Guangda Liu, Yiquan Wang, Chengwei Li, Wenhao Chen, Jing Lin
- **发布日期**: 2026-06-18
- **链接**: [arXiv:2606.20005v1](https://arxiv.org/abs/2606.20005v1) | [PDF](https://arxiv.org/pdf/2606.20005v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

Attention distillation, which trains one attention distribution to match another by minimizing their Kullback-Leibler (KL) divergence, is widely used in knowledge distillation, model compression, continual learning, and sparse-attention LLM training.

However, existing approaches materialize both attention distributions before computing the KL reduction, incurring $O(N_QN_K)$ memory and IO costs that become prohibitive at long context lengths.

We present StreamKL, the first fused GPU primitive for attention KL divergence that eliminates this quadratic materialization.

StreamKL derives a novel o

### AI 总结

总结生成失败

---

## 3. Online Dynamic Batching with Formal Guarantees for LLM Training

- **作者**: Dian Li, Zekun Wang, Yaoru Wang, Jiahong Yan
- **发布日期**: 2026-06-18
- **链接**: [arXiv:2606.19989v1](https://arxiv.org/abs/2606.19989v1) | [PDF](https://arxiv.org/pdf/2606.19989v1)
- **分类**: cs.DC, cs.LG
- **含金量**: 20/43 分

### 摘要

Modern LLM training breaks a core assumption behind offline batch samplers: the true training cost of a sample is only observable after preprocessing, augmentation, templating, tokenization, and multimodal visual-token expansion.

Unless one pays for a preprocessing- and augmentation-dependent length cache, batch construction is therefore blind to the quantity that determines padding, memory use, and GPU saturation.

We introduce Online Dynamic Batching (ODB), a DataLoader-side drop-in system that moves batch formation to this point of accurate observability while preserving DDP step alignment.



### AI 总结

总结生成失败

---

## 4. IHUBERT: Vector-Based Semantic Deduplication and Domain-Balanced Pretraining for Persian Resources

- **作者**: Arash Ghafouri, Mahdi Firouzmandi, Hossein Saberi, Mohammad Reza Hasani Ahangar
- **发布日期**: 2026-06-18
- **链接**: [arXiv:2606.20089v1](https://arxiv.org/abs/2606.20089v1) | [PDF](https://arxiv.org/pdf/2606.20089v1)
- **分类**: cs.CL, cs.AI
- **含金量**: 20/43 分

### 摘要

Persian pretrained language models (PLMs) are still limited by the scarcity of large-scale, high-quality pretraining corpora and by insufficient evaluation beyond standard classification and NER tasks.

We present IHUBERT, a monolingual Persian PLM trained from scratch with the RoBERTa-base encoder (125M parameters) on a 45 GB curated subset of the Sepahr-Danesh collection (about 7-8B tokens).

To improve corpus quality and reduce redundancy, we employ a multi-stage preprocessing pipeline that includes normalization, exact and near-duplicate removal, anonymization, and vector-database-based sema

### AI 总结

总结生成失败

---

## 5. Query-aware Routing for Filtered Approximate Nearest Neighbors Search

- **作者**: Qianqian Xiong, Mengxuan Zhang
- **发布日期**: 2026-06-18
- **链接**: [arXiv:2606.19898v1](https://arxiv.org/abs/2606.19898v1) | [PDF](https://arxiv.org/pdf/2606.19898v1)
- **分类**: cs.DB, cs.IR
- **含金量**: 20/43 分

### 摘要

Filtered ANN search, which combines vector similarity with attribute predicates, is a core primitive in modern vector databases and retrieval-augmented generation.

We benchmark all major categorical filtered ANN methods across multiple datasets under three predicates and find that no single method dominates.

Moreover, even within a single dataset and predicate type, the best method for a query can vary.

Therefore, we propose a query-aware routing framework.

A lightweight ML model predicts each candidate method's recall on the query, and the router consults an offline benchmark table that maps 

### AI 总结

总结生成失败

---

## 6. Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases

- **作者**: Lakshmi Sahithi Yalamarthi, Primal Pappachan
- **发布日期**: 2026-06-18
- **链接**: [arXiv:2606.19803v1](https://arxiv.org/abs/2606.19803v1) | [PDF](https://arxiv.org/pdf/2606.19803v1)
- **分类**: cs.DB, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

Vector databases are increasingly used in security sensitive contexts with Retrieval Augmented Generation and organizational AI pipelines; however, their security capabilities remain limited.

Specifically, Fine-grained Access Control (FGAC) which is required to ensure that data access adheres to user-specific policies is not fully supported in modern vector databases.

Unlike relational databases, vector databases combine structured and unstructured attributes to provide semantic, approximate query results, which complicates FGAC implementation.

This creates an inherent tension between enforcin

### AI 总结

总结生成失败

---

## 7. Library-Aware Doubles and Iterative Repair for Large Language Model-Generated Unit Tests in OpenSIL Firmware

- **作者**: Ma Toan Bach, Yuchi Zheng, Haingo Razafindranto, Tanvir Alam, Aric Leather
- **发布日期**: 2026-06-18
- **链接**: [arXiv:2606.19725v1](https://arxiv.org/abs/2606.19725v1) | [PDF](https://arxiv.org/pdf/2606.19725v1)
- **分类**: cs.SE, cs.AI, cs.MA
- **含金量**: 20/43 分

### 摘要

Validating changes in low-level C firmware is expensive because unit tests (UTs) are fragile under strict build constraints, where missing headers, unresolved symbols, and dependency mismatches frequently prevent compilation and linking.

This study introduces an automated UT authoring workflow for the Open-Source Silicon Initialization Library (openSIL) firmware codebase maintained by Advanced Micro Devices (AMD) that reduces manual effort through a large language model (LLM) guided multi-agent pipeline.

The workflow combines automated generation of test scaffolds, library-aware creation or re

### AI 总结

总结生成失败

---

## 8. Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think

- **作者**: Gia-Binh Nguyen, Trong-Bao Ho, Thien-Loc Ha, Khoa Vo, Philip Lund Møller
- **发布日期**: 2026-06-18
- **链接**: [arXiv:2606.20246v1](https://arxiv.org/abs/2606.20246v1) | [PDF](https://arxiv.org/pdf/2606.20246v1)
- **分类**: cs.RO, cs.AI
- **含金量**: 20/43 分

### 摘要

Vision-Language-Action (VLA) models pre-trained on massive video-robot datasets have revolutionized robotic manipulation, yet their multi-billion parameter architectures impose prohibitive computational burdens during downstream fine-tuning and real-time inference.

In this work, we reveal a highly non-trivial architectural characteristic of these continuous control foundation policies (e.g., pi_0, GR00T-N1.5): despite being trained on diverse physical trajectories, they exhibit severe layer-wise representational redundancy.

To exploit this, we introduce a structural compression pipeline that i

### AI 总结

总结生成失败

---

## 9. Quantum ring all-reduce: communication and privacy advantages for distributed learning

- **作者**: María Gragera Garcés, Lirandë Pira
- **发布日期**: 2026-06-18
- **链接**: [arXiv:2606.20344v1](https://arxiv.org/abs/2606.20344v1) | [PDF](https://arxiv.org/pdf/2606.20344v1)
- **分类**: quant-ph, cs.DC, cs.LG
- **含金量**: 20/43 分

### 摘要

Machine learning models have scaled to unprecedented sizes, making training across distributed devices the de facto standard in the field.

In this work, we explore how quantum communications can make distributed training both more communication-efficient and information-theoretically private, for both classical and quantum learning models.

Ring all-reduce is the foundational communication primitive for large-scale distributed training.

We present a quantum version that reduces per-link online communication by a provably optimal factor of two using pre-shared entanglement and superdense coding,

### AI 总结

总结生成失败

---

