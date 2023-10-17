"""
This code is part of the GITS (GIT Simplified) project and is licensed under MIT license (see LICENSE.txt for details). 
Link: https://github.com/mksami22/SE-Project-2/blob/main/LICENSE
"""

#!/usr/bin/python3

from subprocess import PIPE
import subprocess


def switch_branch(args):
    """
    Function that allows user to switch between branches
    """
    try:
        switch_cmd = list()
        switch_cmd.append("git")
        switch_cmd.append("checkout")
        switch_cmd.append(args.branch_name)
        process1 = subprocess.Popen(switch_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        print("Switched to branch:", args.branch_name)

    except Exception as e:
        print("ERROR: gits switch command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
