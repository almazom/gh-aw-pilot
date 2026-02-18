---
on:
  issue_comment:
    types: [created]

permissions:
  contents: read

safe-outputs:
  add-comment:

tools:
  bash: ["echo", "date", "uname", "pwd", "ls"]
---

# Bash Agent - System Info

When someone comments `@agent info`, show system information.

## Instructions

1. Check if the comment body contains "@agent info"
2. If yes, run these commands:
   - `date` - show current date/time
   - `uname -a` - show system info
   - `pwd` - show current directory
   - `ls -la` - list files
3. Post the results as a formatted comment

## Safety

- Only respond to "@agent info"
- Only use allowed bash commands
- Do not execute user input
