# 大数据论文日报

每日自动抓取 arXiv 上大数据领域相关论文并生成 AI 总结。

## 功能特性

- 每天自动抓取大数据领域最新论文
- 使用 LLM 生成中文总结
- 自动生成 Markdown 格式报告
- GitHub Pages 静态页面展示

## 关键词追踪

本项目追踪以下领域的研究进展：

- Big Data / 大数据
- Distributed Systems / 分布式系统
- Data Pipeline / 数据管道
- Data Lake / Warehouse / 数据湖/仓库
- Streaming Data / 流式数据
- Real-time Processing / 实时处理
- Data Engineering / 数据工程
- ETL / 数据处理
- Data Governance / 数据治理
- Data Quality / 数据质量
- Apache Spark/Flink/Kafka
- Data Mesh / 数据网格
- Query Optimization / 查询优化

## 目录结构

```
.
├── .github/
│   └── workflows/
│       └── daily.yml      # GitHub Actions 配置
├── papers/
│   └── YYYY-MM-DD/        # 每日论文
│       ├── papers.json    # 原始数据
│       └── README.md      # 当日报告
├── fetch_arxiv.py         # 抓取论文脚本
├── summarize.py           # 总结论文脚本
├── push_to_repo.py        # 推送脚本
├── requirements.txt       # Python 依赖
└── README.md              # 本文件
```

## 使用方法

### 1. Fork 本仓库

### 2. 配置 Secrets

在仓库设置中添加以下 Secrets：

- `OPENAI_API_KEY`: OpenAI API 密钥
- `OPENAI_BASE_URL`: (可选) 自定义 API 地址

### 3. 启用 GitHub Actions

在 Actions 页面启用工作流。

### 4. 手动触发或等待定时运行

可以手动触发工作流，或等待每天北京时间 9:00 自动运行。

## 本地运行

```bash
# 安装依赖
pip install -r requirements.txt

# 设置环境变量
export OPENAI_API_KEY="your-api-key"
# 可选：使用国内代理
export OPENAI_BASE_URL="https://api.openai.com/v1"

# 运行抓取
python fetch_arxiv.py

# 运行总结
python summarize.py

# 推送到仓库
python push_to_repo.py
```

## 许可证

MIT License