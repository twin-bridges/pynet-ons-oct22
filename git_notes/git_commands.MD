# Git Basics  

## Set up your information
```
git config --global user.name "John Doe"  
git config --global user.email "jdoe@domain.com"  
```


## Clone a repository
```
git clone https://github.com/twin-bridges/pynet-ons
```


## Add file to a repository
```
git add my_file.py  
git commit -m "Adding my_file.py"  
```


## Remove a file/directory
```
git rm ex1_strings.py  
git rm -r <directory>
git commit -m "Removin ex1_strings.py  
```


## View status of repository and pending changes
```
git status  
git diff  
git diff <file_name>  
```


## Push changes to remote repository
```
git push origin main

where 'origin' is defined in 'git remote -v'  
where 'main' branch is the src branch; dest branch is same as src branch  
```


## Pull changes from remote repository
```
git pull origin main

where 'origin' is defined in 'git remote -v'  
where 'main' branch is the src branch; dest branch is same as src branch  
```


## Branches
```
git branch                          # Look at branches  
git branch dev                      # Create a 'dev' branch  
git checkout dev                    # Switch to 'dev' branch  
git checkout main                   # Switch back to 'main' branch  
git push origin dev                 # Push changes up to GitHub for 'dev' branch jj
git merge dev                       # merge 'dev' into main (switch to 'main' branch first)  
git branch -d dev                   # delete this branch  
git branch -vv                      # To see the remote branch that it is tracking
git branch -u origin/develop        # Set current branch to track origin/develop (must exist)
```


## Misc
```
git log                             # View the commit log  
git log -p -1                       # Show the changes in the last commit  
git stash                           # Temporarily save uncommitted changes  
git stash pop                       # Remove changes from stash and reapply to repository  
```

