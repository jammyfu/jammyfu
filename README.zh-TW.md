# jammyfu / PaintingCoder

**做能用的工具、能玩的遊戲，也做可重用的 AI 工作流程。**

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

我從實際需求出發製作工具，把想法轉為能檢視、能執行、能使用的成果。公開專案涵蓋 AI 輔助遊戲開發、內容排版、ComfyUI 工作流程與開源探索。

[↓ 代表作品](#selected-work) · [↓ 更多公開專案](#public-projects)

<a id="selected-work"></a>
## 代表作品

| 預覽 | 專案與實作 |
| --- | --- |
| <a href="https://github.com/jammyfu/open-game-skills"><img src="https://raw.githubusercontent.com/jammyfu/open-game-skills/cdd133e8fd71b45fb519c49cd3532b1bed3ec83c/docs/open_game_logo.png" width="220" alt="Open Game Skills"></a><br><a href="https://raw.githubusercontent.com/jammyfu/open-game-skills/cdd133e8fd71b45fb519c49cd3532b1bed3ec83c/docs/showcase/punchbox-fighter-finisher-flame.gif"><img src="https://raw.githubusercontent.com/jammyfu/open-game-skills/cdd133e8fd71b45fb519c49cd3532b1bed3ec83c/docs/showcase/punchbox-fighter-finisher-flame.gif" width="220" alt="公開 Skill 儲存庫中的 PunchBox Fighter 終結技錄影，並非即時生成。"></a> | **[Open Game Skills · PunchBox Fighter](https://github.com/jammyfu/open-game-skills)**<br>**不只寫 Skill，讓遊戲成果呈現工作流程。** · 技能集 + 遊戲範例<br><br>Agent Skills · Python · 遊戲開發工作流程<br>[**查看專案 →**](https://github.com/jammyfu/open-game-skills) · [查看實作](https://github.com/jammyfu/open-game-skills/tree/main/skills) |<br><details><summary>展開詳情與範圍</summary>依開發任務調度專業技能與遊戲引擎介接。PunchBox Fighter 是公開展示的工作流程範例，包含打擊停頓、反擊、連段回饋與終結技演出；工具包也提供可檢視的動畫和骨架綁定範例。這是可重用的開發技能集，不是遊戲引擎。</details>
| <a href="https://raw.githubusercontent.com/jammyfu/TheLegendOfTrump/7e154883b561920093376d0b2de7595c61448dc7/artifacts/boss-summoned-guards.png"><img src="https://raw.githubusercontent.com/jammyfu/TheLegendOfTrump/7e154883b561920093376d0b2de7595c61448dc7/artifacts/boss-summoned-guards.png" width="220" alt="實際頭目戰畫面：目標鎖定、守衛與戰鬥介面。"></a> | **[The Legend of Trump · 白宮奇遇記](https://github.com/jammyfu/TheLegendOfTrump)**<br>**從場景到戰鬥，做成能玩的瀏覽器冒險遊戲。** · 應用程式 / 可玩專案<br><br>React · TypeScript · Three.js / R3F · WebGL<br>[**查看專案 →**](https://github.com/jammyfu/TheLegendOfTrump) · [查看實作](https://github.com/jammyfu/TheLegendOfTrump/tree/main/src/game) |<br><details><summary>展開詳情與範圍</summary>AI 協作開發的低多邊形 3D 冒險：探索、劍盾與弓箭戰鬥、敵人行為、頭目戰，以及鍵盤滑鼠和觸控操作。公開儲存庫包含模擬邏輯、介面、素材與瀏覽器測試，是能檢視實作的遊戲專案，不只是一張概念圖。非官方獨立作品，並非授權重製版。</details>
| <a href="assets/magmark-live.jpg"><img src="assets/magmark-live.jpg" width="220" alt="以下均為實際執行畫面或範例錄影，保留原始介面語言。點選圖片可查看原始大圖。"></a> | **[MagMark](https://github.com/jammyfu/MagMark)**<br>**不只是預覽 Markdown，而是產出可用版面。** · 應用程式 / 可玩專案<br><br>TypeScript · 編輯器使用體驗 · 算繪與匯出<br>[**查看專案 →**](https://github.com/jammyfu/MagMark) · [查看實作](https://github.com/jammyfu/MagMark/tree/main/src) |<br><details><summary>展開詳情與範圍</summary>針對中文與中英混排的瀏覽器編輯器，提供分頁預覽、PNG、列印 / PDF 與微信公眾號格式化文字。各種輸出方式分別說明限制。目前仍為 beta，須在目標瀏覽器與發布環境驗證。</details>
| <a href="https://raw.githubusercontent.com/jammyfu/xiangsheng-genealogy/5dd9860199b2f341cd7ea027a5cfdb5f0607db7a/docs/qa/layered-scroll-fullscreen.png"><img src="https://raw.githubusercontent.com/jammyfu/xiangsheng-genealogy/5dd9860199b2f341cd7ea027a5cfdb5f0607db7a/docs/qa/layered-scroll-fullscreen.png" width="220" alt="實際山水長卷介面，呈現字輩、人物與師承關係。"></a> | **[Xiangsheng Genealogy · 相聲家譜](https://github.com/jammyfu/xiangsheng-genealogy)**<br>**讓文化資料成為可探索的互動作品。** · 互動視覺化<br><br>React · Three.js · TypeScript · 結構化資料<br>[**查看專案 →**](https://github.com/jammyfu/xiangsheng-genealogy) · [查看實作](https://github.com/jammyfu/xiangsheng-genealogy/tree/main/data) |<br><details><summary>展開詳情與範圍</summary>水墨山水長卷、三維師承視圖、搜尋與人物資料，將視覺互動連結至結構化人物、關係和引用來源。保留師承爭議標記，不把資料整理當作權威定論。</details>
| <a href="https://raw.githubusercontent.com/jammyfu/ComfyUI_PaintingCoderUtils/ccf81d94fecd805bb57fe5764c29cab17af01aa4/docs/images/image_resolution_adjuster01.png"><img src="https://raw.githubusercontent.com/jammyfu/ComfyUI_PaintingCoderUtils/ccf81d94fecd805bb57fe5764c29cab17af01aa4/docs/images/image_resolution_adjuster01.png" width="220" alt="以下均為實際執行畫面或範例錄影，保留原始介面語言。點選圖片可查看原始大圖。"></a> | **[ComfyUI PaintingCoderUtils](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils)**<br>**用小工具減少創作流程中的重複作業。** · AI 工作流程整合<br><br>Python · 影像工作流程 · 整合體驗<br>[**查看專案 →**](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils) · [查看實作](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils/tree/main/workflow) |<br><details><summary>展開詳情與範圍</summary>為 ComfyUI 提供影像尺寸、文字清理、遮罩與工作流程修復節點；附有工作流程 JSON 與版本遷移修復工具，不只是展示圖片。</details>

<sub>以下均為實際執行畫面或範例錄影，保留原始介面語言。點選圖片可查看原始大圖。</sub>

<a id="public-projects"></a>
## 更多公開專案

應用程式、遊戲、可重用技能與研究目錄各有不同價值，以下分別呈現，不將所有專案包裝成同一類成果。

| 專案 | 呈現的能力 / 目前限制 |
| --- | --- |
| [github-risers](https://github.com/jammyfu/github-risers) | 依每日新增 Star 探索專案，提供計算規則、歷史快照與多語內容。 |
| [reverse-engineering-atlas](https://github.com/jammyfu/reverse-engineering-atlas) | 依技術與平台整理跨平台逆向工程研究，保留來源與能力限制。 |
| [awesome-ai-model-showcases](https://github.com/jammyfu/awesome-ai-model-showcases) | 可追溯來源的 AI 作品集。這裡呈現的是目錄整理與瀏覽體驗，收錄作品屬於各自署名的創作者。 |
| [TokenSpeedSimulator](https://github.com/jammyfu/TokenSpeedSimulator) | 瀏覽器 A/B 文字串流示範，將 tokens/s 化為可感受的閱讀節奏；是模擬器，不是模型效能測試。 |
| [bitmap-vector-studio](https://github.com/jammyfu/bitmap-vector-studio) | 基於 VTracer 的點陣圖轉向量圖工具，整合桌面、CLI 與 API；並非自研描圖引擎。 |
| [local-tool-skill](https://github.com/jammyfu/local-tool-skill) | 用於本機瀏覽器工具的 Agent Skill 與 TypeScript 範本，包含證件照尺寸和列印排版流程。 |
| [llm_gpu_toolkit](https://github.com/jammyfu/llm_gpu_toolkit) | Ollama 模型資料整理與粗略顯示記憶體估算，供選型參考，不代表硬體實測效能。 |
| [hf-download-list](https://github.com/jammyfu/hf-download-list) | 透過 CLI 與網頁整理 Hugging Face 模型檔案連結，不直接下載模型權重。 |
| [MiiAIPlaza](https://github.com/jammyfu/MiiAIPlaza) | 以既有 Mii 編輯器為基礎擴充的 AI Agent 廣場實驗；目前為 mock / fixture 預覽，並非線上多人服務。 |
| [photo-spec-library](https://github.com/jammyfu/photo-spec-library) | 將證件照規格整理為有來源的 JSON 與 Schema；未明訂欄位保留未知，不保證審核通過。 |
| [awesome-game-assets](https://github.com/jammyfu/awesome-game-assets) | 以原專案預覽、用途和授權說明整理遊戲素材；素材作品歸各自創作者所有。 |
| [practical-oss](https://github.com/jammyfu/practical-oss) | 依用途整理開源專案、工作流程位置與授權資訊，呈現研究整理能力，而非上游工具作者身分。 |

[**完整公開作品集 →**](https://github.com/jammyfu?tab=repositories)
