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

const safeData = JSON.stringify(allData).replace(/<\//g, '<\\/');
const days = Object.keys(allData).sort().reverse();
const latestDay = days[0] || '';

const html = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI+\u5177\u8eab\u667a\u80fd\u8d44\u8baf\u805a\u5408</title>
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
.tag-g{background:#ecfdf5;color:#059669}
.tag-y{background:#fef3c7;color:#b45309}
.tag-r{background:#fee2e2;color:#dc2626}
.tag-b{background:#eff6ff;color:#2563eb}
.tag-p{background:#f3e8ff;color:#7c3aed}
[data-theme=dark] .tag-g{background:#064e3b;color:#6ee7b7}
[data-theme=dark] .tag-y{background:#451a03;color:#fcd34d}
[data-theme=dark] .tag-r{background:#450a0a;color:#fca5a5}
[data-theme=dark] .tag-b{background:#1e3a5f;color:#93c5fd}
[data-theme=dark] .tag-p{background:#3b0764;color:#c4b5fd}
/* Section titles */
.sec{font-size:1rem;font-weight:700;margin:1.2rem 0 .6rem;padding-left:.6rem;border-left:3px solid var(--accent);color:var(--text)}
/* Hot topic card */
.htcard{background:var(--card);border-radius:12px;padding:1rem;margin-bottom:.8rem;box-shadow:var(--shadow);display:flex;gap:1rem;align-items:flex-start;transition:all .2s}
.htcard:hover{box-shadow:var(--shadow2);transform:translateY(-1px)}
.htcard .num{font-size:1.4rem;font-weight:800;color:var(--accent);min-width:2rem;text-align:center}
.htcard .body{flex:1}.htcard .body h4{font-size:.92rem;font-weight:600;margin-bottom:.3rem}
.htcard .body h4 a{color:var(--text);text-decoration:none}.htcard .body h4 a:hover{color:var(--accent)}
.htcard .body p{font-size:.82rem;color:var(--t2);line-height:1.6}
.htcard .meta{font-size:.75rem;color:var(--t3);margin-top:.3rem}
.stars{color:var(--star);font-size:.8rem;letter-spacing:1px}
/* Startup table */
.stable{width:100%;border-collapse:collapse;font-size:.84rem;margin-bottom:1rem}
.stable th{background:var(--accent);color:#fff;padding:.6rem .8rem;text-align:left;font-weight:600;font-size:.8rem}
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
/* Search in all news */
.search-bar{margin-bottom:1rem;position:relative}
.search-bar input{width:100%;padding:.7rem 1rem .7rem 2.5rem;border:2px solid var(--border);border-radius:12px;font-size:.9rem;background:var(--card);color:var(--text);outline:none}
.search-bar input:focus{border-color:var(--accent)}
.search-bar .ico{position:absolute;left:.8rem;top:50%;transform:translateY(-50%);color:var(--t3)}
/* News list */
.ncard{background:var(--card);border-radius:10px;padding:.8rem 1rem;margin-bottom:.6rem;box-shadow:var(--shadow);display:flex;justify-content:space-between;align-items:center;gap:.8rem}
.ncard .left{flex:1}.ncard .left h4{font-size:.88rem;font-weight:600}
.ncard .left h4 a{color:var(--text);text-decoration:none}.ncard .left h4 a:hover{color:var(--accent)}
.ncard .left .nm{font-size:.75rem;color:var(--t3);margin-top:.2rem}
.ncard .right{text-align:right;flex-shrink:0}
.ncard .cat{font-size:.72rem;padding:.15rem .5rem;border-radius:8px;background:var(--accent);color:#fff;display:inline-block}
.ftr{background:var(--ftbg);color:var(--ftc);text-align:center;padding:1.2rem;margin-top:2rem;font-size:.82rem}
@media(max-width:768px){.hd h1{font-size:1.4rem}.ct{padding:.8rem}.htcard{flex-direction:column;gap:.5rem}.stable{font-size:.76rem}.tabs{gap:0}.tab{padding:.5rem .8rem;font-size:.8rem}}
</style>
</head>
<body>
<header class="hd">
<button class="tbtn" onclick="toggleTheme()">&#x1F319;</button>
<h1>&#x1F916; AI+\u5177\u8eab\u667a\u80fd\u8d44\u8baf\u805a\u5408</h1>
<p class="sub">\u591a\u89d2\u8272\u89c6\u89d2 \u00b7 \u6bcf\u65e5\u66f4\u65b0 \u00b7 \u521b\u4e1a / \u4ea7\u54c1 / \u7b97\u6cd5 / \u9879\u76ee\u7ba1\u7406</p>
<p class="ut" id="ut"></p>
</header>
<div class="ct">
<div class="days" id="dayPicker"></div>
<div class="tabs" id="tabs">
<div class="tab a" data-t="hot">\u{1F525} \u4eca\u65e5\u70ed\u70b9</div>
<div class="tab" data-t="startup">\u{1F680} \u521b\u4e1a\u677f\u5757</div>
<div class="tab" data-t="pm">\u{1F4CB} \u4ea7\u54c1\u7ecf\u7406</div>
<div class="tab" data-t="algo">\u{1F9EC} \u7b97\u6cd5\u5de5\u7a0b\u5e08</div>
<div class="tab" data-t="proj">\u{1F4C5} \u9879\u76ee\u7ecf\u7406</div>
<div class="tab" data-t="action">\u{2705} \u884c\u52a8\u5efa\u8bae</div>
<div class="tab" data-t="all">\u{1F4F0} \u5168\u90e8\u8d44\u8baf</div>
</div>
<div id="content"></div>
</div>
<footer class="ftr">\u7531 WorkBuddy \u81ea\u52a8\u751f\u6210 \u00b7 \u6570\u636e\u6bcf\u65e5\u66f4\u65b0 \u00b7 \u4ec5\u4fdd\u7559\u8fd1\u4e00\u5468\u6570\u636e \u00b7 &copy; 2026</footer>
<script>
var W=${safeData};
var days=${JSON.stringify(days)};
var curDay=days[0]||'';
var curTab='hot';

function esc(t){var d=document.createElement('div');d.textContent=t;return d.innerHTML}
function stars(r){var s='';for(var i=0;i<5;i++)s='<span style="color:'+(i<r?'var(--star)':'var(--star0)')+'">\\u2605</span>';return s}
function starsStr(r){var s='';for(var i=0;i<5;i++)s+=(i<r?'\\u2605':'\\u2606');return s}

function initDays(){
  var h='';
  days.forEach(function(d){h+='<button class="day-btn'+(d===curDay?' a':'')+'" onclick="pickDay(\\''+d+'\\',this)">'+d+'</button>'});
  document.getElementById('dayPicker').innerHTML=h;
}

function pickDay(d,el){
  curDay=d;
  document.querySelectorAll('.day-btn').forEach(function(b){b.classList.remove('a')});
  el.classList.add('a');
  render();
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

function render(){
  var data=W[curDay];
  if(!data){document.getElementById('content').innerHTML='<div style="text-align:center;padding:3rem;color:var(--t2)">\u6682\u65e0\u8be5\u65e5\u6570\u636e</div>';return}
  document.getElementById('ut').textContent='\u6700\u540e\u66f4\u65b0\uff1a'+(data.update_time||curDay);
  var fn={hot:renderHot,startup:renderStartup,pm:renderPM,algo:renderAlgo,proj:renderProj,action:renderAction,all:renderAll};
  (fn[curTab]||renderHot)(data);
}

function renderHot(d){
  var h='<div class="sec">\u{1F525} \u4eca\u65e5\u70ed\u70b9 ('+(d.hot_topics||[]).length+'\u6761)</div>';
  (d.hot_topics||[]).forEach(function(t,i){
    h+='<div class="htcard"><div class="num">'+(i+1)+'</div><div class="body"><h4><a href="'+esc(t.url)+'" target="_blank">'+esc(t.title)+'</a></h4><p>'+esc(t.summary)+'</p><div class="meta">'+esc(t.source)+' \u00b7 '+esc(t.category)+' \u00b7 <span class="stars">'+starsStr(t.rating)+'</span></div></div></div>';
  });
  document.getElementById('content').innerHTML=h;
}

function renderStartup(d){
  var s=d.startup_board;
  if(!s){document.getElementById('content').innerHTML='<div class="bcard"><h3>\u{1F680} \u521b\u4e1a\u677f\u5757</h3><p>\u6682\u65e0\u65b0\u52a8\u6001</p></div>';return}
  var h='<div class="sec">\u{1F680} \u521b\u4e1a\u677f\u5757 \u2014 \u91cd\u70b9\u4f01\u4e1a\u8ddf\u8e2a</div>';
  h+='<table class="stable"><tr><th>\u4f01\u4e1a</th><th>\u8d5b\u9053</th><th>\u6280\u672f\u8def\u7ebf</th><th>\u878d\u8d44/\u8ba2\u5355</th><th>\u62e9\u4e1a\u5224\u65ad</th></tr>';
  (s.companies||[]).forEach(function(c){
    h+='<tr><td><strong>'+esc(c.name)+'</strong></td><td>'+esc(c.field)+'</td><td>'+esc(c.route)+'</td><td>'+esc(c.funding)+'</td><td>'+esc(c.verdict)+'</td></tr>';
  });
  h+='</table>';
  if(s.trend)h+='<div class="bcard"><h3>\u{1F4C8} \u8d5b\u9053\u8d8b\u52bf</h3><p>'+esc(s.trend)+'</p></div>';
  document.getElementById('content').innerHTML=h;
}

function renderPM(d){
  var b=d.pm_board;
  if(!b){document.getElementById('content').innerHTML='<div class="bcard"><p>\u6682\u65e0\u65b0\u52a8\u6001</p></div>';return}
  var h='<div class="sec">\u{1F4CB} \u4ea7\u54c1\u7ecf\u7406\u677f\u5757</div>';
  (b.insights||[]).forEach(function(t){
    h+='<div class="bcard"><h3>'+esc(t.title)+'</h3><p>'+esc(t.content)+'</p></div>';
  });
  if(b.focus&&b.focus.length){
    h+='<div class="sec">\u{1F4CC} \u672a\u6765\u5173\u6ce8\u91cd\u70b9</div>';
    h+='<div class="bcard"><ul>';
    b.focus.forEach(function(f){h+='<li>'+esc(f)+'</li>'});
    h+='</ul></div>';
  }
  document.getElementById('content').innerHTML=h;
}

function renderAlgo(d){
  var b=d.algo_board;
  if(!b){document.getElementById('content').innerHTML='<div class="bcard"><p>\u6682\u65e0\u65b0\u52a8\u6001</p></div>';return}
  var h='<div class="sec">\u{1F9EC} \u7b97\u6cd5\u5de5\u7a0b\u5e08\u677f\u5757</div>';
  (b.insights||[]).forEach(function(t){
    h+='<div class="bcard"><h3>'+esc(t.title)+'</h3><p>'+esc(t.content)+'</p></div>';
  });
  if(b.tech_radar&&b.tech_radar.length){
    h+='<div class="sec">\u{1F6F0}\uFE0F \u6280\u672f\u96f7\u8fbe</div><div class="bcard">';
    b.tech_radar.forEach(function(r){
      var dot=r.status.indexOf('\u9a8c\u8bc1')!==-1?'dot-green':r.status.indexOf('\u6210\u957f')!==-1?'dot-blue':r.status.indexOf('\u89c2\u671b')!==-1?'dot-yellow':'dot-red';
      h+='<div class="radar-item"><span class="radar-dot '+dot+'"></span><span class="radar-name">'+esc(r.direction)+'</span><span class="radar-status">'+esc(r.status)+'</span><span class="radar-advice">'+esc(r.advice)+'</span></div>';
    });
    h+='</div>';
  }
  if(b.focus&&b.focus.length){
    h+='<div class="sec">\u{1F4CC} \u672a\u6765\u5173\u6ce8\u91cd\u70b9</div><div class="bcard"><ul>';
    b.focus.forEach(function(f){h+='<li>'+esc(f)+'</li>'});
    h+='</ul></div>';
  }
  document.getElementById('content').innerHTML=h;
}

function renderProj(d){
  var b=d.projmgr_board;
  if(!b){document.getElementById('content').innerHTML='<div class="bcard"><p>\u6682\u65e0\u65b0\u52a8\u6001</p></div>';return}
  var h='<div class="sec">\u{1F4C5} \u9879\u76ee\u7ecf\u7406\u677f\u5757</div>';
  (b.insights||[]).forEach(function(t){
    h+='<div class="bcard"><h3>'+esc(t.title)+'</h3><p>'+esc(t.content)+'</p></div>';
  });
  if(b.focus&&b.focus.length){
    h+='<div class="sec">\u{1F4CC} \u672a\u6765\u5173\u6ce8\u91cd\u70b9</div><div class="bcard"><ul>';
    b.focus.forEach(function(f){h+='<li>'+esc(f)+'</li>'});
    h+='</ul></div>';
  }
  document.getElementById('content').innerHTML=h;
}

function renderAction(d){
  var a=d.action_items;
  if(!a){document.getElementById('content').innerHTML='<div class="bcard"><p>\u6682\u65e0</p></div>';return}
  var h='';
  if(a.tech_selection){
    h+='<div class="sec">\u{1F527} \u6280\u672f\u9009\u578b</div><div class="bcard"><ul>';
    a.tech_selection.forEach(function(t){h+='<li>'+esc(t)+'</li>'});
    h+='</ul></div>';
  }
  if(a.track_judgment){
    h+='<div class="sec">\u{1F3AF} \u8d5b\u9053\u5224\u65ad</div><div class="bcard"><ul>';
    a.track_judgment.forEach(function(t){h+='<li>'+esc(t)+'</li>'});
    h+='</ul></div>';
  }
  if(a.watch_list){
    h+='<div class="sec">\u{1F440} Watch List</div><div class="bcard"><ul>';
    a.watch_list.forEach(function(t){h+='<li>'+esc(t)+'</li>'});
    h+='</ul></div>';
  }
  document.getElementById('content').innerHTML=h;
}

function renderAll(d){
  var arts=d.raw_articles||[];
  var h='<div class="search-bar"><span class="ico">\\uD83D\\uDD0D</span><input id="sInput" placeholder="\\u641c\\u7d22\\u6807\\u9898\\u6216\\u6458\\u8981..." oninput="filterAll()"></div>';
  h+='<div id="allList"></div>';
  document.getElementById('content').innerHTML=h;
  window._allArts=arts;
  filterAll();
}

function filterAll(){
  var q=(document.getElementById('sInput')||{}).value||'';
  q=q.toLowerCase().trim();
  var arts=window._allArts||[];
  if(q)arts=arts.filter(function(a){return a.title.toLowerCase().indexOf(q)!==-1||a.summary.toLowerCase().indexOf(q)!==-1});
  var h='';
  if(!arts.length){h='<div style="text-align:center;padding:2rem;color:var(--t2)">\\u672a\\u627e\\u5230\\u5339\\u914d\\u8d44\\u8baf</div>'}
  else{arts.forEach(function(a){
    h+='<div class="ncard"><div class="left"><h4><a href="'+esc(a.url)+'" target="_blank">'+esc(a.title)+'</a></h4><div class="nm">'+esc(a.source)+' \u00b7 '+a.publish_time+' \u00b7 '+starsStr(a.rating)+'</div></div><div class="right"><span class="cat">'+esc(a.category)+'</span></div></div>';
  })}
  document.getElementById('allList').innerHTML=h;
}

function toggleTheme(){
  var dk=document.body.getAttribute('data-theme')==='dark';
  document.body.setAttribute('data-theme',dk?'light':'dark');
  document.querySelector('.tbtn').innerHTML=dk?'&#x1F319;':'&#x2600;&#xFE0F;';
  localStorage.setItem('ai-news-theme',dk?'light':'dark');
}

document.addEventListener('DOMContentLoaded',function(){
  var sv=localStorage.getItem('ai-news-theme');
  if(sv==='dark'||(!sv&&window.matchMedia('(prefers-color-scheme:dark)').matches)){
    document.body.setAttribute('data-theme','dark');
    document.querySelector('.tbtn').innerHTML='&#x2600;&#xFE0F;';
  }
  initDays();initTabs();render();
});
</script>
</body>
</html>`;

fs.writeFileSync(path.join(__dirname, 'site/index.html'), html, 'utf8');
console.log('Build OK! Days: ' + days.join(', ') + ' | Articles: ' + Object.values(allData).reduce((s,d) => s + (d.raw_articles||[]).length, 0));
