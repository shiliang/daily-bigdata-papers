# 大数据+AI 领域论文日报

**日期**: 2026-03-21

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Modeling Overlapped Speech with Shu...](https://arxiv.org/abs/2603.17769v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Genetic Algorithms in Regression](https://arxiv.org/abs/2603.14801v2) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [AutoScout: Structured Optimization ...](https://arxiv.org/abs/2603.11603v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [TensorCircuit-NG: A Universal, Comp...](https://arxiv.org/abs/2602.14167v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [SCPL: Enhancing Neural Network Trai...](https://arxiv.org/abs/2602.00062v2) | 待分析 | 评估失败 | [Code](https://github.com/minyaho/scpl) | 20/43 |
| 6 | [Towards Resiliency in Large Languag...](https://arxiv.org/abs/2601.22438v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Quantum Model Parallelism for MRI-B...](https://arxiv.org/abs/2602.00128v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Path Types in Algebraic Type Theory](https://arxiv.org/abs/2601.06567v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Heterogeneous Low-Bandwidth Pre-Tra...](https://arxiv.org/abs/2601.02360v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [FastMPS: Revisit Data Parallel in L...](https://arxiv.org/abs/2512.20064v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Modeling Overlapped Speech with Shuffles

- **作者**: Matthew Wiesner, Samuele Cornell, Alexander Polok, Lucas Ondel Yang, Lukáš Burget
- **发布日期**: 2026-03-18
- **链接**: [arXiv:2603.17769v1](https://arxiv.org/abs/2603.17769v1) | [PDF](https://arxiv.org/pdf/2603.17769v1)
- **分类**: cs.SD, cs.CL, cs.LG, eess.AS
- **含金量**: 20/43 分

### 摘要

We propose to model parallel streams of data, such as overlapped speech, using shuffles.

Specifically, this paper shows how the shuffle product and partial order finite-state automata (FSAs) can be used for alignment and speaker-attributed transcription of overlapped speech.

We train using the total score on these FSAs as a loss function, marginalizing over all possible serializations of overlapping sequences at subword, word, and phrase levels.

To reduce graph size, we impose temporal constraints by constructing partial order FSAs.

We address speaker attribution by modeling (token, speaker) t

### AI 总结

总结生成失败

---

## 2. Genetic Algorithms in Regression

- **作者**: Mo Li, QiQi Lu, Robert Lund, Xueheng Shi
- **发布日期**: 2026-03-16
- **链接**: [arXiv:2603.14801v2](https://arxiv.org/abs/2603.14801v2) | [PDF](https://arxiv.org/pdf/2603.14801v2)
- **分类**: stat.AP, stat.CO
- **含金量**: 20/43 分

### 摘要

Many statistical problems involve optimization over a discrete parameter space having an unknown dimension.

In such settings, gradient-based methods often fail due to the non-differentiability of the objective function or a non-convex or massive search space with an objective function having many local maxima/minima.

This paper presents GAReg, a unified genetic algorithm package that handles discrete optimization regression problems, which works well when standard algorithms are unjustified.

GAReg provides a compact chromosome representation supporting optimal knot placement for regression spl

### AI 总结

总结生成失败

---

## 3. AutoScout: Structured Optimization for Automating ML System Configuration

- **作者**: Jimmy Shong, Yuhan Ding, Yihan Jiang, Liheng Jing, Haonan Chen
- **发布日期**: 2026-03-12
- **链接**: [arXiv:2603.11603v1](https://arxiv.org/abs/2603.11603v1) | [PDF](https://arxiv.org/pdf/2603.11603v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Machine learning (ML) systems expose a rapidly expanding configuration space spanning model-parallelism strategies, communication optimizations, and low-level runtime parameters.

End-to-end system efficiency is highly sensitive to these choices, yet identifying high-performance configurations is challenging due to heterogeneous feature types (e.g., sparse and dense parameters), conditional dependencies (e.g., valid execution parameters only under specific upstream decisions), and the high search (profiling) cost.

Existing approaches either optimize a narrow subset of configuration dimensions o

### AI 总结

总结生成失败

---

## 4. TensorCircuit-NG: A Universal, Composable, and Scalable Platform for Quantum Computing and Quantum Simulation

- **作者**: Shi-Xin Zhang, Yu-Qin Chen, Weitang Li, Jiace Sun, Wei-Guo Ma
- **发布日期**: 2026-02-15
- **链接**: [arXiv:2602.14167v1](https://arxiv.org/abs/2602.14167v1) | [PDF](https://arxiv.org/pdf/2602.14167v1)
- **分类**: quant-ph
- **含金量**: 20/43 分

### 摘要

We present TensorCircuit-NG, a next-generation quantum software platform designed to bridge the gap between quantum physics, artificial intelligence, and high-performance computing.

Moving beyond the scope of traditional circuit simulators, TensorCircuit-NG establishes a unified, tensor-native programming paradigm where quantum circuits, tensor networks, and neural networks fuse into a single, end-to-end differentiable computational graph.

Built upon industry-standard machine learning backends (JAX, TensorFlow, PyTorch), the framework introduces comprehensive capabilities for approximate circu

### AI 总结

总结生成失败

---

## 5. SCPL: Enhancing Neural Network Training Throughput with Decoupled Local Losses and Model Parallelism

- **作者**: Ming-Yao Ho, Cheng-Kai Wang, You-Teng Lin, Hung-Hsuan Chen
- **发布日期**: 2026-01-20
- **链接**: [arXiv:2602.00062v2](https://arxiv.org/abs/2602.00062v2) | [PDF](https://arxiv.org/pdf/2602.00062v2)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/minyaho/scpl) ⭐ 0 (Python)

### 摘要

Adopting large-scale AI models in enterprise information systems is often hindered by high training costs and long development cycles, posing a significant managerial challenge.

The standard end-to-end backpropagation (BP) algorithm is a primary driver of modern AI, but it is also the source of inefficiency in training deep networks.

This paper introduces a new training methodology, Supervised Contrastive Parallel Learning (SCPL), that addresses this issue by decoupling BP and transforming a long gradient flow into multiple short ones.

This design enables the simultaneous computation of parame

### AI 总结

总结生成失败

---

## 6. Towards Resiliency in Large Language Model Serving with KevlarFlow

- **作者**: Shangshu Qian, Kipling Liu, P. C. Sruthi, Lin Tan, Yongle Zhang
- **发布日期**: 2026-01-30
- **链接**: [arXiv:2601.22438v1](https://arxiv.org/abs/2601.22438v1) | [PDF](https://arxiv.org/pdf/2601.22438v1)
- **分类**: cs.DC, cs.CL, cs.LG
- **含金量**: 20/43 分

### 摘要

Large Language Model (LLM) serving systems remain fundamentally fragile, where frequent hardware faults in hyperscale clusters trigger disproportionate service outages in the software stack.

Current recovery mechanisms are prohibitively slow, often requiring up to 10 minutes to reinitialize resources and reload massive model weights.

We introduce KevlarFlow, a fault tolerant serving architecture designed to bridge the gap between hardware unreliability and service availability.

KevlarFlow leverages 1) decoupled model parallelism initialization, 2) dynamic traffic rerouting, and 3) background K

### AI 总结

总结生成失败

---

## 7. Quantum Model Parallelism for MRI-Based Classification of Alzheimer's Disease Stages

- **作者**: Emine Akpinar, Murat Oduncuoglu
- **发布日期**: 2026-01-28
- **链接**: [arXiv:2602.00128v1](https://arxiv.org/abs/2602.00128v1) | [PDF](https://arxiv.org/pdf/2602.00128v1)
- **分类**: cs.LG, quant-ph
- **含金量**: 20/43 分

### 摘要

With increasing life expectancy, AD has become a major global health concern.

While classical AI-based methods have been developed for early diagnosis and stage classification of AD, growing data volumes and limited computational resources necessitate faster, more efficient approaches.

Quantum-based AI methods, which leverage superposition and entanglement principles along with high-dimensional Hilbert space, can surpass classical approaches' limitations and offer higher accuracy for high-dimensional, heterogeneous, and noisy data.

In this study, a Quantum-Based Parallel Model (QBPM) architect

### AI 总结

总结生成失败

---

## 8. Path Types in Algebraic Type Theory

- **作者**: Steve Awodey, Joseph Hua
- **发布日期**: 2026-01-10
- **链接**: [arXiv:2601.06567v1](https://arxiv.org/abs/2601.06567v1) | [PDF](https://arxiv.org/pdf/2601.06567v1)
- **分类**: math.CT, math.AT, math.LO
- **含金量**: 20/43 分

### 摘要

A new approach to the semantics of identity types in intensional Martin-Löf type theory is proposed, assuming only a category with finite limits and an interval.

The specification of \emph{extensional} identity types in the original presentation of natural models paralleled that of the other type formers $Σ$ and $Π$, but the treatment of the \emph{intensional} case there was less uniform.

It was later reformulated to an account based on polynomials; here a further improvement in the style of the other type formers is achieved by employing an interval, in order to give a single pullback specifi

### AI 总结

总结生成失败

---

## 9. Heterogeneous Low-Bandwidth Pre-Training of LLMs

- **作者**: Yazan Obeidi, Amir Sarfi, Joel Lidin, Paul Janson, Eugene Belilovsky
- **发布日期**: 2026-01-05
- **链接**: [arXiv:2601.02360v1](https://arxiv.org/abs/2601.02360v1) | [PDF](https://arxiv.org/pdf/2601.02360v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Pre-training large language models (LLMs) increasingly requires distributed compute, yet bandwidth constraints make it difficult to scale beyond well-provisioned datacenters-especially when model parallelism forces frequent, large inter-device communications.

We study whether SparseLoCo, a low-communication data parallel method based on infrequent synchronization and sparse pseudo-gradient exchange, can be combined with low-bandwidth pipeline model parallelism via activation and activation-gradient compression.

We introduce a heterogeneous distributed training framework where some participants

### AI 总结

总结生成失败

---

## 10. FastMPS: Revisit Data Parallel in Large-scale Matrix Product State Sampling

- **作者**: Yaojian Chen, Si-Qiu Gong, Lin Gan, Yanfei Liu, An Yang
- **发布日期**: 2025-12-23
- **链接**: [arXiv:2512.20064v1](https://arxiv.org/abs/2512.20064v1) | [PDF](https://arxiv.org/pdf/2512.20064v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

Matrix Product State (MPS) is a versatile tensor network representation widely applied in quantum physics, quantum chemistry, and machine learning, etc.

MPS sampling serves as a critical fundamental operation in these fields.

As the problems become more complex, the scale of MPS is rapidly increasing.

Traditional data parallelism is limited by memory and heavy I/O in large-scale MPS.

Model parallelism that can handle large-scale MPS imposes rigid process bindings and lacks scalability.

This work proposes Fast-MPS, a multi-level parallel framework for scalable MPS sampling.

Our design combines 

### AI 总结

总结生成失败

---

