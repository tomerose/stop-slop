# Reddit Post: r/ClaudeAI and r/programming

## Title
Stop Slop v1.0 — The first bilingual (CN/EN) anti-AI-writing skill for Claude Code

## Body

The original [stop-slop](https://github.com/hardikpandya/stop-slop) by Hardik Pandya hit 9,200+ stars for a good reason: it actually works. One markdown file that teaches Claude to detect and eliminate its own AI writing tells.

But it was English-only. Chinese AI writing has its own set of tells — formulaic era-openers, idiom stacking, rhetorical questions disguised as conclusions. So I forked it and added **Chinese-specific anti-pattern detection**.

**What it does:**
- 5-dimension scoring (Directness / Rhythm / Trust / Authenticity / Density)
- 41 anti-patterns detected (English + Chinese)
- Score < 35/50 → rewrite. Target ≥ 45 for publishable quality.
- Works with Claude Code, Cursor, Copilot

**Install:**
```bash
git clone https://github.com/tomerose/stop-slop.git ~/.claude/skills/stop-slop
```

**MIT. Free forever.**

If your Claude writes like a LinkedIn influencer, give it this skill.

https://github.com/tomerose/stop-slop
