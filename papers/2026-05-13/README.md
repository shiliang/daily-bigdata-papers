# 大数据+AI 领域论文日报

**日期**: 2026-05-13

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Pion: A Spectrum-Preserving Optimiz...](https://arxiv.org/abs/2605.12492v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Avoiding Cross-Datacenter Collectiv...](https://arxiv.org/abs/2605.11852v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [FalconGEMM: Surpassing Hardware Pea...](https://arxiv.org/abs/2605.06057v2) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Attacks and Mitigations for Distrib...](https://arxiv.org/abs/2605.12364v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Can a Single Message Paralyze the A...](https://arxiv.org/abs/2605.11442v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [A categorical error sensitivity ind...](https://arxiv.org/abs/2605.12328v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [NAVIS: Concurrent Search and Update...](https://arxiv.org/abs/2605.11523v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [VLADriver-RAG: Retrieval-Augmented ...](https://arxiv.org/abs/2605.08133v2) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Ada-MK: Adaptive MegaKernel Optimiz...](https://arxiv.org/abs/2605.11581v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [VIMCAN: Visual-Inertial 3D Human Po...](https://arxiv.org/abs/2605.07552v2) | 待分析 | 评估失败 | [Code](https://github.com/Eddieyzp/VIMCAN) | 20/43 |

---


## 1. Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation

- **作者**: Kexuan Shi, Hanxuan Li, Zeju Qiu, Yandong Wen, Simon Buchholz
- **发布日期**: 2026-05-12
- **链接**: [arXiv:2605.12492v1](https://arxiv.org/abs/2605.12492v1) | [PDF](https://arxiv.org/pdf/2605.12492v1)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

We introduce Pion, a spectrum-preserving optimizer for large language model (LLM) training based on orthogonal equivalence transformation.

Unlike additive optimizers such as Adam and Muon, Pion updates each weight matrix through left and right orthogonal transformations, preserving its singular values throughout training.

This yields an optimization mechanism that modulates the geometry of weight matrices while keeping their spectral norm fixed.

We derive the Pion update rule, systematically examine its design choices, and analyze its convergence behavior along with several key properties.

Emp

### AI 总结

总结生成失败

---

## 2. Avoiding Cross-Datacenter Collective Congestion via Disaggregated Buffering

- **作者**: Mariano Scazzariello, Noga H. Rotman, Dima Gavrilenko, Sajy Khashab, Alexander Shpiner
- **发布日期**: 2026-05-12
- **链接**: [arXiv:2605.11852v1](https://arxiv.org/abs/2605.11852v1) | [PDF](https://arxiv.org/pdf/2605.11852v1)
- **分类**: cs.NI
- **含金量**: 20/43 分

### 摘要

LLM training at the scale of tens of thousands of GPUs now spans multiple datacenters (DC), making cross-DC collectives over long-haul links unavoidable.

A critical and overlooked bottleneck arises when these collectives collide with intra-DC traffic at the destination - a common pattern in real workloads.

The multi-millisecond congestion control loop is too slow to react, triggering severe packet loss and congestion collapse.

We present Spillway, a transparent in-network mechanism that buffers dropped packets in switch-disaggregated buffers in a destination data center and drains them once 

### AI 总结

总结生成失败

---

## 3. FalconGEMM: Surpassing Hardware Peaks with Lower-Complexity Matrix Multiplication

- **作者**: Honglin Zhu, Jiaping Cao, Jiang Shao, Siyuan Feng, Qian Qiu
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.06057v2](https://arxiv.org/abs/2605.06057v2) | [PDF](https://arxiv.org/pdf/2605.06057v2)
- **分类**: cs.DC, cs.MS
- **含金量**: 20/43 分

### 摘要

Peak breaking Matrix Multiplication is a promising technique to improve the performance of DL, especially in LLM training and inference.

We present FalconGEMM, a cross-platform framework that automates the deployment, optimization, and selection of Lower-Complexity Matrix Multiplication Algorithms (LCMAs) across diverse hardware.

There are three key innovations: (1) a Deployment Module that enables portable execution across various hardware and input configurations through code generation; (2) an Execution Module with Group-Parallel Optimizations that maximizes on-chip data reuse, utilizes par

### AI 总结

总结生成失败

---

## 4. Attacks and Mitigations for Distributed Governance of Agentic AI under Byzantine Adversaries

- **作者**: Matthew D. Laws, Alina Oprea, Cristina Nita-Rotaru
- **发布日期**: 2026-05-12
- **链接**: [arXiv:2605.12364v1](https://arxiv.org/abs/2605.12364v1) | [PDF](https://arxiv.org/pdf/2605.12364v1)
- **分类**: cs.CR, cs.LG, cs.MA
- **含金量**: 20/43 分

### 摘要

Agentic AI governance is a critical component of agentic AI infrastructure ensuring that agents follow their owner's communication and interaction policies, and providing protection against attacks from malicious agents.

The state-of-the-art solution, SAGA, assumes a logically centralized point of trust, the Provider, which serves as a repository for user and agent information and actively enforces policies.

While SAGA provides protection against malicious agents, it remains vulnerable to a malicious Provider that deviates from the protocol, undermining the security of the identity and access 

### AI 总结

总结生成失败

---

## 5. Can a Single Message Paralyze the AI Infrastructure? The Rise of AbO-DDoS Attacks through Targeted Mobius Injection

- **作者**: Zi Liang, Ronghua Li, Yanyun Wang, Qingqing Ye, Haibo Hu
- **发布日期**: 2026-05-12
- **链接**: [arXiv:2605.11442v1](https://arxiv.org/abs/2605.11442v1) | [PDF](https://arxiv.org/pdf/2605.11442v1)
- **分类**: cs.CR, cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

Large Language Model (LLM) agents have emerged as key intermediaries, orchestrating complex interactions between human users and a wide range of digital services and LLM infrastructures.

While prior research has extensively examined the security of LLMs and agents in isolation, the systemic risk of the agent acting as a disruptive hub within the user-agent-service chain remains largely overlooked.

In this work, we expose a novel threat paradigm by introducing Mobius Injection, a sophisticated attack that weaponizes autonomous agents into zombie nodes to launch what we define as gent-based and 

### AI 总结

总结生成失败

---

## 6. A categorical error sensitivity index (ISEC): A preventive ordinal decision-support measure for irrecoverable errors in manual data entry systems

- **作者**: Ricardo Raúl Palma, Mauro Anibal Benetti, Fabricio Orlando Sanchez Varretti
- **发布日期**: 2026-05-12
- **链接**: [arXiv:2605.12328v1](https://arxiv.org/abs/2605.12328v1) | [PDF](https://arxiv.org/pdf/2605.12328v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

Data entry systems remain structurally vulnerable to categorical misclassifications, particularly in small and medium sized enterprises (SMEs).

When nominal categories exhibit semantic or morphological proximity, human machine interaction may produce errors that are irrecoverable ex post.

In the absence of automated input controls, manual data entry frequently generates irrecoverable categorical distortions that propagate into Key Performance Indicators (KPIs), thereby misleading managerial decision making.

State of the art normalization tools typically evaluate semantic and morphological dime

### AI 总结

总结生成失败

---

## 7. NAVIS: Concurrent Search and Update with Low Position-Seeking Overhead in On-SSD Graph-Based Vector Search

- **作者**: Jaeyong Song, Hongsun Jang, Changmin Shin, Seongyeon Park, Yong Jae Ryoo
- **发布日期**: 2026-05-12
- **链接**: [arXiv:2605.11523v1](https://arxiv.org/abs/2605.11523v1) | [PDF](https://arxiv.org/pdf/2605.11523v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

On-disk graph-based vector search (GVS) has become the dominant approach for serving large-scale vector databases at high recall, but prior systems struggle to sustain concurrent search and update throughput on high-dimensional workloads.

We find the main cause of this in position seeking, a full graph traversal that every update performs to locate neighbors before linking the new vector into the graph.

Position seeking is fundamentally heavier than a search query, and its cost is further amplified by two systemic limitations of current GVS systems, packed layouts that couple every edge fetch 

### AI 总结

总结生成失败

---

## 8. VLADriver-RAG: Retrieval-Augmented Vision-Language-Action Models for Autonomous Driving

- **作者**: Rui Zhao, Haofeng Hu, Zhenhai Gao, Jiaqiao Liu, Gao Fei
- **发布日期**: 2026-05-01
- **链接**: [arXiv:2605.08133v2](https://arxiv.org/abs/2605.08133v2) | [PDF](https://arxiv.org/pdf/2605.08133v2)
- **分类**: cs.CV, cs.AI
- **含金量**: 20/43 分

### 摘要

Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving, yet their reliance on implicit parametric knowledge limits generalization in long-tail scenarios.

While Retrieval-Augmented Generation (RAG) offers a solution by accessing external expert priors, standard visual retrieval suffers from high latency and semantic ambiguity.

To address these challenges, we propose \textbf{VLADriver-RAG}, a framework that grounds planning in explicit, structure-aware historical knowledge.

Specifically, we abstract sensory inputs into spatiotemporal semantic g

### AI 总结

总结生成失败

---

## 9. Ada-MK: Adaptive MegaKernel Optimization via Automated DAG-based Search for LLM Inference

- **作者**: Wenxin Dong, Mingqing Hu, Guanghui Yu, Qiang Fu, Peng Xu
- **发布日期**: 2026-05-12
- **链接**: [arXiv:2605.11581v1](https://arxiv.org/abs/2605.11581v1) | [PDF](https://arxiv.org/pdf/2605.11581v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

When large language models (LLMs) serve real-time inference in commercial online advertising systems, end-to-end latency must be strictly bounded to the millisecond range.

Yet every token generated during the decode phase triggers thousands of kernel launches, and kernel launch overhead alone can account for 14.6% of end-to-end inference time.

MegaKernel eliminates launch overhead and inter-operator HBM round-trips by fusing multiple operators into a single persistent kernel.

However, existing MegaKernel implementations face a fundamental tension between portability and efficiency on resource-

### AI 总结

总结生成失败

---

## 10. VIMCAN: Visual-Inertial 3D Human Pose Estimation with Hybrid Mamba-Cross-Attention Network

- **作者**: Zepeng Yang, Junxuan Bai, Hao Li, Ju Dai, Junjun Pan
- **发布日期**: 2026-05-08
- **链接**: [arXiv:2605.07552v2](https://arxiv.org/abs/2605.07552v2) | [PDF](https://arxiv.org/pdf/2605.07552v2)
- **分类**: cs.CV
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/Eddieyzp/VIMCAN) ⭐ 0

### 摘要

The rapid advances in deep learning have significantly enhanced the accuracy of multimodal 3D human pose estimation (HPE).

However, the state-of-the-art (SOTA) HPE pipelines still rely on Transformers, whose quadratic complexity makes real-time processing for long sequences impractical.

Mamba addresses this issue through selective state-space modeling, enabling efficient sequence processing without sacrificing representational power.

Nevertheless, it struggles to capture complex spatial dependencies in multimodal settings.

To bridge this gap, we propose VIMCAN, a hybrid architecture that combi

### AI 总结

总结生成失败

---

