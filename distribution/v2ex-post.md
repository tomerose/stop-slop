# V2EX 帖子：首发中文去AI味 Claude Skill

## 标题
第一个支持中文的去AI味写作技能——你的Claude终于能写人话了

## 正文（Markdown）

先看两组对比：

**修改前（AI味重）：**
> 在当今快速变化的时代，我们需要拥抱不确定性，在挑战中寻找机遇。这不仅仅是技术问题，更是一个系统性挑战。

**修改后（人话）：**
> 时代变得快。你不跟上，就被甩掉。这不是技术问题。

---

事情的起因：GitHub 上有个叫 [stop-slop](https://github.com/hardikpandya/stop-slop) 的项目火了，9200+ Star。一个纯 Markdown 文件，教 Claude 消除自己的 AI 写作口癖——喉塞开场白、二元对立、副词堆砌、假能动。

但它是纯英文的。中文 AI 写作的问题更严重：
- "在当今...的时代" 万能开头
- "不仅仅是...更是..." 万能句式
- 四字成语叠叠乐
- "综上所述/毋庸置疑/众所周知"
- 每段结尾必有一个金句

于是我把原版改了，加入 **中文专属反模式检测**，做成第一个双语去AI味 Claude Skill。

---

### 工作原理

1. 安装后，Claude 每段文字自动用 **5维评分** 检查：
   - 直接性 / 节奏 / 信任 / 真实感 / 密度
2. 低于 35/50 → 打回重写
3. 目标：45+ 分 = 读者嗅不出 AI 味

### 检测的反模式（41种）

| 英文 | 中文 |
|------|------|
| "Here's the thing:" | "在当今...的时代" |
| "Not because X. Because Y." | "不仅仅是...更是..." |
| All adverbs (-ly) | 四字成语堆砌（每段>1个） |
| "Let that sink in." | "值得我们深思" |
| em-dashes | "毋庸置疑/显而易见/众所周知" |

### 怎么用

```bash
git clone https://github.com/tomerose/stop-slop.git ~/.claude/skills/stop-slop
```

重启 Claude Code。写东西时自动生效，或手动 `/stop-slop`。

支持 Claude Code / Cursor / Copilot。

---

代码在这：https://github.com/tomerose/stop-slop

MIT 开源，永远免费。如果对你有用，点个 Star 支持。

需要定制企业 tone of voice 可以看 README 联系。

---

### 发布节点
`share` 或 `programmers` 节点

### 最佳发布时间
工作日 12:00 或 20:00
