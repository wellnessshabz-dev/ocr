# OpenCode Command Quick Reference

## When to use what

| You want to... | Use this | Instead of... |
|---|---|---|
| Read a file | `read` | cat, head, tail |
| List directory contents | `read` (on a dir) | ls |
| Search file contents | `grep` | grep, rg |
| Find files by name pattern | `glob` | find, ls |
| Edit a specific line/block | `edit` | sed, awk |
| Create/overwrite a file | `write` | echo >, cat << EOF |
| Run git, npm, docker etc. | `bash` | — |
| Search the web | `websearch` | — |
| Fetch a URL | `webfetch` | curl |
| Research codebase patterns | `task` (explore agent) | manual digging |
| Multi-step work | `task` (general agent) | sequential reads |
| Ask you a question | `question` | guessing |
| Track progress | `todowrite` | mental notes |
| Load domain expertise | `skill` | prompting from scratch |

## Golden rules

1. **Always `read` before `edit`** — edits fail if you haven't read the file first
2. **`edit` needs unique context** — if `oldString` matches multiple times, add more surrounding lines
3. **`bash` = last resort for file ops** — use `read`/`write`/`edit`/`grep`/`glob` instead
4. **Parallel calls are fine** — independent tool calls in one message run simultaneously
5. **Sequential work needs chaining** — use `&&` in bash, or send separate messages

## Examples

```
read /path/to/file.py           # see contents
read /path/to/dir               # list directory
grep pattern file.py            # search for pattern
glob "src/**/*.ts"              # find all ts files
edit file.py "old" "new"        # replace exact text
write /path/to/file "content"   # create file
bash "npm run test"             # run tests
websearch "topic 2026"          # search web
webfetch "https://example.com"  # fetch URL
```
