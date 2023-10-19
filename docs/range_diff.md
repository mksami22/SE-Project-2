# About gits range-diff

This command is used to show the difference between any two commits.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/mksami22/SE-Project-2/blob/master/code/gits_range_diff.py).

# Code Description
## Functions
1. range_diff(args): 
   This function shows the difference between any two specified commits. It takes two commit references as arguments, along with any additional options.
   Function prints the output of the `git range-diff` command.

# How to run it? (Small Example)
Use the command as below to show the difference between two commits:
$ gits range-diff --rev1 <commit_ref_1> --rev2 <commit_ref_2> --options <additional_options>

## Options
- `--rev1`: Specifies the first commit for comparison.
  Example:
  ```bash
  $ gits range-diff --rev1 <commit_ref_1> --rev2 <commit_ref_2>
- `--rev2`: Specifies the second commit for comparison.
  Example:
  ```bash
  $ gits range-diff --rev1 <commit_ref_1> --rev2 <commit_ref_2>
- `--options`: Additional options to be passed to the underlying git range-diff command.
  Example:
  ```bash
  $ gits range-diff --rev1 <commit_ref_1> --rev2 <commit_ref_2> --options "-U3"

Feel free to explore additional options by referring to the Git range-diff documentation.
