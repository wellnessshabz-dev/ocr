# docs_github

Source: https://opencode.ai/docs/github/

# GitHub

GitHub integration for PR creation, issue reading, review requests, and CI checks.

## Setup

1. Connect GitHub via `/connect`
2. Or configure a GitHub app via `~/.config/opencode/github-app.yml`

## Features

- Create/update PRs
- Read issues and comments
- Request reviews
- View CI check status
- List branches

## Commands

- `/github pr create`
- `/github pr list`
- `/github issue list`
- `/github review request`
- `/github ci view`

## Permissions

Requires `repo` and `pull_requests` scopes for the personal access token or GitHub App.
