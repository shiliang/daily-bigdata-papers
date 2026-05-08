# 大数据+AI 领域论文日报

**日期**: 2026-05-08

**论文数量**: 4 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Quantizing With Randomized Hadamard...](https://arxiv.org/abs/2605.06014v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Open-SAT: LLM-Guided Query Embeddin...](https://arxiv.org/abs/2605.05344v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Career-Aware Resume Tailoring via M...](https://arxiv.org/abs/2605.05257v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Topology-Driven Anti-Entanglement C...](https://arxiv.org/abs/2605.05236v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Quantizing With Randomized Hadamard Transforms: Efficient Heuristic Now Proven

- **作者**: Ran Ben-Basat, William Kuszmaul, Michael Mitzenmacher, Amit Portnoy, Shay Vargaftik
- **发布日期**: 2026-05-07
- **链接**: [arXiv:2605.06014v1](https://arxiv.org/abs/2605.06014v1) | [PDF](https://arxiv.org/pdf/2605.06014v1)
- **分类**: cs.LG, cs.AI, cs.DS, cs.NI
- **含金量**: 20/43 分

### 摘要

Uniform random rotations (URRs) are a common preprocessing step in modern quantization approaches used for gradient compression, inference acceleration, KV-cache compression, model weight quantization, and approximate nearest-neighbor search in vector databases.

In practice, URRs are often replaced by randomized Hadamard transforms (RHTs), which preserve orthogonality while admitting fast implementations.

The remaining issue is the performance for worst-case inputs.

With a URR, each coordinate is individually distributed as a shifted beta distribution, which converges to a Gaussian distributio

### AI 总结

总结生成失败

---

## 2. Open-SAT: LLM-Guided Query Embedding Refinement for Open-Vocabulary Object Retrieval in Satellite Imagery

- **作者**: Md Adnan Arefeen, Biplob Debnath, Ravi K. Rajendran, Murugan Sankaradas, Srimat T. Chakradhar
- **发布日期**: 2026-05-06
- **链接**: [arXiv:2605.05344v1](https://arxiv.org/abs/2605.05344v1) | [PDF](https://arxiv.org/pdf/2605.05344v1)
- **分类**: cs.CV, cs.AI, cs.IR
- **含金量**: 20/43 分

### 摘要

In satellite applications, user queries often take the form of open-ended natural language, extending beyond a fixed set of predefined categories.

This open-vocabulary nature poses significant challenges for retrieving relevant image tiles, as the retrieval system must generalize to a wide range of unseen objects and concepts.

While vision-language models (VLMs) such as CLIP are widely used for text-image retrieval, even fine-tuned variants often struggle to accurately align such queries with satellite imagery.

To address this, we propose Open-SAT, a training-free query embedding refinement al

### AI 总结

总结生成失败

---

## 3. Career-Aware Resume Tailoring via Multi-Source Retrieval-Augmented Generation with Provenance Tracking: A Case Study

- **作者**: Kumar Abhinav
- **发布日期**: 2026-05-06
- **链接**: [arXiv:2605.05257v1](https://arxiv.org/abs/2605.05257v1) | [PDF](https://arxiv.org/pdf/2605.05257v1)
- **分类**: cs.IR, cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

AI-assisted resume tailoring systems commonly operate on a single uploaded resume, which limits their ability to recover relevant experience omitted from the current draft and makes it difficult for users to distinguish grounded edits from model-generated suggestions.

This paper presents Resume Tailor, an agentic resume-tailoring system that maintains a longitudinal career vault in a vector database and uses multi-source retrieval-augmented generation (RAG) to assemble job-specific resume content from historical resumes and structured career records.

The system is implemented as a 12-node Lang

### AI 总结

总结生成失败

---

## 4. Topology-Driven Anti-Entanglement Control for Soft Robots

- **作者**: Haoyang Le, Shengxuan Wang, Mohan Chen, Shuo Feng
- **发布日期**: 2026-05-01
- **链接**: [arXiv:2605.05236v1](https://arxiv.org/abs/2605.05236v1) | [PDF](https://arxiv.org/pdf/2605.05236v1)
- **分类**: cs.RO, cs.AI
- **含金量**: 20/43 分

### 摘要

In the field of precision manufacturing in complex constrained environments, the role of soft robots is increasingly prominent, and the realization of anti-winding control based on multi-intelligent body reinforcement learning has become a research hotspot.

One of the core problems at present is to coordinate multiple robots to complete the unwinding operation in a highly constrained environment.

The existing distributed training framework faces some observability challenges in high-density barrier and unstable environments, resulting in poor learning results.

This paper proposes a topology-dr

### AI 总结

总结生成失败

---

