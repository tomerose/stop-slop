"""Auto-post stop-slop to V2EX/Reddit/Twitter using browser cookies."""
import os, sys, json, time, urllib.request, urllib.parse, ssl
from pathlib import Path

# ── V2EX Poster ──
def post_v2ex(title, content, node="share"):
    """Post to V2EX using cookies extracted from browser."""
    print("\n📮 V2EX 发帖中...")

    # V2EX login URL
    body = urllib.parse.urlencode({
        "title": title,
        "content": content,
        "node_name": node,
    }).encode()

    # Try posting — V2EX checks cookies + CSRF once token
    # First get once token
    try:
        ctx = ssl.create_default_context()
        req = urllib.request.Request(
            f"https://www.v2ex.com/write?node={node}",
            headers={"User-Agent": "Mozilla/5.0 Chrome/130.0"}
        )
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            html = resp.read().decode()
            import re
            once_match = re.search(r'name="once" value="(\d+)"', html)
            if once_match:
                once = once_match.group(1)
                print(f"  CSRF token: {once[:10]}...")

                # POST with once token
                post_body = urllib.parse.urlencode({
                    "title": title,
                    "content": content,
                    "node_name": node,
                    "once": once,
                }).encode()

                post_req = urllib.request.Request(
                    "https://www.v2ex.com/write",
                    data=post_body,
                    headers={
                        "User-Agent": "Mozilla/5.0 Chrome/130.0",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Referer": f"https://www.v2ex.com/write?node={node}",
                        "Origin": "https://www.v2ex.com",
                    }
                )
                with urllib.request.urlopen(post_req, timeout=15, context=ctx) as pr:
                    result_url = pr.geturl()
                    if "/t/" in result_url:
                        print(f"  ✅ 发布成功: {result_url}")
                        return result_url
                    else:
                        print(f"  ⚠ 跳转: {result_url} (可能需要登录)")
                        return None
            else:
                print("  ⚠ 未找到 CSRF token (需要先登录 V2EX)")
                return None
    except Exception as e:
        print(f"  ❌ V2EX 发帖失败: {e}")
        return None


def post_reddit(subreddit, title, content):
    """Post to Reddit using rdt CLI."""
    import subprocess
    print(f"\n📮 Reddit r/{subreddit} 发帖中...")

    # Write content to temp file
    tmpfile = Path(os.environ["TEMP"]) / "reddit_post.txt"
    tmpfile.write_text(f"{title}\n\n{content}", encoding="utf-8")

    result = subprocess.run(
        ["rdt", "submit", subreddit, title, "--body-file", str(tmpfile)],
        capture_output=True, text=True, timeout=30
    )
    print(result.stdout)
    if result.returncode == 0:
        print(f"  ✅ Reddit 发布成功")
    else:
        print(f"  ❌ Reddit 失败: {result.stderr[:200]}")
    return result.returncode == 0


def post_twitter(content):
    """Post to Twitter using twitter CLI."""
    import subprocess
    print(f"\n📮 Twitter 发帖中...")

    result = subprocess.run(
        ["twitter", "tweet", content],
        capture_output=True, text=True, timeout=30
    )
    print(result.stdout[:500])
    if result.returncode == 0:
        print(f"  ✅ Twitter 发布成功")
    else:
        print(f"  ❌ Twitter 失败: {result.stderr[:200]}")
    return result.returncode == 0


# ── Main ──
if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "all"

    # V2EX post content
    v2ex_title = "第一个支持中文的去AI味写作Skill — 让你的Claude写出人话（开源）"
    v2ex_body = """先看两组对比：

修改前（AI味重）：
> 在当今快速变化的时代，我们需要拥抱不确定性，在挑战中寻找机遇。这不仅仅是技术问题，更是一个系统性挑战。

修改后（人话）：
> 时代变得快。你不跟上，就被甩掉。这不是技术问题。

---

GitHub 上 stop-slop 项目火了（9200+ Star）。一个纯 Markdown 文件，教 Claude 消除 AI 写作口癖——喉塞开场白、二元对立、副词堆砌、假能动。

但它是纯英文的。中文 AI 写作问题更严重：
- "在当今...的时代" 万能开头
- "不仅仅是...更是..." 万能句式
- 四字成语叠叠乐
- "综上所述/毋庸置疑/众所周知"
- 每段结尾必有一个金句

于是我做了第一个双语版：加入中文专属反模式检测，5维评分体系，41种反模式。

安装：
git clone https://github.com/tomerose/stop-slop.git ~/.claude/skills/stop-slop

重启 Claude Code，自动生效。支持 Claude Code / Cursor / Copilot。

代码：https://github.com/tomerose/stop-slop
MIT 开源，永远免费。点个 Star 支持。

P.S. 另外做了个免费 Newsletter：经济学+AI 每日简报 https://newsletter-landing-mgw171vf9-mango-s-projects5.vercel.app"""

    if action in ("all", "v2ex"):
        post_v2ex(v2ex_title, v2ex_body)

    if action in ("all", "reddit"):
        reddit_title = "Stop Slop v1.0 — First bilingual (CN/EN) anti-AI-writing skill for Claude Code"
        reddit_body = """The original stop-slop by Hardik Pandya hit 9,200+ stars for a reason: it works. One markdown file that teaches Claude to detect and eliminate its own AI writing tells.

But it was English-only. Chinese AI writing has its own tells — formulaic era-openers, idiom stacking, rhetorical questions disguised as conclusions.

I added **Chinese-specific anti-pattern detection**:
- 5-dimension scoring (Directness / Rhythm / Trust / Authenticity / Density)
- 41 anti-patterns (English + Chinese)
- Score < 35/50 → rewrite. Target ≥ 45 for publishable quality.

**Install:** `git clone https://github.com/tomerose/stop-slop.git ~/.claude/skills/stop-slop`

**MIT. Free forever.**

https://github.com/tomerose/stop-slop"""
        post_reddit("ClaudeAI", reddit_title, reddit_body)

    if action in ("all", "twitter"):
        twitter_content = """I shipped the first bilingual anti-AI-writing skill for Claude Code.

Chinese AI writing has its own tells:
• "在当今...的时代" — formulaic era-openers
• "不仅仅是...更是..." — binary contrasts
• 四字成语叠叠乐 — idiom stacking

5-dimension scoring. 41 anti-patterns. Free.

github.com/tomerose/stop-slop"""
        post_twitter(twitter_content)

    print("\n✅ 分发完成")
