# 大数据+AI 领域论文日报

**日期**: 2026-05-11

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [HexiSeq: Accommodating Long Context...](https://arxiv.org/abs/2605.07569v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Boosting Automatic Java-to-Cangjie ...](https://arxiv.org/abs/2605.07403v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Minimizing Modality Gap from the In...](https://arxiv.org/abs/2605.05927v2) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Retina-RAG: Retrieval-Augmented Vis...](https://arxiv.org/abs/2605.06173v2) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [VIMCAN: Visual-Inertial 3D Human Po...](https://arxiv.org/abs/2605.07552v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [AsymTalker: Identity-Consistent Lon...](https://arxiv.org/abs/2605.02948v2) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Self-Play Enhancement via Advantage...](https://arxiv.org/abs/2605.07977v1) | 待分析 | 评估失败 | [Code](https://github.com/lee3296/SPEAR.) | 20/43 |
| 8 | [Characterizing and Correcting Effec...](https://arxiv.org/abs/2605.07886v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Regret-Oracle Complexity Tradeoffs ...](https://arxiv.org/abs/2605.07155v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Online Localized Conformal Predicti...](https://arxiv.org/abs/2605.05497v2) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. HexiSeq: Accommodating Long Context Training of LLMs over Heterogeneous Hardware

- **作者**: Yan Liang, Youhe Jiang, Ran Yan, Binhang Yuan, Wei Wang
- **发布日期**: 2026-05-08
- **链接**: [arXiv:2605.07569v1](https://arxiv.org/abs/2605.07569v1) | [PDF](https://arxiv.org/pdf/2605.07569v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Long-context training of large language models (LLMs) is commonly distributed with Context Parallelism (CP) and Head Parallelism (HP), but existing training systems largely assume homogeneous GPU meshes.

This paper extends CP and HP to heterogeneous GPU clusters with mixed GPU models and non-uniform network bandwidths, a common setting in production training.

We introduce HexiSeq, a system that supports fully asymmetric CP--HP partitioning by assigning sequence shards and attention heads according to device compute, memory, and communication capabilities.

We formalize heterogeneous CP--HP allo

### AI 总结

总结生成失败

---

## 2. Boosting Automatic Java-to-Cangjie Translation with Multi-Stage LLM Training and Error Repair

- **作者**: Xinyue Liang, Jingxuan Zhang, Lin Li, Jun Zhang, Junhao Chen
- **发布日期**: 2026-05-08
- **链接**: [arXiv:2605.07403v1](https://arxiv.org/abs/2605.07403v1) | [PDF](https://arxiv.org/pdf/2605.07403v1)
- **分类**: cs.SE
- **含金量**: 20/43 分

### 摘要

With the rapid evolution of emerging programming language ecosystems, the demand for code translation to low-resource languages continues to grow.

As Cangjie emerges as a new programming language, its ecosystem and development toolchains are rapidly expanding.

Automated translation from popular programming languages to Cangjie is therefore valuable for practical development.

However, constrained by both insufficient Cangjie knowledge and scarce parallel code corpora, general Large Language Models (LLMs) are prone to syntactic errors and semantic as well as structural misalignment in code trans

### AI 总结

总结生成失败

---

## 3. Minimizing Modality Gap from the Input Side: Your Speech LLM Can Be a Prosody-Aware Text LLM

- **作者**: Wenqian Cui, Xiao-Hui Li, Daxin Tan, Qiyong Zheng, Irwin King
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.05927v2](https://arxiv.org/abs/2605.05927v2) | [PDF](https://arxiv.org/pdf/2605.05927v2)
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

## 4. Retina-RAG: Retrieval-Augmented Vision-Language Modeling for Joint Retinal Diagnosis and Clinical Report Generation

- **作者**: Abdelrahman Zaian, Sheethal Bhat, Mohamed Abdalkader, Andreas Maier
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.06173v2](https://arxiv.org/abs/2605.06173v2) | [PDF](https://arxiv.org/pdf/2605.06173v2)
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

## 5. VIMCAN: Visual-Inertial 3D Human Pose Estimation with Hybrid Mamba-Cross-Attention Network

- **作者**: Zepeng Yang, Junxuan Bai, Hao Li, Ju Dai, Junjun Pan
- **发布日期**: 2026-05-08
- **链接**: [arXiv:2605.07552v1](https://arxiv.org/abs/2605.07552v1) | [PDF](https://arxiv.org/pdf/2605.07552v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

The rapid advances in deep learning have significantly enhanced the accuracy of multimodal 3D human pose estimation (HPE).

However, the state-of-the-art (SOTA) HPE pipelines still rely on Transformers, whose quadratic complexity makes real-time processing for long sequences impractical.

Mamba addresses this issue through selective state-space modeling, enabling efficient sequence processing without sacrificing representational power.

Nevertheless, it struggles to capture complex spatial dependencies in multimodal settings.

To bridge this gap, we propose VIMCAN, a hybrid architecture that combi

### AI 总结

总结生成失败

---

## 6. AsymTalker: Identity-Consistent Long-Term Talking Head Generation via Asymmetric Distillation

- **作者**: Yuxin Lu, Qian Qiao, Jiayang Sun, Guibo Zhu, Min Cao
- **发布日期**: 2026-05-01
- **链接**: [arXiv:2605.02948v2](https://arxiv.org/abs/2605.02948v2) | [PDF](https://arxiv.org/pdf/2605.02948v2)
- **分类**: cs.LG, cs.AI, cs.SD
- **含金量**: 20/43 分

### 摘要

Diffusion-based talking head generation has achieved remarkable visual quality, yet scaling it to long-term videos remains challenging.

The widely adopted chunk-wise paradigm introduces two fundamental failures: (1) temporal-spatial misalignment between static identity references and dynamic audio streams, and (2) cascading identity drift propagated through self-generated continuity references across chunks.

To address both issues, we propose AsymTalker, a novel diffusion-based talking head generation method comprising Temporal Reference Encoding (TRE) and Asymmetric Knowledge Distillation (AK

### AI 总结

总结生成失败

---

## 7. Self-Play Enhancement via Advantage-Weighted Refinement in Online Federated LLM Fine-Tuning with Real-Time Feedback

- **作者**: Seohyun Lee, Wenzhi Fang, Dong-Jun Han, Seyyedali Hosseinalipour, Christopher G. Brinton
- **发布日期**: 2026-05-08
- **链接**: [arXiv:2605.07977v1](https://arxiv.org/abs/2605.07977v1) | [PDF](https://arxiv.org/pdf/2605.07977v1)
- **分类**: cs.LG
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/lee3296/SPEAR.) ⭐ 0

### 摘要

Recent works have advanced feedback-based learning systems, whereby a foundation model is able to intake incoming feedback (e.g., a user) to self-improve, creating a self-loop system of training.

However, existing works are limited in needing to consider an offline setup to allow for such feedback-based methods, and are further limited in the need of requiring privileged ground-truth contexts for training.

Moreover, there is limited consideration of federated learning (FL), which is particularly well-suited for incorporating external feedback across large networks of end users, for example, bu

### AI 总结

总结生成失败

---

## 8. Characterizing and Correcting Effective Target Shift in Online Learning

- **作者**: Ziyan Li, Naoki Hiratani
- **发布日期**: 2026-05-08
- **链接**: [arXiv:2605.07886v1](https://arxiv.org/abs/2605.07886v1) | [PDF](https://arxiv.org/pdf/2605.07886v1)
- **分类**: stat.ML, cs.LG
- **含金量**: 20/43 分

### 摘要

Online learning from a stream of data is a defining feature of intelligence, yet modern machine learning systems often struggle in this setting, especially under distributional shift.

To understand its basic properties, we study the relationship between online and offline learning in the context of kernel regression.

We derive a closed-form expression for the function learned by online kernel regression, revealing that online kernel regression is equivalent to offline regression with shifted, inaccurate target outputs.

Conversely, we show that by compensating for this effective shift in the te

### AI 总结

总结生成失败

---

## 9. Regret-Oracle Complexity Tradeoffs in Agnostic Online Learning

- **作者**: Idan Attias, Steve Hanneke, Arvind Ramaswami
- **发布日期**: 2026-05-08
- **链接**: [arXiv:2605.07155v1](https://arxiv.org/abs/2605.07155v1) | [PDF](https://arxiv.org/pdf/2605.07155v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Agnostic online learning is classically solved via a reduction to the realizable setting, utilizing Littlestone's Standard Optimal Algorithm (SOA) as a base learner.

However, the SOA is computationally intractable to execute even for a single round.

To overcome this barrier, recent work in oracle-efficient online learning replaces the SOA with a realizable base learner that accesses the concept class exclusively through an offline empirical risk minimization (ERM) oracle.

While such agnostic learners achieve near-optimal expected regret, they suffer from a doubly-exponential oracle complexity 

### AI 总结

总结生成失败

---

## 10. Online Localized Conformal Prediction

- **作者**: Yuheng Lai, Garvesh Raskutti
- **发布日期**: 2026-05-06
- **链接**: [arXiv:2605.05497v2](https://arxiv.org/abs/2605.05497v2) | [PDF](https://arxiv.org/pdf/2605.05497v2)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Conformal prediction is a framework that provides valid uncertainty quantification for general models with exchangeable data.

However, in the online learning and time-series settings, exchangeability is not satisfied.

Existing online conformal methods, such as adaptive conformal inference (ACI), can achieve long-run validity, yet they remain inefficient under covariate heterogeneity because they rely on global calibration.

We propose \emph{Online Localized Conformal Prediction (OLCP)}, which combines online adaptation with covariate-dependent localization to better reflect heterogeneity.

To re

### AI 总结

总结生成失败

---

