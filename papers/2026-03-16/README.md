# 大数据领域论文日报

**日期**: 2026-03-16

**论文数量**: 60

---

## 1. Multimodal OCR: Parse Anything from Documents

**作者**: Handong Zheng, Yumeng Li, Kaile Zhang, Liang Xin, Guangwei Zhao
**发布日期**: 2026-03-13
**arXiv ID**: [2603.13032v1](https://arxiv.org/abs/2603.13032v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.13032v1)
**分类**: cs.CV

### 论文摘要

We present Multimodal OCR (MOCR), a document parsing paradigm that jointly parses text and graphics into unified textual representations. Unlike conventional OCR systems that focus on text recognition and leave graphical regions as cropped pixels, our method, termed dots.mocr, treats visual elements such as charts, diagrams, tables, and icons as first-class parsing targets, enabling systems to parse documents while preserving semantic relationships across elements. It offers several advantages: ...

### AI 总结

1. **一句话概述**
本文提出 MOCR 范式，将文档文本与图形统一解析为结构化表示，支持端到端训练，解析性能达到业界领先水平。

2. **核心贡献**
*   **新范式**：将文本和图形统一解析为结构化文本，保留跨元素语义关系。
*   **数据引擎**：构建多源数据（PDF/网页/SVG），训练 3B 紧凑模型。
*   **高性能**：文档解析开源领先，图形重建质量超越 Gemini 3 Pro。
*   **新监督**：将图形转化为代码级监督，解锁多模态预训练语料。

3. **技术要点**
*   采用统一文本表示法（含 SVG 代码）解析异构元素。
*   基于 PDF、网页和 SVG 资产构建综合数据引擎。
*   使用 3B 参数模型进行分阶段预训练和监督微调。
*   支持端到端训练， exploit 文本与视觉组件间的语义关系。

4. **潜在应用场景**
*   高保真文档数字化与重建
*   多模态检索增强生成（RAG）
*   UI 布局与设计稿还原
*   科学图表与化学结构图解析

---

## 2. Nyxus: A Next Generation Image Feature Extraction Library for the Big Data and AI Era

**作者**: Nicholas Schaub, Andriy Kharchenko, Hamdah Abbasi, Sameeul Samee, Hythem Sidky
**发布日期**: 2026-03-12
**arXiv ID**: [2603.12016v1](https://arxiv.org/abs/2603.12016v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.12016v1)
**分类**: cs.CV, q-bio.QM

### 论文摘要

Modern imaging instruments can produce terabytes to petabytes of data for a single experiment. The biggest barrier to processing big image datasets has been computational, where image analysis algorithms often lack the efficiency needed to process such large datasets or make tradeoffs in robustness and accuracy. Deep learning algorithms have vastly improved the accuracy of the first step in an analysis workflow (region segmentation), but the expansion of domain specific feature extraction librar...

### AI 总结

1. **一句话概述**
Nyxus 是面向大数据与 AI 的新一代图像特征提取库，支持 2D/3D 数据、多平台部署及高效可扩展计算。

2. **核心贡献**
*   **高效可扩展：** 支持 2D/3D 数据的核外（out-of-core）特征提取，兼容 CPU 与 GPU 加速。
*   **领域覆盖广：** 涵盖放射组学、细胞分析等多生物医学领域的综合特征集，并经严格测试。
*   **使用门槛低：** 提供 Python 包、命令行、Napari 插件及容器化等多种访问方式，适配不同技能用户。
*   **方法可调优：** 支持特征集程序化调优，可针对机器学习应用优化计算效率或特征覆盖率。

3. **技术要点**
*   核外计算架构（处理超出内存的数据）
*   CPU/GPU 并行加速
*   OCI 标准容器化部署
*   特征集程序化调优接口

4. **潜在应用场景**
*   大规模生物医学图像处理（TB 至 PB 级数据）
*   放射组学与细胞分析研究
*   云端或超级计算机工作流
*   机器学习与深度学习模型的特征工程

---

## 3. Deep Domain Decomposition Method for Solving the Variational Inequality Problems

**作者**: Yiyang Wang, Qijia Zhou, Shengyuan Deng, Chenliang Li
**发布日期**: 2026-03-12
**arXiv ID**: [2603.11552v1](https://arxiv.org/abs/2603.11552v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.11552v1)
**分类**: math.NA

### 论文摘要

By integrating physics-informed neural network (PINN) techniques with domain decomposition method, a deep domain decomposition method is presented for solving elliptic variational inequality problems. Based on the Ritz variation method, the elliptic variational inequality problem is firstly reformulated as an optimization problem, and then the subproblem in each subdomain is solved by using the Ritz-PINN method, which the parameters in the network are updated by the Adam optimizer, and the resid...

### AI 总结

1. **一句话概述**
本文结合 PINN 与域分解提出深度算法，求解椭圆变分不等式，实现高精度且迭代次数与网格无关。

2. **核心贡献**
*   提出融合 PINN 与域分解的深度方法，用于求解椭圆变分不等式问题。
*   基于 Ritz 变分法将原问题重构为优化问题，并利用 Ritz-PINN 求解子域。
*   引入残差自适应数据集更新策略，引导模型逐步学习复杂区域。
*   数值验证表明算法精度高（MSE 达 1e-7）且迭代次数与网格长度无关。

3. **技术要点**
*   **问题重构**：利用 Ritz 变分法将变分不等式转化为优化问题。
*   **子域求解**：在各子域内采用 Ritz-PINN 方法，参数由 Adam 优化器更新。
*   **自适应训练**：通过残差自适应策略动态更新训练数据集。
*   **域分解机制**：探索了重叠区域大小对算法性能的影响。

4. **潜在应用场景**
*   力学接触问题（如弹性体接触分析）。
*   金融数学（如美式期权定价模型）。
*   物理障碍问题及各类椭圆型偏微分方程约束优化问题。

---

## 4. WORKSWORLD: A Domain for Integrated Numeric Planning and Scheduling of Distributed Pipelined Workflows

**作者**: Taylor Paul, William Regli
**发布日期**: 2026-03-12
**arXiv ID**: [2603.12214v1](https://arxiv.org/abs/2603.12214v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.12214v1)
**分类**: cs.DC, cs.AI

### 论文摘要

This work pursues automated planning and scheduling of distributed data pipelines, or workflows. We develop a general workflow and resource graph representation that includes both data processing and sharing components with corresponding network interfaces for scheduling. Leveraging these graphs, we introduce WORKSWORLD, a new domain for numeric domain-independent planners designed for permanently scheduled workflows, like ingest pipelines. Our framework permits users to define data sources, ava...

### AI 总结

1. **一句话概述**
本文提出 WORKSWORLD 领域，实现分布式数据管道联合规划与调度，无需用户显式定义完整工作流。

2. **核心贡献**
- 提出 WORKSWORLD 新领域，专为数字独立规划器设计。
- 构建包含数据处理、共享及网络接口的通用图表示模型。
- 实现联合求解，同时生成工作流图并调度组件资源。
- 实证表明普通硬件可解决跨 8 站点的 14 组件线性工作流。

3. **技术要点**
- 基于数字独立规划器（Numeric Domain-Independent Planners）。
- 工作流与资源图的统一表示与建模。
- 规划（构建图）与调度（分配资源）的联合求解。
- 支持永久调度工作流（如摄入管道）。

4. **潜在应用场景**
- 分布式数据摄入管道（Ingest Pipelines）。
- 跨站点数据处理工作流。
- 自动化 ETL 流程构建。
- 云计算环境下的资源与工作流协同管理。

---

## 5. AS-Bridge: A Bidirectional Generative Framework Bridging Next-Generation Astronomical Surveys

**作者**: Dichang Zhang, Yixuan Shao, Simon Birrer, Dimitris Samaras
**发布日期**: 2026-03-12
**arXiv ID**: [2603.11928v1](https://arxiv.org/abs/2603.11928v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.11928v1)
**分类**: astro-ph.IM, cs.CV

### 论文摘要

The upcoming decade of observational cosmology will be shaped by large sky surveys, such as the ground-based LSST at the Vera C. Rubin Observatory and the space-based Euclid mission. While they promise an unprecedented view of the Universe across depth, resolution, and wavelength, their differences in observational modality, sky coverage, point-spread function, and scanning cadence make joint analysis beneficial, but also challenging. To facilitate joint analysis, we introduce A(stronomical)S(ur...

### AI 总结

1. **一句话概述**
本文提出 AS-Bridge 双向生成框架，利用扩散模型连接地面与空间天文观测，促进跨巡天联合分析与缺失预测。

2. **核心贡献**
*   提出首个连接 LSST（地面）与 Euclid（空间）观测的双向生成框架。
*   实现不同观测模态间的高保真图像翻译与转换。
*   支持缺失观测数据的概率预测及跨巡天稀有事件检测。
*   验证了跨巡天生成建模可行性，可增强未来数据管道的科学回报。

3. **技术要点**
*   **模型架构**：基于扩散模型（Diffusion Model）。
*   **核心过程**：采用随机布朗桥（Brownian Bridge）过程连接两种观测分布。
*   **建模方法**：利用重叠天区显式建模条件概率分布，实现双向转换。

4. **潜在应用场景**
*   单一巡天缺失观测数据的忠实预测。
*   跨巡天稀有天文事件协同检测。
*   未来 LSST-Euclid 联合数据处理管道组件。
*   多模态天文数据的协同分析与增强。

---

## 6. Evaluation of LLMs in retrieving food and nutritional context for RAG systems

**作者**: Maks Požarnik Vavken, Matevž Ogrinc, Tome Eftimov, Barbara Koroušić Seljak
**发布日期**: 2026-03-10
**arXiv ID**: [2603.09704v2](https://arxiv.org/abs/2603.09704v2)
**PDF**: [下载](https://arxiv.org/pdf/2603.09704v2)
**分类**: cs.CL

### 论文摘要

In this article, we evaluate four Large Language Models (LLMs) and their effectiveness at retrieving data within a specialized Retrieval-Augmented Generation (RAG) system, using a comprehensive food composition database. Our method is focused on the LLMs ability to translate natural language queries into structured metadata filters, enabling efficient retrieval via a Chroma vector database. By achieving high accuracy in this critical retrieval step, we demonstrate that LLMs can serve as an acces...

### AI 总结

1. **一句话概述**
本文评估四种大模型在食物营养 RAG 系统中的检索能力，证实其自然语言转换高效，但复杂约束处理仍具挑战。

2. **核心贡献**
*   评估了 4 种大模型在专业食物数据库 RAG 系统中的表现。
*   实现了自然语言查询到结构化元数据过滤的自动转换。
*   显著降低了领域专家使用复杂数据的技术门槛。
*   揭示了模型在处理不可表达约束时的检索局限性。

3. **技术要点**
基于 RAG 架构，利用大模型将自然语言查询转化为结构化元数据过滤条件，结合 Chroma 向量数据库实现高效检索。

4. **潜在应用场景**
*   营养学家与食品编译者快速检索专业成分数据。
*   健康咨询系统提供基于准确营养信息的回答。
*   食品数据库的自然语言交互界面开发。

---

## 7. Fusing Semantic, Lexical, and Domain Perspectives for Recipe Similarity Estimation

**作者**: Denica Kjorvezir, Danilo Najkov, Eva Valencič, Erika Jesenko, Barbara Koroišić Seljak
**发布日期**: 2026-03-10
**arXiv ID**: [2603.09688v2](https://arxiv.org/abs/2603.09688v2)
**PDF**: [下载](https://arxiv.org/pdf/2603.09688v2)
**分类**: cs.CL

### 论文摘要

This research focuses on developing advanced methods for assessing similarity between recipes by combining different sources of information and analytical approaches. We explore the semantic, lexical, and domain similarity of food recipes, evaluated through the analysis of ingredients, preparation methods, and nutritional attributes. A web-based interface was developed to allow domain experts to validate the combined similarity results. After evaluating 318 recipe pairs, experts agreed on 255 (8...

### AI 总结

1. **一句话概述**
本研究融合语义、词汇及领域信息评估食谱相似度，经专家验证有效，并分析了各维度影响力。

2. **核心贡献**
- 构建多视角融合的食谱相似度评估模型。
- 开发 Web 界面供领域专家验证相似度结果。
- 实现 80% 的专家评估一致性，验证方法可靠性。
- 量化分析不同维度对专家决策的影响程度。

3. **技术要点**
- **分析维度**：涵盖食材、制作方法及营养属性。
- **融合策略**：结合语义、词汇与领域特定知识。
- **验证方式**：基于 Web 接口进行领域专家人工评估。

4. **潜在应用场景**
- 食品工业优化。
- 个性化饮食与营养推荐。
- 自动化食谱生成系统。

---

## 8. A New Modeling to Feature Selection Based on the Fuzzy Rough Set Theory in Normal and Optimistic States on Hybrid Information Systems

**作者**: Mohammad Hossein Safarpour, Seyed Majid Alavi, Mohammad Izadikhah, Hossein Dibachi
**发布日期**: 2026-03-09
**arXiv ID**: [2603.08900v2](https://arxiv.org/abs/2603.08900v2)
**PDF**: [下载](https://arxiv.org/pdf/2603.08900v2)
**分类**: cs.LG, cs.AI

### 论文摘要

Considering the high volume, wide variety, and rapid speed of data generation, investigating feature selection methods for big data presents various applications and advantages. By removing irrelevant and redundant features, feature selection reduces data dimensions, thereby facilitating optimal decision-making within decision systems. One of the key tools for feature selection in hybrid information systems is fuzzy rough set theory. However, this theory faces two significant challenges: First, ...

### AI 总结

1. **一句话概述**
本文提出 FSbuHD 模型，利用模糊粗糙集理论将特征选择转化为优化问题，有效解决高维数据效率与噪声挑战。

2. **核心贡献**
*   克服了传统模糊粗糙集在高维空间计算耗时、内存占用大及产生噪声的缺陷。
*   提出通过计算对象间组合距离来推导模糊等价关系的新方法。
*   将特征选择问题重构为优化问题，可利用元启发式算法求解。
*   设计了正常和乐观两种运行模式，增强了模型的适应性。
*   在 UCI 数据集上的实验表明，该方法比现有算法更高效且有效。

3. **技术要点**
*   基于模糊粗糙集理论（Fuzzy Rough Set Theory）。
*   基于对象组合距离计算推导模糊等价关系。
*   特征选择建模为优化问题。
*   采用元启发式算法进行求解。
*   支持正常（Normal）和乐观（Optimistic）两种状态模式。

4. **潜在应用场景**
*   大数据预处理与降维。
*   混合信息系统中的决策支持。
*   高维数据的特征提取与分析。
*   需要高效特征选择的机器学习任务。

---

## 9. Automatic End-to-End Data Integration using Large Language Models

**作者**: Aaron Steiner, Christian Bizer
**发布日期**: 2026-03-11
**arXiv ID**: [2603.10547v1](https://arxiv.org/abs/2603.10547v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.10547v1)
**分类**: cs.CL

### 论文摘要

Designing data integration pipelines typically requires substantial manual effort from data engineers to configure pipeline components and label training data. While LLMs have shown promise in handling individual steps of the integration process, their potential to replace all human input across end-to-end data integration pipelines has not been investigated. As a step toward exploring this potential, we present an automatic data integration pipeline that uses GPT-5.2 to generate all artifacts r...

### AI 总结

1. **一句话概述**
该研究利用大语言模型实现全自动端到端数据集成，自动生成配置内容，成本远低于人工且效果相当。

2. **核心贡献**
*   提出基于 LLM 的全自动端到端数据集成方案，无需人工干预配置管道。
*   实现 schema 映射、值标准化、实体匹配及冲突解决数据的全自动生成。
*   实验表明其集成效果媲美或优于人工管道，数据集规模与密度相当。
*   显著降低成本，单案例配置费用仅约 10 美元，远低于人工成本。

3. **技术要点**
*   **核心模型**：使用 GPT-5.2 生成管道适配所需的所有工件。
*   **关键生成物**：包括 schema 映射、值映射、实体匹配训练数据、冲突解决验证数据。
*   **评估方法**：通过视频游戏、音乐和公司数据三个案例，对比人工与 LLM 管道的性能及产出质量。

4. **潜在应用场景**
*   多领域多源数据融合项目（如游戏、音乐、企业信息系统）。
*   预算有限或需要快速部署的数据集成任务。
*   旨在减少数据工程师手动配置和标注工作量的自动化流程。

---

## 10. Effective Dataset Distillation for Spatio-Temporal Forecasting with Bi-dimensional Compression

**作者**: Taehyung Kwon, Yeonje Choi, Yeongho Kim, Kijung Shin
**发布日期**: 2026-03-11
**arXiv ID**: [2603.10410v1](https://arxiv.org/abs/2603.10410v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.10410v1)
**分类**: cs.LG, cs.AI, cs.DB

### 论文摘要

Spatio-temporal time series are widely used in real-world applications, including traffic prediction and weather forecasting. They are sequences of observations over extensive periods and multiple locations, naturally represented as multidimensional data. Forecasting is a central task in spatio-temporal analysis, and numerous deep learning methods have been developed to address it. However, as dataset sizes and model complexities continue to grow in practice, training deep learning models has be...

### AI 总结

1. **一句话概述**
本文提出首个时空预测数据集蒸馏方法 STemDist，通过时空双向压缩实现更快、更省内存且更有效的模型训练。

2. **核心贡献**
*   提出首个专为时空预测设计的数据集蒸馏方法 STemDist。
*   实现时空双维度平衡压缩，解决现有方法仅压缩单维度的局限。
*   结合集群级与子集粒度蒸馏，有效平衡蒸馏成本与预测性能。
*   实证显示训练提速 6 倍、内存节省 8 倍、预测误差降低 12%。

3. **技术要点**
*   **双向压缩机制**：同时压缩时间与空间维度以减少数据量。
*   **集群级蒸馏**：在聚类层面进行蒸馏，降低计算开销。
*   **子集粒度蒸馏**：辅以细粒度子集蒸馏，增强模型 forecasting 能力。

4. **潜在应用场景**
*   交通流量与速度预测。
*   气象与天气预报建模。
*   其他资源受限的大规模时空序列分析任务。

---

## 11. Thousand-GPU Large-Scale Training and Optimization Recipe for AI-Native Cloud Embodied Intelligence Infrastructure

**作者**: Chen Zhou, Haoran Sun, Hedan Yang, Jing Long, Junwu Xiong
**发布日期**: 2026-03-11
**arXiv ID**: [2603.11101v1](https://arxiv.org/abs/2603.11101v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.11101v1)
**分类**: cs.RO, cs.AI, cs.DC

### 论文摘要

Embodied intelligence is a key step towards Artificial General Intelligence (AGI), yet its development faces multiple challenges including data, frameworks, infrastructure, and evaluation systems. To address these issues, we have, for the first time in the industry, launched a cloud-based, thousand-GPU distributed training platform for embodied intelligence, built upon the widely adopted LeRobot framework, and have systematically overcome bottlenecks across the entire pipeline. At the data layer...

### AI 总结

1. **一句话概述**
本文首创千 GPU 云原生具身智能训练平台，通过全链路优化实现 40 倍训练加速，为下一代自主机器人奠定技术基础。

2. **核心贡献**
*   **平台首创**：行业首发基于 LeRobot 框架的千 GPU 云原生具身智能分布式训练平台。
*   **效率突破**：GR00T-N1.5 模型单轮训练时间从 15 小时降至 22 分钟，速度提升 40 倍。
*   **全链路优化**：系统性解决数据、模型、基础设施及评估系统的瓶颈问题。
*   **闭环评估**：构建端到端评估系统，实现从训练、仿真到评估的完整闭环。

3. **技术要点**
*   **模型层**：变长 FlashAttention、Data Packing、π-0.5 注意力优化、FP8 量化。
*   **数据层**：重构数据流水线，优化具身训练数据流。
*   **基础设施**：3.2T RDMA 网络、高性能存储、Ray 驱动弹性 AI 数据湖。
*   **系统协同**：实现数据、存储、通信与计算的深度协同。

4. **潜在应用场景**
*   下一代自主智能机器人的开发与训练。
*   大规模具身智能模型的云端部署与迭代。
*   人机融合时代的智能基础设施构建。
*   具身智能算法的快速仿真与性能评估。

---

## 12. Fish Audio S2 Technical Report

**作者**: Shijia Liao, Yuxuan Wang, Songting Liu, Yifan Cheng, Ruoyi Zhang
**发布日期**: 2026-03-09
**arXiv ID**: [2603.08823v2](https://arxiv.org/abs/2603.08823v2)
**PDF**: [下载](https://arxiv.org/pdf/2603.08823v2)
**分类**: cs.SD, cs.AI, cs.CL

### 论文摘要

We introduce Fish Audio S2, an open-sourced text-to-speech system featuring multi-speaker, multi-turn generation, and, most importantly, instruction-following control via natural-language descriptions. To scale training, we develop a multi-stage training recipe together with a staged data pipeline covering video captioning and speech captioning, voice-quality assessment, and reward modeling. To push the frontier of open-source TTS, we release our model weights, fine-tuning code, and an SGLang-ba...

### AI 总结

1. **一句话概述**
Fish Audio S2 是支持自然语言指令控制、多说话人的开源 TTS 系统，具备低延迟流式推理能力。

2. **核心贡献**
- 实现基于自然语言描述的指令跟随控制。
- 提出涵盖数据清洗与奖励建模的多阶段训练方案。
- 开源模型权重、微调代码及生产级推理引擎。
- 达成低于 100ms 的首音频延迟与高效流式输出。

3. **技术要点**
- **训练策略**：多阶段训练配方，包含视频/语音 captioning、质量评估及奖励建模。
- **推理引擎**：基于 SGLang 开发，支持流式传输，RTF 达 0.195。
- **功能特性**：支持多说话人、多轮生成及精细指令控制。

4. **潜在应用场景**
- 个性化语音定制与克隆。
- 交互式语音助手与对话系统。
- 实时音频内容生成与直播。
- 需要精细控制语音情感或风格的场景。

---

## 13. Measuring onion website discovery and Tor users' interests with honeypots

**作者**: Arttu Paju, Waris Abdullah, Juha Nurmi
**发布日期**: 2026-03-10
**arXiv ID**: [2603.09329v1](https://arxiv.org/abs/2603.09329v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.09329v1)
**分类**: cs.CR

### 论文摘要

Tor enables anonymous web browsing and access to anonymous onion websites. Prior work has focused on crawling and content analysis rather than on what users actually try to access. Our honeypot approach measures engagement across onion-site categories, revealing behavioral interest rather than inferred popularity. In March--April 2025, we deployed honeypot onion websites and seeded neutral-looking links via three channels -- the Ahmia Tor search engine, Stronghold paste onion "paste" service, an...

### AI 总结

1. **一句话概述**
本研究利用蜜罐测量 Tor 用户行为，发现 Ahmia 是主要访问来源，且用户对 CSAM 主题网站的互动率显著最高。

2. **核心贡献**
*   提出基于蜜罐的方法，直接测量用户实际访问意图而非仅分析现有内容。
*   证实 Ahmia 搜索引擎是 Tor 用户发现洋葱网站的核心渠道。
*   揭示用户对儿童性虐待材料（CSAM）主题的兴趣显著高于其他犯罪类别。
*   发现英语版本的洋葱网站相比多语言版本更易引发用户交互。

3. **技术要点**
*   部署代表不同犯罪类别（如毒品、武器、CSAM 等）的蜜罐洋葱网站。
*   通过三个渠道（Ahmia、Stronghold、pastebin）植入链接以追踪流量来源。
*   以 CAPTCHA 求解和注册/登录尝试作为量化用户交互的关键指标。

4. **潜在应用场景**
*   暗网威胁情报收集与用户行为趋势分析。
*   执法部门针对高热度犯罪领域的调查资源分配。
*   匿名网络搜索引擎的内容过滤策略优化。

---

## 14. Nezha: A Key-Value Separated Distributed Store with Optimized Raft Integration

**作者**: Yangyang Wang, Yucong Dong, Ziqian Cheng, Zichen Xu
**发布日期**: 2026-03-10
**arXiv ID**: [2603.09122v1](https://arxiv.org/abs/2603.09122v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.09122v1)
**分类**: cs.DC, cs.DB

### 论文摘要

Distributed key-value stores are widely adopted to support elastic big data applications, leveraging purpose-built consensus algorithms like Raft to ensure data consistency. However, through systematic analysis, we reveal a critical performance issue in such consistent stores, i.e., overlapping persistence operations between consensus protocols and underlying storage engines result in significant I/O overhead. To address this issue, we present Nezha, a prototype distributed storage system that i...

### AI 总结

1. **一句话概述**
本文提出 Nezha 系统，结合键值分离与优化 Raft 集成，解决持久化 I/O 重叠瓶颈，显著提升吞吐性能。

2. **核心贡献**
*   揭示了基于 Raft 的一致性存储中，共识协议与存储引擎持久化操作重叠导致的 I/O 开销问题。
*   设计了 Nezha 原型系统，创新性地将键值分离架构与 Raft 协议集成。
*   重构了操作级别的持久化策略，并引入分层垃圾回收机制以优化性能。
*   在保证 Raft 安全属性的前提下，大幅提升了写、读及扫描操作的吞吐量。

3. **技术要点**
*   **键值分离架构**：优化数据存储布局。
*   **Raft 优化集成**：减少共识与存储间的冗余操作。
*   **操作级持久化重构**：降低 I/O 重叠开销。
*   **分层垃圾回收**：高效管理存储碎片。

4. **潜在应用场景**
*   需要强一致性保证的弹性大数据应用。
*   高吞吐需求的分布式键值存储系统。
*   对读写性能敏感的云端存储服务。

---

## 15. Stepping VLMs onto the Court: Benchmarking Spatial Intelligence in Sports

**作者**: Yuchen Yang, Yuqing Shao, Duxiu Huang, Linfeng Dong, Yifei Liu
**发布日期**: 2026-03-10
**arXiv ID**: [2603.09896v1](https://arxiv.org/abs/2603.09896v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.09896v1)
**分类**: cs.CV

### 论文摘要

Sports have long attracted broad attention as they push the limits of human physical and cognitive capabilities. Amid growing interest in spatial intelligence for vision-language models (VLMs), sports provide a natural testbed for understanding high-intensity human motion and dynamic object interactions. To this end, we present CourtSI, the first large-scale spatial intelligence dataset tailored to sports scenarios. CourtSI contains over 1M QA pairs, organized under a holistic taxonomy that syst...

### AI 总结

1. **一句话概述**
本文提出首个体育空间智能数据集 CourtSI 及基准，揭示 VLM 不足，微调后显著提升模型空间智能。

2. **核心贡献**
*   构建首个体育场景大规模空间智能数据集 CourtSI，含超 100 万 QA 对。
*   提出高质量评估基准 CourtSI-Bench，涵盖计数、测距、定位等任务。
*   评估 25 个 VLM 模型，揭示现有基准泛化性不足及显著的人机性能差距。
*   微调模型在基准上准确率提升 23.5%，并能有效泛化至未见体育项目。

3. **技术要点**
*   利用球场几何结构作为度量锚点，确保空间数据准确性。
*   开发半自动数据引擎重建体育场景，实现数据规模化 curated。
*   建立涵盖计数、测距、定位及关系推理的系统化任务分类体系。

4. **潜在应用场景**
*   智能体育赛事解说生成。
*   辅助裁判判罚与规则验证。
*   运动员训练动作与战术分析。
*   提升通用 VLM 在动态场景下的空间智能。

---

## 16. MAcPNN: Mutual Assisted Learning on Data Streams with Temporal Dependence

**作者**: Federico Giannini, Emanuele Della Valle
**发布日期**: 2026-03-09
**arXiv ID**: [2603.08972v1](https://arxiv.org/abs/2603.08972v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.08972v1)
**分类**: cs.LG

### 论文摘要

Internet of Things (IoT) Analytics often involves applying machine learning (ML) models on data streams. In such scenarios, traditional ML paradigms face obstacles related to continuous learning while dealing with concept drifts, temporal dependence, and avoiding forgetting. Moreover, in IoT, different edge devices build up a network. When learning models on those devices, connecting them could be useful in improving performance and reusing others' knowledge. This work proposes Mutual Assisted L...

### AI 总结

1. **一句话概述**
该文提出 MAcPNN 框架，基于维果茨基理论实现设备互助学习，有效处理 IoT 数据流漂移并减少通信开销。

2. **核心贡献**
*   提出无需中央协调的互助学习范式，设备具备自主决策能力。
*   设计按需通信机制，仅在性能下降时求助，大幅减少网络连接。
*   结合连续渐进神经网络（cPNN），有效处理时间依赖与灾难性遗忘。
*   引入量化技术降低内存占用，使模型更适配资源受限的边缘设备。

3. **技术要点**
*   **互助触发机制**：基于性能退化检测概念漂移并触发求助。
*   **cPNN 架构**：支持单数据点预测，适应动态数据流。
*   **知识效用评估**：设备自主判断他人知识是否有助于解决新问题。
*   **模型量化**：压缩内存 footprint，优化边缘部署。

4. **潜在应用场景**
*   物联网（IoT）边缘设备协同分析。
*   存在概念漂移的实时传感器数据监控。
*   带宽或计算资源受限的分布式学习网络。

---

## 17. Don't Look Back in Anger: MAGIC Net for Streaming Continual Learning with Temporal Dependence

**作者**: Federico Giannini, Sandro D'Andrea, Emanuele Della Valle
**发布日期**: 2026-03-09
**arXiv ID**: [2603.08600v1](https://arxiv.org/abs/2603.08600v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.08600v1)
**分类**: cs.LG, cs.AI

### 论文摘要

Concept drift, temporal dependence, and catastrophic forgetting represent major challenges when learning from data streams. While Streaming Machine Learning and Continual Learning (CL) address these issues separately, recent efforts in Streaming Continual Learning (SCL) aim to unify them. In this work, we introduce MAGIC Net, a novel SCL approach that integrates CL-inspired architectural strategies with recurrent neural networks to tame temporal dependence. MAGIC Net continuously learns, looks b...

### AI 总结

1. **一句话概述**
本文提出 MAGIC Net，融合持续学习策略与 RNN，实现在线流式学习并缓解概念漂移与遗忘问题。

2. **核心贡献**
*   统一流式机器学习与持续学习框架，应对数据流三大挑战。
*   引入 RNN 捕捉时间依赖性，增强对动态概念的适应能力。
*   利用可学习掩码回顾过往知识，必要时动态扩展架构。
*   全在线操作模式，限制内存使用且保证推理实时可用。

3. **技术要点**
*   **架构融合**：集成持续学习架构策略与循环神经网络（RNN）。
*   **知识回顾**：通过可学习掩码作用于冻结权重，复用历史知识。
*   **动态扩展**：根据数据流需求动态扩展网络架构。
*   **在线流程**：所有学习与推理操作均在线进行，无需离线批次。

4. **潜在应用场景**
*   金融时间序列预测（如股票趋势分析）。
*   物联网传感器数据流实时监控。
*   用户行为实时追踪与个性化推荐。
*   动态环境下的在线异常检测系统。

---

## 18. Query-Guided Analysis and Mitigation of Data Verification Errors (Extended Version)

**作者**: Ran Schreiber, Yael Amsterdamer
**发布日期**: 2026-03-09
**arXiv ID**: [2603.08612v1](https://arxiv.org/abs/2603.08612v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.08612v1)
**分类**: cs.DB

### 论文摘要

Data verification, the process of labeling data items as correct or incorrect, is a preprocessing step that may critically affect the quality of results in data-driven pipelines. Despite recent advances, verification can still produce erroneous labels that propagate to downstream query results in complex ways. We present a framework that complements existing verification tools by assessing the impact of potential labeling errors on query outputs and guiding additional verification steps to impro...

### AI 总结

1. **一句话概述**
本文提出一种框架，通过量化验证错误对查询结果的影响，指导额外验证步骤以显著提升数据流程的结果可靠性。

2. **核心贡献**
*   提出互补现有工具的框架，评估标签错误对下游查询结果的传播影响。
*   引入最大错误分数（MES），作为独立于数据分布的最坏情况不确定性指标。
*   定义“风险元组”，识别减少标签不确定性反而可能增加输出不确定性的特殊情况。
*   开发 MESReduce 算法，交互外部验证器以选择最优的额外验证步骤，降低误差。

3. **技术要点**
*   **MES 度量**：量化查询输出元组的可靠性上限。
*   **风险检测**：高效算法识别反直觉的风险输入元组。
*   **迭代优化**：基于 MES 和风险指标动态选择验证目标。

4. **潜在应用场景**
*   数据清洗与预处理管道。
*   数据质量管理系统。
*   对查询结果可靠性要求高的分析系统。
*   众包数据标注或人工验证辅助系统。

---

## 19. PRIME: Efficient Algorithm for Token Graph Routing Problem

**作者**: Haotian Xu, Yuqing Zhu, Yuming Huang, Jing Tang
**发布日期**: 2026-03-09
**arXiv ID**: [2603.08337v1](https://arxiv.org/abs/2603.08337v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.08337v1)
**分类**: cs.DB

### 论文摘要

Optimizing asset exchanges on blockchain-driven platforms poses a novel and challenging graph query optimization problem. In this model, assets represent vertices and exchanges form edges, recasting the graph query task as a routing problem over a large-scale, dynamic graph. However, the existing solutions fail to solve the problem efficiently due to the non-linear nature of the edge weights defined by a concave swap function. To address the challenge, we propose PRIME, a two-stage iterative gra...

### AI 总结

1. **一句话概述**
本文提出 PRIME 算法，通过两阶段迭代优化区块链代币图路由，显著提升交易价格并降低计算成本。

2. **核心贡献**
*   提出 PRIME 算法解决非线性的代币图路由问题（TGRP）。
*   设计两阶段框架：剪枝搜索路径结合凸优化分配。
*   发明自适应符号梯度法（ASGM），实现线性收敛。
*   实测优于 Uniswap，交易价格更高且计算量大幅减少。
*   已在对冲基金生产环境部署，验证了可扩展性。

3. **技术要点**
*   **问题建模**：将资产交换建模为带凹交换函数的动态图路由。
*   **路径搜索**：采用剪枝图搜索高效识别高潜力路径。
*   **优化 formulation**：将分配任务转化为强凸优化问题。
*   **求解算法**：使用 ASGM 算法求解，保证高效收敛。

4. **潜在应用场景**
*   去中心化金融（DeFi）平台的交易路由优化。
*   高频去中心化市场的资产交换执行。
*   对冲基金及机构的链上大额交易策略。
*   大规模动态图查询处理系统。

---

## 20. Seed2Scale: A Self-Evolving Data Engine for Embodied AI via Small to Large Model Synergy and Multimodal Evaluation

**作者**: Cong Tai, Zhaoyu Zheng, Haixu Long, Hansheng Wu, Zhengbin Long
**发布日期**: 2026-03-09
**arXiv ID**: [2603.08260v1](https://arxiv.org/abs/2603.08260v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.08260v1)
**分类**: cs.RO

### 论文摘要

Existing data generation methods suffer from exploration limits, embodiment gaps, and low signal-to-noise ratios, leading to performance degradation during self-iteration. To address these challenges, we propose Seed2Scale, a self-evolving data engine that overcomes the data bottleneck through a heterogeneous synergy of "small-model collection, large-model evaluation, and target-model learning". Starting with as few as four seed demonstrations, the engine employs the lightweight Vision-Language-...

### AI 总结

1. **一句话概述**
Seed2Scale 是一个自进化数据引擎，利用大小模型协同与多模态评估，解决具身 AI 数据生成瓶颈并显著提升性能。

2. **核心贡献**
*   提出 Seed2Scale 引擎，突破具身 AI 数据生成中的探索限制与高噪声问题。
*   设计“小模型收集、大模型评估、目标模型学习”的异构协同架构。
*   仅需 4 个种子演示即可启动，有效防止自迭代过程中的模型崩溃。
*   目标模型成功率提升 131.2%，性能显著优于现有数据增强方法。

3. **技术要点**
*   **收集端：** 使用轻量级 VLA 模型 SuperTiny 作为收集器，凭借强归纳偏置实现并行环境下的鲁棒探索。
*   **评估端：** 集成预训练 VLM 作为验证器，自动对生成轨迹进行成败判断与质量打分。
*   **进化机制：** 通过筛选高质量轨迹驱动目标模型学习，确保自进化过程的稳定性与扩展性。

4. **潜在应用场景**
*   通用具身智能体（Generalist Embodied AI）的大规模开发。
*   机器人技能学习的低成本数据增强与自动化训练。
*   少样本（Few-shot）场景下的模型自进化与性能提升。

---

## 21. Fusion-Poly: A Polyhedral Framework Based on Spatial-Temporal Fusion for 3D Multi-Object Tracking

**作者**: Xian Wu, Yitao Wu, Xiaoyu Li, Zijia Li, Lijun Zhao
**发布日期**: 2026-03-09
**arXiv ID**: [2603.08199v1](https://arxiv.org/abs/2603.08199v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.08199v1)
**分类**: cs.CV, cs.RO

### 论文摘要

LiDAR-camera 3D multi-object tracking (MOT) combines rich visual semantics with accurate depth cues to improve trajectory consistency and tracking reliability. In practice, however, LiDAR and cameras operate at different sampling rates. To maintain temporal alignment, existing data pipelines usually synchronize heterogeneous sensor streams and annotate them at a reduced shared frequency, forcing most prior methods to perform spatial fusion only at synchronized timestamps through projection-based...

### AI 总结

1. **一句话概述**
本文提出 Fusion-Poly 框架，融合异步 LiDAR 与相机数据实现高频跟踪，在 nuScenes 上刷新 3D MOT 性能纪录。

2. **核心贡献**
*   突破传统同步融合限制，有效利用异步多模态观测数据。
*   提出频率感知模块，支持高频运动状态更新与轨迹维持。
*   设计观测对齐模块，优化同步时刻的跨模态一致性。
*   在 nuScenes 测试集取得 76.5% AMOTA，确立追踪检测新方法 SOTA。

3. **技术要点**
*   **时空融合架构**：结合同步时刻的多模态关联与异步时刻的单模态观测。
*   **频率感知级联匹配**：根据帧类型（同步/异步）自适应调整匹配策略。
*   **高频轨迹估计**：通过运动预测、差分更新及置信度生命周期管理维持轨迹。
*   **全状态观测对齐**：在同步时刻最小化图像投影误差以提升一致性。

4. **潜在应用场景**
*   自动驾驶环境感知系统。
*   机器人多传感器融合导航。
*   复杂动态场景的智能监控。

---

## 22. TS-MLLM: A Multi-Modal Large Language Model-based Framework for Industrial Time-Series Big Data Analysis

**作者**: Haiteng Wang, Yikang Li, Yunfei Zhu, Jingheng Yan, Lei Ren
**发布日期**: 2026-03-08
**arXiv ID**: [2603.07572v1](https://arxiv.org/abs/2603.07572v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.07572v1)
**分类**: cs.LG

### 论文摘要

Accurate analysis of industrial time-series big data is critical for the Prognostics and Health Management (PHM) of industrial equipment. While recent advancements in Large Language Models (LLMs) have shown promise in time-series analysis, existing methods typically focus on single-modality adaptations, failing to exploit the complementary nature of temporal signals, frequency-domain visual representations, and textual knowledge information. In this paper, we propose TS-MLLM, a unified multi-mod...

### AI 总结

1. **一句话概述**
提出 TS-MLLM 框架，融合时序、频域及文本信息，显著提升工业时序分析性能与泛化能力。

2. **核心贡献**
*   提出 TS-MLLM 统一框架，联合建模时序信号、频域图像及文本知识。
*   设计时序 Patch 建模分支，有效捕捉长程时序动态特征。
*   引入 SVLMA 机制，使模型内化频域模式与语义上下文先验。
*   提出 TMAF 机制，以时序特征为查询实现深度跨模态对齐。
*   在少样本及复杂场景下优于 SOTA，验证了框架的鲁棒性与效率。

3. **技术要点**
*   **多模态输入**：整合时序信号、频域可视化图像及领域文本知识。
*   **时序 Patch 建模**：专门分支处理工业时间序列的长距离依赖。
*   **SVLMA 机制**：频谱感知视觉 - 语言模型适配，融合频域与语义信息。
*   **TMAF 机制**：时序中心多模态注意力融合，主动检索视觉和文本线索。

4. **潜在应用场景**
*   工业设备预测与健康管理（PHM）。
*   复杂工况下的故障诊断与寿命预测。
*   少样本条件下的工业时序数据分析和异常检测。

---

## 23. Novel Table Search [Technical Report]

**作者**: Besat Kassaie, Renée J. Miller
**发布日期**: 2026-03-07
**arXiv ID**: [2603.07235v1](https://arxiv.org/abs/2603.07235v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.07235v1)
**分类**: cs.DB

### 论文摘要

Avoiding redundancy in query results has been extensively studied in relational databases and information retrieval, yet its implications for data lakes remain largely unexplored. We bridge this gap by investigating how to discover unionable tables that contribute new information for a given query table in large-scale data lakes. We formally define Novel Table Search (NTS) as the problem of finding tables that are novel with respect to a given query table and identify two desirable properties th...

### AI 总结

1. **一句话概述**
本文针对数据湖查询冗余问题，提出新颖表搜索任务及高效近似算法 ANTs，旨在发现能提供新信息的表。

2. **核心贡献**
*   形式化定义新颖表搜索（NTS）问题及评分函数应具备的属性。
*   提出句法新颖性评分机制，并证明其优化问题为 NP 难。
*   开发基于惩罚机制的高效近似算法 ANTs 以解决计算挑战。
*   提出新颖性评估指标及变体，实验验证 ANTs 性能最优。

3. **技术要点**
*   **句法新颖性建模**：定义表之间基于属性的信息新颖度。
*   **近似优化技术**：采用基于惩罚的策略处理 NP 难优化问题。
*   **属性级搜索**：基于属性匹配实现高效的表发现与评分。

4. **潜在应用场景**
*   大规模数据湖中的表发现与探索。
*   避免信息冗余的数据查询与检索系统。
*   需要补充新维度的数据集成与增强任务。

---

## 24. AutoResearch-RL: Perpetual Self-Evaluating Reinforcement Learning Agents for Autonomous Neural Architecture Discovery

**作者**: Nilesh Jain, Rohit Yadav, Sagar Kotian, Claude AI
**发布日期**: 2026-03-07
**arXiv ID**: [2603.07300v1](https://arxiv.org/abs/2603.07300v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.07300v1)
**分类**: cs.LG

### 论文摘要

We present AutoResearch-RL, a framework in which a reinforcement learning agent conducts open-ended neural architecture and hyperparameter research without human supervision, running perpetually until a termination oracle signals convergence or resource exhaustion. At each step the agent proposes a code modification to a target training script, executes it under a fixed wall clock time budget, observes a scalar reward derived from validation bits-per-byte (val-bpb), and updates its policy via Pr...

### AI 总结

1. **一句话概述**
AutoResearch-RL 是一种无需人工监督的强化学习框架，能自主持续优化神经架构与超参数，直至收敛或资源耗尽。

2. **核心贡献**
*   实现无监督永久自评估，代理自主进行架构与超参数研究。
*   分离冻结环境、可变代码与元学习器，确保公平性与状态可编辑。
*   形式化为马尔可夫决策过程，并在温和假设下推导收敛保证。
*   单 GPU 实证显示，300 次迭代后性能媲美或超越人工调优基线。

3. **技术要点**
*   **算法策略**：使用近端策略优化（PPO）更新代理策略。
*   **奖励信号**：基于验证集 bits-per-byte (val-bpb) 的标量奖励。
*   **执行机制**：代理直接修改训练脚本（train.py），在固定时间预算内执行。
*   **终止条件**：引入终止预言机，根据收敛性或资源耗尽信号停止运行。

4. **潜在应用场景**
*   自动化神经网络架构搜索（NAS）与超参数优化。
*   资源受限环境下的自主模型预训练与调优。
*   无需人工干预的持续机器学习系统研发。
*   自动化代码级算法改进与实验探索。

---

## 25. Seeing the Context: Rich Visual Context-Aware Speech Recognition via Multimodal Reasoning

**作者**: Wenjie Tian, Mingchen Shao, Bingshen Mu, Xuelong Geng, Chengyou Wang
**发布日期**: 2026-03-07
**arXiv ID**: [2603.07263v1](https://arxiv.org/abs/2603.07263v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.07263v1)
**分类**: cs.SD, eess.AS

### 论文摘要

Audio-visual speech recognition (AVSR) is an extension of ASR that incorporates visual signals. Current AVSR approaches primarily focus on lip motion, largely overlooking rich context present in the video such as speaking scene and on-screen text. To tackle such CAVSR (AVSR including rich visual Context), we propose VASR designed to "see" and reason the visual context to improve speech recognition. Specifically, we construct an Audio-Visual Chain-of-Thought (AV-CoT) that explicitly enforces inte...

### AI 总结

1. **一句话概述**
本文提出 VASR 模型，通过音视频思维链利用丰富视觉上下文提升语音识别，解决单模态主导问题并开源数据集。

2. **核心贡献**
*   提出 VASR 框架，专注于利用场景、屏幕文字等丰富视觉上下文的语音识别任务。
*   设计音视频思维链（AV-CoT），实现声学信号与视觉证据的显式跨模态对齐。
*   缓解“单模态主导”问题，避免模型过度依赖或忽略视觉上下文。
*   构建并发布专用数据流水线及测试集，填补该领域数据稀缺空白。

3. **技术要点**
*   **音视频思维链（AV-CoT）：** 强制模型进行中间跨模态推理，增强模态间 grounding。
*   **证据驱动推理：** 利用视觉证据辅助声学信号，平衡多模态信息权重。
*   **上下文感知：** 不仅关注唇动，还整合场景背景和屏幕文本等视觉信息。

4. **潜在应用场景**
*   复杂视觉场景下的视频自动字幕生成。
*   嘈杂环境中的会议记录与语音转录。
*   包含屏幕文字的教学视频或演示内容分析。
*   多模态智能助手与听障人士辅助工具。

---

## 26. Single-pass Possibilistic Clustering with Damped Window Footprints

**作者**: Jeffrey Dale, James Keller, Aquila Galusha
**发布日期**: 2026-03-06
**arXiv ID**: [2603.06889v1](https://arxiv.org/abs/2603.06889v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.06889v1)
**分类**: cs.LG

### 论文摘要

Streaming clustering is a domain that has become extremely relevant in the age of big data, such as in network traffic analysis or in processing continuously-running sensor data. Furthermore, possibilistic models offer unique benefits over approaches from the literature, especially with the introduction of a "fuzzifier" parameter that controls how quickly typicality degrades as one gets further from cluster centers. We propose a single-pass possibilistic clustering (SPC) algorithm that is effect...

### AI 总结

1. **一句话概述**
本文提出基于阻尼窗口足迹的单遍可能性聚类算法 SPC，适用于流数据且支持非球形簇建模。

2. **核心贡献**
- 提出单遍可能性聚类（SPC）算法，有效且易于应用。
- 具备建模非球形簇结构的能力，突破球形假设限制。
- 实现任意大小阻尼窗口的封闭式足迹更新。
- 引入协方差并集方法合并簇均值与协方差估计。
- 在聚类纯度和归一化互信息指标上优于五种对比算法。

3. **技术要点**
- **可能性模型**：利用模糊化参数控制典型性随距离衰减的速度。
- **单遍处理**：适用于流式数据，无需多次迭代。
- **阻尼窗口**：支持基于时间衰减的窗口足迹计算。
- **簇合并策略**：借用多假设跟踪文献中的协方差并集技术。

4. **潜在应用场景**
- 网络流量分析。
- 连续运行的传感器数据处理。
- 其他需要实时处理的大数据流式聚类场景。

---

## 27. A Hazard-Informed Data Pipeline for Robotics Physical Safety

**作者**: Alexei Odinokov, Rostislav Yavorskiy
**发布日期**: 2026-03-06
**arXiv ID**: [2603.06130v1](https://arxiv.org/abs/2603.06130v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.06130v1)
**分类**: cs.RO, cs.AI

### 论文摘要

This report presents a structured Robotics Physical Safety Framework based on explicit asset declaration, systematic vulnerability enumeration, and hazard-driven synthetic data generation. The approach bridges classical risk engineering with modern machine learning pipelines, enabling safety envelope learning grounded in a formalized hazard ontology. The key contribution of this framework is the alignment between classical safety engineering, digital twin simulation, synthetic data generation, a...

### AI 总结

1. **一句话概述**
本文提出一种危害驱动的机器人安全框架，融合经典风险工程与机器学习，通过合成数据实现安全包络学习。

2. **核心贡献**
*   提出基于资产声明与漏洞枚举的结构化安全框架。
*   连接经典风险工程与现代机器学习管道。
*   实现基于形式化危害本体论的安全包络学习。
*   对齐数字孪生仿真、合成数据生成与模型训练流程。

3. **技术要点**
显式资产声明、系统漏洞枚举、危害驱动合成数据生成、形式化危害本体论、数字孪生仿真。

4. **潜在应用场景**
工业机器人安全认证、自主机器人系统测试、安全关键型模型训练、数字孪生安全仿真。

---

## 28. RESYSTANCE: Unleashing Hidden Performance of Compaction in LSM-trees via eBPF

**作者**: Hongsu Byun, Seungjae Lee, Honghyeon Yoo, Myoungjoon Kim, Sungyong Park
**发布日期**: 2026-03-05
**arXiv ID**: [2603.05162v1](https://arxiv.org/abs/2603.05162v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.05162v1)
**分类**: cs.DB

### 论文摘要

The development of high-speed storage devices such as NVMe SSDs has shifted the primary I/O bottleneck from hardware to software. Modern database systems also rely on kernel-based I/O paths, where frequent system call invocations and kernel-user space transitions lead to relatively large overheads and performance degradation. This issue is particularly pronounced in Log-Structured Merge-tree (LSM-tree)-based NoSQL databases. We identified that, in particular, the background compaction process ge...

### AI 总结

1. **一句话概述**
本文提出 RESYSTANCE，利用 eBPF 和 io_uring 将 LSM 树压缩 I/O 移至内核，减少系统调用，显著提升数据库性能。

2. **核心贡献**
*   **瓶颈识别**：发现 LSM 树后台压缩产生大量读系统调用，是高速存储下的主要软件瓶颈。
*   **方案提出**：提出 RESYSTANCE，利用 eBPF 在内核态直接处理压缩，消除系统调用开销。
*   **高效兼容**：结合 io_uring 优化磁盘 I/O，且无需修改原有 LSM 树结构或压缩算法。
*   **性能提升**：压缩系统调用减少 99%，写密集负载吞吐量提升最高 75%，p99 延迟降低 40%。

3. **技术要点**
*   **eBPF 内核态卸载**：通过 eBPF 程序在内核中直接处理压缩逻辑，避免用户态与内核态频繁切换。
*   **io_uring 异步 I/O**：利用 io_uring 接口实现高效磁盘读取，减少 I/O 等待时间。
*   **零侵入式设计**：仅卸载关键 I/O 例程至内核，完全兼容现有 LSM 树架构。
*   **系统调用消除**：将压缩过程中的读系统调用减少 99%，大幅降低软件栈开销。

4. **潜在应用场景**
*   基于 LSM 树的 NoSQL 数据库系统（如 RocksDB、LevelDB）。
*   搭载 NVMe SSD 等高速存储设备的服务器环境。
*   写密集型业务场景，如高频交易、日志存储及实时数据分析系统。

---

## 29. Engineering Regression Without Real-Data Training: Domain Adaptation for Tabular Foundation Models Using Multi-Dataset Embeddings

**作者**: Lyle Regenwetter, Rosen Yu, Cyril Picard, Faez Ahmed
**发布日期**: 2026-03-05
**arXiv ID**: [2603.04692v1](https://arxiv.org/abs/2603.04692v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.04692v1)
**分类**: cs.LG

### 论文摘要

Predictive modeling in engineering applications has long been dominated by bespoke models and small, siloed tabular datasets, limiting the applicability of large-scale learning approaches. Despite recent progress in tabular foundation models, the resulting synthetic training distributions used for pre-training may not reflect the statistical structure of engineering data, limiting transfer to engineering regression. We introduce TREDBench, a curated collection of 83 real-world tabular regression...

### AI 总结

1. **一句话概述**
本文提出嵌入引导的合成数据筛选方法，无需真实工程数据，即可显著提升表格基础模型在工程回归任务上的性能与效率。

2. **核心贡献**
*   构建 TREDBench 基准（83 个数据集），用于分析工程与非工程数据的域结构。
*   揭示标准合成数据与工程数据存在显著域差距，且可通过数据集嵌入进行区分。
*   提出无需真实数据的嵌入引导合成数据筛选与继续预训练方法， bridging 域差距。
*   在 35 个工程任务上超越 TabPFN 2.5 与 AutoGluon，平均数据效率提升 1.75 倍至 4.44 倍。

3. **技术要点**
*   **数据集嵌入表示：** 利用 TabPFN 2.5 的数据集级嵌入在共同表示空间中度量域相似性。
*   **合成数据筛选：** 基于嵌入相似度生成并识别“类工程”的合成数据集。
*   **无真实数据适配：** 仅使用筛选后的合成任务进行模型的继续预训练，实现领域适配。

4. **潜在应用场景**
*   数据稀缺的工程设计优化与性能预测。
*   科学发现及工业领域的表格回归建模。
*   真实数据收集成本高、受限或隐私敏感的建模场景。

---

## 30. The Case for Cardinality Lower Bounds

**作者**: Mihail Stoian, Tiemo Bang, Hangdong Zhao, Jesús Camacho-Rodríguez, Yuanyuan Tian
**发布日期**: 2026-01-19
**arXiv ID**: [2601.13117v2](https://arxiv.org/abs/2601.13117v2)
**PDF**: [下载](https://arxiv.org/pdf/2601.13117v2)
**分类**: cs.DB, cs.IT

### 论文摘要

Despite decades of research, cardinality estimation remains the optimizer's Achilles heel, with industrial-strength systems exhibiting a systemic tendency toward underestimation. At cloud scale, this is a severe production vulnerability: in Microsoft's Fabric Data Warehouse (DW), a mere 0.05% of extreme underestimates account for 95% of all CPU under-allocation, causing preventable slowdowns for thousands of queries daily. Yet recent theoretical work on provable upper bounds only corrects overes...

### AI 总结

1. **一句话概述**
本文针对数据库基数估计低估难题，提出首个可证明连接大小下界框架 xBound，显著改善生产系统查询性能。

2. **核心贡献**
*   指出基数估计低估是云规模数据库的严重生产漏洞，现有研究仅关注上界。
*   提出 xBound，首个可证明连接大小下界的理论框架。
*   仅需少量轻量级基表统计信息即可构建数学安全网。
*   在生产环境中修正 23.6% 低估案例，查询加速最高达 20.1 倍。

3. **技术要点**
*   **可证明下界：** 建立连接大小的理论下界计算模型。
*   **估计裁剪：** 从下方裁剪优化器的估计值，防止过度低估。
*   **轻量依赖：** 仅依赖基表统计信息，计算开销低。

4. **潜在应用场景**
*   云数据仓库（如 Microsoft Fabric）的查询优化器。
*   对 CPU 资源分配敏感的大规模查询场景。
*   需要防止因基数低估导致性能抖动的生产系统。

---

## 31. Stan: An LLM-based thermodynamics course assistant

**作者**: Eric M. Furst, Vasudevan Venkateshwaran
**发布日期**: 2026-03-04
**arXiv ID**: [2603.04657v1](https://arxiv.org/abs/2603.04657v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.04657v1)
**分类**: cs.CL, cs.CY, physics.ed-ph

### 论文摘要

Discussions of AI in education focus predominantly on student-facing tools -- chatbots, tutors, and problem generators -- while the potential for the same infrastructure to support instructors remains largely unexplored. We describe Stan, a suite of tools for an undergraduate chemical engineering thermodynamics course built on a data pipeline that we develop and deploy in dual roles: serving students and supporting instructors from a shared foundation of lecture transcripts and a structured text...

### AI 总结

1. **一句话概述**
Stan 是一个基于本地开源大模型的热力学课程助手，兼具学生答疑与教师教学分析功能，保障数据隐私与成本可控。

2. **核心贡献**
*   **双角色架构**：基于同一 lecture 转录和教材索引，同时服务于学生问答与教师教学反思。
*   **本地化部署**：完全使用本地硬件与开源模型，无云 API 依赖，确保数据隐私、成本可控及可复现性。
*   **教学洞察生成**：自动提取讲座摘要、学生疑问及教学类比，构建可搜索的学期级教学记录。
*   **工程实践总结**：分享了在长文本结构化提取中遇到的上下文截断、输出分布双峰及模式漂移等问题的解决方案。

3. **技术要点**
*   **模型栈**：Whisper large-v3（语音转文本）+ Llama 3.1 8B（文本生成与分析）。
*   **核心管道**：学生端采用检索增强生成（RAG）提供带引用的回答；教师端采用结构化分析管道。
*   **部署环境**：完全本地化硬件运行，无第三方服务依赖。
*   **难点攻关**：针对 7-8B 参数模型处理长转录文本时的失效模式进行了特定优化。

4. **潜在应用场景**
*   高校 STEM 专业课程的辅助教学与答疑。
*   教师教学反思、课程评估与持续改进。
*   对数据隐私敏感或预算有限的教育机构。
*   构建可搜索的课程知识库与学生学习档案。

---

## 32. Synthetic-Child: An AIGC-Based Synthetic Data Pipeline for Privacy-Preserving Child Posture Estimation

**作者**: Taowen Zeng
**发布日期**: 2026-03-03
**arXiv ID**: [2603.02598v1](https://arxiv.org/abs/2603.02598v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.02598v1)
**分类**: cs.CV

### 论文摘要

Accurate child posture estimation is critical for AI-powered study companion devices, yet collecting large-scale annotated datasets of children is both expensive and ethically prohibitive due to privacy concerns. We present Synthetic-Child, an AIGC-based synthetic data pipeline that produces photorealistic child posture training images with ground-truth-projected keypoint annotations, requiring zero real child photographs. The pipeline comprises four stages: (1) a programmable 3D child body mode...

### AI 总结

1. **一句话概述**
本文提出 Synthetic-Child，利用 AIGC 生成合成数据，无需真实儿童照片即可实现高精度隐私保护姿态估计及边缘部署。

2. **核心贡献**
*   **隐私保护：** 构建零真实儿童照片的 AIGC 数据管道，解决数据采集伦理难题。
*   **精度提升：** 合成数据训练模型超越成人数据基线 12.5 AP，实测优于商业矫正器。
*   **边缘部署：** 模型经 INT8 量化后，在低算力 NPU 上实现 22 FPS 实时推理。
*   **响应速度：** 系统平均响应速度比商业竞品快约 1.8 倍，识别率更高。

3. **技术要点**
*   **数据生成：** 基于 SMPL-X 3D 模型生成姿态，利用双 ControlNet 配合 FLUX-1 Dev 合成高保真图像。
*   **数据清洗：** 采用 ViTPose 进行置信度过滤，去除生成失败样本并增强鲁棒性。
*   **模型架构：** RTMPose-M 微调结合几何特征工程与轻量 MLP 进行分类。
*   **部署优化：** 模型量化为 INT8 格式，适配 Rockchip RK3568 NPU 硬件。

4. **潜在应用场景**
*   AI 学习伴侣设备中的儿童坐姿监测。
*   儿童健康管理与视力保护系统。
*   其他隐私敏感领域（如医疗康复、养老监护）的行为分析。

---

## 33. The Science Data Lake: A Unified Open Infrastructure Integrating 293 Million Papers Across Eight Scholarly Sources with Embedding-Based Ontology Alignment

**作者**: Jonas Wilinski
**发布日期**: 2026-03-03
**arXiv ID**: [2603.03126v1](https://arxiv.org/abs/2603.03126v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.03126v1)
**分类**: cs.DL, cs.DB, cs.IR, cs.SI

### 论文摘要

Scholarly data are largely fragmented across siloed databases with divergent metadata and missing linkages among them. We present the Science Data Lake, a locally-deployable infrastructure built on DuckDB and simple Parquet files that unifies eight open sources - Semantic Scholar, OpenAlex, SciSciNet, Papers with Code, Retraction Watch, Reliance on Science, a preprint-to-published mapping, and Crossref - via DOI normalization while preserving source-level schemas. The resource comprises approxim...

### AI 总结

1. **一句话概述**
本文提出科学数据湖，基于 DuckDB 统一整合 8 大来源的 2.93 亿篇论文，实现嵌入本体对齐与本地部署。

2. **核心贡献**
*   **数据整合**：统一 8 大开放来源（如 OpenAlex），涵盖 2.93 亿篇论文，通过 DOI 标准化消除数据孤岛。
*   **本体对齐**：利用 BGE-large 嵌入技术映射科学主题至 13 个本体，准确率优于传统基线方法。
*   **易用性**：支持本地 DuckDB 部署或远程查询，文档结构化以适配 LLM 代理。
*   **质量验证**：通过自动化检查、引用一致性分析及人工标注确保数据可靠性。

3. **技术要点**
*   **存储计算**：采用 DuckDB 引擎与 Parquet 文件格式，支持高效本地查询。
*   **语义对齐**：使用 BGE-large 句向量嵌入进行本体映射，F1 值达 0.77。
*   **数据清洗**：基于 DOI 进行归一化，同时保留各源头的原始模式架构。
*   **评估验证**：结合自动化检查、跨源引用皮尔逊相关性分析及分层人工标注。

4. **潜在应用场景**
*   大规模跨数据库文献计量学与科学图谱分析。
*   基于大语言模型（LLM）的科研智能体数据后端。
*   科学本体自动化映射、语义搜索及跨源数据关联研究。
*   需要本地部署高性能查询的学术数据基础设施搭建。

---

## 34. DiffusionXRay: A Diffusion and GAN-Based Approach for Enhancing Digitally Reconstructed Chest Radiographs

**作者**: Aryan Goyal, Ashish Mittal, Pranav Rao, Manoj Tadepalli, Preetham Putha
**发布日期**: 2026-03-02
**arXiv ID**: [2603.01686v1](https://arxiv.org/abs/2603.01686v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.01686v1)
**分类**: cs.CV

### 论文摘要

Deep learning-based automated diagnosis of lung cancer has emerged as a crucial advancement that enables healthcare professionals to detect and initiate treatment earlier. However, these models require extensive training datasets with diverse case-specific properties. High-quality annotated data is particularly challenging to obtain, especially for cases with subtle pulmonary nodules that are difficult to detect even for experienced radiologists. This scarcity of well-labeled datasets can limit ...

### AI 总结

1. **一句话概述**
DiffusionXRay 利用扩散模型与 GAN 协同增强数字重建胸片，解决肺癌诊断中数据稀缺及图像质量退化问题。

2. **核心贡献**
*   提出 DiffusionXRay 框架，融合 DDPM 与 GAN 提升数字重建胸片（DRR）质量。
*   克服 DRR 图像解剖特征模糊及肺野结构丢失的质量退化难题。
*   创新两阶段训练策略，先通过风格迁移生成低质图像，再学习复原细节。
*   经量化指标与专家评估验证，有效提升清晰度并保留临床显著伪影。

3. **技术要点**
*   **核心模型**：结合去噪扩散概率模型（DDPM）与生成对抗网络（GAN/MUNIT）。
*   **训练流程**：采用两阶段法。第一阶段利用 DDPM-LQ 和 MUNIT-LQ 生成低质量胸片（视为风格迁移）；第二阶段训练 DDPM 基于配对数据进行图像复原。
*   **优化目标**：在增强对比度与清晰度的同时，确保细微病灶特征不被丢失。

4. **潜在应用场景**
*   肺癌自动诊断深度学习模型的训练数据扩充。
*   基于 CT 扫描生成带有肺结节的高质量合成胸片。
*   低质量医学影像的清晰度增强与病灶细节复原。

---

## 35. SEAnet: A Deep Learning Architecture for Data Series Similarity Search

**作者**: Qitong Wang, Themis Palpanas
**发布日期**: 2026-03-02
**arXiv ID**: [2603.01448v1](https://arxiv.org/abs/2603.01448v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.01448v1)
**分类**: cs.DB, cs.LG

### 论文摘要

A key operation for massive data series collection analysis is similarity search. According to recent studies, SAX-based indexes offer state-of-the-art performance for similarity search tasks. However, their performance lags under high-frequency, weakly correlated, excessively noisy, or other dataset-specific properties. In this work, we propose Deep Embedding Approximation (DEA), a novel family of data series summarization techniques based on deep neural networks. Moreover, we describe SEAnet, ...

### AI 总结

1. **一句话概述**
本文提出 SEAnet 架构及 DEA 技术，利用深度神经网络与平方和保留属性，优化大规模数据序列相似性搜索。

2. **核心贡献**
*   提出基于深度神经网络的数据序列摘要新技术 DEA。
*   设计具有平方和保留属性的 SEAnet 架构。
*   引入 SEAtrans 编码器及 SEAsam 采样策略解决大规模训练难题。
*   多数据集实验验证了其在搜索精度与摘要质量上的优势。

3. **技术要点**
*   深度嵌入近似（DEA）
*   平方和保留机制
*   SEAtrans 编码器
*   SEAsam/SEAsamE 采样策略

4. **潜在应用场景**
*   大规模时间序列数据库检索
*   高频交易或弱相关数据分析
*   工业传感器高噪声数据监控

---

## 36. The Gravitational-wave Optical Transient Observer (GOTO) data pipeline and workflow for transient discovery

**作者**: J. D. Lyman, D. O'Neill, T. Killestein, D. Jarvis, A. Kumar
**发布日期**: 2026-03-02
**arXiv ID**: [2603.02330v1](https://arxiv.org/abs/2603.02330v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.02330v1)
**分类**: astro-ph.IM, astro-ph.SR

### 论文摘要

Wide-field and high-cadence sky surveys are the first step in the chain of discovery and characterisation of astrophysical transients such as supernovae, kilonovae, and tidal disruption events, each linked to the varied demise of stellar systems. The Gravitational-wave Optical Transient Observer (GOTO) is a telescope array of thirty-two 40 cm unit telescopes split over two almost antipodal sites. It performs a regular time-domain sky-survey in the optical to ~20 mag in addition to immediate sche...

### AI 总结

1. **一句话概述**
本文介绍了 GOTO 望远镜的低延迟数据管道，旨在快速发现引力波对应体及偶然瞬变源，通常在关闸后 7 分钟内完成候选体识别。

2. **核心贡献**
*   构建了适用于 GOTO 阵列的低延迟数据处理工作流。
*   利用差分成像分析，实现观测后约 7 分钟内输出候选体。
*   结合自动化与人工复核，支持瞬变源的即时表征与社区报告。
*   验证了该流程在快速发现及表征早期瞬变源方面的有效性。

3. **技术要点**
*   差分成像分析（DIA）识别候选源。
*   低延迟流水线架构。
*   自动化筛选与人机协作复核机制。
*   支持外部多信使触发调度与夜间即时跟进观测。

4. **潜在应用场景**
*   引力波事件光学对应体搜寻。
*   超新星、千新星及潮汐瓦解事件发现。
*   大规模时域天文巡天。
*   多信使天文学联合观测。

---

## 37. Trident: Adaptive Scheduling for Heterogeneous Multimodal Data Pipelines

**作者**: Ding Pan, Zhuangzhuang Zhou, Long Qian, Binhang Yuan
**发布日期**: 2026-03-02
**arXiv ID**: [2603.02075v1](https://arxiv.org/abs/2603.02075v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.02075v1)
**分类**: cs.DC

### 论文摘要

The rapid adoption of large language models and multimodal foundation models has made multimodal data preparation pipelines critical AI infrastructure. These pipelines interleave CPU-heavy preprocessing with accelerator-backed (GPU/NPU/TPU) inference and produce massive intermediate artifacts. Achieving high throughput is difficult because workloads are highly non-stationary: regime shifts, input-dependent inference, and transient memory spikes cause rapid performance fluctuations and out-of-mem...

### AI 总结

1. **一句话概述**
Trident 是面向异构多模态管道的自适应调度框架，通过三层闭环优化解决负载波动与内存溢出，显著提升吞吐量。

2. **核心贡献**
*   提出 Trident 框架，专为固定资源集群上的异构多模态数据管道设计。
*   构建观测 - 适应 - 调度三层闭环架构，协同优化异步算子性能。
*   有效应对负载非平稳性及内存溢出风险，优于传统阈值或静态调度器。
*   在 Ray Data 上实现，文档与视频管道吞吐量提升最高达 2.01 倍，开销低。

3. **技术要点**
*   **观测层**：利用高斯过程回归与异常过滤，估算异步算子的可持续吞吐量。
*   **适应层**：在线检测负载变化，采用内存约束贝叶斯优化推荐防溢出配置。
*   **调度层**：求解混合整数线性规划（MILP），联合优化并行度、放置及滚动更新。
*   **反馈机制**：决策触发样本失效与模型刷新，确保估计与当前配置一致。

4. **潜在应用场景**
*   大语言模型及多模态基础模型的数据准备管道。
*   大规模文档（如 PDF）与视频内容的清洗与策展流程。
*   混合 CPU 预处理与 GPU 推理的异构计算任务。
*   资源固定但负载波动剧烈、需避免内存溢出的 AI 基础设施。

---

## 38. Autoregressive Synthesis of Sparse and Semi-Structured Mixed-Type Data

**作者**: Thomas Rückstieß, Robin Vujanic
**发布日期**: 2026-03-02
**arXiv ID**: [2603.01444v1](https://arxiv.org/abs/2603.01444v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.01444v1)
**分类**: cs.LG

### 论文摘要

Synthetic data generation is a critical capability for data sharing, privacy compliance, system benchmarking and test data provisioning. Existing methods assume dense, fixed-schema tabular data, yet this assumption is increasingly at odds with modern data systems - from document databases, REST APIs to data lakes - which store and exchange data in sparse, semi-structured formats like JSON. Applying existing tabular methods to such data requires flattening of nested data into wide, sparse tables ...

### AI 总结

1. **一句话概述**
本文提出 Origami 模型，首次实现端到端原生合成稀疏半结构化数据，无需扁平化且性能优于现有方法。

2. **核心贡献**
*   提出 Origami 架构，基于自回归 Transformer 原生处理半结构化数据。
*   无需扁平化或插补，直接处理嵌套对象、变长数组及高稀疏性。
*   在保真度、效用及隐私指标上显著优于 GAN、VAE 等现有基线。
*   首个支持端到端原生建模与生成半结构化数据的架构。

3. **技术要点**
*   **架构：** 采用自回归 Transformer 模型。
*   **Token 化：** 将数据记录转化为键（key）、值（value）及结构 token 序列。
*   **原生支持：** 直接处理层级结构、变长数组及混合类型，避免扁平化导致的扩展性问题。

4. **潜在应用场景**
*   数据共享与隐私合规。
*   系统基准测试与测试数据生成。
*   文档数据库、REST API 及数据湖中的半结构化数据处理。

---

## 39. Contextual Invertible World Models: A Neuro-Symbolic Agentic Framework for Colorectal Cancer Drug Response

**作者**: Christopher Baker, Karen Rafferty, Hui Wang
**发布日期**: 2026-03-01
**arXiv ID**: [2603.02274v1](https://arxiv.org/abs/2603.02274v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.02274v1)
**分类**: q-bio.QM, cs.AI

### 论文摘要

Precision oncology is currently limited by the small-N, large-P paradox, where high-dimensional genomic data is abundant, but high-quality drug response samples are often sparse. While deep learning models achieve high predictive accuracy, they remain black boxes that fail to provide the causal mechanisms required for clinical decision-making. We present a Neuro-Symbolic Agentic Framework that bridges this gap by integrating a quantitative machine learning World Model with an LLM-based agentic r...

### AI 总结

1. **一句话概述**
本文提出神经符号代理框架，结合世界模型与 LLM，通过逆推理机制解决结直肠癌药物反应预测的小样本与黑盒难题。

2. **核心贡献**
*   构建神经符号代理框架，融合量化预测模型与 LLM 逻辑推理层。
*   引入临床上下文（如 MSI 状态）显式建模，显著提升预测相关性。
*   提出“逆推理”概念，模拟特定基因编辑对药物敏感性的因果影响。
*   经临床数据验证，提供透明且具生物学依据的可解释 AI 路径。

3. **技术要点**
*   **神经符号架构：** 集成机器学习世界模型与 LLM 代理推理层。
*   **可逆世界模型：** 支持正向药物反应预测与逆向因果推断。
*   **体外扰动模拟：** 代理层执行 in silico CRISPR 扰动（如 APC/TP53 修复）。
*   **法医式数据管道：** 基于 Sanger GDSC 数据集构建高质量分析流程。

4. **潜在应用场景**
*   结直肠癌精准用药方案制定。
*   肿瘤药物耐药机制分析与干预策略。
*   基因编辑疗法的虚拟筛选与效果预测。
*   高维基因组数据下的因果医学决策支持。

---

## 40. Cloud-OpsBench: A Reproducible Benchmark for Agentic Root Cause Analysis in Cloud Systems

**作者**: Yilun Wang, Guangba Yu, Haiyu Huang, Zirui Wang, Yujie Huang
**发布日期**: 2026-02-28
**arXiv ID**: [2603.00468v1](https://arxiv.org/abs/2603.00468v1)
**PDF**: [下载](https://arxiv.org/pdf/2603.00468v1)
**分类**: cs.SE

### 论文摘要

The transition to agentic Root Cause Analysis (RCA) necessitates benchmarks that evaluate active reasoning rather than passive classification. However, current frameworks fail to reconcile ecological validity with reproducibility. We introduce Cloud-OpsBench, a large-scale benchmark that employs a State Snapshot Paradigm to construct a deterministic digital twin of the cloud, featuring 452 distinct fault cases across 40 root cause types spanning the full Kubernetes stack. Crucially, Cloud-OpsBen...

### AI 总结

1. **一句话概述**
Cloud-OpsBench 基于状态快照构建数字孪生，解决云代理根因分析中有效性与可复现性矛盾。

2. **核心贡献**
*   **提出新基准**：兼顾生态有效性与可复现性，填补代理式根因分析评估空白。
*   **构建大规模故障集**：涵盖 40 种根因类型及全 Kubernetes 栈的 452 个 distinct 故障案例。
*   **定义三大功能角色**：作为数据引擎赋能模型微调、RL 环境提供安全沙箱、诊断标准指导系统设计。

3. **技术要点**
*   状态快照范式（State Snapshot Paradigm）
*   确定性数字孪生构建
*   以过程为中心的评估协议
*   支持 SFT 与强化学习的架构设计

4. **潜在应用场景**
*   云系统站点可靠性工程（SRE）研究
*   运维领域小语言模型监督微调
*   高风险运维操作的强化学习安全训练
*   根因分析多智能体系统架构优化

---

## 41. Automated Dose-Based Anatomic Region Classification of Radiotherapy Treatment for Big Data Applications

**作者**: Justin Hink, Yasin Abdulkadir, Jack Neylon, James Lamb
**发布日期**: 2026-02-26
**arXiv ID**: [2602.23536v1](https://arxiv.org/abs/2602.23536v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.23536v1)
**分类**: physics.med-ph, cs.CV

### 论文摘要

Curation is a significant barrier to using 'big data' radiotherapy planning databases of 100,000+ patients. Anatomic site stratification is essential for downstream analyses, but current methods rely on inconsistent plan labels or target nomenclature, which is unreliable for multi-institutional data. We developed software to automate labeling by inferring anatomic regions directly from dose-volume overlap with deep-learning segmentations, eliminating metadata reliance. The software processes DIC...

### AI 总结

1. **一句话概述**
本研究开发自动化工具，利用深度学习分割和剂量重叠分析，准确分类放疗解剖区域，助力大数据应用。

2. **核心贡献**
*   摆脱不一致元数据依赖，直接基于剂量 - 解剖重叠推断区域。
*   分类准确率高，验证集 Top-1 准确率达 95%。
*   提供可扩展、标准化方案，适用于多机构大数据清洗。
*   有效补充文本方法，能合理解释解剖边界模糊案例。

3. **技术要点**
*   深度学习自动分割 118 种结构（器官、骨骼等）并归类为 6 大解剖区域。
*   批量处理 DICOM 文件，将 85% 和 50% 等剂量线转化为结构。
*   计算器官特异性剂量重叠指标，基于交集生成排序区域标签。

4. **潜在应用场景**
*   大规模放疗数据库的自动化整理与分层。
*   多中心研究中的计划检索与队列构建。
*   放疗计划质量控制及回顾性疗效分析。

---

## 42. Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning

**作者**: Hao Yu, Shuning Jia, Guanghao Li, Wenhao Jiang, Chun Yuan
**发布日期**: 2026-02-26
**arXiv ID**: [2602.22703v1](https://arxiv.org/abs/2602.22703v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.22703v1)
**分类**: cs.LG

### 论文摘要

Vision-language models (VLMs) often struggle with geometric reasoning due to their limited perception of fundamental diagram elements. To tackle this challenge, we introduce GeoPerceive, a benchmark comprising diagram instances paired with domain-specific language (DSL) representations, along with an efficient automatic data generation pipeline. This design enables the isolated evaluation of geometric perception independently from reasoning. To exploit the data provided by GeoPerceive for enhanc...

### AI 总结

1. **一句话概述**
本文提出 GeoPerceive 基准与 GeoDPO 框架，利用翻译器引导强化学习显著增强 VLM 几何感知与推理能力。

2. **核心贡献**
*   构建 GeoPerceive 基准，提供图表 -DSL 配对数据，实现几何感知独立评估。
*   提出 GeoDPO 框架，利用 NL-to-DSL 翻译器引导强化学习优化模型感知。
*   实验证明 GeoDPO 在域内、域外及下游推理任务上均显著优于监督微调（SFT）。

3. **技术要点**
*   **NL-to-DSL 翻译器**：桥接自然语言与领域特定语言，实现细粒度语义对齐。
*   **细粒度奖励机制**：基于 DSL 级别匹配度计算分数，作为强化学习的奖励信号。
*   **自动数据生成**：通过合成数据引擎生成训练对，支持翻译器训练及基准构建。

4. **潜在应用场景**
*   数学几何题目自动求解。
*   教育智能辅导系统中的图表理解。
*   科研文献中的图表信息提取与分析。

---

## 43. Managing Uncertainty in LLM-based Multi-Agent System Operation

**作者**: Man Zhang, Tao Yue, Yihua He
**发布日期**: 2026-02-26
**arXiv ID**: [2602.23005v1](https://arxiv.org/abs/2602.23005v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.23005v1)
**分类**: cs.SE

### 论文摘要

Applying LLM-based multi-agent software systems in safety-critical domains such as lifespan echocardiography introduces system-level risks that cannot be addressed by improving model accuracy alone. During system operation, beyond individual LLM behavior, uncertainty propagates through agent coordination, data pipelines, human-in-the-loop interaction, and runtime control logic. Yet existing work largely treats uncertainty at the model level rather than as a first-class software engineering conce...

### AI 总结

1. **一句话概述**
本文针对安全关键领域 LLM 多智能体系统，提出生命周期不确定性管理框架，实现结构化运行时治理与适应。

2. **核心贡献**
*   将不确定性视为系统工程核心问题，区分认识论与本体论不确定性。
*   提出包含表示、识别、演化、适应四种机制的生命周期管理框架。
*   在真实医疗系统中验证，显著提升了诊断推理的可靠性与可诊断性。
*   方法可泛化至其他安全关键领域，支持超越模型中心的运行保证。

3. **技术要点**
*   **不确定性分类**：在系统运行语境下区分认识论和本体论不确定性。
*   **四机制框架**：通过表示、识别、演化、适应管理不确定性的生命周期。
*   **运行时治理**：控制不确定性在架构层与执行阶段间的传播与缓解。

4. **潜在应用场景**
*   医疗诊断辅助系统（如超声心动图分析）。
*   自动驾驶、工业控制等安全关键领域的多智能体系统。
*   涉及人机协作与复杂运行控制逻辑的 LLM 软件系统。

---

## 44. Kerr-induced Spectral Interferometry for Direct Ultra-sensitive Phase Recovery

**作者**: Glitta R. Cheeran, Mehmet Müftüoğlu, Sobhi Saeed, Bennet Fischer, Mario Chemnitz
**发布日期**: 2026-02-26
**arXiv ID**: [2602.22845v1](https://arxiv.org/abs/2602.22845v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.22845v1)
**分类**: physics.optics

### 论文摘要

Measuring the phase of light is fundamental to optical imaging, sensing, and signal processing applications. Conventional optical phase measurements rely on multipath configurations, bulky interferometric setups, and computationally intensive data pipelines, limiting scalability, robustness, and practicality. We introduce a technique that allows for reference-free in-line phase retrieval of abrupt phase transitions in optical pulses directly from spectral measurements. Theory, simulations, and e...

### AI 总结

1. **一句话概述**
本文提出一种克尔诱导光谱干涉技术，无需参考光和算法，可直接从光谱中高灵敏恢复光脉冲的相位突变。

2. **核心贡献**
*   提出无需参考光的在线相位检索新方法。
*   阐明克尔介导干涉的物理机制。
*   实现无需算法的直接相位测量。
*   达到π/385 高灵敏度与 80 MHz 高速率。

3. **技术要点**
*   **机制：** 利用克尔非线性效应，使投影线性波分量与相位改变脉冲的高强度残留部分发生干涉。
*   **测量：** 仅通过光谱测量即可直接提取相位信息，无需多路干涉装置。
*   **处理：** 摒弃复杂计算流程，实现算法免费的实时恢复。

4. **潜在应用场景**
*   光通信（飞秒脉冲作为宽带数据载体）
*   光信息处理
*   直接高通量相位成像
*   光学传感

---

## 45. Workload-Aware Incremental Reclustering in Cloud Data Warehouses

**作者**: Yipeng Liu, Renfei Zhou, Jiaqi Yan, Haunchen Zhang
**发布日期**: 2026-02-26
**arXiv ID**: [2602.23289v1](https://arxiv.org/abs/2602.23289v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.23289v1)
**分类**: cs.DB

### 论文摘要

Modern cloud data warehouses store data in micro-partitions and rely on metadata (e.g., zonemaps) for efficient data pruning during query processing. Maintaining data clustering in a large-scale table is crucial for effective data pruning. Existing automatic clustering approaches lack the flexibility required in dynamic cloud environments with continuous data ingestion and evolving workloads. This paper advocates a clean separation between reclustering policy and clustering-key selection. We int...

### AI 总结

1. **一句话概述**
本文提出 WAIR 算法，通过负载感知增量重聚类边界微分区，以低成本实现接近最优的查询性能。

2. **核心贡献**
*   主张重聚类策略与聚类键选择分离，增强动态云环境适应性。
*   引入“边界微分区”概念，精准定位影响剪枝效率的关键数据块。
*   设计 WAIR 算法，仅对关键边界分区进行增量重聚类，显著降低成本。
*   经基准测试验证，在接近最优查询性能的同时减少总体开销。

3. **技术要点**
*   基于微分区与元数据（如 zonemaps）的数据剪枝机制。
*   负载感知的边界微分区识别技术。
*   增量式重聚类策略及重聚类成本的理论上限分析。

4. **潜在应用场景**
*   云数据仓库的自动聚类优化服务。
*   高频数据摄入与查询负载演变的动态场景。
*   大规模表结构的性能与成本平衡管理。

---

## 46. Disentangling Shared and Target-Enriched Topics via Background-Contrastive Non-negative Matrix Factorization

**作者**: Yixuan Li, Archer Y. Yang, Yue Li
**发布日期**: 2026-02-25
**arXiv ID**: [2602.22387v1](https://arxiv.org/abs/2602.22387v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.22387v1)
**分类**: cs.LG

### 论文摘要

Biological signals of interest in high-dimensional data are often masked by dominant variation shared across conditions. This variation, arising from baseline biological structure or technical effects, can prevent standard dimensionality reduction methods from resolving condition-specific structure. The challenge is that these confounding topics are often unknown and mixed with biological signals. Existing background correction methods are either unscalable to high dimensions or not interpretabl...

### AI 总结

1. **一句话概述**
本文提出 bcNMF 方法，通过背景对比非负矩阵分解，分离共享变异并提取目标特有的可解释生物信号。

2. **核心贡献**
*   提出背景对比非负矩阵分解，有效解耦共享变异与目标特异性结构。
*   生成非负组件，实现特征层面的直接可解释性。
*   算法支持 GPU 加速与小批量训练，具备大规模数据可扩展性。
*   在多种生物场景中揭示了被传统方法掩盖的关键信号。

3. **技术要点**
*   **联合分解：** 同时分解目标数据集与匹配背景，共享非负基。
*   **对比目标：** 引入对比目标函数，主动抑制背景中表达的结构。
*   **高效更新：** 基于矩阵乘法的高效乘法更新算法。
*   **可扩展性：** 采用类似深度学习的小批量训练策略，适配 GPU 硬件。

4. **潜在应用场景**
*   单细胞 RNA 测序中的疾病相关程序识别（如抑郁症脑组织）。
*   基因型关联的蛋白质表达模式分析（如小鼠模型）。
*   特定治疗下的转录组变化研究（如白血病治疗）。
*   癌症细胞系的药物反应依赖性分析（如 TP53 依赖型）。

---

## 47. Quantum Resistance in Multilayer Graphene-BiFeO3 Memristor for Brain-Inspired Computing

**作者**: Suman Roy, Priyanka Sahu, Subhabrata Das, Sameer Kumar Mallik, Susmita Jana
**发布日期**: 2026-02-25
**arXiv ID**: [2602.21986v1](https://arxiv.org/abs/2602.21986v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.21986v1)
**分类**: cond-mat.mes-hall

### 论文摘要

In the era of big data and the Internet of Things, quantum-level control of conductance states offers a promising route toward high-density data storage and brain-inspired neuromorphic computing. Although quantum conductance (QC) phenomena have been demonstrated in various metal oxide memristors, achieving reliable and precise control over quantized states remains in its infancy. Here, we demonstrate bidirectional quantum conductance states in multifunctional BiFeO3 (BFO) perovskite memristors i...

### AI 总结

1. **一句话概述**
本文提出多层石墨烯-BiFeO3 忆阻器，实现双向量子电导态控制，适用于高精度类脑计算与识别。

2. **核心贡献**
*   实现了石墨烯-BiFeO3 忆阻器的双向高阶量子电导态调控。
*   阐明了氧空位动力学与界面局域电场诱导量子点接触的机制。
*   验证了器件模拟突触可塑性及高精度神经网络识别的能力。
*   证明了钙钛矿 -2D 异质结在量子忆阻器开发中的潜力。

3. **技术要点**
*   **材料体系**：多层石墨烯与 BiFeO3 钙钛矿异质结构。
*   **表征手段**：XPS 分析氧空位，第一性原理 DFT 计算界面电场。
*   **工作机制**：基于量子点接触形成的电流控制高阶量子电导跃迁。
*   **调控方式**：动态电压脉冲调谐下的量子态随机演化量化。

4. **潜在应用场景**
*   高密度数据存储。
*   类脑神经形态计算。
*   卷积神经网络（图像与数字识别）。
*   量子工程化记忆与计算设备。

---

## 48. Energy Efficient Federated Learning with Hyperdimensional Computing (HDC)

**作者**: Yahao Ding, Yinchao Yang, Jiaxiang Wang, Zhonghao Liu, Zhaohui Yang
**发布日期**: 2026-02-25
**arXiv ID**: [2602.22290v1](https://arxiv.org/abs/2602.22290v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.22290v1)
**分类**: cs.DC

### 论文摘要

This paper investigates the problem of minimizing total energy consumption for secure federated learning (FL) in wireless edge networks, a key paradigm for decentralized big data analytics. To tackle the high computational cost and privacy challenges of processing large-scale distributed data with conventional neural networks, we propose an FL with hyperdimensional computing and differential privacy (FL-HDC-DP) framework. Each edge device employs hyperdimensional computing (HDC) for lightweight ...

### AI 总结

1. **一句话概述**
本文提出结合超维计算与差分隐私的联邦学习框架，通过联合优化资源分配，显著降低无线边缘网络能耗。

2. **核心贡献**
*   提出 FL-HDC-DP 框架，利用超维计算降低计算成本，差分隐私保障数据安全。
*   建立总能耗最小化模型，联合优化超维维度、发射功率及 CPU 频率。
*   开发高效混合算法，结合外层枚举与内层一维搜索快速求解最优配置。
*   仿真显示相比基线方案能耗降低高达 83.3%，且保持高精度与快收敛。

3. **技术要点**
*   **超维计算（HDC）：** 用于边缘设备轻量级本地训练。
*   **差分隐私（DP）：** 添加噪声保护传输的模型更新。
*   **联合优化：** 同时调整计算与通信资源以最小化能耗。
*   **混合算法：** 外层枚举 HDC 维度，内层一维搜索资源分配。

4. **潜在应用场景**
*   无线边缘网络中的分布式大数据分析。
*   资源受限的物联网（IoT）设备协同学习。
*   对隐私和能耗敏感的智能终端应用（如移动健康监测）。

---

## 49. On Data Engineering for Scaling LLM Terminal Capabilities

**作者**: Renjie Pi, Grace Lam, Mohammad Shoeybi, Pooya Jannaty, Bryan Catanzaro
**发布日期**: 2026-02-24
**arXiv ID**: [2602.21193v1](https://arxiv.org/abs/2602.21193v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.21193v1)
**分类**: cs.CL

### 论文摘要

Despite rapid recent progress in the terminal capabilities of large language models, the training data strategies behind state-of-the-art terminal agents remain largely undisclosed. We address this gap through a systematic study of data engineering practices for terminal agents, making two key contributions: (1) Terminal-Task-Gen, a lightweight synthetic task generation pipeline that supports seed-based and skill-based task construction, and (2) a comprehensive analysis of data and training stra...

### AI 总结

1. **一句话概述**
本文研究 LLM 终端能力的数据工程，提出任务生成管道与数据集，显著提升模型性能并开源资源。

2. **核心贡献**
*   提出 Terminal-Task-Gen 轻量级合成任务生成管道。
*   构建并开源大规模终端任务数据集 Terminal-Corpus。
*   系统分析数据过滤、课程学习及长上下文等训练策略。
*   训练出的 Nemotron-Terminal 模型在基准测试上性能大幅提升，媲美更大模型。

3. **技术要点**
*   **任务生成**：支持基于种子和基于技能的合成任务构造。
*   **数据工程**：实施数据过滤与课程学习策略优化训练效果。
*   **模型扩展**：分析长上下文训练与模型 Scaling 行为。
*   **基座模型**：基于 Qwen3 (8B/14B/32B) 进行初始化与微调。

4. **潜在应用场景**
*   自动化命令行终端代理（CLI Agents）。
*   系统运维与复杂任务自动化脚本生成。
*   代码执行环境交互与调试助手。
*   LLM 智能体数据工程与基准测试研究。

---

## 50. Should I Hide My Duck in the Lake?

**作者**: Jonas Dann, Gustavo Alonso
**发布日期**: 2026-02-21
**arXiv ID**: [2602.18775v1](https://arxiv.org/abs/2602.18775v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.18775v1)
**分类**: cs.DB

### 论文摘要

Data lakes spend a significant fraction of query execution time on scanning data from remote storage. Decoding alone accounts for 46% of runtime when running TPC-H directly on Parquet files. To address this bottleneck, we propose a vision for a data processing SmartNIC for the cloud that sits on the network datapath of compute nodes to offload decoding and pushed-down operators, effectively hiding the cost of querying raw files. Our experimental estimations with DuckDB suggest that by operating ...

### AI 总结

1. **一句话概述**
本文提出云 SmartNIC 方案，通过卸载解码和算子隐藏数据湖查询成本，使小 CPU 匹配原有吞吐量。

2. **核心贡献**
*   揭示数据湖查询中远程存储解码耗时占比高（46%）的性能瓶颈。
*   提出部署于网络数据路径的 SmartNIC 架构，用于卸载解码与下推算子。
*   验证该方案可使较小规格 CPU 达到传统设置的查询吞吐量。

3. **技术要点**
*   SmartNIC 硬件卸载技术。
*   网络数据路径集成。
*   算子下推（Pushed-down operators）。
*   预过滤数据传输。

4. **潜在应用场景**
*   云端数据湖查询加速。
*   大规模数据分析任务。
*   计算资源受限的云环境。

---

## 51. LakeMLB: Data Lake Machine Learning Benchmark

**作者**: Feiyu Pan, Tianbin Zhang, Aoqian Zhang, Yu Sun, Zheng Wang
**发布日期**: 2026-02-11
**arXiv ID**: [2602.10441v1](https://arxiv.org/abs/2602.10441v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.10441v1)
**分类**: cs.LG, cs.AI

### 论文摘要

Modern data lakes have emerged as foundational platforms for large-scale machine learning, enabling flexible storage of heterogeneous data and structured analytics through table-oriented abstractions. Despite their growing importance, standardized benchmarks for evaluating machine learning performance in data lake environments remain scarce. To address this gap, we present LakeMLB (Data Lake Machine Learning Benchmark), designed for the most common multi-source, multi-table scenarios in data lak...

### AI 总结

1. **一句话概述**
本文提出 LakeMLB 基准，填补数据湖机器学习评估空白，涵盖多表场景、真实数据集及多种集成策略的评估。

2. **核心贡献**
- 提出首个针对数据湖多源多表场景的机器学习基准 LakeMLB。
- 提供涵盖政府、金融等领域的 6 个真实数据集（Union 和 Join 场景各 3 个）。
- 系统评估了预训练、数据增强和特征增强三种数据集成策略。
- 开源数据集与代码，促进数据湖生态下的严谨研究。

3. **技术要点**
- **场景建模**：聚焦数据湖最常见的 Union（并集）和 Join（连接）多表操作。
- **策略对比**：实现并比较三种代表性的多表数据整合技术路线。
- **实验验证**：基于最先进（SOTA）表格学习方法进行广泛性能测试。

4. **潜在应用场景**
- 数据湖平台机器学习性能评测与算法选型。
- 跨源异构数据的自动化整合与特征工程研究。
- 金融风控、政府数据分析及电商推荐等多表关联任务。

---

## 52. Optimal Bounds-Only Pruning for Spatial AkNN Joins

**作者**: Dominik Winecki
**发布日期**: 2026-02-10
**arXiv ID**: [2602.10027v1](https://arxiv.org/abs/2602.10027v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.10027v1)
**分类**: cs.DB

### 论文摘要

We propose a bounds-only pruning test for exact Euclidean AkNN joins on partitioned spatial datasets. Data warehouses commonly partition large tables and store row group statistics for them to accelerate searches and joins, rather than maintaining indexes. AkNN joins can benefit from such statistics by constructing bounds and localizing join evaluations to a few partitions before loading them to build spatial indexes. Existing pruning methods are overly conservative for bounds-only spatial data ...

### AI 总结

1. **一句话概述**
该论文提出了一种最优的仅边界剪枝测试，用于加速数据仓库中分区空间数据集上的精确欧几里得 AkNN 连接操作。

2. **核心贡献**
- 提出针对分区空间数据集的仅边界剪枝测试方法。
- 克服现有方法因忽略方向语义而过于保守的缺陷。
- 设计三界邻近性测试，实现早期跳过无关分区。
- 证明该算法在理论上最优且执行高效。

3. **技术要点**
- 利用数据仓库现有的行组统计信息构建边界，无需预先维护索引。
- 通过三界邻近性测试捕捉空间数据的方向语义，判断分区间的遮挡关系。
- 在加载数据构建空间索引之前，将连接评估定位到少数分区，减少 I/O 开销。

4. **潜在应用场景**
- 大型数据仓库中的空间连接查询加速。
- 无预建索引环境下的大规模空间数据分析。
- 地理信息系统（GIS）中的大规模邻近点搜索任务。

---

## 53. LakeHopper: Cross Data Lakes Column Type Annotation through Model Adaptation

**作者**: Yushi Sun, Xujia Li, Nan Tang, Quanqing Xu, Chuanhui Yang
**发布日期**: 2026-02-09
**arXiv ID**: [2602.08793v1](https://arxiv.org/abs/2602.08793v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.08793v1)
**分类**: cs.CL, cs.DB

### 论文摘要

Column type annotation is vital for tasks like data cleaning, integration, and visualization. Recent solutions rely on resource-intensive language models fine-tuned on well-annotated columns from a particular set of tables, i.e., a source data lake. In this paper, we study whether we can adapt an existing pre-trained LM-based model to a new (i.e., target) data lake to minimize the annotations required on the new data lake. However, challenges include the source-target knowledge gap, selecting in...

### AI 总结

1. **一句话概述**
本文提出 LakeHopper 框架，通过模型适配实现跨数据湖列类型标注，显著减少新数据湖的标注成本。

2. **核心贡献**
*   提出 LakeHopper 框架，支持跨数据湖的列类型标注模型迁移。
*   通过语言模型交互识别并解决源与目标数据湖间的知识差距。
*   设计基于聚类的数据选择方案，高效筛选未标注列中的信息样本。
*   采用增量微调机制，在适配目标数据湖时避免丢失共享知识。

3. **技术要点**
*   **知识差距识别**：利用语言模型交互分析源域与目标域的差异。
*   **聚类数据选择**：针对未标注列进行聚类，选取代表性样本进行标注。
*   **增量微调**：逐步更新模型参数，平衡新旧知识保留，防止灾难性遗忘。

4. **潜在应用场景**
*   数据清洗与集成任务中的自动化列类型识别。
*   数据可视化前的元数据理解与 Schema 匹配。
*   新数据湖接入时的低资源快速标注与模型适配。

---

## 54. ByteHouse: A Cloud-Native OLAP Engine with Incremental Computation and Multi-Modal Retrieval

**作者**: Yuxing Han, Yu Lin, Yifeng Dong, Xuanhe Zhou, Xindong Peng
**发布日期**: 2026-02-09
**arXiv ID**: [2602.08226v1](https://arxiv.org/abs/2602.08226v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.08226v1)
**分类**: cs.DB

### 论文摘要

With the rapid rise of intelligent data services, modern enterprises increasingly require efficient, multimodal, and cost-effective data analytics infrastructures. However, in ByteDance's production environments, existing systems fall short due to limitations such as I/O-inefficient multimodal storage, inflexible query optimization (e.g., failing to optimize multimodal access patterns), and performance degradation caused by resource disaggregation (e.g., loss of data locality in remote storage)....

### AI 总结

1. **一句话概述**
ByteHouse 是字节云原生数仓，支持多模态实时分析，通过存算优化与 AI 辅助查询提升效率。

2. **核心贡献**
*   解决多模态存储 I/O 低效及资源分离导致的性能瓶颈。
*   设计统一表引擎与集群级 SSD 缓存，实现高效数据访问。
*   支持增量计算与混合查询优化，适应多样化执行模式。
*   引入 AI 辅助优化器，基于历史轨迹提升查询计划质量。

3. **技术要点**
*   **存储层**：统一表引擎（两层逻辑抽象）、CrossCache（共享 SSD 缓存）、NexusFS（虚拟文件系统）。
*   **计算层**：支持分析/批处理/增量模式，优化分层向量索引上的混合查询。
*   **控制层**：全局元数据管理，基于历史轨迹与 AI 的查询优化器。

4. **潜在应用场景**
*   企业级智能数据服务基础设施。
*   实时多模态数据分析（如向量检索与结构化数据混合查询）。
*   对成本与效率敏感的云原生数据仓库场景。

---

## 55. Beyond Text-to-SQL: Autonomous Research-Driven Database Exploration with DAR

**作者**: Ostap Vykhopen, Viktoria Skorik, Maksym Tereshchenko, Veronika Solopova
**发布日期**: 2025-12-16
**arXiv ID**: [2512.14622v2](https://arxiv.org/abs/2512.14622v2)
**PDF**: [下载](https://arxiv.org/pdf/2512.14622v2)
**分类**: cs.DB

### 论文摘要

Large language models can already query databases, yet most existing systems remain reactive: they rely on explicit user prompts and do not actively explore data. We introduce DAR (Data Agnostic Researcher), a multi-agent system that performs end-to-end database research without human-initiated queries. DAR orchestrates specialized AI agents across three layers: initialization (intent inference and metadata extraction), execution (SQL and AI-based query synthesis with iterative validation), and ...

### AI 总结

1. **一句话概述**
本文提出 DAR 系统，可在云数据仓库内自主研究数据库，无需人工查询，分析速度比人类快 32 倍。

2. **核心贡献**
*   **范式创新**：将数据库交互从被动查询转向自主研究驱动的探索。
*   **系统设计**：实现端到端无人工干预的多智能体协作架构。
*   **数据治理**：利用原生 AI 函数库内推理，无需数据移动，保障安全。
*   **性能验证**：实证分析速度比专业分析师快约 32 倍，且能提供有效洞察。

3. **技术要点**
*   **三层智能架构**：涵盖初始化（意图推断）、执行（查询合成与验证）、合成（报告生成）。
*   **库内推理**：基于 BigQuery 原生生成式 AI 函数直接执行，避免数据导出。
*   **迭代验证**：SQL 与 AI 结合的查询合成机制，内置质量控制流程。

4. **潜在应用场景**
*   快速探索性数据分析。
*   自动化商业智能报告生成。
*   高数据治理要求下的安全洞察。
*   资产或事件异常模式发现。

---

## 56. Learned Query Optimizer in Alibaba MaxCompute: Challenges, Analysis, and Solutions

**作者**: Lianggui Weng, Dandan Liu, Wenzhuang Zhu, Rong Zhu, Junzheng Zheng
**发布日期**: 2026-02-07
**arXiv ID**: [2602.07336v1](https://arxiv.org/abs/2602.07336v1)
**PDF**: [下载](https://arxiv.org/pdf/2602.07336v1)
**分类**: cs.DB

### 论文摘要

Existing learned query optimizers remain ill-suited to modern distributed, multi-tenant data warehouses due to idealized modeling assumptions and design choices. Using Alibaba's MaxCompute as a representative, we surface four fundamental, system-agnostic challenges for any deployable learned query optimizer: 1) highly dynamic execution environments that induce large variance in plan costs; 2) potential absence of input statistics needed for cost estimation; 3) infeasibility of conventional model...

### AI 总结

1. **一句话概述**
本文针对 MaxCompute 提出 LOAM 框架，解决学习型优化器在分布式多租户环境的部署挑战，实现显著 CPU 节省。

2. **核心贡献**
*   揭示了学习型优化器在生产环境面临的四大核心挑战（环境动态、统计缺失等）。
*   提出 LOAM 框架，采用无统计信息计划编码和环境感知设计。
*   引入域适应技术，无需传统模型微调即可有效泛化至在线查询。
*   在生产负载上实现比原生优化器最高 30% 的 CPU 成本节省。

3. **技术要点**
*   **无统计信息编码**：利用算子语义和历史执行推断数据分布，显式编码执行环境。
*   **在线预测策略**：提供性能理论界及平滑环境波动的实用方法，应对未知环境。
*   **域适应训练**：集成域适应技术，避免常规模型 refinement，适应在线计划。
*   **轻量级选择器**：优先选择高收益项目进行部署，确保优化效益。

4. **潜在应用场景**
*   大规模分布式多租户数据仓库（如 MaxCompute）。
*   输入统计信息缺失或动态变化的云数据库系统。
*   对计算资源成本敏感的大规模生产级查询环境。

---

## 57. Evaluation of Oncotimia: An LLM based system for supporting tumour boards

**作者**: Luis Lorenzo, Marcos Montana-Mendez, Sergio Figueiras, Miguel Boubeta, Cristobal Bernardo-Castineira
**发布日期**: 2026-01-27
**arXiv ID**: [2601.19899v1](https://arxiv.org/abs/2601.19899v1)
**PDF**: [下载](https://arxiv.org/pdf/2601.19899v1)
**分类**: cs.CL

### 论文摘要

Multidisciplinary tumour boards (MDTBs) play a central role in oncology decision-making but require manual processes and structuring large volumes of heterogeneous clinical information, resulting in a substantial documentation burden. In this work, we present ONCOTIMIA, a modular and secure clinical tool designed to integrate generative artificial intelligence (GenAI) into oncology workflows and evaluate its application to the automatic completion of lung cancer tumour board forms using large la...

### AI 总结

1. **一句话概述**
本研究评估了 ONCOTIMIA 系统，利用 LLM 自动填充肺癌肿瘤委员会表格，证实了其减轻文档负担的可行性与有效性。

2. **核心贡献**
*   设计了 ONCOTIMIA 系统，将生成式 AI 整合到肿瘤学多学科会诊工作流中。
*   基于 10 个肺癌病例，评估了 6 种 LLM 的表单填充准确率与端到端延迟。
*   最佳配置实现了 80% 的字段填充准确率，且响应时间符合临床要求。
*   证实了 LLM 辅助自动填表能显著减少文档负担并保持数据质量。

3. **技术要点**
*   **架构：** 多层数据湖，混合关系型与向量存储。
*   **算法：** 检索增强生成（RAG）与规则驱动的自适应表单模型。
*   **部署：** 通过 AWS Bedrock 部署多种大语言模型。
*   **功能：** 将非结构化临床文档转化为结构化标准记录。

4. **潜在应用场景**
*   多学科肿瘤委员会（MDTB）的决策支持与会诊记录。
*   肿瘤临床诊疗表单的自动化填写与结构化。
*   医院临床工作流中的医疗文档减负与质量管控。
*   扩展至其他癌种或复杂临床决策场景的 AI 辅助记录。

---

## 58. Create Benchmarks for Data Lakes

**作者**: Yi Lyu, Pei-Chieh Lo, Natan Lidukhover
**发布日期**: 2026-01-27
**arXiv ID**: [2601.19176v1](https://arxiv.org/abs/2601.19176v1)
**PDF**: [下载](https://arxiv.org/pdf/2601.19176v1)
**分类**: cs.DB

### 论文摘要

Data lakes have emerged as a flexible and scalable solution for storing and analyzing large volumes of heterogeneous data, including structured, semi-structured, and unstructured formats. Despite their growing adoption in both industry and academia, there is a lack of standardized and comprehensive benchmarks for evaluating the performance of data lake systems. Existing benchmarks primarily target traditional data warehouses and focus on structured SQL workloads, making them insufficient for cap...

### AI 总结

1. **一句话概述**
本文提出新型数据湖基准测试框架，涵盖多数据类型与工作负载，用于客观评估不同数据湖系统的性能表现。

2. **核心贡献**
- 填补了数据湖领域缺乏标准化综合基准测试的空白。
- 涵盖多种数据类型及工作负载模型，包含常被忽视的相似度搜索。
- 定义了查询执行时间、元数据生成时间及大小等关键性能指标。
- 框架具备可扩展性与可复现性，支持生成多样化真实场景数据集。

3. **技术要点**
- 支持结构化、半结构化及非结构化多种数据格式。
- 包含数据检索、聚合、查询及相似度搜索等工作负载。
- 在不同规模因子下测量系统性能与元数据开销。
- 基于 CloudLab 实现，支持商业与开源平台对比评估。

4. **潜在应用场景**
- 数据湖系统开发商进行性能优化与版本对比。
- 学术研究人员评估新型数据湖架构或算法。
- 企业用户在选型时客观对比商业与开源数据湖平台。

---

## 59. A Distributed Spatial Data Warehouse for AIS Data (DIPAAL)

**作者**: Alex S. Klitgaard, Lau E. Josefsen, Mikael V. Mikkelsen, Kristian Torp
**发布日期**: 2026-01-20
**arXiv ID**: [2601.13795v1](https://arxiv.org/abs/2601.13795v1)
**PDF**: [下载](https://arxiv.org/pdf/2601.13795v1)
**分类**: cs.DB

### 论文摘要

AIS data from ships is excellent for analyzing single-ship movements and monitoring all ships within a specific area. However, the AIS data needs to be cleaned, processed, and stored before being usable. This paper presents a system consisting of an efficient and modular ETL process for loading AIS data, as well as a distributed spatial data warehouse storing the trajectories of ships. To efficiently analyze a large set of ships, a raster approach to querying the AIS data is proposed. A spatiall...

### AI 总结

1. **一句话概述**
本文提出分布式空间数据仓库 DIPAAL，通过栅格化查询和空间分片，高效存储与分析海量 AIS 船舶轨迹数据。

2. **核心贡献**
*   设计了包含高效模块化 ETL 流程的分布式空间数据仓库系统。
*   提出基于栅格化的 AIS 数据查询方法，效率优于传统轨迹查询。
*   实现空间分片存储策略，支持大规模区域分析的良好扩展性。
*   在十亿级行数据规模下验证了系统的高性能与线性扩展能力。

3. **技术要点**
*   分布式空间数据仓库架构
*   模块化 ETL 数据处理
*   栅格化单元（Cell）表示法
*   空间分片（Spatial Sharding）
*   热力图可视化呈现

4. **潜在应用场景**
*   单船或多船运动轨迹监控
*   特定海域船舶流量统计
*   海事交通密度热力图生成
*   大规模航运数据挖掘与分析

---

## 60. AHA: Scalable Alternative History Analysis for Operational Timeseries Applications

**作者**: Harshavardhan Kamarthi, Harshil Shah, Henry Milner, Sayan Sinha, Yan Li
**发布日期**: 2026-01-07
**arXiv ID**: [2601.04432v1](https://arxiv.org/abs/2601.04432v1)
**PDF**: [下载](https://arxiv.org/pdf/2601.04432v1)
**分类**: cs.DB

### 论文摘要

Many operational systems collect high-dimensional timeseries data about users/systems on key performance metrics. For instance, ISPs, content distribution networks, and video delivery services collect quality of experience metrics for user sessions associated with metadata (e.g., location, device, ISP). Over such historical data, operators and data analysts often need to run retrospective analysis; e.g., analyze anomaly detection algorithms, experiment with different configurations for alerts, e...

### AI 总结

1. **一句话概述**
AHA 系统针对运营时间序列数据，提供低成本且高保真的替代历史分析，克服了传统方案在成本与准确性上的局限。

2. **核心贡献**
*   定义了运营数据集上的“替代历史分析”工作负载类别。
*   设计 AHA 系统，兼顾高维数据的成本效率与分析保真度。
*   实现下游任务 100% 准确，总拥有成本降低高达 85 倍。
*   经真实数据集及生产管道验证了系统有效性。

3. **技术要点**
*   利用底层统计信息的可分解性。
*   利用属性值组合上活跃子群体的稀疏性。
*   优化现代分析数据库中聚合操作的效率结构。

4. **潜在应用场景**
*   ISP、CDN 及视频服务的用户体验质量监控。
*   异常检测算法评估与警报配置实验。
*   运营系统的高维时间序列数据回溯分析。

---

