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
import re
from pathlib import Path
from datetime import datetime
from openai import OpenAI

# 强制刷新 stdout
sys.stdout.reconfigure(line_buffering=True) if hasattr(sys.stdout, 'reconfigure') else None

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

def evaluate_paper(paper, client, model, max_retries=3):
    """评估论文价值和含金量"""
    prompt = f"""请评估以下论文的学术价值和含金量：

标题: {paper['title']}
作者: {', '.join(paper['authors'][:5])}
摘要: {paper['summary'][:800]}

请从以下维度评分（1-10分）：
1. **创新性**：方法/思路的新颖程度
2. **影响力**：对领域的潜在影响
3. **实用性**：工程落地价值
4. **严谨性**：实验设计和论证质量

只需输出JSON格式：
{{"innovation": X, "impact": X, "practicality": X, "rigor": X, "total": X, "reason": "一句话评价"}}"""

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "你是学术评估专家，请客观评估论文价值。只输出JSON。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=200,
            )
            content = response.choices[0].message.content
            # 提取JSON
            if '```' in content:
                content = content.split('```')[1].strip()
                if content.startswith('json'):
                    content = content[4:].strip()
            result = json.loads(content)
            return result
        except Exception as e:
            if attempt == max_retries - 1:
                return {"innovation": 5, "impact": 5, "practicality": 5, "rigor": 5, "total": 20, "reason": "评估失败"}
            time.sleep(2)

def summarize_paper(paper, client, model, max_retries=3):
    """使用LLM总结单篇论文"""
    prompt = f"""请用中文总结以下论文的核心内容：

标题: {paper['title']}
作者: {', '.join(paper['authors'][:5])}
摘要: {paper['summary']}

请按以下格式输出（不要有多余文字）：

**概述**：一句话概括论文（不超过50字）

**核心贡献**：
- 贡献1
- 贡献2
- 贡献3

**技术要点**：
- 要点1
- 要点2

**应用场景**：场景1、场景2等"""

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "你是一个学术研究助手，擅长用简洁的中文总结论文。请严格按指定格式输出。"},
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

def generate_markdown(papers, summaries, evaluations, date_str):
    """生成Markdown报告"""
    md_content = f"""# 大数据+AI 领域论文日报

**日期**: {date_str}

**论文数量**: {len(papers)} 篇精选论文

---

"""

    for i, paper in enumerate(papers, 1):
        summary = summaries.get(paper['id'], '总结生成失败')
        eval_result = evaluations.get(paper['id'], {})

        # 格式化摘要，添加换行
        abstract = paper['summary']
        abstract_formatted = re.sub(r'\.\s+', '.\n\n', abstract[:600])

        # 含金量评分
        total_score = eval_result.get('total', 0)
        reason = eval_result.get('reason', '')

        md_content += f"""## {i}. {paper['title']}

- **作者**: {', '.join(paper['authors'][:5])}
- **发布日期**: {paper['published']}
- **链接**: [arXiv:{paper['id']}](https://arxiv.org/abs/{paper['id']}) | [PDF]({paper['pdf_url']})
- **分类**: {', '.join(paper['categories'])}
- **含金量**: {total_score}/40 分

### 摘要

{abstract_formatted}

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

    index_content = f"""# 大数据+AI 论文日报

每日自动抓取 arXiv 上大数据+AI 领域相关论文，筛选含金量最高的论文并生成总结。

## 历史日报

| 日期 | 论文数量 |
|------|----------|
"""

    for date in dates:
        papers_file = papers_dir / date / "papers.json"
        if papers_file.exists():
            with open(papers_file, "r", encoding="utf-8") as f:
                count = len(json.load(f))
            index_content += f"| [{date}](./papers/{date}/README.md) | {count} |\n"

    index_content += f"""
## 关键词

本项目追踪以下领域的研究进展：

- LLM Training / 大模型训练
- AI Infrastructure / AI基础设施
- Vector Database / 向量数据库
- RAG / 检索增强生成
- Data Lake + AI / 数据湖+AI
- Streaming ML / 流式机器学习
- Distributed Training / 分布式训练
- Real-time Inference / 实时推理

---

*最后更新: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""

    return index_content

def main():
    print("="*60)
    print("Summarizing and evaluating papers...")
    print("="*60)

    date_str = datetime.now().strftime("%Y-%m-%d")
    papers = load_papers(date_str)

    if not papers:
        print("No papers to summarize!")
        return

    # 初始化客户端
    client, model = get_client()

    # 评估论文价值
    print("\n[Phase 1] Evaluating paper quality...")
    evaluations = {}
    for i, paper in enumerate(papers, 1):
        print(f"  [{i}/{len(papers)}] Evaluating: {paper['title'][:40]}...")
        eval_result = evaluate_paper(paper, client, model)
        evaluations[paper['id']] = eval_result
        time.sleep(0.5)

    # 按含金量排序，筛选最高的10篇
    papers_with_scores = [(p, evaluations.get(p['id'], {}).get('total', 0)) for p in papers]
    papers_with_scores.sort(key=lambda x: x[1], reverse=True)
    top_papers = [p for p, score in papers_with_scores[:10]]

    print(f"\n[Phase 2] Selected top 10 papers by quality score:")
    for i, (p, score) in enumerate(papers_with_scores[:10], 1):
        print(f"  {i}. [{score}/40] {p['title'][:50]}...")

    # 总结筛选后的论文
    print("\n[Phase 3] Summarizing top papers...")
    summaries = {}
    for i, paper in enumerate(top_papers, 1):
        print(f"  [{i}/10] {paper['title'][:50]}...")
        summary = summarize_paper(paper, client, model)
        if summary:
            summaries[paper['id']] = summary
        time.sleep(1)

    print(f"\nSuccessfully summarized: {len(summaries)}/10")

    # 生成Markdown
    md_content = generate_markdown(top_papers, summaries, evaluations, date_str)

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