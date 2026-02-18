---
on:
  slash_command:
    name: summarize
    events: [issues, issue_comment]

permissions:
  contents: read
  issues: read

safe-outputs:
  add-comment:
---

# Summarize Agent

When someone types `/summarize` in an issue or comment, provide a concise summary of the discussion.

## Instructions

1. **Read the issue context** from: `${{ needs.activation.outputs.text }}`

2. **Analyze the content**:
   - What is the main topic/question?
   - What are the key points discussed?
   - Are there any decisions made or action items?
   - What is the current status?

3. **Generate a summary** with:
   - Brief overview (1-2 sentences)
   - Key points (bullet list)
   - Current status or next steps

4. **Post the summary** using `add_comment` tool:
   ```json
   {"type": "add_comment", "body": "## 📋 Summary\n\n..."}
   ```

## Example Output Format

```
## 📋 Summary

**Overview**: This issue discusses implementing dark mode support for the UI.

**Key Points**:
- Users prefer dark themes for late-night coding
- Should respect system preference automatically
- Need to maintain existing color schemes

**Status**: Feature request accepted, awaiting implementation.
```

Keep the summary concise but informative. Use markdown formatting for readability.
