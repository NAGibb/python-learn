#!/bin/bash
echo "Cleaning up and backing up data"
#
# data clean up goes here


# data backup (git) goes here
cd ~/code/python-learn
git add .
git commit -m "updating learning"
git push --set-upstream origin ng_learn
git status
