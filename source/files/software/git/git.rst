============
Git
============
Git is a distributed version control system that tracks changes in any set of computer files, usually used for coordinating 
work among programmers who are collaboratively developing source code during software development

Git commands
============

* ``git remote -v`` - show remote repositories (``git remote -vv`` - show remote repositories with more details)
  
* ``git branch -v`` - show local branches
  
* ``git branch -r`` - show remote branches
  
* ``git branch -a`` - show all branches (local and remote)

* ``git fetch`` - fetch changes from remote repository
  
* ``git merge <branch_name>`` - merge branch_name into current branch (commits history will be saved)  
  simply put "Please add my changes to the branch I'm currently on."  

* ``git rebase <branch_name>`` - rebase current branch on top of branch_name (commits history will be rewritten by new commits from branch_name)  
  simply put "Please add my changes on top of what everybody else has already done."  

* ``git add .`` - add all files to staging area (including untracked files)  

* ``git commit -am "Some commit message"`` - add all files to staging area and commit changes (``-a`` - add all files to staging area, ``m`` - commit message)  
  NB! Untracked files will not be added to staging area. Use ``git add .`` to add all files to staging area (including untracked files)


  .. note::     
     Use rebase only for local branches. Do not rebase branches others are working on. Rebase changes  
     the commit history, and others will not know about it.  


* ``git branch -m <old_name> <new_name>`` - rename branch 

To create a new repository local and remote on github.com
---------------------------------------------------------

#. Create new folder "my_new_repository"
#. ``git init`` - initialize local repository
#. ``git add .`` - add all files to staging area (including untracked files)
#. ``git commit -m "first commit"`` - commit changes
#. ``git branch -M main`` - rename branch 'master' to 'main'
#. On github.com create new repository 'my_new_repository'
#. ``git remote add origin https://github.com/jevgenik/my_new_repository.git`` - add remote repository
#. ``git push --set-upstream origin main`` or ``git push -u origin main`` - push changes to remote repository


To develop a new feature
------------------------

#. ``git checkout new-branch`` (e.g. new-feature) - create new branch and switch to it
#. Develop new feature
#. ``git add –A`` - add all files to staging area (the same as ``git add .``) (including untracked files)
#. ``git commit –m "Some commit message"`` - commit changes (``-a`` - add all files to staging area, ``m`` - commit message)
#. ``git checkout main`` - switch to main branch
#. ``git merge new-branch`` (e.g. new-feature) - merge new-feature into main


Credentials
===========

* ``git config --global user.name "John Doe"`` - set user name
* ``git config --global user.email "john.doe@gmail.com"`` - set user email
* ``git config --global credential.helper store`` - store credentials in plain text file (``~/.git-credentials``)  

.. warning::  
   ~/.git-credentials is not secure, but it is convenient, especially if you have many repositories.  
   If you want to use this option, you should consider encrypting your home directory.  
   See `Encrypting your home directory <https://help.ubuntu.com/community/EncryptedHome>`_ for more information.

To remove credentials from plain text file
------------------------------------------

* ``git config --global --unset credential.helper`` - unset credential helper
* ``rm ~/.git-credentials`` - remove plain text file with credentials
