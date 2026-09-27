# Artifact Studio Skill

An Agent Skill for building project-faithful interactive artifacts, components, screens, and prototypes with verified browser previews. Designed for AI coding assistants (Antigravity, OpenCode, Claude Code, Cursor, etc.).

## Features

- **Project-Faithful UI Implementation**: Reuses existing project components, design tokens, icons, and style loading chains rather than generating generic look-alike replacements.
- **Multi-Framework Adapters**: Guidance and patterns across Next.js, React, Vue, Nuxt, Angular, Svelte, Astro, and HTML/CSS/JS.
- **Verified Browser Preview**: Quality gates and local Playwright smoke helpers to inspect rendering, layout overflow, broken images, and runtime errors.
- **Defensive & Safe Execution**: Read-only bounded discovery and local loopback-only preview testing without unexpected modifications.

## Repository Structure

```text
├── SKILL.md                  # Main skill definition and instructions
├── agents/                   # Agent configuration
│   └── openai.yaml
├── assets/                   # Skill assets (icon, etc.)
│   └── icon.svg
├── references/               # Standards, contracts, and reference guides
│   ├── framework-adapters.md
│   ├── preview-delivery.md
│   ├── project-fidelity.md
│   ├── quality-gates.md
│   └── reuse-contract.md
└── scripts/                  # Bounded helper scripts
    ├── browser_smoke.mjs
    └── inspect_project.py
```

## Usage

This skill can be installed into any Agent Skills compatible environment (such as `~/.gemini/antigravity-cli/skills/artifact-studio` or `.opencode/skills/artifact-studio`).
