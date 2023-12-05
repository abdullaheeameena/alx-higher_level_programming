#!/usr/bin/python3
"""
Python script that uses the GitHub API to list 10 commit recent to oldest) of a given repository and user.
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    params = {
        'per_page': 10,
        'page': 1,
    }

    response = requests.get(url, params=params)

    try:
        commits = response.json()
        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit', {}).get('author', {}).get('name')
            print(f"{sha}: {author_name}")

    except ValueError:
        print("Could not retrieve commits.")

