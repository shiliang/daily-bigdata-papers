#!/usr/bin/env python3
"""
主入口：抓取论文并生成总结，然后推送到仓库
"""

import subprocess
import sys
import os
from datetime import datetime

def run_cmd(cmd, check=True, capture=False):
    """运行shell命令"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=capture, text=capture)
    if check and result.returncode != 0:
        raise Exception(f"Command failed: {cmd}")
    return result

def main():
    print("="*60)
    print("Starting daily paper fetch pipeline...")
    print("="*60)

    # Step 1: 抓取论文
    print("\n[Step 1/3] Fetching papers from arXiv...")
    result = subprocess.run([sys.executable, "fetch_arxiv.py"], check=False)
    if result.returncode != 0:
        print(f"Warning: fetch_arxiv.py exited with code {result.returncode}")

    # Step 2: 生成总结
    print("\n[Step 2/3] Summarizing papers...")
    result = subprocess.run([sys.executable, "summarize.py"], check=False)
    if result.returncode != 0:
        print(f"Warning: summarize.py exited with code {result.returncode}")

    # Step 3: 推送到仓库
    print("\n[Step 3/3] Pushing to repository...")

    # 检查是否有更改
    result = run_cmd("git status --porcelain", check=False, capture=True)
    if not result.stdout or result.stdout.strip() == "":
        print("No changes to commit")
    else:
        # 配置git
        run_cmd('git config user.name "gitee-actions"')
        run_cmd('git config user.email "actions@gitee.com"')

        # 添加并提交
        run_cmd("git add papers/ README.md")

        date_str = datetime.now().strftime("%Y-%m-%d")
        run_cmd(f'git commit -m "docs: 添加 {date_str} 论文日报"')

        # 推送
        run_cmd("git push origin main")

    print("\n" + "="*60)
    print("Pipeline completed!")
    print("="*60)

if __name__ == "__main__":
    main()