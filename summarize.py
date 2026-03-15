#!/usr/bin/env python3
"""
使用LLM总结论文并生成Markdown报告
支持 OpenAI 和阿里云 DashScope API
"""

import json
import os
import sys
import argparse
import time
from pathlib import Path
from datetime import datetime
from openai import OpenAI

def get_client():
    """初始化 LLM 客户端"""
    # 优先从命令行参数获取
    parser = argparse.ArgumentParser()
    parser.add_argument('--api-key', type=str, default=None)
    parser.add_argument('--base-url', type=str, default=None)
    args, _ = parser.parse_known_args()

    # API Key: 命令行参数 > 环境变量
    api_key = args.api_key or os.environ.get("OPENAI_API_KEY", "")
    # Base URL: 命令行参数 > 环境变量 > 默认值
    base_url = args.base_url or os.environ.get("OPENAI_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")

    # 检测是否为阿里云 DashScope
    if "dashscope" in base_url or "aliyuncs" in base_url:
        model = os.environ.get("LLM_MODEL", "qwen3.5-plus")
        print(f"Using Alibaba Cloud DashScope with model: {model}")
    else:
        model = os.environ.get("LLM_MODEL", "qwen3.5-plus")
        print(f"Using API with model: {model}")

    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
        timeout=60.0,
    )
    return client, model

def load_papers(date_str=None):
    """加载论文数据"""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")

    papers_file = Path("papers") / date_str / "papers.json"

    if not papers_file.exists():
        print(f"No papers found for {date_str}")
        return []

    with open(papers_file, "r", encoding="utf-8") as f:
        return json.load(f)

def summarize_paper(paper, client, model, max_retries=3):
    """使用LLM总结单篇论文"""
    prompt = f"""请用中文总结以下论文的核心内容：

标题: {paper['title']}
作者: {', '.join(paper['authors'][:5])}
摘要: {paper['summary']}

请提供：
1. 一句话概述（不超过50字）
2. 核心贡献（3-5点）
3. 技术要点
4. 潜在应用场景

请用简洁的中文回答。"""

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "你是一个学术研究助手，擅长用简洁的中文总结论文。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=500,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"  Attempt {attempt + 1}/{max_retries} failed: {e}")
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 5
                print(f"  Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"  All retries failed for: {paper['title'][:50]}")
                return None

def generate_markdown(papers, summaries, date_str):
    """生成Markdown报告"""
    md_content = f"""# 大数据领域论文日报

**日期**: {date_str}

**论文数量**: {len(papers)}

---

"""

    for i, paper in enumerate(papers, 1):
        summary = summaries.get(paper['id'], '总结生成失败')

        md_content += f"""## {i}. {paper['title']}

**作者**: {', '.join(paper['authors'][:5])}
**发布日期**: {paper['published']}
**arXiv ID**: [{paper['id']}](https://arxiv.org/abs/{paper['id']})
**PDF**: [下载]({paper['pdf_url']})
**分类**: {', '.join(paper['categories'])}

### 论文摘要

{paper['summary'][:500]}...

### AI 总结

{summary}

---

"""

    return md_content

def generate_index_md(date_str):
    """生成索引页面"""
    papers_dir = Path("papers")

    # 获取所有日期目录
    dates = sorted([d.name for d in papers_dir.iterdir() if d.is_dir()], reverse=True)

    index_content = f"""# 大数据论文日报

每日自动抓取 arXiv 上大数据领域相关论文并生成总结。

## 历史日报

| 日期 | 论文数量 |
|------|----------|
"""

    for date in dates:
        papers_file = papers_dir / date / "papers.json"
        if papers_file.exists():
            with open(papers_file, "r", encoding="utf-8") as f:
                count = len(json.load(f))
            index_content += f"| [{date}](./{date}/README.md) | {count} |\n"

    index_content += f"""
## 关键词

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

---

*最后更新: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""

    return index_content

def main():
    print("="*60)
    print("Summarizing papers...")
    print("="*60)

    date_str = datetime.now().strftime("%Y-%m-%d")
    papers = load_papers(date_str)

    if not papers:
        print("No papers to summarize!")
        return

    # 初始化客户端
    client, model = get_client()

    # 总结每篇论文
    summaries = {}
    success_count = 0

    for i, paper in enumerate(papers, 1):
        print(f"[{i}/{len(papers)}] {paper['title'][:50]}...")
        summary = summarize_paper(paper, client, model)
        if summary:
            summaries[paper['id']] = summary
            success_count += 1
        # 避免 API 限流
        time.sleep(1)

    print(f"\nSuccessfully summarized: {success_count}/{len(papers)}")

    # 生成Markdown
    md_content = generate_markdown(papers, summaries, date_str)

    # 保存Markdown文件
    papers_dir = Path("papers") / date_str
    readme_file = papers_dir / "README.md"
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(md_content)

    # 更新索引
    index_content = generate_index_md(date_str)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(index_content)

    print(f"\nGenerated report: {readme_file}")
    print(f"Updated index: README.md")

if __name__ == "__main__":
    main()