##### When working on another branch while master is in a PR, approved and you want to pull changes
- ```git checkout master```
- ```git pull origin master```
- ```git checkout {your branch}```
- ```git merge master```

##### Once Master branch is updated and you want to start a new branch based off Master
- ```git checkout master```
- ```git pull origin master```
- ```git checkout -b new-branch-name```
- ```git branch ```
- ```git push -u origin new-branch-name``` #This command will push the branch and set the upstream tracking to the remote repository.

##### If a branch is missing from pulling it down in Master, you can directly reference it
- ```git fetch origin feat/blah/JIRATICKET-12324```
- ```git checkout feat/blah/JIRATICKET-12324```
- ```git branch```
- ```git pull origin feat/blah/JIRATICKET-12324``` #gives you any updates

##### If you want to switch branches, but don't want to push your code, STASH it
- ```git stash save "Optional stash message"```
- ```git checkout -f feat/new_branch_i_want_to_switch_to``` #OR  ```- git checkout --force feat/new_branch_i_want_to_switch_to```

##### If you get an error that says: fatal: The current branch feat/mybranch has no upstream branch. To push the current branch and set the remote as upstream, use
- ```git push --set-upstream origin feat/pull_mixpanel_end_to_end``` #this is because it does not exist in git yet, you only need to run upstream once

##### If you have formatting checks or other things that don't pass, you can override this commit failure
- ```git commit -m 'updated xyz' --no-verify```

##### If you run into this error: fatal: 'origin' does not appear to be a git repository,fatal: Could not read from remote repository.
- Check if origin is set up: ```git remote -v``` -if it returns nothing, add it by: ```git remote add origin <repository-URL>```
- ```git remote add origin https://github.com/sarahrmclaughlin/evidently_ai.git```
- Then do a fetch
