# 大数据+AI 领域论文日报

**日期**: 2026-07-20

**论文数量**: 6 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Understanding Reasoning from Pretra...](https://arxiv.org/abs/2607.16097v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Adaptive Fault Injection Planning f...](https://arxiv.org/abs/2607.16161v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [LLM Latent Edge Measurement: Point-...](https://arxiv.org/abs/2607.15640v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Robust Monitoring of Arc Welding Pr...](https://arxiv.org/abs/2607.16013v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [NeuralActuator: Neural Actuation Mo...](https://arxiv.org/abs/2607.11734v2) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Cura 1T: Specialized Model for Agen...](https://arxiv.org/abs/2607.15314v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Understanding Reasoning from Pretraining to Post-Training

- **作者**: Jingyan Shen, Ang Li, Salman Rahman, Yifan Sun, Micah Goldblum
- **发布日期**: 2026-07-17
- **链接**: [arXiv:2607.16097v1](https://arxiv.org/abs/2607.16097v1) | [PDF](https://arxiv.org/pdf/2607.16097v1)
- **分类**: cs.LG, cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

Reinforcement learning (RL) has become central to improving large language models (LLMs) on complex reasoning tasks, yet RL post-training is largely studied in isolation from the pretraining that precedes it.

As a result, two basic questions remain open: (1) how do pretraining choices (model size, data) shape the returns to RL compute, and (2) what does RL actually do to the model? These questions are difficult to study in the standard LLM setting: pretraining corpora are vast and uncontrolled, making it hard to attribute behaviors to pretraining versus RL, and systematic compute sweeps across

### AI 总结

总结生成失败

---

## 2. Adaptive Fault Injection Planning for Multi-Layer Self-Healing AI Infrastructure

- **作者**: Saurabh Kulkarni, Yuxin Yang, Rohan Kulkarni, Gautam Nayak
- **发布日期**: 2026-07-17
- **链接**: [arXiv:2607.16161v1](https://arxiv.org/abs/2607.16161v1) | [PDF](https://arxiv.org/pdf/2607.16161v1)
- **分类**: cs.ET
- **含金量**: 20/43 分

### 摘要

Modern GPU-accelerator platforms rely on multi-layer self-healing pipelines that span hardware, firmware, management software, and orchestration.

When faults propagate across layer boundaries, they can bypass detection, corrupt diagnosis, or trigger conflicting remediations--yet conventional fault-injection campaigns test each layer in isolation.

We present ADA-ST, an adaptive fault-injection methodology that uses a weighted fault-propagation graph to guide cross-layer scenario selection.

We construct four-layer graphs for three successive platforms at a hyperscale operator: Alpha, Beta, and G

### AI 总结

总结生成失败

---

## 3. LLM Latent Edge Measurement: Point-in-Time Economic Graphs for Quantitative Investing from Corporate Disclosures

- **作者**: Fan Yang, Lin Zhang
- **发布日期**: 2026-07-17
- **链接**: [arXiv:2607.15640v1](https://arxiv.org/abs/2607.15640v1) | [PDF](https://arxiv.org/pdf/2607.15640v1)
- **分类**: stat.AP
- **含金量**: 20/43 分

### 摘要

Standard industry classification systems such as GICS assign each firm to a single sector, but the economic relationships through which shocks propagate, such as supplier agreements, customer concentration, intellectual property licensing, cloud service dependencies, and power purchase contracts frequently cross sector boundaries and are often disclosed only in unstructured text.

We formulate the construction of a firm-level adjacency matrix as a measurement problem and propose an LLM based pipeline that extracts a weighted, directed, point in time corporate network from public disclosures.



### AI 总结

总结生成失败

---

## 4. Robust Monitoring of Arc Welding Processes: A Generalizable Framework with DVAE and Particle Filter

- **作者**: Yue Cao, Hai Lin, YuMing Zhang
- **发布日期**: 2026-07-17
- **链接**: [arXiv:2607.16013v1](https://arxiv.org/abs/2607.16013v1) | [PDF](https://arxiv.org/pdf/2607.16013v1)
- **分类**: eess.IV
- **含金量**: 20/43 分

### 摘要

Arc welding processes are essential for continuous fabrication but prone to disturbances that impair weld quality, making real-time monitoring critical yet difficult due to complex visual patterns and nonlinear, time-varying dynamics.

Deep learning shows promise but faces scalability limits because of its dependence on large labeled datasets and application-specific tuning.

We explore whether a unified approach can characterize major arc welding processes across applications and improve scalability through consistent state monitoring.

This paper introduces a robust and generalizable monitoring

### AI 总结

总结生成失败

---

## 5. NeuralActuator: Neural Actuation Modeling for Robot Dynamics and External Force Perception

- **作者**: Zhiyang Dou, John U. Onyemelukwe, Hangxing Zhang, Heng Zhang, Minghao Guo
- **发布日期**: 2026-07-13
- **链接**: [arXiv:2607.11734v2](https://arxiv.org/abs/2607.11734v2) | [PDF](https://arxiv.org/pdf/2607.11734v2)
- **分类**: cs.RO, cs.CV, cs.GR, cs.LG
- **含金量**: 20/43 分

### 摘要

Differentiable simulators have advanced policy learning and model-based control across robotic tasks.

Yet actuator dynamics remain underexplored and can be a major source of sim-to-real error, particularly on low-cost platforms, where the linear current-to-joint-torque approximation $τ= K_t I$ becomes unreliable because of friction, hysteresis, backlash, and thermal effects.

Accurate actuator models can also support force perception and integrated force/position control.

We present NeuralActuator, which jointly predicts (i) a torque surrogate for trajectory propagation on low-cost servo platfo

### AI 总结

总结生成失败

---

## 6. Cura 1T: Specialized Model for Agentic Healthcare

- **作者**: actAVA AI,  :, Haolin Chen, Leon Qi, Steve Brown
- **发布日期**: 2026-07-15
- **链接**: [arXiv:2607.15314v1](https://arxiv.org/abs/2607.15314v1) | [PDF](https://arxiv.org/pdf/2607.15314v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

Healthcare spans high-stakes communication, expert reasoning, and workflow execution, yet specialized LLMs that cover these use cases together remain limited.

A healthcare model must handle patient consultation, clinical reasoning over text and images, interactive diagnosis, and electronic health record (EHR) tool use.

These capabilities fail in different ways, and a narrow update for one task can degrade another.

We present Cura 1T, a healthcare-specialized LLM trained through a human-gated self-evolution loop.

In each evolution round, a training agent plans a target capability, trains the mo

### AI 总结

总结生成失败

---

