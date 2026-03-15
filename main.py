#!/usr/bin/env python3
"""
主入口：抓取论文并生成总结
"""

import subprocess
import sys

def main():
    print("="*60)
    print("Starting daily paper fetch pipeline...")
    print("="*60)

    # Step 1: 抓取论文
    print("\n[Step 1/2] Fetching papers from arXiv...")
    result = subprocess.run([sys.executable, "fetch_arxiv.py"], check=False)
    if result.returncode != 0:
        print(f"Warning: fetch_arxiv.py exited with code {result.returncode}")

    # Step 2: 生成总结
    print("\n[Step 2/2] Summarizing papers...")
    result = subprocess.run([sys.executable, "summarize.py"], check=False)
    if result.returncode != 0:
        print(f"Warning: summarize.py exited with code {result.returncode}")

    print("\n" + "="*60)
    print("Pipeline completed!")
    print("="*60)

if __name__ == "__main__":
    main()