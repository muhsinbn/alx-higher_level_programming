#!/usr/bin/python3
"""
Python script that retrieves and displays the 10 most recent commits
of a repository by a specific user using the GitHub API.

Requirements:
- Uses the GitHub API to retrieve commits of a repository.
- Prints all commits in the format "<sha>: <author name>" (one by line).
- Takes 2 arguments: repository name and owner name.
- Uses the packages requests and sys.
- Does not import packages other than requests and sys.
- Does not need to check arguments passed to the script (number or type).
"""
import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Define the Github API endpoint to retrieve commits
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    # Send a GET request to the Github API
    resp = requests.get(url)

    if resp.status_code == 200:
        commits = resp.json()

        # Display the 10 most recent commits
        for commit in commits[:10]:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}")
