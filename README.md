# Git Commands

## Overview

Welcome to the Git Commands Basics workshop! This workshop is designed to help you get started with the fundamentals of Git, a distributed version control system. Whether you are new to Git or looking to refresh your knowledge, this workshop will guide you through essential Git commands and workflows.

## Prerequisites

This is workshop for Linux, So before you begin, make sure you have the following installed on your linux server.

```
apt install git
```

or you could use your local computer Windows

```
https://git-scm.com/downloads
```

## Workshop Content

### 1. Introduction to Git

-   Overview of version control
-   Benefits of using Git and Why gits
-   Basic Git concepts

### 2. Setting Up Git

-   Configuring your Git identity
-   Initializing a new Git repository
-   Cloning an existing repository

### 3. Github

#### Create account

```
https://github.com/
```

#### Create repository

```
https://github.com/new
```

### 4. Git Basics

#### 4.1. Git init

Initializes a new Git repository. If you want to place a project under revision control, this is the first command you need to learn.

-   ##### If in target folder

```
git init
```

-   ##### If want to create folder with git

```
git init folder_name
```

#### 4.2. Git status

This command is used to check the current status of your Git repository. It shows which files are modified, which files are staged for commit, and which files are untracked. This step helps you understand the state of your repository before proceeding with further actions.

```
git status
```

you can try this command to see some hidden folders for (mac user or linux).

```
ls -la
```

#### 4.3. Git add

Before add let's create some new files

```
mkdir folder_name
```

```
touch main.py
```

This command is used to add all modified and new files in the current directory to the staging area.
The dot . represents the current directory. By using git add ., you're staging all changes in the current directory for the next commit.

Add all changed files.

```
git add .
```

Add Specific files.

```
git add file1.txt file2.txt
```

#### 4.4. Git status again

After adding changes to the staging area, it's a good practice to check the status again to ensure that all changes you intended to stage are properly staged and there are no untracked files left.

```
git status
```

#### 4.5. Git commit

This command commits the staged changes to the **local repository** along with a descriptive message "Initial commit". The -m flag is used to include a commit message directly from the command line.

```
git commit -m "Initial commit"
```

#### 4.6. Git remote

```
git remote add origin https://github.com/your-username/your-repository.git
```

#### 4.7. Git push

This command is used to push committed changes from the local repository to the remote repository. However, before pushing, it's necessary to set up a connection to a remote repository using git remote add and specifying the URL of the remote repository.

```
git push origin main
```

Push to the specific branch

```
git push <remote> <branch>
```

### 5. Collaborating with Git

Let's clone git repository

```
git clone https://github.com/ArKaRaShi/git-commands-workshop.git
```
#### 5.1 Create a branch

This command creates a new branch but does not switch to it.

```
git branch branch_name
```

To switch to the new branch, you would use.

```
git checkout branch_name
```

Alternatively, you can create and switch to a new branch in one command

```
git checkout -b branch_name
```

#### 5.2 List branches

This command lists all the branches in your repository.

```
git branch
```

#### 5.3 Delete a branch

This command deletes the specified branch.

```
git branch -d branch_name
```

If the branch contains changes that are not merged, you might need to force the deletion using -D.

```
git branch -D branch_name
```

#### 5.4 Merge branches

To integrate changes from one branch into another, you can use the git merge command. For example, to merge a branch into the current branch
```
git checkout <target_branch>
```
```
git merge <source_branch>
```

#### 5.5 Rebase branches

Another way to integrate changes is through rebasing. It essentially moves or combines a sequence of commits to a new base commit.

```
git checkout feature_branch
```
```
git rebase main_branch
```

#### 5.6 Resolve conflict

During branch merging or rebasing, conflicts might arise if changes conflict with each other. Use git mergetool or manually edit the conflicting files to resolve the conflicts.

```
git mergetool
```

#### 5.7 View commit history

This command shows the commit history of the current branch.

```
git log
```
### 6. Git Extras

-   Git log and history exploration
-   Tagging releases
-   Ignoring files with `.gitignore`

### Resources

-   [Git Documentation](https://git-scm.com/doc)
-   [GitHub Guides](https://guides.github.com/)
-   [Pro Git Book](https://git-scm.com/book/en/v2)
