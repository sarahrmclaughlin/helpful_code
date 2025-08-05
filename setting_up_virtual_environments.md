
### How to set-up a virtual environment in VSCode

##### I did this in my terminal within VSCode

  1. Install Homebrew (add directions*)
  2. Install python ``brew install python`` and check version ```python3 --version```
  3. Install virtual environment ```pip3 install virtualenv```
  4. Run this in VScode terminal : ```python3 -m venv test_venv``` (Here test_env is the name for the virtual env and appears once activated. You only need to set it up once.)
     - After running that successfully, you will see some files generated on the left in VS code (bin, include, libpyenv.cfg)
  5. Activate Virual Environment: ```source test_venv/bin/activate```
     -  On the left hand side of the VScode terminal you will see the virtual environment name in brackets,this means it is activated/on: (test_venv). Doing this runs the activate file from the folder test_venv/bin:
     - You can also see this on file on your VS Code under the newly created folder: $activate
  6. To deactivate, in terminal: deactivate
	
 - Confirm you are in a virtual environment by doing ```which pip```
	- returns a path with your project directory and venv
	- /Users/sarahrmclaughlin/Documents/repos/check_venv/test_venv/bin/pip
 - Confirm your python version on your mac ```python3 --version```
 - After step 5, confirm your python version within your virtual environment ```python --version```

#### Step 1-4 only need to be done once
#### Steps 5 & 6 are what you need to do each time you want to work in your virtual environment.

##### If you need to delete the virtual env
```rm -rf venv```

##### If you have a requirements file with all the packages you would like installed within the virtual env
```pip install -r requirments.txt```

##### If you are trying to run python, you can select it using the Python Interpreter 
- In the top search bar type ```> Python Select Interpreter```, and find the one available in your virtual environment.

##### If you have an older python version and you need a newer one for the venv
- Make sure you are in the venv, then check the version ```python --version ```
- deactivate the venv ```deactivate```
- delete the venv ```rm -rf .venv```
- recreate it with correct python version ```python3.12 -m venv .venv```
- activate it ```source .venv/bin/activate```
- confirm python version is update ```source .venv/bin/activate```
