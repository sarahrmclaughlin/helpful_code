##### When working on another branch while Main just got approved with updates from another PR and you want to pull changes from Main
- ```git checkout master```
- ```git pull origin master```
- ```git checkout {your branch}```
- ```git merge master```
- in VSCode, it will ask about opening Merge Editor. ```Incoming`` means changes from **Main** branch and ``Current`` is talking about your working branch.

##### Once Master branch is updated and you want to start a new branch based off Main
- ```git checkout master```
- ```git pull origin master```
- ```git checkout -b new-branch-name```
- ```git branch ```
- ```git push -u origin new-branch-name``` #This command will push the branch and set the upstream tracking to the remote repository.

##### If a branch is missing from pulling it down in Main, you can directly reference it
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

##### If you run into this error: 'You have divergent branches and need to specify how to reconcile them, git confi pull.rebase false(true) or .ff only
- This usually happens when you are working on a branch and are trying to switch without pulling first. You can try the suggestions, but it usually doesn't help.
- If you've already saved the changes of what you are working on or are fine with starting from scratch , you can follow these steps.
- ***BE EXTRA CAREFUL IN DOING THIS**** *This deletes and recreates your repo. MAKE SURE EVERYTHING IS PUSHED REMOTELY ALREADY*
- ```cd ..```
- ```rm rf name_of_repo_to_be_deleted_and_recreated```
- Description of both```rm``` remove/delete, ```rf``` recursive format/forced delete, this will completely delete your local repo
- That specific repo will be gone after these commands
- Then reclone the repo locally.
- git clone git@github.com:sarah/sarah_previously_delete_repo
- *This can also be used when you have a bunch of local repos that you want to clean up. Excessive branchery*
- cd into the repo within your workspace
- you will need to initialize this repo ```git init``` and/or run your `Makefile` ```make setup``` in order to have git initialized and have your hooks to connect to remote Git
  
