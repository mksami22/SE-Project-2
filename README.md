# GITS

### GIT Simplified

![GitHub](https://img.shields.io/github/license/harshitpatel96/GITS)
[![Build Status](https://app.travis-ci.com/mksami22/SE-Project-2.svg?branch=main)](https://app.travis-ci.com/mksami22/SE-Project-2)
[![codecov](https://codecov.io/gh/mksami22/SE-Project-2/graph/badge.svg?token=HKVX8YRIRG)](https://codecov.io/gh/mksami22/SE-Project-2)
![YouTube Video Views](https://img.shields.io/youtube/views/6Y8_RQecnZ8?style=social)

[![DOI](https://zenodo.org/badge/295480790.svg)](https://zenodo.org/badge/latestdoi/295480790)

![GitHub issues](https://img.shields.io/github/issues/mksami22/SE-Project-2)
![GitHub closed issues](https://img.shields.io/github/issues-closed/mksami22/SE-Project-2)

[![Scc Count Badge](https://sloc.xyz/github/mksami22/SE-Project-2/)](https://github.com/mksami22/SE-Project-2/)

[![](https://img.youtube.com/vi/6Y8_RQecnZ8/hqdefault.jpg)](https://youtu.be/6Y8_RQecnZ8 "GITS demo")

# About GITS

GITS streamlines most frequently performed workflows using fewer commands which is so much easier and better than usual.
Git-Simplified AKA GITS can be thought of wrapper around major Git functionalities.

# Installation for Linux

1. Clone GITS Repo
2. From the root directory run the following command
   ```
   pip install -r requirements.txt
   ```
3. Go to configurations directory and run the following command

   If you are working on Linux system with a bash terminal or a Windows system using Windows subsystem for linux:

   ```
   bash project_init.sh
   ```

   If you are working on Linux system with a fish terminal:

   ```
   fish project_init.fish
   ```

4. Source the bashrc file

   ```
   source ~/.bashrc
   ```

   Note: Open the .bashrc file in User home directory to make sure that the alias command does not have any white spaces in the path. If so, rename the directory to remove the white spaces and re-run the setup.

# Installation for Windows

1.  Clone GITS Repo
2.  From the root directory run the following command
    ```
    pip install -r requirements.txt
    ```
3.  Currently, this project cannot be run on Windows. You need to make use of WSL to work on this project in Windows
    although this fix would only work for systems running Windows 10. If you are using another version of Windows, using a
    virtual machine might be preferred.

        Please refer this link to enable WSL : https://docs.microsoft.com/en-us/windows/wsl/install-win10

# How to Contribute?

Please take a look at our CONTRIBUTING.md where we provide instructions on contributing to the repo and help us in enhancing the current video conferencing platforms.

# Documentation

## Functionalities Implemented

1. [gits profile](https://github.com/harshitpatel96/GITS/blob/master/docs/profile.md)
1. [gits rebase](https://github.com/harshitpatel96/GITS/blob/master/docs/rebase.md)
1. [gits reset](https://github.com/harshitpatel96/GITS/blob/master/docs/reset.md)
1. [gits revert](https://github.com/harshitpatel96/GITS/blob/master/docs/revert.md)
1. [gits upstream](https://github.com/harshitpatel96/GITS/blob/master/docs/upstream.md)
1. [gits super reset](https://github.com/harshitpatel96/GITS/blob/master/docs/super_reset.md)
1. [gits commit](https://github.com/harshitpatel96/GITS/blob/master/docs/commit.md)
1. [gits create_branch](https://github.com/harshitpatel96/GITS/blob/master/docs/create_branch.md)
1. [gits logging](https://github.com/harshitpatel96/GITS/blob/master/docs/logging.md)
1. [gits undo](https://github.com/harshitpatel96/GITS/blob/master/docs/undo.md)
1. [gits untrack](https://github.com/harshitpatel96/GITS/blob/master/docs/untrack.md)
1. [gits track](https://github.com/harshitpatel96/GITS/blob/master/docs/track.md)
1. [gits delete](https://github.com/harshitpatel96/GITS/blob/master/docs/delete.md)
1. [gits sync](https://github.com/harshitpatel96/GITS/blob/master/docs/sync.md)
1. [gits switch](https://github.com/harshitpatel96/GITS/blob/master/docs/switch.md)
1. [gits status](https://github.com/harshitpatel96/GITS/blob/master/docs/status.md)
1. [gits branch](https://github.com/harshitpatel96/GITS/blob/master/docs/branch.md)
1. [gits diff](https://github.com/harshitpatel96/GITS/blob/master/docs/diff.md)
1. [gits init](https://github.com/harshitpatel96/GITS/blob/master/docs/init.md)
1. [gits merge](https://github.com/harshitpatel96/GITS/blob/master/docs/merge.md)
1. [gits push](https://github.com/harshitpatel96/GITS/blob/master/docs/push.md)
1. [gits pull](https://github.com/harshitpatel96/GITS/blob/master/docs/pull.md)
1. [gits fetch](https://github.com/harshitpatel96/GITS/blob/master/docs/fetch.md)

## Pydoc implementation

We have tried to write as much documentation as possible. You can use pydoc to go through the documentation.
For example if you want to go through all the documentation for all files in code/ directory, do the following:

`cd code`<br>
`python3 -m pydoc -b `

This will open up a browser and you can see all the files. You can click on a particular file to access the
documentation associated with that file.

This repository is made for CSC 510 Software Engineering Course at NC State University.

## Experimentation setup for phase 3

This project aims to ease the developers efforts while interacting with version control system Git.
Here are few motivation points behind coming up with this idea:

- Few git command names are very misleading from the end user's perspective. Consider this, `git checkout` command is used for both switching the branches and removing changes present inside working directory.
- Based on the development practice used by various teams, there are some tasks which requires the execution of more than one command to complete the task. This process can be easily automated such that developer only need to execute a single command to get their work done.
- There are almost always the cases that because of not much efficient syncing techniques, code pushed to the remote repository results in conflict while merging. It is always best practice to solve any such merge conflicts on the local repo rather than the remote one.

To solve the issues described above, we came up with the project **gits** that stands for **git-Simplified**.
So, this experiment aims to compare various aspects to traditional git and our proposed gits.

### Participation

Basic idea here is to let the participants finish the tasks present in the tasks list mentioned below, and observe whether gits made this process easier or not.
This is higher level idea for this study.
There are two ways to choose who will use git and who will use gits.

1. If you have significant number of participants, you can divide them up into two groups. Participants from one group will use Gits to complete the set of tasks while participants from second group will use traditional Git to finish their tasks.
   to achieve some great results, participants with lesser git knowledge should be assigned to later group who will be using git to finish their task. That would lessen the bias in observations since people would be already familiar with git rather than gits.
2. If number of participants are limited and have enough time, you can let each participants finish the set of tasks twice. Once using traditional git and then using gits.
   However, to remove any unwanted bias here as well, divide the participants in two groups. first group should use the git first and then gits. Second group should finish the tasks using gits first and then using git.

Ask each participants to setup the gits inside their local machine before starting the study using steps shown above.

### Tasks list

Here is basic draft of the tasks that covers almost each enhancement.
Feel free to edit this list as per your convenience. Add few tasks if you got more time for the experiment.

- Create a test repository that can be used by participants to complete their tasks.
- Ask participant to clone the repository on their local machine.
- Ask participant to set their git profile name and email to "dummy_name" and "dummy@name.com" respectively. Once they are done, ask them to switch it back to the original ones.
- Create two branches with name: branch1 and branch2.
- list all the branches.
- From current branch, switch to the branch1.
- create a file named "foo.txt" and write some text in it.
- track the file "foo.txt" so that it gets considered for the next commit.
- Create another file named "bar.txt" and add some text in it.
- track this file "bar.txt" so that it gets considered for the next commit.
- commit these changes with appropriate commit message.
- make some change to the "bar.txt" and track those changes so that they get considered for the next commit.
- You found some issues with changes to this file and now you don't want it to be considered for the next commit. remove those changes from commit area.
- Also remove those changes from working directory.
- commit these changes with appropriate commit message and switch to the main branch.
- merge changes from the branch1 into this main branch and push those changes to the remote main branch.
- Now switch to branch2.
- Main branch has changed since we created this branch so this branch is working behind in changes. Make this branch up to date with local main branch.
- You just got to know that some other developer merged his changes to the remote main branch. Since you have checked out from the main branch, you also want those changes in development branch. So, make your branch up to date with remote main branch.
- Now switch to main branch again.
- create new file "temp.txt" and write some text in it and commit those changes.
- You just realized you directly made changes to the main branch rather than your development branch by mistake. Undo those changes by making current main branch same as remote main branch.
- You just got to know that someone merged their changes to the remote main branch. Sync your main branch.
- Last commit that is present in the main branch is not working well so you want to remove changes made by that commit entirely on both: local and remote.
- You are doing great till now but assume a hypothetical scenario where you have made a mess in your local repo and want to delete the current repo and fork it all again.

### Quantitative measures

Here are some measures that can help compare the results between traditional git and gits.

1. Time taken to finish a particular task.
2. Number of commands executed to complete each task.
3. Number of time participants referred to the documentation or any other resources.

### Qualitative measures

Along with quantitative measures described above, few qualitative measures can help to assess the performance better.

1. Familiarity with traditional git
2. hardness of the task

# Support
## Discord Community

Welcome to the GITS Discord community – your central hub for connecting with other GITS enthusiasts, seeking support, and collaborating with developers and contributors. Join our vibrant community by clicking the link below:

[Join Discord](https://discord.gg/XwpEJeJn)

### Discord Channels:

1. **#rules 📜:**
   - **Description:** Familiarize yourself with the rules before diving into discussions. Respect and positive vibes are the foundation of our community.

2. **#updates 🚀:**
   - **Description:** Stay in the loop with the latest news, announcements, and exciting updates about GITS.

3. **#support 🛠️:**
   - **Description:** Encounter a coding challenge or need assistance with GITS? This channel is your go-to place for community-driven support.

4. **#important-links 🔗:**
   - **Description:** Access essential links and resources, including documentation and project repositories, to enhance your GITS experience.

5. **#general 🌐:**
   - **Description:** The heart of our community! Engage in friendly discussions, share coding triumphs, and connect with other GITS enthusiasts.

6. **#users 👥:**
   - **Description:** Connect with fellow GITS users, share experiences, and seek advice in this user-centric channel.

7. **#developers 👩‍💻👨‍💻 (Private):**
   - **Description:** A private enclave for developers actively involved in shaping the technical aspects of GITS. Dive into technical discussions and coding wonders.

8. **#contributors 👥👩‍💻 (Private):**
   - **Description:** An exclusive space for elite contributors. Collaborate on top-secret projects and actively contribute to the evolution of GITS.

### Roles:

1. **User 👤:**
   - **Description:** The starting point for every GITS adventurer! As a user, you have access to general channels and discussions.

2. **Developer 👩‍💻👨‍💻:**
   - **Description:** Elevated to Developer status! If you're actively involved in the development of GITS, this role opens the door to the private #developers channel.

3. **Contributor 👥👩‍💻:**
   - **Description:** The elite contributors! If you've made significant contributions to GITS, this role grants you access to the private #contributors channel.

### Guidelines:

1. **Respect and Positive Vibes:**
   - **Description:** Treat others with kindness and respect. We're a diverse community with a shared passion for GITS. Let's keep the vibes positive!

2. **Clear Communication:**
   - **Description:** When seeking support or discussing ideas, provide clear and detailed information. This helps others understand your context and provide better assistance.

3. **No Unauthorized Bots:**
   - **Description:** To maintain a streamlined experience, refrain from adding unauthorized bots to the server without approval.

4. **Constructive Feedback:**
   - **Description:** Embrace the spirit of improvement! Provide constructive feedback, share your thoughts on features, and let's collectively enhance GITS.

5. **Privacy and Security:**
   - **Description:** Protect your privacy! Avoid sharing sensitive information such as passwords or personal details in public channels.

6. **Have Fun! 😄:**
   - **Description:** Lastly, let's have a blast! Share funny anecdotes, celebrate each other's victories, and make GITS a place of joy.

## Support Email

For more sensitive matters or issues requiring private communication, you can reach out to our support email at **gitsimplified@gmail.com**. Feel free to use this email for specific concerns or inquiries that may not be suitable for public channels.
Guidelines for Email Communication:
Clear Subject Line:

When sending an email to support, use a clear and concise subject line that reflects the nature of your inquiry (e.g., "Technical Issue," "Bug Report," "Feature Request").
Detailed Description:

Provide a detailed description of your issue or inquiry in the body of the email. Include relevant information such as the version of GITS you are using, your operating system, and any error messages you've encountered.
Attachments (if applicable):

If your inquiry involves screenshots or additional files, feel free to attach them to the email. This can help our support team better understand and address your concern.
Continuous Improvement:
Your feedback and interactions with our support team contribute to the continuous improvement of GITS. We appreciate your engagement and are dedicated to delivering a positive user experience.

For urgent matters or issues that require immediate attention, please use the #support channel on the Discord server in addition to sending an email.

Thank you for choosing GITS, and we look forward to assisting you through our support email at gitsimplified@gmail.com.
