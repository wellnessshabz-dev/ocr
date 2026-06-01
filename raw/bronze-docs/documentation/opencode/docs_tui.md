# docs_tui

Source: https://opencode.ai/docs/tui/

[Skip to content](https://opencode.ai/docs/tui/#_top)

# TUI

Using the OpenCode terminal user interface.

OpenCode provides an interactive terminal interface or TUI for working on your projects with an LLM.

Running OpenCode starts the TUI for the current directory.

```
opencode
```

Or you can start it for a specific working directory.

```
opencode /path/to/project
```

Once you’re in the TUI, you can prompt it with a message.

```
Give me a quick summary of the codebase.
```

* * *

## [File references](https://opencode.ai/docs/tui/\#file-references)

You can reference files in your messages using `@`. This does a fuzzy file search in the current working directory.

```
How is auth handled in @packages/functions/src/api/index.ts?
```

The content of the file is added to the conversation automatically.

Configured references also appear in `@` autocomplete. Type `@alias` to add the reference root as context, or type `@alias/` to autocomplete files inside that reference.

```
Compare our setup with @docs/README.md
```

* * *

## [Bash commands](https://opencode.ai/docs/tui/\#bash-commands)

Start a message with `!` to run a shell command.

```
!ls -la
```

The output of the command is added to the conversation as a tool result.

* * *

## [Commands](https://opencode.ai/docs/tui/\#commands)

When using the OpenCode TUI, you can type `/` followed by a command name to quickly execute actions. For example:

```
/help
```

Most commands also have keyboard shortcuts using `ctrl+x` as the default leader key. [Learn more](https://opencode.ai/docs/keybinds).

Here are all available slash commands:

* * *

### [connect](https://opencode.ai/docs/tui/\#connect)

Add a provider to OpenCode. Allows you to select from available providers and add their API keys.

```
/connect
```

* * *

### [compact](https://opencode.ai/docs/tui/\#compact)

Compact the current session. _Alias_: `/summarize`

```
/compact
```

**Keybind:**`ctrl+x c`

* * *

### [details](https://opencode.ai/docs/tui/\#details)

Toggle tool execution details.

```
/details
```

* * *

### [editor](https://opencode.ai/docs/tui/\#editor)

Open external editor for composing messages. Uses the editor set in your `EDITOR` environment variable. [Learn more](https://opencode.ai/docs/tui/#editor-setup).

```
/editor
```

**Keybind:**`ctrl+x e`

* * *

### [exit](https://opencode.ai/docs/tui/\#exit)

Exit OpenCode. _Aliases_: `/quit`, `/q`

```
/exit
```

**Keybind:**`ctrl+x q`

* * *

### [export](https://opencode.ai/docs/tui/\#export)

Export current conversation to Markdown and open in your default editor. Uses the editor set in your `EDITOR` environment variable. [Learn more](https://opencode.ai/docs/tui/#editor-setup).

```
/export
```

**Keybind:**`ctrl+x x`

* * *

### [help](https://opencode.ai/docs/tui/\#help)

Show the help dialog.

```
/help
```

* * *

### [init](https://opencode.ai/docs/tui/\#init)

Guided setup for creating or updating `AGENTS.md`. [Learn more](https://opencode.ai/docs/rules).

```
/init
```

* * *

### [models](https://opencode.ai/docs/tui/\#models)

List available models.

```
/models
```

**Keybind:**`ctrl+x m`

* * *

### [new](https://opencode.ai/docs/tui/\#new)

Start a new session. _Alias_: `/clear`

```
/new
```

**Keybind:**`ctrl+x n`

* * *

### [redo](https://opencode.ai/docs/tui/\#redo)

Redo a previously undone message. Only available after using `/undo`.

Internally, this uses Git to manage the file changes. So your project **needs to**
**be a Git repository**.

```
/redo
```

**Keybind:**`ctrl+x r`

* * *

### [sessions](https://opencode.ai/docs/tui/\#sessions)

List and switch between sessions. _Aliases_: `/resume`, `/continue`

```
/sessions
```

**Keybind:**`ctrl+x l`

* * *

Share current session. [Learn more](https://opencode.ai/docs/share).

```
/share
```

* * *

### [themes](https://opencode.ai/docs/tui/\#themes)

List available themes.

```
/themes
```

**Keybind:**`ctrl+x t`

* * *

### [thinking](https://opencode.ai/docs/tui/\#thinking)

Toggle the visibility of thinking/reasoning blocks in the conversation. When enabled, you can see the model’s reasoning process for models that support extended thinking.

```
/thinking
```

* * *

### [undo](https://opencode.ai/docs/tui/\#undo)

Undo last message in the conversation. Removes the most recent user message, all subsequent responses, and any file changes.

Internally, this uses Git to manage the file changes. So your project **needs to**
**be a Git repository**.

```
/undo
```

**Keybind:**`ctrl+x u`

* * *

### [unshare](https://opencode.ai/docs/tui/\#unshare)

Unshare current session. [Learn more](https://opencode.ai/docs/share#un-sharing).

```
/unshare
```

* * *

## [Editor setup](https://opencode.ai/docs/tui/\#editor-setup)

Both the `/editor` and `/export` commands use the editor specified in your `EDITOR` environment variable.

- [Linux/macOS](https://opencode.ai/docs/tui/#tab-panel-4)
- [Windows (CMD)](https://opencode.ai/docs/tui/#tab-panel-5)
- [Windows (PowerShell)](https://opencode.ai/docs/tui/#tab-panel-6)

```
# Example for nano or vim

export EDITOR=nano

export EDITOR=vim

# For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.

# include --wait

export EDITOR="code --wait"
```

To make it permanent, add this to your shell profile;
`~/.bashrc`, `~/.zshrc`, etc.

```
set EDITOR=notepad

# For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.

# include --wait

set EDITOR=code --wait
```

To make it permanent, use **System Properties** \> **Environment**
**Variables**.

```
$env:EDITOR = "notepad"

# For GUI editors, VS Code, Cursor, VSCodium, Windsurf, Zed, etc.

# include --wait

$env:EDITOR = "code --wait"
```

To make it permanent, add this to your PowerShell profile.

Popular editor options include:

- `code` \- Visual Studio Code
- `cursor` \- Cursor
- `windsurf` \- Windsurf
- `nvim` \- Neovim editor
- `vim` \- Vim editor
- `nano` \- Nano editor
- `notepad` \- Windows Notepad
- `subl` \- Sublime Text

Some editors need command-line arguments to run in blocking mode. The `--wait` flag makes the editor process block until closed.

* * *

## [Configure](https://opencode.ai/docs/tui/\#configure)

You can customize TUI behavior through `tui.json` (or `tui.jsonc`).

```
{

  "$schema": "https://opencode.ai/tui.json",

  "theme": "opencode",

  "leader_timeout": 2000,

  "keybinds": {

    "leader": "ctrl+x",

    "command_list": "ctrl+p"

  },

  "scroll_speed": 3,

  "scroll_acceleration": {

    "enabled": false

  },

  "diff_style": "auto",

  "mouse": true,

  "attention": {

    "enabled": true,

    "notifications": true,

    "sound": true,

    "volume": 0.4,

    "sound_pack": "opencode.default",

    "sounds": {

      "error": "./sounds/error.mp3"

    }

  }

}
```

This is separate from `opencode.json`, which configures server/runtime behavior.

`keybinds` is merged with built-in defaults, so you only need to configure the shortcuts you want to change.

### [Options](https://opencode.ai/docs/tui/\#options)

- `theme` \- Sets your UI theme. [Learn more](https://opencode.ai/docs/themes).
- `keybinds` \- Customizes keyboard shortcuts. [Learn more](https://opencode.ai/docs/keybinds).
- `leader_timeout` \- Controls how long OpenCode waits after the leader key. Defaults to `2000`.
- `scroll_acceleration.enabled` \- Enable macOS-style scroll acceleration for smooth, natural scrolling. When enabled, scroll speed increases with rapid scrolling gestures and stays precise for slower movements. **This setting takes precedence over `scroll_speed` and overrides it when enabled.**
- `scroll_speed` \- Controls how fast the TUI scrolls when using scroll commands (minimum: `0.001`, supports decimal values). Defaults to `3`. **Note: This is ignored if `scroll_acceleration.enabled` is set to `true`.**
- `diff_style` \- Controls diff rendering. `"auto"` adapts to terminal width, `"stacked"` always shows a single-column layout.
- `mouse` \- Enable or disable mouse capture in the TUI (default: `true`). When disabled, the terminal’s native mouse selection/scrolling behavior is preserved.
- `attention` \- Configures TUI desktop notifications and sounds. Disabled by default.

Use `OPENCODE_TUI_CONFIG` to load a custom TUI config path.

### [Attention](https://opencode.ai/docs/tui/\#attention)

The TUI can request attention for questions, permissions, session errors, and completed sessions. Enable it with `attention.enabled`; built-in events play sounds when triggered, and non-subagent events request desktop notifications only when the terminal is blurred.

- `enabled` \- Enable all attention notifications and sounds. Defaults to `false`.
- `notifications` \- Allow terminal-mediated desktop notifications when attention is enabled. Defaults to `true`.
- `sound` \- Allow attention sounds when attention is enabled. Defaults to `true`.
- `volume` \- Default sound volume from `0` to `1`. Defaults to `0.4`.
- `sound_pack` \- Sound pack ID to use. Defaults to `opencode.default`.
- `sounds` \- Override sound files for `default`, `question`, `permission`, `error`, `done`, or `subagent_done`. Paths can be absolute, `file://` URLs, or relative to `tui.json`.

* * *

## [Customization](https://opencode.ai/docs/tui/\#customization)

You can customize various aspects of the TUI view using the command palette (`ctrl+p`). These settings persist across restarts.

* * *

#### [Username display](https://opencode.ai/docs/tui/\#username-display)

Toggle whether your username appears in chat messages. Access this through:

- Command palette: Search for “username” or “hide username”
- The setting persists automatically and will be remembered across TUI sessions