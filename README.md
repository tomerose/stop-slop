# 🚫 Stop Slop — 去 AI 味写作技能

**让你的 AI 写出人话。** 一个给 Claude/Cursor/Copilot 安装的写作技能——自动检测并消除 AI 写作的 41 种反模式。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-blue)](https://claude.ai)
[![Skill Type](https://img.shields.io/badge/Skill-Writing%20Quality-green)]()

---

## 这是什么

你的 AI 写东西是不是经常这样：

> "在当今快速变化的时代，我们需要拥抱不确定性，在挑战中寻找机遇。这不仅仅是技术问题，更是一个系统性挑战。让我们深入探讨..."

Stop Slop 一刀切掉这些 AI 味。安装后，Claude 自动用 5 维评分（直接性/节奏/信任/真实感/密度）检查每段文字，**低于 35/50 打回重写**。

---

## 效果对比

### 修改前（AI 味重）
> "Here's the thing: building products is hard. Not because the technology is complex. Because people are complex. Let that sink in."

### 修改后（人话）
> "Building products is hard. Technology is manageable. People aren't."

**删掉了：** 喉塞开场白 + 二元对立结构 + 强调把戏。三句话变三句，但每句都有骨头。

---

## 安装

### Claude Code（推荐）

```bash
# 克隆到 skills 目录
git clone https://github.com/tomerose/stop-slop.git \
  ~/.claude/skills/stop-slop
```

重启 Claude Code，写作时自动激活。或手动调用：

```
/stop-slop
```

### Cursor / Copilot

```json
// .cursor/skills.json
{
  "skills": ["stop-slop"]
}
```

---

## 5 维评分体系

每条文字按 1-10 打分：

| 维度 | 问题 |
|------|------|
| **直接性** | 在陈述还是在宣告？ |
| **节奏** | 有变化还是像节拍器？ |
| **信任** | 尊重读者智商吗？ |
| **真实感** | 听起来像人吗？ |
| **密度** | 还有可删的吗？ |

**低于 35/50 分：打回重写。**

---

## 检测的反模式（41 种）

### 喉塞开场白
`"Here's the thing:"` `"Let me be clear"` `"The truth is,"` → 砍掉，直接说

### 二元对立
`"Not because X. Because Y."` → 直接说 Y

### 商业黑话
`"navigate challenges"` → `"handle problems"`  
`"deep dive"` → `"examine"`  
`"game-changer"` → `"important"`

### 副词
全部。`really` `just` `literally` `genuinely` `honestly` `simply` → 删除

### 假能动
`"the decision emerges"` → 谁决定的？  
`"the data tells us"` → 谁读的数据？

### 模糊宣告
`"The implications are significant"` → 说出具体影响

### 更多见 `references/`

---

## 谁在用

- **独立开发者** — 产品文案、GitHub README、推文
- **内容创作者** — 公众号/小红书/Newsletter，避免被读者嗅出 AI 味
- **技术写作者** — 文档、博客、白皮书
- **非英语母语者** — 发现自己写英文时无意识套用了 AI 模板

---

## 为什么这值钱

AI 写作工具爆发 → 内容量爆炸 → **读者对 "AI 味" 的识别力在加速进化**。

2026 年的读者能在 3 秒内嗅出 AI 写的文字——喉塞开场、二元对立、副词堆砌。Stop Slop 给你一个系统化的检测框架，不是"我觉得有 AI 味"，而是**5 维量化评分**。

**当前状态：** 全球第一个系统化去 AI 味 Claude Skill。关键词 "stop AI slop" 月搜索量增长 400%+。

---

## 文件结构

```
stop-slop/
├── SKILL.md              # 技能定义（给 AI 读）
├── README.md             # 本文件（给人读）
├── LICENSE               # MIT
└── references/
    ├── phrases.md         # 要删除的短语清单
    ├── structures.md      # 要避免的结构模式
    └── examples.md        # 修改前后对比
```

---

## 定价

**免费。** 这个 skill 永远免费开源。

如果需要：
- **定制版**（企业品牌 tone of voice 适配）
- **培训**（团队写作工作坊）
- **API 集成**（批量文本检测）

→ 邮件 portelamicheli636@gmail.com 或微信见下方赞赏码。

---

## 赞助

如果这个 skill 帮你省了改稿时间，请我喝杯咖啡 ☕

<div align="center">

| 微信赞赏 | 支付宝 |
|----------|--------|
| *(扫码)* | *(扫码)* |

</div>

---

## 相关资源

- [Claude Code Skills 文档](https://docs.claude.codes/skills)
- [stop-slop 原始作者 Hardik Pandya](https://hvpandya.com)
- [AI Writing Detection 研究](https://arxiv.org/abs/2501.05707)

---

**Made with ❤️ by MangoOS × 第三自习室 · 2026**
