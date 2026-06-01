# docs_gitlab

Source: https://opencode.ai/docs/gitlab/

# GitLab

GitLab integration for MR (merge request) creation, issue management, and CI.

## Setup

Connect via `/connect` and provide the GitLab personal access token and instance URL.

## Features

- Create/update merge requests
- Read issues
- View pipeline status
- List branches

## Commands

- `/gitlab mr create`
- `/gitlab mr list`
- `/gitlab issue list`
- `/gitlab pipeline view`

## Permissions

Requires `api` scope on the personal access token.
