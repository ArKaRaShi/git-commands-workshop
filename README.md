Git Commands Cheat Sheet
========================

This README provides a quick reference for commonly used Git commands. GOOD LUCK!!!

Table of Contents
-----------------

1. [Install](#install)
2. [Setup](#setup)
3. [Basic Concepts](#basicconepts)
5. [Create Git Repository](#create-git-repo)
6. [Make a Change](#makechange)
7. [Branching](#branching)
8. [Merging](#merging)
9. [Rebasing](#rebase)
10. [Undoing Changes](#undoing-changes)
11. [Synchronizing](#sync)

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
	
	Open github -> Click profile github at top right -> **Settings** -> **SSH and GPG keys** -> **New SSH Key** -> Add **"Title"** box and paste public key in **"Key"** box -> **Add SSH key**
	<!-- insert a picture for put key -->

Basic Concepts <a name="basicconecpts"></a>
--------------

This section will explain about important words in git

- **main** is default branch
- **origin** is default alias on upstream repo
- **HEAD** is current branch
- **HEAD^** is parant of **HEAD**
- **HEAD~2** is grandparent of **HEAD**

**TRICK : Can change "HEAD" and number to branch and number what you want**

Create Git Repository <a name="create-git-repo"></a>
--------------

- First make repo on githost, in this case we use github.

	Open github -> Click profile github at top right -> **New** -> Add name of repo in **"Repository name"** box -> **Create repository**
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

- Add files to stage

	```sh
	git add <file>
	```

	**use "." for add all your current files**

- Commit all staged files to git repo

	```sh
	git commit -m <"recommend comment about your change">
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

- Move branch1 to branch2's point

	```sh
	git branch -f branch1 branch2
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

- "git rebase" gives the branch2 connect with branch1,
given branch1 is base

	```sh
	git rebase <branch1> <branch2>
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

	**By default "git fecth" fetch from all branch**

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
