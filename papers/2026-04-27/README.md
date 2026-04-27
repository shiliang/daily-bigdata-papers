# 大数据+AI 领域论文日报

**日期**: 2026-04-27

**论文数量**: 6 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [CAP: Controllable Alignment Prompti...](https://arxiv.org/abs/2604.21251v2) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Compositional Online Learning for M...](https://arxiv.org/abs/2604.22624v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [One Shot Learning for Edge Detectio...](https://arxiv.org/abs/2604.22354v1) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [PermaFrost-Attack: Stealth Pretrain...](https://arxiv.org/abs/2604.22117v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [When Cow Urine Cures Constipation o...](https://arxiv.org/abs/2604.22002v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [SparseBalance: Load-Balanced Long C...](https://arxiv.org/abs/2604.13847v2) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. CAP: Controllable Alignment Prompting for Unlearning in LLMs

- **作者**: Zhaokun Wang, Jinyu Guo, Jingwen Pu, Hongli Pu, Meng Yang
- **发布日期**: 2026-04-23
- **链接**: [arXiv:2604.21251v2](https://arxiv.org/abs/2604.21251v2) | [PDF](https://arxiv.org/pdf/2604.21251v2)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

Large language models (LLMs) trained on unfiltered corpora inherently risk retaining sensitive information, necessitating selective knowledge unlearning for regulatory compliance and ethical safety.

However, existing parameter-modifying methods face fundamental limitations: high computational costs, uncontrollable forgetting boundaries, and strict dependency on model weight access.

These constraints render them impractical for closed-source models, yet current non-invasive alternatives remain unsystematic and reliant on empirical experience.

To address these challenges, we propose the Controll

### AI 总结

总结生成失败

---

## 2. Compositional Online Learning for Multi-Objective System Co-Design

- **作者**: Meshal Alharbi, Munther A. Dahleh, Gioele Zardini
- **发布日期**: 2026-04-24
- **链接**: [arXiv:2604.22624v1](https://arxiv.org/abs/2604.22624v1) | [PDF](https://arxiv.org/pdf/2604.22624v1)
- **分类**: math.OC, eess.SY
- **含金量**: 20/43 分

### 摘要

Many engineered systems must balance competing objectives, such as performance and safety, cost and reliability, or efficiency and sustainability, and are naturally modeled as compositions of interacting subsystems.

We study online multi-objective decision-making in monotone co-design, where functionalities and resources are partially ordered, and the goal is to identify the target-feasible antichain of non-dominated trade-offs using few expensive evaluations.

We introduce optimistic evaluators: history-dependent bounds on functionality and resource mappings that enable safe elimination of imp

### AI 总结

总结生成失败

---

## 3. One Shot Learning for Edge Detection on Point Clouds

- **作者**: Zhikun Tu, Yuhe Zhang, Yiou Jia, Kang Li, Daniel Cohen-Or
- **发布日期**: 2026-04-24
- **链接**: [arXiv:2604.22354v1](https://arxiv.org/abs/2604.22354v1) | [PDF](https://arxiv.org/pdf/2604.22354v1)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

Each scanner possesses its unique characteristics and exhibits its distinct sampling error distribution.

Training a network on a dataset that includes data collected from different scanners is less effective than training it on data specific to a single scanner.

Therefore, we present a novel one-shot learning method allowing for edge extraction on point clouds, by learning the specific data distribution of the target point cloud, and thus achieve superior results compared to networks that were trained on general data distributions.

More specifically, we present how to train a lightweight netwo

### AI 总结

总结生成失败

---

## 4. PermaFrost-Attack: Stealth Pretraining Seeding(SPS) for planting Logic Landmines During LLM Training

- **作者**: Harsh Kumar, Rahul Maity, Tanmay Joshi, Aman Chadha, Vinija Jain
- **发布日期**: 2026-04-23
- **链接**: [arXiv:2604.22117v1](https://arxiv.org/abs/2604.22117v1) | [PDF](https://arxiv.org/pdf/2604.22117v1)
- **分类**: cs.LG, cs.AI, cs.CL
- **含金量**: 20/43 分

### 摘要

Aligned large language models(LLMs) remain vulnerable to adversarial manipulation, and their dependence on web-scale pretraining creates a subtle but serious attack surface.

We study Stealth Pretraining Seeding (SPS), a new attack family in which adversaries distribute small amounts of poisoned content across stealth websites, expose them to web crawlers through robots.txt, and thereby increase the likelihood that such content is absorbed into future training corpora derived from sources such as Common Crawl.

Because each individual payload is tiny, diffuse, and superficially benign, the attac

### AI 总结

总结生成失败

---

## 5. When Cow Urine Cures Constipation on YouTube: Limits of LLMs in Detecting Culture-specific Health Misinformation

- **作者**: Anamta Khan, Ratna Kandala, Deepti, Sheza Munir, Joyojeet Pal
- **发布日期**: 2026-04-23
- **链接**: [arXiv:2604.22002v1](https://arxiv.org/abs/2604.22002v1) | [PDF](https://arxiv.org/pdf/2604.22002v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

Social media platforms have become primary channels for health information in the Global South.

Using gomutra (cow urine) discourse on YouTube in India as a case study, we present a post-facto Large Language Model (LLM)-assisted discourse analysis of 30 multilingual transcripts showing that promotional content blends sacred traditional language with pseudo-scientific claims in ways that sophisticated debunking content itself mirrors, creating a rhetorical register that LLMs, trained predominantly on Western corpora, are systematically ill-equipped to analyse.

Varying prompt tone across three L

### AI 总结

总结生成失败

---

## 6. SparseBalance: Load-Balanced Long Context Training with Dynamic Sparse Attention

- **作者**: Hongtao Xu, Jianchao Tan, Yuxuan Hu, Pengju Lu, Hongyu Wang
- **发布日期**: 2026-04-15
- **链接**: [arXiv:2604.13847v2](https://arxiv.org/abs/2604.13847v2) | [PDF](https://arxiv.org/pdf/2604.13847v2)
- **分类**: cs.LG, cs.AI
- **含金量**: 20/43 分

### 摘要

While sparse attention mitigates the computational bottleneck of long-context LLM training, its distributed training process exhibits extreme heterogeneity in both \textit{1)} sequence length and \textit{2)} sparsity sensitivity, leading to a severe imbalance problem and sub-optimal model accuracy.

Existing algorithms and training frameworks typically focus on single issue, failing to systematically co-optimize these two problems.

Therefore, we propose SparseBalance, a novel algorithm-system co-design framework, which exploits the sparsity and sequence heterogeneity to optimize model accuracy 

### AI 总结

总结生成失败

---

