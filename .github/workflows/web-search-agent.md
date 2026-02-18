---
on:
  issue_comment:
    types: [created]

permissions:
  contents: read

safe-outputs:
  add-comment:

tools:
  web-search:
---

# Web Search Agent

When someone comments `@agent search [query]`, search the web and summarize findings.

## Instructions

1. Check if the comment body starts with "@agent search"
2. If yes:
   - Extract the search query (everything after "@agent search ")
   - Use the web-search tool to find information
   - Summarize the top 3 results
   - Post a reply with the summary

Example:
User: "@agent search python async best practices"
Agent: "🔍 Here's what I found about Python async best practices:

1. **Using asyncio properly** — Real Python guide covers event loops and coroutines...
2. **Avoiding common pitfalls** — Article about blocking calls and thread pools...
3. **Performance tips** — Documentation on async/await optimization..."

## Safety

- Only respond to comments starting with "@agent search"
- Summarize results, don't copy full text
- Include source URLs
- Keep response under 500 characters
- If no results found, say "No results found for [query]"
