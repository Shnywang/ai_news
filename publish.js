// publish.js - 每日发布流程一键脚本
// 1) 运行 build.js 重新生成 index.html
// 2) 清理超过7天的旧数据文件
// 3) git add/commit/push，自动发布到 GitHub Pages

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const repoDir = __dirname;
const dataDir = path.join(repoDir, 'data');

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

// ========== 1. 构建网页 ==========
console.log('=== [1/3] Build site ===');
run('node build.js');

// ========== 2. 清理超过7天的旧数据（以最新日期为锚，保留7天窗口） ==========
console.log('\n=== [2/3] Cleanup old data (keep latest 7-day window) ===');
const files = fs.readdirSync(dataDir)
  .filter(f => /^\d{4}-\d{2}-\d{2}\.json$/.test(f))
  .sort()
  .reverse();

if (files.length === 0) {
  console.log('No data files found.');
} else {
  // 以"最新数据日期"为锚点，保留它及往前6天（共7天窗口）
  const latestDateStr = files[0].replace('.json', '');
  const latestDate = new Date(latestDateStr + 'T00:00:00');
  const cutoff = new Date(latestDate);
  cutoff.setDate(cutoff.getDate() - 6); // 7天窗口 = [latest-6, latest]

  const toKeep = [];
  const toDelete = [];
  for (const f of files) {
    const d = new Date(f.replace('.json', '') + 'T00:00:00');
    if (d >= cutoff) toKeep.push(f);
    else toDelete.push(f);
  }

  if (toDelete.length === 0) {
    console.log('No old files to remove.');
  } else {
    for (const f of toDelete) {
      fs.unlinkSync(path.join(dataDir, f));
      console.log(`Deleted: ${f}`);
    }
  }
  console.log(`Kept ${toKeep.length} files (window ${cutoff.toISOString().slice(0,10)} ~ ${latestDateStr}): ${toKeep.join(', ')}`);
}

// ========== 3. Git 提交并推送 ==========
console.log('\n=== [3/3] Git commit & push ===');
try {
  const status = run('git status --porcelain').trim();
  if (!status) {
    console.log('No changes to commit. Skip push.');
    process.exit(0);
  }
  const today = new Date().toISOString().slice(0, 10);
  run('git add .');
  run(`git commit -m "update: ${today} daily digest"`);
  run('git push origin main');
  console.log('\n✅ Published to https://shnywang.github.io/ai_news/');
} catch (e) {
  console.error('\n❌ Git step failed. You may need to push manually.');
  process.exit(1);
}
