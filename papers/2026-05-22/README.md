# 大数据+AI 领域论文日报

**日期**: 2026-05-22

**论文数量**: 4 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [TransitLM: A Large-Scale Dataset an...](https://arxiv.org/abs/2605.22355v1) | 待分析 | 评估失败 | [Code](https://github.com/HotTricker/TransitLM.) | 20/43 |
| 2 | [LLM-Metrics: Measuring Research Imp...](https://arxiv.org/abs/2605.22176v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [LiveR: Fine-Grained Elasticity via ...](https://arxiv.org/abs/2605.22014v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [MambaGaze: Bidirectional Mamba with...](https://arxiv.org/abs/2605.22775v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. TransitLM: A Large-Scale Dataset and Benchmark for Map-Free Transit Route Generation

- **作者**: Hanyu Guo, Jiedong Yang, Chao Chen, Longfei Xu, Kaikui Liu
- **发布日期**: 2026-05-21
- **链接**: [arXiv:2605.22355v1](https://arxiv.org/abs/2605.22355v1) | [PDF](https://arxiv.org/pdf/2605.22355v1)
- **分类**: cs.CL, cs.AI, cs.LG
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/HotTricker/TransitLM.) ⭐ 0

### 摘要

Public transit route planning traditionally depends on structured map infrastructure and complex routing engines, and no existing dataset supports training models to bypass this dependency.

We present TransitLM, a large-scale dataset of over 13 million transit route planning records from four Chinese cities covering 120,845 stations and 13,666 lines, released as a continual pre-training corpus and benchmark data for three evaluation tasks with complementary metrics.

Experiments show that an LLM trained on TransitLM produces structurally valid routes at high accuracy and implicitly grounds arbi

### AI 总结

总结生成失败

---

## 2. LLM-Metrics: Measuring Research Impact Through Large Language Model Memory

- **作者**: Si Shen, Wenhua Zhao, Danhao Zhu
- **发布日期**: 2026-05-21
- **链接**: [arXiv:2605.22176v1](https://arxiv.org/abs/2605.22176v1) | [PDF](https://arxiv.org/pdf/2605.22176v1)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

Citation counts remain the dominant metric for assessing research impact, yet they suffer from well-documented limitations: temporal lag, disciplinary bias, and Matthew effects.

Here we propose LLM-Metrics, a research-impact assessment metric derived from the parametric memory of large language models (LLMs).

The central hypothesis is that high-impact papers receive greater exposure in the academic community, that this exposure enters LLM training data in textual form, and that models consequently form stronger parametric memory of these papers.

We designed four types of multiple-choice probes

### AI 总结

总结生成失败

---

## 3. LiveR: Fine-Grained Elasticity via Live Reconfiguration for Model Training

- **作者**: Haoyuan Liu, Kairui Zhou, Shuyao Qi, Qinwei Yang, Shengkai Lin
- **发布日期**: 2026-05-21
- **链接**: [arXiv:2605.22014v1](https://arxiv.org/abs/2605.22014v1) | [PDF](https://arxiv.org/pdf/2605.22014v1)
- **分类**: cs.DC
- **含金量**: 20/43 分

### 摘要

To reduce user costs and maximize cluster utilization, large model training increasingly leverages volatile but inexpensive GPU capacity, such as spot instances and reclaimable resources in shared clusters.

Yet, capitalizing on these economic benefits requires jobs to adapt within the short warning windows that many such environments provide.

Existing elastic training systems still treat reconfiguration as stop-and-restart: they externalize distributed state through checkpoints, rebuild the distributed runtime on a new topology, and restart training, turning each resize event into a storage-he

### AI 总结

总结生成失败

---

## 4. MambaGaze: Bidirectional Mamba with Explicit Missing Data Modeling for Cognitive Load Assessment from Eye-Gaze Tracking Data

- **作者**: Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh, Mimi Xie, Rocky Slavin
- **发布日期**: 2026-05-21
- **链接**: [arXiv:2605.22775v1](https://arxiv.org/abs/2605.22775v1) | [PDF](https://arxiv.org/pdf/2605.22775v1)
- **分类**: cs.LG, cs.AI, cs.HC
- **含金量**: 20/43 分

### 摘要

Real-time cognitive load assessment from eye-tracking signals could potentially enable adaptive human-centered-AI such as safety-critical applications such as driver vigilance monitoring or automated flight deck assistance, yet two challenges persist: handling frequent data missingness from blinks and tracking failures, and efficiently modeling long-range temporal dependencies.

We propose MambaGaze, a framework that addresses these challenges through 1) XMD encoding, which augments raw features with observation masks and time-deltas to explicitly model data uncertainty, and 2) bidirectional Ma

### AI 总结

总结生成失败

---

