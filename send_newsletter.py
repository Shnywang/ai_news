#!/usr/bin/env python3
"""
AI资讯每日推送 - 读取 subscribers.json，抓取最新数据，通过 QQ 邮箱 SMTP 群发
Usage: python3 send_newsletter.py [--dry-run]
Cron: 每天早上 9:00 (Asia/Shanghai)
"""

import json
import os
import re
import ssl
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr, formatdate
import smtplib
import urllib.request
import http.client

# --- 配置 ---
SMTP_HOST = "smtp.qq.com"
SMTP_PORT = 465
SMTP_USER = "779284414@qq.com"
SMTP_AUTH = os.environ.get("SMTP_QQ_AUTH_CODE", "")  # 从环境变量读取授权码
SENDER_NAME = "AI资讯"
SUBSCRIBERS_URL = "https://raw.githubusercontent.com/Shnywang/ai_news/main/subscribers.json"
RSS_URL = "https://shnywang.github.io/ai_news/site/feed.xml"
SITE_URL = "https://shnywang.github.io/ai_news/site/index.html"
NEWSLETTER_DAYS = 3  # 推送最近 N 天的资讯

def get_sha(path):
    """获取 GitHub 文件的 SHA（通过 IP 直连）"""
    import base64
    TOKEN = ""
    try:
        with open(os.path.expanduser("~/.git-credentials")) as f:
            content = f.read()
        for line in content.strip().split('\n'):
            if 'ghp_' in line:
                TOKEN = line[line.index('ghp_'):line.index('@github.com')]
                break
    except:
        pass
    
    GITHUB_IP = "140.82.121.6"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    conn = http.client.HTTPSConnection(GITHUB_IP, 443, context=ctx)
    conn.request('GET', f'/repos/Shnywang/ai_news/contents/{path}?ref=main',
                 headers={
                     'Host': 'api.github.com',
                     'Authorization': f'Bearer {TOKEN}',
                     'User-Agent': 'Hermes'
                 })
    data = json.loads(conn.getresponse().read())
    conn.close()
    return data['sha']

def update_subscribers_on_github(email, new_content):
    """通过 GitHub API 更新 subscribers.json"""
    import base64
    TOKEN = ""
    try:
        with open(os.path.expanduser("~/.git-credentials")) as f:
            content = f.read()
        for line in content.strip().split('\n'):
            if 'ghp_' in line:
                TOKEN = line[line.index('ghp_'):line.index('@github.com')]
                break
    except:
        pass
    
    sha = get_sha("subscribers.json")
    content_b64 = base64.b64encode(new_content.encode()).decode()
    
    payload = json.dumps({
        "message": f"sub: add {email}",
        "content": content_b64,
        "sha": sha,
        "branch": "main"
    })
    
    GITHUB_IP = "140.82.121.6"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    conn = http.client.HTTPSConnection(GITHUB_IP, 443, context=ctx)
    conn.request('PUT', '/repos/Shnywang/ai_news/contents/subscribers.json',
                 payload.encode(),
                 headers={
                     'Host': 'api.github.com',
                     'Authorization': f'Bearer {TOKEN}',
                     'User-Agent': 'Hermes',
                     'Content-Type': 'application/json'
                 })
    resp = conn.getresponse()
    data = json.loads(resp.read())
    conn.close()
    
    if 'message' in data and 'sha' not in data.get('content', {}):
        raise Exception(f"Failed to update subscribers: {data.get('message')}")
    
    return data['content']['sha']

def add_subscriber(email):
    """添加订阅者到 subscribers.json"""
    # 读取当前列表
    try:
        req = urllib.request.Request(SUBSCRIBERS_URL)
        with urllib.request.urlopen(req, timeout=10) as resp:
            subs = json.loads(resp.read().decode())
    except:
        subs = []
    
    if email in subs:
        print(f"  {email} already subscribed, skipping")
        return False
    
    subs.append(email)
    new_content = json.dumps(subs, ensure_ascii=False)
    
    sha = update_subscribers_on_github(email, new_content)
    print(f"  Added {email} to subscribers.json (SHA: {sha[:12]})")
    return True

def fetch_feed():
    """获取 RSS feed 数据"""
    try:
        req = urllib.request.Request(RSS_URL)
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml_data = resp.read().decode()
    except Exception as e:
        print(f"Error fetching RSS: {e}")
        return []
    
    articles = []
    for item in ET.fromstring(xml_data).findall('item'):
        title = item.findtext('title', '')
        link = item.findtext('link', '')
        pubDate = item.findtext('pubDate', '')
        category = item.findtext('category', '')
        description = item.findtext('description', '')
        articles.append({
            'title': title,
            'link': link,
            'pubDate': pubDate,
            'category': category,
            'description': description[:100] + '...' if description and len(description) > 100 else description
        })
    
    return articles

