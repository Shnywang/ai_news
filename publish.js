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

console.log(`=== [1/4] Build site ===`);
console.log(`Copied ${dataFiles.length} data files + ${mdFiles.length} md files to site/`);

// ========== 2. 生成最简 site/index.html ==========
const days = dataFiles.map(f => f.replace('.json', '')).sort().reverse();
const recentDays = days.slice(0, 7); // 7天窗口

// 解析每个 day 的 JSON
const dayData = {};
recentDays.forEach(d => {
  try {
    const content = JSON.parse(fs.readFileSync(path.join(dataDir, `${d}.json`), 'utf8'));
    dayData[d] = content[d] || {};
  } catch (e) {
    console.error(`Failed to parse ${d}.json: ${e.message}`);
  }
});

const indexHtml = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI+具身智能日报 | shnywang</title>
  <meta name="description" content="每日 AI 具身智能行业日报 + 深度技术拆解">
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 900px; margin: 0 auto; padding: 20px; background: #fafafa; color: #222; }
    h1 { color: #1a1a1a; border-bottom: 2px solid #1a1a1a; padding-bottom: 10px; }
    .day { background: white; border-radius: 8px; padding: 20px; margin: 20px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
    .day h2 { color: #1a1a1a; margin-top: 0; }
    .topic { padding: 12px 0; border-bottom: 1px solid #eee; }
    .topic:last-child { border-bottom: none; }
    .topic h3 { margin: 0 0 8px 0; font-size: 17px; }
    .topic p { color: #555; font-size: 14px; line-height: 1.6; margin: 4px 0; }
    .badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11px; margin-right: 6px; }
    .rating5 { background: #d32f2f; color: white; }
    .rating4 { background: #f57c00; color: white; }
    .rating3 { background: #fbc02d; color: white; }
    .cat { background: #e0e0e0; color: #333; }
    footer { text-align: center; color: #999; padding: 20px; font-size: 13px; }
    a { color: #1976d2; text-decoration: none; }
  </style>
</head>
<body>
  <h1>AI+具身智能日报</h1>
  <p style="color:#666;">7 天滚动窗口 · 哲学深度 + 独家解读 + 硬数据 · 每日 18:00 更新</p>
  ${recentDays.map(d => {
    const data = dayData[d];
    if (!data || !data.hot_topics) return '';
    const updateTime = data.update_time || d;
    return `
    <div class="day">
      <h2>📅 ${d} <span style="font-size:13px;color:#999;">${updateTime}</span></h2>
      ${(data.hot_topics || []).map(t => `
      <div class="topic">
        <h3>
          <span class="badge rating${t.rating || 3}">★${t.rating || 3}</span>
          <span class="badge cat">${t.category || '其他'}</span>
          <a href="#${d}-${t.title.slice(0,20)}">${t.title}</a>
        </h3>
        <p>${(t.summary || '').slice(0, 200)}...</p>
      </div>
      `).join('')}
    </div>
    `;
  }).join('')}
  <footer>
    <p>由 Mavis 自动生成 · <a href="https://github.com/Shnywang/ai_news">GitHub</a></p>
    <p>哲学框架：对立统一 / 否定之否定 / 扬弃 / 具身认知 / 证伪主义 / 语言游戏 / 目的论 vs 机械论</p>
  </footer>
</body>
</html>`;

fs.writeFileSync(path.join(siteDir, 'index.html'), indexHtml, 'utf8');
console.log(`=== [2/4] Generated site/index.html ===`);
console.log(`Recent days: ${recentDays.join(', ')}`);

// ========== 3. 生成 RSS feed ==========
const rssItems = [];
recentDays.forEach(d => {
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
    run(`git commit -m "update: 2026-06-17 daily digest (emergency rebuild after .git deletion)"`);
    run('git push origin main --force');
    console.log('\n✅ Published to https://shnywang.github.io/ai_news/');
  }
} catch (e) {
  console.error('\n❌ Git step failed.');
  console.error('请检查：1) 网络可达 github.com:443  2) git remote 已配  3) 远端历史未冲突');
  process.exit(1);
}
