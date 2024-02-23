Git Commands Cheat Sheet
========================

This README provides a quick reference for commonly used Git commands. GOOD LUCK!!!

Table of Contents
-----------------

1. [Install](#install)
2. [Setup](#setup)
3. [Basic Concepts](#basicconepts)
4. [Understanding Git Structure](#git-structure)
5. [Create Git Repository](#create-git-repo)
6. [Make & Show a Change](#makechange)
7. [Branching](#branching)
8. [Merging](#merging)
9. [Rebasing](#rebase)
10. [Undoing Changes](#undoing-changes)
11. [Synchronizing](#sync)
12. [Resources](#resources)

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

- Adding SSH Key on GitHub:

1. **Open GitHub**.
2. Click on your **profile icon** at the top right corner.
3. Select **"Settings"**.
4. Choose **"SSH and GPG keys"** from the sidebar.
5. Click on **"New SSH Key"**.
6. Add a descriptive title in the **"Title"** box.
7. Paste your public key in the **"Key"** box.
8. Click **"Add SSH key"** to save.

<!-- insert a picture for put key -->

Basic Concepts <a name="basicconecpts"></a>
--------------

This section explains important words in Git:

- **main**		is default branch
- **origin**	is default alias on upstream repo
- **HEAD**		is current branch
- **HEAD^**		is parant of **HEAD**
- **HEAD~2**	is grandparent of **HEAD**

> [!TIP]
> **Can change `HEAD` and `number` to branch and number what you want**

Understanding Git Structure <a name="git-structure"></a>
---------------------------

![Structure Of Git](/assets/StructureOfGit.webp)

Create Git Repository <a name="create-git-repo"></a>
--------------

### Creating a New Repository on GitHub:
	
1. **Open GitHub**.
2. Click on your **profile icon** at the top right corner.
3. Select **"New"**.
4. In the **"Repository name"** box, add the desired name for your repository.
5. Click on **"Create repository"**.

	<!-- maybe insert a picture -->

### Creating a New Repository on Your Computer:

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
### Making Changes:

- Add files to stage:

	```sh
	git add <file>
	```

> [!TIP]
> **use `.` for add all your current files**

- Commit staged files:

	```sh
	git commit -m <"recommend comment about your change">
	```

### Showing Changes:

- Shows the commit history of the current branch:

	```sh
	git log
	```

- Shows the status of your local repository:

	```sh
	git status
	```

- Shows the commit as human readable of the current branch:

	```sh
	git show <commit_hash>
	```

Branching <a name="branching"></a>
---------

- Create a new branch:

	```sh
	git branch <branch_name>
	```

- List branches:

	```sh
	git branch <flags>
	```

	*flags : -a = all branch, -r = remote branch, -v = local branch*

-  Move branch pointer, `<branch1>` to `<branch2>`:

	```sh
	git branch -f <branch1> <branch2>
	```

- Delete a branch:

	```sh
	git branch -d <branch_name>
	```

- Switch to anoter branch:

	```sh
	git checkout <branch_name>
	```

> [!TIP]
> **use `git checkout -b <branch_name>` for create + switch**

Merging <a name="merging"></a>
-------

- Merge branch into current branch:

	```sh
	git merge <another_branch>
	```

Rebasing <a name="rebase"></a>
--------

- Rebase `current branch` onto `<branch1>`:

	```sh
	git rebase <branch1>
	```

- Rebase `<branch2>` onto `<branch1>`:

	```sh
	git rebase <branch1> <branch2>
	```

Undoing Changes <a name="undoing-changes"></a>
---------------

- Create a new commit to revert a previous commit:

	```sh
	git revert <commmit_hash>
	```

- Move current branch pointer to a `<commit_hash>`:

	```sh
	git reset <commit_hash>
	```

- Restore working directory to the last commit:

	```sh
	git restore .
	```

Synchronizing <a name="sync"></a>
-------------

This section try to explain synchronizing local repo with remote repo.

- Add a remote repository:

	```sh
	git remote add <alias> <git_url>
	```

> [!NOTE]
> *By default alias is "origin"*

- View all remote connections:

	```sh
	git remote -v
	```

- Remove a remote connection:

	```sh
	git remote remove <alias>
	```

- Rename a remote alias:

	```sh
	git remote rename <old_name> <new_name>
	```

- Fetch only specific branch from remote repo (not merge):

	```sh
	git fetch <alias> <branch>
	```
	
> [!NOTE]
> *By default use `git fecth` to fetch from all branch*

- Fetch + merge from the current branch:

	```sh
	git pull
	```

- Fetch + rebase from current branch:

	```sh
	git pull --rebase
	```

- Upload local changes from `<branch>` to a remote repository:

	```sh
	git push <alias> <branch>
	```

> [!NOTE]
> *By default `git push` upload from current branch*

Resources <a name="resources"></a>
---------

Leraning more : [learngitbranching](https://learngitbranching.js.org/)

Picture :
[What is Git: Features, Command and How to Use it?](https://intellipaat.com/blog/what-is-git/)
