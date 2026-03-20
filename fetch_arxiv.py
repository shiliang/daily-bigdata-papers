#!/usr/bin/env python3
"""
抓取arXiv上大数据+AI领域相关论文
支持跨日期去重、GitHub代码检测
"""

import arxiv
import json
import time
import re
import requests
from datetime import datetime
from pathlib import Path

# 历史记录文件
HISTORY_FILE = Path("papers/history.json")

# 大数据 + AI 关键词
KEYWORD_GROUPS = [
    # 大模型与AI基础设施
    ["LLM training", "large language model infrastructure", "AI infrastructure"],
    # 向量数据库与检索
    ["vector database", "RAG retrieval augmented", "embedding search"],
    # 数据湖与AI
    ["data lake AI", "lakehouse machine learning", "Iceberg AI"],
    # 流式AI与实时推理
    ["streaming ML", "real-time inference", "online learning"],
    # 分布式训练
    ["distributed training", "GPU cluster training", "model parallelism"],
]

def extract_github_url(text):
    """从文本中提取GitHub链接"""
    # 匹配 https://github.com/owner/repo 格式
    pattern = r'https://github\.com/([a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+)'
    matches = re.findall(pattern, text)
    if matches:
        # 返回第一个匹配的完整URL
        return f"https://github.com/{matches[0]}"
    return None

def get_github_stats(github_url):
    """获取GitHub仓库的Star数和描述"""
    if not github_url:
        return None

    try:
        # 提取 owner/repo
        match = re.search(r'github\.com/([a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+)', github_url)
        if not match:
            return None

        repo_path = match.group(1)
        api_url = f"https://api.github.com/repos/{repo_path}"

        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "url": github_url,
                "stars": data.get("stargazers_count", 0),
                "description": data.get("description", "")[:100] if data.get("description") else "",
                "language": data.get("language", ""),
            }
    except Exception as e:
        print(f"    Warning: Failed to fetch GitHub stats: {e}")

    return {"url": github_url, "stars": 0, "description": "", "language": ""}

def load_history():
    """加载历史已抓取的论文ID"""
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(data.get("paper_ids", []))
    return set()

def save_history(paper_ids):
    """保存历史记录"""
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "paper_ids": list(paper_ids),
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }, f, ensure_ascii=False, indent=2)

def fetch_papers_by_keyword(keyword, max_results=20, client=None, check_github=True):
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
                "github": None,  # GitHub信息
            }

            # 检测GitHub链接
            if check_github:
                github_url = extract_github_url(result.summary)
                if github_url:
                    print(f"    Checking GitHub: {github_url.split('/')[-1]}...")
                    github_stats = get_github_stats(github_url)
                    paper["github"] = github_stats
                    if github_stats and github_stats.get("stars", 0) > 0:
                        print(f"    [*] {github_stats['stars']} stars")

            papers.append(paper)
            print(f"  Fetched: {paper['title'][:50]}...")
    except Exception as e:
        print(f"  Warning: Error fetching '{keyword}': {e}")

    return papers

def fetch_papers(max_results_per_keyword=15, total_max=30, history_ids=None):
    """从arXiv抓取论文，分批查询避免请求过大，支持跨日期去重"""
    client = arxiv.Client()
    all_papers = {}
    total_fetched = 0
    skipped_count = 0

    # 初始化历史记录
    if history_ids is None:
        history_ids = set()

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

            # 用 ID 去重（包括跨日期历史）
            for paper in papers:
                paper_id = paper["id"]
                # 跨日期去重
                if paper_id in history_ids:
                    skipped_count += 1
                    continue
                # 本次抓取去重
                if paper_id not in all_papers:
                    all_papers[paper_id] = paper
                    total_fetched += 1

            # 避免请求过快
            time.sleep(3)

    # 按更新日期排序
    papers_list = sorted(
        all_papers.values(),
        key=lambda x: x["updated"],
        reverse=True
    )

    if skipped_count > 0:
        print(f"\nSkipped {skipped_count} papers (already in history)")

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
    print("Fetching Big Data + AI papers from arXiv...")
    print("="*60)

    # 加载历史记录
    history_ids = load_history()
    print(f"Loaded {len(history_ids)} papers from history")

    # 先抓取更多论文，后续筛选含金量最高的10篇
    papers = fetch_papers(max_results_per_keyword=15, total_max=30, history_ids=history_ids)

    if papers:
        save_papers(papers)
        print(f"\nSuccessfully fetched {len(papers)} new papers!")

        # 更新历史记录
        new_ids = {p["id"] for p in papers}
        history_ids.update(new_ids)
        save_history(history_ids)
        print(f"Updated history: {len(history_ids)} total papers")
    else:
        print("No new papers found!")

    return papers

if __name__ == "__main__":
    main()