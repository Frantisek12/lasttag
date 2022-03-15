#!/bin/python

import os
import sys
import git
import asyncio
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
    print(f'Pulling ${repo_origin}')
    repo_origin.pull()


def get_subfolders(path):
    return glob(f'{path}/*/')


def set_origin(path):
    repo = git.Repo(path)
    origin = repo.remotes.origin

    return origin


def get_tag(path):
    try:
        repo = git.Repo(path)
    except git.exc.InvalidGitRepositoryError as e:
        print(f'this is not repo path ${path}')

    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
    latest_tag = tags[-3]

    print(latest_tag)


def main():
    parser = arg_init()
    args = parser.parse_args()

    if args.fetch:
        set_origin(args.dest).fetch()

    if args.pull:
        pull(set_origin(args.dest))

    if args.recursive:
        for sub in get_subfolders(args.dest):
            os.chdir(sub)
            print(f'Pulling ${sub}')
            pull(set_origin(sub))
            get_tag(sub)

        print("all paths pulled")
        quit()

    get_tag(args.dest)

if __name__ == '__main__':
    main()
