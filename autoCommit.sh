#!/bin/bash

# Settings
GITHUB_USERNAME="hammad-sarfraz-1"
REPO_NAME="minikube-app"
REPO_PATH="/home/geek/mlops_assign"
COMMIT_MESSAGE="Auto-commit by $GITHUB_USERNAME"
INTERVAL=216000  # Every 6 hrs

# Move into repo directory
cd "$REPO_PATH" || { echo "Repository path not found!"; exit 1; }

# Infinite loop
while true; do
    # Check if there are changes
    if [ -n "$(git status --porcelain)" ]; then
        git add .
        git commit -m "$COMMIT_MESSAGE $(date '+%Y-%m-%d %H:%M:%S')"
        git push
        echo "Changes pushed at $(date)"
    else
        echo "No changes to commit at $(date)"
    fi
    sleep "$INTERVAL"
done
