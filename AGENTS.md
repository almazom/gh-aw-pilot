# GitHub Agentic Workflows (gh-aw) - Agent Guide

## Project Overview

This project demonstrates GitHub Agentic Workflows (`gh aw`) - a system for creating AI-powered automation workflows on GitHub.

## Documentation Library

### Location
All documentation is cached locally in:
```
docs/kimi/
```

This folder contains **60+ HTML files** downloaded from the official GitHub Agentic Workflows documentation site (`github.github.com/gh-aw/`).

### Why Local Documentation?

The `docs/kimi/` folder serves as an offline documentation library because:
1. The official docs are comprehensive (60+ pages)
2. Internet searches may return outdated or partial information
3. HTML files contain exact syntax examples and patterns
4. Faster to grep/search locally than fetch from web

### Key Documentation Files

| File | Content |
|------|---------|
| `reference_safe-outputs.html` | All safe output types: `add-comment`, `add-labels`, `create-issue`, `update-issue`, etc. |
| `reference_frontmatter-full.html` | Complete frontmatter reference for `.md` workflow files |
| `patterns_issueops.html` | IssueOps patterns - workflows triggered by issues |
| `patterns_labelops.html` | LabelOps patterns - workflows triggered by label changes |
| `patterns_multirepoops.html` | Multi-repo operations |
| `setup_creating-workflows.html` | How to create workflows |
| `reference_compilation-process.html` | How `gh aw compile` works |
| `introduction_architecture.html` | System architecture |

### How to Use Documentation

#### 1. Search for Specific Topics

Use `grep` to find relevant documentation:

```bash
# Find all files mentioning "add-labels"
grep -l "add-labels" docs/kimi/*.html

# Find examples of specific tool usage
grep -A 10 "add-labels" docs/kimi/patterns_issueops.html

# Search for JSON format examples
grep -B 2 -A 5 '"type":' docs/kimi/patterns_*.html
```

#### 2. Extract Code Examples

HTML files contain syntax-highlighted code blocks. Extract them:

```bash
# Extract YAML examples for safe-outputs
grep -A 30 "add-labels:" docs/kimi/reference_safe-outputs.html | head -40

# Find JSON format for tool calls
grep -o '{"type":[^}]*}' docs/kimi/*.html
```

#### 3. Read Specific Sections

For detailed reading, use `cat` with line limits:

```bash
# Read safe-outputs reference (first 100 lines)
cat docs/kimi/reference_safe-outputs.html | head -100

# Search for specific section
grep -n "id=\"add-labels" docs/kimi/reference_safe-outputs.html
```

### Common Patterns from Documentation

#### Tool Call Format

The correct JSON format for tool calls is:

```json
{"type": "add_labels", "labels": ["bug", "urgent"]}
{"type": "add_comment", "body": "Your comment here"}
{"type": "create_issue", "title": "Issue title", "body": "Issue body"}
```

**Critical:** The `type` field uses **underscores**, not hyphens:
- ✅ `"add_labels"` - CORRECT
- ❌ `"add-labels"` - WRONG

#### Safe Outputs Configuration

In workflow `.md` files:

```yaml
---
safe-outputs:
  add-comment:
  add-labels:
    allowed: [bug, enhancement, documentation]
    max: 3
---
```

### Important Findings from Documentation

#### 1. `update-issue` Does NOT Support Labels

From `reference_safe-outputs.html`:
- `update-issue` only supports: `status`, `title`, `body`
- To add labels, use `add-labels` tool, NOT `update-issue`

#### 2. Engine Differences

| Engine | Supports | Notes |
|--------|----------|-------|
| Copilot (default) | Basic tools | May hallucinate tool names |
| Claude | Web search, advanced tools | Requires `ANTHROPIC_API_KEY` |
| OpenAI | All tools | Requires `OPENAI_API_KEY` |

#### 3. Compilation Required

After editing `.md` files:
```bash
gh aw compile
```

This generates `.lock.yml` files that are actually used by GitHub Actions.

### Troubleshooting with Documentation

When workflows fail:

1. **Check safe-output artifacts**:
   ```bash
   gh run download <run-id> --name safe-output --dir /tmp/safe
   cat /tmp/safe/outputs.jsonl
   ```

2. **Verify tool names in docs**:
   ```bash
   grep "name.*add_labels" docs/kimi/reference_safe-outputs.html
   ```

3. **Check JSON format**:
   ```bash
   grep -B 2 -A 5 '"type": "add_labels"' docs/kimi/patterns_*.html
   ```

### Quick Reference Commands

```bash
# List all documentation files
ls docs/kimi/*.html

# Find pattern across all docs
grep -r "your-pattern" docs/kimi/

# Get example workflows
grep -A 20 "expressive-code" docs/kimi/patterns_issueops.html

# Check specific tool documentation
grep -A 50 'id="add-labels' docs/kimi/reference_safe-outputs.html
```

### Maintenance

The documentation was downloaded using:
```bash
./download_docs.sh
```

To update documentation, re-run the script (requires internet connection to `github.github.com/gh-aw/`).

---

## Workflow Development Best Practices

1. **Always compile after editing**:
   ```bash
   gh aw compile
   ```

2. **Test with simple issues first**:
   ```bash
   gh issue create --title "Test" --body "Test body"
   ```

3. **Check run logs**:
   ```bash
   gh run view <run-id> --job=<job-id> --log
   ```

4. **Download artifacts for debugging**:
   ```bash
   gh run download <run-id> --name safe-output
   ```

5. **Use local docs before searching web**:
   ```bash
   # Prefer this
   grep -r "pattern" docs/kimi/
   
   # Over this
   search_web "gh-aw pattern"
   ```
