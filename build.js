const fs = require('fs');
const path = require('path');

// Read all daily JSON files in data dir (keep only last 7 days)
const dataDir = path.join(__dirname, 'data');
const files = fs.readdirSync(dataDir).filter(f => /^\d{4}-\d{2}-\d{2}\.json$/.test(f)).sort().reverse().slice(0, 7);

const allData = {};
for (const f of files) {
  const raw = fs.readFileSync(path.join(dataDir, f), 'utf8').replace(/^\uFEFF/, '');
  const parsed = JSON.parse(raw);
  Object.assign(allData, parsed);
}

const days = Object.keys(allData).sort().reverse();
const latestDay = days[0] || '';

// Copy data JSON files to site/data/ so they're served by GitHub Pages
const siteDataDir = path.join(__dirname, 'site', 'data');
if (!fs.existsSync(siteDataDir)) fs.mkdirSync(siteDataDir, { recursive: true });
for (const f of files) {
  fs.copyFileSync(path.join(dataDir, f), path.join(siteDataDir, f));
  // Remove stale files from site/data/
  const stale = fs.readdirSync(siteDataDir).filter(x => /^\d{4}-\d{2}-\d{2}\.json$/.test(x) && !files.includes(x));
  stale.forEach(x => fs.unlinkSync(path.join(siteDataDir, x)));
}

const safeDays = JSON.stringify(days);

