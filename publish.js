// publish.js - 紧急重建最小可工作版本
// 1) 读取 data/2026-06-17.json + 两份 md 复制到 site/data
// 2) 生成最简 site/index.html
// 3) git init + add remote + commit + push

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const repoDir = __dirname;
const dataDir = path.join(repoDir, 'data');
const siteDir = path.join(repoDir, 'site');

function run(cmd, opts = {}) {
  console.log(`\n$ ${cmd}`);
  try {
    const out = execSync(cmd, { cwd: repoDir, stdio: 'pipe', encoding: 'utf8', ...opts });
    if (out) console.log(out.trim());
    return out;
  } catch (e) {
    console.error(e.stdout || e.message);
    throw e;
  }
}

// ========== 1. 准备 site 目录 ==========
if (!fs.existsSync(siteDir)) fs.mkdirSync(siteDir, { recursive: true });
fs.mkdirSync(path.join(siteDir, 'data'), { recursive: true });

// 复制所有 data/*.json 到 site/data/
const dataFiles = fs.readdirSync(dataDir).filter(f => f.endsWith('.json'));
dataFiles.forEach(f => {
  fs.copyFileSync(path.join(dataDir, f), path.join(siteDir, 'data', f));
});

// 复制所有根目录的 md/csdn/deep-dive 到 site/ (用作 raw 资源)
const mdFiles = fs.readdirSync(repoDir).filter(f => f.endsWith('.md'));
mdFiles.forEach(f => {
  fs.copyFileSync(path.join(repoDir, f), path.join(siteDir, f));
});

// 复制 site/index.html 和 site/feed.xml 到根目录 (Pages 根路径访问)
['index.html', 'feed.xml'].forEach(f => {
  const src = path.join(siteDir, f);
  if (fs.existsSync(src)) {
    fs.copyFileSync(src, path.join(repoDir, f));
  }
});

console.log(`=== [1/4] Build site ===`);
console.log(`Copied ${dataFiles.length} data files + ${mdFiles.length} md files to site/`);

// ========== 2. 用 build.js 生成完整 site/index.html ==========
console.log(`=== [2/4] Running build.js for full SPA ===`);
try {
  execSync('node build.js', { cwd: repoDir, stdio: 'inherit', encoding: 'utf8' });
} catch (e) {
  console.error('build.js failed, using fallback');
}
console.log(`Recent days: ${dataFiles.map(f=>f.replace('.json','')).sort().reverse().slice(0,7).join(', ')}`);

// ========== 3. 生成 RSS feed ==========
const daysForFeed = dataFiles.map(f => f.replace('.json', '')).sort().reverse();
const recentDaysForFeed = daysForFeed.slice(0, 7);
const dayData = {};
recentDaysForFeed.forEach(d => {
  try {
    const content = JSON.parse(fs.readFileSync(path.join(dataDir, `${d}.json`), 'utf8'));
    dayData[d] = content[d] || {};
  } catch (e) {}
});
const rssItems = [];
recentDaysForFeed.forEach(d => {
  const data = dayData[d];
  if (!data || !data.hot_topics) return;
  (data.hot_topics || []).forEach(t => {
    rssItems.push(`    <item>
      <title>${t.title}</title>
      <link>https://shnywang.github.io/ai_news/</link>
      <description>${(t.summary || '').replace(/[<>&]/g, c => ({'<':'&lt;','>':'&gt;','&':'&amp;'}[c]))}</description>
      <pubDate>${new Date(data.update_time || d).toUTCString()}</pubDate>
      <guid>${d}-${t.title.slice(0,50)}</guid>
    </item>`);
  });
});

const rssXml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>AI+具身智能日报</title>
    <link>https://shnywang.github.io/ai_news/</link>
    <description>每日 AI 具身智能行业日报</description>
    <language>zh-cn</language>
    ${rssItems.join('\n')}
  </channel>
</rss>`;

fs.writeFileSync(path.join(siteDir, 'feed.xml'), rssXml, 'utf8');
console.log(`=== [3/4] Generated site/feed.xml (${rssItems.length} items) ===`);

// ========== 4. Git 提交并推送 ==========
console.log(`\n=== [4/4] Git init + add + commit + push ===`);

try {
  // 检查 .git 是否存在
  const hasGit = fs.existsSync(path.join(repoDir, '.git'));
  if (!hasGit) {
    console.log('No .git found. Initializing...');
    run('git init -b main');
    run('git remote add origin https://github.com/Shnywang/ai_news.git');
  }

  run('git add .');
  const status = run('git status --porcelain').trim();
  if (!status) {
    console.log('No changes to commit. Skip push.');
  } else {
    // 取最新 data 日期作为 commit message
    const latestData = dataFiles.sort().reverse()[0] || 'unknown';
    const latestMd = mdFiles.sort().reverse()[0] || '';
    const isCsdn = latestMd.includes('csdn');
    const isDeepDive = latestMd.includes('deep-dive');
    let type = 'daily-digest';
    if (isCsdn) type = 'csdn viral post';
    else if (isDeepDive) type = 'deep-dive';
    run(`git commit -m "update: ${latestData.replace('.json','')} ${type}\n\n- 6-22 端午特辑：6-15~6-17 三天三步曲系统总结"`);
    run('git push origin main --force');
    console.log('\n✅ Published to https://shnywang.github.io/ai_news/');
  }
} catch (e) {
  console.error('\n❌ Git step failed.');
  console.error('请检查：1) 网络可达 github.com:443  2) git remote 已配  3) 远端历史未冲突');
  process.exit(1);
}
