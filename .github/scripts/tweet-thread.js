// Post stop-slop thread to Twitter — uses v1.1 for Free tier compatibility
const { TwitterApi } = require('twitter-api-v2');

const THREAD = [
  `Your AI writes like a LinkedIn influencer and everyone can tell.

82% of creators use AI daily.
76% of readers spot AI slop in under 3 seconds.

I built a skill that fixes this:
github.com/tomerose/stop-slop`,

  `The original stop-slop teaches Claude to kill its own writing tells:

• Throat-clearing openers
• "Not X. But Y." contrasts
• All adverbs
• Vague declaratives

One markdown file. Zero code. 9,200 stars.`,

  `Chinese AI writing is worse:

"在当今快速变化的时代..."
"不仅仅是...更是..."
四字成语 ×3 per paragraph

So I added 12 Chinese-specific anti-patterns. First bilingual version.`,

  `How it works:

1. You write with Claude
2. Skill auto-scores on 5 dimensions
3. Score < 35/50 → rewrite
4. Deliver at 45+

Prevention over detection.`,

  `MIT. Free. 1 minute install:

git clone https://github.com/tomerose/stop-slop.git ~/.claude/skills/stop-slop

If it saves you an hour of editing, drop a ⭐`,
];

async function main() {
  // Try OAuth 1.0a with user context
  const client = new TwitterApi({
    appKey: process.env.TWITTER_API_KEY?.trim(),
    appSecret: process.env.TWITTER_API_SECRET?.trim(),
    accessToken: process.env.TWITTER_ACCESS_TOKEN?.trim(),
    accessSecret: process.env.TWITTER_ACCESS_SECRET?.trim(),
  });

  // Verify credentials first
  try {
    const me = await client.v1.verifyCredentials();
    console.log(`✅ Authenticated as @${me.screen_name}`);
  } catch (e) {
    console.error('❌ Auth verification failed:', e.data?.detail || e.message);
    console.error('   Check that API Key/Secret and Access Token/Secret are correct');
    console.error('   and that app permissions are "Read and Write"');
    process.exit(1);
  }

  // Post thread using v1.1 statuses/update (more compatible with Free tier)
  let replyTo = null;
  for (let i = 0; i < THREAD.length; i++) {
    const params = { status: THREAD[i] };
    if (replyTo) params.in_reply_to_status_id = replyTo;

    const result = await client.v1.tweet(THREAD[i], replyTo ? {
      in_reply_to_status_id: replyTo
    } : undefined);

    replyTo = result.id_str;
    console.log(`✅ Tweet ${i + 1}/${THREAD.length}: https://x.com/i/status/${replyTo}`);
  }

  console.log(`\n🎉 Thread complete! ${THREAD.length} tweets posted.`);
}

main().catch(e => {
  console.error('❌ Failed:', e.data?.detail || e.message);
  process.exit(1);
});
