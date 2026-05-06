# 贡献指南

感谢你对 AI+具身智能资讯聚合项目的关注！

## 贡献方式

### 1. 提交新资讯

如果你想为某一天的资讯聚合贡献内容，请编辑对应的 `data/YYYY-MM-DD.json` 文件。

#### 数据格式规范

每条资讯（raw_articles 中的条目）必须包含以下字段：

```json
{
  "id": 1,
  "title": "资讯标题（必填）",
  "source": "来源媒体（必填）",
  "url": "https://原文链接（必填）",
  "publish_time": "YYYY-MM-DD",
  "summary": "资讯摘要，2-3句话（必填）",
  "category": "分类标签（必填，见下方分类表）",
  "rating": 4
}
```

#### 分类标签

请优先使用以下英文标识（也可使用中文标签，系统会自动映射）：

| 英文标识                | 中文标签      | 适用范围                     |
|-------------------------|--------------|------------------------------|
| `policy_signal`         | 政策信号      | 政府政策、监管动态             |
| `algorithm_breakthrough`| 算法突破/大模型| 模型发布、基准测试、学术论文   |
| `industry_dynamics`     | 企业动态      | 公司公告、战略合作、产品发布   |
| `market_data`           | 市场动态/市场数据| 融资、估值、上市、市场分析   |
| `open_source`           | 开源动态      | 仓库发布、SDK 更新             |
| `hardware`              | 硬件与机器人/具身智能| 机器人硬件、传感器、执行器 |
| `academic`              | 学术前沿      | 会议论文、预印本、实验室成果   |
| `other`                 | 其他          | 无法归入以上类别               |

#### 评分标准

| 评分 | 含义 | 标准                                 |
|------|------|--------------------------------------|
| 1    | 低质 | 来源不明、信息量低、纯转载             |
| 2    | 一般 | 媒体通稿、常规报道                     |
| 3    | 中等 | 有一定行业参考价值                     |
| 4    | 高质 | 独家信息、深度分析、权威来源            |
| 5    | 顶尖 | 行业里程碑事件、独家深度报道            |

### 2. 新增信源

如果你想推荐新的信息源，请按以下步骤操作：

1. 在 [Issues](https://github.com/Shnywang/ai_news/issues) 中创建 Issue，标题格式：`[信源建议] 信源名称`
2. 说明以下信息：
   - 信源 URL / RSS 地址
   - 信源类型（媒体 / 博客 / 学术 / 社交）
   - 主要内容领域
   - 更新频率
   - 为什么推荐这个信源

3. 维护者评估后会将信源加入采集管线。

### 3. 提交流程

```bash
# 1. Fork 本仓库
# 2. Clone 你的 Fork
git clone https://github.com/YOUR_USERNAME/ai_news.git
cd ai_news

# 3. 创建新分支
git checkout -b feature/add-article-YYYY-MM-DD

# 4. 编辑或新增数据文件
# 编辑 data/YYYY-MM-DD.json

# 5. 运行数据校验
node validate.js

# 6. 提交更改
git add data/
git commit -m "添加 YYYY-MM-DD 资讯"

# 7. 推送并创建 Pull Request
git push origin feature/add-article-YYYY-MM-DD
```

### 4. 代码贡献

如果你想改进构建脚本、前端界面或其他代码：

```bash
# 运行构建测试
node build.js

# 确认 site/index.html 生成正常
# 确认 site/feed.xml 生成正常
# 确认 site/sitemap.xml 生成正常
```

### 5. 审核标准

所有 Pull Request 会经过以下审核：

- [ ] JSON 格式正确
- [ ] 所有必填字段完整
- [ ] URL 链接有效
- [ ] 评分合理（1-5）
- [ ] 分类标签正确
- [ ] 标题格式规范
- [ ] 摘要准确、无抄袭

### 6. 行为准则

- 提交的内容必须真实、准确
- 禁止提交虚假信息或恶意链接
- 尊重知识产权，摘要需原创
- 友好交流，尊重不同意见

## 联系方式

- 问题反馈：[GitHub Issues](https://github.com/Shnywang/ai_news/issues)
- 讨论：[GitHub Discussions](https://github.com/Shnywang/ai_news/discussions)
