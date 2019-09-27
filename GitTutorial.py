
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
# 7. DID THIS GET CHANGED?
#
#
print("Hello World")