const html = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="AI+具身智能资讯聚合 — 多角色视角 · 每日更新 · 创业 / 产品 / 算法 / 项目管理">
<meta property="og:title" content="AI+具身智能资讯聚合">
<meta property="og:description" content="多角色视角 · 每日更新 · 创业 / 产品 / 算法 / 项目管理">
<title>AI+\\u5177\\u8eab\\u667a\\u80fd\\u8d44\\u8baf\\u805a\\u5408</title>
<style>
:root{--bg:#f0f2f5;--card:#fff;--text:#1a1a2e;--t2:#6b7280;--t3:#9ca3af;--accent:#6366f1;--accent2:#818cf8;--border:#e5e7eb;--shadow:0 1px 3px rgba(0,0,0,.08);--shadow2:0 8px 24px rgba(0,0,0,.1);--g1:#6366f1;--g2:#8b5cf6;--star:#f59e0b;--star0:#d1d5db;--green:#059669;--red:#dc2626;--ftbg:#1e1b4b;--ftc:#c7d2fe}
[data-theme=dark]{--bg:#0f0f23;--card:#1a1a2e;--text:#e2e8f0;--t2:#94a3b8;--t3:#64748b;--accent:#818cf8;--accent2:#a5b4fc;--border:#334155;--shadow:0 1px 3px rgba(0,0,0,.3);--shadow2:0 8px 24px rgba(0,0,0,.4);--star0:#475569;--ftbg:#0a0a1a}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Microsoft YaHei',sans-serif;background:var(--bg);color:var(--text);line-height:1.6}
.hd{background:linear-gradient(135deg,var(--g1),var(--g2));color:#fff;padding:2rem 1.5rem;text-align:center;position:relative}
.hd h1{font-size:1.8rem;font-weight:800}.hd .sub{font-size:.9rem;opacity:.85;margin-top:.4rem}
.hd .ut{font-size:.8rem;opacity:.7;margin-top:.2rem}
.tbtn{position:absolute;top:1rem;right:1rem;background:rgba(255,255,255,.2);border:none;border-radius:50%;width:38px;height:38px;cursor:pointer;font-size:1.2rem;display:flex;align-items:center;justify-content:center}
.ct{max-width:1200px;margin:0 auto;padding:1rem}
/* Day selector */
.days{display:flex;gap:.5rem;overflow-x:auto;padding:.5rem 0;margin-bottom:1rem}
.day-btn{padding:.4rem 1rem;border-radius:20px;border:1.5px solid var(--border);background:var(--card);color:var(--t2);cursor:pointer;font-size:.82rem;font-weight:500;white-space:nowrap;transition:all .2s}
.day-btn.a{background:var(--accent);color:#fff;border-color:var(--accent)}
/* Board tabs */
.tabs{display:flex;gap:0;border-bottom:2px solid var(--border);margin-bottom:1.2rem;overflow-x:auto}
.tab{padding:.7rem 1.2rem;cursor:pointer;font-size:.88rem;font-weight:600;color:var(--t2);border-bottom:3px solid transparent;white-space:nowrap;transition:all .2s}
.tab:hover{color:var(--accent)}.tab.a{color:var(--accent);border-bottom-color:var(--accent)}
/* Panels */
.panel{display:none}.panel.a{display:block}
/* Cards */
.bcard{background:var(--card);border-radius:14px;padding:1.2rem;margin-bottom:1rem;box-shadow:var(--shadow);border-left:4px solid var(--accent);transition:box-shadow .2s}
.bcard:hover{box-shadow:var(--shadow2)}
.bcard h3{font-size:.95rem;font-weight:700;margin-bottom:.4rem;color:var(--text)}
.bcard p,.bcard li{font-size:.88rem;color:var(--t2);line-height:1.7}
.bcard ul{padding-left:1.2rem;margin-top:.3rem}
.bcard .tag{display:inline-block;padding:.15rem .5rem;border-radius:8px;font-size:.72rem;font-weight:600;margin-right:.3rem}
.tag-g{background:#ecfdf5;color:#059669}.tag-y{background:#fef3c7;color:#b45309}.tag-r{background:#fee2e2;color:#dc2626}
.tag-b{background:#eff6ff;color:#2563eb}.tag-p{background:#f3e8ff;color:#7c3aed}
[data-theme=dark] .tag-g{background:#064e3b;color:#6ee7b7}[data-theme=dark] .tag-y{background:#451a03;color:#fcd34d}
[data-theme=dark] .tag-r{background:#450a0a;color:#fca5a5}[data-theme=dark] .tag-b{background:#1e3a5f;color:#93c5fd}
[data-theme=dark] .tag-p{background:#3b0764;color:#c4b5fd}
/* Section titles */
.sec{font-size:1rem;font-weight:700;margin:1.2rem 0 .6rem;padding-left:.6rem;border-left:3px solid var(--accent);color:var(--text)}
/* Hot topic card */
.htcard{background:var(--card);border-radius:12px;padding:1rem;margin-bottom:.8rem;box-shadow:var(--shadow);display:flex;gap:1rem;align-items:flex-start;transition:all .2s}
.htcard:hover{box-shadow:var(--shadow2);transform:translateY(-1px)}
.htcard .num{font-size:1.4rem;font-weight:800;color:var(--accent);min-width:2rem;text-align:center}
.htcard .body{flex:1}.htcard .body h4{font-size:.92rem;font-weight:600;margin-bottom:.3rem}
.htcard .body h4 a{color:var(--text);text-decoration:none;transition:color .2s}.htcard .body h4 a:hover{color:var(--accent)}
.bcard h3 a,.bcard h3>a{color:var(--text);text-decoration:none;transition:color .2s}.bcard h3 a:hover,.bcard h3>a:hover{color:var(--accent);text-decoration:underline}
.htcard .body p{font-size:.82rem;color:var(--t2);line-height:1.6}
.htcard .meta{font-size:.75rem;color:var(--t3);margin-top:.3rem}
a{color:inherit}
.stars{color:var(--star);font-size:.8rem;letter-spacing:1px}
/* Startup table */
.stable-wrap{overflow-x:auto;margin-bottom:1rem}
.stable{width:100%;border-collapse:collapse;font-size:.84rem}
.stable th{background:var(--accent);color:#fff;padding:.6rem .8rem;text-align:left;font-weight:600;font-size:.8rem;white-space:nowrap}
.stable td{padding:.6rem .8rem;border-bottom:1px solid var(--border);vertical-align:top}
.stable tr:hover td{background:rgba(99,102,241,.04)}
/* Radar */
.radar-item{display:flex;align-items:center;gap:.8rem;padding:.6rem 0;border-bottom:1px solid var(--border)}
.radar-item:last-child{border:none}
.radar-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
.dot-green{background:#059669}.dot-yellow{background:#d97706}.dot-red{background:#dc2626}.dot-blue{background:#2563eb}
.radar-name{font-weight:600;font-size:.88rem;min-width:140px}
.radar-status{font-size:.78rem;color:var(--t2);flex:1}
.radar-advice{font-size:.78rem;color:var(--accent);font-weight:500}
/* News list */
.ncard{background:var(--card);border-radius:10px;padding:.8rem 1rem;margin-bottom:.6rem;box-shadow:var(--shadow);display:flex;justify-content:space-between;align-items:center;gap:.8rem}
.ncard .left{flex:1}.ncard .left h4{font-size:.88rem;font-weight:600}
.ncard .left h4 a{color:var(--text);text-decoration:none;transition:color .2s}.ncard .left h4 a:hover{color:var(--accent)}
.ncard .left .nm{font-size:.75rem;color:var(--t3);margin-top:.2rem}
.ncard .right{text-align:right;flex-shrink:0}
.ncard .cat{font-size:.72rem;padding:.15rem .5rem;border-radius:8px;background:var(--accent);color:#fff;display:inline-block}
/* Global search bar (in header) */
.search-toggle{position:absolute;top:1rem;left:1rem;background:rgba(255,255,255,.2);border:none;border-radius:50%;width:38px;height:38px;cursor:pointer;font-size:1.2rem;display:flex;align-items:center;justify-content:center}
/* Search overlay */
.search-overlay{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.5);z-index:1000;justify-content:center;align-items:flex-start;padding:15vh 1rem}
.search-overlay.open{display:flex}
.search-box{background:var(--card);border-radius:16px;width:100%;max-width:700px;max-height:60vh;box-shadow:var(--shadow2);overflow:hidden;display:flex;flex-direction:column}
.search-box input{width:100%;padding:1rem 1.2rem;border:none;font-size:1rem;background:transparent;color:var(--text);outline:none;border-bottom:1px solid var(--border)}
.search-results{overflow-y:auto;flex:1;padding:.5rem}
.search-item{padding:.8rem 1rem;border-radius:10px;cursor:pointer;transition:background .15s}
.search-item:hover{background:rgba(99,102,241,.08)}
.search-item h4{font-size:.88rem;font-weight:600;margin-bottom:.2rem}
.search-item h4 a{color:var(--accent);text-decoration:none}
.search-item .nm{font-size:.75rem;color:var(--t3)}
.search-hint{padding:2rem;text-align:center;color:var(--t2);font-size:.88rem}
/* Copy link toast */
.toast{position:fixed;bottom:2rem;left:50%;transform:translateX(-50%);background:var(--accent);color:#fff;padding:.6rem 1.2rem;border-radius:10px;font-size:.85rem;font-weight:500;opacity:0;transition:opacity .3s;z-index:2000;pointer-events:none}
.toast.show{opacity:1}
/* Footer */
.ftr{background:var(--ftbg);color:var(--ftc);text-align:center;padding:1.2rem;margin-top:2rem;font-size:.82rem}
.ftr a{color:var(--ftc);text-decoration:underline}
/* Loading */
.loading{text-align:center;padding:3rem;color:var(--t2);font-size:.9rem}
.loading::after{content:'...';animation:dots 1.5s infinite}
@keyframes dots{0%,20%{content:'.'}40%,60%{content:'..'}80%,100%{content:'...'}}
@media(max-width:768px){
.hd h1{font-size:1.4rem}.ct{padding:.8rem}
.htcard{flex-direction:column;gap:.5rem}
.stable{font-size:.76rem}
.stable th,.stable td{padding:.4rem .5rem;font-size:.76rem}
.tabs{gap:0}.tab{padding:.5rem .8rem;font-size:.8rem}
.search-toggle,.tbtn{width:32px;height:32px;font-size:1rem}
.search-toggle{top:.7rem;left:.7rem}.tbtn{top:.7rem;right:.7rem}
.search-box{max-width:95%;max-height:70vh}
}
</style>
</head>
<body>
<header class="hd">
<button class="search-toggle" onclick="openSearch()" title="\\u641c\\u7d22 (Ctrl+K)">\\uD83D\\uDD0D</button>
<button class="tbtn" onclick="toggleTheme()" title="\\u5207\\u6362\\u4e3b\\u9898">&#x1F319;</button>
<h1>&#x1F916; AI+\\u5177\\u8eab\\u667a\\u80fd\\u8d44\\u8baf\\u805a\\u5408</h1>
<p class="sub">\\u591a\\u89d2\\u8272\\u89c6\\u89d2 \\u00b7 \\u6bcf\\u65e5\\u66f4\\u65b0 \\u00b7 \\u521b\\u4e1a / \\u4ea7\\u54c1 / \\u7b97\\u6cd5 / \\u9879\\u76ee\\u7ba1\\u7406</p>
<p class="ut" id="ut"></p>
</header>
<div class="ct">
<div class="days" id="dayPicker"></div>
<div class="tabs" id="tabs">
<div class="tab a" data-t="hot">\\u{1F525} \\u4eca\\u65e5\\u70ed\\u70b9</div>
<div class="tab" data-t="startup">\\u{1F680} \\u521b\\u4e1a\\u677f\\u5757</div>
<div class="tab" data-t="pm">\\u{1F4CB} \\u4ea7\\u54c1\\u7ecf\\u7406</div>
<div class="tab" data-t="algo">\\u{1F9EC} \\u7b97\\u6cd5\\u5de5\\u7a0b\\u5e08</div>
<div class="tab" data-t="proj">\\u{1F4C5} \\u9879\\u76ee\\u7ecf\\u7406</div>
<div class="tab" data-t="action">\\u{2705} \\u884c\\u52a8\\u5efa\\u8bae</div>
<div class="tab" data-t="hermes">\\u{1F916} Hermes</div>
<div class="tab" data-t="all">\\u{1F4F0} \\u5168\\u90e8\\u8d44\\u8baf</div>
</div>
<div id="content"></div>
</div>
<!-- Search overlay -->
<div class="search-overlay" id="searchOverlay" onclick="if(event.target===this)closeSearch()">
<div class="search-box">
<input id="gSearchInput" placeholder="\\u641c\\u7d22\\u6240\\u6709\\u8d44\\u8baf... (Ctrl+K)" oninput="globalSearch()">
<div class="search-results" id="gSearchResults"></div>
</div>
</div>
<!-- Toast -->
<div class="toast" id="toast"></div>
<footer class="ftr">\\u7531 WorkBuddy \\u81ea\\u52a8\\u751f\\u6210 \\u00b7 \\u6570\\u636e\\u6bcf\\u65e5\\u66f4\\u65b0 \\u00b7 \\u4ec5\\u4fdd\\u7559\\u8fd1\\u4e00\\u5468\\u6570\\u636e \\u00b7 \\u95ee\\u9898\\u53cd\\u9988: <a href="https://github.com/Shnywang/ai_news/issues" target="_blank" rel="noopener noreferrer">GitHub Issues</a> \\u00b7 &copy; 2026</footer>
<script>
var days=${safeDays};
var curDay=days[0]||'';
var curTab='hot';
var cache={};       // day -> data object
var loaded=new Set(); // days that have been fetched

function esc(t){var d=document.createElement('div');d.textContent=t;return d.innerHTML}
function link(url,title){return '<a href="'+esc(url)+'" target="_blank" rel="noopener noreferrer">'+esc(title)+'</a>'}
function stars(r){var s='';for(var i=0;i<5;i++)s+='<span style="color:'+(i<r?'var(--star)':'var(--star0)')+'">\\u2605</span>';return s}
function starsStr(r){var s='';for(var i=0;i<5;i++)s+=(i<r?'\\u2605':'\\u2606');return s}

/* --- Data loading (on-demand from /data/JSON files) --- */
async function loadData(day){
  if(cache[day]) return cache[day];
  try{
    var resp=await fetch('data/'+day+'.json');
    if(!resp.ok) throw new Error(resp.status);
    var json=await resp.json();
    // Each file is {"YYYY-MM-DD": { data... }}
    cache[day]=json[day]||json;
    loaded.add(day);
    return cache[day];
  }catch(e){
    console.error('Failed to load '+day,e);
    return null;
  }
}

function showToast(msg){
  var t=document.getElementById('toast');
  t.textContent=msg;t.classList.add('show');
  setTimeout(function(){t.classList.remove('show')},1500);
}

function initDays(){
  var h='';
  days.forEach(function(d){h+='<button class="day-btn'+(d===curDay?' a':'')+'" onclick="pickDay(\\''+d+'\\',this)">'+d+'</button>'});
  document.getElementById('dayPicker').innerHTML=h;
}

async function pickDay(d,el){
  curDay=d;
  document.querySelectorAll('.day-btn').forEach(function(b){b.classList.remove('a')});
  el.classList.add('a');
  await render();
}

function initTabs(){
  document.querySelectorAll('.tab').forEach(function(t){
    t.addEventListener('click',function(){
      curTab=this.getAttribute('data-t');
      document.querySelectorAll('.tab').forEach(function(x){x.classList.remove('a')});
      this.classList.add('a');
      render();
    });
  });
}

async function render(){
  var data=await loadData(curDay);
  if(!data){
    document.getElementById('content').innerHTML='<div class="loading">\\u52a0\\u8f7d\\u4e2d</div>';
    return;
  }
  document.getElementById('ut').textContent='\\u6700\\u540e\\u66f4\\u65b0\\uff1a'+(data.update_time||curDay);
  var fn={hot:renderHot,startup:renderStartup,pm:renderPM,algo:renderAlgo,proj:renderProj,action:renderAction,hermes:renderHermes,all:renderAll};
  (fn[curTab]||renderHot)(data);
}

function renderHot(d){
  var h='<div class="sec">\\u{1F525} \\u4eca\\u65e5\\u70ed\\u70b9 ('+(d.hot_topics||[]).length+'\\u6761)</div>';
  (d.hot_topics||[]).forEach(function(t,i){
    h+='<div class="htcard"><div class="num">'+(i+1)+'</div><div class="body"><h4>'+link(t.url,t.title)+'</h4><p>'+esc(t.summary)+'</p><div class="meta">'+esc(t.source)+' \\u00b7 '+esc(t.category)+' \\u00b7 <span class="stars">'+starsStr(t.rating)+'</span></div></div></div>';
  });
  document.getElementById('content').innerHTML=h;
}

function renderStartup(d){
  var s=d.startup_board;
  if(!s){document.getElementById('content').innerHTML='<div class="bcard"><h3>\\u{1F680} \\u521b\\u4e1a\\u677f\\u5757</h3><p>\\u6682\\u65e0\\u65b0\\u52a8\\u6001</p></div>';return}
  var h='<div class="sec">\\u{1F680} \\u521b\\u4e1a\\u677f\\u5757 \\u2014 \\u91cd\\u70b9\\u4f01\\u4e1a\\u8ddf\\u8e2a</div>';
  h+='<div class="stable-wrap"><table class="stable"><tr><th>\\u4f01\\u4e1a</th><th>\\u8d5b\\u9053</th><th>\\u6280\\u672f\\u8def\\u7ebf</th><th>\\u878d\\u8d44/\\u8ba2\\u5355</th><th>\\u62e9\\u4e1a\\u5224\\u65ad</th></tr>';
  (s.companies||[]).forEach(function(c){
    h+='<tr><td><strong>'+esc(c.name)+'</strong></td><td>'+esc(c.field)+'</td><td>'+esc(c.route)+'</td><td>'+esc(c.funding)+'</td><td>'+esc(c.verdict)+'</td></tr>';
  });
  h+='</table></div>';
  if(s.trend)h+='<div class="bcard"><h3>\\u{1F4C8} \\u8d5b\\u9053\\u8d8b\\u52bf</h3><p>'+esc(s.trend)+'</p></div>';
  document.getElementById('content').innerHTML=h;
}

function renderPM(d){
  var b=d.pm_board;
  if(!b){document.getElementById('content').innerHTML='<div class="bcard"><p>\\u6682\\u65e0\\u65b0\\u52a8\\u6001</p></div>';return}
  var h='<div class="sec">\\u{1F4CB} \\u4ea7\\u54c1\\u7ecf\\u7406\\u677f\\u5757</div>';
  (b.insights||[]).forEach(function(t){
    var ln=t.url?link(t.url,t.title):esc(t.title);
    h+='<div class="bcard"><h3>'+ln+'</h3><p>'+esc(t.content)+'</p></div>';
  });
  if(b.focus&&b.focus.length){
    h+='<div class="sec">\\u{1F4CC} \\u672a\\u6765\\u5173\\u6ce8\\u91cd\\u70b9</div><div class="bcard"><ul>';
    b.focus.forEach(function(f){h+='<li>'+esc(f)+'</li>'});
    h+='</ul></div>';
  }
  document.getElementById('content').innerHTML=h;
}

function renderAlgo(d){
  var b=d.algo_board;
  if(!b){document.getElementById('content').innerHTML='<div class="bcard"><p>\\u6682\\u65e0\\u65b0\\u52a8\\u6001</p></div>';return}
  var h='<div class="sec">\\u{1F9EC} \\u7b97\\u6cd5\\u5de5\\u7a0b\\u5e08\\u677f\\u5757</div>';
  (b.insights||[]).forEach(function(t){
    var ln=t.url?link(t.url,t.title):esc(t.title);
    h+='<div class="bcard"><h3>'+ln+'</h3><p>'+esc(t.content)+'</p></div>';
  });
  if(b.tech_radar&&b.tech_radar.length){
    h+='<div class="sec">\\u{1F6F0}\\uFE0F \\u6280\\u672f\\u96f7\\u8fbe</div><div class="bcard">';
    b.tech_radar.forEach(function(r){
      var dot=r.status.indexOf('\\u9a8c\\u8bc1')!==-1?'dot-green':r.status.indexOf('\\u6210\\u957f')!==-1?'dot-blue':r.status.indexOf('\\u89c2\\u671b')!==-1?'dot-yellow':'dot-red';
      h+='<div class="radar-item"><span class="radar-dot '+dot+'"></span><span class="radar-name">'+esc(r.direction)+'</span><span class="radar-status">'+esc(r.status)+'</span><span class="radar-advice">'+esc(r.advice)+'</span></div>';
    });
    h+='</div>';
  }
  if(b.focus&&b.focus.length){
    h+='<div class="sec">\\u{1F4CC} \\u672a\\u6765\\u5173\\u6ce8\\u91cd\\u70b9</div><div class="bcard"><ul>';
    b.focus.forEach(function(f){h+='<li>'+esc(f)+'</li>'});
    h+='</ul></div>';
  }
  document.getElementById('content').innerHTML=h;
}

function renderProj(d){
  var b=d.projmgr_board;
  if(!b){document.getElementById('content').innerHTML='<div class="bcard"><p>\\u6682\\u65e0\\u65b0\\u52a8\\u6001</p></div>';return}
  var h='<div class="sec">\\u{1F4C5} \\u9879\\u76ee\\u7ecf\\u7406\\u677f\\u5757</div>';
  (b.insights||[]).forEach(function(t){
    h+='<div class="bcard"><h3>'+esc(t.title)+'</h3><p>'+esc(t.content)+'</p></div>';
  });
  if(b.focus&&b.focus.length){
    h+='<div class="sec">\\u{1F4CC} \\u672a\\u6765\\u5173\\u6ce8\\u91cd\\u70b9</div><div class="bcard"><ul>';
    b.focus.forEach(function(f){h+='<li>'+esc(f)+'</li>'});
    h+='</ul></div>';
  }
  document.getElementById('content').innerHTML=h;
}

function renderAction(d){
  var a=d.action_items;
  if(!a){document.getElementById('content').innerHTML='<div class="bcard"><p>\\u6682\\u65e0</p></div>';return}
  var h='';
  if(a.tech_selection){
    h+='<div class="sec">\\u{1F527} \\u6280\\u672f\\u9009\\u578b</div><div class="bcard"><ul>';
    a.tech_selection.forEach(function(t){h+='<li>'+esc(t)+'</li>'});
    h+='</ul></div>';
  }
  if(a.track_judgment){
    h+='<div class="sec">\\u{1F3AF} \\u8d5b\\u9053\\u5224\\u65ad</div><div class="bcard"><ul>';
    a.track_judgment.forEach(function(t){h+='<li>'+esc(t)+'</li>'});
    h+='</ul></div>';
  }
  if(a.watch_list){
    h+='<div class="sec">\\u{1F440} Watch List</div><div class="bcard"><ul>';
    a.watch_list.forEach(function(t){h+='<li>'+esc(t)+'</li>'});
    h+='</ul></div>';
  }
  document.getElementById('content').innerHTML=h;
}

function renderHermes(d){
  var hb=d.hermes_board;
  if(!hb){document.getElementById('content').innerHTML='<div class="bcard"><p>\\u6682\\u65e0 Hermes \\u8d44\\u8baf</p></div>';return}
  var h='<div class="sec">\\u{1F916} Hermes Agent \\u2014 AI \\u4ee3\\u7406\\u5de5\\u4f5c\\u6d41\\u4e0e\\u8d44\\u8baf</div>';
  (hb.insights||[]).forEach(function(t){
    h+='<div class="bcard"><h3>'+link(t.url||'#',t.title)+'</h3><p>'+esc(t.content)+'</p></div>';
  });
  if(hb.tech_stack&&hb.tech_stack.length){
    h+='<div class="sec">\\u{1F6E0}\\uFE0F \\u6280\\u672f\\u6808\\u4e0e\\u5de5\\u5177</div>';
    hb.tech_stack.forEach(function(t){
      h+='<div class="bcard"><h3>'+link(t.url||'#',t.title)+'</h3><p>'+esc(t.content)+'</p></div>';
    });
  }
  if(hb.community&&hb.community.length){
    h+='<div class="sec">\\u{1F310} \\u793e\\u533a\\u52a8\\u6001</div>';
    hb.community.forEach(function(c){
      h+='<div class="bcard"><h3>'+link(c.url||'#',c.title)+'</h3><p>'+esc(c.content)+'</p></div>';
    });
  }
  document.getElementById('content').innerHTML=h;
}

function renderAll(d){
  var arts=d.raw_articles||[];
  var h='<div id="allList"></div>';
  document.getElementById('content').innerHTML=h;
  window._allArts=arts;
  filterAll('');
}

function filterAll(q){
  q=(q||'').toLowerCase().trim();
  var arts=window._allArts||[];
  if(q)arts=arts.filter(function(a){return a.title.toLowerCase().indexOf(q)!==-1||a.summary.toLowerCase().indexOf(q)!==-1||a.category.toLowerCase().indexOf(q)!==-1||a.source.toLowerCase().indexOf(q)!==-1});
  var h='';
  if(!arts.length){h='<div style="text-align:center;padding:2rem;color:var(--t2)">\\u672a\\u627e\\u5230\\u5339\\u914d\\u8d44\\u8baf</div>'}
  else{arts.forEach(function(a){
    h+='<div class="ncard"><div class="left"><h4>'+link(a.url,a.title)+'</h4><div class="nm">'+esc(a.source)+' \\u00b7 '+a.publish_time+' \\u00b7 '+starsStr(a.rating)+'</div></div><div class="right"><span class="cat">'+esc(a.category)+'</span></div></div>';
  })}
  document.getElementById('allList').innerHTML=h;
}

/* --- Global Search (Ctrl+K) --- */
async function openSearch(){
  document.getElementById('searchOverlay').classList.add('open');
  var inp=document.getElementById('gSearchInput');
  inp.value='';inp.focus();
  document.getElementById('gSearchResults').innerHTML='<div class="search-hint">\\u8f93\\u5165\\u5173\\u952e\\u8bcd\\u641c\\u7d22\\u6240\\u6709\\u8d44\\u8baf\\uff08\\u81ea\\u52a8\\u52a0\\u8f7d\\u6240\\u6709\\u65e5\\u6570\\u636e\\uff09</div>';
  // Pre-load all days in background
  if(loaded.size<days.length){
    Promise.allSettled(days.map(function(d){return loadData(d)})).then(function(){
      // If still searching, trigger a search
      if(document.getElementById('searchOverlay').classList.contains('open')&&inp.value.trim()){
        globalSearch();
      }
    });
  }
}
function closeSearch(){
  document.getElementById('searchOverlay').classList.remove('open');
}
async function globalSearch(){
  var q=document.getElementById('gSearchInput').value.toLowerCase().trim();
  var res=document.getElementById('gSearchResults');
  if(!q){res.innerHTML='<div class="search-hint">\\u8f93\\u5165\\u5173\\u952e\\u8bcd\\u641c\\u7d22\\u6240\\u6709\\u8d44\\u8baf\\u00b7\\u00b7\\u00b7</div>';return}
  // Ensure all data loaded
  await Promise.allSettled(days.map(function(d){return loadData(d)}));
  var items=[];
  Object.keys(cache).forEach(function(day){
    var d=cache[day];if(!d)return;
    // Search in hot_topics
    (d.hot_topics||[]).forEach(function(t){
      if(t.title.toLowerCase().indexOf(q)!==-1||t.summary.toLowerCase().indexOf(q)!==-1)
        items.push({title:t.title,url:t.url,meta:day+' \\u00b7 '+t.source+' \\u00b7 \\u{1F525}\\u70ed\\u70b9',date:day});
    });
    // Search in raw_articles
    (d.raw_articles||[]).forEach(function(a){
      if(a.title.toLowerCase().indexOf(q)!==-1||a.summary.toLowerCase().indexOf(q)!==-1||a.category.toLowerCase().indexOf(q)!==-1){
        items.push({title:a.title,url:a.url,meta:a.publish_time+' \\u00b7 '+a.source+' \\u00b7 '+a.category+' \\u00b7 '+starsStr(a.rating),date:a.publish_time||day});
      }
    });
    // Search in insights (pm, algo, hermes)
    ['pm_board','algo_board'].forEach(function(k){
      var b=d[k];if(!b)return;
      (b.insights||[]).forEach(function(t){
        if(t.title.toLowerCase().indexOf(q)!==-1||t.content.toLowerCase().indexOf(q)!==-1)
          items.push({title:t.title,url:t.url,meta:day+' \\u00b7 \\u{1F4CB}\\u6536\\u5165\\u89c6\\u89d2',date:day});
      });
    });
    var hb=d.hermes_board;if(hb){
      (hb.insights||[]).concat(hb.tech_stack||[]).concat(hb.community||[]).forEach(function(t){
        if(t.title.toLowerCase().indexOf(q)!==-1||t.content.toLowerCase().indexOf(q)!==-1)
          items.push({title:t.title,url:t.url,meta:day+' \\u00b7 \\u{1F916} Hermes',date:day});
      });
    }
  });
  // Deduplicate by title
  var seen={};var unique=[];
  items.forEach(function(it){if(!seen[it.title]){seen[it.title]=true;unique.push(it)}});
  unique.sort(function(a,b){return(b.date||'').localeCompare(a.date||'')});
  var h='';
  if(!unique.length){h='<div class="search-hint">\\u672a\\u627e\\u5230\\u5339\\u914d\\u201c'+esc(q)+'\\u201d\\u7684\\u7ed3\\u679c</div>'}
  else{h='<div style="padding:.3rem .5rem;font-size:.78rem;color:var(--t3)">\\u627e\\u5230 '+unique.length+' \\u6761\\u7ed3\\u679c</div>';
    unique.forEach(function(it){
      h+='<div class="search-item"><h4>'+link(it.url,it.title)+'</h4><div class="nm">'+it.meta+'</div></div>';
    });
  }
  res.innerHTML=h;
}

/* --- Copy link --- */
function copyLink(url){
  navigator.clipboard.writeText(url).then(function(){
    showToast('\\u2705 \\u94fe\\u63a5\\u5df2\\u590d\\u5236');
  }).catch(function(){
    showToast('\\u274c \\u590d\\u5236\\u5931\\u8d25');
  });
}

/* --- Theme --- */
function toggleTheme(){
  var dk=document.body.getAttribute('data-theme')==='dark';
  document.body.setAttribute('data-theme',dk?'light':'dark');
  document.querySelector('.tbtn').innerHTML=dk?'&#x1F319;':'&#x2600;&#xFE0F;';
  localStorage.setItem('ai-news-theme',dk?'light':'dark');
}

document.addEventListener('DOMContentLoaded',function(){
  // Theme: localStorage > system preference > default light
  var sv=localStorage.getItem('ai-news-theme');
  if(sv==='dark'||(!sv&&window.matchMedia('(prefers-color-scheme:dark)').matches)){
    document.body.setAttribute('data-theme','dark');
    document.querySelector('.tbtn').innerHTML='&#x2600;&#xFE0F;';
  }
  // Keyboard shortcuts
  document.addEventListener('keydown',function(e){
    if((e.ctrlKey||e.metaKey)&&e.key==='k'){e.preventDefault();openSearch()}
    if(e.key==='Escape')closeSearch();
  });
  initDays();initTabs();render();
});
</script>
</body>
</html>`;

fs.writeFileSync(path.join(__dirname, 'site/index.html'), html, 'utf8');
console.log('Build OK! Days: ' + days.join(', ') + ' | Files in site/data/: ' + files.length);
