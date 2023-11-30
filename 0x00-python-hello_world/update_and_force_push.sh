#!/bin/bash

# Add all changes
git add .

# Amend the last commit without changing the commit message
git commit --amend --no-edit

# Force push the changes to the 'master' branch
git push origin master --force

