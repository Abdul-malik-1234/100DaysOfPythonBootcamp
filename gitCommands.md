#Git HELP commands
**git help** -> getting general help
**git help command** ->  getting help about a specific Git command

#Git Configuration Commands
##What's the current directory (present working directory)?
pwd
Git Config (Global/User-level) Syntax
git config --global setting value
##Configure User and Email
###General Syntax:

git config --global user.name "Your Name"
git config --global user.email "you@someplace.com"
##Example using course author's information:

git config --global user.name "Jason Taylor"
git config --global user.email "jason@jasongtaylor.com"
##Listing All Global Configuration Settings
git config --global --list
##Seeing Git's User-based Config file
cat ~/.gitconfig

#Starting Commands
Git Starting Commands
 

##Lecture Command Listing - Fresh Start
pwd
cd projects/
git init git-demo
 

##Lecture Command Listing - Start with Existing Project
pwd
cd projects/
cd website/
ls
git init
 

##Git initialization

git init [project-name]
project-name parameter is optional. If not supplied, Git will initialize the current directory.


#First Commit Commands
##Git First Commit Commands
 

Lecture Command Listing
pwd
ls
mate README.md
ls
git status
git add README.md
git status
git commit -m "Initial commit"
clear
git status
 

Command Reference
List

ls
Lists files and folders in current directory. Without parameters, will list non-hidden folders and files.

##Git Status

git status
Shows which files have been modified in the working directory vs Git's staging area.

##Git Add

git add file-name
Adds the new or newly modified file-name to Git's staging area (index).

##Git Commit

git commit -m "A really good commit message"
Commits all files currently in Git's staging area. The -m parameter allows for a commit message directly from the command line.

##Clear!

clear
Clears all previous commands from the terminal screen -- just a bit of clean up.
