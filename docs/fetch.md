# About gits fetch

This command is used to fetch updates from a remote repository.

# Location of Code
The code that implements the above-mentioned gits functionality is located [here](https://github.com/mksami22/SE-Project-2/blob/master/code/gits_fetch.py).

# Code Description
## Functions
1. gits_fetch(args): 
   This function fetches updates from the remote repository. It can fetch all branches or append the ref names and object names of fetched refs to the existing fetch head.
   Function returns True for successful execution and False otherwise with an exception.

# How to run it? (Small Example)
Use the command as below to fetch updates:
$ gits fetch

## Options
- `--all`: Fetch updates from all remotes.
  Example:
$ gits fetch --all

- `--append`: Append ref names and object names of fetched refs to the existing fetch head.
Example:
$ gits fetch --append


Feel free to explore additional options by referring to the [Git fetch documentation](https://git-scm.com/docs/git-fetch).