def build_email_content(articles, date_str):
    """构建 HTML 邮件内容"""
    if not articles:
        return "<p>暂无新资讯。</p>"
    
    # 按分类分组
    categories = {}
    for a in articles:
        cat = a['category'] or '其他'
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(a)
    
    html = f"""<html>
<head>
<style>
  body {{ font-family: -apple-system, 'Segoe UI', 'Microsoft YaHei', sans-serif; background: #f8f9fa; margin: 0; padding: 0; }}
  .container {{ max-width: 600px; margin: 0 auto; background: #fff; }}
  .header {{ background: linear-gradient(135deg, #1a3a5c, #2980b9); color: #fff; padding: 30px 20px; text-align: center; }}
  .header h1 {{ margin: 0; font-size: 22px; }}
  .header p {{ margin: 8px 0 0; opacity: 0.8; font-size: 14px; }}
  .content {{ padding: 20px; }}
  .section {{ margin-bottom: 25px; }}
  .section-title {{ color: #1a3a5c; font-size: 16px; border-bottom: 2px solid #d5e1ed; padding-bottom: 6px; margin-bottom: 12px; }}
  .article {{ padding: 10px 0; border-bottom: 1px solid #f0f0f0; }}
  .article a {{ color: #2980b9; text-decoration: none; font-size: 14px; line-height: 1.5; font-weight: 600; }}
  .article a:hover {{ color: #1a3a5c; }}
  .article .desc {{ color: #666; font-size: 12px; margin-top: 4px; }}
  .article .date {{ color: #999; font-size: 11px; float: right; }}
  .footer {{ background: #f8f9fa; padding: 20px; text-align: center; font-size: 12px; color: #999; }}
  .footer a {{ color: #2980b9; text-decoration: none; }}
  .badge {{ display: inline-block; background: #d5e1ed; color: #1a3a5c; padding: 2px 8px; border-radius: 10px; font-size: 11px; margin-bottom: 6px; }}
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>AI资讯日报</h1>
    <p>{date_str} | 每日精选 AI 行业动态</p>
  </div>
  <div class="content">"""
    
    for cat, arts in categories.items():
        cat_display = {
            'algorithm_breakthrough': '算法突破',
            'academic': '学术论文',
            'market_data': '市场动态',
            'hardware': '具身智能',
            'policy_signal': '政策信号',
            'industry_dynamics': '企业动态',
            'open_source': '开源动态',
            'other': '其他'
        }.get(cat, cat)
        
        html += f'\n  <div class="section">\n    <div class="section-title">{cat_display}</div>\n'
        for a in arts:
            date_part = a['pubDate'][:10] if a['pubDate'] else ''
            html += f'    <div class="article">\n'
            html += f'      <a href="{a["link"]}" target="_blank">{a["title"]}</a>\n'
            if date_part:
                html += f'      <span class="date">{date_part}</span>\n'
            if a.get('description'):
                html += f'      <div class="desc">{a["description"]}</div>\n'
            html += '    </div>\n'
        html += '  </div>\n'
    
    html += f"""  </div>
  <div class="footer">
    <p>由 <a href="{SITE_URL}" target="_blank">AI资讯</a> 自动发送 | 共 {len(articles)} 条资讯</p>
    <p>如果您不想继续接收，请回复此邮件"退订"以取消订阅</p>
  </div>
</div>
</body>
</html>"""
    
    return html

def send_email(recipient, subject, html_content):
    """通过 QQ 邮箱 SMTP 发送邮件"""
    msg = MIMEMultipart('alternative')
    msg['From'] = formataddr((SENDER_NAME, SMTP_USER))
    msg['To'] = recipient
    msg['Subject'] = subject
    msg['Date'] = formatdate(localtime=True)
    
    msg.attach(MIMEText(html_content, 'html', 'utf-8'))
    
    try:
        ctx = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=ctx) as server:
            server.login(SMTP_USER, SMTP_AUTH)
            server.sendmail(SMTP_USER, recipient, msg.as_string())
        return True
    except Exception as e:
        print(f"  Failed to send to {recipient}: {e}")
        return False

def main():
    dry_run = "--dry-run" in sys.argv
    
    print("=== AI资讯日报推送 ===")
    print(f"时间: {datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M')}")
    
    # 1. 获取订阅者列表
    print("\n[1/4] 获取订阅者列表...")
    try:
        req = urllib.request.Request(SUBSCRIBERS_URL)
        with urllib.request.urlopen(req, timeout=10) as resp:
            subscribers = json.loads(resp.read().decode())
    except Exception as e:
        print(f"  Error fetching subscribers: {e}")
        subscribers = []
    
    print(f"  订阅者数量: {len(subscribers)}")
    if not subscribers:
        print("  暂无订阅者，跳过发送")
        return
    
    # 2. 获取最新资讯
    print("\n[2/4] 获取最新资讯...")
    articles = fetch_feed()
    print(f"  RSS 文章总数: {len(articles)}")
    
    # 取最近的 (按 pubDate 排序，取前 N 天)
    if articles:
        recent = articles[:30]  # 取最新 30 条
        print(f"  本次推送: {len(recent)} 条")
    else:
        recent = []
        print("  无可用资讯")
        return
    
    # 3. 构建邮件
    print("\n[3/4] 构建邮件内容...")
    today = datetime.now(timezone(timedelta(hours=8))).strftime('%Y年%m月%d日')
    subject = f"AI资讯日报 - {today}"
    html = build_email_content(recent, today)
    print(f"  邮件主题: {subject}")
    print(f"  邮件内容: {len(html)} 字符")
    
    # 4. 发送
    print(f"\n[4/4] 发送邮件...")
    if dry_run:
        print("  [DRY RUN 模式] 不会实际发送")
        for i, email in enumerate(subscribers):
            print(f"  [{i+1}/{len(subscribers)}] 将发送给: {email}")
        print("\n=== DRY RUN 完成 ===")
        return
    
    if not SMTP_AUTH:
        print("  ERROR: SMTP_QQ_AUTH_CODE 环境变量未设置")
        print("  请设置: export SMTP_QQ_AUTH_CODE='你的授权码'")
        sys.exit(1)
    
    sent = 0
    failed = 0
    for i, email in enumerate(subscribers):
        print(f"  [{i+1}/{len(subscribers)}] 发送给: {email}", end=" ")
        if send_email(email, subject, html):
            sent += 1
            print("OK")
        else:
            failed += 1
            print("FAIL")
        # 间隔 1-2 秒，避免触发限流
        import time
        time.sleep(1.5)
    
    print(f"\n=== 完成 ===")
    print(f"成功: {sent} | 失败: {failed} | 总计: {len(subscribers)}")

if __name__ == "__main__":
    main()
