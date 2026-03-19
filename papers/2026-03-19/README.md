# 大数据+AI 领域论文日报

**日期**: 2026-03-19

**论文数量**: 10 篇精选论文

---

## 1. Drug-like antibodies with low immunogenicity in human panels designed with Latent-X2

- **作者**: Latent Labs Team, Henry Kenlay, Daniella Pretorius, Jonathan Crabbé, Alex Bridgland
- **发布日期**: 2025-12-23
- **链接**: [arXiv:2512.20263v1](https://arxiv.org/abs/2512.20263v1) | [PDF](https://arxiv.org/pdf/2512.20263v1)
- **分类**: q-bio.BM
- **含金量**: 9/40 分

### 摘要

Drug discovery has long sought computational systems capable of designing drug-like molecules directly: developable and non-immunogenic from the start.

Here we introduce Latent-X2, a frontier generative model that achieves this goal through zero-shot design of antibodies with strong binding affinities, drug-like properties, and, for the first time for any de novo generated antibody, confirmed low immunogenicity in human donor panels.

Latent-X2 is an all-atom model conditioned on target structure, epitope specification, and optional antibody framework, jointly generating sequences and structure

### AI 总结

**概述**：本文提出 Latent-X2 模型，首次实现零样本设计低免疫原性抗体并经人类面板验证。

**核心贡献**：
- 首次确认 AI 生成抗体在人类供体面板中具有低免疫原性
- 零样本设计抗体可开发性媲美获批药物，无需优化筛选
- 模型泛化能力强，成功生成针对难成药靶点 K-Ras 的大环肽

**技术要点**：
- 基于靶点结构、表位及框架条件化的全原子生成模型
- 联合生成序列与结构并建模结合复合物，支持零样本设计

**应用场景**：抗体药物发现、难成药靶点开发、大环肽设计

---

## 2. IndicSafe: A Benchmark for Evaluating Multilingual LLM Safety in South Asia

- **作者**: Priyaranjan Pattnayak, Sanchari Chowdhuri
- **发布日期**: 2026-03-18
- **链接**: [arXiv:2603.17915v1](https://arxiv.org/abs/2603.17915v1) | [PDF](https://arxiv.org/pdf/2603.17915v1)
- **分类**: cs.CL, cs.AI
- **含金量**: 8.3/40 分

### 摘要

As large language models (LLMs) are deployed in multilingual settings, their safety behavior in culturally diverse, low-resource languages remains poorly understood.

We present the first systematic evaluation of LLM safety across 12 Indic languages, spoken by over 1.2 billion people but underrepresented in LLM training data.

Using a dataset of 6,000 culturally grounded prompts spanning caste, religion, gender, health, and politics, we assess 10 leading LLMs on translated variants of the prompt.

Our analysis reveals significant safety drift: cross-language agreement is just 12.8\%, and \textt

### AI 总结

**概述**：本文提出 IndicSafe 基准，评估 12 种印度语言大模型安全性，发现跨语言安全对齐存在显著差距。

**核心贡献**：
- 首创 IndicSafe 基准，覆盖 12 种印度语言及 6000 个文化相关提示词
- 评估 10 个主流大模型，揭示跨语言安全一致性低至 12.8%
- 提出多项量化指标，证明安全对齐无法均匀迁移至不同语言

**技术要点**：
- 构建涵盖种姓、宗教等维度的文化接地提示词数据集
- 利用提示词熵和多语言一致性指数量化安全失效模式

**应用场景**：南亚多语言大模型部署、低资源语言安全对齐优化、跨文化内容风险评测

---

## 3. HyGra: Accelerating Network-State Simulation for LLM Training in DCNs via Adaptive Packet-Flow Granularity

- **作者**: Wenyi Wang, Zheng Wu, Yanmeng Wang, Haolin Mao, Lei Han
- **发布日期**: 2026-03-13
- **链接**: [arXiv:2603.12671v1](https://arxiv.org/abs/2603.12671v1) | [PDF](https://arxiv.org/pdf/2603.12671v1)
- **分类**: cs.NI
- **含金量**: 8/40 分

### 摘要

In recent years, large language models (LLMs) have driven substantial intelligent transformation across diverse industries.

Commercial LLM training is typically performed over data center networks (DCNs) comprising hundreds to thousands of GPUs, with multiple devices collocated per node.

As network scale expands, inter-node communication becomes a primary bottleneck to training efficiency.

Network-state simulators therefore play a crucial role by enabling cost-effective evaluation of network configurations and parallelization strategies through faithful emulation of DCN dynamics during LLM tra

### AI 总结

**概述**：本文提出 HyGra 模拟器，通过自适应切换包级与流级粒度，加速数据中心网络大模型训练状态模拟。

**核心贡献**：
- 提出混合粒度模拟器 HyGra，突破现有模拟器效率与保真度的权衡限制。
- 设计自适应机制，在非稳态阶段用包级、稳态阶段用流级进行模拟。
- 在多种商业大模型负载下实现最高 15.4 倍加速，且保持高模拟精度。

**技术要点**：
- 利用训练内在网络动态，识别瞬态波动与周期模式以切换粒度。
- 无需专用硬件，支持单机部署并兼容现有模拟器架构。

**应用场景**：大模型训练网络配置评估、并行化策略优化、数据中心网络动态仿真

---

## 4. The Curse and Blessing of Mean Bias in FP4-Quantized LLM Training

- **作者**: Hengjie Cao, Zhendong Huang, Mengyi Chen, Yifeng Yang, Fanqi Yu
- **发布日期**: 2026-03-11
- **链接**: [arXiv:2603.10444v1](https://arxiv.org/abs/2603.10444v1) | [PDF](https://arxiv.org/pdf/2603.10444v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 8/40 分

### 摘要

Large language models trained on natural language exhibit pronounced anisotropy: a small number of directions concentrate disproportionate energy, while the remaining dimensions form a broad semantic tail.

In low-bit training regimes, this geometry becomes numerically unstable.

Because blockwise quantization scales are determined by extreme elementwise magnitudes, dominant directions stretch the dynamic range, compressing long-tail semantic variation into narrow numerical bins.

We show that this instability is primarily driven by a coherent rank-one mean bias, which constitutes the dominant co

### AI 总结

**概述**：本文揭示低比特训练不稳定源于均值偏差，提出简单均值减法操作，有效恢复 FP4 训练稳定性。

**核心贡献**：
- 揭示低比特训练不稳定性主要由秩一均值偏差驱动
- 提出硬件高效的源级均值减法操作替代复杂谱方法
- 实证表明该方法在 FP4 训练中显著缩小与 BF16 的性能差距

**技术要点**：
- 识别出均值偏差是动态范围膨胀及量化不稳定的主要驱动因素
- 利用标准量化内核和归约操作实现均值移除，无需额外硬件开销

**应用场景**：低比特大模型训练、FP4 量化训练、高效能推理部署

---

## 5. Orion: Characterizing and Programming Apple's Neural Engine for LLM Training and Inference

- **作者**: Ramchand Kumaresan
- **发布日期**: 2026-03-06
- **链接**: [arXiv:2603.06728v1](https://arxiv.org/abs/2603.06728v1) | [PDF](https://arxiv.org/pdf/2603.06728v1)
- **分类**: cs.LG, cs.AR, cs.CL
- **含金量**: 8/40 分

### 摘要

Over two billion Apple devices ship with a Neural Processing Unit (NPU) - the Apple Neural Engine (ANE) - yet this accelerator remains largely unused for large language model workloads.

CoreML, Apple's public ML framework, imposes opaque abstractions that prevent direct ANE programming and do not support on-device training.

We present Orion, to our knowledge the first open end-to-end system that combines direct ANE execution, a compiler pipeline, and stable multi-step training with checkpoint resume in a single native runtime, bypassing CoreML entirely via Apple's private _ANEClient and _ANECo

### AI 总结

**概述**：本文提出 Orion 系统，绕过 CoreML 直接编程苹果神经引擎，实现大模型高效训练与推理。

**核心贡献**：
- 首创绕过 CoreML 的端到端系统，支持 ANE 直接执行与稳定训练。
- 扩展 ANE 约束知识目录，发现 14 项未文档化的硬件与编译限制。
- 实现权重热更新机制，将训练重编译时间减少 8.5 倍，速度提升 3.8 倍。

**技术要点**：
- 包含五层优化 passes 的编译器及基于 IOSurface 的零拷贝张量运行时。
- 采用卸载 - 补丁 - 重载机制更新权重，支持 LoRA 适配器热切换无需重编译。

**应用场景**：端侧大模型推理、端侧大模型训练、LoRA 适配器热切换

---

## 6. NEST: Network- and Memory-Aware Device Placement For Distributed Deep Learning

- **作者**: Irene Wang, Vishnu Varma Venkata, Arvind Krishnamurthy, Divya Mahajan
- **发布日期**: 2026-03-06
- **链接**: [arXiv:2603.06798v1](https://arxiv.org/abs/2603.06798v1) | [PDF](https://arxiv.org/pdf/2603.06798v1)
- **分类**: cs.LG, cs.DC, stat.ML
- **含金量**: 8/40 分

### 摘要

The growing scale of deep learning demands distributed training frameworks that jointly reason about parallelism, memory, and network topology.

Prior works often rely on heuristic or topology-agnostic search, handling communication and memory separately.

Without per-device memory awareness, these methods typically ensure feasibility post hoc by sharding parameters and activations across many devices, increasing synchronization, inflating communication, and underutilizing compute-limiting scalability and efficiency on real datacenter networks.

We present NEST, a network-, compute-, and memory-a

### AI 总结

**概述**：NEST 是一个网络、计算和内存感知的设备放置框架，通过动态规划统一优化分布式深度学习并行策略。

**核心贡献**：
- 提出联合感知网络、计算和内存的设备放置框架，解决现有方法分离优化的问题
- 定义涵盖张量、流水线、数据和专家并行的原则性混合策略搜索空间
- 在多样硬件下实现最高 2.43 倍吞吐量提升，优于现有最先进基线

**技术要点**：
- 基于结构化动态规划，在算子图上处理多种并行配置及内存可行性
- 显式建模层级或任意网络拓扑下的通信延迟与计算内存配置文件

**应用场景**：分布式深度学习训练、数据中心网络协同设计、大规模 AI 基础设施优化

---

## 7. Word Recovery in Large Language Models Enables Character-Level Tokenization Robustness

- **作者**: Zhipeng Yang, Shu Yang, Lijie Hu, Di Wang
- **发布日期**: 2026-03-11
- **链接**: [arXiv:2603.10771v1](https://arxiv.org/abs/2603.10771v1) | [PDF](https://arxiv.org/pdf/2603.10771v1)
- **分类**: cs.CL
- **含金量**: 7.8/40 分

### 摘要

Large language models (LLMs) trained with canonical tokenization exhibit surprising robustness to non-canonical inputs such as character-level tokenization, yet the mechanisms underlying this robustness remain unclear.

We study this phenomenon through mechanistic interpretability and identify a core process we term word recovery.

We first introduce a decoding-based method to detect word recovery, showing that hidden states reconstruct canonical word-level token identities from character-level inputs.

We then provide causal evidence by removing the corresponding subspace from hidden states, whi

### AI 总结

**概述**：论文揭示了大语言模型通过隐藏状态中的“单词恢复”机制，实现了对字符级分词输入的鲁棒性处理。

**核心贡献**：
- 提出“单词恢复”概念，解释模型从字符级输入重建标准词元身份的现象
- 提供因果证据，证明移除恢复子空间会显著降低下游任务性能
- 发现早期层中同词字符间的组内注意力对单词恢复至关重要

**技术要点**：
- 基于解码的方法检测隐藏状态中是否重建了标准词元身份
- 通过子空间移除和注意力掩码实验验证机制的因果性与关键层

**应用场景**：提升模型鲁棒性、机制可解释性研究、分词策略优化

---

## 8. Shopping Companion: A Memory-Augmented LLM Agent for Real-World E-Commerce Tasks

- **作者**: Zijian Yu, Kejun Xiao, Huaipeng Zhao, Tao Luo, Xiaoyi Zeng
- **发布日期**: 2026-03-16
- **链接**: [arXiv:2603.14864v1](https://arxiv.org/abs/2603.14864v1) | [PDF](https://arxiv.org/pdf/2603.14864v1)
- **分类**: cs.CL
- **含金量**: 7.5/40 分

### 摘要

In e-commerce, LLM agents show promise for shopping tasks such as recommendations, budgeting, and bundle deals, where accurately capturing user preferences from long-term conversations is critical.

However, two challenges hinder realizing this potential: (1) the absence of benchmarks for evaluating long-term preference-aware shopping tasks, and (2) the lack of end-to-end optimization due to existing designs that treat preference identification and shopping assistance as separate components.

In this paper, we introduce a novel benchmark with a long-term memory setup, spanning two shopping tasks

### AI 总结

**概述**：论文提出 Shopping Companion 框架及长程记忆基准，通过统一优化和强化学习解决电商长期偏好捕捉难题。

**核心贡献**：
- 提出包含长程记忆设置的新基准，涵盖两任务及 120 万真实商品
- 设计 Shopping Companion 统一框架，联合优化记忆检索与购物协助
- 开发双奖励强化学习策略，解决多轮交互中奖励稀疏问题

**技术要点**：
- 统一框架设计：联合处理记忆检索与购物协助，支持用户干预
- 双奖励强化学习：采用工具级奖励策略，处理多轮交互中的稀疏奖励

**应用场景**：商品推荐、预算规划、组合优惠

---

## 9. From $\boldsymbol{\logπ}$ to $\boldsymbolπ$: Taming Divergence in Soft Clipping via Bilateral Decoupled Decay of Probability Gradient Weight

- **作者**: Xiaoliang Fu, Jiaye Lin, Yangyi Fang, Chaowen Hu, Cong Qin
- **发布日期**: 2026-03-15
- **链接**: [arXiv:2603.14389v1](https://arxiv.org/abs/2603.14389v1) | [PDF](https://arxiv.org/pdf/2603.14389v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 7.5/40 分

### 摘要

Reinforcement Learning with Verifiable Rewards (RLVR) has catalyzed a leap in Large Language Model (LLM) reasoning, yet its optimization dynamics remain fragile.

Standard algorithms like GRPO enforce stability via ``hard clipping'', which inadvertently stifles exploration by discarding gradients of tokens outside the trust region.

While recent ``soft clipping'' methods attempt to recover these gradients, they suffer from a critical challenge: relying on log-probability gradient ($\nabla_θ\log π_θ$) yields divergent weights as probabilities vanish, destabilizing LLM training.

We rethink this co

### AI 总结

**概述**：本文提出 DGPO 方法，以概率梯度替代对数概率梯度，解决软裁剪发散，提升 RLVR 训练稳定性与探索。

**核心贡献**：
- 揭示软裁剪依赖对数概率梯度导致概率趋零时权重发散的问题。
- 提出 DGPO 方法，确立概率梯度为更优优化原语并设计解耦衰减机制。
- 在多种模型规模的数学基准测试中，性能持续优于强基线方法。

**技术要点**：
- 采用概率梯度替代传统的对数概率梯度作为优化基础。
- 基于重要性采样比率实施双侧解耦衰减，对边界令牌不对称连续衰减。

**应用场景**：大语言模型推理、可验证奖励强化学习、数学问题求解

---

## 10. HTMuon: Improving Muon via Heavy-Tailed Spectral Correction

- **作者**: Tianyu Pang, Yujie Fang, Zihang Liu, Shenyang Deng, Lei Hsiung
- **发布日期**: 2026-03-10
- **链接**: [arXiv:2603.10067v1](https://arxiv.org/abs/2603.10067v1) | [PDF](https://arxiv.org/pdf/2603.10067v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 7.5/40 分

### 摘要

Muon has recently shown promising results in LLM training.

In this work, we study how to further improve Muon.

We argue that Muon's orthogonalized update rule suppresses the emergence of heavy-tailed weight spectra and over-emphasizes the training along noise-dominated directions.

Motivated by the Heavy-Tailed Self-Regularization (HT-SR) theory, we propose HTMuon.

HTMuon preserves Muon's ability to capture parameter interdependencies while producing heavier-tailed updates and inducing heavier-tailed weight spectra.

Experiments on LLM pretraining and image classification show that HTMuon consis

### AI 总结

**概述**：本文提出 HTMuon 优化器，通过重尾谱修正改进 Muon，在 LLM 预训练及图像分类任务中显著提升性能。

**核心贡献**：
- 指出 Muon 正交化更新抑制重尾权重谱及过度强调噪声方向的问题。
- 提出 HTMuon 方法，产生更重尾的更新和权重谱，同时保留参数依赖捕捉能力。
- 实验显示其在 LLM 预训练和图像分类上优于基线，并提供理论收敛性分析。

**技术要点**：
- 基于重尾自正则化（HT-SR）理论引入谱修正机制。
- 理论上对应 Schatten-q 范数约束下的最速下降优化。

**应用场景**：LLM 预训练、图像分类

---

