# jammyfu / PaintingCoder

**使えるツール、遊べるゲーム、再利用できる AI ワークフローを作る。**

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

アイデアを、確認・実行・利用できる形にする実用的なツールを開発しています。公開プロジェクトは AI を活用したゲーム開発、組版、ComfyUI のワークフロー、オープンソース探索が中心です。

[↓ 代表作品](#selected-work) · [↓ その他の公開プロジェクト](#public-projects)

<a id="selected-work"></a>
## 代表作品

| プレビュー | プロジェクトと実装 |
| --- | --- |
| **[Open Game Skills · PunchBox Fighter](https://github.com/jammyfu/open-game-skills)**<br><br><a href="https://github.com/jammyfu/open-game-skills"><img src="https://raw.githubusercontent.com/jammyfu/open-game-skills/cdd133e8fd71b45fb519c49cd3532b1bed3ec83c/docs/open_game_logo.png" width="140" alt="Open Game Skills"></a><br><a href="https://raw.githubusercontent.com/jammyfu/open-game-skills/cdd133e8fd71b45fb519c49cd3532b1bed3ec83c/docs/showcase/punchbox-fighter-finisher-flame.gif"><img src="https://raw.githubusercontent.com/jammyfu/open-game-skills/cdd133e8fd71b45fb519c49cd3532b1bed3ec83c/docs/showcase/punchbox-fighter-finisher-flame.gif" width="140" alt="公開スキルリポジトリの PunchBox Fighter 録画。リアルタイム生成ではありません。"></a> | **スキルを説明するだけでなく、ゲームで示す。** · スキル集 + ゲーム例<br><br>Agent Skills · Python · ゲーム開発ワークフロー<br>[**プロジェクトを見る →**](https://github.com/jammyfu/open-game-skills) · [実装を見る](https://github.com/jammyfu/open-game-skills/tree/main/skills) |
| **[The Legend of Trump · 白宫奇遇记](https://github.com/jammyfu/TheLegendOfTrump)**<br><br><a href="assets/trump-live-intro.jpg"><img src="assets/trump-live-intro.jpg" width="140" alt="実機のオープニング：ホワイトハウスへ向かうヘリコプター。"></a> | **世界づくりから戦闘まで、遊べるブラウザー冒険ゲームに。** · アプリ / プレイ可能な作品<br><br>React · TypeScript · Three.js / R3F · WebGL<br>[**プロジェクトを見る →**](https://github.com/jammyfu/TheLegendOfTrump) · [実装を見る](https://github.com/jammyfu/TheLegendOfTrump/tree/main/src/game) |
| **[MagMark](https://github.com/jammyfu/MagMark)**<br><br><a href="assets/magmark-live.jpg"><img src="assets/magmark-live.jpg" width="140" alt="実際の画面と収録済みのデモです。UI の言語は原画面のままです。画像をクリックすると元の画像を開けます。"></a> | **Markdown を実際に使える誌面へ。** · アプリ / プレイ可能な作品<br><br>TypeScript · エディター UX · 描画と書き出し<br>[**プロジェクトを見る →**](https://github.com/jammyfu/MagMark) · [実装を見る](https://github.com/jammyfu/MagMark/tree/main/src) |
| **[Xiangsheng Genealogy · 相声家谱](https://github.com/jammyfu/xiangsheng-genealogy)**<br><br><a href="https://raw.githubusercontent.com/jammyfu/xiangsheng-genealogy/5dd9860199b2f341cd7ea027a5cfdb5f0607db7a/docs/qa/layered-scroll-fullscreen.png"><img src="https://raw.githubusercontent.com/jammyfu/xiangsheng-genealogy/5dd9860199b2f341cd7ea027a5cfdb5f0607db7a/docs/qa/layered-scroll-fullscreen.png" width="140" alt="実際の巻物 UI：世代、人物名、師弟関係を表示。"></a> | **文化資料を探索できるインタラクティブ作品へ。** · インタラクティブ可視化<br><br>React · Three.js · TypeScript · 構造化データ<br>[**プロジェクトを見る →**](https://github.com/jammyfu/xiangsheng-genealogy) · [実装を見る](https://github.com/jammyfu/xiangsheng-genealogy/tree/main/data) |
| **[ComfyUI PaintingCoderUtils](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils)**<br><br><a href="https://raw.githubusercontent.com/jammyfu/ComfyUI_PaintingCoderUtils/ccf81d94fecd805bb57fe5764c29cab17af01aa4/docs/images/image_resolution_adjuster01.png"><img src="https://raw.githubusercontent.com/jammyfu/ComfyUI_PaintingCoderUtils/ccf81d94fecd805bb57fe5764c29cab17af01aa4/docs/images/image_resolution_adjuster01.png" width="140" alt="実際の画面と収録済みのデモです。UI の言語は原画面のままです。画像をクリックすると元の画像を開けます。"></a> | **創作の繰り返し作業を減らす小さなツール。** · AI ワークフロー統合<br><br>Python · 画像ワークフロー · 統合の使いやすさ<br>[**プロジェクトを見る →**](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils) · [実装を見る](https://github.com/jammyfu/ComfyUI_PaintingCoderUtils/tree/main/workflow) |

<details>
<summary>Open Game Skills · 詳細と範囲</summary>

開発タスクに応じて専門スキルとエンジンアダプターを選択。公開例の PunchBox Fighter はヒットストップ、カウンター、コンボ表示、フィニッシュ演出を備えます。アニメーションとリギングの実装例も含む再利用可能なスキル集で、ゲームエンジンではありません。

</details>

<details>
<summary>The Legend of Trump · 詳細と範囲</summary>

AI と協力して開発したローポリゴン 3D 冒険ゲーム。探索、剣・盾・弓、敵の行動、ボス戦、マウス・キーボードとタッチ操作を実装。公開リポジトリでシミュレーション、UI、アセット、ブラウザーテストを確認できます。非公式の独立作品であり、ライセンスを受けたリメイクではありません。

</details>

<details>
<summary>MagMark · 詳細と範囲</summary>

中国語と欧文の混植に対応するブラウザーエディター。ページプレビュー、PNG、印刷 / PDF、WeChat 向けリッチテキストの出力経路と制約を分けています。現在はベータ版で、利用環境と公開先での確認が必要です。

</details>

<details>
<summary>Xiangsheng Genealogy · 詳細と範囲</summary>

水墨風の巻物、3D の師弟関係、検索と人物情報を、構造化した人物・関係・出典データにつなげます。異説のある関係には印を残し、資料整理を確定史実として扱いません。

</details>

<details>
<summary>ComfyUI PaintingCoderUtils · 詳細と範囲</summary>

画像サイズ、テキスト整形、マスク、ワークフロー修復用の ComfyUI カスタムノード。画像だけでなく、サンプル JSON と移行用修復ツールを提供します。

</details>

<sub>実際の画面と収録済みのデモです。UI の言語は原画面のままです。画像をクリックすると元の画像を開けます。</sub>

<a id="public-projects"></a>
## その他の公開プロジェクト

アプリ、ゲーム、再利用可能なスキル、調査カタログを分け、それぞれの価値と範囲を示します。

| プロジェクト | 示す技術 / 現在の範囲 |
| --- | --- |
| [github-risers](https://github.com/jammyfu/github-risers) | 1 日当たりの Star 増加で探すランキング。計算規則、履歴、多言語出力を公開。 |
| [reverse-engineering-atlas](https://github.com/jammyfu/reverse-engineering-atlas) | 技術とプラットフォーム別に整理したリバースエンジニアリング資料。出典と能力の限界を明記。 |
| [awesome-ai-model-showcases](https://github.com/jammyfu/awesome-ai-model-showcases) | 出典付きの AI 作品ギャラリー。ここでの取り組みはカタログと閲覧体験の構築であり、掲載作品は各作者に帰属します。 |
| [TokenSpeedSimulator](https://github.com/jammyfu/TokenSpeedSimulator) | ブラウザー上の A/B テキスト再生で tokens/s の体感を説明。モデルの実測ベンチマークではありません。 |
| [bitmap-vector-studio](https://github.com/jammyfu/bitmap-vector-studio) | VTracer を使うラスター・ベクター変換ツール。デスクトップ、CLI、API を統合し、独自のトレースエンジンは主張しません。 |
| [local-tool-skill](https://github.com/jammyfu/local-tool-skill) | ローカルのブラウザーツール向け Agent Skill と TypeScript テンプレート。証明写真のサイズ調整や印刷レイアウトを含みます。 |
| [llm_gpu_toolkit](https://github.com/jammyfu/llm_gpu_toolkit) | Ollama のモデル情報と概算 VRAM を整理。選定の参考であり、ハードウェアの実測ではありません。 |
| [hf-download-list](https://github.com/jammyfu/hf-download-list) | CLI と Web UI で Hugging Face のモデルファイル URL を列挙。重みをダウンロードするツールではありません。 |
| [MiiAIPlaza](https://github.com/jammyfu/MiiAIPlaza) | 既存の Mii エディターを拡張した AI エージェント広場の実験。mock / fixture 表示であり、オンラインのマルチプレイではありません。 |
| [photo-spec-library](https://github.com/jammyfu/photo-spec-library) | 出典付きの証明写真規格を JSON と Schema に整理。不明な要件を補わず、審査通過も保証しません。 |
| [awesome-game-assets](https://github.com/jammyfu/awesome-game-assets) | 元のプレビュー、用途、ライセンス情報でゲーム素材を整理。作品は各作者に帰属します。 |
| [practical-oss](https://github.com/jammyfu/practical-oss) | 用途、ワークフロー上の位置、ライセンスを整理するオープンソース調査。掲載ツールの作者であるとは主張しません。 |

[**公開ポートフォリオ →**](https://github.com/jammyfu?tab=repositories)
