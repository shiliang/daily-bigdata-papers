# 大数据+AI 领域论文日报

**日期**: 2026-06-17

**论文数量**: 8 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [From Trainee to Trainer: LLM-Design...](https://arxiv.org/abs/2606.17682v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [AI Adoption Across a Multinational ...](https://arxiv.org/abs/2606.17887v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [ConTex: Reformulating Counterfactua...](https://arxiv.org/abs/2606.18049v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [MaineCoon: Pursuing A Real-Time Aud...](https://arxiv.org/abs/2606.17800v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [RT-Counter: Real-Time Text-Guided O...](https://arxiv.org/abs/2606.17561v1) | 待分析 | 评估失败 | [Code](https://github.com/Jason-Mar1/RT-Counter.) | 20/43 |
| 6 | [Online LLM Selection via Constraine...](https://arxiv.org/abs/2606.17489v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [When the Next Step Is Not One Step:...](https://arxiv.org/abs/2606.17508v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [On the Memorization Behavior of LLM...](https://arxiv.org/abs/2606.17276v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. From Trainee to Trainer: LLM-Designed Training Environment for RL with Multi-Agent Reasoning

- **作者**: Chao Chen, Chengzu Li, Zhiwei Li, Yinhong Liu, Zhijiang Guo
- **发布日期**: 2026-06-16
- **链接**: [arXiv:2606.17682v1](https://arxiv.org/abs/2606.17682v1) | [PDF](https://arxiv.org/pdf/2606.17682v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

Reinforcement learning pipelines for Large Language Model (LLM) training often rely on manually redesigned environments between stages, requiring practitioners to heuristically infer which configuration will best improve the current policy.

To automate this process, we propose the LLM-as-Environment-Engineer framework in which the current policy model analyzes failure trajectories together with contextual information and proposes modifications to the next-stage training environment configuration.

We also introduce MAPF-FrozenLake, a controllable testbed whose generator exposes multi-dimensiona

### AI 总结

总结生成失败

---

## 2. AI Adoption Across a Multinational Workforce: Sociotechnical Conditions for GenAI Acceptance in Human Resources

- **作者**: Dalia Ali, Maria José Rodríguez Velázquez, Manoel Horta Ribeiro, Vera Liao, Orestis Papakyriakopoulos
- **发布日期**: 2026-06-16
- **链接**: [arXiv:2606.17887v1](https://arxiv.org/abs/2606.17887v1) | [PDF](https://arxiv.org/pdf/2606.17887v1)
- **分类**: cs.HC, cs.AI
- **含金量**: 20/43 分

### 摘要

Generative AI (GenAI) deployment in the workplace is accelerating rapidly.

Nevertheless, questions of who adopts, who benefits, and who is left behind and why are still understudied.

In this paper, we investigate these dynamics in the context of a multinational tech company transitioning from a legacy Human Resources (HR) search system to a GenAI-supported system, analyzing search log data, survey data (n=25), and ten semi-structured interviews.

Our findings show that adoption depended on the fit between the GenAI system's design assumptions and employees' work positionalities (role, spoken la

### AI 总结

总结生成失败

---

## 3. ConTex: Reformulating Counterfactual Generation For Time Series Forecasting

- **作者**: Jan Voets, Hasan Tercan, Tobias Meisen, Sebastian Baum
- **发布日期**: 2026-06-16
- **链接**: [arXiv:2606.18049v1](https://arxiv.org/abs/2606.18049v1) | [PDF](https://arxiv.org/pdf/2606.18049v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Decision-making with deep learning-based time series forecasting requires not only accurate predictions but also actionable insights.

However, current architectures do not inherently provide such information.

Specifically, guidance is needed on how current conditions must be modified to shift from a predicted outcome to a desired future scenario.

Counterfactual explanations provide a natural framework for this task, as they represent minimal input changes that alter the model's prediction, indicating when and how intervention is required.

Existing approaches rely on instance-wise optimization,

### AI 总结

总结生成失败

---

## 4. MaineCoon: Pursuing A Real-Time Audio-Visual Social World Model

- **作者**: Lichen Bai, Tianhao Zhang, Shitong Shao, Dingwei Tan, Qiyu Zhong
- **发布日期**: 2026-06-16
- **链接**: [arXiv:2606.17800v1](https://arxiv.org/abs/2606.17800v1) | [PDF](https://arxiv.org/pdf/2606.17800v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

As an increasing majority of global video content is consumed on social platforms for interactive social purposes, video generation models built for social worlds are important but largely overlooked by previous studies.

In this work, we define the position of social world models and build a prototype model as the first step towards this goal.

While previous world models successfully simulate physical environments or gaming world exploration, they remain fundamentally detached from human-centric social dynamics.

To bridge this gap as the first step to social world models, we present MaineCoon,

### AI 总结

总结生成失败

---

## 5. RT-Counter: Real-Time Text-Guided Open-Vocabulary Object Counting

- **作者**: Hao-Yuan Ma, Li Zhang, Zhiwei Zhu, Jie Gao
- **发布日期**: 2026-06-16
- **链接**: [arXiv:2606.17561v1](https://arxiv.org/abs/2606.17561v1) | [PDF](https://arxiv.org/pdf/2606.17561v1)
- **分类**: cs.CV
- **含金量**: 20/43 分
- **代码**: [GitHub](https://github.com/Jason-Mar1/RT-Counter.) ⭐ 0

### 摘要

Text-guided open-vocabulary object counting (TOOC) aims to count objects belonging to the categories specified by natural language descriptions.

Although vision-language pre-trained models have been successful applied to TOOC tasks, they still struggle with fine-grained spatial understanding and real-time inference requirements in counting scenarios.

To address these limitations, this paper proposes a real-time TOOC framework, called the Real-Time Counter (RT-Counter), that achieves not only good counting accuracy but also high computational efficiency.

RT-Counter designs a novel Visual Protot

### AI 总结

总结生成失败

---

## 6. Online LLM Selection via Constrained Bandits with Time-Varying Demand

- **作者**: Yin Huang, Qingsong Liu, Jie Xu
- **发布日期**: 2026-06-16
- **链接**: [arXiv:2606.17489v1](https://arxiv.org/abs/2606.17489v1) | [PDF](https://arxiv.org/pdf/2606.17489v1)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

Large Language Models (LLMs) are increasingly deployed in edge-cloud inference systems to handle diverse user tasks with heterogeneous accuracy, latency, and cost profiles.

Selecting the appropriate LLM for each incoming task is critical for ensuring service quality and efficient resource utilization.

However, model heterogeneity, stochastic and unknown performance characteristics, and time-varying task demands make static selection strategies inadequate.

Real-world deployments often impose hard resource budgets such as monetary expenditure limits, along with soft service-level requirements su

### AI 总结

总结生成失败

---

## 7. When the Next Step Is Not One Step: Distribution-Aware Execution Modeling for Concurrent Go Programs

- **作者**: Kaviru Hapuarachchi
- **发布日期**: 2026-06-16
- **链接**: [arXiv:2606.17508v1](https://arxiv.org/abs/2606.17508v1) | [PDF](https://arxiv.org/pdf/2606.17508v1)
- **分类**: cs.LG, cs.DC, cs.PL, cs.SE
- **含金量**: 20/43 分

### 摘要

Training a model to predict the next step in a concurrent program is harder than it looks: two runs of the same program from the same trace prefix can produce different next events, both valid, because the scheduler is nondeterministic.

A model trained against a single label is learning to guess one outcome of a random process.

We turn this around and use the nondeterminism as a training signal.

We run each program many times, aggregate the observed next events into an empirical distribution, and fine-tune a 7B model to match that distribution with a KL objective.

On 798 held-out predictions d

### AI 总结

总结生成失败

---

## 8. On the Memorization Behavior of LLMs in Generative Recommendation: Observations, Implications, and Training Strategies

- **作者**: Sunwoo Kim, Sunkyung Lee, Clark Mingxuan Ju, Donald Loveland, Bhuvesh Kumar
- **发布日期**: 2026-06-15
- **链接**: [arXiv:2606.17276v1](https://arxiv.org/abs/2606.17276v1) | [PDF](https://arxiv.org/pdf/2606.17276v1)
- **分类**: cs.IR, cs.LG
- **含金量**: 20/43 分

### 摘要

Generative recommendation (GR) has emerged as a promising direction for recommender systems.

Recently, large language models (LLMs) have been increasingly adopted for GR, as their rich pretrained knowledge is expected to help them generalize beyond common user behavior patterns that traditional memorization-oriented baselines can capture.

However, existing LLM-based GR works largely ignore LLMs' well-known tendency to memorize, which, if present in LLMs fine-tuned for GR, would restrict their utilization of pretrained knowledge.

In this work, we investigate this concern by examining one-hop me

### AI 总结

总结生成失败

---

