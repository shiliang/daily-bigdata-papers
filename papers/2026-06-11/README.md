# 大数据+AI 领域论文日报

**日期**: 2026-06-11

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Which Models Are Our Models Built O...](https://arxiv.org/abs/2606.12385v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [DrivingAgent: Design and Scheduling...](https://arxiv.org/abs/2606.12236v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Lung-R1: A Knowledge Graph-Guided L...](https://arxiv.org/abs/2606.11675v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [What Limits Does Quantization Place...](https://arxiv.org/abs/2606.11780v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Performance Analysis of YOLOv11 and...](https://arxiv.org/abs/2606.12066v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Privacy-Preserving Federated Autoen...](https://arxiv.org/abs/2606.11556v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [MB-Loc: Multi-planar Bird's-eye-vie...](https://arxiv.org/abs/2606.08744v2) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Efficient and Robust Online Learnin...](https://arxiv.org/abs/2606.12246v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Hey Chat, Can You Teach Me? Structu...](https://arxiv.org/abs/2606.11744v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Capacity-Constrained Online Convex ...](https://arxiv.org/abs/2606.11711v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs

- **作者**: Sanjay Adhikesaven, Haoxiang Sun, Sewon Min
- **发布日期**: 2026-06-10
- **链接**: [arXiv:2606.12385v1](https://arxiv.org/abs/2606.12385v1) | [PDF](https://arxiv.org/pdf/2606.12385v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

Modern LLM training pipelines increasingly rely on other models to generate data, filter corpora, judge outputs, and guide development decisions.

These dependencies are recursive: a model may depend on an upstream artifact whose own dependencies are documented only in separate releases and artifacts.

As a result, the full dependency structure is fragmented across heterogeneous public artifacts, with complexity and recursive depth far outpacing humans' ability to trace.

We introduce ModSleuth, an agentic system that recursively reconstructs LLM dependency graphs from public artifacts with sourc

### AI 总结

总结生成失败

---

## 2. DrivingAgent: Design and Scheduling Agents for Autonomous Driving Systems

- **作者**: Zhongyu Xia, Wenhao Chen, Yongtao Wang, Ming-Hsuan Yang
- **发布日期**: 2026-06-10
- **链接**: [arXiv:2606.12236v1](https://arxiv.org/abs/2606.12236v1) | [PDF](https://arxiv.org/pdf/2606.12236v1)
- **分类**: cs.RO, cs.CV
- **含金量**: 20/43 分

### 摘要

Many autonomous driving systems are increasingly incorporating foundation models to improve generalization and handle long-tail scenarios.

However, this trend introduces two key challenges: (i) the manual and labor-intensive process of designing and integrating new models, and (ii) the lack of intelligent, dynamic scheduling mechanisms to meet strict real-time constraints.

While Large Language Model (LLM)-based agents offer a promising avenue for automation, existing frameworks are ill-suited for autonomous driving.

Specifically, they fail to distinguish between the fundamentally different req

### AI 总结

总结生成失败

---

## 3. Lung-R1: A Knowledge Graph-Guided LLM for Pulmonary Diagnostic Reasoning

- **作者**: Haoyang Zeng, Yuanxi Fu, Rongzhen Li, Yuming Yang, Xiao Sun
- **发布日期**: 2026-06-10
- **链接**: [arXiv:2606.11675v1](https://arxiv.org/abs/2606.11675v1) | [PDF](https://arxiv.org/pdf/2606.11675v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

Diagnosing pulmonary diseases requires integrating heterogeneous evidence amid phenotypic variability and cross-disease overlap.

Although large language models (LLMs) have shown progress on pulmonary knowledge question answering (QA) and information-processing tasks, reliable pulmonary diagnosis requires patient-specific, relation-aware reasoning over electronic medical record (EMR) evidence rather than isolated knowledge recall.

We define this gap between pulmonary knowledge and case-level diagnostic reasoning as the Pulmonary Knowledge-to-Diagnosis Gap.

To address it, we introduce LungKG, th

### AI 总结

总结生成失败

---

## 4. What Limits Does Quantization Place on Dense Top-$k$ Retrieval? A Theoretical Study

- **作者**: Koki Okajima, Tsukasa Yoshida
- **发布日期**: 2026-06-10
- **链接**: [arXiv:2606.11780v1](https://arxiv.org/abs/2606.11780v1) | [PDF](https://arxiv.org/pdf/2606.11780v1)
- **分类**: cs.IR, cs.AI, cs.IT
- **含金量**: 20/43 分

### 摘要

We establish conditions for embedding a corpus of $N$ documents as $d$-dimensional vectors such that every $k$-subset $S \subseteq [N]$ is realizable as a result of top-$k$ retrieval by some query vector.

Recent work shows that $d = O(k)$ suffices for such embeddings to exist in $\mathbb{R}^d$, independently of $N$.

We theoretically prove that this corpus-independent bound is specific to infinite precision.

With $B$ bits per coordinate, perfect top-$k$ retrieval requires $Bd = Ω(k \ln N)$; thus, at any fixed precision, the dimension must grow at least logarithmically with $N$.

Specializing to 

### AI 总结

总结生成失败

---

## 5. Performance Analysis of YOLOv11 and YOLOv8 for Mixed Traffic Object Detection under Adverse Weather Conditions in Developing Countries

- **作者**: Quoc Thuan Nguyen, Ha Anh Vu, Ngo Dang Thanh Ngan, Minh Phuc Hoang Ngoc
- **发布日期**: 2026-06-10
- **链接**: [arXiv:2606.12066v1](https://arxiv.org/abs/2606.12066v1) | [PDF](https://arxiv.org/pdf/2606.12066v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

In modern vehicular systems, robust performance under harsh conditions has become a critical problem of autonomous driving.

Our study delivers a comprehensive evaluation of the newest iteration of the YOLO series, which is YOLOv11 Nano architecture benchmarked against the widely adopted YOLOv8 Nano as a baseline on a custom fused dataset that combines the Indian Driving Dataset (IDD) [1] and Berkeley Deep Drive Dataset (BDD100K) [2].

We have analyzed the trade-offs among detection accuracy, inference speed, and computational efficiency in high-entropy scenarios involving dense mixed traffic, r

### AI 总结

总结生成失败

---

## 6. Privacy-Preserving Federated Autoencoder for ECG Anomaly Detection on Edge Devices

- **作者**: Kaan Arda Akyol, Jakub Kacper Szeląg, Aydin Abadi, Maha Alghamdi, Ghadah Albalawi
- **发布日期**: 2026-06-10
- **链接**: [arXiv:2606.11556v1](https://arxiv.org/abs/2606.11556v1) | [PDF](https://arxiv.org/pdf/2606.11556v1)
- **分类**: cs.CR, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

Continuous electrocardiography (ECG) monitoring could surface rhythm abnormalities before they escalate into cardiovascular events.

However, a deployable system must satisfy three requirements simultaneously: legal-grade privacy (GDPR, HIPAA), real-time inference on constrained edge hardware, and detection quality under non-IID cross-hospital data.

We design and evaluate an end-to-end federated system addressing all three for unsupervised 12-lead ECG anomaly detection on PTB-XL dataset, combining three autoencoder families (VanillaAE, ConvAE, VAE), Flower-based federated averaging (FedAvg) a

### AI 总结

总结生成失败

---

## 7. MB-Loc: Multi-planar Bird's-eye-view Localization in outdoor LiDAR scenes

- **作者**: Ayaan Choudhury, Preet Savalia, Anirudh Pydah, Avinash Sharma
- **发布日期**: 2026-06-07
- **链接**: [arXiv:2606.08744v2](https://arxiv.org/abs/2606.08744v2) | [PDF](https://arxiv.org/pdf/2606.08744v2)
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

## 8. Efficient and Robust Online Learning to Rank in Decentralized Systems

- **作者**: Marcel Gregoriadis, Martijn de Vos, Sayan Biswas, Anne-Marie Kermarrec, Johan Pouwelse
- **发布日期**: 2026-06-10
- **链接**: [arXiv:2606.12246v1](https://arxiv.org/abs/2606.12246v1) | [PDF](https://arxiv.org/pdf/2606.12246v1)
- **分类**: cs.DC, cs.IR
- **含金量**: 20/43 分

### 摘要

In Online Learning to Rank (OLTR), ranking models are trained directly from live user interactions, but existing systems rely on a trusted central server to collect and process these interactions.

This leaves operators free to introduce biases that conflict with user interests.

Decentralized learning offers an attractive alternative, allowing users to collaboratively train a shared ranking model by exchanging model updates directly with one another, without any central authority.

In such settings, however, malicious nodes can send poisoned model updates that degrade the ranking quality of hone

### AI 总结

总结生成失败

---

## 9. Hey Chat, Can You Teach Me? Structuring Socratic Dialogue for Human Learning in the Wild

- **作者**: Sidney Tio, Arunesh Sinha, Pradeep Varakantham
- **发布日期**: 2026-06-10
- **链接**: [arXiv:2606.11744v1](https://arxiv.org/abs/2606.11744v1) | [PDF](https://arxiv.org/pdf/2606.11744v1)
- **分类**: cs.CL, cs.AI
- **含金量**: 20/43 分

### 摘要

Large language models are now widely used for everyday learning, but the underlying interactions are typically unstructured chats rather than following a curriculum.

Unlike formal online learning systems, these interactions carry no prior record of the student, so any estimate of what the student already knows must be inferred from the dialogue itself.

We show that this gap is not closed by scaling models alone.

Frontier and education-tuned LLMs perform poorly when asked to tutor a student over an extended session, because doing so requires three things at once.

The tutor must sequence a curri

### AI 总结

总结生成失败

---

## 10. Capacity-Constrained Online Convex Optimization with Delayed Feedback

- **作者**: Alexander Ryabchenko, Idan Attias, Daniel M. Roy
- **发布日期**: 2026-06-10
- **链接**: [arXiv:2606.11711v1](https://arxiv.org/abs/2606.11711v1) | [PDF](https://arxiv.org/pdf/2606.11711v1)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

Online learning with delayed feedback typically assumes that the learner can track all pending rounds until their feedback arrives.

In practice, tracking resources are finite, and feedback from untracked rounds is permanently lost.

In this paper, we study delayed online convex optimization (OCO) under a hard capacity constraint, where at most $C$ pending rounds can be tracked at any time.

To model delay information, we introduce a semi-clairvoyant model that refines the clairvoyant assumption from prior work: rather than requiring delays to be known at prediction time, the learner observes del

### AI 总结

总结生成失败

---

