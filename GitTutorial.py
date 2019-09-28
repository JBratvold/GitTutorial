# GIT TUTORIAL
#
# =========== SETUP ===============
# git config --global user.name "USER NAME"
# git config --global user.email "EMAIL@EMAIL.COM"
# git config --list
#

# ======= GIT HELP =============
# git help config
# git config --help


#
# 1. Navigate to the directory of the project you're working in:
#       cd PROJECT_FOLDER

# 2. A) Create a repository on your local machine:
#       git init
#    B) Clone an existing repository remotely from GitHub (This is the most common):
#       git clone https://github.com/SOMEONES_NAME/SOMEONES_PROJECT.git

# 3. Check the changes made:
#       git status

# 4. Add the changes of a file to the staging area (or use -A for all files):
#       git add FILENAME_WITH_EXTENSION
#             OR [TO REMOVE/RESET]
#       git reset FILENAME_WITH_EXTENSION
#                   OR
#       git reset

# 5. After adding changes to the staging area, commit the changes (use -m "MESSAGE" for message):
#       git commit -m "THIS IS MY USEFUL COMMIT MESSAGE EXPLAINING WHAT YOU DID"

# 6. To get the most up to date copy from the previous local commit (NOT FROM GITHUB) use:
#       git checkout -- .
#

#  ============== PUTTING STUFF TO REMOTE REPOSITORY (GITHUB) =================
# 1. After adding to stage area, and committing changes locally (#3,#4,#5), pull from the remote repository
#    to make sure your current copy is up-to-date:
#       git pull <name of repository> <branch of repository>
#       git pull origin master
#
# 2. After pulling the most up-to-date copy, you can now PUSH your files into the remote repository
#       git push <name of repository> <branch of repository>
#       git push origin master

# ============== CREATING A BRANCH FOR DESIRED PROGRAM FEATURE ====================
# 1. Create a branch from the repository:
#       git branch <desired branch name>
#       git branch ChatProgram_SaveTextInputs
#
# 2. Checkout a branch to work on
#       git checkout <branch name>
#       git branch ChatProgram_SaveTextInputs
#
# 3. To see all the branches you have locally (If it has a *, that's the one you're working on currently)
#       git branch -a
#
# 4. Push a branch to the repository
#       git push -u <name of repository> <name of branch>
#       git push -u origin ChatProgram_SaveTextInputs

# ============== MERGE A BRANCH WITH MASTER BRANCH ====================
# This is what you will do after working locally with your code, and ready to merge it to the "Final" Program
# 1. First, need to checkout the master branch:
#       git checkout master
# 2. Pull down the most recent up-to-date copy of master before we merge our copy into master
#       git pull origin master
# 3. Merge the branch you've been working on to the remote master branch
#       git merge <name of branch>
#       git merge ChatProgram_SaveTextInputs
# 4. Push those changes to the remote master
#       git push origin master

# ================ DELETING A BRANCH (WHEN IT'S FINISHED BEING WORKED ON OF COURSE) =============
# 1. Delete a local branch
#       git branch -d <name of local branch>
#       git branch -d ChatProgram_SaveTextInputs
#
# 2. Delete branch Remotely (on GitHub)
#       git push <name of repository> --delete <name of remote branch>
#       git push origin --delete ChatProgram_SaveTextInputs

print("Hello World")
