# Reddit Post: r/ClaudeAI

## Title
Your Claude writes like a LinkedIn influencer. This skill fixes that.

## Body

Read this. Three seconds. Can you smell the AI?

> "In today's rapidly evolving landscape, organizations must embrace uncertainty and leverage systematic innovation to navigate emerging challenges. This isn't merely a technological shift — it's a fundamental strategic transformation."

Of course you can. Throat-clearing opener. Binary contrast. Jargon stack. Three tells in two sentences.

Now the human version:

> "The world moves faster than your company. Adapt or die. This isn't a tech problem."

**Same message. Actual bones. Reads like a person wrote it.**

---

### What this is

[stop-slop](https://github.com/hardikpandya/stop-slop) by Hardik Pandya hit 9,200+ stars on GitHub. One markdown file. Zero code. It teaches Claude to detect and eliminate its own AI writing tells.

I forked it and added **Chinese-specific anti-pattern detection** — the first bilingual version. Because Chinese AI writing has its own set of tells that are arguably worse than English ones.

**What it catches (41 patterns total):**

| English | Chinese |
|---------|---------|
| "Here's the thing:" | "在当今...的时代" |
| "Not because X. Because Y." | "不仅仅是...更是..." |
| All -ly adverbs | 四字成语叠叠乐 (idiom stacking) |
| "Let that sink in." | "值得我们深思" |
| Vague declaratives | 万能金句结尾 |

**5-dimension scoring:** Directness / Rhythm / Trust / Authenticity / Density. Score < 35/50 → rewrite. Target ≥ 45.

---

### Install

```bash
git clone https://github.com/tomerose/stop-slop.git ~/.claude/skills/stop-slop
```

Works with Claude Code, Cursor, Copilot. Restart and it's active.

---

### Why this matters

Two numbers:
- **82%** of creators use AI daily
- **76%** of readers can identify AI slop in under 3 seconds

Your readers are faster than your model. Stop Slop closes that gap.

🔗 https://github.com/tomerose/stop-slop

**MIT. Free forever.** If it saves you editing time, drop a Star.
