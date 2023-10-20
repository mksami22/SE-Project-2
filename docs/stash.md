# About gits status

This command is used to record the current state of the working directory. Use when you want to save local changes and revert to a clean working directory.

# Location of Code
The code that implements the above mentioned gits functionality is located [here](https://github.com/mksami22/SE-Project-2/blob/main/code/gits_stash.py).

# Code Description
## Functions
1. gits_stash(args): 
This function allows users to stash changes.
Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Use the command as below to see the status:
```bash
$ gits stash branch <branchname> <stash>
```
## Options
- '--show': inspect modifications stashed away.

Example:
```bash
$ gits stash show [-u | --include-untracked | --only-untracked] [<diff-options>] [<stash>]
```
Feel free to explore additional options by referring to the Git stash documentation.
