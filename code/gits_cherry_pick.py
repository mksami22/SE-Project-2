# This code is part of the GITS (GIT Simplified) project and is licensed under MIT license (see LICENSE.txt for details).
# Link: https://github.com/mksami22/SE-Project-2/blob/main/LICENSE

# !/usr/bin/python3

from subprocess import PIPE
import subprocess


def gits_cherry_pick(args):
    """
    Function that allows user to cherry pick commits
    """
    try:
        cherry_pick_cmd = list()
        cherry_pick_cmd.append("git")
        cherry_pick_cmd.append("cherry-pick")
        commit_id = args.commit_id
        if not commit_id:
            print("Fatal: Please provide valid commit id")
            return False
        cherry_pick_cmd.append(commit_id)
        process1 = subprocess.Popen(cherry_pick_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        if stderr != b"":
            print(stderr.decode("utf-8"))
        else:
            print("Cherry picked the commit id:", args.commit_id)

    except Exception as e:
        print("ERROR: gits cherry-pick command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
