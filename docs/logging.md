# About gits branch
This command is used to list all the branches present.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/harshitpatel96/GITS/blob/master/code/gits_logging.py).

# Code Description
## Functions
1. gits_branch(args): 
This function simply displays all the branch present inside the local repository. It also places * in front of the branch that is currently checked out.
Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Use the command as below to list all branches:
```
$ gits branch
```$ gits logging
## Options
- `--author`: Filter the log to include only commits by the specified author.
  Example:
$ gits logging --author JohnDoe
- `--since`: Show commits more recent than a specific date.
Example:
$ gits logging --since "2022-01-01"

- `--until`: Show commits older than a specific date.
Example:
$ gits logging --until "2022-12-31"

- `--oneline`: Condense each commit to a single line, showing only the commit message.
Example:
$ gits logging --oneline

- `--graph`: Display an ASCII graph representing branch and merge history.
Example:
$ gits logging --graph
```
# Feel free to explore additional options by referring to the [Git log documentation](https://git-scm.com/docs/git-log).
