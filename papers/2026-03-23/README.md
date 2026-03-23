# 大数据+AI 领域论文日报

**日期**: 2026-03-23

**论文数量**: 4 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Regret Analysis of Sleeping Competi...](https://arxiv.org/abs/2603.19700v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Dual-Domain Representation Alignmen...](https://arxiv.org/abs/2603.19563v1) | 待分析 | 评估失败 | [Code](https://github.com/EMI-Group/evonas) | 20/43 |
| 3 | [SOFTMAP: Sim2Real Soft Robot Forwar...](https://arxiv.org/abs/2603.19384v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Stochastic Sequential Decision Maki...](https://arxiv.org/abs/2603.19501v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Regret Analysis of Sleeping Competing Bandits

- **作者**: Shinnosuke Uba, Yutaro Yamaguchi
- **发布日期**: 2026-03-20
- **链接**: [arXiv:2603.19700v1](https://arxiv.org/abs/2603.19700v1) | [PDF](https://arxiv.org/pdf/2603.19700v1)
- **分类**: cs.LG, cs.GT
- **含金量**: 20/43 分

### 摘要

The Competing Bandits framework is a recently emerging area that integrates multi-armed bandits in online learning with stable matching in game theory.

While conventional models assume that all players and arms are constantly available, in real-world problems, their availability can vary arbitrarily over time.

In this paper, we formulate this setting as Sleeping Competing Bandits.

To analyze this problem, we naturally extend the regret definition used in existing competing bandits and derive regret bounds for the proposed model.

We propose an algorithm that simultaneously achieves an asymptoti

### AI 总结

总结生成失败

---

## 2. Dual-Domain Representation Alignment: Bridging 2D and 3D Vision via Geometry-Aware Architecture Search

- **作者**: Haoyu Zhang, Zhihao Yu, Rui Wang, Yaochu Jin, Qiqi Liu
- **发布日期**: 2026-03-20
- **链接**: [arXiv:2603.19563v1](https://arxiv.org/abs/2603.19563v1) | [PDF](https://arxiv.org/pdf/2603.19563v1)
- **分类**: cs.CV, cs.AI
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/EMI-Group/evonas) ⭐ 0 (Python)

### 摘要

Modern computer vision requires balancing predictive accuracy with real-time efficiency, yet the high inference cost of large vision models (LVMs) limits deployment on resource-constrained edge devices.

Although Evolutionary Neural Architecture Search (ENAS) is well suited for multi-objective optimization, its practical use is hindered by two issues: expensive candidate evaluation and ranking inconsistency among subnetworks.

To address them, we propose EvoNAS, an efficient distributed framework for multi-objective evolutionary architecture search.

We build a hybrid supernet that integrates Vis

### AI 总结

总结生成失败

---

## 3. SOFTMAP: Sim2Real Soft Robot Forward Modeling via Topological Mesh Alignment and Physics Prior

- **作者**: Ziyong Ma, Uksang Yoo, Jonathan Francis, Weiming Zhi, Jeffrey Ichnowski
- **发布日期**: 2026-03-19
- **链接**: [arXiv:2603.19384v1](https://arxiv.org/abs/2603.19384v1) | [PDF](https://arxiv.org/pdf/2603.19384v1)
- **分类**: cs.RO
- **含金量**: 20/43 分

### 摘要

While soft robot manipulators offer compelling advantages over rigid counterparts, including inherent compliance, safe human-robot interaction, and the ability to conform to complex geometries, accurate forward modeling from low-dimensional actuation commands remains an open challenge due to nonlinear material phenomena such as hysteresis and manufacturing variability.

We present SOFTMAP, a sim-to-real learning framework for real-time 3D forward modeling of tendon-actuated soft finger manipulators.

SOFTMAP combines four components: (1) As-Rigid-As-Possible (ARAP)-based topological alignment th

### AI 总结

总结生成失败

---

## 4. Stochastic Sequential Decision Making over Expanding Networks with Graph Filtering

- **作者**: Zhan Gao, Bishwadeep Das, Elvin Isufi
- **发布日期**: 2026-03-19
- **链接**: [arXiv:2603.19501v1](https://arxiv.org/abs/2603.19501v1) | [PDF](https://arxiv.org/pdf/2603.19501v1)
- **分类**: cs.LG, eess.SP
- **含金量**: 20/43 分

### 摘要

Graph filters leverage topological information to process networked data with existing methods mainly studying fixed graphs, ignoring that graphs often expand as nodes continually attach with an unknown pattern.

The latter requires developing filter-based decision-making paradigms that take evolution and uncertainty into account.

Existing approaches rely on either pre-designed filters or online learning, limited to a myopic view considering only past or present information.

To account for future impacts, we propose a stochastic sequential decision-making framework for filtering networked data 

### AI 总结

总结生成失败

---

