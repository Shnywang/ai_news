#!/usr/bin/env python3
"""Add role-specific boards to the 7 visible days (May 7-13)"""
import json
import os

DATA_DIR = "/home/wyf/.hermes/hermes-agent/ai_news/data"

# Role-specific boards for each day - analytical perspectives on the same news
boards = {
    "2026-05-07": {
        "startup_board": {
            "companies": [
                {"name": "Apple", "field": "端侧AI/大模型", "route": "iOS 20集成3B设备端LLM+AI Siri+AI Xcode", "funding": "自研Apple Intelligence平台", "verdict": "WWDC 2026将成Apple AI战略转折点，设备端LLM策略差异化明显"},
                {"name": "Google DeepMind", "field": "通用AI Agent", "route": "Gato 2单一模型完成600种任务，迈向AGI", "funding": "Alphabet持续投入", "verdict": "Gato 2展示的通用性标志着从'专用AI'向'通用AI'的关键转变"},
                {"name": "傅利叶智能", "field": "人形机器人", "route": "GR-2完成户外复杂地形2公里自主行走", "funding": "已完成多轮融资", "verdict": "户外复杂地形行走是人形机器人实用化的关键瓶颈，GR-2的突破意义重大"},
                {"name": "Anthropic", "field": "大模型/企业AI", "route": "Claude企业版私有部署，数据不出企业防火墙", "funding": "估值达1万亿美元", "verdict": "企业合规需求驱动私有部署方案，金融/政府客户将成增长引擎"},
            ],
            "trend": "AI竞争进入'端侧+企业+通用'三线并进阶段：Apple主攻端侧，Anthropic深耕企业，Google/DeepMind追求AGI通用性"
        },
        "pm_board": {
            "insights": [
                {"title": "端侧AI将成为消费电子产品的分水岭", "content": "Apple iOS 20的设备端LLM方案标志着一个重要趋势：用户越来越关注AI隐私和离线可用性。产品经理需要思考：如何在端侧算力有限的情况下设计差异化AI体验？离线场景的AI功能设计将成为新课题。"},
                {"title": "AI伦理从'可选'变成'必选项'", "content": "中国发布全球首个具身智能伦理准则，联合国通过全球AI治理决议。对产品经理而言，AI产品设计必须从一开始就嵌入伦理考量(隐私、可追溯、不伤害)，这不再是'锦上添花'而是市场准入条件。"},
                {"title": "AI Agent企业化部署的合规挑战", "content": "Anthropic推出私有VPC部署方案、法律AI Harvey估值120亿美元——垂直领域的AI应用必须在'强大功能'与'合规安全'之间找到平衡。产品设计需要考虑数据驻留、审计追溯、权限管控。"},
            ],
            "focus": ["端侧AI体验设计", "AI产品伦理合规框架", "垂直行业AI产品化策略", "AI Agent的企业落地路径"]
        },
        "algo_board": {
            "insights": [
                {"title": "Gato 2：重新定义'通用'的标准", "content": "DeepMind Gato 2以单一模型完成600种任务(Atari游戏→机器人操作→代码编写)，核心技术突破在于统一的token化表示和多任务联合训练策略。这验证了'通用AI Agent'的技术可行性。", "url": "https://deepmind.google/blog/gato-2/"},
                {"title": "Qwen-3-VL多模态能力碾压GPT-5", "content": "阿里Qwen-3-VL在文档理解、图表分析、视频问答上超越GPT-5，开源Apache 2.0。技术亮点包括改进的视觉编码器和跨模态对齐策略。", "url": "https://qwenlm.github.io/blog/qwen-3-vl/"},
                {"title": "AI自主完成数学猜想证明", "content": "DeepMind AlphaProof驱动的AI系统自主完成图论猜想完整证明，经6位数学家审稿确认。技术关键：结合形式化验证(Lean)和强化学习的定理证明策略。"},
            ],
            "tech_radar": [
                {"direction": "通用AI Agent(Gato范式)", "status": "技术验证", "advice": "关注统一token化表示和多任务联合训练方法"},
                {"direction": "端侧LLM(3B-7B)", "status": "快速迭代", "advice": "量化+蒸馏+MoE小模型是端侧部署的关键路径"},
                {"direction": "AI定理证明", "status": "里程碑突破", "advice": "形式化验证(Lean/Coq)与RL结合是突破口"},
                {"direction": "多模态大模型", "status": "商业化加速", "advice": "视觉-语言对齐质量已接近实用门槛"},
                {"direction": "AI安全对齐", "status": "持续演进", "advice": "Constitutional AI等自我监督方法降低对齐成本"},
            ],
            "focus": ["通用AI Agent架构", "端侧模型推理优化", "多模态对齐技术", "AI数学推理"]
        },
        "projmgr_board": {
            "insights": [
                {"title": "全球AI治理框架化增加了项目合规成本", "content": "联合国通过全球AI治理决议、中国发布具身智能伦理准则——AI项目管理需要新增'合规里程碑'节点，包括伦理审查、安全测试、可追溯性验证等。"},
                {"title": "AI项目从'技术驱动'转向'价值驱动'", "content": "百度自动驾驶在武汉全域开放(覆盖1100万人)、法律AI Harvey估值120亿美元——这些案例的共同点是：项目的商业价值验证(PMF)远比技术炫技重要。"},
            ],
            "focus": ["AI项目合规管理", "具身智能量产交付", "AI产品PMF验证方法"]
        },
        "action_items": {
            "tech_selection": ["端侧部署优先评估Qwen-3-VL等开源方案", "企业AI选型考虑Claude私有部署的合规优势", "通用AI场景关注Gato 2的统一架构思路"],
            "track_judgment": ["AI伦理合规从可选项变为必选项，提前布局降低成本", "开源多模态模型(Qwen/VL系列)已具备商用竞争力"],
            "watch_list": ["Apple WWDC 2026 AI发布", "Gato 2后续开源计划", "具身智能伦理标准落地进展", "AI治理国际协调进展"]
        },
        "hermes_board": {
            "insights": [
                {"title": "Hermes Agent 多平台连接能力持续增强", "content": "Hermes Agent支持Telegram、Discord、Slack、WeChat、QQ等多平台消息互通，AI Agent作为'消息中枢'的定位越来越清晰。结合Claude、GPT等后端模型，可实现跨平台智能问答和任务执行。"},
                {"title": "AI Agent工作流编排成为效率提升关键", "content": "LangChain完成1.5亿美元融资，CrewAI发布企业版——多Agent协作编排正成为企业AI部署的标准模式。Hermes Agent的skill系统和delegate_task机制与此趋势高度契合。"},
            ],
            "tech_stack": [
                {"title": "Skill系统：可复用的AI工作流组件", "content": "Hermes Agent的skill机制允许将复杂任务封装为可复用技能，支持create/patch/edit生命周期管理，配合cronjob实现定时自动化。", "url": "https://hermes-agent.nousresearch.com/docs"},
            ],
            "community": [
                {"title": "LangChain获1.5亿美元B轮融资", "content": "AI Agent框架成为基础设施赛道，LangChain的LangGraph月下载破5000万次，验证了Agent编排框架的商业价值。", "url": "https://techcrunch.com/2026/05/05/langchain-150m-series-b/"},
            ]
        }
    },
    "2026-05-08": {
        "startup_board": {
            "companies": [
                {"name": "NVIDIA", "field": "AI芯片", "route": "Rubin架构2027年目标单卡10 PFLOPS", "funding": "市值突破5万亿美元", "verdict": "Rubin架构3nm GAA+HBM4是应对AMD/Intel挑战的关键，CUDA生态护城河仍深"},
                {"name": "Tesla/Optimus", "field": "人形机器人", "route": "Gen 3实现自主充电，24/7无人化运营", "funding": "自研+外部订单(丰田500台)", "verdict": "自主充电是工厂无人化的最后拼图，Optimus正在从'demo'走向'产品'"},
                {"name": "Thinking Machines", "field": "安全AI", "route": "OpenAI前CTO Mira Murati创办，专注安全AGI", "funding": "10亿美元种子轮", "verdict": "OpenAI高层出走创办新公司，'安全AGI'叙事获得顶级资本背书"},
                {"name": "Intel", "field": "AI芯片", "route": "Falcon Shores 3正面挑战NVIDIA", "funding": "Intel 18A工艺自研", "verdict": "新CEO陈立武称此为'生死之战'，Intel能否在AI芯片市场分一杯羹?"},
            ],
            "trend": "AI芯片进入'三国杀'时代(NVIDIA/AMD/Intel)，人形机器人从研发走向交付，OpenAI人才外溢催生新一轮创业潮"
        },
        "pm_board": {
            "insights": [
                {"title": "'家用AI数据中心'概念：是泡沫还是未来?", "content": "多家创业公司推出5万美元家用AI服务器，号称可在家运行大模型赚取推理费。产品经理需理性评估：用户真实需求是什么？经济模型是否成立？参考'挖矿热'的历史教训。"},
                {"title": "人形机器人的'产品化'拐点", "content": "特斯拉Optimus实现自主充电意味着机器人可以脱离人类干预持续运行。产品维度看，人形机器人正从'需要操作员'的工具变成'自主运行'的产品，这是产品定义的质变。"},
                {"title": "AI内容版权的新模式值得关注", "content": "Anthropic推出Creator Fund，将20% API利润分配给训练数据中的内容创作者。这为AI时代的版权问题提供了创新解决方案，PM应思考如何将'内容贡献者'纳入产品生态。"},
            ],
            "focus": ["AI硬件消费化趋势", "人形机器人产品定义", "AI版权分配机制", "OpenAI人才外溢的产业影响"]
        },
        "algo_board": {
            "insights": [
                {"title": "Rubin架构：从制程到封装的全方位创新", "content": "NVIDIA Rubin采用3nm GAA工艺+HBM4内存+先进Chiplet设计，单卡AI算力目标10 PFLOPS。这不仅是制程升级，更是系统级架构革新。", "url": "https://blogs.nvidia.com/blog/rubin-architecture-2027/"},
                {"title": "'家用数据中心'背后的技术可行性", "content": "在消费级硬件上运行大模型的核心技术：INT4/INT8量化、投机解码(Speculative Decoding)、MoE稀疏激活。RTX 6090的120 TFLOPS FP16算力理论上可运行70B模型。"},
            ],
            "tech_radar": [
                {"direction": "3nm GAA AI芯片", "status": "2027量产", "advice": "Rubin/IPC Falcon Shores将重划AI芯片格局"},
                {"direction": "端侧大模型推理", "status": "进入实用", "advice": "量化+投机解码使消费级硬件运行大模型成为可能"},
                {"direction": "自主充电机器人", "status": "技术突破", "advice": "特斯拉Optimus方案验证了自主能源管理的可行性"},
                {"direction": "AI版权/收益分配", "status": "早期探索", "advice": "Anthropic Creator Fund模式值得关注"},
            ],
            "focus": ["3nm AI芯片架构", "端侧模型推理优化", "AI能源效率", "模型训练数据版权"]
        },
        "projmgr_board": {
            "insights": [
                {"title": "AI芯片供应链风险管理日益重要", "content": "NVIDIA Rubin、Intel Falcon Shores、AMD MI400三线并进，但3nm产能有限(台积电80%产能用于AI芯片)。项目管理需要建立多供应商策略和产能风险预案。"},
                {"title": "OpenAI管理层震荡的启示", "content": "CTO Mira Murati等高管离职后立即获10亿美元融资创办新公司——顶级AI人才的流动性和创业门槛值得关注。项目管理层面应建立关键人才风险应对机制。"},
            ],
            "focus": ["AI芯片供应链风险", "AI团队人才保留策略", "人形机器人量产项目管理"]
        },
        "action_items": {
            "tech_selection": ["AI训练芯片关注Rubin架构(2027)和Falcon Shores 3路线图", "端侧推理优先评估RTX 6090+量化方案", "版权合规关注Anthropic Creator Fund模式"],
            "track_judgment": ["AI芯片市场将从'NVIDIA一家独大'走向'三强竞争'，2027年是关键转折点", "OpenAI组织动荡可能加速AI人才向创业公司流动"],
            "watch_list": ["NVIDIA Rubin架构量产时间表", "Intel Falcon Shores 3独立评测", "Mira Murati的Thinking Machines产品方向", "Optimus丰田订单交付时间"]
        },
        "hermes_board": {
            "insights": [
                {"title": "AI Agent框架生态快速成熟", "content": "CrewAI发布企业版多Agent框架，支持角色定义和任务编排。Hermes Agent的delegate_task机制作为多Agent协作的基础设施，与行业趋势高度一致。"},
                {"title": "Linux基金会成立AI Infra联盟", "content": "Intel、AMD、Arm等30家企业联合推进AI基础设施开放标准。Hermes Agent作为跨平台AI Agent，开放标准对其生态扩展至关重要。", "url": "https://www.linuxfoundation.org/press/ai-infra-alliance"},
            ],
            "tech_stack": [
                {"title": "CrewAI企业版：多Agent协作编排", "content": "支持角色定义、任务编排、Agent间通信，300+企业付费客户。可作为Hermes Agent多Agent模式的参考实现。", "url": "https://blog.crewai.com/enterprise-2026"},
            ],
            "community": [
                {"title": "AI Infra Alliance成立", "content": "Linux Foundation主导的AI基础设施联盟，推动GPU、NPU、AI框架的互操作性标准。", "url": "https://www.linuxfoundation.org/press/ai-infra-alliance"},
            ]
        }
    },
    "2026-05-09": {
        "startup_board": {
            "companies": [
                {"name": "月之暗面(Kimi)", "field": "大模型/长上下文", "route": "1000万token超大上下文2.0", "funding": "多轮融资，估值超200亿", "verdict": "千万级上下文是差异化杀手锏，法律/金融等长文档场景有独特优势"},
                {"name": "Anthropic", "field": "大模型/AI版权", "route": "Creator Fund：API利润20%分配给创作者", "funding": "估值1万亿美元", "verdict": "AI版权破局方案，可能成为行业标准，但也面临利润分配比例争议"},
                {"name": "Intel", "field": "AI芯片", "route": "Falcon Shores 3，采用Intel 18A工艺", "funding": "自研，新CEO陈立武主导", "verdict": "'不成功便成仁'的豪赌，Intel在AI芯片市场的最后机会窗口"},
                {"name": "宇树科技", "field": "人形机器人", "route": "G1首批通过中国L3人形机器人能力认证", "funding": "已完成B+轮", "verdict": "中国首个机器人能力等级标准发布，宇树先发优势明显"},
            ],
            "trend": "长上下文竞赛升级(百万→千万token)，AI版权分配从'对抗'走向'合作'，中国机器人标准化进程加速"
        },
        "pm_board": {
            "insights": [
                {"title": "AI版权分成：产品设计的新维度", "content": "Anthropic的Creator Fund开创了AI平台与内容创作者的利益分配机制。产品经理需要考虑：如何在产品中追踪内容来源、计算贡献度、实现公平分配？这可能催生全新的'AI版权管理'产品品类。"},
                {"title": "人形机器人'驾照'标准的产品意义", "content": "中国发布L1-L5五级机器人能力标准——类比自动驾驶分级，为产品定位和用户预期管理提供了清晰的框架。产品经理可以用'L3级人形机器人'这样直观的标签进行市场沟通。"},
                {"title": "长上下文=新产品形态?", "content": "Kimi 1000万token上下文(可处理整部大英百科全书)不仅是技术参数提升，更可能催生全新的产品形态：全库检索、跨文档推理、知识图谱自动构建等。"},
            ],
            "focus": ["AI版权分配的产品化", "长上下文场景设计", "人形机器人产品分级", "AI芯片选型策略"]
        },
        "algo_board": {
            "insights": [
                {"title": "1000万token上下文的实现挑战", "content": "Kimi的超大上下文版本背后的技术：分块注意力(Chunked Attention)+层次化缓存+检索增强。关键挑战在于长文本中的'中间丢失'(Lost in the Middle)问题和推理延迟。", "url": "https://www.qbitai.com/2026/05/28500.html"},
                {"title": "Intel 18A工艺+RibbonFET：能否挑战台积电?", "content": "Intel Falcon Shores 3采用自研18A(1.8nm)工艺和RibbonFET(GAA)晶体管，这是Intel首次在先进制程上正面挑战台积电。Chiplet设计同时降低了单芯片面积和良率压力。"},
            ],
            "tech_radar": [
                {"direction": "千万级上下文窗口", "status": "技术突破", "advice": "分块注意力是关键，关注长文本检索精度"},
                {"direction": "Intel 18A + GAA", "status": "必须成功", "advice": "Falcon Shores 3是Intel AI芯片生死战"},
                {"direction": "AI内容溯源/水印", "status": "标准制定中", "advice": "C2PA标准+区块链溯源是主要技术路线"},
                {"direction": "机器人能力分级标准", "status": "中国首发", "advice": "L1-L5分级框架可能成为国际标准参考"},
            ],
            "focus": ["长上下文注意力机制", "Intel vs TSMC先进制程竞赛", "AI内容溯源技术", "机器人能力评估基准"]
        },
        "projmgr_board": {
            "insights": [
                {"title": "NVIDIA反垄断调查增加供应链不确定性", "content": "中国和欧盟同时对NVIDIA启动反垄断调查，关注CUDA生态的排他性。AI项目如果重度依赖CUDA，需要考虑备选方案(AMD ROCm/Intel oneAPI)。"},
                {"title": "AI标准化进程加速要求项目提前对齐", "content": "中国人形机器人能力分级标准发布，欧盟AI水印标准2027年生效——项目规划需要考虑标准合规的时间窗口，避免产品上市后被迫返工。"},
            ],
            "focus": ["AI供应链多元化", "国际AI标准合规", "人形机器人认证流程"]
        },
        "action_items": {
            "tech_selection": ["长上下文场景优先评估Kimi等千万级方案", "AI芯片选型关注Intel Falcon Shores 3(2026年底)", "AI内容合规关注C2PA水印标准"],
            "track_judgment": ["NVIDIA反垄断调查可能重塑AI芯片市场格局", "AI版权分配机制将从'对抗'转向'合作'"],
            "watch_list": ["Intel Falcon Shores 3独立性能评测", "NVIDIA反垄断调查进展", "中国机器人L4/L5标准制定", "Anthropic Creator Fund首批分配数据"]
        },
        "hermes_board": {
            "insights": [
                {"title": "多Agent协作标准化的前夜", "content": "AI Agent框架爆发(LangChain/CrewAI/AutoGen)，但缺乏统一的Agent间通信标准。Hermes Agent的MCP(Model Context Protocol)可能是解决这一问题的关键。"},
                {"title": "GitHub Copilot X：代码仓库级别的AI理解", "content": "Copilot X可理解整个代码仓库上下文，支持跨文件重构。这与Hermes Agent的codebase-inspection skill思路一致——AI需要全局理解而非局部补全。", "url": "https://github.blog/2026-05-09-copilot-x-ga/"},
            ],
            "tech_stack": [
                {"title": "GitHub Copilot X：全仓库AI理解", "content": "支持跨文件重构、自动PR描述、代码审查意见生成。代表了AI编程工具从'行级补全'到'仓库级理解'的进化。", "url": "https://github.blog/2026-05-09-copilot-x-ga/"},
            ],
            "community": [
                {"title": "斯坦福HAI 2026 AI Index发布", "content": "中国在AI专利和机器人部署上领先，美国在基础模型和AI人才上保持优势。", "url": "https://hai.stanford.edu/news/ai-index-2026"},
            ]
        }
    },
    "2026-05-10": {
        "startup_board": {
            "companies": [
                {"name": "零一万物", "field": "开源大模型", "route": "Yi-3.0 340B MoE，全面对标GPT-5", "funding": "李开复创办，多轮融资", "verdict": "中文开源模型最强选手之一，数学推理能力突出"},
                {"name": "傅利叶智能", "field": "医疗机器人", "route": "GR-2获FDA认证，全球首款临床级人形康复机器人", "funding": "已完成C轮", "verdict": "FDA认证是人形机器人医疗化的里程碑，打开了全新的百亿美元市场"},
                {"name": "AMD", "field": "AI芯片", "route": "MI400系列降价40%正面挑战NVIDIA", "funding": "自研+台积电代工", "verdict": "价格战是AMD最有效的武器，CUDA兼容层是破局关键"},
                {"name": "DeepMind", "field": "AI研究", "route": "AI发现新拓扑不变量+开源Genie 3世界模型", "funding": "Alphabet支持", "verdict": "同时推进基础科学突破和开源工具，DeepMind的'双向战略'日渐清晰"},
            ],
            "trend": "AMD发起AI芯片价格战，开源模型进入'性能对标闭源'阶段，人形机器人医疗化开辟新市场"
        },
        "pm_board": {
            "insights": [
                {"title": "AI芯片降价潮：算力成本曲线加速下降", "content": "AMD MI400系列降价40%+AWS自研Trainium 3+Intel Falcon Shores 3入局——AI算力正在从'稀缺资源'变成'竞争性商品'。产品经理应预期推理成本在未来18个月下降50-70%，这会影响AI产品的定价策略。"},
                {"title": "人形机器人进入医疗：产品设计的新要求", "content": "傅利叶GR-2获FDA认证意味着人形机器人进入高度监管的医疗市场。产品设计需要满足：安全性(失效保护)、有效性(临床证据)、可用性(医护操作简便)。这是完全不同于工厂场景的产品逻辑。"},
                {"title": "开源模型的'商用就绪'信号", "content": "零一万物Yi-3.0开源且性能对标GPT-5，IBM Granite 4.0全系列开源——开源模型正在从'研究玩具'变成'生产工具'。产品选型时开源方案应从'备选'升级为'首选评估'。"},
            ],
            "focus": ["AI算力成本趋势预测", "医疗机器人产品设计", "开源vs闭源模型选型框架", "AI芯片价格战对产品定价的影响"]
        },
        "algo_board": {
            "insights": [
                {"title": "Yi-3.0：340B MoE架构的技术路线", "content": "零一万物Yi-3.0采用340B参数MoE架构(激活约45B)，在中文数学推理上尤其突出。关键技术：改进的MoE路由算法+中文语料深度优化+多阶段对齐训练。", "url": "https://www.01.ai/blog/yi-3-2026"},
                {"title": "DeepMind AI数学发现：AI开始做原创科学", "content": "AI发现全新拓扑不变量被称为'AI不变量'——这是AI在纯数学领域做出的首个原创性贡献。技术关键：结合大规模搜索+符号推理+数学家反馈循环。", "url": "https://www.nature.com/articles/s41586-026-00890-3"},
                {"title": "Genie 3：世界模型的开放之路", "content": "DeepMind开源Genie 3，从单张图片生成可交互3D世界。底层技术：视频预测模型+动作条件生成+3D隐式表示。对机器人学习和游戏开发有巨大价值。"},
            ],
            "tech_radar": [
                {"direction": "中文开源大模型", "status": "成熟商用", "advice": "Yi-3.0/Qwen-3已具备替代闭源产品的能力"},
                {"direction": "AI科学发现(数学/物理)", "status": "原创突破", "advice": "AI开始在纯科学领域做出人类未发现的贡献"},
                {"direction": "世界模型(Genie/Sora)", "status": "快速迭代", "advice": "从视频生成到可交互3D世界，进步速度惊人"},
                {"direction": "MoE架构优化", "status": "主流方案", "advice": "MoE已成为千亿级模型的标准架构"},
            ],
            "focus": ["MoE路由算法优化", "AI for Math/Science", "世界模型架构", "开源模型商用部署"]
        },
        "projmgr_board": {
            "insights": [
                {"title": "AI芯片价格战=算力成本红利期", "content": "AMD降价40%+AWS自研芯片+AWS Trainium 3——项目经理应抓住这波算力成本下降窗口期，锁定长期算力合同。同时建立多芯片供应商策略，降低单一依赖风险。"},
                {"title": "医疗机器人项目管理：合规是第一优先级", "content": "傅利叶GR-2获FDA认证的过程为行业提供了模板：临床验证→安全测试→监管沟通→上市后监测。医疗AI项目管理需要预留充足的合规时间(通常12-18个月)。"},
            ],
            "focus": ["算力采购策略优化", "医疗AI合规路径", "开源模型部署成本评估"]
        },
        "action_items": {
            "tech_selection": ["中文场景首选Yi-3.0/Qwen-3等开源方案", "AI训练芯片关注AMD MI400降价后的性价比", "世界模型/3D生成关注Genie 3开源生态"],
            "track_judgment": ["AI芯片价格战将加速AI应用落地，算力成本不再是最主要瓶颈", "医疗级人形机器人打开了全新的蓝海市场"],
            "watch_list": ["AMD MI400实际性能和CUDA兼容性", "Yi-3.0社区生态发展", "FDA后续机器人认证案例", "Apple ACDC AI芯片进展"]
        },
        "hermes_board": {
            "insights": [
                {"title": "世界模型开源对Agent的意义", "content": "DeepMind开源Genie 3——可交互3D世界模型对AI Agent的'具身化'训练至关重要。未来Hermes Agent可能通过世界模型进行'想象性规划'(mental simulation)，提升复杂任务的决策质量。"},
                {"title": "AI for Science成为Agent的新战场", "content": "AI发现新拓扑不变量、AI设计抗癌分子进入临床——这些案例表明AI Agent在科学研究自动化方面有巨大潜力。Hermes Agent的研究类skills可以向'AI科学家'方向演进。"},
            ],
            "tech_stack": [
                {"title": "Genie 3世界模型", "content": "从单张图片生成可交互3D世界，对Agent的模拟训练和场景理解有重要价值。", "url": "https://deepmind.google/blog/genie-3-open-source/"},
            ],
            "community": [
                {"title": "AI芯片价格战开启", "content": "AMD MI400降价40%，AWS Trainium 3发布，Intel Falcon Shores 3即将入局——AI算力民主化加速。", "url": "https://www.tomshardware.com/news/amd-mi400-price-cut-nvidia"},
            ]
        }
    },
    "2026-05-11": {
        "startup_board": {
            "companies": [
                {"name": "DeepSeek", "field": "开源大模型", "route": "梁文锋宣布持续开源所有模型", "funding": "幻方量化自研", "verdict": "开源承诺巩固了DeepSeek在开源社区的领导地位"},
                {"name": "Figure AI", "field": "人形机器人", "route": "在宝马工厂连续30天零事故运行", "funding": "估值超300亿美元", "verdict": "30天零事故是人形机器人从'可行'到'可靠'的关键里程碑"},
                {"name": "软银/ARM", "field": "AI芯片", "route": "秘密研发'寒武纪'AI处理器，目标2028年对标Rubin", "funding": "软银500亿美元AI基建计划", "verdict": "软银试图在AI芯片市场建立第三极(除NVIDIA/AMD外)"},
                {"name": "Graphcore", "field": "AI芯片", "route": "被软银收购后发布Colossus MK3，晶圆级集成", "funding": "软银全资", "verdict": "晶圆级AI芯片是差异化路线，但生态建设是最大挑战"},
            ],
            "trend": "GitHub 41%新代码由AI生成，编程自动化进入新阶段；人形机器人可靠性获验证；软银加速AI芯片布局"
        },
        "pm_board": {
            "insights": [
                {"title": "AI编程渗透率达41%：开发者的角色正在改变", "content": "GitHub报告41%新代码由AI生成。对产品经理而言，这意味着：1) 产品开发周期将大幅缩短；2) '会写代码'不再是产品经理与工程师沟通的硬门槛；3) 产品迭代速度将成为新的竞争维度。"},
                {"title": "30天零事故：工业人形机器人的'iPhone时刻'?", "content": "Figure 02在宝马工厂连续30天24小时运行零事故——这相当于汽车行业的'10万公里无大修'。工业客户最关心的可靠性问题获得了确凿的数据背书，人形机器人大规模部署的最后障碍正在消除。"},
                {"title": "梁文锋的'反垄断AI'宣言", "content": "DeepSeek创始人公开表态'AI不应该被少数公司垄断'，承诺持续开源。这一定位在开发者社区中获得强烈共鸣，'开源AI'正在成为一种价值观品牌。"},
            ],
            "focus": ["AI对软件开发流程的影响", "人形机器人可靠性标准", "开源AI的品牌化策略", "AI芯片供应链安全"]
        },
        "algo_board": {
            "insights": [
                {"title": "41%的代码由AI生成：这意味着什么?", "content": "GitHub Octoverse报告的技术内涵：AI生成的代码主要集中在模板代码(boilerplate)、测试用例、文档生成。但在核心算法和系统架构层面，人类仍占主导。Python超越JavaScript成为AI时代第一语言。", "url": "https://github.blog/2026-05-11-octoverse-ai-code-report/"},
                {"title": "ARM'寒武纪'：全新神经计算架构", "content": "软银通过ARM研发的'寒武纪'AI处理器据传采用全新神经计算架构(非传统SIMD/SIMT)，可能通过更高效的稀疏计算和近存计算来挑战NVIDIA的GPU架构。"},
            ],
            "tech_radar": [
                {"direction": "AI辅助编程", "status": "主流化(41%)", "advice": "开发者角色从'写代码'转向'审查AI生成的代码'"},
                {"direction": "人形机器人可靠性", "status": "工业级验证", "advice": "30天零事故是重要的可靠性里程碑"},
                {"direction": "晶圆级AI芯片", "status": "技术探索", "advice": "Graphcore Colossus路线，集成度极高但良率挑战大"},
                {"direction": "神经计算架构", "status": "早期研发", "advice": "ARM'寒武纪'试图用新架构挑战GPU范式"},
            ],
            "focus": ["AI代码生成质量评估", "机器人可靠性工程", "新型AI芯片架构", "开源模型训练效率"]
        },
        "projmgr_board": {
            "insights": [
                {"title": "AI辅助开发改变项目管理节奏", "content": "41%代码由AI生成意味着开发速度可能提升2-3倍，但代码审查和质量保证的负担也随之增加。项目管理需要调整：增加代码审查资源、建立AI生成代码的质量标准、重新定义'完成'(DoD)。"},
                {"title": "人形机器人从'能不能用'到'可不可靠'", "content": "Figure 02的30天零事故数据为人形机器人建立了可靠性基线。项目管理层面，这意味着可以开始使用MTBF(平均无故障时间)、可用率等工业指标来管理机器人部署项目。"},
            ],
            "focus": ["AI辅助开发的项目管理", "机器人可靠性度量", "AI生成代码质量管控"]
        },
        "action_items": {
            "tech_selection": ["AI辅助编程工具：GitHub Copilot X + Cursor组合", "中文大模型：DeepSeek持续开源，适合长期锁定", "AI芯片：关注ARM'寒武纪'进展，作为供应链多元化选项"],
            "track_judgment": ["AI辅助编程将从根本上改变软件开发行业，项目经理需提前准备", "人形机器人已通过工业可靠性验证，大规模部署即将开始"],
            "watch_list": ["ARM'寒武纪'芯片发布时间", "Figure AI下一轮融资/IPO", "DeepSeek下一代模型发布计划", "GitHub Copilot使用率趋势"]
        },
        "hermes_board": {
            "insights": [
                {"title": "AI编程渗透41%：Hermes Agent的代码生成能力", "content": "GitHub的数据验证了AI编程的主流化趋势。Hermes Agent通过codebase-inspection、code-review等skill，以及terminal/execute_code工具，正成为AI辅助编程的重要平台。"},
                {"title": "开源AI生态的持续壮大", "content": "DeepSeek承诺持续开源+HuggingFace用户破500万+Yi-3.0开源——开源AI生态正以前所未有的速度扩张。Hermes Agent作为开源AI Agent平台，将直接受益于这一趋势。"},
            ],
            "tech_stack": [
                {"title": "GitHub Copilot X：全仓库级别AI理解", "content": "可理解整个代码仓库上下文，代表AI编程工具的最高水平。", "url": "https://github.blog/2026-05-11-octoverse-ai-code-report/"},
            ],
            "community": [
                {"title": "GitHub Octoverse 2026", "content": "41%新代码由AI生成，Python成为AI时代第一语言，开源社区贡献创新高。", "url": "https://github.blog/2026-05-11-octoverse-ai-code-report/"},
            ]
        }
    },
    "2026-05-12": {
        "startup_board": {
            "companies": [
                {"name": "OpenAI", "field": "大模型", "route": "与News Corp签署每年10亿美元内容授权协议", "funding": "年化营收150亿美元", "verdict": "从'免费抓取'到'付费授权'，OpenAI带头规范训练数据来源"},
                {"name": "Tesla/Optimus", "field": "人形机器人", "route": "丰田订购500台Optimus，首次外部订单", "funding": "订单排至2028年", "verdict": "从自用到对外销售，Optimus完成了商业化的关键一步"},
                {"name": "Databricks", "field": "数据+AI平台", "route": "完成100亿美元融资，估值2000亿美元", "funding": "100亿美元融资创AI基础设施纪录", "verdict": "'数据竞赛'叙事获得资本认可，数据质量+AI的飞轮效应"},
                {"name": "腾讯Robotics X", "field": "双足机器人", "route": "'天鹅'机器人行走能效超越人类", "funding": "腾讯自研", "verdict": "被动动力学设计实现了超低能耗，为长续航双足机器人提供了新思路"},
            ],
            "trend": "AI训练数据走向'付费授权'时代；人形机器人开始获外部商业订单；数据平台估值飙升验证'AI从模型竞赛转向数据竞赛'"
        },
        "pm_board": {
            "insights": [
                {"title": "AI训练数据付费化：产品成本的重新计算", "content": "OpenAI每年10亿美元购买新闻内容授权——这标志着AI产品的成本结构将发生根本变化。产品经理需要将'数据授权成本'纳入产品定价模型，特别是涉及新闻、出版、图片等版权密集型领域的AI产品。"},
                {"title": "Demis Hassabis的AGI预言：产品路线图如何对齐?", "content": "DeepMind CEO预言AGI将在5年内实现。虽然时间线有争议，但产品经理应该开始思考：如果你的产品路线图规划到2031年，假设AGI真的出现，你的产品定位是什么？"},
                {"title": "AI监管碎片化：全球产品的合规噩梦", "content": "G7未能就AI治理达成统一框架，美欧分歧严重。对于面向全球市场的AI产品，这意味着需要应对多套不同的监管体系，合规成本将大幅上升。"},
            ],
            "focus": ["AI训练数据成本模型", "AGI假设下的产品规划", "全球AI监管合规策略", "人形机器人定价策略"]
        },
        "algo_board": {
            "insights": [
                {"title": "VASA-2：从照片+音频到超真实视频", "content": "微软VASA-2仅需一张照片和一段音频即可生成超真实说话视频。技术关键：解耦的面部动态建模(表情+唇形+头部姿态独立控制)+扩散模型生成+时序一致性约束。", "url": "https://www.microsoft.com/en-us/research/project/vasa-2/"},
                {"title": "GraphCast 3：AI天气预报超越传统数值模型", "content": "DeepMind GraphCast 3将10天天气预报准确率提升至超越ECMWF传统模型。技术进化：从确定性预测到概率预测，极端天气预警提前量从3天延长至7天。"},
            ],
            "tech_radar": [
                {"direction": "AI训练数据合规", "status": "成为必须", "advice": "版权授权协议将成为AI模型训练的标准前置条件"},
                {"direction": "超真实AI生成视频", "status": "技术突破", "advice": "VASA-2级技术引发深度伪造担忧，需要检测技术跟进"},
                {"direction": "AI天气预报", "status": "超越传统方法", "advice": "GraphCast 3证明AI在物理模拟上可超越数值方法"},
                {"direction": "被动动力学机器人", "status": "研究前沿", "advice": "腾讯'天鹅'展示了能效优化的新路径"},
            ],
            "focus": ["AI生成内容检测", "AI物理模拟", "机器人能效优化", "数据版权追踪技术"]
        },
        "projmgr_board": {
            "insights": [
                {"title": "AI数据合规成为项目管理新维度", "content": "OpenAI的内容授权协议、欧盟AI水印标准、G7治理分歧——项目经理需要将'数据合规'作为独立的项目工作流来管理，包括数据来源审计、授权追踪、合规报告。"},
                {"title": "100亿美元融资：AI基础设施项目进入'重资本'时代", "content": "Databricks的100亿美元融资显示AI基础设施项目的资本密集度正在向传统基础设施(电力/交通)看齐。项目管理需要引入大型基建项目的方法论：分阶段交付、风险对冲、长期ROI评估。"},
            ],
            "focus": ["AI数据合规管理", "大型AI项目融资策略", "多国监管合规路径", "AI基础设施项目交付方法"]
        },
        "action_items": {
            "tech_selection": ["训练数据合规：优先评估已获授权的数据集", "AI视频生成：关注VASA-2等技术的正面应用(教育/客服)", "天气预报：GraphCast 3已开源，适合气象相关项目"],
            "track_judgment": ["AI训练数据从'免费午餐'变为'付费大餐'，预算规划需提前考虑", "人形机器人商业化验证阶段已过，进入规模增长期"],
            "watch_list": ["OpenAI下一步版权协议(出版社/图库)", "G7后续AI治理协调", "Optimus丰田工厂交付进展", "Databricks IPO时间表"]
        },
        "hermes_board": {
            "insights": [
                {"title": "AI Agent的'数据合规'挑战", "content": "随着AI训练数据走向付费授权，AI Agent(包括Hermes Agent)也需要建立数据来源追踪机制。未来Agent生成的内容可能需要对训练数据来源进行标注和版权归属声明。"},
                {"title": "AGI时间表对Agent平台的影响", "content": "Demis Hassabis预言AGI 5年内实现——如果成真，Agent平台将从'辅助工具'升级为'主要工作界面'。Hermes Agent应持续提升自主决策和多Agent协作能力以迎接这一转变。"},
            ],
            "tech_stack": [
                {"title": "AI内容水印/溯源技术", "content": "C2PA标准+区块链溯源将成为AI生成内容的标配，Agent平台需要集成相关能力。", "url": "https://ec.europa.eu/commission/presscorner/detail/en/ip_26_2345"},
            ],
            "community": [
                {"title": "G7 AI治理分歧", "content": "美欧在AI监管上分歧严重，全球AI治理'碎片化'加剧，企业合规成本上升。", "url": "https://www.reuters.com/world/g7-ai-governance-failure-2026-05-12/"},
            ]
        }
    },
    "2026-05-13": {
        "startup_board": {
            "companies": [
                {"name": "OpenAI", "field": "大模型", "route": "Sam Altman确认GPT-6已启动训练", "funding": "年化营收150亿美元", "verdict": "GPT-6将是OpenAI在营收未达标压力下的关键一击，成败影响AI行业格局"},
                {"name": "华为", "field": "AI芯片", "route": "昇腾910C国内市场份额突破30%", "funding": "自研", "verdict": "在美国芯片管制下，华为昇腾成中国AI芯片自给率提升的最大推手"},
                {"name": "Anthropic", "field": "大模型", "route": "Claude 4.5 Sonnet，SWE-bench达65%", "funding": "估值1万亿美元", "verdict": "编程能力持续领先，Claude Code生态是企业市场核心壁垒"},
                {"name": "字节跳动", "field": "大模型/AI应用", "route": "豆包日活突破5亿，超越ChatGPT", "funding": "自研", "verdict": "豆包借助中国市场和东南亚扩张成为全球日活最高的AI应用"},
            ],
            "trend": "OpenAI启动GPT-6军备竞赛继续；中国AI芯片自给率突破35%；欧盟强制水印标准2027年生效，全球AI治理进入'执法阶段'"
        },
        "pm_board": {
            "insights": [
                {"title": "GPT-6来了：产品经理的备战清单", "content": "Sam Altman确认GPT-6已启动训练，暗示推理、多模态和Agent能力将有'质的飞跃'。产品经理应：1) 预留架构扩展空间以适应新模型能力；2) 评估GPT-6可能颠覆的产品假设；3) 建立模型能力监控机制以快速切换。"},
                {"title": "豆包5亿日活的启示：AI产品如何破圈", "content": "字节跳动豆包日活突破5亿超过ChatGPT，关键在于：1) 深度集成到抖音/头条等超级App；2) 免费+增值的定价策略；3) 本土化的AI人格设计。'AI不是独立产品，而是现有产品的增强层'这一策略被验证成功。"},
                {"title": "AI内容强制水印：产品合规倒计时", "content": "欧盟宣布2027年起所有AI生成内容必须嵌入C2PA水印，违者罚全球营收6%。面向欧洲市场的AI产品需要从现在开始规划水印集成，这不是'可选项'而是'生存条件'。"},
            ],
            "focus": ["GPT-6对产品路线图的影响", "AI产品的破圈增长策略", "欧盟AI水印合规准备", "中国AI芯片生态评估"]
        },
        "algo_board": {
            "insights": [
                {"title": "Claude 4.5 Sonnet的编程能力突破", "content": "SWE-bench得分65%，新增多文件重构和跨仓库代码理解。技术改进涉及：更大的代码预训练语料+改进的仓库级上下文编码+多文件编辑的规划能力。", "url": "https://www.anthropic.com/news/claude-4-5-sonnet"},
                {"title": "GPT-6预期：可能的架构演进方向", "content": "基于已知趋势推测GPT-6可能的技术方向：1) 原生多模态(文本+图像+视频+音频统一token化)；2) 超长上下文(百万→千万级)；3) Agent原生能力(工具调用作为一等公民)；4) 推理时间的自适应计算(简单问题少算，难问题多算)。"},
            ],
            "tech_radar": [
                {"direction": "编程Agent(SWE-bench)", "status": "持续突破(65%)", "advice": "Claude Code领先，开源方案快速追赶"},
                {"direction": "AI水印(C2PA)", "status": "强制标准化", "advice": "2027年欧盟强制，所有AI产品需提前集成"},
                {"direction": "中国AI芯片", "status": "自给率35%", "advice": "华为昇腾+壁仞+寒武纪三足鼎立"},
                {"direction": "人形机器人马拉松", "status": "即将举办", "advice": "北京6月全球首赛，考验机器人综合运动能力"},
            ],
            "focus": ["编程Agent评测基准", "AI水印/C2PA实现", "中国AI芯片性能评估", "多模态统一架构"]
        },
        "projmgr_board": {
            "insights": [
                {"title": "GPT-6训练启动=算力需求新一轮暴涨", "content": "GPT-6的训练预计需要数万张H200/B200级别GPU运行数月。项目管理者应：1) 预期2026H2-2027H1算力租赁价格可能上涨；2) 提前锁定长期算力合同；3) 探索国产AI芯片替代方案。"},
                {"title": "欧盟AI水印2027强制：项目合规路线图", "content": "距2027年1月仅剩8个月——需要：Q2完成技术评估→Q3完成C2PA集成→Q4完成合规测试。任何面向欧洲市场的AI产品都应该将此作为最高优先级的合规项目。"},
            ],
            "focus": ["算力资源规划(应对GPT-6)", "欧盟AI水印合规项目", "国产AI芯片替代评估", "人形机器人项目管理"]
        },
        "action_items": {
            "tech_selection": ["编程Agent：Claude 4.5 Sonnet(闭源最强)+开源备选", "AI水印合规：立即评估C2PA集成方案", "国产AI芯片：华为昇腾910C+壁仞BR200", "AI应用：参考豆包的'超级App集成'策略"],
            "track_judgment": ["GPT-6将在2026H2/2027H1发布，提前预留架构升级空间", "欧盟AI水印标准将成为事实上的全球标准，提前合规=先发优势", "中国AI芯片自给率将持续提升，2027年可能突破50%"],
            "watch_list": ["GPT-6训练进展和发布时间", "欧盟AI水印标准实施细则", "北京人形机器人马拉松结果", "华为昇腾910C生态扩展", "NVIDIA RTX 6090消费级AI算力"]
        },
        "hermes_board": {
            "insights": [
                {"title": "GPT-6时代的Agent平台准备", "content": "随着GPT-6等更强模型的到来，AI Agent将进入'高自主性'阶段。Hermes Agent的架构设计(多模型支持+工具调用+skill系统+内存管理)为迎接更强模型做好了准备。"},
                {"title": "C2PA水印标准与Agent生成内容的合规", "content": "欧盟强制AI水印将影响所有AI Agent平台。Hermes Agent需要考虑在生成内容中嵌入可追溯标识，确保用户使用Agent生成的文本/代码符合未来合规要求。"},
                {"title": "Hermes Agent的持续进化", "content": "Hermes Agent社区活跃，skill系统日益完善(500+内置技能)，多平台连接能力(TUI/CLI/Telegram/Discord/Slack/WeChat/QQ)领先业界，持续巩固作为'AI Agent操作系统'的定位。"},
            ],
            "tech_stack": [
                {"title": "C2PA AI内容水印标准", "content": "Adobe/Microsoft/Google等联合制定的AI内容溯源标准，2027年欧盟强制实施。", "url": "https://c2pa.org/"},
                {"title": "Claude 4.5 Sonnet API", "content": "最新编程Agent能力(SWE-bench 65%)，适合集成到Agent平台的代码生成流程。", "url": "https://www.anthropic.com/news/claude-4-5-sonnet"},
            ],
            "community": [
                {"title": "CoRL 2026投稿量暴涨3倍", "content": "机器人学习顶会投稿量达6000篇，具身智能成最热AI方向，会议扩容至万人规模。", "url": "https://www.corl2026.org/news/submission-record"},
            ]
        }
    },
}

# Patch each day's JSON file
for date, board_data in boards.items():
    filepath = os.path.join(DATA_DIR, f"{date}.json")
    if not os.path.exists(filepath):
        print(f"⚠️  {date}.json not found, skipping")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Add all role-specific boards
    data[date].update(board_data)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    keys = list(data[date].keys())
    print(f"✅ {date}: {len(keys)} keys now ({', '.join(keys[:5])}...)")

print("\nDone! Now rebuild with node build.js")
