# docs_skills

Source: https://opencode.ai/docs/skills/

# Skills

Skills are specialized instruction sets loaded into the agent's context when a matching task is detected.

## Skill Structure

```
~/.claude/skills/<skill-name>/
├── SKILL.md        # Main skill instructions
└── ...             # Supporting files
```

## Load Skills

- Agent auto-detects relevant skills based on task description
- Use the `/skill` command to load a skill explicitly
- Skills in `~/.claude/skills/` are auto-discovered

## Built-in Skills

- `skill-watcher` — Manages the skill ecosystem
- `vps-manager` — VPS/server management
- `whatsapp-bot-reference` — WhatsApp bot patterns

## Skill Format

Skills include:
- Name and description
- Trigger conditions
- Detailed workflow instructions
- File/reference resources
