import subprocess
from subprocess import PIPE
import helper

def gits_fetch(args):
    """
    This function is used to download objects
    and reference from another repository 
    Usage: gits fetch
           gits fetch --all
           gits fetch --append
           gits fetch --depth=<depth>
    """
    try:
        arguments = []
        if args.all is True:
            arguments += ["--all"]
        elif args.append is True:
            arguments += ["--append"]
        elif args.depth is True:
            arguments += [args.depth]
        
        fetch_command = ["git", "fetch"] + arguments
        process1 = subprocess.Popen(fetch_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        print(stdout.decode("utf-8"))

    except Exception as e:
        print("ERROR: gits fetch command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    