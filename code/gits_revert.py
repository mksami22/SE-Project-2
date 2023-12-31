# This code is part of the GITS (GIT Simplified) project and is licensed under MIT license (see LICENSE.txt for details).
# Link: https://github.com/mksami22/SE-Project-2/blob/main/LICENSE

# !/usr/bin/python3

from subprocess import PIPE
import subprocess


def gits_revert(args):
    """
    Function that allows user to revert commit
    """
    try:
        untracked_file_check_status = ["git", "status", "--porcelain"]
        process0 = subprocess.Popen(untracked_file_check_status,
                                    stdout=PIPE, stderr=PIPE)
        stdout, stderr = process0.communicate()
        print(stdout.decode("utf-8"))
        if stdout != b'':
            print("Error: Please commit or stash changes before revert")
            return False
        revert_cmd = list()
        revert_cmd.append("git")
        revert_cmd.append("revert")
        revert_cmd.append("--no-edit")
        commit_id = args.commit_id
        revert_cmd.append(commit_id)
        process1 = subprocess.Popen(revert_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        print("Reverted the commit:", args.commit_id)

    except Exception as e:
        print("ERROR: gits revert command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
