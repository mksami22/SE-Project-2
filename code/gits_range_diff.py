# This code is part of the GITS (GIT Simplified) project and is licensed under MIT license (see LICENSE.txt for details).
# Link: https://github.com/mksami22/SE-Project-2/blob/main/LICENSE

import subprocess
from subprocess import PIPE


def range_diff(args):
    """
    Shows difference between any two commits

    Args:
      rev1: First commit
      rev2: Second commit
      options: Additional options to git range-diff command if any

    Returns:
      str: The output of the range-diff command
    """
    try:
        range_diff_cmd = list()
        range_diff_cmd.append("git")
        range_diff_cmd.append("range-diff")
        range_diff_cmd.append("-U10")
        if args.rev1 and args.rev2:
            commit_hash = ""
            commit_hash += str(args.rev1)
            commit_hash += "..."
            commit_hash += str(args.rev2)
            range_diff_cmd.append(commit_hash)
        else:
            return False
        if args.options:
            range_diff_cmd.append(args.options)
        process = subprocess.Popen(range_diff_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print(stdout.decode("UTF-8"))
    except Exception as e:
        print("ERROR: git range-diff command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
