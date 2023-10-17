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
    range_diff_cmd = list()
    range_diff_cmd.append("git")
    range_diff_cmd.append("range-diff")
    if args.rev1:
        range_diff_cmd.append(args.rev1)
    if args.rev2:
        range_diff_cmd.append(args.rev2)
    if args.options:
        range_diff_cmd.append(args.options)
    try:
        process = subprocess.Popen(range_diff_cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print(stdout.decode("utf-8"))
    except Exception as e:
        print("ERROR: git range-diff command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
