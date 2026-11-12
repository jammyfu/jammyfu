# jammyfu / PaintingCoder

**I build tools you can use, games you can play, and workflows you can reuse.**

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

I build practical tools that turn an idea into something people can inspect, run, and use. My public work spans AI-assisted game development, publishing software, ComfyUI workflows, and open-source discovery.

[↓ Selected work](#selected-work) · [↓ More public projects](#public-projects)

<a id="selected-work"></a>
## Selected work

### [Open Game Skills · PunchBox Fighter](https://github.com/jammyfu/open-game-skills)

<a href="https://github.com/jammyfu/open-game-skills"><img src="https://raw.githubusercontent.com/jammyfu/open-game-skills/cdd133e8fd71b45fb519c49cd3532b1bed3ec83c/docs/open_game_logo.png" width="640" alt="Open Game Skills"></a>

**From reusable agent skills to a fighting-game result.** · Skill pack + example game

<a href="https://raw.githubusercontent.com/jammyfu/open-game-skills/cdd133e8fd71b45fb519c49cd3532b1bed3ec83c/docs/showcase/punchbox-fighter-finisher-flame.gif"><img src="https://raw.githubusercontent.com/jammyfu/open-game-skills/cdd133e8fd71b45fb519c49cd3532b1bed3ec83c/docs/showcase/punchbox-fighter-finisher-flame.gif" width="880" alt="Recorded PunchBox Fighter finisher from the public skill repository, not live generation."></a>

Game-development tasks are routed to specialized skills and engine adapters. PunchBox Fighter is a publicly documented example of the workflow: hitstop, counter hits, combo feedback and finisher cinematics. The skill pack also includes inspectable animation and rigging examples; it is not a game engine.

Agent Skills · Python · game-development workflows

[**View project →**](https://github.com/jammyfu/open-game-skills) · [Inspect implementation](https://github.com/jammyfu/open-game-skills/tree/main/skills)

### [The Legend of Trump · 白宫奇遇记](https://github.com/jammyfu/TheLegendOfTrump)

**A browser adventure, from world-building to combat.** · Application / playable project

<a href="https://raw.githubusercontent.com/jammyfu/TheLegendOfTrump/7e154883b561920093376d0b2de7595c61448dc7/artifacts/boss-summoned-guards.png"><img src="https://raw.githubusercontent.com/jammyfu/TheLegendOfTrump/7e154883b561920093376d0b2de7595c61448dc7/artifacts/boss-summoned-guards.png" width="880" alt="Actual boss encounter: targeting, guards and combat HUD."></a>

AI-assisted development of a playable low-poly 3D adventure: exploration, sword/shield and bow combat, enemy behavior, a boss encounter, keyboard/mouse and touch controls. The public repository exposes simulation code, UI, assets and browser tests. An independent unofficial game, not a licensed remake.

React · TypeScript · Three.js / R3F · WebGL

[**View project →**](https://github.com/jammyfu/TheLegendOfTrump) · [Inspect implementation](https://github.com/jammyfu/TheLegendOfTrump/tree/main/src/game)

### [MagMark](https://github.com/jammyfu/MagMark)

**From Markdown to a usable publication.** · Application / playable project

<a href="assets/magmark-live.jpg"><img src="assets/magmark-live.jpg" width="880" alt="Real running interfaces and recorded examples. Images preserve their original UI language; click to inspect the full-size source."></a>

A browser editor for Chinese and mixed-language typography, paginated previews, PNG output, print/PDF and WeChat rich text. Separate output paths make their constraints visible. Currently beta; target-browser and publishing checks still matter.

TypeScript · editor UX · rendering and export

[**View project →**](https://github.com/jammyfu/MagMark) · [Inspect implementation](https://github.com/jammyfu/MagMark/tree/main/src)

### [Xiangsheng Genealogy · 相声家谱](https://github.com/jammyfu/xiangsheng-genealogy)

**Make a cultural dataset feel explorable.** · Interactive visualization

<a href="https://raw.githubusercontent.com/jammyfu/xiangsheng-genealogy/5dd9860199b2f341cd7ea027a5cfdb5f0607db7a/docs/qa/layered-scroll-fullscreen.png"><img src="https://raw.githubusercontent.com/jammyfu/xiangsheng-genealogy/5dd9860199b2f341cd7ea027a5cfdb5f0607db7a/docs/qa/layered-scroll-fullscreen.png" width="880" alt="Actual landscape-scroll interface with generations and relationship labels."></a>

An interactive genealogy with an ink-landscape scroll, 3D relationship views, search and person details. It connects a visual interface to structured people, relationships and cited sources. Disputed historical relationships remain marked rather than presented as settled facts.

React · Three.js · TypeScript · structured data

[**View project →**](https://github.com/jammyfu/xiangsheng-genealogy) · [Inspect implementation](https://github.com/jammyfu/xiangsheng-genealogy/tree/main/data)

### [ComfyUI PaintingCoderUtils](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils)

**Small tools that remove friction from creative work.** · AI workflow integration

<a href="https://raw.githubusercontent.com/jammyfu/ComfyUI_PaintingCoderUtils/ccf81d94fecd805bb57fe5764c29cab17af01aa4/docs/images/image_resolution_adjuster01.png"><img src="https://raw.githubusercontent.com/jammyfu/ComfyUI_PaintingCoderUtils/ccf81d94fecd805bb57fe5764c29cab17af01aa4/docs/images/image_resolution_adjuster01.png" width="880" alt="Real running interfaces and recorded examples. Images preserve their original UI language; click to inspect the full-size source."></a>

Custom ComfyUI nodes for image dimensions, text cleanup, masks and workflow repair. Includes example workflow JSON and a migration fixer, rather than screenshots alone.

Python · image workflows · integration ergonomics

[**View project →**](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils) · [Inspect implementation](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils/tree/main/workflow)

<sub>Real running interfaces and recorded examples. Images preserve their original UI language; click to inspect the full-size source.</sub>

<a id="public-projects"></a>
## More public projects

Working software, reusable workflows, and research catalogs are different kinds of work. The sections below keep that distinction visible.

| Project | What it demonstrates / scope |
| --- | --- |
| [github-risers](https://github.com/jammyfu/github-risers) | Daily star-growth rankings with published calculation rules, archived snapshots and multilingual output. |
| [reverse-engineering-atlas](https://github.com/jammyfu/reverse-engineering-atlas) | Cross-platform reverse-engineering research, organized by technique and platform, with sources and capability limits. |
| [awesome-ai-model-showcases](https://github.com/jammyfu/awesome-ai-model-showcases) | A source-linked gallery of AI-made work. My contribution here is the catalog and browsing experience; the showcased works belong to their credited creators. |
| [TokenSpeedSimulator](https://github.com/jammyfu/TokenSpeedSimulator) | Browser A/B text-stream playback for explaining tokens/s; a simulation, not a model benchmark. |
| [bitmap-vector-studio](https://github.com/jammyfu/bitmap-vector-studio) | VTracer-based bitmap-to-vector tooling with desktop, CLI and API paths; builds on VTracer, not a new tracing engine. |
| [local-tool-skill](https://github.com/jammyfu/local-tool-skill) | Agent skill and TypeScript templates for local browser tools, including photo sizing and print sheets. |
| [llm_gpu_toolkit](https://github.com/jammyfu/llm_gpu_toolkit) | Ollama model data and rough GPU-memory estimates; a planning aid, not tested hardware performance. |
| [hf-download-list](https://github.com/jammyfu/hf-download-list) | Hugging Face model-file URL lists through CLI and web UI; lists links rather than downloading weights. |
| [MiiAIPlaza](https://github.com/jammyfu/MiiAIPlaza) | Experimental AI-agent plaza extending an upstream Mii editor; mock/fixture modes, not a live multiplayer service. |
| [photo-spec-library](https://github.com/jammyfu/photo-spec-library) | ID-photo requirements as sourced JSON and schemas; unknown requirements stay unset, no approval guarantee. |
| [awesome-game-assets](https://github.com/jammyfu/awesome-game-assets) | Game asset discovery with original previews and practical license notes; resources remain their creators’ work. |
| [practical-oss](https://github.com/jammyfu/practical-oss) | Purpose-organized open-source research, workflow fit and licensing notes; not authorship of listed tools. |

[**Full public portfolio →**](https://github.com/jammyfu?tab=repositories)
