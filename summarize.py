#!/usr/bin/env python3
"""
使用LLM总结论文并生成Markdown报告
"""

import json
import os
from pathlib import Path
from datetime import datetime
from openai import OpenAI

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

def summarize_paper(paper, client):
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

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "你是一个学术研究助手，擅长用简洁的中文总结论文。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error summarizing paper: {e}")
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

    # 初始化OpenAI客户端
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
    )

    # 总结每篇论文
    summaries = {}
    for i, paper in enumerate(papers, 1):
        print(f"Summarizing {i}/{len(papers)}: {paper['title'][:50]}...")
        summary = summarize_paper(paper, client)
        if summary:
            summaries[paper['id']] = summary

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