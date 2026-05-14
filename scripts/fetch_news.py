#!/usr/bin/env python3
"""Fetch AI news from RSS feeds and output raw data for processing.

Usage:
  python3 scripts/fetch_news.py

Outputs /tmp/raw_ai_news.json with title/url/source for each article.
The LLM or add_boards.py can then generate summaries, categories, ratings,
and role-specific boards from this data.

Run from the ai_news project root directory.
"""
import urllib.request
import ssl
import re
import json
import time
import html as html_mod
import random
import os

ssl_ctx = ssl.create_default_context()

def fetch(url, timeout=12, retry=2):
    """Fetch URL with retry and exponential backoff."""
    for attempt in range(retry):
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,text/xml,application/xml,*/*',
            })
            resp = urllib.request.urlopen(req, timeout=timeout, context=ssl_ctx)
            return resp.read().decode('utf-8', errors='replace')
        except Exception as e:
            if attempt < retry - 1:
                time.sleep(random.uniform(3, 6))
            else:
                print(f"  FAIL: {url} -> {e}")
                return None

def parse_rss(html):
    """Parse RSS/Atom feeds, handling CDATA and HTML in descriptions."""
    items = []
    
    # Try CDATA descriptions first
    cdata_blocks = re.findall(r'<description[^>]*>\s*<!\[CDATA\[(.*?)\]\]>\s*</description>', html, re.DOTALL)
    encoded = re.findall(r'<content:encoded[^>]*>\s*<!\[CDATA\[(.*?)\]\]>\s*</content:encoded>', html, re.DOTALL)
    
    # Standard descriptions
    titles = re.findall(r'<title[^>]*>([^<]+)</title>', html)
    links = re.findall(r'<link[^>]*>([^<]+)</link>', html)
    descs = re.findall(r'<description[^>]*>([^<]+)</description>', html)
    
    if len(titles) > 1:
        # RSS 2.0
        for i in range(min(len(titles), len(links))):
            desc = ''
            if i < len(cdata_blocks):
                desc = cdata_blocks[i]
            elif i < len(encoded):
                desc = encoded[i]
            elif i < len(descs):
                desc = descs[i]
            desc = re.sub(r'<[^>]+>', ' ', desc)
            desc = re.sub(r'\s+', ' ', html_mod.unescape(desc)).strip()[:500]
            items.append({
                'title': re.sub(r'\s+', ' ', html_mod.unescape(titles[i])).strip(),
                'url': re.sub(r'\s+', '', links[i]).strip(),
                'summary': desc
            })
    else:
        # Atom
        titles = re.findall(r'<title[^>]*>([^<]+)</title>', html)
        links = re.findall(r'<link[^>]+href="([^"]+)"', html)
        descs = re.findall(r'<summary[^>]*>\s*<!\[CDATA\[(.*?)\]\]>\s*</summary>', html, re.DOTALL)
        if not descs:
            descs = re.findall(r'<summary[^>]*>([^<]+)</summary>', html)
        for i in range(min(len(titles), len(links))):
            desc = descs[i] if i < len(descs) else ''
            desc = re.sub(r'<[^>]+>', ' ', desc)
            desc = re.sub(r'\s+', ' ', html_mod.unescape(desc)).strip()[:500]
            items.append({
                'title': re.sub(r'\s+', ' ', html_mod.unescape(titles[i])).strip(),
                'url': re.sub(r'\s+', '', links[i]).strip(),
                'summary': desc
            })
    return items

# RSS feeds to scrape (ordered by reliability)
FEEDS = [
    ('Ars Technica AI', 'https://arstechnica.com/ai/feed/'),
    ('TechCrunch AI', 'https://techcrunch.com/category/artificial-intelligence/feed/'),
    ('Wired AI', 'https://www.wired.com/feed/tag/ai/latest/rss'),
    ('MIT Tech Review', 'https://www.technologyreview.com/feed/'),
    ('TechCrunch main', 'https://techcrunch.com/feed/'),
    ('Ars Technica main', 'https://arstechnica.com/feed/'),
]

# Keywords to filter AI-related articles
AI_KW = [
    'ai', 'artificial intelligence', 'machine learning', 'llm', 'robot',
    'chatgpt', 'claude', 'gpt', 'openai', 'anthropic', 'deep learning',
    'neural', 'generative', 'embodiment', 'data center', 'compute', 'gpu',
    'groq', 'xai', 'grok', 'musk', 'altman'
]

# Navigation titles to skip
NAV_TITLES = {
    'ai', 'ai news & artificial intelligence | techcrunch',
    'feed: artificial intelligence latest', 'ai - ars technica',
    'mit technology review'
}

def main():
    all_items = []
    seen = set()
    
    for name, url in FEEDS:
        print(f"Fetching {name}...")
        h = fetch(url)
        if h:
            items = parse_rss(h)
            for it in items:
                title = it['title'].strip()
                if not title or len(title) < 10 or title.lower() in NAV_TITLES:
                    continue
                key = title.lower()
                if key in seen:
                    continue
                if any(kw in (title + ' ' + it.get('summary', '')).lower() for kw in AI_KW):
                    seen.add(key)
                    it['source'] = name
                    all_items.append(it)
        time.sleep(random.uniform(1, 2))
    
    # Output to project data directory
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'raw_ai_news.json')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_items, f, ensure_ascii=False, indent=2)
    
    print(f"\nTotal unique AI articles: {len(all_items)}")
    print(f"Saved to {output_path}")
    
    # Show source distribution
    sources = {}
    for a in all_items:
        sources[a['source']] = sources.get(a['source'], 0) + 1
    for s, c in sorted(sources.items(), key=lambda x: -x[1]):
        print(f"  {s}: {c}")
    
    return all_items

if __name__ == '__main__':
    main()
