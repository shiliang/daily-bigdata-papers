#!/usr/bin/env python3
"""
将生成的论文报告推送到GitHub仓库
"""

import subprocess
import os
from datetime import datetime
from pathlib import Path

def run_command(cmd, check=True):
    """运行shell命令"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if check and result.returncode != 0:
        raise Exception(f"Command failed: {cmd}")
    return result

def push_to_repo():
    """推送更改到GitHub"""
    date_str = datetime.now().strftime("%Y-%m-%d")

    # 检查是否有更改
    result = run_command("git status --porcelain", check=False)

    if not result.stdout.strip():
        print("No changes to commit")
        return

    # 配置git用户
    run_command('git config user.name "GitHub Actions"')
    run_command('git config user.email "actions@github.com"')

    # 添加更改
    run_command("git add papers/ README.md")

    # 提交
    commit_message = f"docs: 添加 {date_str} 论文日报"
    run_command(f'git commit -m "{commit_message}"')

    # 推送
    run_command("git push origin main")

    print(f"\nSuccessfully pushed changes for {date_str}")

def main():
    print("="*60)
    print("Pushing to GitHub...")
    print("="*60)

    push_to_repo()

if __name__ == "__main__":
    main()