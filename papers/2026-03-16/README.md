# 大数据领域论文日报

**日期**: 2026-03-16

**论文数量**: 10

---

## 1. Nyxus: A Next Generation Image Feature Extraction Library for the Big Data and AI Era

- **作者**: Nicholas Schaub, Andriy Kharchenko, Hamdah Abbasi, Sameeul Samee, Hythem Sidky
- **发布日期**: 2026-03-12
- **链接**: [arXiv:2603.12016v1](https://arxiv.org/abs/2603.12016v1) | [PDF](https://arxiv.org/pdf/2603.12016v1)
- **分类**: cs.CV, q-bio.QM

### 摘要

Modern imaging instruments can produce terabytes to petabytes of data for a single experiment.

The biggest barrier to processing big image datasets has been computational, where image analysis algorithms often lack the efficiency needed to process such large datasets or make tradeoffs in robustness and accuracy.

Deep learning algorithms have vastly improved the accuracy of the first step in an analysis workflow (region segmentation), but the expansion of domain specific feature extraction libraries across scientific disciplines has made it difficult to compare the performance and accuracy of e

### AI 总结

**概述**：本文介绍了 Nyxus，一个专为大数据和 AI 时代设计的可扩展图像特征提取库，支持 2D/3D 数据处理。

**核心贡献**：
- 开发了支持 2D/3D 图像数据可扩展核外特征提取的 Nyxus 库
- 提供涵盖放射组学和细胞分析等多领域的综合特征集
- 提供 Python 包、命令行、Napari 插件及容器等多种访问方式

**技术要点**：
- 支持跨 CPU 和 GPU 的计算可扩展性
- 允许程序化调优特征集以优化效率或覆盖范围

**应用场景**：放射组学、细胞分析、云计算工作流、超级计算、机器学习与深度学习应用

---

## 2. Deep Domain Decomposition Method for Solving the Variational Inequality Problems

- **作者**: Yiyang Wang, Qijia Zhou, Shengyuan Deng, Chenliang Li
- **发布日期**: 2026-03-12
- **链接**: [arXiv:2603.11552v1](https://arxiv.org/abs/2603.11552v1) | [PDF](https://arxiv.org/pdf/2603.11552v1)
- **分类**: math.NA

### 摘要

By integrating physics-informed neural network (PINN) techniques with domain decomposition method, a deep domain decomposition method is presented for solving elliptic variational inequality problems.

Based on the Ritz variation method, the elliptic variational inequality problem is firstly reformulated as an optimization problem, and then the subproblem in each subdomain is solved by using the Ritz-PINN method, which the parameters in the network are updated by the Adam optimizer, and the residual-adaptive training by introducing a residual-adaptive dataset update strategy to gradually guide 

### AI 总结

**概述**：本文提出融合物理信息神经网络与域分解方法的深度算法，用于高效求解椭圆变分不等式问题。

**核心贡献**：
- 提出了结合 PINN 与域分解方法的深度域分解算法
- 引入残差自适应数据集更新策略以引导模型学习复杂区域
- 验证了算法在均匀重叠条件下迭代次数与网格长度无关

**技术要点**：
- 基于 Ritz 变分法将问题重构为优化问题
- 采用 Ritz-PINN 方法求解子域子问题并使用 Adam 优化器更新参数

**应用场景**：椭圆变分不等式问题、科学计算中的偏微分方程求解

---

## 3. Evaluation of LLMs in retrieving food and nutritional context for RAG systems

- **作者**: Maks Požarnik Vavken, Matevž Ogrinc, Tome Eftimov, Barbara Koroušić Seljak
- **发布日期**: 2026-03-10
- **链接**: [arXiv:2603.09704v2](https://arxiv.org/abs/2603.09704v2) | [PDF](https://arxiv.org/pdf/2603.09704v2)
- **分类**: cs.CL

### 摘要

In this article, we evaluate four Large Language Models (LLMs) and their effectiveness at retrieving data within a specialized Retrieval-Augmented Generation (RAG) system, using a comprehensive food composition database.

Our method is focused on the LLMs ability to translate natural language queries into structured metadata filters, enabling efficient retrieval via a Chroma vector database.

By achieving high accuracy in this critical retrieval step, we demonstrate that LLMs can serve as an accessible, high-performance tool, drastically reducing the manual effort and technical expertise previou

### AI 总结

**概述**：本文评估了四种大语言模型在食物营养 RAG 系统中将自然语言查询转化为结构化元数据过滤器的有效性。

**核心贡献**：
- 评估了四种 LLM 在专用食物成分数据库 RAG 系统中的检索效果
- 证明 LLM 能降低领域专家使用复杂数据的技术门槛和手动工作量
- 揭示了 LLM 在处理无法明确表达的约束条件时检索可靠性下降的问题

**技术要点**：
- 利用 LLM 将自然语言查询翻译为结构化元数据过滤器以实现高效检索
- 基于 Chroma 向量数据库构建检索增强生成（RAG）系统进行验证

**应用场景**：食物编纂者、营养师、食物营养数据查询系统

---

## 4. Fusing Semantic, Lexical, and Domain Perspectives for Recipe Similarity Estimation

- **作者**: Denica Kjorvezir, Danilo Najkov, Eva Valencič, Erika Jesenko, Barbara Koroišić Seljak
- **发布日期**: 2026-03-10
- **链接**: [arXiv:2603.09688v2](https://arxiv.org/abs/2603.09688v2) | [PDF](https://arxiv.org/pdf/2603.09688v2)
- **分类**: cs.CL

### 摘要

This research focuses on developing advanced methods for assessing similarity between recipes by combining different sources of information and analytical approaches.

We explore the semantic, lexical, and domain similarity of food recipes, evaluated through the analysis of ingredients, preparation methods, and nutritional attributes.

A web-based interface was developed to allow domain experts to validate the combined similarity results.

After evaluating 318 recipe pairs, experts agreed on 255 (80%).

The evaluation of expert assessments enables the estimation of which similarity aspects--lexica

### AI 总结

**概述**：本文提出融合语义、词汇和领域视角的食谱相似度评估方法，并通过专家验证分析了各因素的影响力。

**核心贡献**：
- 提出融合语义、词汇及领域信息的食谱相似度综合评估方法
- 开发基于 Web 的接口供领域专家验证相似度结果
- 通过专家评估确定了影响决策的关键相似度维度

**技术要点**：
- 分析食材、制作方法及营养属性以计算多维度相似度
- 基于 318 对食谱的专家评估验证方法有效性（一致率 80%）

**应用场景**：食品工业、个性化饮食、营养推荐、自动食谱生成

---

## 5. A New Modeling to Feature Selection Based on the Fuzzy Rough Set Theory in Normal and Optimistic States on Hybrid Information Systems

- **作者**: Mohammad Hossein Safarpour, Seyed Majid Alavi, Mohammad Izadikhah, Hossein Dibachi
- **发布日期**: 2026-03-09
- **链接**: [arXiv:2603.08900v2](https://arxiv.org/abs/2603.08900v2) | [PDF](https://arxiv.org/pdf/2603.08900v2)
- **分类**: cs.LG, cs.AI

### 摘要

Considering the high volume, wide variety, and rapid speed of data generation, investigating feature selection methods for big data presents various applications and advantages.

By removing irrelevant and redundant features, feature selection reduces data dimensions, thereby facilitating optimal decision-making within decision systems.

One of the key tools for feature selection in hybrid information systems is fuzzy rough set theory.

However, this theory faces two significant challenges: First, obtaining fuzzy equivalence relations through intersection operations in high-dimensional spaces can

### AI 总结

**概述**：本文提出特征选择模型，利用对象距离构建模糊等价关系，将问题转为优化求解，解决高维数据效率与噪声难题

**核心贡献**：
- 提出新模型解决模糊粗糙集在高维空间计算耗时及产生噪声数据的问题
- 将特征选择重构为优化问题，可利用合适的元启发式算法进行求解
- 设计正常和乐观两种运行模式，基于两种引入的模糊等价关系进行选择

**技术要点**：
- 通过计算对象间的组合距离来推导模糊等价关系，避免直接交集运算
- 在 UCI 标准数据集上测试，对比证明该方法比现有算法更高效有效

**应用场景**：混合信息系统、大数据特征选择、决策系统优化

---

## 6. Measuring onion website discovery and Tor users' interests with honeypots

- **作者**: Arttu Paju, Waris Abdullah, Juha Nurmi
- **发布日期**: 2026-03-10
- **链接**: [arXiv:2603.09329v1](https://arxiv.org/abs/2603.09329v1) | [PDF](https://arxiv.org/pdf/2603.09329v1)
- **分类**: cs.CR

### 摘要

Tor enables anonymous web browsing and access to anonymous onion websites.

Prior work has focused on crawling and content analysis rather than on what users actually try to access.

Our honeypot approach measures engagement across onion-site categories, revealing behavioral interest rather than inferred popularity.

In March--April 2025, we deployed honeypot onion websites and seeded neutral-looking links via three channels -- the Ahmia Tor search engine, Stronghold paste onion "paste" service, and pastebin.com -- to observe discovery and subsequent interaction events (CAPTCHA solves; registrati

### AI 总结

**概述**：本文利用蜜罐技术测量 Tor 用户发现洋葱网站的路径，并揭示了对不同非法内容类别的实际行为兴趣。

**核心贡献**：
- 提出蜜罐方法以测量用户实际交互兴趣，弥补了仅依赖内容爬取的不足
- 证实 Ahmia 搜索引擎是 Tor 用户发现洋葱网站近乎唯一的来源
- 发现儿童性虐待材料（CSAM）主题引发的用户参与度显著高于其他犯罪类别

**技术要点**：
- 通过 Ahmia、Stronghold 等多个渠道植入链接以观察网站发现机制
- 记录 CAPTCHA 解决与登录尝试等事件，对比不同主题及语言版本的交互差异

**应用场景**：Tor 网络流量分析、网络犯罪趋势监控、匿名用户行为研究

---

## 7. Nezha: A Key-Value Separated Distributed Store with Optimized Raft Integration

- **作者**: Yangyang Wang, Yucong Dong, Ziqian Cheng, Zichen Xu
- **发布日期**: 2026-03-10
- **链接**: [arXiv:2603.09122v1](https://arxiv.org/abs/2603.09122v1) | [PDF](https://arxiv.org/pdf/2603.09122v1)
- **分类**: cs.DC, cs.DB

### 摘要

Distributed key-value stores are widely adopted to support elastic big data applications, leveraging purpose-built consensus algorithms like Raft to ensure data consistency.

However, through systematic analysis, we reveal a critical performance issue in such consistent stores, i.e., overlapping persistence operations between consensus protocols and underlying storage engines result in significant I/O overhead.

To address this issue, we present Nezha, a prototype distributed storage system that innovatively integrates key-value separation with Raft to provide scalable throughput in a strong con

### AI 总结

**概述**：本文提出 Nezha 系统，通过键值分离与 Raft 优化集成，解决持久化重叠 I/O 开销问题，显著提升吞吐性能。

**核心贡献**：
- 揭示了共识协议与存储引擎间持久化操作重叠导致的性能瓶颈。
- 设计了 Nezha 系统，创新集成键值分离与 Raft 以保证强一致性高吞吐。
- 实验证明 Nezha 在写、读及扫描操作上平均吞吐量提升显著。

**技术要点**：
- 操作级别的持久化策略重设计。
- 引入分层垃圾回收机制。

**应用场景**：弹性大数据应用、强一致性分布式存储系统

---

## 8. MAcPNN: Mutual Assisted Learning on Data Streams with Temporal Dependence

- **作者**: Federico Giannini, Emanuele Della Valle
- **发布日期**: 2026-03-09
- **链接**: [arXiv:2603.08972v1](https://arxiv.org/abs/2603.08972v1) | [PDF](https://arxiv.org/pdf/2603.08972v1)
- **分类**: cs.LG

### 摘要

Internet of Things (IoT) Analytics often involves applying machine learning (ML) models on data streams.

In such scenarios, traditional ML paradigms face obstacles related to continuous learning while dealing with concept drifts, temporal dependence, and avoiding forgetting.

Moreover, in IoT, different edge devices build up a network.

When learning models on those devices, connecting them could be useful in improving performance and reusing others' knowledge.

This work proposes Mutual Assisted Learning, a learning paradigm grounded on Vygotsky's popular Sociocultural Theory of Cognitive Develo

### AI 总结

**概述**：本文提出 MAcPNN 框架，利用互助学习范式处理物联网数据流，解决概念漂移与遗忘问题并减少通信开销。

**核心贡献**：
- 提出基于维果茨基理论的互助学习范式，实现设备间自主知识共享
- 相比联邦学习大幅减少通信连接，仅在性能下降时请求协助
- 在合成及真实数据流上验证了该方法提升性能的有效性

**技术要点**：
- 采用连续渐进神经网络（cPNN）处理数据流的动态性及时间依赖
- 应用量化技术减少内存占用，支持单数据点预测

**应用场景**：物联网分析、边缘设备网络、含概念漂移的数据流处理

---

## 9. Don't Look Back in Anger: MAGIC Net for Streaming Continual Learning with Temporal Dependence

- **作者**: Federico Giannini, Sandro D'Andrea, Emanuele Della Valle
- **发布日期**: 2026-03-09
- **链接**: [arXiv:2603.08600v1](https://arxiv.org/abs/2603.08600v1) | [PDF](https://arxiv.org/pdf/2603.08600v1)
- **分类**: cs.LG, cs.AI

### 摘要

Concept drift, temporal dependence, and catastrophic forgetting represent major challenges when learning from data streams.

While Streaming Machine Learning and Continual Learning (CL) address these issues separately, recent efforts in Streaming Continual Learning (SCL) aim to unify them.

In this work, we introduce MAGIC Net, a novel SCL approach that integrates CL-inspired architectural strategies with recurrent neural networks to tame temporal dependence.

MAGIC Net continuously learns, looks back at past knowledge by applying learnable masks over frozen weights, and expands its architecture 

### AI 总结

**概述**：本文提出 MAGIC Net，结合 CL 策略与 RNN 的流式持续学习方法，处理时间依赖并缓解遗忘。

**核心贡献**：
- 提出 MAGIC Net 框架，统一解决流式学习中的概念漂移、时间依赖与灾难性遗忘问题。
- 实现在线持续学习机制，确保模型在任何时刻均可用进行推理，无需离线中断。
- 通过合成与真实数据流实验，验证了其在适应新概念及限制内存使用方面的有效性。

**技术要点**：
- 集成持续学习架构策略与循环神经网络，以有效捕捉数据流中的时间依赖性。
- 采用冻结权重上的可学习掩码回顾过往知识，并根据需要动态扩展网络架构。

**应用场景**：数据流处理、流式机器学习、持续学习系统

---

## 10. TS-MLLM: A Multi-Modal Large Language Model-based Framework for Industrial Time-Series Big Data Analysis

- **作者**: Haiteng Wang, Yikang Li, Yunfei Zhu, Jingheng Yan, Lei Ren
- **发布日期**: 2026-03-08
- **链接**: [arXiv:2603.07572v1](https://arxiv.org/abs/2603.07572v1) | [PDF](https://arxiv.org/pdf/2603.07572v1)
- **分类**: cs.LG

### 摘要

Accurate analysis of industrial time-series big data is critical for the Prognostics and Health Management (PHM) of industrial equipment.

While recent advancements in Large Language Models (LLMs) have shown promise in time-series analysis, existing methods typically focus on single-modality adaptations, failing to exploit the complementary nature of temporal signals, frequency-domain visual representations, and textual knowledge information.

In this paper, we propose TS-MLLM, a unified multi-modal large language model framework designed to jointly model temporal signals, frequency-domain image

### AI 总结

**概述**：论文提出 TS-MLLM 框架，联合建模时序信号、频域图像和文本知识，用于工业时间序列大数据分析。

**核心贡献**：
- 提出 TS-MLLM 框架，联合建模时序信号、频域图像和文本领域知识
- 引入频谱感知视觉语言模型适配机制，内化频域模式与语义上下文
- 设计时序中心多模态注意力融合机制，确保深度跨模态对齐

**技术要点**：
- 工业时间序列 Patch 建模分支捕捉长程时序动态
- 以时序特征为查询主动检索相关视觉和文本线索

**应用场景**：工业设备预测与健康管理、工业时间序列预测、少样本及复杂场景分析

---

