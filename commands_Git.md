--- Git commands ---
- `git remote -v` - show remote repositories  
- `git branch -v` - show local branches  
- `git merge <branch_name>` - merge branch_name into current branch (commits history will be saved)  
                            simply put "Please add my changes to the branch I'm currently on."  
- `git rebase <branch_name>` - rebase current branch on top of branch_name (commits history will be rewritten by new commits from branch_name)  
                             simply put "Please add my changes on top of what everybody else has already done."  

  >Note. Use rebase only for local branches. Do not rebase branches others are working on. Rebase changes   
  >the commit history, and others will not know about it.  

- `git branch -m <old_name> <new_name>` - rename branch 

For example if you have a branch called new-feature and you want to merge it into main, you would do the following:
`git checkout main`
`git merge new-feature` // merge new-feature into main
// or
`git checkout new-feature`
`git rebase main` // rebase new-feature on top of main (commits history of new-feature will be rewritten by new commits from main)

-- If you're merging a new feature into the main branch, 
you first want to switch to the main branch and then merge into it:

`git checkout new-branch` (e.g. new-feature)
# ...develop some code...

1. `git add –A`
2. `git commit –m "Some commit message"`
3. `git checkout main`  
Switched to branch 'main'  
4. `git merge new-branch` (e.g. new-feature)

### To create new repository "my_new_repository" local and remote on github.com
1. Create new folder "my_new_repository"
2. `git init` - initialize local repository
3. `git add .` - add all files to staging area
4. `git commit -m "first commit"` - commit changes
6. `git branch -M main` - rename branch `master` to `main
5. On github.com create new repository "my_new_repository"
6. `git remote add origin https://github.com/jevgenik/my_new_repository.git` - add remote repository
7. `git push --set-upstream origin main` or `git push -u origin main` - push changes to remote repository