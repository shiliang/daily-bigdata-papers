# 大数据+AI 领域论文日报

**日期**: 2026-03-20

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Efficient Exploration at Scale](https://arxiv.org/abs/2603.17378v1) | 提出了一种显著改善 RLHF 数据效率的在线学习算法。 | 该论文提出结合不确定性建模与信息导向探索的在线 RLHF 算 | 无 | 8.8/43 |
| 2 | [Artificial intelligence-enabled sin...](https://arxiv.org/abs/2603.14177v2) | 开发了基于 ECGFounder 基础模型微调的 Pocke | 该研究利用基础模型微调单导联 ECG 实现高钾血症无创筛查， | 无 | 8.5/43 |
| 3 | [Real-Time Online Learning for Model...](https://arxiv.org/abs/2603.17632v1) | 提出了高效的近似时空高斯过程模型实现方案 | 该研究针对 GP-MPC 在线计算瓶颈提出了恒定复杂度的时空 | 无 | 8.3/43 |
| 4 | [Online Learning for Supervisory Swi...](https://arxiv.org/abs/2603.14762v2) | 提出了监督控制的新型非渐近分析方法，弥补了经典方法缺乏有限时 | 该论文填补了经典监督控制与在线学习间的非渐近理论空白，尤其在 | 无 | 8.3/43 |
| 5 | [Articulated-Body Dynamics Network: ...](https://arxiv.org/abs/2603.19078v1) | 提出 ABDNet，将刚体动力学算法结构融入图神经网络作为策 | 该论文创新性地将经典动力学算法结构融入图神经网络，为机器人强 | 无 | 8/43 |
| 6 | [Online Learning and Equilibrium Com...](https://arxiv.org/abs/2603.19221v1) | 建立了仅观察动作排名的在线学习模型，涵盖瞬时与时间平均效用机 | 该论文创新性地引入排序反馈机制解决隐私与人机交互限制，理论框 | 无 | 8/43 |
| 7 | [FSMC-Pose: Frequency and Spatial Fu...](https://arxiv.org/abs/2603.16596v1) | 提出 FSMCPose 框架，集成轻量级频率空间融合骨干网与 | 面向畜牧养殖的特定场景优化，工程落地价值突出，但算法核心多为 | [有代码](link) | 8/43 |
| 8 | [RadarXFormer: Robust Object Detecti...](https://arxiv.org/abs/2603.14822v1) | 提出 RadarXFormer 框架，实现 4D 雷达频谱与 | 该研究针对 4D 雷达噪声与数据挑战，提出频谱与图像跨维度融 | 无 | 8.0/43 |
| 9 | [Ada3Drift: Adaptive Training-Time D...](https://arxiv.org/abs/2603.11984v1) | 提出 Ada3Drift 框架，实现从 3D 点云观察的高保 | 该论文利用训练 - 推理算力不对称性解决单步策略多模态坍塌问 | 无 | 8/43 |
| 10 | [Revisiting Bi-Encoder Neural Search...](https://arxiv.org/abs/2408.01094v2) | 分析了双编码器架构在所见数据集及零样本场景下的性能局限 | 该文从理论层面重构双编码器范式，提出编码搜索分离视角，对密集 | 无 | 8/43 |

---


## 1. Efficient Exploration at Scale

- **作者**: Seyed Mohammad Asghari, Chris Chute, Vikranth Dwaracherla, Xiuyuan Lu, Mehdi Jafarnia
- **发布日期**: 2026-03-18
- **链接**: [arXiv:2603.17378v1](https://arxiv.org/abs/2603.17378v1) | [PDF](https://arxiv.org/pdf/2603.17378v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 8.8/43 分

### 摘要

We develop an online learning algorithm that dramatically improves the data efficiency of reinforcement learning from human feedback (RLHF).

Our algorithm incrementally updates reward and language models as choice data is received.

The reward model is fit to the choice data, while the language model is updated by a variation of reinforce, with reinforcement signals provided by the reward model.

Several features enable the efficiency gains: a small affirmative nudge added to each reinforcement signal, an epistemic neural network that models reward uncertainty, and information-directed explorati

### AI 总结

**概述**：本文提出在线学习算法，大幅提升 RLHF 数据效率，少量标签即可匹配大规模离线训练效果。

**核心贡献**：
- 提出了一种显著改善 RLHF 数据效率的在线学习算法。
- 在 Gemma 模型上实现 10 倍以上数据效率增益，少标签匹配高性能。
- 首次证明算法优化可实现千倍级别数据效率提升的潜力。

**技术要点**：
- 增量更新奖励与语言模型，利用奖励模型信号通过 REINFORCE 变体优化语言模型。
- 结合肯定性微调、认知神经网络建模不确定性及信息导向探索以提升效率。

**应用场景**：人类反馈强化学习（RLHF）、大语言模型对齐、数据稀缺场景下的模型优化

---

## 2. Artificial intelligence-enabled single-lead ECG for non-invasive hyperkalemia detection: development, multicenter validation, and proof-of-concept deployment

- **作者**: Gongzheng Tang, Qinghao Zhao, Guangkun Nie, Yujie Xiao, Shijia Geng
- **发布日期**: 2026-03-15
- **链接**: [arXiv:2603.14177v2](https://arxiv.org/abs/2603.14177v2) | [PDF](https://arxiv.org/pdf/2603.14177v2)
- **分类**: cs.LG, cs.AI
- **含金量**: 8.5/43 分

### 摘要

Hyperkalemia is a life-threatening electrolyte disorder that is common in patients with chronic kidney disease and heart failure, yet frequent monitoring remains difficult outside hospital settings.

We developed and validated Pocket-K, a single-lead AI-ECG system initialized from the ECGFounder foundation model for non-invasive hyperkalemia screening and handheld deployment.

In this multicentre observational study using routinely collected clinical ECG and laboratory data, 34,439 patients contributed 62,290 ECG--potassium pairs.

Lead I data were used to fine-tune the model.

Data from Peking Un

### AI 总结

**概述**：本文开发并验证了 Pocket-K 系统，利用单导联 AI 心电图无创筛查高钾血症，支持手持设备部署。

**核心贡献**：
- 开发了基于 ECGFounder 基础模型微调的 Pocket-K 单导联 AI 心电图系统
- 在多中心数据集上验证了模型检测高钾血症的高准确性与负预测值
- 实现了手持原型部署，支持近实时推理，便于院外筛查

**技术要点**：
- 使用单导联（Lead I）心电图数据对基础模型进行微调
- 采用多中心观察性研究设计，包含内部、时间及外部验证集

**应用场景**：慢性肾病患者、心力衰竭患者、院外无创监测场景

---

## 3. Real-Time Online Learning for Model Predictive Control using a Spatio-Temporal Gaussian Process Approximation

- **作者**: Lars Bartels, Amon Lahr, Andrea Carron, Melanie N. Zeilinger
- **发布日期**: 2026-03-18
- **链接**: [arXiv:2603.17632v1](https://arxiv.org/abs/2603.17632v1) | [PDF](https://arxiv.org/pdf/2603.17632v1)
- **分类**: eess.SY, cs.RO, math.OC
- **含金量**: 8.3/43 分

### 摘要

Learning-based model predictive control (MPC) can enhance control performance by correcting for model inaccuracies, enabling more precise state trajectory predictions than traditional MPC.

A common approach is to model unknown residual dynamics as a Gaussian process (GP), which leverages data and also provides an estimate of the associated uncertainty.

However, the high computational cost of online learning poses a major challenge for real-time GP-MPC applications.

This work presents an efficient implementation of an approximate spatio-temporal GP model, offering online learning at constant co

### AI 总结

**概述**：本文提出时空高斯过程近似方法，实现模型预测控制实时在线学习，解决高计算成本挑战并提升控制性能。

**核心贡献**：
- 提出了高效的近似时空高斯过程模型实现方案
- 实现了具有恒定计算复杂度的实时在线学习功能
- 显著提升了实时控制性能，适用于时变系统动力学学习

**技术要点**：
- 采用高斯过程建模未知残差动力学并估计不确定性
- 优化时空高斯过程近似以支持恒定复杂度的在线更新

**应用场景**：自主微型赛车、时变系统实时控制

---

## 4. Online Learning for Supervisory Switching Control

- **作者**: Haoyuan Sun, Ali Jadbabaie
- **发布日期**: 2026-03-16
- **链接**: [arXiv:2603.14762v2](https://arxiv.org/abs/2603.14762v2) | [PDF](https://arxiv.org/pdf/2603.14762v2)
- **分类**: math.OC, cs.LG, eess.SY
- **含金量**: 8.3/43 分

### 摘要

We study supervisory switching control for partially-observed linear dynamical systems.

The objective is to identify and deploy the best controller for the unknown system by periodically selecting among a collection of $N$ candidate controllers, some of which may destabilize the underlying system.

While classical estimator-based supervisory control guarantees asymptotic stability, it lacks quantitative finite-time performance bounds.

Conversely, current non-asymptotic methods in both online learning and system identification require restrictive assumptions that are incompatible in a control se

### AI 总结

**概述**：本文提出基于多臂老虎机的监督切换控制算法，能在有限时间内为未知线性系统识别并部署最佳控制器。

**核心贡献**：
- 提出了监督控制的新型非渐近分析方法，弥补了经典方法缺乏有限时间性能界限的不足
- 设计了利用系统可观测性评分的数据驱动算法，能有效检测潜在不稳定控制器并进行系统识别
- 实现了维度无关的有限时间保证，以 O(N log N) 步数识别最佳控制器并确保有限 L2 增益

**技术要点**：
- 将多臂老虎机算法适配到控制理论设置中，允许测试潜在不稳定控制器
- 通过评分标准利用系统可观测性隔离状态历史效应，实现准确评估

**应用场景**：部分观测线性动态系统、未知系统的监督切换控制、多候选控制器选择场景

---

## 5. Articulated-Body Dynamics Network: Dynamics-Grounded Prior for Robot Learning

- **作者**: Sangwoo Shin, Kunzhao Ren, Xiaobin Xiong, Josiah Hanna
- **发布日期**: 2026-03-19
- **链接**: [arXiv:2603.19078v1](https://arxiv.org/abs/2603.19078v1) | [PDF](https://arxiv.org/pdf/2603.19078v1)
- **分类**: cs.RO
- **含金量**: 8/43 分

### 摘要

Recent work in reinforcement learning has shown that incorporating structural priors for articulated robots, such as link connectivity, into policy networks improves learning efficiency.

However, dynamics properties, despite their fundamental role in determining how forces and motion propagate through the body, remain largely underexplored as an inductive bias for policy learning.

To address this gap, we present the Articulated-Body Dynamics Network (ABD-Net), a novel graph neural network architecture grounded in the computational structure of forward dynamics.

Specifically, we adapt the inert

### AI 总结

**概述**：本文提出 ABD-Net，一种基于前向动力学结构的图神经网络，旨在提升机器人策略学习的效率与鲁棒性。

**核心贡献**：
- 提出 ABD-Net，将刚体动力学算法结构融入图神经网络作为策略先验。
- 在仿真实验中展现出比 Transformer 和 GNN 基线更高的样本效率与泛化能力。
- 在真实 Unitree G1 和 Go2 机器人上验证了动态、多功能且鲁棒的运动行为。

**技术要点**：
- 适配刚体算法中的惯性传播机制，以树状结构从子连杆向父连杆聚合惯性量。
- 用可学习参数替换物理量，使策略网络能够捕捉动作在身体中的传播方式。

**应用场景**：仿真人形机器人、四足机器人、单足跳跃机器人、虚实迁移控制

---

## 6. Online Learning and Equilibrium Computation with Ranking Feedback

- **作者**: Mingyang Liu, Yongshan Chen, Zhiyuan Fan, Gabriele Farina, Asuman Ozdaglar
- **发布日期**: 2026-03-19
- **链接**: [arXiv:2603.19221v1](https://arxiv.org/abs/2603.19221v1) | [PDF](https://arxiv.org/pdf/2603.19221v1)
- **分类**: cs.LG, cs.CL, cs.GT
- **含金量**: 8/43 分

### 摘要

Online learning in arbitrary, and possibly adversarial, environments has been extensively studied in sequential decision-making, and it is closely connected to equilibrium computation in game theory.

Most existing online learning algorithms rely on \emph{numeric} utility feedback from the environment, which may be unavailable in human-in-the-loop applications and/or may be restricted by privacy concerns.

In this paper, we study an online learning model in which the learner only observes a \emph{ranking} over a set of proposed actions at each timestep.

We consider two ranking mechanisms: rankin

### AI 总结

**概述**：本文研究仅基于动作排名反馈的在线学习，提出新算法实现次线性遗憾，并应用于博弈均衡与大模型路由。

**核心贡献**：
- 建立了仅观察动作排名的在线学习模型，涵盖瞬时与时间平均效用机制
- 证明了通用情况下次线性遗憾不可行，但在效用变化受限等条件下可实现
- 设计了新算法，使多玩家重复博弈收敛于近似粗相关均衡

**技术要点**：
- 分析了不同排名机制及信息设置下的遗憾理论界限
- 基于效用序列总变差次线性假设，设计了实现次线性遗憾的算法

**应用场景**：人机交互、隐私受限场景、博弈均衡计算、大语言模型路由

---

## 7. FSMC-Pose: Frequency and Spatial Fusion with Multiscale Self-calibration for Cattle Mounting Pose Estimation

- **作者**: Fangjing Li, Zhihai Wang, Xinxin Ding, Haiyang Liu, Ronghua Gao
- **发布日期**: 2026-03-17
- **链接**: [arXiv:2603.16596v1](https://arxiv.org/abs/2603.16596v1) | [PDF](https://arxiv.org/pdf/2603.16596v1)
- **分类**: cs.CV, cs.AI
- **含金量**: 8/43 分 (含代码+1分)
- **代码**: [GitHub](https://github.com/elianafang/FSMC-Pose.) ⭐ 0

### 摘要

Mounting posture is an important visual indicator of estrus in dairy cattle.

However, achieving reliable mounting pose estimation in real-world environments remains challenging due to cluttered backgrounds and frequent inter-animal occlusion.

We present FSMC-Pose, a top-down framework that integrates a lightweight frequency-spatial fusion backbone, CattleMountNet, and a multiscale self-calibration head, SC2Head.

Specifically, we design two algorithmic components for CattleMountNet: the Spatial Frequency Enhancement Block (SFEBlock) and the Receptive Aggregation Block (RABlock).

SFEBlock separa

### AI 总结

**概述**：本文提出 FSMC-Pose 框架，融合频率空间信息与多尺度自校准，实现复杂环境奶牛爬跨姿态估计。

**核心贡献**：
- 提出 FSMC-Pose 框架，集成轻量级频率空间融合骨干网与多尺度自校准头
- 构建 MOUNT-Cattle 数据集，含 1176 个爬跨实例，支持标准化训练
- 实现复杂环境下高精度实时估计，显著降低计算成本与参数量

**技术要点**：
- 设计 SFEBlock 与 RABlock，分别用于背景分离与多尺度上下文信息捕捉
- 提出 SC2Head，利用空间 - 通道自校准分支缓解互遮挡导致的结构错位

**应用场景**：奶牛发情监测、复杂养殖场环境监控、畜牧姿态估计

---

## 8. RadarXFormer: Robust Object Detection via Cross-Dimension Fusion of 4D Radar Spectra and Images for Autonomous Driving

- **作者**: Yue Sun, Yeqiang Qian, Zhe Wang, Tianhui Li, Chunxiang Wang
- **发布日期**: 2026-03-16
- **链接**: [arXiv:2603.14822v1](https://arxiv.org/abs/2603.14822v1) | [PDF](https://arxiv.org/pdf/2603.14822v1)
- **分类**: cs.CV
- **含金量**: 8.0/43 分

### 摘要

Reliable perception is essential for autonomous driving systems to operate safely under diverse real-world traffic conditions.

However, camera- and LiDAR-based perception systems suffer from performance degradation under adverse weather and lighting conditions, limiting their robustness and large-scale deployment in intelligent transportation systems.

Radar-vision fusion provides a promising alternative by combining the environmental robustness and cost efficiency of millimeter-wave (mmWave) radar with the rich semantic information captured by cameras.

Nevertheless, conventional 3D radar measu

### AI 总结

**概述**：本文提出 RadarXFormer，融合 4D 雷达频谱与图像，提升恶劣条件下自动驾驶目标检测鲁棒性。

**核心贡献**：
- 提出 RadarXFormer 框架，实现 4D 雷达频谱与 RGB 图像的高效跨模态融合
- 直接利用原始雷达频谱构建高效 3D 表示，减少数据量并保留完整空间信息
- 设计跨维度融合机制，将多尺度 3D 雷达特征立方体与 2D 图像特征图互补融合

**技术要点**：
- 摒弃稀疏点云，直接基于原始雷达频谱构建保留完整 3D 空间信息的高效表示
- 采用跨维度融合机制，将多尺度 3D 球形雷达特征立方体与 2D 图像特征图结合

**应用场景**：自动驾驶、恶劣天气感知、智能交通系统

---

## 9. Ada3Drift: Adaptive Training-Time Drifting for One-Step 3D Visuomotor Robotic Manipulation

- **作者**: Chongyang Xu, Yixian Zou, Ziliang Feng, Fanman Meng, Shuaicheng Liu
- **发布日期**: 2026-03-12
- **链接**: [arXiv:2603.11984v1](https://arxiv.org/abs/2603.11984v1) | [PDF](https://arxiv.org/pdf/2603.11984v1)
- **分类**: cs.CV
- **含金量**: 8/43 分

### 摘要

Diffusion-based visuomotor policies effectively capture multimodal action distributions through iterative denoising, but their high inference latency limits real-time robotic control.

Recent flow matching and consistency-based methods achieve single-step generation, yet sacrifice the ability to preserve distinct action modes, collapsing multimodal behaviors into averaged, often physically infeasible trajectories.

We observe that the compute budget asymmetry in robotics (offline training vs.\ real-time inference) naturally motivates recovering this multimodal fidelity by shifting iterative refi

### AI 总结

**概述**：本文提出 Ada3Drift，将迭代优化移至训练阶段，实现 3D 点云下的高保真单步视觉运动控制

**核心贡献**：
- 提出 Ada3Drift 框架，实现从 3D 点云观察的高保真单步动作生成
- 利用训练时漂移场吸引专家模式并排斥其他样本，恢复多模态行为保真度
- 在多个仿真及真实机器人任务中达到最先进性能，且计算效率比扩散方法高 10 倍

**技术要点**：
- 学习训练时漂移场，将迭代细化从推理时转移至训练时
- 引入 Sigmoid 调度损失过渡和多尺度场聚合，以适应少样本机器人场景

**应用场景**：仿真基准测试（Adroit、Meta-World、RoboTwin）、真实世界机器人操作任务

---

## 10. Revisiting Bi-Encoder Neural Search: An Encoding--Searching Separation Perspective

- **作者**: Hung-Nghiep Tran, Akiko Aizawa, Atsuhiro Takasu
- **发布日期**: 2024-08-02
- **链接**: [arXiv:2408.01094v2](https://arxiv.org/abs/2408.01094v2) | [PDF](https://arxiv.org/pdf/2408.01094v2)
- **分类**: cs.LG, cs.IR
- **含金量**: 8/43 分

### 摘要

This paper reviews, analyzes, and proposes a new perspective on the bi-encoder architecture for neural search.

While the bi-encoder architecture is widely used due to its simplicity and scalability at test time, it has some notable issues such as low performance on seen datasets and weak zero-shot performance on new datasets.

In this paper, we analyze these issues and summarize two main critiques: the encoding information bottleneck problem and limitations of the basic assumption of embedding search.

We then construct a thought experiment to logically analyze the encoding and searching operati

### AI 总结

**概述**：本文重新审视双编码器神经搜索，提出编码 - 搜索分离视角，分析问题根源并提出改进策略以提升性能。

**核心贡献**：
- 分析了双编码器架构在所见数据集及零样本场景下的性能局限
- 提出了编码 - 搜索分离视角，概念与实践上分离编码和搜索操作
- 基于新框架解释问题根源并提出策略，有望降低成本并提升检索性能

**技术要点**：
- 指出编码信息瓶颈问题是导致性能局限的原因之一
- 揭示嵌入搜索基本假设存在的局限性并通过思想实验进行挑战

**应用场景**：神经搜索、信息检索、双编码器架构优化

---

