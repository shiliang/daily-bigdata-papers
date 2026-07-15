# 大数据+AI 领域论文日报

**日期**: 2026-07-15

**论文数量**: 6 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Antiproof: Synthesizing Vulnerabili...](https://arxiv.org/abs/2607.12316v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Real-time fall detection based on v...](https://arxiv.org/abs/2607.12909v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [WanToFight: Real-Time Generative Ga...](https://arxiv.org/abs/2607.12592v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Cost-Governed RAG: Unified Per-Tena...](https://arxiv.org/abs/2607.12188v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [LiteTopK: Exploiting the Curse of D...](https://arxiv.org/abs/2607.11976v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [SymbOmni: Evolving Agentic Omni Mod...](https://arxiv.org/abs/2607.12042v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Antiproof: Synthesizing Vulnerability Detectors and Proofs of Exploitability

- **作者**: Alon Shakevsky, Corban Villa, Ion Stoica, Raluca Ada Popa
- **发布日期**: 2026-07-14
- **链接**: [arXiv:2607.12316v1](https://arxiv.org/abs/2607.12316v1) | [PDF](https://arxiv.org/pdf/2607.12316v1)
- **分类**: cs.CR
- **含金量**: 20/43 分

### 摘要

Discovering vulnerabilities before attackers exploit them requires high recall and reliable automatic validation, but existing approaches struggle to achieve both without prohibitive cost.

We present Antiproof, an end-to-end vulnerability discovery system that combines neuro-symbolic detector synthesis for high-recall discovery with proof-of-exploitability oracles for automatic validation.

Antiproof learns and iteratively refines static detectors from vulnerability datasets, then validates candidates by verifying whether executable proofs demonstrate concrete attacker capabilities.

Evaluated o

### AI 总结

总结生成失败

---

## 2. Real-time fall detection based on vision for low-power edge platforms

- **作者**: Wenjun Xia, Zhicheng Peng, Haopeng Li, Zhengdi Zhang
- **发布日期**: 2026-07-14
- **链接**: [arXiv:2607.12909v1](https://arxiv.org/abs/2607.12909v1) | [PDF](https://arxiv.org/pdf/2607.12909v1)
- **分类**: q-bio.NC, cs.AI, cs.CV
- **含金量**: 20/43 分

### 摘要

Falling detection is vital for elderly care and intelligent surveillance; however, prevailing vision-based approaches predominantly frame it as static pose classification or discrete temporal pattern matching, fundamentally overlooking the instability dynamics of the human support system.

This paper proposes a physics-informed falling detection framework that recasts falling as a stability-loss event in a coupled dynamical system.

We introduce a novel dual-LTC architecture comprising a Center-of-Mass (CoM) subsystem and a Base-of-Support (BoS) subsystem, both instantiated as Liquid Time-Consta

### AI 总结

总结生成失败

---

## 3. WanToFight: Real-Time Generative Game Engine for Multi-Player Combat Interaction

- **作者**: Li Hu, Guangyuan Wang, Peng Zhang, Bang Zhang
- **发布日期**: 2026-07-14
- **链接**: [arXiv:2607.12592v1](https://arxiv.org/abs/2607.12592v1) | [PDF](https://arxiv.org/pdf/2607.12592v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

We present WanToFight, a generative game engine that simulates real-time, two-player The King of Fighters '97 (KOF~'97) gameplay from keyboard input.

Prior generative game engines target either single-player first-person settings or non-real-time cooperative scenarios; multi-player control, real-time inference, complex physical interaction, and adversarial gameplay have not been jointly addressed.

WanToFight closes this gap with three components built on the Wan-1.3B video diffusion transformer: a streaming autoregressive generator with block-causal attention and a rolling KV cache; a visually

### AI 总结

总结生成失败

---

## 4. Cost-Governed RAG: Unified Per-Tenant Cost Attribution Across Retrieval and Generation in Multi-Tenant LLM Systems

- **作者**: Navnit Shukla
- **发布日期**: 2026-07-13
- **链接**: [arXiv:2607.12188v1](https://arxiv.org/abs/2607.12188v1) | [PDF](https://arxiv.org/pdf/2607.12188v1)
- **分类**: cs.AI, cs.DB, cs.IR
- **含金量**: 20/43 分

### 摘要

Enterprise Retrieval-Augmented Generation (RAG) deployments face a critical governance gap: while LLM generation cost is metered per token, the retrieval layer - vector memory, similarity compute, and embedding API calls - remains an unattributed shared cost, enabling invisible cross-subsidization among tenants.

We present Cost-Governed RAG, an architecture that integrates a codebook-oblivious vector index (TurboVec) with a multi-tenant LLM governance gateway, creating a unified observability stack where embedding, retrieval, and generation costs are jointly attributable per tenant.

The archit

### AI 总结

总结生成失败

---

## 5. LiteTopK: Exploiting the Curse of Dimensionality for a Fused Indexer-TopK Kernel in Long-Context Sparse Attention

- **作者**: Ziqi Yin, Jianyang Gao, Peiqi Yin, Jiangneng Li, Gao Cong
- **发布日期**: 2026-07-13
- **链接**: [arXiv:2607.11976v1](https://arxiv.org/abs/2607.11976v1) | [PDF](https://arxiv.org/pdf/2607.11976v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Indexer-TopK, the operation to compute the scores and select the top-k candidates, is widely used by sparse attention kernels in large language models and vector retrieval in recommendation systems and vector databases.

However, existing GPU-based Indexer-TopK kernels like DeepSeek Sparse Attention (DSA) remain inefficient due to excessive global memory traffic, costly synchronization, and prohibitive memory overhead.

In this work, we exploit the curse of dimensionality in high-dimensional spaces, where distances between high-dimensional vectors tend to concentrate within a narrow range, to de

### AI 总结

总结生成失败

---

## 6. SymbOmni: Evolving Agentic Omni Models via Symbolic Concept Learning

- **作者**: Jinxiu Liu, Jianru Li, Tanqing Kuang, Xuanming Liu, Kangfu Mei
- **发布日期**: 2026-07-13
- **链接**: [arXiv:2607.12042v1](https://arxiv.org/abs/2607.12042v1) | [PDF](https://arxiv.org/pdf/2607.12042v1)
- **分类**: cs.CV, cs.LG
- **含金量**: 20/43 分

### 摘要

Visual generation is increasingly ubiquitous in diverse domains, from text-to-image/video synthesis to multimodal interactive creation.

Yet prevailing monolithic models remain fundamentally constrained by their inability to learn cumulatively and evolve autonomously, which is a limitation we term the "perpetual novice" problem.

They lack mechanisms for structuring experience into reusable knowledge and therefore rely on brittle, "from-scratch" reasoning for each task, resulting in poor compositional generalization and inefficient knowledge retention.

Motivated by these limitations, we propose 

### AI 总结

总结生成失败

---

