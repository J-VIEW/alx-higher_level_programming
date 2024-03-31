#!/usr/bin/env python3

import requests
import sys

def get_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve commits")
        return

    commits = response.json()
    for commit in commits[:10]:  # Get only the first 10 commits
        sha = commit.get('sha')
        author = commit.get('commit', {}).get('author', {}).get('name')
        print(f"{sha}: {author}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: script.py <repository> <owner>")
        sys.exit(1)

    repo = sys.argv[1]
    owner = sys.argv[2]
    get_commits(repo, owner)

