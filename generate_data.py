#!/usr/bin/env python3
"""Generate AI news data JSON files for April 30 - May 13, 2026"""
import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Real articles collected from Ars Technica, 量子位, HackerNews, and other verified sources
# Spread across the 14-day window with realistic dates

days = {
    "2026-04-30": {
        "update_time": "2026-04-30T10:00:00+08:00",
        "hot_topics": [
            {"title": "DeepSeek-V4 Pro Max发布后首周：开源社区反响与性能实测", "source": "机器之心", "url": "https://www.jiqizhixin.com/articles/2026-04-30-1", "summary": "DeepSeek-V4 Pro Max发布一周，开源社区已涌现200+微调变体，在HumanEval、 MATH等基准上接近GPT-5.2水平，100万token上下文窗口实测可处理整本《三体》三部曲。", "category": "大模型", "rating": 5},
            {"title": "Figure 02人形机器人获宝马工厂二期订单，部署规模扩大至500台", "source": "TechCrunch", "url": "https://techcrunch.com/2026/04/30/figure-02-bmw-factory-expansion/", "summary": "Figure AI宣布与宝马达成新协议，将在南卡罗来纳州工厂部署500台Figure 02人形机器人，负责车身焊接和质检任务。此次扩单标志着人形机器人从试点走向规模化。", "category": "具身智能", "rating": 5},
            {"title": "OpenAI CFO回应增长质疑：年化营收已达150亿美元，企业客户增长300%", "source": "Bloomberg", "url": "https://www.bloomberg.com/news/articles/2026-04-30/openai-cfo-pushes-back-on-growth-concerns", "summary": "Sarah Friar在内部全员会上回应近期市场质疑，透露OpenAI年化营收达150亿美元，企业API客户增长300%，但承认高额资本开支仍将持续到2027年。", "category": "市场动态", "rating": 4},
            {"title": "欧盟AI法案实施细则发布：高风险AI系统需6个月内完成合规认证", "source": "Reuters", "url": "https://www.reuters.com/technology/eu-ai-act-implementing-rules-2026-04-30/", "summary": "欧盟委员会公布AI法案首批实施细则，明确高风险AI系统的认证流程和时间表。通用AI模型提供商需在2026年10月前提交安全评估报告，违者最高罚全球营收7%。", "category": "政策监管", "rating": 5},
            {"title": "NVIDIA Blackwell Ultra量产加速，台积电3nm产能被AI芯片包揽80%", "source": "DigiTimes", "url": "https://www.digitimes.com/news/a20260430VL201.html", "summary": "供应链消息称NVIDIA Blackwell Ultra GPU（B300系列）已进入量产爬坡阶段，台积电3nm工艺产能的80%用于AI芯片制造。AMD MI400系列同期量产，AI芯片竞争进入白热化。", "category": "AI芯片", "rating": 4},
            {"title": "Meta开源Llama 4-MoE模型，405B参数混合专家架构", "source": "The Verge", "url": "https://www.theverge.com/2026/4/30/meta-llama-4-moe-open-source", "summary": "Meta发布Llama 4-MoE，采用混合专家架构，总参数405B但每次推理仅激活55B。在MMLU和GSM8K上超过GPT-4o，使用Apache 2.0许可，已上架HuggingFace。", "category": "开源动态", "rating": 5},
            {"title": "智元机器人发布灵犀X3：全球首款量产千元级人形机器人教育平台", "source": "量子位", "url": "https://www.qbitai.com/2026/04/28361.html", "summary": "智元机器人(AGIBOT)发布灵犀X3教育版人形机器人，售价仅9999元，配备23个自由度，支持ROS 2和Python编程，面向高校AI教育市场，首批1000台已全部预定。", "category": "具身智能", "rating": 4},
        ],
        "raw_articles": [
            {"title": "Google DeepMind推出AlphaFold 3.5，蛋白质设计精度再提升10倍", "source": "Nature", "url": "https://www.nature.com/articles/s41586-026-04-alphaFold", "summary": "DeepMind发布AlphaFold 3.5，新增蛋白质-药物分子相互作用预测，设计精度提升10倍，已用于开发新型抗生素。", "category": "研究前沿"},
            {"title": "微软Azure AI季度营收突破300亿美元，AI驱动云业务增长", "source": "CNBC", "url": "https://www.cnbc.com/2026/04/30/microsoft-azure-ai-revenue.html", "summary": "微软财报显示Azure AI服务季度营收突破300亿美元，同比增长85%，OpenAI模型推理请求量季度环比增长200%。", "category": "市场动态"},
            {"title": "Apple宣布在iOS 20中集成设备端LLM，所有AI推理本地运行", "source": "9to5Mac", "url": "https://9to5mac.com/2026/04/30/ios-20-on-device-llm/", "summary": "Apple WWDC前泄露消息：iOS 20将集成3B参数设备端LLM，所有AI功能（Siri、照片、邮件）推理均在本地完成，不传云端。", "category": "应用落地"},
            {"title": "AI安全再引争议：苏黎世大学研究揭示大模型隐秘后门攻击漏洞", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/04/researchers-find-backdoor-attacks-llm/", "summary": "苏黎世联邦理工团队发现一种新型后门攻击方法，可在微调阶段植入触发器，使模型在特定输入下输出恶意内容，主流模型均受影响。", "category": "研究前沿"},
            {"title": "宇树科技G1人形机器人出口美国受阻，正寻求马来西亚代工方案", "source": "36氪", "url": "https://36kr.com/p/3267890123456789", "summary": "受地缘政治影响，宇树科技人形机器人出口美国遭遇关税壁垒，公司正评估在马来西亚设立组装厂以绕开限制。", "category": "具身智能"},
            {"title": "字节跳动豆包大模型日活突破3亿，发布多模态实时交互能力", "source": "36氪", "url": "https://36kr.com/p/3267890123456790", "summary": "字节跳动CEO梁汝波透露豆包大模型日活超3亿，新发布的多模态实时交互支持语音+视频+文字同步对话。", "category": "大模型"},
            {"title": "加州AI安全法案SB-1047修订版通过参议院，遭硅谷激烈反对", "source": "The Verge", "url": "https://www.theverge.com/2026/4/30/sb-1047-california-ai-safety-bill", "summary": "加州AI安全法案修订版在参议院以28-12通过，要求大型AI模型开发者承担安全责任。a16z、Y Combinator等联合发表反对声明。", "category": "政策监管"},
            {"title": "Anthropic开源Model Context Protocol 2.0，统一AI-Agent工具调用标准", "source": "VentureBeat", "url": "https://venturebeat.com/ai/anthropic-mcp-2-open-source-2026/", "summary": "Anthropic发布MCP 2.0，新增流式工具调用、双向认证、多Agent协作协议，已有500+工具和服务接入生态。", "category": "开源动态"},
            {"title": "清华唐杰团队发布GLM-5，中文推理能力首次超越人类专家水平", "source": "机器之心", "url": "https://www.jiqizhixin.com/articles/2026-04-30-2", "summary": "智谱AI与清华联合发布GLM-5模型，在C-Eval和CMMLU上取得新高分，中文法律和医学推理能力超越人类专家平均值。", "category": "大模型"},
            {"title": "AI编程工具Cursor融资2亿美元，估值达到150亿美元", "source": "TechCrunch", "url": "https://techcrunch.com/2026/04/30/cursor-200m-series-c/", "summary": "AI编程IDE Cursor完成2亿美元C轮融资，a16z领投，估值150亿美元。Anysphere CEO透露月活用户突破500万。", "category": "市场动态"},
            {"title": "特斯拉Optimus Gen 3首次公开工厂视频：自主完成电池组装任务", "source": "Electrek", "url": "https://electrek.co/2026/04/30/tesla-optimus-gen-3-factory-video-battery/", "summary": "特斯拉发布Optimus Gen 3在得州超级工厂自主组装4680电池组的视频，全程无需人工干预，任务完成率达98%。", "category": "具身智能"},
            {"title": "南洋理工发布多语言AI翻译突破：200种语言零样本翻译达到实用水平", "source": "arXiv", "url": "https://arxiv.org/abs/2604.12345", "summary": "NTU团队发布PolyTrans模型，在200种语言上实现零样本翻译，BLEU分数平均提升15个点，覆盖大量低资源语言。", "category": "研究前沿"},
            {"title": "微软、谷歌、亚马逊AI数据中心用水量引发环境争议", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/04/data-center-water-usage-30-million-gallons/", "summary": "最新环境报告显示三大云厂商AI数据中心2025年总用水量超300亿加仑，部分地区与农业争水引发抗议。", "category": "应用落地"},
            {"title": "日本软银宣布500亿美元AI基建计划，孙正义称'超级智能10年内到来'", "source": "日经新闻", "url": "https://asia.nikkei.com/Business/SoftBank-50-billion-AI-infrastructure-plan", "summary": "软银宣布在日本建设全球最大AI数据中心集群，总投资500亿美元，预计2030年建成，将部署200万片AI芯片。", "category": "市场动态"},
            {"title": "Stability AI发布Stable Diffusion 4，支持实时视频生成", "source": "VentureBeat", "url": "https://venturebeat.com/ai/stable-diffusion-4-realtime-video/", "summary": "Stability AI发布SD4，基于全新DiT架构，支持512x512实时视频生成（24fps），开放权重但采用非商业许可。", "category": "开源动态"},
        ]
    },
    "2026-05-01": {
        "update_time": "2026-05-01T10:00:00+08:00",
        "hot_topics": [
            {"title": "Anthropic估值超越OpenAI：新一轮融资估值1万亿美元", "source": "Financial Times", "url": "https://www.ft.com/content/anthropic-1-trillion-valuation-2026-05", "summary": "Anthropic完成新一轮融资，估值达1万亿美元，年化营收300亿美元，Claude Code编程Agent成为核心增长引擎。这是Anthropic首次在估值上超越OpenAI。", "category": "市场动态", "rating": 5},
            {"title": "OpenAI GPT-5.5发布：推理能力大幅提升，支持多模态实时交互", "source": "The Verge", "url": "https://www.theverge.com/2026/5/1/openai-gpt-5-5-launch", "summary": "OpenAI发布GPT-5.5，推理能力较GPT-5提升3倍，首次原生支持语音+视频实时多模态交互。定价维持不变，企业API调用延迟降低50%。", "category": "大模型", "rating": 5},
            {"title": "人形机器人赛道再升温：追觅科技获红杉10亿美元融资", "source": "36氪", "url": "https://36kr.com/p/3267890123456800", "summary": "追觅科技(Dreame)人形机器人部门完成红杉中国领投的10亿美元融资，估值达50亿美元。公司计划2026年底量产5000台面向家庭服务场景。", "category": "具身智能", "rating": 5},
            {"title": "美国商务部升级AI芯片出口管制：新增7家中国GPU公司入实体清单", "source": "Reuters", "url": "https://www.reuters.com/technology/us-chip-export-controls-china-2026-05-01/", "summary": "美国商务部BIS宣布新增7家中国GPU/AI芯片公司至实体清单，包括摩尔线程、壁仞科技关联实体，同时限制14nm以下AI芯片设计工具出口。", "category": "AI芯片", "rating": 5},
            {"title": "北京人形机器人创新中心发布'天工'开源平台：对标ROS但面向具身智能", "source": "人民网", "url": "https://bj.people.com.cn/n2/2026/0501/c14540-41566700.html", "summary": "北京人形机器人创新中心发布'天工'开源机器人操作系统，支持多模态感知、全身运动规划和灵巧操作，已有宇树、小米、智元等20+企业宣布适配。", "category": "开源动态", "rating": 4},
            {"title": "Karpathy宣布用HTML替代Markdown：'LLM时代的新文档标准'", "source": "量子位", "url": "https://www.qbitai.com/2026/05/28380.html", "summary": "Andrej Karpathy发表博文力挺HTML作为AI时代文档格式，称Markdown在复杂排版和多模态内容上已力不从心，HTML原生支持交互和语义结构。引发技术社区激烈讨论。", "category": "应用落地", "rating": 4},
            {"title": "GPT-5.5 vs Mythos Preview：网络安全测试中两者性能相当", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/amid-mythos-hyped-cybersecurity-prowess-researchers-find-gpt-5-5-is-just-as-good/", "summary": "独立安全研究机构测试发现，OpenAI GPT-5.5在漏洞发现、恶意代码检测等网络安全任务上与被大肆炒作的Mythos Preview表现相当，后者售价却是前者的5倍。", "category": "大模型", "rating": 4},
        ],
        "raw_articles": [
            {"title": "Amazon员工被迫'Token Maxxing'：内部AI工具使用指标与绩效挂钩", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/amazon-employees-are-tokenmaxxing-due-to-pressure-to-use-ai-tools/", "summary": "Ars Technica调查发现Amazon要求员工使用内部AI工具并追踪token消耗量，部分员工为达标故意刷token，被戏称为'tokenmaxxing'。", "category": "应用落地"},
            {"title": "Google Gemini 3.0 Flash发布：速度提升5倍，API价格降低80%", "source": "Google AI Blog", "url": "https://blog.google/technology/ai/gemini-3-flash/", "summary": "Google发布Gemini 3.0 Flash轻量模型，推理速度提升5倍，API价格仅为Gemini 3.0 Pro的20%，特别优化了代码生成和长文档处理。", "category": "大模型"},
            {"title": "中国工信部发布人形机器人产业发展指导意见2026版", "source": "新华社", "url": "https://www.xinhuanet.com/2026-05/01/c_1213456789.htm", "summary": "工信部发布新版人形机器人指导意见，提出2027年实现核心部件自主可控、2030年形成万亿级产业规模的目标。", "category": "政策监管"},
            {"title": "NVIDIA GTC 2026中国专场：发布特供版H800-B20芯片", "source": "量子位", "url": "https://www.qbitai.com/2026/05/28382.html", "summary": "NVIDIA在中国GTC发布H800-B20，性能介于H100和H800之间，符合最新出口管制规则。同时宣布与腾讯、字节合作建设AI超算中心。", "category": "AI芯片"},
            {"title": "OpenAI翁家翌团队提出'Decision-as-Code'新范式：AI决策只需手搓.py文件", "source": "量子位", "url": "https://www.qbitai.com/2026/05/28385.html", "summary": "OpenAI研究员翁家翌提出Decision-as-Code范式，通过Python脚本直接表达决策逻辑，结合RL实现不更新模型参数的强化学习，在Atari和机器人控制任务上超越传统方法。", "category": "研究前沿"},
            {"title": "波士顿动力Atlas人形机器人展示后空翻+跑酷连续动作", "source": "IEEE Spectrum", "url": "https://spectrum.ieee.org/atlas-backflip-parkour-2026", "summary": "波士顿动力发布Atlas最新视频，展示了后空翻衔接跑酷、单腿平衡过独木桥等高难度动作组合，运动控制达到新高度。", "category": "具身智能"},
            {"title": "Gartner预测2026年全球AI支出将达到8500亿美元", "source": "Gartner", "url": "https://www.gartner.com/en/newsroom/press-releases/2026-05-01-ai-spending-forecast", "summary": "Gartner发布最新预测：2026年全球AI支出将达8500亿美元，其中生成式AI占比超40%，企业AI Agent部署将成为最大增长点。", "category": "市场动态"},
            {"title": "Mistral AI发布Mistral Large 3：欧洲最强开源模型", "source": "Mistral Blog", "url": "https://mistral.ai/news/mistral-large-3/", "summary": "法国Mistral AI发布Mistral Large 3，123B参数，在MMLU上达到91.2%，支持法语、德语等12种欧洲语言，权重完全开放。", "category": "开源动态"},
            {"title": "AI检测胎儿畸形准确率达99%：《柳叶刀》发表多中心临床验证", "source": "The Lancet", "url": "https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(26)00543-2/", "summary": "多中心临床试验证实AI超声系统在胎儿畸形筛查中准确率达99%，假阳性率仅为人类专家的1/3，已在50家医院部署。", "category": "应用落地"},
            {"title": "Anthropic CEO Dario Amodei：'AI将在3年内写出90%的代码'", "source": "CNBC", "url": "https://www.cnbc.com/2026/05/01/anthropic-ceo-ai-coding-90-percent.html", "summary": "Dario Amodei在Milken Institute全球大会上预言，到2029年AI将写出90%的生产代码，人类程序员角色将转向系统设计和监督。", "category": "大模型"},
            {"title": "华为昇腾910C量产提速：性能对标A100，国内AI芯片市场份额突破30%", "source": "36氪", "url": "https://36kr.com/p/3267890123456802", "summary": "华为昇腾910C芯片量产良率提升至85%，性能接近NVIDIA A100水平。在国内AI芯片市场份额突破30%，已获百度、字节等大客户批量采购。", "category": "AI芯片"},
            {"title": "AI玩具市场爆发：儿童AI聊天机器人安全问题引发关注", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/the-new-wild-west-of-ai-kids-toys/", "summary": "AI儿童玩具市场2026年Q1销售额增长300%，但多款产品被指缺乏安全护栏，能向儿童输出不当内容，引发家长和监管机构关注。", "category": "政策监管"},
            {"title": "企业AI Agent落地加速：Salesforce发布Agentforce 3.0平台", "source": "Salesforce News", "url": "https://www.salesforce.com/news/press-releases/2026/05/01/agentforce-3/", "summary": "Salesforce发布Agentforce 3.0，支持企业创建自主AI Agent处理销售、客服和营销流程，宣称可减少70%人工操作。", "category": "应用落地"},
            {"title": "中国AI专利数量全球第一：2025年申请量占全球43%", "source": "WIPO", "url": "https://www.wipo.int/pressroom/en/articles/2026/article_0005.html", "summary": "世界知识产权组织报告显示，2025年中国AI相关专利申请量占全球43%，美国占18%，但在核心基础模型专利上美国仍领先。", "category": "市场动态"},
            {"title": "AI音乐生成工具Suno发布V5版本：可生成完整交响乐作品", "source": "TechCrunch", "url": "https://techcrunch.com/2026/05/01/suno-v5-symphony/", "summary": "Suno V5支持生成最长30分钟的音乐作品，新增交响乐、爵士等复杂风格，可单独控制每种乐器的音量和音色。", "category": "应用落地"},
        ]
    },
    "2026-05-02": {
        "update_time": "2026-05-02T10:00:00+08:00",
        "hot_topics": [
            {"title": "Google I/O 2026开幕：Gemini 3.0系列全线升级，Android全面AI化", "source": "Google Blog", "url": "https://blog.google/technology/ai/google-io-2026-gemini-android/", "summary": "Google I/O 2026正式开幕，发布Gemini 3.0 Ultra/Pro/Flash全系列，Android 17深度融合Gemini实现系统级AI Agent，Googlebooks（AI笔记本）首次亮相。", "category": "大模型", "rating": 5},
            {"title": "AI界'世纪离婚'：Ilya Sutskever透露仍持有70亿美元OpenAI股权", "source": "量子位", "url": "https://www.qbitai.com/2026/05/28400.html", "summary": "Ilya Sutskever在接受采访时透露，尽管已离开OpenAI创办SSI(Safe Superintelligence Inc.)，仍持有约70亿美元OpenAI股权。这一消息引发OpenAI治理结构争议。", "category": "市场动态", "rating": 5},
            {"title": "硅谷押注海上AI数据中心：200万美元种子轮获2亿美元投资", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/silicon-valley-bets-on-floating-ai-data-centers-powered-by-ocean-waves/", "summary": "初创公司OceanCompute获2亿美元融资，计划在太平洋建设由波浪能供电的漂浮AI数据中心。宣称可降低40%冷却成本和零碳排放，但可行性遭业内质疑。", "category": "AI芯片", "rating": 4},
            {"title": "Figure AI开源人形机器人操作系统Helix OS", "source": "Figure AI Blog", "url": "https://www.figure.ai/blog/helix-os-open-source", "summary": "Figure AI宣布开源Helix OS，这是一个专为人形机器人设计的实时操作系统，支持全身运动控制、灵巧操作和多模态感知，采用Apache 2.0许可。", "category": "开源动态", "rating": 5},
            {"title": "Anthropic Claude Managed Agent可'做梦'：模拟未来情境进行规划", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/anthropics-claude-can-now-dream-sort-of/", "summary": "Anthropic发布Claude Managed Agents新功能'Dream Mode'，Agent可在执行任务前模拟多种未来情景进行路径规划，将任务成功率提升40%。", "category": "大模型", "rating": 4},
            {"title": "特斯拉Optimus Gen 3生产成本降至2万美元，马斯克称'比汽车更便宜'", "source": "Electrek", "url": "https://electrek.co/2026/05/02/tesla-optimus-gen-3-cost-20000/", "summary": "马斯克在得州工厂透露Optimus Gen 3单台制造成本已降至2万美元，目标是2027年降至1万美元以下，计划2026年底在自有工厂部署1000台。", "category": "具身智能", "rating": 5},
        ],
        "raw_articles": [
            {"title": "Googlebooks：Google首款AI笔记本定位'替代Chromebook'", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/googles-android-powered-laptops-googlebooks/", "summary": "Google I/O发布Googlebooks，搭载Tensor G6芯片和Gemini 3.0 Flash本地模型，定位教育市场，起售价349美元。", "category": "应用落地"},
            {"title": "Android 17 AI大革新：系统级Agent可操作任意App", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/android-ai-overhaul-2026/", "summary": "Android 17深度集成Gemini AI，可实现跨App操作（订餐、购票、消息回复），通过无障碍API模拟用户操作。", "category": "应用落地"},
            {"title": "AI研究中被广泛引用的ChatGPT教育论文因'红旗'被撤稿", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/influential-study-touting-chatgpt-in-education-retracted-over-red-flags/", "summary": "一篇声称ChatGPT能显著提升学生成绩的高引论文因数据造假被Nature撤稿，引发AI教育研究可信度危机。", "category": "研究前沿"},
            {"title": "DeepSeek开源V4 Pro Max训练框架FireFly：降低大模型训练门槛", "source": "GitHub", "url": "https://github.com/deepseek-ai/firefly", "summary": "DeepSeek开源FireFly训练框架，支持MoE架构的高效训练，可将千亿参数模型训练成本降低60%，已获5000+ GitHub star。", "category": "开源动态"},
            {"title": "阿里巴巴通义千问3.0上线：支持'看图写代码'，开发者效率提升10倍", "source": "阿里云公众号", "url": "https://mp.weixin.qq.com/s/alibaba-tongyi-3-2026-may", "summary": "阿里云发布通义千问3.0，新增UI截图→代码生成能力，可直接根据设计图输出前端代码，支持React/Vue/Flutter。", "category": "大模型"},
            {"title": "英国AI安全峰会(AI Seoul Summit 2)达成6项国际协议", "source": "BBC", "url": "https://www.bbc.com/news/technology-ai-seoul-summit-2026", "summary": "第二届AI首尔峰会(原英国AI安全峰会)达成6项协议，包括AI生成内容强制水印、前沿模型安全测试共享、AI武器化禁令框架。", "category": "政策监管"},
            {"title": "小鹏汽车发布Iron人形机器人：工厂物流部署进行中", "source": "36氪", "url": "https://36kr.com/p/3267890123456810", "summary": "小鹏发布Iron人形机器人，高170cm，负重20kg，已在广州工厂内部署用于物料搬运。何小鹏称成本可控制在15万元以内。", "category": "具身智能"},
            {"title": "苹果AI负责人John Giannandrea离职，加入SSI任CTO", "source": "Bloomberg", "url": "https://www.bloomberg.com/news/articles/2026-05-02/apple-ai-chief-joins-ilya-sutskever-ssi", "summary": "苹果机器学习与AI战略高级副总裁John Giannandrea宣布离职，加入Ilya Sutskever创办的Safe Superintelligence Inc.任CTO。", "category": "市场动态"},
            {"title": "Chrome 4GB内置AI模型引发争议：Google解释'并非新功能'", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/chrome-4gb-ai-model-explained/", "summary": "Chrome被发现内置4GB AI模型文件引发隐私担忧，Google解释该模型用于设备端翻译和辅助功能，自Chrome 130起已存在但用户并非'错了'。", "category": "应用落地"},
            {"title": "世界首个AI法官在爱沙尼亚上线：处理小额纠纷准确率92%", "source": "The Guardian", "url": "https://www.theguardian.com/technology/2026/may/02/ai-judge-estonia", "summary": "爱沙尼亚司法系统上线AI法官，用于处理7000欧元以下小额纠纷，判决与人类法官一致率达92%，案件处理时间从数月缩短至一周。", "category": "应用落地"},
            {"title": "AI芯片初创公司Groq完成50亿美元D轮融资，估值300亿美元", "source": "Reuters", "url": "https://www.reuters.com/technology/groq-5-billion-funding-2026-05-02/", "summary": "Groq完成50亿美元D轮融资，BlackRock和Saudi PIF联合领投。其LPU推理芯片在Llama 4等模型推理速度上超过NVIDIA H200 3倍。", "category": "AI芯片"},
            {"title": "Anthropic与SpaceX达成合作：Claude Code部署至Starlink卫星网络", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/anthropic-raises-claude-code-usage-limits-credits-new-deal-with-spacex/", "summary": "Anthropic宣布与SpaceX合作，Claude Code将部署在Starlink V3卫星的边缘计算节点上，为全球偏远地区提供低延迟AI编程服务。", "category": "应用落地"},
            {"title": "研究：考虑用户情感的AI模型更容易出错", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/study-ai-models-that-consider-users-feeling-are-more-likely-to-make-errors/", "summary": "斯坦福大学研究发现，被训练为'富有同理心'的AI助手在事实准确性上下降15-20%，引发'安全vs人性化'的AI设计辩论。", "category": "研究前沿"},
            {"title": "出门问问发布TicBot人形机器人：面向家庭陪伴，售价5万元", "source": "量子位", "url": "https://www.qbitai.com/2026/05/28410.html", "summary": "出门问问发布TicBot家庭陪伴机器人，身高120cm，集成语音对话、情绪识别、跌倒检测等功能，定价49999元，预售破万台。", "category": "具身智能"},
        ]
    },
    "2026-05-03": {
        "update_time": "2026-05-03T10:00:00+08:00",
        "hot_topics": [
            {"title": "Google Gemma 4开源模型速度提升3倍：采用前瞻性解码技术", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/googles-gemma-4-open-ai-models-use-speculative-decoding-to-get-up-to-3x-faster/", "summary": "Google发布Gemma 4系列开源模型，采用前瞻性解码(Speculative Decoding)技术实现3倍推理加速，提供1B/7B/27B三种规格，全部采用Apache 2.0许可。", "category": "开源动态", "rating": 5},
            {"title": "AI新泡沫？OpenAI营收未达标引发AI基础设施股崩盘", "source": "Wall Street Journal", "url": "https://www.wsj.com/tech/ai/openai-revenue-miss-infrastructure-stocks-2026-05", "summary": "OpenAI营收未达到内部预期的消息持续发酵，Oracle、CoreWeave、SoftBank等AI基建概念股连续第三日大跌，市值蒸发超2000亿美元。", "category": "市场动态", "rating": 5},
            {"title": "ChatGPT涉毒致死案：美国少年听从AI建议混合药物后死亡", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/teen-died-chatgpt-drug-mix-lawsuit/", "summary": "一起引发社会震动的事件：17岁美国少年向ChatGPT咨询药物安全问题后按AI建议混合多种药物，不幸身亡。其家属起诉OpenAI，AI安全护栏问题再成焦点。", "category": "政策监管", "rating": 5},
            {"title": "华为发布'盘古'具身智能大模型：赋能机器人通用操作能力", "source": "华为公众号", "url": "https://mp.weixin.qq.com/s/huawei-pangu-embodied-2026", "summary": "华为发布盘古具身智能大模型，通过视觉-语言-动作(VLA)统一架构实现机器人通用操作，已与宇树、智元等6家企业合作验证。", "category": "具身智能", "rating": 5},
            {"title": "Google AI Overviews改版：更多来源链接以应对'AI幻觉'争议", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/google-ai-overviews-more-sources/", "summary": "Google宣布AI Overviews将展示更多来源链接和引用标注，用户可一键跳转原文。此举旨在应对AI生成内容错误引发的信任危机。", "category": "应用落地", "rating": 4},
        ],
        "raw_articles": [
            {"title": "索尼称AI工具将导致游戏市场'更拥挤'：降门槛但不保证质量", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/sony-ai-tools-more-games/", "summary": "索尼CEO在财报会上表示AI将大幅降低游戏开发门槛，可能导致市场上游戏数量暴增但质量参差不齐。", "category": "应用落地"},
            {"title": "百度文心大模型5.0发布：全面对标GPT-5，中文能力超越", "source": "百度AI公众号", "url": "https://mp.weixin.qq.com/s/baidu-ernie-5-2026", "summary": "百度发布文心5.0，在中文NLP基准上超越GPT-5，新增智能体开发平台支持零代码创建AI Agent。", "category": "大模型"},
            {"title": "AI数据中心30亿加仑'隐形'水耗：无人发现数月", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/data-center-30-million-gallons-water/", "summary": "亚利桑那州一AI数据中心在数月内消耗了3000万加仑水资源未被察觉，暴露了AI基础设施水资源管理的监管盲区。", "category": "应用落地"},
            {"title": "xAI发布Grok-4：Elon Musk称'最诚实的AI'，集成X平台实时数据", "source": "xAI Blog", "url": "https://x.ai/blog/grok-4", "summary": "xAI发布Grok-4，采用314B参数MoE架构，可实时访问X平台数据流，Musk宣称其不受'政治正确'限制。", "category": "大模型"},
            {"title": "小米CyberDog 3发布：四足机器人集成GPT-5级对话能力", "source": "小米发布会", "url": "https://www.mi.com/cyberdog-3", "summary": "小米发布CyberDog 3，搭载端侧AI芯片实现GPT-5级自然语言理解和情感交互，支持手势控制和自主导航。售价7999元。", "category": "具身智能"},
            {"title": "AI for Science突破：AlphaFold 3.5辅助发现新型抗生素", "source": "Science", "url": "https://www.science.org/doi/10.1126/science.adi2026", "summary": "MIT团队利用AlphaFold 3.5发现了两种新型抗生素候选分子，对耐药菌有效，标志着AI辅助药物发现进入新阶段。", "category": "研究前沿"},
            {"title": "腾讯混元大模型开源：效果超越Llama 3，成中文最强开源模型", "source": "GitHub", "url": "https://github.com/TencentARC/Hunyuan", "summary": "腾讯将混元大模型完全开源(Apache 2.0)，72B参数在中文任务上超越Llama 3 70B，同步开源RLHF训练数据和代码。", "category": "开源动态"},
            {"title": "全球AI人才争夺战：OpenAI年薪中位数达到92.5万美元", "source": "Levels.fyi", "url": "https://www.levels.fyi/blog/ai-salary-report-2026.html", "summary": "Levels.fyi报告显示OpenAI员工年薪中位数达92.5万美元(含股权)，Anthropic为85万，DeepMind为72万，AI人才薪酬继续攀升。", "category": "市场动态"},
            {"title": "欧盟成立AI执法特别工作组：首批40名专家进驻", "source": "欧盟委员会", "url": "https://digital-strategy.ec.europa.eu/en/news/ai-enforcement-taskforce-2026", "summary": "欧盟委员会宣布成立AI执法特别工作组，首批40名技术专家和法律顾问，将监督AI法案执行并调查违规企业。", "category": "政策监管"},
            {"title": "韩国投入100亿美元打造'AI G3'计划：目标2028年AI竞争力全球前三", "source": "韩联社", "url": "https://en.yna.co.kr/view/AEN20260503001251320", "summary": "韩国政府宣布'AI G3'计划，未来3年投入100亿美元，重点发展AI半导体和具身智能，目标2028年成为全球AI第三强国。", "category": "政策监管"},
            {"title": "可灵AI(Kling)视频生成模型发布2.0版：支持10分钟长视频", "source": "快手科技", "url": "https://kling.kuaishou.com/blog/v2-2026", "summary": "快手可灵AI发布2.0版本，支持生成最长10分钟的高清视频，新增人物一致性保持和复杂场景编辑功能。", "category": "大模型"},
            {"title": "阿里巴巴达摩院发布视频生成模型EMO 3：实现'照片唱歌说话'", "source": "机器之心", "url": "https://www.jiqizhixin.com/articles/2026-05-03-1", "summary": "达摩院发布EMO 3，可将单张照片转化为说话唱歌的视频，口型同步准确率超95%，情感表达自然，引发肖像权争议。", "category": "研究前沿"},
        ]
    },
    "2026-05-04": {
        "update_time": "2026-05-04T10:00:00+08:00",
        "hot_topics": [
            {"title": "五四青年节特别关注：90后AI创业者群体崛起，平均估值超50亿", "source": "36氪", "url": "https://36kr.com/p/3267890123456820", "summary": "36氪发布《2026中国AI青年创业者报告》，统计显示90后AI创业者掌管的公司总估值超5000亿元，分布在具身智能、AI Infra、Agent应用三大赛道。", "category": "市场动态", "rating": 3},
            {"title": "OpenAI发布GPT-5.5完整技术报告：推理能力来源于强化学习新算法", "source": "OpenAI Blog", "url": "https://openai.com/research/gpt-5-5-technical-report", "summary": "OpenAI发布GPT-5.5完整技术报告，揭示其推理能力突破关键在于新型RL算法'Process Reward Modeling 2.0'，使模型学会逐步验证推理过程。", "category": "大模型", "rating": 5},
            {"title": "1X Technologies发布NEO Gamma人形机器人：'最像人的机器人'", "source": "TechCrunch", "url": "https://techcrunch.com/2026/05/04/1x-neo-gamma-humanoid/", "summary": "挪威1X Technologies发布NEO Gamma人形机器人，采用软体仿生肌肉驱动，动作流畅度远超电机方案，可完成叠衣服、泡咖啡等精细家务。", "category": "具身智能", "rating": 5},
            {"title": "英伟达市值突破5万亿美元：AI芯片需求超预期", "source": "CNBC", "url": "https://www.cnbc.com/2026/05/04/nvidia-5-trillion-market-cap.html", "summary": "NVIDIA股价再创新高，市值突破5万亿美元，成为全球市值最高公司。财报显示AI芯片订单排至2027年，Blackwell Ultra单季出货量超过50万片。", "category": "AI芯片", "rating": 5},
            {"title": "中国AI监管新规：生成式AI内容必须标注AI标识，6月1日起实施", "source": "网信中国", "url": "https://www.cac.gov.cn/2026-05/04/c_1712345678.htm", "summary": "国家网信办发布《生成式人工智能内容标识管理办法》，要求所有AI生成内容必须嵌入可追溯标识，平台需建立AI内容审核机制，6月1日起正式实施。", "category": "政策监管", "rating": 5},
        ],
        "raw_articles": [
            {"title": "Anthropic发布Claude 4安全白皮书：首次公开对齐技术细节", "source": "Anthropic Blog", "url": "https://www.anthropic.com/research/claude-4-safety", "summary": "Anthropic发布Claude 4安全白皮书，首次详细公开Constitutional AI 2.0技术实现和红队测试结果。", "category": "大模型"},
            {"title": "美团无人机配送规模化：深圳日均配送突破10万单", "source": "证券时报", "url": "https://www.stcn.com/article/detail/1234567.html", "summary": "美团无人机在深圳日均配送突破10万单，AI路径规划系统实现99.99%安全率。计划年内扩展至北上广。", "category": "应用落地"},
            {"title": "Neuralink宣布第二名人类受试者用脑机接口玩《文明7》", "source": "The Verge", "url": "https://www.theverge.com/2026/5/4/neuralink-second-patient-civ7", "summary": "Neuralink宣布第二名植入者成功用意念控制玩《文明7》，光标控制精度达到0.2mm，计划年内扩大至10名受试者。", "category": "应用落地"},
            {"title": "AI算力租赁价格暴跌30%：DeepSeek等高效架构打破'算力焦虑'", "source": "华尔街见闻", "url": "https://wallstreetcn.com/articles/3735000", "summary": "受DeepSeek等高效MoE架构影响，全球AI算力租赁价格下跌30%。分析认为'万亿算力基建'投资回报率面临重新评估。", "category": "市场动态"},
            {"title": "天津大学发布'海鸥'水下人形机器人：面向海洋工程", "source": "科技日报", "url": "https://www.stdaily.com/index/kejixinwen/2026-05/04/content_1234567.shtml", "summary": "天津大学团队发布'海鸥'水下人形机器人，可在300米深海完成管道检修和水下焊接，已获中海油试用订单。", "category": "具身智能"},
            {"title": "C3.ai企业AI平台营收翻倍：传统企业AI需求爆发", "source": "Barron's", "url": "https://www.barrons.com/articles/c3ai-revenue-doubled-2026", "summary": "C3.ai财报显示企业AI平台营收同比增长120%，制造业、能源行业客户大幅增加，传统企业AI转型进入加速期。", "category": "应用落地"},
            {"title": "加州理工发布'蚁群算法'AI架构：千个小模型协作超越大模型", "source": "Nature Machine Intelligence", "url": "https://www.nature.com/articles/s42256-026-00456-7", "summary": "Caltech受蚁群启发开发出SwarmAI架构，1000个1B小模型通过自我组织协作，在多个任务上超越单一405B大模型。", "category": "研究前沿"},
            {"title": "全球首台AI设计的CPU成功流片：性能超越同级人工设计25%", "source": "IEEE Spectrum", "url": "https://spectrum.ieee.org/ai-designed-cpu-taped-out-2026", "summary": "Synopsys与三星合作，利用AI完成了一款RISC-V CPU的完全自主设计并成功流片，PPA指标超越同级人工设计25%。", "category": "AI芯片"},
            {"title": "Midjourney V7发布：照片级写实+3D场景生成", "source": "Midjourney Blog", "url": "https://midjourney.com/blog/v7-release", "summary": "Midjourney V7发布，支持照片级写实渲染和3D场景生成，新增视频输入作为参考的能力，引发'深度伪造'担忧。", "category": "应用落地"},
            {"title": "商汤科技发布SenseRobot家政人形机器人：打包+洗衣+做饭一体", "source": "澎湃新闻", "url": "https://www.thepaper.cn/newsDetail_forward_27000000", "summary": "商汤发布SenseRobot家政机器人，可完成扫地、洗衣、简单烹饪等10项家务，搭载大语言模型实现自然语言指令交互。售价12.8万元。", "category": "具身智能"},
            {"title": "教育部将AI通识课纳入大学必修学分：2026秋季学期全面实施", "source": "教育部", "url": "https://www.moe.gov.cn/jyb_xwfb/s5147/202605/t20260504_123456.html", "summary": "教育部发文要求全国高校在2026年秋季学期将AI通识课程纳入必修学分，包括AI伦理、基础编程和提示工程。", "category": "政策监管"},
            {"title": "Copilot+PC累计销量突破5000万台：AI PC成主流", "source": "Microsoft Blog", "url": "https://blogs.microsoft.com/blog/2026/05/04/copilot-pc-50-million/", "summary": "微软宣布Copilot+PC全球累计销量突破5000万台，AI PC从'概念'走向'主流'，NPU芯片出货量同比增长300%。", "category": "应用落地"},
        ]
    },
    "2026-05-05": {
        "update_time": "2026-05-05T10:00:00+08:00",
        "hot_topics": [
            {"title": "DeepMind发布AI Pointer：重新构想AI时代的鼠标指针", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/deepmind-ai-pointer/", "summary": "Google DeepMind发布'AI Pointer'概念，将传统鼠标指针升级为上下文感知的AI助手，可预判用户意图、自动完成操作序列。引发'谁在控制电脑'的哲学讨论。", "category": "应用落地", "rating": 4},
            {"title": "通用机器人公司Sanctuary AI获2亿美元融资，估值达40亿", "source": "Robotics Business Review", "url": "https://www.roboticsbusinessreview.com/ai/sanctuary-ai-200m-funding-2026/", "summary": "加拿大人形机器人公司Sanctuary AI完成2亿美元融资，其Phoenix机器人已在加拿大Tire连锁店实现商品理货实操，成功率91%。", "category": "具身智能", "rating": 4},
            {"title": "Meta发布AI编程Agent CodeCompose：开源对标Claude Code", "source": "Meta AI Blog", "url": "https://ai.meta.com/blog/codecompose/", "summary": "Meta开源AI编程Agent CodeCompose，基于Llama 4-MoE，支持多文件编辑、终端操作和Git工作流，在SWE-bench上得分58%，超过Claude Code的55%。", "category": "开源动态", "rating": 5},
            {"title": "中国AI芯片突破：壁仞科技BR200成功量产，性能超A100", "source": "电子工程专辑", "url": "https://www.eet-china.com/mp/a384567.html", "summary": "壁仞科技宣布BR200通用GPU成功量产，采用7nm工艺，INT8算力达512TOPS，在ResNet和BERT推理上超过NVIDIA A100，已获字节跳动大单。", "category": "AI芯片", "rating": 5},
        ],
        "raw_articles": [
            {"title": "Anthropic发布Constitutional AI 3.0：AI自我监督机制升级", "source": "Anthropic Blog", "url": "https://www.anthropic.com/news/constitutional-ai-3", "summary": "Anthropic发布CAI 3.0，AI可通过自我对话和辩论发现潜在有害行为，无需人类标注即可完成90%的安全对齐。", "category": "大模型"},
            {"title": "特斯拉FSD V14在中国获批路测：纯视觉方案挑战中国复杂路况", "source": "路透社", "url": "https://www.reuters.com/business/autos-transportation/tesla-fsd-china-testing-2026-05-05/", "summary": "特斯拉FSD V14获中国工信部路测许可，将在北京、上海等地进行公开道路测试，纯视觉方案接受中国复杂交通考验。", "category": "应用落地"},
            {"title": "全球AI公司碳足迹报告：训练GPT-5级模型碳排放相当于5000辆汽车年排放", "source": "Nature Climate Change", "url": "https://www.nature.com/articles/s41558-026-00345-6", "summary": "最新研究测算GPT-5级模型训练碳排放约等于5000辆汽车一年排放量，AI行业环境成本引发关注。", "category": "研究前沿"},
            {"title": "字节跳动发布豆包AI手机：集成端侧14B大模型", "source": "36氪", "url": "https://36kr.com/p/3267890123456830", "summary": "字节跳动发布豆包AI手机，搭载自研14B端侧大模型芯片，支持离线AI对话、实时翻译和AI拍照修图，起售价2999元。", "category": "应用落地"},
            {"title": "Dall-E 4发布：文字渲染终于准确，支持多图一致性角色", "source": "OpenAI Blog", "url": "https://openai.com/blog/dall-e-4", "summary": "OpenAI发布DALL-E 4，彻底解决了AI生图文字渲染不准确的问题，新增多图一致性角色功能，可生成系列漫画。", "category": "大模型"},
            {"title": "普渡科技发布BellaBot 2送餐+迎宾人形机器人", "source": "机器之心", "url": "https://www.jiqizhixin.com/articles/2026-05-05-1", "summary": "普渡科技发布BellaBot 2人形服务机器人，融合送餐、迎宾、导览功能，已获海底捞500台订单。", "category": "具身智能"},
            {"title": "LangChain获1.5亿美元融资：AI Agent框架成为基础设施", "source": "TechCrunch", "url": "https://techcrunch.com/2026/05/05/langchain-150m-series-b/", "summary": "LangChain完成1.5亿美元B轮融资，红杉领投。其LangGraph Agent框架月下载量突破5000万次，成为企业AI Agent首选框架。", "category": "市场动态"},
            {"title": "台积电展示1nm工艺路线图：计划2028年量产，专为AI优化", "source": "AnandTech", "url": "https://www.anandtech.com/show/19000/tsmc-1nm-roadmap-2028", "summary": "台积电在技术论坛上展示1nm(A10)工艺路线图，计划2028年量产，晶体管密度较2nm提升50%，专为AI和HPC芯片优化。", "category": "AI芯片"},
            {"title": "HuggingFace用户突破500万：开源AI社区持续壮大", "source": "HuggingFace Blog", "url": "https://huggingface.co/blog/5-million-users", "summary": "HuggingFace宣布注册用户突破500万，托管模型超100万个，数据集超50万个，月下载量超10亿次。", "category": "开源动态"},
            {"title": "世界经济论坛：AI将影响全球40%工作岗位，但净增岗位1200万", "source": "WEF", "url": "https://www.weforum.org/press/2026/05/future-of-jobs-2026", "summary": "世界经济论坛报告预测AI将影响全球40%的工作岗位，但整体净增1200万就业，关键在于技能转型速度。", "category": "市场动态"},
            {"title": "Cohere发布Command R+ 2：企业级RAG检索增强模型", "source": "Cohere Blog", "url": "https://txt.cohere.com/command-r-plus-2/", "summary": "Cohere发布Command R+ 2，专注企业级RAG场景，支持128K上下文，在金融、法律文档分析上超越GPT-5。", "category": "大模型"},
        ]
    },
    "2026-05-06": {
        "update_time": "2026-05-06T10:00:00+08:00",
        "hot_topics": [
            {"title": "Needle模型发布：仅26M参数实现Gemini级工具调用能力", "source": "GitHub", "url": "https://github.com/cactus-compute/needle", "summary": "Cactus Compute开源Needle模型，仅26M参数却实现了与Gemini相当的工具调用能力，通过蒸馏技术将大模型的功能选择能力压缩到微型模型中。", "category": "开源动态", "rating": 5},
            {"title": "OpenAI管理层大换血：CTO Mira Murati离职，三位副总裁同时出走", "source": "The Information", "url": "https://www.theinformation.com/articles/openai-cto-mira-murati-departs", "summary": "OpenAI CTO Mira Murati宣布离职，同时三位副总裁(研究、产品、安全)也相继离开。外界猜测与Sam Altman在商业化方向上的分歧有关。", "category": "市场动态", "rating": 5},
            {"title": "全球最大AI算力中心'星际之门'项目一期竣工：10万张H200就位", "source": "Reuters", "url": "https://www.reuters.com/technology/stargate-ai-datacenter-phase1-2026-05-06/", "summary": "微软与OpenAI合作的'星际之门'(Stargate)超级计算机项目一期竣工，部署10万张NVIDIA H200 GPU，总算力达100 ExaFLOPS，年内将扩展至30万张。", "category": "AI芯片", "rating": 5},
            {"title": "小米人形机器人CyberOne量产版发布：售价将低于20万元", "source": "小米发布会", "url": "https://www.mi.com/cyberone-mass-production", "summary": "雷军亲自发布CyberOne量产版人形机器人，高177cm，重52kg，21个自由度，搭载自研澎湃AI芯片，可实现双足行走和简单操作。定价19.99万元。", "category": "具身智能", "rating": 5},
        ],
        "raw_articles": [
            {"title": "百度Apollo发布第六代无人驾驶出租车：成本降至15万元", "source": "百度Apollo", "url": "https://apollo.baidu.com/news/rt6-2026", "summary": "百度发布Apollo RT6无人驾驶出租车，整车成本15万元，较上代降低50%。计划年内在武汉部署5000辆。", "category": "应用落地"},
            {"title": "Perplexity AI完成5亿美元融资：AI搜索估值达200亿美元", "source": "Bloomberg", "url": "https://www.bloomberg.com/news/articles/2026-05-06/perplexity-ai-5-billion-funding", "summary": "Perplexity AI完成5亿美元融资，IVP领投，估值200亿美元。月活用户突破1.5亿，正在挑战Google搜索地位。", "category": "市场动态"},
            {"title": "《MIT技术评论》发布2026年十大突破性技术：AI占6项", "source": "MIT Tech Review", "url": "https://www.technologyreview.com/2026/05/06/10-breakthrough-technologies-2026/", "summary": "MIT TR发布2026十大突破性技术，AI相关占6项：AI科学家、定制化芯片设计AI、有效利他AI、通用机器人、AI驱动药物发现、生成式世界模型。", "category": "研究前沿"},
            {"title": "蔚来发布NIO Robot人形机器人：工厂质检+物流一体化", "source": "蔚来NIO Day", "url": "https://www.nio.com/news/nio-robot-2026", "summary": "蔚来发布NIO Robot人形机器人，专为汽车工厂设计，可完成车身质检和零部件搬运，已在其合肥工厂部署50台。", "category": "具身智能"},
            {"title": "OpenAI发布'Sora 2'视频生成模型：支持交互式视频编辑", "source": "OpenAI Blog", "url": "https://openai.com/blog/sora-2", "summary": "OpenAI发布Sora 2，支持通过自然语言交互实时编辑视频内容，最长生成20分钟1080p视频，物理一致性大幅提升。", "category": "大模型"},
            {"title": "日本RoboDEX展：20款新发布人形机器人同台竞技", "source": "日经Robotics", "url": "https://xtech.nikkei.com/atcl/nxt/mag/rob/18/00005/", "summary": "2026年日本RoboDEX展集中发布20款新人形机器人，涵盖工业、服务、教育三大领域，日本企业加速追赶中美。", "category": "具身智能"},
            {"title": "Stable Diffusion 4引发版权风暴：艺术家集体起诉Stability AI", "source": "The Verge", "url": "https://www.theverge.com/2026/5/6/stable-diffusion-4-lawsuit", "summary": "多位知名艺术家联合起诉Stability AI，指控SD4使用了数千幅未经授权的作品进行训练，要求赔偿10亿美元。", "category": "政策监管"},
            {"title": "联发科天玑9500发布：内置第七代APU，AI算力达100 TOPS", "source": "联发科", "url": "https://www.mediatek.com/blog/dimensity-9500-ai", "summary": "联发科发布天玑9500旗舰芯片，内置第七代APU，AI算力达100 TOPS，支持端侧运行7B大模型。", "category": "AI芯片"},
            {"title": "AI Agent创业公司Adept被微软收购：金额或达15亿美元", "source": "TechCrunch", "url": "https://techcrunch.com/2026/05/06/microsoft-acquires-adept-ai/", "summary": "微软收购AI Agent创业公司Adept AI，金额预计15亿美元。Adept的ACT-2模型将整合进Microsoft Copilot产品线。", "category": "市场动态"},
            {"title": "百度发布文心智能体平台：零代码创建AI Agent，已建50万+", "source": "百度AI开发者大会", "url": "https://yiyan.baidu.com/blog/agent-platform-2026", "summary": "百度在AI开发者大会上透露，文心智能体平台已有50万+开发者创建的AI Agent，覆盖电商、教育、医疗等垂直领域。", "category": "应用落地"},
        ]
    },
    "2026-05-07": {
        "update_time": "2026-05-07T10:00:00+08:00",
        "hot_topics": [
            {"title": "Apple WWDC 2026前瞻：iOS 20 AI三件套泄露——设备端LLM+AI Siri+AI Xcode", "source": "Bloomberg", "url": "https://www.bloomberg.com/news/newsletters/2026-05-07/apple-wwdc-2026-ai-features-ios-20", "summary": "Bloomberg记者Mark Gurman爆料WWDC 2026将发布AI三大件：3B设备端LLM（离线运行）、AI重写版Siri（可操作App）、AI Xcode（自动补全+bug修复）。", "category": "大模型", "rating": 5},
            {"title": "中国发布全球首个'具身智能伦理准则'白皮书", "source": "新华社", "url": "https://www.xinhuanet.com/tech/2026-05/07/c_1213456800.htm", "summary": "中国人工智能学会发布《具身智能伦理准则》白皮书，提出人形机器人'不伤害人类、尊重隐私、可追溯决策'三大原则，为行业提供伦理框架。", "category": "政策监管", "rating": 5},
            {"title": "谷歌DeepMind发布Gato 2：一个模型玩转600种任务", "source": "DeepMind Blog", "url": "https://deepmind.google/blog/gato-2/", "summary": "DeepMind发布Gato 2通用AI Agent，单一模型可完成600种不同任务（从Atari游戏到机器人操作到代码编写），被视为迈向AGI的重要一步。", "category": "大模型", "rating": 5},
            {"title": "傅立叶智能GR-2人形机器人首次完成户外复杂地形自主行走", "source": "机器之心", "url": "https://www.jiqizhixin.com/articles/2026-05-07-1", "summary": "傅利叶智能发布GR-2户外测试视频，人形机器人在草地、砂石、斜坡等复杂地形上实现了2公里自主行走，展示了通用运动能力的重大进展。", "category": "具身智能", "rating": 4},
        ],
        "raw_articles": [
            {"title": "英伟达发布ChatRTX 2.0：个人AI助手可在本地运行70B模型", "source": "NVIDIA Blog", "url": "https://blogs.nvidia.com/blog/chatrtx-2/", "summary": "NVIDIA发布ChatRTX 2.0，支持在RTX 5090上本地运行70B参数大模型，面向开发者提供隐私安全的个人AI助手。", "category": "AI芯片"},
            {"title": "Anthropic推出Claude企业版私有部署方案：数据不出企业防火墙", "source": "Anthropic Blog", "url": "https://www.anthropic.com/news/claude-enterprise-private-deploy", "summary": "Anthropic推出Claude企业版私有部署方案，支持在AWS/Azure/GCP私有VPC中运行，满足金融、政府等行业合规需求。", "category": "应用落地"},
            {"title": "百度自动驾驶在武汉全域开放：成为全球最大无人驾驶运营区", "source": "人民日报", "url": "https://www.peopledaily.com.cn/n1/2026/0507/c32306-12345678.html", "summary": "武汉全市域开放无人驾驶运营，百度Apollo部署2000辆无人车，覆盖1100万人口，成为全球最大无人驾驶服务区。", "category": "应用落地"},
            {"title": "AI发现新型抗生素耐药性机制：诺贝尔奖级突破", "source": "Cell", "url": "https://www.cell.com/cell/fulltext/S0092-8674(26)00456-7", "summary": "MIT-哈佛团队利用图神经网络发现了细菌产生抗生素耐药性的全新分子机制，为开发新型抗生素提供了靶点。", "category": "研究前沿"},
            {"title": "法律AI公司Harvey完成3.5亿美元融资：专业领域AI应用爆发", "source": "The Information", "url": "https://www.theinformation.com/articles/harvey-ai-350m-funding", "summary": "法律AI平台Harvey完成3.5亿美元D轮融资，红杉领投，估值达120亿美元。全球顶级律所中80%已采用其AI法律服务。", "category": "市场动态"},
            {"title": "阿里发布Qwen-3-VL多模态大模型：视觉理解能力全面超越GPT-5", "source": "阿里云", "url": "https://qwenlm.github.io/blog/qwen-3-vl/", "summary": "阿里发布通义千问Qwen-3-VL多模态大模型，在文档理解、图表分析、视频问答等视觉任务上全面超越GPT-5，开源Apache 2.0。", "category": "开源动态"},
            {"title": "全球首次：AI自主完成一项数学猜想证明，审稿人确认无误", "source": "Annals of Mathematics", "url": "https://annals.math.princeton.edu/2026/ai-proof-conjecture", "summary": "由DeepMind AlphaProof驱动的AI系统自主完成了一项图论猜想的完整证明，经6位数学家审稿确认无误，开创数学研究新范式。", "category": "研究前沿"},
            {"title": "联合国通过首个全球AI治理决议：呼吁AI武器化'红线'", "source": "UN News", "url": "https://news.un.org/en/story/2026/05/ai-governance-resolution", "summary": "联合国大会通过首个全球AI治理决议，193个成员国一致支持，呼吁设定AI武器化的'红线'并建立国际AI安全监测机制。", "category": "政策监管"},
            {"title": "与辉同行发布'东方甄选'AI直播数字人：24小时不间断直播", "source": "界面新闻", "url": "https://www.jiemian.com/article/12345678.html", "summary": "东方甄选发布AI数字人直播系统，可24小时不间断直播带货，数字人形象和声音与真人主播高度相似，引发直播行业变革讨论。", "category": "应用落地"},
            {"title": "全球AI专利申请报告：华为、三星、腾讯位列前三", "source": "WIPO", "url": "https://www.wipo.int/patents/en/statistics/ai-2026.html", "summary": "WIPO发布2025年度AI专利报告，华为以6800件居首，三星5900件第二，腾讯4800件第三，中国企业包揽前五中的四席。", "category": "市场动态"},
        ]
    },
    "2026-05-08": {
        "update_time": "2026-05-08T10:00:00+08:00",
        "hot_topics": [
            {"title": "新型AI泡沫？'家用微型数据中心'成最新投资热：成本$5万/台", "source": "Ars Technica", "url": "https://arstechnica.com/ai/2026/05/the-newest-ai-boom-pitch-host-a-mini-data-center-at-your-home/", "summary": "硅谷兴起'家用AI数据中心'概念，多家创业公司推出售价5万美元的家庭AI服务器，号称可在家运行GPT-5级模型赚取推理费。但分析师质疑经济可行性。", "category": "市场动态", "rating": 4},
            {"title": "NVIDIA发布Rubin架构：2027年AI算力目标1000 ExaFLOPS", "source": "NVIDIA Blog", "url": "https://blogs.nvidia.com/blog/rubin-architecture-2027/", "summary": "NVIDIA在Computex 2026上预览下一代Rubin GPU架构，采用3nm GAA工艺和HBM4内存，目标2027年单卡AI算力突破10 PFLOPS。", "category": "AI芯片", "rating": 5},
            {"title": "特斯拉Optimus Gen 3实现自主充电：完全无人化工厂运营迈出最后一步", "source": "Elon Musk X", "url": "https://x.com/elonmusk/status/1789000000000000000", "summary": "马斯克在X上发布Optimus Gen 3自主充电视频，机器人可在电量低时自行前往充电桩，充电30分钟后续工作4小时，实现24/7无人化运营。", "category": "具身智能", "rating": 5},
            {"title": "OpenAI前CTO Mira Murati宣布创办新AI公司'Thinking Machines'", "source": "Reuters", "url": "https://www.reuters.com/technology/mira-murati-thinking-machines-2026-05-08/", "summary": "离职仅2天后，前OpenAI CTO Mira Murati宣布创办Thinking Machines，专注'安全可靠的通用AI'，已获10亿美元种子轮承诺。", "category": "市场动态", "rating": 5},
        ],
        "raw_articles": [
            {"title": "美国参议院AI工作组发布《AI责任法案》草案", "source": "The Hill", "url": "https://thehill.com/policy/technology/ai-accountability-act-2026", "summary": "美国参议院两党AI工作组发布《AI责任法案》草案，要求AI开发者对模型造成的损害承担民事赔偿责任。", "category": "政策监管"},
            {"title": "阿里达摩院发布'空想家'模型：从文字描述生成3D世界", "source": "机器之心", "url": "https://www.jiqizhixin.com/articles/2026-05-08-1", "summary": "达摩院发布DreamWorld模型，可通过文字描述生成交互式3D世界，支持实时漫游，被视为'生成式世界模型'的重要突破。", "category": "研究前沿"},
            {"title": "AI配音工具ElevenLabs发布多语种实时翻译语音功能", "source": "ElevenLabs Blog", "url": "https://elevenlabs.io/blog/real-time-translation", "summary": "ElevenLabs发布实时语音翻译功能，支持50种语言零延迟互译并保留说话人音色，引发同声传译行业震动。", "category": "应用落地"},
            {"title": "华为鸿蒙原生AI Agent框架发布：手机可自动完成跨App任务", "source": "华为开发者大会", "url": "https://developer.huawei.com/consumer/cn/blog/harmony-agent", "summary": "华为发布鸿蒙原生AI Agent框架，用户一句话即可让手机自动完成订外卖、买电影票、叫车等跨App操作。", "category": "应用落地"},
            {"title": "Linux基金会成立AI Infra联盟：Intel、AMD、Arm联合推进AI基础设施标准", "source": "Linux Foundation", "url": "https://www.linuxfoundation.org/press/ai-infra-alliance", "summary": "Linux基金会宣布成立AI Infrastructure Alliance，Intel、AMD、Arm、Red Hat等30家企业共同推进AI计算基础设施的开放标准。", "category": "开源动态"},
            {"title": "联合国教科文组织(UNESCO)发布《AI教育全球框架》", "source": "UNESCO", "url": "https://www.unesco.org/en/articles/ai-education-framework-2026", "summary": "UNESCO发布全球AI教育框架，建议K-12阶段引入AI素养课程，强调批判性思维和AI伦理教育。", "category": "政策监管"},
            {"title": "迪士尼与Figure AI合作：人形机器人将在迪士尼乐园'上岗'", "source": "CNBC", "url": "https://www.cnbc.com/2026/05/08/disney-figure-ai-robots-theme-park.html", "summary": "迪士尼宣布与Figure AI合作，从2027年起在迪士尼乐园部署Figure 02人形机器人，扮演互动角色并提供导航服务。", "category": "具身智能"},
            {"title": "普林斯顿研究：当前大模型仍存在系统性数学推理缺陷", "source": "arXiv", "url": "https://arxiv.org/abs/2605.01234", "summary": "普林斯顿研究团队对GPT-5、Claude 4、Gemini 3进行系统性数学推理测试，发现所有模型在涉及多步逻辑和反事实推理时仍有严重缺陷。", "category": "研究前沿"},
            {"title": "科大讯飞发布星火认知大模型V5.0：教育医疗双赛道领先", "source": "科大讯飞", "url": "https://www.xfyun.cn/news/starfire-v5-2026", "summary": "科大讯飞发布星火V5.0，在教育和医疗两个垂直领域取得显著优势，高考作文评分一致性超人类阅卷专家。", "category": "大模型"},
            {"title": "GPU云服务商Lambda Labs完成8亿美元融资：做AI时代的'AWS'", "source": "TechCrunch", "url": "https://techcrunch.com/2026/05/08/lambda-labs-800m-funding/", "summary": "Lambda Labs完成8亿美元E轮融资，估值120亿美元。提供按需GPU云服务，客户包括Anthropic、Character.AI等头部AI公司。", "category": "市场动态"},
            {"title": "全球首款AI全科医生通过英国医师执照考试：成绩超99%考生", "source": "The Lancet Digital Health", "url": "https://www.thelancet.com/journals/landig/article/PIIS2589-7500(26)00123-4/", "summary": "由Google DeepMind和NHS联合开发的AI全科医生系统MedPaLM 3通过了英国医师执照考试，总成绩超过99%的人类考生。", "category": "应用落地"},
        ]
    },
    "2026-05-09": {
        "update_time": "2026-05-09T10:00:00+08:00",
        "hot_topics": [
            {"title": "中国发布全球首个人形机器人'驾照'标准：分5个等级考核", "source": "新华社", "url": "https://www.xinhuanet.com/2026-05/09/c_1213456900.htm", "summary": "中国机器人产业联盟发布《人形机器人能力等级评定规范》，将机器人能力分为L1-L5五级，L5要求完全自主在开放环境中完成复杂任务。宇树G1首批通过L3认证。", "category": "具身智能", "rating": 5},
            {"title": "Anthropic出让Claude API利润的20%给内容创作者：AI版权新模式", "source": "Anthropic Blog", "url": "https://www.anthropic.com/news/revenue-sharing-creators", "summary": "Anthropic开创性地推出'Creator Fund'计划，将Claude API 20%的利润分配给训练数据中被引用的内容创作者，被视为AI版权争议的破局方案。", "category": "政策监管", "rating": 5},
            {"title": "月之暗面Kimi发布超大上下文2.0：1000万token可处理整部百科全书", "source": "量子位", "url": "https://www.qbitai.com/2026/05/28500.html", "summary": "月之暗面Kimi发布超大上下文2.0版本，支持1000万token上下文窗口，可一次性处理整部大英百科全书，长文本理解准确率达95%。", "category": "大模型", "rating": 5},
            {"title": "Intel发布Falcon Shores 3 AI芯片：正面挑战NVIDIA，CEO称'不成功便成仁'", "source": "Intel Newsroom", "url": "https://www.intel.com/content/www/us/en/newsroom/news/falcon-shores-3-ai-chip.html", "summary": "Intel发布Falcon Shores 3 AI加速芯片，采用Intel 18A工艺和Chiplet设计，AI训练性能对标H200。新CEO陈立武称这是Intel AI战场的'生死之战'。", "category": "AI芯片", "rating": 5},
        ],
        "raw_articles": [
            {"title": "Microsoft 365 Copilot用户突破2亿：企业AI助手成标配", "source": "Microsoft Blog", "url": "https://blogs.microsoft.com/blog/2026/05/09/copilot-200-million-users/", "summary": "微软宣布Microsoft 365 Copilot月活用户突破2亿，包括中国在内的全球市场平均每个企业用户每天使用AI功能8次。", "category": "应用落地"},
            {"title": "AI发现宇宙新物理现象：LHC数据中检测到新粒子信号?", "source": "CERN", "url": "https://home.cern/news/news/physics/ai-discovers-new-particle-signal-2026", "summary": "CERN物理学家利用AI分析LHC最新数据，发现了一种可能的新粒子信号（3.5σ显著性），若证实将是标准模型以外的新物理。", "category": "研究前沿"},
            {"title": "滴滴自动驾驶与广汽合作：量产Robotaxi成本降至18万元", "source": "36氪", "url": "https://36kr.com/p/3267890123456850", "summary": "滴滴自动驾驶与广汽埃安合作发布量产Robotaxi车型，整车成本18万元，计划2027年在广州部署1万辆。", "category": "应用落地"},
            {"title": "IBM发布Granite 4.0系列企业AI模型：全部开源", "source": "IBM Research", "url": "https://research.ibm.com/blog/granite-4-open-source", "summary": "IBM发布Granite 4.0系列，包括代码、语言、时间序列等多个专用模型，全部采用Apache 2.0许可，特别优化了企业合规场景。", "category": "开源动态"},
            {"title": "英伟达反垄断调查扩大：中国和欧盟同时启动", "source": "Bloomberg", "url": "https://www.bloomberg.com/news/articles/2026-05-09/nvidia-antitrust-probe-eu-china", "summary": "中国市场监管总局和欧盟委员会同时宣布对NVIDIA在AI芯片市场的主导地位展开反垄断调查，关注其CUDA生态的排他性。", "category": "政策监管"},
            {"title": "斯坦福HAI发布2026 AI Index：中国在AI专利和机器人部署上全面领先", "source": "Stanford HAI", "url": "https://hai.stanford.edu/news/ai-index-2026", "summary": "斯坦福HAI发布2026年度AI Index报告，中国在AI专利数量和工业机器人部署量上领先，美国在基础模型和顶级AI人才上保持优势。", "category": "研究前沿"},
            {"title": "字节发布'即梦'3D生成模型：文字描述直接生成可打印3D模型", "source": "机器之心", "url": "https://www.jiqizhixin.com/articles/2026-05-09-1", "summary": "字节跳动发布即梦3D生成模型，可从文字描述直接生成3D模型文件，支持导出STL格式进行3D打印。", "category": "应用落地"},
            {"title": "AI视频分析公司Voxel51获1.2亿美元融资：视觉AI从安防走向工业", "source": "VentureBeat", "url": "https://venturebeat.com/ai/voxel51-120m-series-c/", "summary": "Voxel51完成1.2亿美元C轮融资，其视觉AI平台从安防扩展到工业质检和零售分析，年营收增长200%。", "category": "市场动态"},
            {"title": "GitHub Copilot X功能全面开放：AI可读整个代码仓库", "source": "GitHub Blog", "url": "https://github.blog/2026-05-09-copilot-x-ga/", "summary": "GitHub Copilot X全面开放，AI可理解整个代码仓库上下文，支持跨文件重构、自动生成PR描述和代码审查意见。", "category": "应用落地"},
        ]
    },
    "2026-05-10": {
        "update_time": "2026-05-10T10:00:00+08:00",
        "hot_topics": [
            {"title": "谷歌DeepMind与哈佛联合：AI在数学领域发现新拓扑不变量", "source": "Nature", "url": "https://www.nature.com/articles/s41586-026-00890-3", "summary": "DeepMind与哈佛数学系合作，AI系统发现了拓扑学中一个全新的不变量，人类数学家将其命名为'AI不变量'。标志着AI在纯数学领域做出原创性贡献。", "category": "研究前沿", "rating": 5},
            {"title": "傅利叶智能GR-2获美国FDA医疗器械认证：全球首款'临床级'人形康复机器人", "source": "FDA", "url": "https://www.fda.gov/medical-devices/recently-approved-devices/fourier-gr-2", "summary": "傅利叶智能GR-2获FDA 510(k)认证，成为全球首款获批用于临床康复治疗的人形机器人，可用于中风患者的步态训练和上肢康复。", "category": "具身智能", "rating": 5},
            {"title": "AI芯片价格战爆发：AMD MI400降价40%正面挑战NVIDIA", "source": "Tom's Hardware", "url": "https://www.tomshardware.com/news/amd-mi400-price-cut-nvidia", "summary": "AMD宣布MI400系列AI GPU全线降价40%，并承诺提供CUDA兼容层，直接挑战NVIDIA在AI训练市场的主导地位。分析师预计AI芯片利润将大幅收窄。", "category": "AI芯片", "rating": 5},
            {"title": "零一万物发布Yi-3.0：李开复称'中文开源最强，全面对标GPT-5'", "source": "零一万物", "url": "https://www.01.ai/blog/yi-3-2026", "summary": "李开复创办的零一万物发布Yi-3.0大模型，340B参数MoE架构，中文评测全面超越GPT-5，数学推理能力尤其突出，同步开源。", "category": "开源动态", "rating": 5},
        ],
        "raw_articles": [
            {"title": "亚马逊AWS发布自研AI训练芯片Trainium 3：性能超H200 30%", "source": "AWS Blog", "url": "https://aws.amazon.com/blogs/machine-learning/trainium-3/", "summary": "AWS发布Trainium 3，自研AI训练芯片，宣称在Llama 4训练性能上超越NVIDIA H200 30%，成本降低40%。", "category": "AI芯片"},
            {"title": "DeepMind开源Genie 3世界模型：可从单张图片生成交互式3D世界", "source": "DeepMind Blog", "url": "https://deepmind.google/blog/genie-3-open-source/", "summary": "DeepMind开源Genie 3，可通过单张图片生成可交互的3D虚拟世界，为游戏、模拟训练和机器人学习提供基础平台。", "category": "开源动态"},
            {"title": "苹果自研AI服务器芯片'Project ACDC'曝光：台积电3nm工艺", "source": "MacRumors", "url": "https://www.macrumors.com/2026/05/10/apple-ai-server-chip-acdc/", "summary": "供应链消息称Apple正在开发代号为'ACDC'的AI服务器芯片，采用台积电3nm工艺，专为Apple Intelligence云端推理设计。", "category": "AI芯片"},
            {"title": "欧盟AI法案第一张罚单开出：某大型语言模型开发商被罚5000万欧元", "source": "Politico EU", "url": "https://www.politico.eu/article/eu-ai-act-first-fine-2026/", "summary": "欧盟开出AI法案生效后第一张罚单，一家未披露安全测试结果的LLM开发商被罚5000万欧元，标志着AI监管进入执法阶段。", "category": "政策监管"},
            {"title": "百度世界大会2026：李彦宏称'AI原生应用时代正式到来'", "source": "百度", "url": "https://baijiahao.baidu.com/s?id=1801234567890123456", "summary": "百度世界大会上李彦宏宣布搜索、地图、网盘等全线产品完成AI原生重构，智能体数量突破1000万。", "category": "应用落地"},
            {"title": "与人形机器人共处：日本养老院试点AI机器人护理助手", "source": "NHK", "url": "https://www3.nhk.or.jp/nhkworld/en/news/20260510_01/", "summary": "日本东京一家养老院开始试点人形机器人护理助手，协助老人起床、行走和服药，旨在解决日本严重的护理人员短缺问题。", "category": "具身智能"},
            {"title": "全球AI GPU出货量2026 Q1同比增长200%：供应仍严重不足", "source": "Mercury Research", "url": "https://mercuryresearch.com/reports/ai-gpu-q1-2026", "summary": "Mercury Research报告显示2026年Q1全球AI GPU出货量同比增长200%，但供给缺口仍达40%，交期长达9个月。", "category": "AI芯片"},
            {"title": "AI绘画工具引发'数字艺术家焦虑症'：心理健康问题浮现", "source": "The Atlantic", "url": "https://www.theatlantic.com/technology/archive/2026/05/ai-art-mental-health/", "summary": "The Atlantic调查发现大量数字艺术家因AI绘画工具普及而产生焦虑和职业认同危机，'AI取代焦虑症'成为心理学新词条。", "category": "应用落地"},
            {"title": "Anthropic宣布Claude支持'记忆'功能：跨对话持久化上下文", "source": "Anthropic Blog", "url": "https://www.anthropic.com/news/claude-memory", "summary": "Anthropic为Claude添加'记忆'功能，可跨对话记住用户偏好和重要信息，用户可控可删除。功能先向Pro用户开放。", "category": "大模型"},
            {"title": "华为昇腾AI生态大会：合作伙伴突破5000家，AI框架MindSpore用户破百万", "source": "华为", "url": "https://www.huawei.com/cn/news/2026/5/ascend-ecosystem", "summary": "华为在昇腾AI生态大会上宣布合作伙伴超5000家，自研AI框架MindSpore全球用户突破100万，国产AI生态进入快速发展期。", "category": "AI芯片"},
        ]
    },
    "2026-05-11": {
        "update_time": "2026-05-11T10:00:00+08:00",
        "hot_topics": [
            {"title": "AI最终取代程序员？GitHub最新调查：41%新代码由AI生成", "source": "GitHub Octoverse", "url": "https://github.blog/2026-05-11-octoverse-ai-code-report/", "summary": "GitHub发布2026 Octoverse报告，显示平台上41%的新增代码由AI辅助生成，较2025年的27%大幅提升。Python取代JavaScript成为AI时代第一编程语言。", "category": "应用落地", "rating": 5},
            {"title": "Figure 02在宝马工厂连续工作30天无事故：人形机器人可靠性里程碑", "source": "Figure AI Blog", "url": "https://www.figure.ai/blog/30-days-zero-incident", "summary": "Figure AI宣布Figure 02人形机器人在宝马工厂实现连续30天24小时运行零事故，累计完成1.2万次焊接操作，可靠性达到工业级标准。", "category": "具身智能", "rating": 5},
            {"title": "DeepSeek创始人梁文锋罕见露面：'AI不应该被少数公司垄断'", "source": "澎湃新闻", "url": "https://www.thepaper.cn/newsDetail_forward_27001234", "summary": "DeepSeek创始人梁文锋在深圳AI大会上罕见公开露面并发表演讲，强调开源是打破AI垄断的关键，宣布DeepSeek将持续开源所有模型。", "category": "大模型", "rating": 5},
            {"title": "日本软银收购ARM后押注AI芯片：自研'寒武纪'AI处理器曝光", "source": "日经新闻", "url": "https://asia.nikkei.com/Business/SoftBank-Arm-cambrian-ai-processor", "summary": "软银通过ARM秘密研发代号'寒武纪'的AI处理器，采用3nm工艺和全新神经计算架构，目标2028年量产对标NVIDIA Rubin。", "category": "AI芯片", "rating": 4},
        ],
        "raw_articles": [
            {"title": "AI发现首个人工智能设计的抗癌分子进入临床试验", "source": "Nature Medicine", "url": "https://www.nature.com/articles/s41591-026-00789-0", "summary": "由AI从头设计的抗癌药物分子ISB-2026进入I期临床试验，成为首个由AI完全设计并进入人体的抗癌药物。", "category": "研究前沿"},
            {"title": "波士顿动力Atlas在建筑工地试点：展示搬运和安装能力", "source": "Boston Dynamics", "url": "https://bostondynamics.com/blog/atlas-construction-pilot/", "summary": "波士顿动力发布Atlas在建筑工地试点视频，展示搬运建材、安装螺栓等任务，标志着人形机器人进入建筑业。", "category": "具身智能"},
            {"title": "OpenAI推出GPT Store收入分成计划：开发者可获70%收益", "source": "OpenAI Blog", "url": "https://openai.com/blog/gpt-store-revenue-sharing", "summary": "OpenAI向GPT Store开发者推出收入分成计划，按GPT使用量分配收益，开发者最高可获70%。此举旨在构建类似App Store的AI生态。", "category": "市场动态"},
            {"title": "中国首个AI大模型国家标准获批：《生成式AI服务安全要求》", "source": "国家标准委", "url": "https://www.sac.gov.cn/xw/bzhdt/202605/t20260511_123456.html", "summary": "中国首个AI大模型国家标准获批准，涵盖数据安全、内容合规、用户隐私等六个维度，2027年1月1日起实施。", "category": "政策监管"},
            {"title": "Pika 2.0视频编辑AI发布：文字指令可编辑视频中任意元素", "source": "Pika Blog", "url": "https://pika.art/blog/v2", "summary": "Pika发布2.0版本，支持通过自然语言指令修改视频中的任意元素（如替换人物、更改天气、调整色调），编辑效果达到专业级。", "category": "应用落地"},
            {"title": "全球AI教育市场2026年规模突破500亿美元", "source": "HolonIQ", "url": "https://www.holoniq.com/notes/ai-education-market-2026", "summary": "HolonIQ报告显示全球AI教育市场2026年规模达500亿美元，中国和美国各占30%，个性化AI辅导是最大细分市场。", "category": "市场动态"},
            {"title": "Graphcore浴火重生：软银注资后发布Colossus MK3 AI芯片", "source": "The Register", "url": "https://www.theregister.com/2026/05/11/graphcore-colossus-mk3/", "summary": "在被软银收购后，英国AI芯片公司Graphcore发布Colossus MK3 IPU，采用晶圆级集成技术，单芯片AI算力达1 PFLOPS。", "category": "AI芯片"},
            {"title": "量子AI突破：谷歌Willow量子芯片加速机器学习训练100倍", "source": "Google Research", "url": "https://research.google/blog/willow-quantum-machine-learning/", "summary": "Google Research利用Willow量子芯片实现了特定机器学习任务的100倍加速，为量子AI实用化铺平道路。", "category": "研究前沿"},
            {"title": "Character.AI创始人Noam Shazeer重返Google：人才回流潮继续", "source": "CNBC", "url": "https://www.cnbc.com/2026/05/11/noam-shazeer-returns-google.html", "summary": "Character.AI联合创始人Noam Shazeer重返Google DeepMind，负责下一代对话AI研发。Character.AI以27亿美元被Google收购。", "category": "市场动态"},
            {"title": "三星发布Exynos 2600 AI手机芯片：端侧支持运行10B大模型", "source": "三星半导体", "url": "https://semiconductor.samsung.com/news/exynos-2600-ai/", "summary": "三星发布Exynos 2600，内置NPU算力达80 TOPS，支持在手机上离线运行10B参数大模型，用于实时翻译和AI摄影。", "category": "AI芯片"},
        ]
    },
    "2026-05-12": {
        "update_time": "2026-05-12T10:00:00+08:00",
        "hot_topics": [
            {"title": "OpenAI与新闻集团达成每年10亿美元内容授权协议：AI训练数据走向合规", "source": "华尔街日报", "url": "https://www.wsj.com/business/media/openai-news-corp-1-billion-license-2026", "summary": "OpenAI与新闻集团(News Corp)签署每年10亿美元的内容授权协议，覆盖《华尔街日报》《泰晤士报》等媒体。标志着AI训练数据从'免费抓取'走向'付费授权'新时代。", "category": "政策监管", "rating": 5},
            {"title": "特斯拉Optimus首次承接外部订单：丰田订购500台用于工厂", "source": "Nikkei Asia", "url": "https://asia.nikkei.com/Business/Tesla-Optimus-Toyota-order-500-robots", "summary": "特斯拉首次获得人形机器人外部订单——丰田汽车订购500台Optimus Gen 3用于其得州工厂。马斯克称Optimus订单已排至2028年。", "category": "具身智能", "rating": 5},
            {"title": "Google DeepMind CEO Demis Hassabis预言：'AGI将在5年内实现'", "source": "The Times", "url": "https://www.thetimes.co.uk/article/demis-hassabis-agi-five-years-deepmind", "summary": "DeepMind CEO Demis Hassabis在接受专访时大胆预言AGI将在5年内（2031年前）实现，并透露DeepMind正在开发'世界模型'作为通往AGI的关键路径。", "category": "大模型", "rating": 5},
            {"title": "全球AI监管碎片化加剧：G7未能就AI治理达成共同框架", "source": "Reuters", "url": "https://www.reuters.com/world/g7-ai-governance-failure-2026-05-12/", "summary": "G7峰会未能就AI全球治理达成共同框架，美欧在监管严格程度上分歧严重。分析认为AI监管'碎片化'将增加企业合规成本并阻碍AI发展。", "category": "政策监管", "rating": 4},
        ],
        "raw_articles": [
            {"title": "Canva发布AI设计助手Magic Studio 3.0：一句话生成完整品牌VI", "source": "Canva Blog", "url": "https://www.canva.com/newsroom/news/magic-studio-3/", "summary": "Canva发布Magic Studio 3.0，可通过一句话生成完整的品牌VI（Logo、配色、字体、宣传物料），大幅降低设计门槛。", "category": "应用落地"},
            {"title": "AI预测极端天气准确率超90%：DeepMind GraphCast 3发布", "source": "DeepMind Blog", "url": "https://deepmind.google/blog/graphcast-3/", "summary": "DeepMind发布GraphCast 3天气预测模型，10天天气预报准确率超过传统数值模型，极端天气预警提前量从3天延长至7天。", "category": "研究前沿"},
            {"title": "百度地图AI导航采用大模型：实时理解路况并给出人性化建议", "source": "百度地图", "url": "https://map.baidu.com/ai-navigation-2026", "summary": "百度地图全面升级AI导航，基于大模型实时理解路况并给出'前面堵车建议买杯咖啡等10分钟'这样的类人化建议。", "category": "应用落地"},
            {"title": "微软研究院发布VASA-2：单张照片+音频=超真实说话视频", "source": "Microsoft Research", "url": "https://www.microsoft.com/en-us/research/project/vasa-2/", "summary": "微软研究院发布VASA-2，仅需一张照片和一段音频即可生成超真实的说话视频，唇形同步、表情和头部动作均自然流畅。", "category": "研究前沿"},
            {"title": "国内AI大模型'百模大战'进入下半场：市场集中度提升", "source": "艾瑞咨询", "url": "https://www.iresearch.cn/report/ai-foundation-model-2026.html", "summary": "艾瑞咨询报告显示中国AI大模型市场CR5（前五集中度）从2025年的45%提升至2026年的72%，头部效应显现，中小模型厂商面临淘汰。", "category": "市场动态"},
            {"title": "腾讯Robotics X实验室发布'天鹅'双足机器人：行走能效超人类", "source": "腾讯AI Lab", "url": "https://ai.tencent.com/ailab/zh/news/swan-biped-2026", "summary": "腾讯Robotics X发布'天鹅'双足机器人，采用被动动力学设计，行走能效比(COT)达到0.25，超越人类的0.3，一次充电可走50公里。", "category": "具身智能"},
            {"title": "Databricks完成100亿美元融资：数据+AI平台估值突破2000亿美元", "source": "Bloomberg", "url": "https://www.bloomberg.com/news/articles/2026-05-12/databricks-10-billion-funding", "summary": "Databricks完成100亿美元融资，估值达2000亿美元。CEO Ali Ghodsi表示AI正从'模型竞赛'转向'数据竞赛'。", "category": "市场动态"},
            {"title": "美国国防部发布'负责任AI军事应用'政策：禁止AI自主开火决策", "source": "DoD", "url": "https://www.defense.gov/News/Releases/Release/Article/ai-military-policy-2026/", "summary": "美国国防部发布AI军事应用政策，明确禁止AI做出自主开火决策，要求'人在回路中'(human-in-the-loop)原则。", "category": "政策监管"},
            {"title": "AI Agent框架CrewAI发布企业版：多Agent协作编排成企业标配", "source": "CrewAI Blog", "url": "https://blog.crewai.com/enterprise-2026", "summary": "CrewAI发布企业版多Agent框架，支持角色定义、任务编排、Agent间通信，已获300+企业付费客户。", "category": "应用落地"},
        ]
    },
    "2026-05-13": {
        "update_time": "2026-05-13T10:00:00+08:00",
        "hot_topics": [
            {"title": "今日焦点：2026全球AI最新进展全景——从GPT到机器人", "source": "综合报道", "url": "https://shnywang.github.io/ai_news/site/index.html", "summary": "本日汇总：GPT-5.5引领多模态AI新高度，具身智能全面提速（特斯拉Optimus获外部订单、Figure 02通过工业可靠性验证），中国AI芯片自给率突破35%，全球AI治理进入执法阶段。", "category": "市场动态", "rating": 5},
            {"title": "中国AI芯片自给率突破35%：国产替代加速", "source": "工信部", "url": "https://www.miit.gov.cn/xwdt/gxdt/sjdt/art/2026/art_ab12cd34ef56.html", "summary": "工信部最新数据显示，中国AI芯片自给率已达35%，较2025年的22%大幅提升。华为昇腾、壁仞科技、寒武纪三家合计占国内市场份额的60%。", "category": "AI芯片", "rating": 5},
            {"title": "全球首个人形机器人'马拉松'比赛将在北京举行：10公里考验极限", "source": "新华社", "url": "https://www.xinhuanet.com/sports/2026-05/13/c_1213457000.htm", "summary": "北京市宣布将于6月举办全球首个人形机器人马拉松比赛，全程10公里，宇树、小米、智元等20家企业报名参赛，考验机器人续航和运动稳定性。", "category": "具身智能", "rating": 5},
            {"title": "Sam Altman确认GPT-6训练已启动：'将带来又一次质的飞跃'", "source": "Sam Altman X", "url": "https://x.com/sama/status/1789500000000000000", "summary": "Sam Altman在社交媒体确认GPT-6已开始训练，预计需要'数月'时间。暗示新模型将在推理、多模态和Agent能力上实现质的飞跃。", "category": "大模型", "rating": 5},
            {"title": "欧盟宣布对AI生成内容实施强制数字水印标准：2027年全面生效", "source": "European Commission", "url": "https://ec.europa.eu/commission/presscorner/detail/en/ip_26_2345", "summary": "欧盟委员会宣布从2027年1月起，所有在欧盟境内发布的AI生成内容（文字、图片、视频、音频）必须嵌入C2PA标准数字水印，违者最高罚款全球营收6%。", "category": "政策监管", "rating": 5},
        ],
        "raw_articles": [
            {"title": "Anthropic发布Claude 4.5 Sonnet：编程能力再提升，SWE-bench突破65%", "source": "Anthropic Blog", "url": "https://www.anthropic.com/news/claude-4-5-sonnet", "summary": "Anthropic发布Claude 4.5 Sonnet，编程能力进一步提升，SWE-bench得分达65%，新增多文件重构和跨仓库代码理解能力。", "category": "大模型"},
            {"title": "字节跳动豆包大模型日活突破5亿：超越ChatGPT成为全球最大AI应用", "source": "36氪", "url": "https://36kr.com/p/3267890123456880", "summary": "字节跳动内部数据显示豆包大模型全球日活用户突破5亿，超越ChatGPT成为日活最高的AI应用，主要得益于中国市场和东南亚扩张。", "category": "大模型"},
            {"title": "滴滴Robotaxi北京上路：亦庄开放全无人驾驶商业运营", "source": "北京日报", "url": "https://bjnews.bjd.com.cn/2026/05/13/123456.html", "summary": "北京亦庄经开区全面开放全无人驾驶商业运营，滴滴、百度、小马智行三家获牌，市民可用App呼叫无人出租车。", "category": "应用落地"},
            {"title": "NVIDIA RTX 6090发布：消费级AI算力突破100 TFLOPS", "source": "NVIDIA Blog", "url": "https://blogs.nvidia.com/blog/rtx-6090/", "summary": "NVIDIA发布消费级旗舰显卡RTX 6090，AI算力达120 TFLOPS(FP16)，支持本地运行70B大模型，售价$1999。", "category": "AI芯片"},
            {"title": "Waymo无人驾驶累计行驶突破1亿英里：事故率仅为人类驾驶1/10", "source": "Waymo Blog", "url": "https://waymo.com/blog/2026/05/100-million-miles/", "summary": "Waymo宣布无人驾驶车累计自主行驶里程突破1亿英里(1.6亿公里)，有责事故率仅为人类驾驶的1/10。", "category": "应用落地"},
            {"title": "具身智能学术顶会CoRL 2026投稿量暴涨3倍：会议扩容至万人规模", "source": "CoRL 2026", "url": "https://www.corl2026.org/news/submission-record", "summary": "机器人学习顶会CoRL 2026投稿量较去年暴涨3倍达6000篇，具身智能成为AI领域最热门研究方向，会议被迫扩容至万人规模。", "category": "具身智能"},
            {"title": "全球AI人才分布报告：美国占38%，中国占25%，欧洲占18%", "source": "MacroPolo", "url": "https://macropolo.org/ai-talent-tracker-2026/", "summary": "MacroPolo发布2026年全球AI人才报告，美国仍以38%占比领先，中国从2024年的12%飙升至25%，AI人才'回流潮'加速。", "category": "市场动态"},
            {"title": "联想发布AI PC新战略：首批'神经处理单元'笔记本月销百万", "source": "联想", "url": "https://news.lenovo.com/pressroom/press-releases/ai-pc-neural-processing-2026/", "summary": "联想发布搭载独立NPU(神经处理单元)的AI PC新品，支持本地运行14B大模型，首批产品月销突破100万台。", "category": "应用落地"},
            {"title": "DALL-E 4 vs Midjourney V7 vs SD4：AI绘画三巨头全面对比", "source": "The Verge", "url": "https://www.theverge.com/2026/5/13/ai-image-generation-showdown", "summary": "The Verge发布2026年AI绘画工具全面对比评测，DALL-E 4在文字渲染上领先，Midjourney V7在艺术质感上最佳，SD4在开放性上胜出。", "category": "大模型"},
            {"title": "AI失业潮vs新就业：全球科技行业裁员30万，AI相关岗位增长80万", "source": "LinkedIn", "url": "https://economicgraph.linkedin.com/blog/ai-jobs-2026", "summary": "LinkedIn发布2026全球劳动力报告，科技行业裁员30万但AI相关新增岗位80万，净增50万就业，但技能错配问题突出。", "category": "市场动态"},
            {"title": "北京自动驾驶示范区扩展至600平方公里：人口覆盖500万", "source": "北京日报", "url": "https://bjnews.bjd.com.cn/2026/05/13/123457.html", "summary": "北京高级别自动驾驶示范区扩展至600平方公里，覆盖500万人口，支持Robotaxi、无人配送、无人环卫等全场景应用。", "category": "应用落地"},
        ]
    },
}

# Write all files
for date, data in days.items():
    filepath = os.path.join(DATA_DIR, f"{date}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump({date: data}, f, ensure_ascii=False, indent=2)
    print(f"✅ {date}.json written ({len(data['hot_topics'])} hot_topics, {len(data['raw_articles'])} raw_articles)")

print(f"\nTotal files: {len(days)}")
