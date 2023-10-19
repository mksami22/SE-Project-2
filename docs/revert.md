# About gits revert

This command is used to create a new commit that undoes changes made in a previous commit.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/harshitpatel96/GITS/blob/master/code/gits_revert.py).

# Code Description
## Functions
1. gits_revert(args): 
   This function creates a new commit that undoes changes made in a specified commit. It takes a commit ID as an argument.
   Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Use the command as below to revert changes from a specific commit:
$ gits revert <commit_id>

## Options
- `--no-commit`: When set, the revert is performed, but the changes are not committed, allowing for manual adjustments before committing.
  Example:
  ```bash
  $ gits revert --no-commit <commit_id>
- `--edit`: When set, the editor is opened to modify the commit message.
  Example:
  ```bash
  $ gits revert --edit <commit_id>
  ```
Feel free to explore additional options by referring to the Git revert documentation.
