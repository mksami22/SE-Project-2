# About gits cherrypick

This command is used to apply the changes introduced by a specific commit or a range of commits to the current branch.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/mksami22/SE-Project-2/blob/master/code/gits_cherry_pick.py).

# Code Description
## Functions
1. gits_cherrypick(args): 
   This function applies the changes introduced by a specific commit or a range of commits to the current branch. It takes commit references as arguments.
   Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Use the command as below to apply changes from a specific commit:
```bash
$ gits cherrypick <commit_ref>
```
## Options
- `--continue`: Continue the cherry-pick operation in case of conflicts.
  Example:
  ```bash
  $ gits cherrypick --continue
- `--abort`: Abort the cherry-pick operation, restoring the branch to its state before the operation started.
  Example:
  ```bash
  $ gits cherrypick --abort
- `--quit`: End the cherry-pick operation, leaving the changes uncommitted.
  Example:
  ```bash
  $ gits cherrypick --quit
  ```
Feel free to explore additional options by referring to the Git cherry-pick documentation.
