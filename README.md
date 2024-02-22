Git Commands Cheat Sheet
========================

This README provides a quick reference for commonly used Git commands. GOOD LUCK!!!

![]()

Table of Contents
-----------------

1. [Install](#install)
2. [Setup](#setup)
3. [Basic Concepts](#basicconepts)
4. [Create Git Repository](#create-git-repo)
5. [Make & Show a Change](#makechange)
6. [Branching](#branching)
7. [Merging](#merging)
8. [Rebasing](#rebase)
9. [Undoing Changes](#undoing-changes)
10. [Synchronizing](#sync)

Install <a name="install"></a>
-------

- For Linux

	```sh
	sudo apt install git
	```

- For macOS/Window can read from this link, sorry, we are lazy.

	[https://git-scm.com/downloads](https://git-scm.com/downloads)

Setup <a name="setup"></a>
-----

- You need to config git local so that githost knows you.

	```sh
	git config --global user.email <"gmail">
	```
	```sh
	git config --global user.name <"git username">
	```

- If you use Linux/Mac, you need to use.

	```sh
	ssh-keygen -o -t rsa -C <"gmail">
	```

- Copy public key and pase in github.
	
	Open github -> Click profile github at top right -> `Settings` -> `SSH and GPG keys` -> `New SSH Key` -> Add **"Title"** box and paste public key in **"Key"** box -> `Add SSH key`
	<!-- insert a picture for put key -->

Basic Concepts <a name="basicconecpts"></a>
--------------

This section will explain about important words in git

- **main**		is default branch
- **origin**	is default alias on upstream repo
- **HEAD**		is current branch
- **HEAD^**		is parant of **HEAD**
- **HEAD~2**	is grandparent of **HEAD**

> [!TIP]
> **Can change "HEAD" and "number" to branch and number what you want**

Create Git Repository <a name="create-git-repo"></a>
--------------

- First make repo on githost, in this case we use github.

	Open github -> Click **profile github at top right** -> `New` -> Add name of repo in **"Repository name"** box -> `Create repository`
	<!-- maybe insert a picture -->

- If you had local repo
	
	```sh
	git init <your directory>
	```

- If you had remote repo

	```sh
	git clone <url> <diretory name>
	```

Make a Change <a name="makechange"></a>
-------------
### Make
- Add files to stage

	```sh
	git add <file>
	```

	**TRICK : use "." for add all your current files**

- Commit all staged files to git repo

	```sh
	git commit -m <"recommend comment about your change">
	```

### Show

- Shows the commit history of the current branch

	```sh
	git log
	```

- Shows the status of your local repository

	```sh
	git status
	```

- Shows the commit as human readable of the current branch

	```sh
	git show <commit_hash>
	```

Branching <a name="branching"></a>
---------

- Create branch

	```sh
	git branch <branch_name>
	```

- Show branch

	```sh
	git branch <flags>
	```

	*flags : -a = all branch, -r = remote branch, -v = local branch*

-  Changes the reference of ```<branch1>``` to point to the same commit as ```<branch2>```

	```sh
	git branch -f <branch1> <branch2>
	```

- Delete a branch

	```sh
	git branch -d <branch_name>
	```

- Switch to anoter branch

	```sh
	git checkout <branch_name>
	```

	**TRICK : use "git checkout -f <branch_name>" for create + switch**

Merging <a name="merging"></a>
-------

- Merge your current branch with another branch

	```sh
	git merge <another_branch>
	```

Rebasing <a name="rebase"></a>
--------

- Moves the commits unique to the current branch on top of ```<branch1>```

	```sh
	git rebase <branch1>
	```

- Moves the commits unique of ```<branch1>``` to the ```<branch2>```

	```sh
	git rebase <branch1> <branch>
	```

Undoing Changes <a name="undoing-changes"></a>
---------------

- Create a new commit that reverses of a previous commit.

	```sh
	git revert <commmit_hash>
	```

- Move your branch to previous commit

	```sh
	git reset <commit_hash>
	```

- Restore working directory files to its state at the last commit

	```sh
	git restore .
	```

Synchronizing <a name="sync"></a>
-------------

This section try to explain synchronizing local repo with remote repo.

- Add remote repo

	```sh
	git remote add <alias> <git_url>
	```

	**By default alias is "origin"**

- View all remote connections

	```sh
	git remote -v
	```

- Remove connection

	```sh
	git remote remove <alias>
	```

- Rename the alias

	```sh
	git remote rename <old_name> <new_name>
	```

- Fetch only branch from remote repo (not merge)

	```sh
	git fetch <alias> <branch>
	```

	**By default use ```git fecth``` to fetch from all branch**

- Fetch + merge from current branch use

	```sh
	git pull
	```

- Fetch + rebase from current branch use

	```sh
	git pull --rebase
	```

- Upload local repo from branch to remote repo

	```sh
	git push <alias> <branch>
	```

	**By default "git push" upload from current branch**
