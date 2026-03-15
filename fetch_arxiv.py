#!/usr/bin/env python3
"""
抓取arXiv上大数据领域相关论文
"""

import arxiv
import json
import time
from datetime import datetime
from pathlib import Path

# 精简关键词，分批查询
KEYWORD_GROUPS = [
    # 核心大数据
    ["big data", "data engineering", "data pipeline"],
    # 数据存储
    ["data lake", "data warehouse", "data lakehouse"],
    # 流处理
    ["stream processing", "real-time data", "data streaming"],
    # 分布式系统
    ["distributed systems", "Apache Spark", "Apache Flink"],
    # 数据管理
    ["data governance", "data quality", "data mesh"],
]

def fetch_papers_by_keyword(keyword, max_results=20, client=None):
    """单个关键词抓取论文"""
    if client is None:
        client = arxiv.Client()

    search = arxiv.Search(
        query=f'all:"{keyword}"',
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    papers = []
    try:
        for result in client.results(search):
            paper = {
                "id": result.entry_id.split("/")[-1],
                "title": result.title,
                "authors": [author.name for author in result.authors],
                "summary": result.summary,
                "published": result.published.strftime("%Y-%m-%d"),
                "updated": result.updated.strftime("%Y-%m-%d"),
                "pdf_url": result.pdf_url,
                "categories": list(result.categories) if result.categories else [],
                "primary_category": result.primary_category,
            }
            papers.append(paper)
            print(f"  Fetched: {paper['title'][:50]}...")
    except Exception as e:
        print(f"  Warning: Error fetching '{keyword}': {e}")

    return papers

def fetch_papers(max_results_per_keyword=15, total_max=60):
    """从arXiv抓取论文，分批查询避免请求过大"""
    client = arxiv.Client()
    all_papers = {}
    total_fetched = 0

    for group in KEYWORD_GROUPS:
        if total_fetched >= total_max:
            break

        print(f"\nFetching group: {', '.join(group[:2])}...")

        for keyword in group:
            if total_fetched >= total_max:
                break

            print(f"  Querying: {keyword}")
            papers = fetch_papers_by_keyword(
                keyword,
                max_results=max_results_per_keyword,
                client=client
            )

            # 用 ID 去重
            for paper in papers:
                if paper["id"] not in all_papers:
                    all_papers[paper["id"]] = paper
                    total_fetched += 1

            # 避免请求过快
            time.sleep(3)

    # 按更新日期排序
    papers_list = sorted(
        all_papers.values(),
        key=lambda x: x["updated"],
        reverse=True
    )

    return papers_list[:total_max]

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

    papers = fetch_papers(max_results_per_keyword=15, total_max=60)

    if papers:
        save_papers(papers)
        print(f"\nSuccessfully fetched {len(papers)} unique papers!")
    else:
        print("No papers found!")

    return papers

if __name__ == "__main__":
    main()