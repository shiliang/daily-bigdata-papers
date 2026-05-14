# 大数据+AI 领域论文日报

**日期**: 2026-05-14

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Avoiding Cross-Datacenter Collectiv...](https://arxiv.org/abs/2605.11852v2) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Recasting AI Data Centers as Engine...](https://arxiv.org/abs/2605.13114v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [VectorSmuggle: Steganographic Exfil...](https://arxiv.org/abs/2605.13764v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Polyhedral Instability Governs Regr...](https://arxiv.org/abs/2605.13692v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [MinT: Managed Infrastructure for Tr...](https://arxiv.org/abs/2605.13779v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Toward Communication-Efficient Spac...](https://arxiv.org/abs/2605.12681v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Carbon-Aware Compute--Power Schedul...](https://arxiv.org/abs/2605.03751v2) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [Don't Be a Pot Stirrer! Authorized ...](https://arxiv.org/abs/2605.01342v2) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [From Heuristics to Analytics: Forec...](https://arxiv.org/abs/2605.12788v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Profit Maximization in Bilateral Tr...](https://arxiv.org/abs/2605.12664v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Avoiding Cross-Datacenter Collective Congestion via Disaggregated Buffering

- **作者**: Mariano Scazzariello, Noga H. Rotman, Dima Gavrilenko, Sajy Khashab, Alexander Shpiner
- **发布日期**: 2026-05-12
- **链接**: [arXiv:2605.11852v2](https://arxiv.org/abs/2605.11852v2) | [PDF](https://arxiv.org/pdf/2605.11852v2)
- **分类**: cs.NI
- **含金量**: 20/43 分

### 摘要

LLM training at the scale of tens of thousands of GPUs now spans multiple datacenters (DC), making cross-DC collectives over long-haul links unavoidable.

A critical and overlooked bottleneck arises when these collectives collide with intra-DC traffic at the destination - a common pattern in real workloads.

The multi-millisecond congestion control loop is too slow to react, triggering severe packet loss and congestion collapse.

We present Spillway, a transparent in-network mechanism that buffers dropped packets in switch-disaggregated buffers in a destination data center and drains them once 

### AI 总结

总结生成失败

---

## 2. Recasting AI Data Centers as Engines for Carbon Removal

- **作者**: Zhicong Fang, Boyu Zhang, Jin Shang, Jiaze Ma
- **发布日期**: 2026-05-13
- **链接**: [arXiv:2605.13114v1](https://arxiv.org/abs/2605.13114v1) | [PDF](https://arxiv.org/pdf/2605.13114v1)
- **分类**: math.OC
- **含金量**: 20/43 分

### 摘要

AI data centers (AIDCs) are rapidly increasing electricity demand and associated CO2 emissions, yet they also generate continuous low-grade waste heat.

Here, we assess whether this heat can be upgraded by heat pumps to drive direct air capture (DAC) and reduce the climate impact of AI infrastructure.

We develop a thermodynamically integrated DAC-AIDC system and conduct a region-resolved assessment across the United States, accounting for AIDC capacity, server composition, local climate, electricity prices, and grid carbon intensity.

We find that AIDC waste heat can substantially improve net CO

### AI 总结

总结生成失败

---

## 3. VectorSmuggle: Steganographic Exfiltration in Embedding Stores and a Cryptographic Provenance Defense

- **作者**: Jascha Wanger
- **发布日期**: 2026-05-13
- **链接**: [arXiv:2605.13764v1](https://arxiv.org/abs/2605.13764v1) | [PDF](https://arxiv.org/pdf/2605.13764v1)
- **分类**: cs.CR, cs.IR, cs.LG
- **含金量**: 20/43 分

### 摘要

Modern retrieval-augmented generation (RAG) systems convert sensitive content into high-dimensional embeddings and store them in vector databases that treat the resulting numerical artifacts as opaque.

Major vector-store products do not provide native controls for embedding integrity, ingestion-time distributional anomaly detection, or cryptographic provenance attestation.

We show this opens a class of steganographic exfiltration attacks: an attacker with write access to the ingestion pipeline can hide payload data inside embeddings using simple post-embedding perturbations (noise injection, r

### AI 总结

总结生成失败

---

## 4. Polyhedral Instability Governs Regret in Online Learning

- **作者**: Yuetai Li, Fengqing Jiang, Yichen Feng, Kaiyuan Zheng, Luyao Niu
- **发布日期**: 2026-05-13
- **链接**: [arXiv:2605.13692v1](https://arxiv.org/abs/2605.13692v1) | [PDF](https://arxiv.org/pdf/2605.13692v1)
- **分类**: cs.LG, cs.CC
- **含金量**: 20/43 分

### 摘要

Many online decision problems over combinatorial actions are addressed via convex relaxations, leading to online convex optimization with piecewise linear objectives and induced polyhedral structure.

We show that regret in such problems is governed by \emph{polyhedral instability}: the number of changes of the active region.

Under full information feedback and fixed partition assumptions, if $\mathrm{RS}_T$ denotes the number of region switches and $V_{\max}$ the maximum number of vertices per region, we prove $\Regret_T= Θ(\sqrt{(1+\mathrm{RS}_T)\,T\,\log V_{\max}})$ interpolating between exp

### AI 总结

总结生成失败

---

## 5. MinT: Managed Infrastructure for Training and Serving Millions of LLMs

- **作者**: Mind Lab, :, Song Cao, Vic Cao, Andrew Chen
- **发布日期**: 2026-05-13
- **链接**: [arXiv:2605.13779v1](https://arxiv.org/abs/2605.13779v1) | [PDF](https://arxiv.org/pdf/2605.13779v1)
- **分类**: cs.LG, cs.AI, cs.DC
- **含金量**: 20/43 分

### 摘要

We present MindLab Toolkit (MinT), a managed infrastructure system for Low-Rank Adaptation (LoRA) post-training and online serving.

MinT targets a setting where many trained policies are produced over a small number of expensive base-model deployments.

Instead of materializing each policy as a merged full checkpoint, MinT keeps the base model resident and moves exported LoRA adapter revisions through rollout, update, export, evaluation, serving, and rollback, hiding distributed training, serving, scheduling, and data movement behind a service interface.

MinT scales this path along three axes.



### AI 总结

总结生成失败

---

## 6. Toward Communication-Efficient Space Data Centers: Bottlenecks, Architectures, and New Paradigms

- **作者**: Minghao Sun, Zehui Chen, Jinbo Hou, Kezhi Wang, Xiaoli Chu
- **发布日期**: 2026-05-12
- **链接**: [arXiv:2605.12681v1](https://arxiv.org/abs/2605.12681v1) | [PDF](https://arxiv.org/pdf/2605.12681v1)
- **分类**: cs.NI
- **含金量**: 20/43 分

### 摘要

The rapid growth of foundation model training and large-scale AI services has driven ground data centers toward unprecedented power densities, intensifying challenges in energy supply, cooling, and spatial scalability.

Space Data Centers (SDCs) have emerged as a promising paradigm for hosting energy-intensive computing infrastructures in orbit, leveraging continuous solar energy and radiative cooling advantages.

However, unlike ground facilities primarily constrained by power and site availability, SDCs are fundamentally limited by communication capability.

The gap between petabit-scale intern

### AI 总结

总结生成失败

---

## 7. Carbon-Aware Compute--Power Scheduling for AI Data Centers with Microgrid Prosumer Operations

- **作者**: Johnny R. Zhang, Gaoyuan Du, Qianyi Sun, Shiqi Wang, Jiaxuan Li
- **发布日期**: 2026-05-05
- **链接**: [arXiv:2605.03751v2](https://arxiv.org/abs/2605.03751v2) | [PDF](https://arxiv.org/pdf/2605.03751v2)
- **分类**: cs.CE
- **含金量**: 20/43 分

### 摘要

AI data centers are increasingly becoming tightly coupled compute--energy systems, where workload placement, cooling demand, electricity procurement, storage operation, and carbon emissions interact over time.

This paper studies carbon-aware compute--power scheduling for geographically distributed AI data centers with microgrid prosumer capabilities.

We propose a mixed-integer linear programming (MILP) framework that jointly schedules rigid training jobs, routes elastic inference workloads, dispatches local generation and battery storage, and manages bidirectional grid interaction under latenc

### AI 总结

总结生成失败

---

## 8. Don't Be a Pot Stirrer! Authorized Vector Data Retrieval via Access-Aware Indexing

- **作者**: Shanshan Han, Vishal Chakraborty, Sharad Mehrotra
- **发布日期**: 2026-05-02
- **链接**: [arXiv:2605.01342v2](https://arxiv.org/abs/2605.01342v2) | [PDF](https://arxiv.org/pdf/2605.01342v2)
- **分类**: cs.DB
- **含金量**: 20/43 分

### 摘要

Vector databases increasingly enforce role-based access control, where each top-k approximate nearest neighbor query must return only vectors the querying role is authorized to access.

Two extremes bracket the design space.

A single global index built over all vectors avoids duplication but wastes search effort on unauthorized vectors and degrades recall, while an oracle index, built with all authorized vectors to the query roles, searches only authorized vectors but duplicates every shared vector between roles or queries.

We present Veda and its efficient variant EffVeda, two indexing strateg

### AI 总结

总结生成失败

---

## 9. From Heuristics to Analytics: Forecasting Effort and Progress in Online Learning

- **作者**: Eric S. Qiu, Danielle R. Thomas, Boyuan Guo, Vincent Aleven, Conrad Borchers
- **发布日期**: 2026-05-12
- **链接**: [arXiv:2605.12788v1](https://arxiv.org/abs/2605.12788v1) | [PDF](https://arxiv.org/pdf/2605.12788v1)
- **分类**: cs.LG, cs.CY
- **含金量**: 20/43 分

### 摘要

Sustained effort is essential for realizing the benefits of intelligent tutoring systems (ITS), yet many learners disengage or underuse available practice time.

We introduce engagement forecasting as a supervised prediction task based on ITS logs, targeting two outcomes central to effort and learning progress: minutes practiced per week and new skills mastered per week.

Using interaction log data from 425 middle-school students over a school year, we benchmark fifteen predictors including regressions, decision trees, and neural networks.

We show that these feature-based models reduce mean abso

### AI 总结

总结生成失败

---

## 10. Profit Maximization in Bilateral Trade against a Smooth Adversary

- **作者**: Simone Di Gregorio, Paul Dütting, Federico Fusco, Chris Schwiegelshohn
- **发布日期**: 2026-05-12
- **链接**: [arXiv:2605.12664v1](https://arxiv.org/abs/2605.12664v1) | [PDF](https://arxiv.org/pdf/2605.12664v1)
- **分类**: cs.GT, cs.LG
- **含金量**: 20/43 分

### 摘要

Bilateral trade models the task of intermediating between two strategic agents, a seller and a buyer, who wish to trade a good.

We study this problem from the perspective of a profit-maximizing broker within an online learning framework, where the agents' valuations are generated by a smooth adversary.

We devise a learning algorithm that guarantees a $\tilde{O}(\sqrt{T})$ regret bound, which is tight in the time horizon $T$ up to poly-logarithmic factors.

This matches the minimax rate for the stochastic i.i.d.

case, and is also well separated from the adversarial setting, where sublinear-reg

### AI 总结

总结生成失败

---

