#!/bin/python

import sys
import git

if len(sys.argv) == 1:
    print('Path is required')
    exit()

wd = sys.argv[1]
repo = git.Repo(wd)

tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
latest_tag = tags[-1]

print(latest_tag)
