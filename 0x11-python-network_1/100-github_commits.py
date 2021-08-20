#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""

from sys import argv
import requests

if __name__ == '__main__':
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    commits = r.json()

    for i in range(10):
        commit = commits[i]
        name = ((commit['commit'])['author'])['name']
        sha = commit['sha']
        print("{}: {}".format(sha, name))
