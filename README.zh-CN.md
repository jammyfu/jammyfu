# jammyfu / PaintingCoder

**做能用的工具、能玩的游戏，也做可复用的 AI 工作流。**

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

我围绕真实任务构建工具：把想法变成可查看、可运行、可使用的成果。公开项目覆盖 AI 辅助游戏开发、内容排版、ComfyUI 工作流与开源发现。

[↓ 代表作品](#selected-work) · [↓ 更多公开项目](#public-projects)

<a id="selected-work"></a>
## 代表作品

### [The Legend of Trump · 白宫奇遇记](https://github.com/jammyfu/TheLegendOfTrump)

**从场景到战斗，做成能玩的浏览器冒险游戏。** · 应用 / 可玩项目

<a href="https://raw.githubusercontent.com/jammyfu/TheLegendOfTrump/7e154883b561920093376d0b2de7595c61448dc7/artifacts/boss-summoned-guards.png"><img src="https://raw.githubusercontent.com/jammyfu/TheLegendOfTrump/7e154883b561920093376d0b2de7595c61448dc7/artifacts/boss-summoned-guards.png" width="880" alt="真实 Boss 战画面：目标锁定、守卫与战斗界面。"></a>

AI 协作开发的低多边形 3D 冒险：探索、剑盾与弓箭战斗、敌人行为、Boss 战，以及键鼠和触屏操作。公开仓库包含模拟逻辑、界面、资产与浏览器测试，是可查看实现的完整游戏项目，而非一张概念图。非官方独立作品，不是授权重制版。

React · TypeScript · Three.js / R3F · WebGL

[**查看项目 →**](https://github.com/jammyfu/TheLegendOfTrump) · [查看实现](https://github.com/jammyfu/TheLegendOfTrump/tree/main/src/game)

### [Open Game Skills · PunchBox Fighter](https://github.com/jammyfu/open-game-skills)

**不只写 Skill，让游戏结果证明工作流。** · 技能集 + 游戏案例

<a href="https://raw.githubusercontent.com/jammyfu/open-game-skills/cdd133e8fd71b45fb519c49cd3532b1bed3ec83c/docs/showcase/punchbox-fighter-finisher-flame.gif"><img src="https://raw.githubusercontent.com/jammyfu/open-game-skills/cdd133e8fd71b45fb519c49cd3532b1bed3ec83c/docs/showcase/punchbox-fighter-finisher-flame.gif" width="880" alt="公开 Skill 仓库中的 PunchBox Fighter 终结技实录，并非现场生成。"></a>

按开发任务调度专业技能与引擎适配器。PunchBox Fighter 是公开展示的工作流案例，包含打击停顿、反击、连段反馈与终结技演出；工具包同时提供可检查的动画和绑定案例。它是可复用的开发技能集，不是游戏引擎。

Agent Skills · Python · game-development workflows

[**查看项目 →**](https://github.com/jammyfu/open-game-skills) · [查看实现](https://github.com/jammyfu/open-game-skills/tree/main/skills)

### [MagMark](https://github.com/jammyfu/MagMark)

**不止预览 Markdown，而是交付可用版面。** · 应用 / 可玩项目

<a href="assets/magmark-live.jpg"><img src="assets/magmark-live.jpg" width="880" alt="以下均为真实运行界面或案例实录，保留原始界面语言。点击图片可查看原始大图。"></a>

面向中文与中英混排的浏览器编辑器，提供分页预览、PNG、打印 / PDF 与公众号富文本。不同输出路径明确区分限制。目前仍是 beta，目标浏览器和发布环节需要验收。

TypeScript · 编辑器体验 · 渲染与导出

[**查看项目 →**](https://github.com/jammyfu/MagMark) · [查看实现](https://github.com/jammyfu/MagMark/tree/main/src)

### [Xiangsheng Genealogy · 相声家谱](https://github.com/jammyfu/xiangsheng-genealogy)

**让文化资料变成可探索的交互作品。** · 交互可视化

<a href="https://raw.githubusercontent.com/jammyfu/xiangsheng-genealogy/5dd9860199b2f341cd7ea027a5cfdb5f0607db7a/docs/qa/layered-scroll-fullscreen.png"><img src="https://raw.githubusercontent.com/jammyfu/xiangsheng-genealogy/5dd9860199b2f341cd7ea027a5cfdb5f0607db7a/docs/qa/layered-scroll-fullscreen.png" width="880" alt="真实山水长卷界面，呈现字辈、人物与师承关系。"></a>

水墨山水长卷、三维师承视图、检索与人物资料，把视觉交互连接到结构化人物、关系及引用来源。对存在争议的师承保留标记，不把资料整理冒充权威定论。

React · Three.js · TypeScript · structured data

[**查看项目 →**](https://github.com/jammyfu/xiangsheng-genealogy) · [查看实现](https://github.com/jammyfu/xiangsheng-genealogy/tree/main/data)

### [ComfyUI PaintingCoderUtils](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils)

**用小工具消除创作流程里的重复劳动。** · AI 工作流集成

<a href="https://raw.githubusercontent.com/jammyfu/ComfyUI_PaintingCoderUtils/ccf81d94fecd805bb57fe5764c29cab17af01aa4/docs/images/image_resolution_adjuster01.png"><img src="https://raw.githubusercontent.com/jammyfu/ComfyUI_PaintingCoderUtils/ccf81d94fecd805bb57fe5764c29cab17af01aa4/docs/images/image_resolution_adjuster01.png" width="880" alt="以下均为真实运行界面或案例实录，保留原始界面语言。点击图片可查看原始大图。"></a>

为 ComfyUI 提供图像尺寸、文本清理、遮罩与工作流修复节点；附带工作流 JSON 和迁移修复工具，不只展示效果图。

Python · 图像工作流 · 集成体验

[**查看项目 →**](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils) · [查看实现](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils/tree/main/workflow)

<sub>以下均为真实运行界面或案例实录，保留原始界面语言。点击图片可查看原始大图。</sub>

<a id="public-projects"></a>
## 更多公开项目

应用、游戏、可复用技能与研究目录承担不同价值，下面分别展示，不把所有项目都包装成同一种成果。

| 项目 | 体现的能力 / 当前边界 |
| --- | --- |
| [github-risers](https://github.com/jammyfu/github-risers) | 按每日新增 Star 发现项目，公开计算规则、历史快照与多语言结果。 |
| [reverse-engineering-atlas](https://github.com/jammyfu/reverse-engineering-atlas) | 按技术和平台组织跨平台逆向研究，保留来源与能力边界。 |
| [awesome-ai-model-showcases](https://github.com/jammyfu/awesome-ai-model-showcases) | 可追溯来源的 AI 作品展厅。这里体现的是目录整理与浏览体验建设，收录作品归署名创作者所有。 |
| [TokenSpeedSimulator](https://github.com/jammyfu/TokenSpeedSimulator) | 浏览器 A/B 文字流演示，把 tokens/s 变成可感受的阅读节奏；是模拟器，不是模型跑分。 |
| [bitmap-vector-studio](https://github.com/jammyfu/bitmap-vector-studio) | 基于 VTracer 的位图转矢量工具，连接桌面、CLI 与 API；不是自研描摹引擎。 |
| [local-tool-skill](https://github.com/jammyfu/local-tool-skill) | 面向本地浏览器工具的 Agent Skill 与 TypeScript 模板，包含证件照尺寸和打印排版流程。 |
| [llm_gpu_toolkit](https://github.com/jammyfu/llm_gpu_toolkit) | Ollama 模型资料整理与粗略显存估算，用于选型参考，不代表真实硬件性能。 |
| [hf-download-list](https://github.com/jammyfu/hf-download-list) | 通过 CLI 和网页整理 Hugging Face 模型文件链接，不直接下载模型权重。 |
| [MiiAIPlaza](https://github.com/jammyfu/MiiAIPlaza) | 基于上游 Mii 编辑器扩展的 AI Agent 广场实验；目前是 mock / fixture 预览，不是在线多人服务。 |
| [photo-spec-library](https://github.com/jammyfu/photo-spec-library) | 把证件照要求整理成有来源的 JSON 和 Schema，缺失字段保持未知，不保证审核通过。 |
| [awesome-game-assets](https://github.com/jammyfu/awesome-game-assets) | 以原项目预览、用途与许可说明组织游戏素材；素材作品归各自创作者。 |
| [practical-oss](https://github.com/jammyfu/practical-oss) | 按用途梳理开源项目、工作流位置和许可信息，体现研究整理，而非上游工具作者身份。 |

[**完整公开作品集 →**](https://github.com/jammyfu?tab=repositories)
