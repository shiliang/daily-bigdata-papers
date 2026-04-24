# 大数据+AI 领域论文日报

**日期**: 2026-04-24

**论文数量**: 7 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Why are all LLMs Obsessed with Japa...](https://arxiv.org/abs/2604.21751v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [CAP: Controllable Alignment Prompti...](https://arxiv.org/abs/2604.21251v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Surrogate modeling for interpreting...](https://arxiv.org/abs/2604.20331v2) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Spatial Metaphors for LLM Memory: A...](https://arxiv.org/abs/2604.21284v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [FSFM: A Biologically-Inspired Frame...](https://arxiv.org/abs/2604.20300v2) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [A Lightweight Transformer for Pain ...](https://arxiv.org/abs/2604.16491v2) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [SCM: Sleep-Consolidated Memory with...](https://arxiv.org/abs/2604.20943v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Why are all LLMs Obsessed with Japanese Culture? On the Hidden Cultural and Regional Biases of LLMs

- **作者**: Joseba Fernandez de Landa, Carla Perez-Almendros, Jose Camacho-Collados
- **发布日期**: 2026-04-23
- **链接**: [arXiv:2604.21751v1](https://arxiv.org/abs/2604.21751v1) | [PDF](https://arxiv.org/pdf/2604.21751v1)
- **分类**: cs.CL, cs.AI, cs.CY
- **含金量**: 20/43 分

### 摘要

LLMs have been showing limitations when it comes to cultural coverage and competence, and in some cases show regional biases such as amplifying Western and Anglocentric viewpoints.

While there have been works analysing the cultural capabilities of LLMs, there has not been specific work on highlighting LLM regional preferences when it comes to cultural-related questions.

In this work, we propose a new dataset based on a comprehensive taxonomy of Culture-Related Open Questions (CROQ).

The results show that, contrary to previous cultural bias work, LLMs show a clear tendency towards countries suc

### AI 总结

总结生成失败

---

## 2. CAP: Controllable Alignment Prompting for Unlearning in LLMs

- **作者**: Zhaokun Wang, Jinyu Guo, Jingwen Pu, Hongli Pu, Meng Yang
- **发布日期**: 2026-04-23
- **链接**: [arXiv:2604.21251v1](https://arxiv.org/abs/2604.21251v1) | [PDF](https://arxiv.org/pdf/2604.21251v1)
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

## 3. Surrogate modeling for interpreting black-box LLMs in medical predictions

- **作者**: Changho Han, Songsoo Kim, Dong Won Kim, Leo Anthony Celi, Jaewoong Kim
- **发布日期**: 2026-04-22
- **链接**: [arXiv:2604.20331v2](https://arxiv.org/abs/2604.20331v2) | [PDF](https://arxiv.org/pdf/2604.20331v2)
- **分类**: cs.CL, cs.AI, cs.LG
- **含金量**: 20/43 分

### 摘要

Large language models (LLMs), trained on vast datasets, encode extensive real-world knowledge within their parameters, yet their black-box nature obscures the mechanisms and extent of this encoding.

Surrogate modeling, which uses simplified models to approximate complex systems, can offer a path toward better interpretability of black-box models.

We propose a surrogate modeling framework that quantitatively explains LLM-encoded knowledge.

For a specific hypothesis derived from domain knowledge, this framework approximates the latent LLM knowledge space using observable elements (input-output p

### AI 总结

总结生成失败

---

## 4. Spatial Metaphors for LLM Memory: A Critical Analysis of the MemPalace Architecture

- **作者**: Robin Dey, Panyanon Viradecha
- **发布日期**: 2026-04-23
- **链接**: [arXiv:2604.21284v1](https://arxiv.org/abs/2604.21284v1) | [PDF](https://arxiv.org/pdf/2604.21284v1)
- **分类**: cs.AI, cs.CL, cs.IR
- **含金量**: 20/43 分

### 摘要

MemPalace is an open-source AI memory system that applies the ancient method of loci (memory palace) spatial metaphor to organize long-term memory for large language models; launched in April 2026, it accumulated over 47,000 GitHub stars in its first two weeks and claims state-of-the-art retrieval performance on the LongMemEval benchmark (96.6% Recall@5) without requiring any LLM inference at write time.

Through independent codebase analysis, benchmark replication, and comparison with competing systems, we find that MemPalace's headline retrieval performance is attributable primarily to its ve

### AI 总结

总结生成失败

---

## 5. FSFM: A Biologically-Inspired Framework for Selective Forgetting of Agent Memory

- **作者**: Yingjie Gu, Wenjian Xiong, Liqiang Wang, Pengcheng Ren, Chao Li
- **发布日期**: 2026-04-22
- **链接**: [arXiv:2604.20300v2](https://arxiv.org/abs/2604.20300v2) | [PDF](https://arxiv.org/pdf/2604.20300v2)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

For LLM agents, memory management critically impacts efficiency, quality, and security.

While much research focuses on retention, selective forgetting--inspired by human cognitive processes (hippocampal indexing/consolidation theory and Ebbinghaus forgetting curve)--remains underexplored.

We argue that in resource-constrained environments, a well-designed forgetting mechanism is as crucial as remembering, delivering benefits across three dimensions: (1) efficiency via intelligent memory pruning, (2) quality by dynamically updating outdated preferences and context, and (3) security through acti

### AI 总结

总结生成失败

---

## 6. A Lightweight Transformer for Pain Recognition from Brain Activity

- **作者**: Stefanos Gkikas, Christian Arzate Cruz, Yu Fang, Lu Cao, Muhammad Umar Khan
- **发布日期**: 2026-04-13
- **链接**: [arXiv:2604.16491v2](https://arxiv.org/abs/2604.16491v2) | [PDF](https://arxiv.org/pdf/2604.16491v2)
- **分类**: cs.CV, cs.AI
- **含金量**: 20/43 分

### 摘要

Pain is a multifaceted and widespread phenomenon with substantial clinical and societal burden, making reliable automated assessment a critical objective.

This paper presents a lightweight transformer architecture that fuses multiple fNIRS representations through a unified tokenization mechanism, enabling joint modeling of complementary signal views without requiring modality-specific adaptations or increasing architectural complexity.

The proposed token-mixing strategy preserves spatial, temporal, and time-frequency characteristics by projecting heterogeneous inputs onto a shared latent repre

### AI 总结

总结生成失败

---

## 7. SCM: Sleep-Consolidated Memory with Algorithmic Forgetting for Large Language Models

- **作者**: Saish Sachin Shinde
- **发布日期**: 2026-04-22
- **链接**: [arXiv:2604.20943v1](https://arxiv.org/abs/2604.20943v1) | [PDF](https://arxiv.org/pdf/2604.20943v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

We present SCM (Sleep-Consolidated Memory), a research preview of a memory architecture for large language models that draws on neuroscientific principles to address a fundamental limitation in current systems: the absence of persistent, structured, and biologically plausible memory.

Existing approaches rely on truncating context windows, growing vector databases without bound, or tiered storage systems that lack consolidation and forgetting mechanisms.

SCM implements five core components inspired by human memory: a limited-capacity working memory, multi-dimensional importance tagging, offline

### AI 总结

总结生成失败

---

