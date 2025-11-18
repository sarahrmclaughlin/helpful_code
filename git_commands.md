### Terminology
- Main == Master (We should be using the phrase **Main**, but some systems need to reference the old term Master.)
- Origin/Remote - refers to the cloud Git location, i.e. the Github, Bitbucket version.
    - The code in the Main Github/Bitbucket location is our source of truth.
- Local - What is stored on your computer.
    - When you write in an editor (VSCode, etc), changes are saved locally.
    - This will be different than what is remote(in Github), until you commit the changes and push them.

#### If this is the first time creating and cloning a repo
- Create the repo in GitHub
- Add ```.gitignore file``` (this can also be done in VS Code later)
  - It is helpful to make sure this file includes things you use frequently, but don't want to push to git
  ```
  # Ignore Python cache files
    __pycache__/
    *.pyc
  # Ignore environment or IDE-specific files
  .env
  .vscode/
  .DS_Store
  # Ignore virtual environments
  venv/```
- In VScode(or your regular terminal) , cd to your repo folder, then ```git clone https://github.com/sarah/ml_ops.git```
  - (This comes from the < > button in Github)
- Make sure to initialize this repo ```git init```

#### If you are working on another branch while Main/Master just got approved with updates from another PR and you want to pull changes from Main
- ```git checkout main```
- ```git pull origin main```
- ```git checkout {your branch}```
- ```git merge main```
- in VSCode, it will ask about opening Merge Editor. ```Incoming``` means changes from **Main** branch,```Current``` is talking about your **Working** branch.

#### If the remote Main branch is updated and you want to start a new branch based off Main
- ```git checkout main```
- ```git pull origin main```
- ```git checkout -b new-branch-name```
- ```git branch ```
- ```git push -u origin new-branch-name``` #This command will push the branch and set the upstream tracking to the remote repository.

#### If a local branch is missing after you pulled Main from remote(Github), you can directly reference it
- ```git fetch```
- ```git branch -r``` -r is for remote, let's you see which remote branches are available 
- ```git switch --track origin/feat/blah/JIRATICKET-12324```
- ```git branch```
- ```git pull origin feat/blah/JIRATICKET-12324``` #gives you any updates

#### If you want to switch branches, but don't want to push your code, STASH it
- ```git stash save "Optional stash message"```
- ```git checkout -f feat/new_branch_i_want_to_switch_to``` #OR  ```- git checkout --force feat/new_branch_i_want_to_switch_to```

#### If you get an error that says: fatal: The current branch feat/mybranch has no upstream branch. 
- To push the current branch and set the remote as upstream, use:
- ```git push --set-upstream origin feat/pull_mixpanel_data```
- This is because it does not exist in git yet, you only need to run upstream once

#### If you have formatting checks or other things that don't pass, you can override this commit failure
- ```git commit -m 'updated xyz' --no-verify```

#### If you run into this error: fatal: 'origin' does not appear to be a git repository,fatal: Could not read from remote repository.
- Check if origin is set up: ```git remote -v```
- If it returns nothing, add it by: ```git remote add origin <repository-URL>```
- ```git remote add origin https://github.com/sarahrmclaughlin/evidently_ai.git```
- Then do a fetch

#### If you run into this error: 'You have divergent branches and need to specify how to reconcile them, git confi pull.rebase false(true) or .ff only
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

#### If you want to add packages you just installed to the requirements.txt (or create this file). 
- ```pip freeze > requirements.txt```

#### If you accidentally forget to add your virtual env to your .ignore file
- When adding packages automatically (above^), the virtual environment files will also be added.
  - This results in a large amount of files and you may not be able to push your changes to Git.
  - Remove them by:
    ```git rm -r -rm --cached venv/```
    
#### If you want to delete a local branch
- Delete only fully merged branches (the safer choice) ``` git branch -d feat/branch_name_to_delete ```
- Delete any branch even if not fully merged (do with caution) ``` git branch -D feat/branch_name_to_delete ```

#### If you want to add an .env to your repo
- In the terminal ```touch .env``` - You will see this pop up as a file here.
- If you are storing tokens or keys or secrets here, make sure you add this to your ```.gitignore``` file in your project repo

#### If you want to generate/integrate SSH keys
- Purpose: Securely authenticate your local computer environment with services like Github so no password is required.
- This is how we can run Git commands(push/pull/commit) and connect local(personal computer) with the remote Github repos.
- 1. Go to your home directory ```cd ~```. Verify by ```pwd``` and you should see something like ```/users/sarah```
- 2. ```cd ~/.ssh``` This changes your directory to the hidden ssh folder in your home directory
     - This is where SSH stores public and private key
- 3. Generate a new SSH key pair ssh-keygen -t rsa
     - Two files are created id_rsa (private key) and id_rsa.pub(public key added to Github account, looks like a weird image)
     - Access the public key cat ```id_rsa.pub```, copy from terminal and paste in Github
    
##### If you want to use UV as a package manager
- Can be installed within a virtual environment or outside
- UV is a tool for environment managment, it is installed globally usually here: ```~/.cargo/bin/uv```
- Check whether it is installed ```cat ~.zshrc```, or open and manually view ```open -e /.zshrc```
- ```curl -LsSf https://astral.sh/uv/install.sh | sh```
- ```uv --version```
- Usually can't find it so restart terminal manually or run ```source ~/.zshrc```
- Make sure your venv is deactivate and deleted ```rm -rf venv/```
- Within your repo, cd to your project. Here you will create a toml file which is used in UV for package management
- Copy this into your terminal, specifying project name and packages needed
- ```cat > pyproject.toml << EOF
[project]
name = "sarah_project_for_uv"
version = "0.1.0"
description = "A project for pkg management learning"
requires-python = ">=3.10"
dependencies = [
    "openai>=1.3.0, <2.0",
    "python-dotenv>=1.0.0, <2.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/sarah_project_for_uv"]
EOF```
- UV will now create the venv ```uv sync```
- Activate this new venv ```source .venv/bin/activate```
    
    
