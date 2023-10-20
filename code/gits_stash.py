# This code is part of the GITS (GIT Simplified) project and is licensed under MIT license (see LICENSE.txt for details).
# Link: https://github.com/mksami22/SE-Project-2/blob/main/LICENSE

# !/usr/bin/python3

import subprocess
from subprocess import PIPE


def stash(args):
    """
    Function that allows user to stash changes. Testing change.
    """
    try:
        stash_cmd = list()
        stash_cmd.append("git")
        stash_cmd.append("stash")
        if len(vars(args)) > 0:
            if args.save:
                stash_cmd.append("save")
                if args.save != "":
                    stash_cmd.append(args.save)
            if args.list:
                stash_cmd.append("list")
            if args.drop:
                stash_cmd.append("drop")
                if args.drop != "":
                    stash_cmd.append(args.drop)
            if args.apply:
                stash_cmd.append("apply")
                if stash_cmd != "":
                    stash_cmd.append(args.apply)
            if args.pop:
                stash_cmd.append("pop")
                if args.pop != "":
                    stash_cmd.append(args.pop)
            if args.clear:
                stash_cmd.append("clear")
        else:
            pass
        process = subprocess.Popen(stash_cmd, stdout=PIPE, stderr=PIPE)

        stdout, stderr = process.communicate()
        print(stdout.decode("utf-8"))

    except Exception as e:
        print("ERROR: gits stash command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
