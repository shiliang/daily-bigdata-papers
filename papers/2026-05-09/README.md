# 大数据+AI 领域论文日报

**日期**: 2026-05-09

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Verifier-Backed Hard Problem Genera...](https://arxiv.org/abs/2605.06660v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [ResiHP: Taming LLM Training Failure...](https://arxiv.org/abs/2605.06374v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [FalconGEMM: Surpassing Hardware Pea...](https://arxiv.org/abs/2605.06057v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Minimizing Modality Gap from the In...](https://arxiv.org/abs/2605.05927v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Revealing Modular Gradient Noise Im...](https://arxiv.org/abs/2605.05794v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Retina-RAG: Retrieval-Augmented Vis...](https://arxiv.org/abs/2605.06173v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Adding Thermal Awareness to Visual ...](https://arxiv.org/abs/2605.06010v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [AgriKD: Cross-Architecture Knowledg...](https://arxiv.org/abs/2605.01355v2) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Distributed Online Learning for Tim...](https://arxiv.org/abs/2605.06437v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [LearnMate^2: Design and Evaluation ...](https://arxiv.org/abs/2605.06257v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Verifier-Backed Hard Problem Generation for Mathematical Reasoning

- **作者**: Yuhang Lai, Jiazhan Feng, Yee Whye Teh, Ning Miao
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.06660v1](https://arxiv.org/abs/2605.06660v1) | [PDF](https://arxiv.org/pdf/2605.06660v1)
- **分类**: cs.LG, cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

Large Language Models (LLMs) demonstrate strong capabilities for solving scientific and mathematical problems, yet they struggle to produce valid, challenging, and novel problems - an essential component for advancing LLM training and enabling autonomous scientific research.

Existing problem generation approaches either depend on expensive human expert involvement or adopt naive self-play paradigms, which frequently yield invalid problems due to reward hacking.

This work introduces VHG, a verifier-enhanced hard problem generation framework built upon three-party self-play.

By integrating an in

### AI 总结

总结生成失败

---

## 2. ResiHP: Taming LLM Training Failures with Dynamic Hybrid

- **作者**: Tenghui Ma, Jihu Guo, Wei Gao, Sitian Lu, Zhisheng Ye
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.06374v1](https://arxiv.org/abs/2605.06374v1) | [PDF](https://arxiv.org/pdf/2605.06374v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Hybrid parallelism underpins large-scale LLM training across tens of thousands of GPUs.

At such scale, hardware failures on individual devices lead to performance skew across devices, diminishing overall training efficiency.

Existing resilient systems overlook sequence length variability in datasets and device performance skew under hybrid parallelism.

As a result, (1) iteration time fluctuations induced by sequence length variability can trigger spurious fail-slow detections, and (2) failures are mitigated through individual adaptations in hybrid parallelism, leading to unnecessary detection 

### AI 总结

总结生成失败

---

## 3. FalconGEMM: Surpassing Hardware Peaks with Lower-Complexity Matrix Multiplication

- **作者**: Honglin Zhu, Jiaping Cao, Jiang Shao, Siyuan Feng, Qian Qiu
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.06057v1](https://arxiv.org/abs/2605.06057v1) | [PDF](https://arxiv.org/pdf/2605.06057v1)
- **分类**: cs.DC, cs.MS
- **含金量**: 20/43 分

### 摘要

Peak breaking Matrix Multiplication is a promising technique to improve the performance of DL, especially in LLM training and inference.

We present FalconGEMM, a cross-platform framework that automates the deployment, optimization, and selection of Lower-Complexity Matrix Multiplication Algorithms (LCMAs) across diverse hardware.

There are three key innovations: (1) a Deployment Module that enables portable execution across various hardware and input configurations through code generation; (2) an Execution Module with Group-Parallel Optimizations that maximizes on-chip data reuse, utilizes par

### AI 总结

总结生成失败

---

## 4. Minimizing Modality Gap from the Input Side: Your Speech LLM Can Be a Prosody-Aware Text LLM

- **作者**: Wenqian Cui, Xiao-Hui Li, Daxin Tan, Qiyong Zheng, Irwin King
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.05927v1](https://arxiv.org/abs/2605.05927v1) | [PDF](https://arxiv.org/pdf/2605.05927v1)
- **分类**: cs.CL, cs.SD, eess.AS
- **含金量**: 20/43 分

### 摘要

Speech large language models (SLMs) are typically built from text large language model (TLM) checkpoints, yet they still suffer from a substantial modality gap.

Prior work has mainly attempted to reduce this gap from the output side by making speech generation more text-like, but the gap remains.

We argue that the key remaining bottleneck lies on the input side.

We propose TextPro-SLM, an SLM that makes spoken input more closely resemble that of a prosody-aware text LLM.

TextPro-SLM combines WhisperPro, a unified speech encoder that produces synchronized text tokens and prosody embeddings, wit

### AI 总结

总结生成失败

---

## 5. Revealing Modular Gradient Noise Imbalance in LLMs: Calibrating Adam via Signal-to-Noise Ratio

- **作者**: Ziqing Wen, Zhouyang Liu, Jiahuan Wang, Ping Luo, Li Shen
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.05794v1](https://arxiv.org/abs/2605.05794v1) | [PDF](https://arxiv.org/pdf/2605.05794v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

The impressive performance of large language models (LLMs) arises from their massive scale and heterogeneous module composition.

However, this structural heterogeneity introduces additional optimization challenges.

While adaptive optimizers such as Adam(W) provide per-parameter adaptivity, they do not explicitly account for module-level gradient heterogeneity, resulting in slower convergence, suboptimal performance, or training instability.

Existing approaches typically rely on manually tuned module-specific learning rates or specific optimization strategies, which are computationally costly a

### AI 总结

总结生成失败

---

## 6. Retina-RAG: Retrieval-Augmented Vision-Language Modeling for Joint Retinal Diagnosis and Clinical Report Generation

- **作者**: Abdelrahman Zaian, Sheethal Bhat, Mohamed Abdalkader, Andreas Maier
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.06173v1](https://arxiv.org/abs/2605.06173v1) | [PDF](https://arxiv.org/pdf/2605.06173v1)
- **分类**: cs.CV, cs.AI
- **含金量**: 20/43 分

### 摘要

Diabetic Retinopathy (DR) is a leading cause of preventable blindness among working-age adults worldwide, yet most automated screening systems are limited to image-level classification and lack clinically structured reporting.

We propose Retina-RAG, a low-cost modular framework that jointly performs DR severity grading, macular edema (ME) detection, and report generation.

The architecture decouples a high-performance retinal classifier and a parameter-efficient vision-language model (Qwen2.5-VL-7B-Instruct) adapted via Low-Rank Adaptation (LoRA), enabling flexible component integration.

A retr

### AI 总结

总结生成失败

---

## 7. Adding Thermal Awareness to Visual Systems in Real-Time via Distilled Diffusion Models

- **作者**: Yuchen Guo, Junli Gong, Wenjun Dong, Yiuming Cheung, Weifeng Su
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.06010v1](https://arxiv.org/abs/2605.06010v1) | [PDF](https://arxiv.org/pdf/2605.06010v1)
- **分类**: cs.CV, cs.AI
- **含金量**: 20/43 分

### 摘要

Purely RGB-based vision models often fail to provide reliable cues in challenging scenarios such as nighttime and fog, leading to degraded performance and safety risks.

Infrared imaging captures heat-emitting sources and provides critical complementary information, but existing high-fidelity fusion methods suffer from prohibitive latency, rendering them impractical for real-time edge deployment.

To address this, we propose FusionProxy, a real-time image fusion module designed as a fully independent, plug-and-play component with diffusion level quality.

FusionProxy exploits two complementary st

### AI 总结

总结生成失败

---

## 8. AgriKD: Cross-Architecture Knowledge Distillation for Efficient Leaf Disease Classification

- **作者**: Minh-Dung Le, Minh-Duc Hoang, Hoang-Vu Truong, Thi-Thu-Hong Phan
- **发布日期**: 2026-05-02
- **链接**: [arXiv:2605.01355v2](https://arxiv.org/abs/2605.01355v2) | [PDF](https://arxiv.org/pdf/2605.01355v2)
- **分类**: cs.CV, cs.AI
- **含金量**: 20/43 分

### 摘要

Automated leaf disease classification is critical for early disease detection in resource-constrained field environments.

Vision Transformers (ViTs) provide strong representation capability by modeling long-range dependencies and inter-class relationships; however, their high computational cost makes them impractical for deployment on edge devices.

As a result, existing approaches struggle to effectively transfer these rich representations to lightweight models.

This paper introduces AgriKD, a cross-architecture knowledge distillation framework for efficient edge deployment, which transfers kn

### AI 总结

总结生成失败

---

## 9. Distributed Online Learning for Time-Critical Communication in 6G Industrial Subnetworks

- **作者**: Samira Abdelrahman, Hossam Farag, Gilberto Berardinelli
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.06437v1](https://arxiv.org/abs/2605.06437v1) | [PDF](https://arxiv.org/pdf/2605.06437v1)
- **分类**: eess.SY
- **含金量**: 20/43 分

### 摘要

6G industrial in-X subnetworks are expected to support highly time-critical alarm reporting in large-scale environments characterized by mobility, bursty event-driven traffic, and limited radio resources.

In such settings, conventional medium access solutions are ill-suited to guarantee reliable delivery of critical traffic, e.g., emergency alarms, within strict deadlines, especially when multiple subnetworks become simultaneously active after a common alarm event, a scenario widely referred as medium access with a shared message.

This paper proposes a distributed deep reinforcement learning (

### AI 总结

总结生成失败

---

## 10. LearnMate^2: Design and Evaluation of an LLM-powered Personalized and Adaptive Support System for Online Learning

- **作者**: Xinyu Jessica Wang, Christine P. Lee, Bilge Mutlu
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.06257v1](https://arxiv.org/abs/2605.06257v1) | [PDF](https://arxiv.org/pdf/2605.06257v1)
- **分类**: cs.HC
- **含金量**: 20/43 分

### 摘要

Personalization is crucial for effective learning, yet online learning, designed for widespread availability and open access, lacks personalized guidance.

Recent advancements in large language models (LLMs) offer opportunities to bridge this gap.

We explore how LLM-driven tools may be designed to support personalized and adaptive learning and examine how they shape user experience and learning outcomes.

We iteratively designed \tool{} to support online learning by providing personalized study plans, real-time contextual assistance, and adaptive learning activities.

A preliminary study ($n=24$)

### AI 总结

总结生成失败

---

