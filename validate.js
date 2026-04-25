const fs = require('fs');
let raw = fs.readFileSync('C:/Users/shnywang/ai_news/data/2026-03-27_14.json', 'utf8');
// Remove BOM if present
if (raw.charCodeAt(0) === 0xFEFF) raw = raw.slice(1);
const d = JSON.parse(raw);
console.log('✅ JSON valid');
console.log('Total:', d.total_count);
console.log('Articles:', d.articles.length);
console.log('Update:', d.update_time);
const cats = {};
d.articles.forEach(a => { cats[a.category] = (cats[a.category] || 0) + 1; });
console.log('Categories:', JSON.stringify(cats, null, 0));
const titles = d.articles.map(a => a.title);
const unique = new Set(titles);
console.log('Unique titles:', unique.size, '/', titles.length);
console.log('All have URLs:', d.articles.every(a => a.url));
console.log('Ratings range:', Math.min(...d.articles.map(a => a.rating)), '-', Math.max(...d.articles.map(a => a.rating)));
console.log('Articles >= 10:', d.articles.length >= 10 ? 'PASS' : 'FAIL');
console.log('No duplicates:', unique.size === titles.length ? 'PASS' : 'FAIL');
