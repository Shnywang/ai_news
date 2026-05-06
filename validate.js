const fs = require('fs');
const path = require('path');

// 默认读取最新日期的数据文件
const dataDir = path.join(__dirname, 'data');
const files = fs.readdirSync(dataDir)
  .filter(f => /^\d{4}-\d{2}-\d{2}\.json$/.test(f))
  .sort()
  .reverse();

// 支持命令行参数指定文件，如：node validate.js 2026-04-29.json
const targetFile = process.argv[2]
  ? (process.argv[2].includes('/') || process.argv[2].includes('\\'))
    ? process.argv[2]
    : path.join(dataDir, process.argv[2])
  : (files[0] ? path.join(dataDir, files[0]) : null);

if (!targetFile) {
  console.error('No data files found in data/ directory.');
  process.exit(1);
}

let raw = fs.readFileSync(targetFile, 'utf8');
console.log('Validating:', targetFile);
// Remove BOM if present
if (raw.charCodeAt(0) === 0xFEFF) raw = raw.slice(1);
const parsed = JSON.parse(raw);

// 新格式: { "YYYY-MM-DD": { hot_topics: [], raw_articles: [], ... } }
// 兼容旧格式: { articles: [], total_count: n, update_time: "" }
const dateKey = Object.keys(parsed).find(k => /^\d{4}-\d{2}-\d{2}$/.test(k));
const d = dateKey ? parsed[dateKey] : parsed;

console.log('✅ JSON valid');
console.log('Date:', dateKey || '(legacy format)');
console.log('Update time:', d.update_time);

// Collect all articles from all sections
const hotTopics = d.hot_topics || [];
const rawArticles = d.raw_articles || [];
const allArticles = [...hotTopics, ...rawArticles];

// Also collect from board sections (insights have different structure)
const pmInsights = (d.pm_board && d.pm_board.insights) || [];
const algoInsights = (d.algo_board && d.algo_board.insights) || [];
const projInsights = (d.projmgr_board && d.projmgr_board.insights) || [];
const hermesInsights = (d.hermes_board && d.hermes_board.insights) || [];
const hermesTech = (d.hermes_board && d.hermes_board.tech_stack) || [];
const hermesCommunity = (d.hermes_board && d.hermes_board.community) || [];
const actionItems = [];
if (d.action_items) {
  if (d.action_items.tech_selection) actionItems.push(...d.action_items.tech_selection);
  if (d.action_items.track_judgment) actionItems.push(...d.action_items.track_judgment);
  if (d.action_items.watch_list) actionItems.push(...d.action_items.watch_list);
}
const startupCompanies = (d.startup_board && d.startup_board.companies) || [];

const totalHot = hotTopics.length;
const totalRaw = rawArticles.length;
const totalBoards = pmInsights.length + algoInsights.length + projInsights.length + hermesInsights.length + hermesTech.length + hermesCommunity.length + actionItems.length + startupCompanies.length;
const totalAll = allArticles.length;

console.log('\n--- Content Stats ---');
console.log('Hot topics:', totalHot);
console.log('Raw articles:', totalRaw);
console.log('Board items (PM/Algo/Proj/Hermes/Action/Startup):', totalBoards);
console.log('Total articles (hot + raw):', totalAll);

if (totalAll > 0) {
  const cats = {};
  allArticles.forEach(a => { if (a.category) cats[a.category] = (cats[a.category] || 0) + 1; });
  console.log('Categories:', JSON.stringify(cats));

  const titles = allArticles.map(a => a.title);
  const unique = new Set(titles);
  console.log('Unique titles:', unique.size, '/', titles.length);
  console.log('All have URLs:', allArticles.every(a => a.url));
  const ratings = allArticles.map(a => a.rating).filter(r => r !== undefined);
  if (ratings.length > 0) {
    console.log('Ratings range:', Math.min(...ratings), '-', Math.max(...ratings));
  }
  console.log('Articles >= 10:', totalAll >= 10 ? 'PASS' : 'FAIL');
  console.log('No duplicates:', unique.size === titles.length ? 'PASS' : 'FAIL');
} else {
  console.log('No articles found to validate.');
}
