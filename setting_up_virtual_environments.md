
### How to set-up a virtual environment in VSCode

##### I did this in my terminal within VSCode

  1. Install Homebrew (add directions*)
  2. Install python ``brew install python`` and check version ```python3 --version```
  3. Install virtual environment ```pip3 install virtualenv```
  4. Run this in VScode terminal : ```python3 -m venv test_venv``` (Here test_env is the name for the virtual env and appears once activated
  5. After running that successfully, you will see some files generated on the left in VS code (bin, include, libpyenv.cfg)
  7. Activate Virual Environment: ```source test_venv/bin/activate```
  8.  On the left hand side of the VScode terminal you will see the virtual environment name in brackets,this means it is activated/on: (test_venv). Doing this runs the activate file from the folder test_venv/bin:
  9.  You can also see this on file on your VS Code under the newly created folder: $activate
  10. To deactivate, in terminal: deactivate
	
 - Confirm you are in a virtual environment by doing ```which pip```
	- returns a path with your project directory and venv
	- /Users/sarahrmclaughlin/Documents/repos/check_venv/test_venv/bin/pip

#### Step 1-3 only need to be done once
#### Steps 6 & 10 are what you need to do each time you want to work in your virtual environment.

##### If you need to delete the virtual env
```rm -rf venv```

##### If you have a requirements file with all the packages you would like installed within the virtual env
```pip install -r requirments.txt```
