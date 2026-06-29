# 大数据+AI 领域论文日报

**日期**: 2026-06-29

**论文数量**: 2 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Mechanism-Driven Monitors for Preem...](https://arxiv.org/abs/2606.28116v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [RedKnot: Efficient Long-Context LLM...](https://arxiv.org/abs/2606.06256v2) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability

- **作者**: Ruixuan Huang, Yipei Wang, Wenyi Fang, Hantao Huang, Yifan Huang
- **发布日期**: 2026-06-26
- **链接**: [arXiv:2606.28116v1](https://arxiv.org/abs/2606.28116v1) | [PDF](https://arxiv.org/pdf/2606.28116v1)
- **分类**: cs.CL
- **含金量**: 20/43 分

### 摘要

Frontier large language model training consumes massive accelerator fleets and long wall-clock computation, making stability failures costly when they occur.

After a numerical or a hyperparameter fault has already destabilized the training dynamics, it may continue for thousands of steps while loss and gradient norms still appear normal.

We study mechanism-driven detection of training instability by deriving internal monitors from the functional role of each critical module and from the earliest computational sites where failures are expected to produce measurable signatures.

For low-precision

### AI 总结

总结生成失败

---

## 2. RedKnot: Efficient Long-Context LLM Serving with Head-Aware KV Reuse and SegPagedAttention

- **作者**: Yang Liu, ZhaoKai Luo, HuaYi Jin, ZhiYong Wang, RuoZhou He
- **发布日期**: 2026-06-04
- **链接**: [arXiv:2606.06256v2](https://arxiv.org/abs/2606.06256v2) | [PDF](https://arxiv.org/pdf/2606.06256v2)
- **分类**: cs.AI
- **含金量**: 20/43 分

### 摘要

As the input length of large language model (LLM) serving continues to grow, the KV cache has become a dominant bottleneck in AI infrastructure.

It limits GPU memory capacity, serving concurrency, cache reuse, and distributed scalability.

Multiple important problems, including position-independent KV cache, prefix KV cache compression, hot/cold KV cache separation, and distributed KV cache management, all depend on how the KV cache is represented and managed.

However, existing serving systems largely rely on a monolithic KV cache abstraction, where the KV cache is treated as a homogeneous sequ

### AI 总结

总结生成失败

---

