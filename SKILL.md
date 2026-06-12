---
name: stop-slop
description: Remove AI writing patterns from prose. Use when drafting, editing, or reviewing text to eliminate predictable AI tells. Triggers on: writing prose, editing drafts, reviewing content, 写作, 文案, 去AI味.
version: 1.0.0
author: MangoOS × 第三自习室
license: MIT
tags: [writing, editing, AI-detection, prose, quality, chinese, english]
marketplace:
  claude-skills: true
  cursor-skills: true
  copilot-skills: true
---

# Stop Slop — 去 AI 味写作

Eliminate predictable AI writing patterns from prose. 系统化检测并消除 AI 写作反模式。

## Core Rules

1. **Cut filler phrases.** Remove throat-clearing openers, emphasis crutches, and all adverbs. See [references/phrases.md](references/phrases.md).

2. **Break formulaic structures.** Avoid binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency. See [references/structures.md](references/structures.md).

3. **Use active voice.** Every sentence needs a human subject doing something. No passive constructions. No inanimate objects performing human actions.

4. **Be specific.** No vague declaratives. Name the specific thing. No lazy extremes ("every," "always," "never").

5. **Put the reader in the room.** No narrator-from-a-distance voice. "You" beats "People." Specifics beat abstractions.

6. **Vary rhythm.** Mix sentence lengths. Two items beat three. End paragraphs differently. No em dashes.

7. **Trust readers.** State facts directly. Skip softening, justification, hand-holding.

8. **Cut quotables.** If it sounds like a pull-quote, rewrite it.

## Quick Checks

Before delivering prose, scan for:

- [ ] Any adverbs? Kill them.
- [ ] Any passive voice? Find the actor, make them the subject.
- [ ] Inanimate thing doing a human verb? Name the person.
- [ ] Sentence starts with a Wh- word? Restructure.
- [ ] Any "here's what/this/that" throat-clearing? Cut to the point.
- [ ] Any "not X, it's Y" contrasts? State Y directly.
- [ ] Three consecutive sentences match length? Break one.
- [ ] Paragraph ends with punchy one-liner? Vary it.
- [ ] Em-dash anywhere? Remove.
- [ ] Vague declarative? Name the specific implication.
- [ ] Narrator-from-a-distance? Put the reader in the scene.
- [ ] Meta-joiners ("The rest of this essay...")? Delete.

## Scoring

Rate 1-10 on each dimension:

| Dimension | Question |
|-----------|----------|
| Directness | Statements or announcements? |
| Rhythm | Varied or metronomic? |
| Trust | Respects reader intelligence? |
| Authenticity | Sounds human? |
| Density | Anything cuttable? |

**Below 35/50: revise. Target ≥ 45/50 for publishable quality.**

## Examples

See [references/examples.md](references/examples.md) for before/after transformations.

## Chinese-Specific Notes

中文 AI 写作的额外反模式：

- **"在当今...的时代"** → 砍掉，直接说
- **"不仅仅是...更是..."** → 二元对立的中文变体
- **"值得我们深思"** → 让读者自己判断
- **"随着...的发展"** → 万能开头模板
- **"综上所述"** → 直接给结论
- **四字成语堆砌** → 每段最多1个
- **"毋庸置疑/显而易见/众所周知"** → 全砍

## License

MIT
