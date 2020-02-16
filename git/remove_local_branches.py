#!/usr/bin/python3
import os


# Removes all local branches with exception of the master, develop, and currently checked out branch
def remove_local_branches():
    branches = os.popen('git branch').read().splitlines()

    for branch in branches:
        branch_name = branch.strip()
        if safe_to_remove(branch_name):
            os.popen('git branch -d ' + branch_name)
            print('Removed branch: ' + branch_name)


def safe_to_remove(branch_name):
    return branch_name != 'master' and branch_name != 'develop' and branch_name[0] != '*'


if __name__ == '__main__':
    remove_local_branches()
