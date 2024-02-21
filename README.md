Git Commands Cheat Sheet
========================

This README provides a quick reference for commonly used Git commands. GOOD LUCK!!!

Table of Contents
-----------------

1. [Install](#install)
1. [Setup](#setup)
2. [Create Git Repository](#create-git-repo)
3. [Branching](#branching)
4. [Merging](#merging)
5. [Undoing Changes](#undoing-changes)

Install <a name="install"></a>
-------

Setup <a name="setup"></a>
-----
#### git config
1. you need to config git local so that git host knows you
	```bash
	git config --global user.email "gmail"
	```
	```bash
	git config --global user.name "git username"
	```
2. if you use Linux/Mac, you need to use
	```bash
	ssh-keygen -o -t rsa -C "gmail"
	```

	<!-- insert a picture for put key -->

so now git host know you

Create Git Repository <a name="create-git-repo"></a>
--------------
1. First make repo on git host, in this case we use github

	<!-- maybe insert a picture -->

2. if you had directory
	
	```bash
	git init <your directory>
	```
	```bash
	git remote origin add <url>
	```
	if you don't have yet, you can git clone from repo on github
	```bash
	git clone <url> <diretory name>
	```

Branching <a name="branching"></a>
---------

Merging <a name="merging"></a>
-------

Undoing Changes <a name="undoing-changes"></a>
---------------