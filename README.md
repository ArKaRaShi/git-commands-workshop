Git Commands Cheat Sheet
========================

This README provides a quick reference for commonly used Git commands. GOOD LUCK!!!

Table of Contents
-----------------

1. [Install](#install)
1. [Setup](#setup)
2. [Create Git Repository](#create-git-repo)
4. [Make a Change](#makechange)
3. [Branching](#branching)
4. [Merging](#merging)
5. [Rebasing](#rebase)
6. [Undoing Changes](#undoing-changes)
7. [Synchronizing](#sync)

Install <a name="install"></a>
-------

Setup <a name="setup"></a>
-----
#### git config
- you need to config git local so that githost knows you
	```sh
	git config --global user.email <"gmail">
	```
	```sh
	git config --global user.name <"git username">
	```
- if you use Linux/Mac, you need to use
	```sh
	ssh-keygen -o -t rsa -C <"gmail">
	```

	<!-- insert a picture for put key -->

Create Git Repository <a name="create-git-repo"></a>
--------------
- First make repo on githost, in this case we use github

	<!-- maybe insert a picture -->

- if you had local repo
	
	```sh
	git init <your directory>
	```
- if you had remote repo
	```sh
	git clone <url> <diretory name>
	```

Make a Change <a name="makechange"></a>
-------------

	```sh
	git add <file>
	```
	
	use "." for add all your current files
	
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
	-a = all branch, -r = remote branch, -v = local branch
- Move branch1 to branch2's commit
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
This section try to explain synchronizing local repo with remote repo
- Add remote repo
	```sh
	git remote add <alias> <git_url>
	```
	**Default alias is "origin"**
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
	**Use only "git fecth" fetch from all branch**
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
	**Use only "git push" upload from current branch**