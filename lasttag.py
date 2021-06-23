#!/bin/python

import os
import sys
import git
import argparse

from glob import glob

def arg_init() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [path to repo] [OPTION]...",
        description="Print last git tag"
    )

    parser.add_argument(
        "dest",
        nargs='*',
        default=os.getcwd(),
        help='Path to repo'
    )

    parser.add_argument(
        "-f", "--fetch",
        action='store_true',
        help="If flag set lasttag will fetch from origin first"
    )

    parser.add_argument(
        "-p", "--pull",
        help="If flag set lasttag will only pull from origin"
    )

    parser.add_argument(
        "-r", "--recursive",
        action='store_true',
        help="if flag is set it will do action recursively in all subfolders where applicable"
    )

    parser.parse_args(['--fetch'])
    return parser

def pull(repo_origin):
    repo_origin.pull()

def get_subfolders(path):
    return glob(f'{path}/*/')

def set_origin(path):
    repo = git.Repo(path)
    origin = repo.remotes.origin

    return origin

if __name__ == '__main__':
    parser = arg_init()
    args = parser.parse_args()

    print(args.dest)
    repo = git.Repo(args.dest)

    if args.fetch:
        set_origin(args.dest).fetch()

    if args.pull:
        pull(set_origin(args.dest))

    if args.recursive:
        for sub in get_subfolders(args.dest):
            os.chdir(sub)

            pull(set_origin(sub))

        print("all paths pulled")
        quit()

    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
    latest_tag = tags[-1]

    print(latest_tag)
