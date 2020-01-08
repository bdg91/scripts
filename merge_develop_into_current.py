#!/usr/bin/python3
import os


def merge_develop_into_current():
    current_branch = find_current_branch()

    print(os.popen('git checkout develop').read())
    print(os.popen('git pull').read())
    print(os.popen('git checkout ' + current_branch).read())
    print(os.popen('git pull').read())
    print(os.popen('git merge develop').read())
    print(os.popen('git push').read())


def find_current_branch():
    branches = os.popen('git branch').read().splitlines()

    for branch in branches:
        if branch[0] == '*':
            return branch[2:]


if __name__ == '__main__':
    merge_develop_into_current()