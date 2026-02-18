---
on:
  issue_comment:
    types: [created]

permissions:
  contents: read

safe-outputs:
  add-comment:

engine:
  id: claude
  env:
    ANTHROPIC_BASE_URL: https://api.z.ai/api/anthropic
    ANTHROPIC_DEFAULT_OPUS_MODEL: glm-5
    ANTHROPIC_SMALL_FAST_MODEL: glm-5
    ANTHROPIC_DEFAULT_HAIKU_MODEL: glm-5
    ANTHROPIC_DEFAULT_SONNET_MODEL: glm-5
    CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS: "1"
    CLAUDE_CODE_SUBAGENT_MODEL: glm-5
    CLAUDE_CODE_MAX_TURNS: "10"
    CLAUDE_CODE_EFFORT_LEVEL: high
    MAX_THINKING_TOKENS: "4000"
    CLAUDE_CODE_PERMISSION_MODE: bypassPermissions
    CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC: "1"

tools:
  web-search:
  bash: true
  edit:
---

# Claude Custom Agent with Web Search

Advanced agent using custom Anthropic-compatible API endpoint with web search capability.

## Instructions

When someone comments:
- `@agent search [query]` - Search the web and summarize results
- `@agent help` - Show available commands
- `@agent status` - Show current configuration

For search queries:
1. Extract the search query from the comment
2. Use web-search tool to find information
3. Analyze and summarize top results
4. Post a concise summary with sources

## Safety

- Only respond to commands starting with `@agent`
- Summarize web results, don't copy full content
- Always cite sources
- Keep responses under 600 characters
