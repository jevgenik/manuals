============
Git
============
Git is a distributed version control system that tracks changes in any set of computer files, usually used for coordinating 
work among programmers who are collaboratively developing source code during software development

Git commands
============

* ``git remote -v`` - show remote repositories
  
* ``git branch -v`` - show local branches
  
* ``git branch -r`` - show remote branches
  
* ``git branch -a`` - show all branches (local and remote)
  
* ``git merge <branch_name>`` - merge branch_name into current branch (commits history will be saved)  
  simply put "Please add my changes to the branch I'm currently on."  

* ``git rebase <branch_name>`` - rebase current branch on top of branch_name (commits history will be rewritten by new commits from branch_name)  
  simply put "Please add my changes on top of what everybody else has already done."  


  .. note::     
     Use rebase only for local branches. Do not rebase branches others are working on. Rebase changes  
     the commit history, and others will not know about it.  


* ``git branch -m <old_name> <new_name>`` - rename branch 

To create a new repository "my_new_repository" local and remote on github.com
-----------------------------------------------------------------------------

#. Create new folder "my_new_repository"
#. ``git init`` - initialize local repository
#. ``git add .`` - add all files to staging area
#. ``git commit -m "first commit"`` - commit changes
#. ``git branch -M main`` - rename branch 'master' to 'main'
#. On github.com create new repository 'my_new_repository'
#. ``git remote add origin https://github.com/jevgenik/my_new_repository.git`` - add remote repository
#. ``git push --set-upstream origin main`` or ``git push -u origin main`` - push changes to remote repository


To develop a new feature
------------------------

#. ``git checkout new-branch`` (e.g. new-feature) - create new branch and switch to it
#. Develop new feature
#. ``git add –A`` - add all files to staging area
#. ``git commit –m "Some commit message"`` - commit changes
#. ``git checkout main`` - switch to main branch
#. ``git merge new-branch`` (e.g. new-feature) - merge new-feature into main
