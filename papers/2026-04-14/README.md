# 大数据+AI 领域论文日报

**日期**: 2026-04-14

**论文数量**: 10 篇精选论文

## 论文对比表

| # | 论文 | 核心方法 | 主要贡献 | 代码 | 评分 |
|---|------|----------|----------|------|------|
| 1 | [Ψ-Map: Panoptic Surface Integrated ...](https://arxiv.org/abs/2604.10982v1) | 待分析 | 评估失败 | - | 20/43 |
| 2 | [Fast-SegSim: Real-Time Open-Vocabul...](https://arxiv.org/abs/2604.10951v1) | 待分析 | 评估失败 | - | 20/43 |
| 3 | [Matrix-Game 3.0: Real-Time and Stre...](https://arxiv.org/abs/2604.08995v2) | 待分析 | 评估失败 | - | 20/43 |
| 4 | [Gradient-Variation Regret Bounds fo...](https://arxiv.org/abs/2604.11151v1) | 待分析 | 评估失败 | - | 20/43 |
| 5 | [Continuous-time Online Learning via...](https://arxiv.org/abs/2604.10958v1) | 待分析 | 评估失败 | - | 20/43 |
| 6 | [Learning to Test: Physics-Informed ...](https://arxiv.org/abs/2604.10967v1) | 待分析 | 评估失败 | - | 20/43 |
| 7 | [Whisper-AuT: Domain-Adapted Audio E...](https://arxiv.org/abs/2604.10438v1) | 待分析 | 评估失败 | - | 20/43 |
| 8 | [LLM-PRISM: Characterizing Silent Da...](https://arxiv.org/abs/2604.10390v1) | 待分析 | 评估失败 | - | 20/43 |
| 9 | [Energy-Efficient Federated Edge Lea...](https://arxiv.org/abs/2604.10662v1) | 待分析 | 评估失败 | - | 20/43 |
| 10 | [Agentic Application in Power Grid S...](https://arxiv.org/abs/2604.09995v1) | 待分析 | 评估失败 | - | 20/43 |

---


## 1. Ψ-Map: Panoptic Surface Integrated Mapping Enables Real2Sim Transfer

- **作者**: Xuan Yu, Yuxuan Xie, Changjian Jiang, Shichao Zhai, Rong Xiong
- **发布日期**: 2026-04-13
- **链接**: [arXiv:2604.10982v1](https://arxiv.org/abs/2604.10982v1) | [PDF](https://arxiv.org/pdf/2604.10982v1)
- **分类**: cs.RO
- **含金量**: 20/43 分

### 摘要

Open-vocabulary panoptic reconstruction is essential for advanced robotics perception and simulation.

However, existing methods based on 3D Gaussian Splatting (3DGS) often struggle to simultaneously achieve geometric accuracy, coherent panoptic understanding, and real-time inference frequency in large-scale scenes.

In this paper, we propose a comprehensive framework that integrates geometric reinforcement, end-to-end panoptic learning, and efficient rendering.

First, to ensure physical realism in large-scale environments, we leverage LiDAR data to construct plane-constrained multimodal Gaussia

### AI 总结

总结生成失败

---

## 2. Fast-SegSim: Real-Time Open-Vocabulary Segmentation for Robotics in Simulation

- **作者**: Xuan Yu, Yuxuan Xie, Shichao Zhai, Shuhao Ye, Rong Xiong
- **发布日期**: 2026-04-13
- **链接**: [arXiv:2604.10951v1](https://arxiv.org/abs/2604.10951v1) | [PDF](https://arxiv.org/pdf/2604.10951v1)
- **分类**: cs.RO
- **含金量**: 20/43 分

### 摘要

Open-vocabulary panoptic reconstruction is crucial for advanced robotics and simulation.

However, existing 3D reconstruction methods, such as NeRF or Gaussian Splatting variants, often struggle to achieve the real-time inference frequency required by robotic control loops.

Existing methods incur prohibitive latency when processing the high-dimensional features required for robust open-vocabulary segmentation.

We propose Fast-SegSim, a novel, simple, and end-to-end framework built upon 2D Gaussian Splatting, designed to realize real-time, high-fidelity, and 3D-consistent open-vocabulary segment

### AI 总结

总结生成失败

---

## 3. Matrix-Game 3.0: Real-Time and Streaming Interactive World Model with Long-Horizon Memory

- **作者**: Zile Wang, Zexiang Liu, Jiaxing Li, Kaichen Huang, Baixin Xu
- **发布日期**: 2026-04-10
- **链接**: [arXiv:2604.08995v2](https://arxiv.org/abs/2604.08995v2) | [PDF](https://arxiv.org/pdf/2604.08995v2)
- **分类**: cs.CV
- **含金量**: 20/43 分

### 摘要

With the advancement of interactive video generation, diffusion models have increasingly demonstrated their potential as world models.

However, existing approaches still struggle to simultaneously achieve memory-enabled long-term temporal consistency and high-resolution real-time generation, limiting their applicability in real-world scenarios.

To address this, we present Matrix-Game 3.0, a memory-augmented interactive world model designed for 720p real-time longform video generation.

Building upon Matrix-Game 2.0, we introduce systematic improvements across data, model, and inference.

First, 

### AI 总结

总结生成失败

---

## 4. Gradient-Variation Regret Bounds for Unconstrained Online Learning

- **作者**: Yuheng Zhao, Andrew Jacobsen, Nicolò Cesa-Bianchi, Peng Zhao
- **发布日期**: 2026-04-13
- **链接**: [arXiv:2604.11151v1](https://arxiv.org/abs/2604.11151v1) | [PDF](https://arxiv.org/pdf/2604.11151v1)
- **分类**: cs.LG, stat.ML
- **含金量**: 20/43 分

### 摘要

We develop parameter-free algorithms for unconstrained online learning with regret guarantees that scale with the gradient variation $V_T(u) = \sum_{t=2}^T \|\nabla f_t(u)-\nabla f_{t-1}(u)\|^2$.

For $L$-smooth convex loss, we provide fully-adaptive algorithms achieving regret of order $\widetilde{O}(\|u\|\sqrt{V_T(u)} + L\|u\|^2+G^4)$ without requiring prior knowledge of comparator norm $\|u\|$, Lipschitz constant $G$, or smoothness $L$.

The update in each round can be computed efficiently via a closed-form expression.

Our results extend to dynamic regret and find immediate implications to th

### AI 总结

总结生成失败

---

## 5. Continuous-time Online Learning via Mean-Field Neural Networks: Regret Analysis in Diffusion Environments

- **作者**: Erhan Bayraktar, Bingyan Han, Ziqing Zhang
- **发布日期**: 2026-04-13
- **链接**: [arXiv:2604.10958v1](https://arxiv.org/abs/2604.10958v1) | [PDF](https://arxiv.org/pdf/2604.10958v1)
- **分类**: cs.LG, cs.AI, math.OC
- **含金量**: 20/43 分

### 摘要

We study continuous-time online learning where data are generated by a diffusion process with unknown coefficients.

The learner employs a two-layer neural network, continuously updating its parameters in a non-anticipative manner.

The mean-field limit of the learning dynamics corresponds to a stochastic Wasserstein gradient flow adapted to the data filtration.

We establish regret bounds for both the mean-field limit and finite-particle system.

Our analysis leverages the logarithmic Sobolev inequality, Polyak-Lojasiewicz condition, Malliavin calculus, and uniform-in-time propagation of chaos.

U

### AI 总结

总结生成失败

---

## 6. Learning to Test: Physics-Informed Representation for Dynamical Instability Detection

- **作者**: Minxing Zheng, Zewei Deng, Liyan Xie, Shixiang Zhu
- **发布日期**: 2026-04-13
- **链接**: [arXiv:2604.10967v1](https://arxiv.org/abs/2604.10967v1) | [PDF](https://arxiv.org/pdf/2604.10967v1)
- **分类**: cs.LG
- **含金量**: 20/43 分

### 摘要

Many safety-critical scientific and engineering systems evolve according to differential-algebraic equations (DAEs), where dynamical behavior is constrained by physical laws and admissibility conditions.

In practice, these systems operate under stochastically varying environmental inputs, so stability is not a static property but must be reassessed as the context distribution shifts.

Repeated large-scale DAE simulation, however, is computationally prohibitive in high-dimensional or real-time settings.

This paper proposes a test-oriented learning framework for stability assessment under distrib

### AI 总结

总结生成失败

---

## 7. Whisper-AuT: Domain-Adapted Audio Encoder for Efficient Audio-LLM Training

- **作者**: Jielin Qiu, Ming Zhu, Wenting Zhao, Zhiwei Liu, Liangwei Yang
- **发布日期**: 2026-04-12
- **链接**: [arXiv:2604.10438v1](https://arxiv.org/abs/2604.10438v1) | [PDF](https://arxiv.org/pdf/2604.10438v1)
- **分类**: cs.SD
- **含金量**: 20/43 分

### 摘要

Audio-native large language models (audio-LLMs) commonly use Whisper as their audio encoder.

However, Whisper was trained exclusively on speech data, producing weak representations for music and environmental sound.

This forces downstream audio-LLMs to compensate through extensive training on large-scale non-speech data.

We present Whisper-AuT, a domain-adapted audio encoder obtained by fine-tuning Whisper-large-v3 on a curated mixture of speech (80%), environmental sound (10%), and music (10%) totaling approximately 20M samples.

The full encoder-decoder is trained end-to-end with a seq2seq ca

### AI 总结

总结生成失败

---

## 8. LLM-PRISM: Characterizing Silent Data Corruption from Permanent GPU Faults in LLM Training

- **作者**: Abhishek Tyagi, Saurabh Hukerikar, Nirmal Saxena, Yanxiang Huang, Philip Shirvani
- **发布日期**: 2026-04-12
- **链接**: [arXiv:2604.10390v1](https://arxiv.org/abs/2604.10390v1) | [PDF](https://arxiv.org/pdf/2604.10390v1)
- **分类**: cs.AR
- **含金量**: 20/43 分

### 摘要

Large-scale LLM training is increasingly susceptible to hardware defects stemming from manufacturing escapes and silicon aging.

These defects manifest as Silent Data Corruption (SDC) that perturb gradients and parameters throughout the training process.

We present LLM-PRISM, a methodology to characterize LLM pre-training resilience to hardware faults.

LLM-PRISM couples RTL-level GPU fault simulation with a stochastic injection engine embedded in Megatron-LM.

Through 7,664 training runs across FP16, BF16, and FP8 regimes, we analyze how fault type, rate, and numeric format govern resilience.

We

### AI 总结

总结生成失败

---

## 9. Energy-Efficient Federated Edge Learning For Small-Scale Datasets in Large IoT Networks

- **作者**: Haihui Xie, Wenkun Wen, Shuwu Chen, Zhaogang Shu, Minghua Xia
- **发布日期**: 2026-04-12
- **链接**: [arXiv:2604.10662v1](https://arxiv.org/abs/2604.10662v1) | [PDF](https://arxiv.org/pdf/2604.10662v1)
- **分类**: cs.LG, cs.IT
- **含金量**: 20/43 分

### 摘要

Large-scale Internet of Things (IoT) networks enable intelligent services such as smart cities and autonomous driving, but often face resource constraints.

Collecting heterogeneous sensory data, especially in small-scale datasets, is challenging, and independent edge nodes can lead to inefficient resource utilization and reduced learning performance.

To address these issues, this paper proposes a collaborative optimization framework for energy-efficient federated edge learning with small-scale datasets.

We first derive an expected learning loss to quantify the relationship between the number o

### AI 总结

总结生成失败

---

## 10. Agentic Application in Power Grid Static Analysis: Automatic Code Generation and Error Correction

- **作者**: Qinjuan Wang, Shan Yang, Yongli Zhu
- **发布日期**: 2026-04-11
- **链接**: [arXiv:2604.09995v1](https://arxiv.org/abs/2604.09995v1) | [PDF](https://arxiv.org/pdf/2604.09995v1)
- **分类**: eess.SY, cs.AI
- **含金量**: 20/43 分

### 摘要

This paper introduces an LLM agent that automates power grid static analysis by converting natural language into MATPOWER scripts.

The framework utilizes DeepSeek-OCR to build an enhanced vector database from MATPOWER manuals.

To ensure reliability, it devises a three-tier error-correction system: a static pre-check, a dynamic feedback loop, and a semantic validator.

Operating via the Model Context Protocol, the tool enables asynchronous execution and automatically debugging in MATLAB.

Experimental results demonstrate that the system achieves a 82.38% accuracy regarding the code fidelity, effe

### AI 总结

总结生成失败

---

