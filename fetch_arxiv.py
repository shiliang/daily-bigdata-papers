#!/usr/bin/env python3
"""
抓取arXiv上大数据领域相关论文
"""

import arxiv
import json
import os
from datetime import datetime
from pathlib import Path

# 大数据相关关键词
KEYWORDS = [
    "big data",
    "distributed systems",
    "data pipeline",
    "data lake",
    "data warehouse",
    "streaming data",
    "real-time processing",
    "data engineering",
    "ETL",
    "data governance",
    "data quality",
    "Apache Spark",
    "Apache Flink",
    "Apache Kafka",
    "Hadoop",
    "data mesh",
    "data catalog",
    "columnar storage",
    "query optimization",
    "data lakehouse",
]

def fetch_papers(max_results=50):
    """从arXiv抓取论文"""
    papers = []

    # 构建搜索查询
    query = " OR ".join([f'all:"{kw}"' for kw in KEYWORDS])

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    for result in search.results():
        paper = {
            "id": result.entry_id.split("/")[-1],
            "title": result.title,
            "authors": [author.name for author in result.authors],
            "summary": result.summary,
            "published": result.published.strftime("%Y-%m-%d"),
            "updated": result.updated.strftime("%Y-%m-%d"),
            "pdf_url": result.pdf_url,
            "categories": result.categories,
            "primary_category": result.primary_category,
        }
        papers.append(paper)
        print(f"Fetched: {paper['title'][:60]}...")

    return papers

def save_papers(papers, date_str=None):
    """保存论文到JSON文件"""
    if date_str is None:
        date_str = datetime.now().strftime("%Y-%m-%d")

    # 创建papers目录
    papers_dir = Path("papers") / date_str
    papers_dir.mkdir(parents=True, exist_ok=True)

    # 保存原始数据
    data_file = papers_dir / "papers.json"
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)

    print(f"\nSaved {len(papers)} papers to {data_file}")
    return papers_dir

def main():
    print("="*60)
    print("Fetching big data papers from arXiv...")
    print("="*60)

    papers = fetch_papers(max_results=50)

    if papers:
        save_papers(papers)
        print(f"\nSuccessfully fetched {len(papers)} papers!")
    else:
        print("No papers found!")

    return papers

if __name__ == "__main__":
    main()