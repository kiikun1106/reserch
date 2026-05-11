# 翻訳判断記録（Translation Log）

OECD Education Working Papers No. 316  
*Innovative Tools for the Direct Assessment of Social and Emotional Skills*  
日本語訳プロジェクト

---

## 1. 全体方針

### 文体
- **である調**で統一。論文・政策文書として一貫性を担保。
- ですます調混入チェックは QC スクリプト（`qc/qc_check.py`）で全章自動検出。全章で混入0。

### 文法
- 英語の受動態は、日本語として自然な場合は能動態に転換。例：「participants are presented with...」→「参加者には…が提示される」（受動維持が自然）／「researchers measured...」→「研究者らは…を測定した」（能動転換）。
- 一文が長い英語学術文は、日本語では2〜3文に分割。比率は QC で原文1文：訳文1.0〜2.5文の範囲で安定。

### 用語
- CLAUDE.md の標準訳と `glossary.json`（99項目）を参照源として使用。
- 略語は初出時のみ正式名称＋カタカナ／日本語訳を併記。
  例：「OECD生徒の学習到達度調査（Programme for International Student Assessment: PISA）」、2回目以降は「PISA」。
- テスト・課題・ゲームの固有名詞は原語維持＋初出時のみ日本語名称併記。
  例：「Emotional Stroop task（情動ストループ課題）」、「Multifaceted Empathy Test（MET、多面的共感検査）」。

---

## 2. 用語選定の主要判断

### 2.1 OECD SES 5領域

OECD既訳・国立教育政策研究所『社会情動的スキル：学びに向かう力』(明石書店, 2018) を参照。

| 原語 | 採用訳 | 代替候補 | 採用理由 |
|---|---|---|---|
| Task performance | 課題遂行 | タスク遂行 | OECD既訳の慣行 |
| Emotion regulation | 情動制御 | 情動調整 | 心理学定訳 |
| Collaboration | 協働 | 協調・コラボレーション | 教育心理学定訳 |
| Open-mindedness | 心の開放性 | 開放性 | OECDの「Big Five」由来訳 |
| Engaging with others | 他者との関与 | 他者との交わり | OECD既訳 |

### 2.2 信頼性・妥当性関連

心理測定学（テスト理論）の定訳に従う。

- `internal consistency` → 内的整合性
- `test-retest reliability` → 再検査信頼性
- `construct validity` → 構成概念妥当性
- `convergent validity` → 収束的妥当性
- `discriminant / divergent validity` → 弁別的妥当性
- `criterion validity` → 基準関連妥当性
- `concurrent validity` → 同時的妥当性
- `predictive validity` → 予測的妥当性
- `consequential validity` → 結果的妥当性（Messick由来、定訳が比較的新しい）
- `ecological validity` → 生態学的妥当性
- `fairness` → 公正性（CLAUDE.md準拠：equity 系の訳と整合）
- `measurement invariance` → 測定不変性

### 2.3 表記が揺れる用語の確定

| 原語 | 採用訳 | 不採用候補 | 採用理由 |
|---|---|---|---|
| empathy | 共感性 | 共感 | 名詞用法はスキルとしての「性」を含めるOECD訳に従う |
| co-operation | 協調性 | 協力 | OECD Big Five 派生のSESスキルとしては「協調性」 |
| trust | 信頼 | （ほぼ揺れなし） | — |
| grit | グリット（やり抜く力） | やり抜く力／気概 | Duckworthの原概念尊重、初出時のみ意味併記 |
| persistence | 粘り強さ | 忍耐 | OECD SES文脈の慣用 |
| optimism | 楽観性 | 楽観主義 | スキルとして測定対象の場合は「性」 |
| metacognition | メタ認知 | メタ認知能力 | 心理学定訳 |
| perspective-taking | 視点取得 | 他者視点取得・視点取り | 発達心理学定訳 |
| emotional intelligence | 情動知能 | 感情知能・EQ | Mayer–Saloveyモデル文脈では「情動知能」 |
| affective | 情動的 | 感情的 | 心理学定訳。テスト名（Affective Simon Task等）は原語維持 |
| stimuli | 刺激 | （定訳） | — |
| valence | 感情価／情動価 | 価 | 文脈で使い分け |
| reference bias | 参照バイアス | 比較基準バイアス | West et al.(2016)に対応する暫定訳。定訳未確立 |
| immediacy bias | 直近バイアス | 即時性バイアス | 同上 |

### 2.4 技術系用語

| 原語 | 採用訳 | 採用理由 |
|---|---|---|
| virtual reality (VR) | バーチャルリアリティ（VR） | カタカナが主流。本文中は「VR」 |
| augmented reality (AR) | 拡張現実（AR） | 定訳 |
| artificial intelligence (AI) | 人工知能（AI） | 定訳 |
| biophysiological measures | 生体生理指標 | 神経科学・心理生理学の慣用 |
| heart rate variability (HRV) | 心拍変動（HRV） | 生理学定訳 |
| electroencephalography (EEG) | 脳波（EEG） | 定訳 |
| eye tracking | 視線追跡（アイトラッキング） | 両表記併用 |
| machine learning | 機械学習 | 定訳 |
| digital footprints | デジタルフットプリント | カタカナ慣用 |
| affective computing | 情動コンピューティング | 学術慣用 |
| social signal processing | 社会的シグナル処理 | 直訳 |
| non-playable character (NPC) | ノンプレイヤーキャラクター（NPC） | ゲーム業界慣用 |
| stealth assessment | ステルス・アセスメント | 教育測定領域の新興定訳 |

### 2.5 検査・課題・ゲーム名

原則として **原語維持＋初出時のみ日本語訳併記**。

例：
- Emotional Stroop task → 情動ストループ課題
- Go/No-Go Task → Go/No-Go課題
- Mirror Tracing Frustration Task → ミラートレース・フラストレーション課題
- Reading the Mind in the Eyes Test → 心の理論—眼の写真検査（児童版）（RMET-C）
- MSCEIT-YV / Multifaceted Empathy Test / FERET / GERT / LEAS / SAT-MC / VESIP 等 → 略語＋正式名称＋初出時の日本語訳併記

ゲーム名（ZooU, Physics Playground, Circuit Runner, Questions Worlds, VESIP, Crystal Island, Nevermind, Simoland, Athenea, Faculty Game, Pizzagame, Poptropica, Minecraft）→ 原語維持。

---

## 3. 図表・コラム処理

CLAUDE.md ルール（Figure → 図、Table → 表、Box → コラム）に従う。

| 原文 | 訳出 |
|---|---|
| Figure 4.1 | 図4.1 |
| Table 6.1 | 表6.1 |
| Box 1.1 | コラム1.1 |
| Annex Table 1 | 付録表1 |
| (see Figure 4.2) | （図4.2を参照） |
| Note: | 注： |
| Source: | 出典： |

**画像のみの図（Table 4.1、Figure 4.1、Figure 4.6等）**: 訳注で「画像形式のため本ファイルには展開しない」と明記し、原文の参照を案内。

**図中テキスト**: 心理測定刺激語（"anger"、"joy" 等）は原語維持＋訳注（[原文: ...] 形式は本翻訳では訳注ブロックで処理）。

---

## 4. 引用・脚注処理

- 引用文献の[番号]マーカー（例：`Wigelsworth et al., 2010[11]`）は原文の位置・形式を完全保持。
- 文献年（2010, 2018等）は原文どおり。
- 脚注は本文中の番号で参照しつつ、本文後ろに `> **脚注N**: ...` 形式で配置。
- References セクション（PDF p.71–85、約500件）は **翻訳せず原文のまま** `output/references_raw.md` に転載。

---

## 5. 章ごとの主要な翻訳判断

### 第1章 序論
- コラム1.1 のOECD SES定義（7項目箇条書き）はOECD既訳に近い形で訳出。
- 「foundational cognitive processes」→「基礎的認知過程」、「academic skills」→「学習スキル」（OECD既訳）。

### 第2章
- §2.1 で5種のバイアスを列挙：social desirability bias → 社会的望ましさバイアス、immediacy bias → 直近バイアス、acquiescence bias → 黙従バイアス、memory bias → 記憶バイアス、reference bias → 参照バイアス。
- §2.2 SJTs：「situational judgement test」→「状況判断テスト」（産業心理学定訳）。STEU/STEM/SRC-AM の検査例文は和訳して提示し、選択肢符号(a)(b)(c)(d)は原文維持。

### 第3章
- 検索式（"social and emotional skills" 等の検索ターム）は **原語のまま** 維持。これは文献検索の再現性を担保するため。
- 検査・課題名の英文・「2015 cutoff」「6 years old」など数値は原文どおり。

### 第4章（最大、全34ページ）
- §4.1 Tasks：13スキルカテゴリーを順次提示。
- §4.2 Mixed batteries：SELweb (EE/LE) と MSCEIT/MSCEIT-YV。
- §4.3 Digital games：6ゲーム（ZooU, Physics Playground, Circuit Runner, Questions Worlds, VESIP, Simoland）を詳述。
- 「stealth assessment」→「ステルス・アセスメント」（カタカナ採用、初出時に意味解説併記）。

### 第5章
- §5.1 Biophysiological（3技術：HRV, eye tracking, cortisol）
- §5.2 VR/AR
- §5.3 AI applications（5.3.1 方法論、5.3.2 課題・倫理、5.3.3 結論）
- §5.4 Digital footprints
- 「Big Five」「HEXACO」モデル → 原語＋日本語名併記なし（パーソナリティ心理学の定訳カタカナ）。

### 第6章
- 表6.1・表6.2 は原文の箇条書きを Markdown 表に再構成（訳注で記載）。

### 第7章
- 1ページに収まる短い結論。「unified behaviour-based assessment」→「統合型行動ベースのアセスメント」。

### 付録A・B
- 付録A：OECD SES枠組み表（5領域＋補足）。Big Five系の括弧表記（Conscientiousness等）も訳出。
- 付録B：57ツールの一覧。**ツール名は原語維持**、DOIリンクはそのまま転載。

---

## 6. QCで検出された主な「未整合」とその扱い

QCスクリプト（`qc/qc_check.py`）は以下を自動検出：
1. 用語整合性（glossary との照合）
2. 文量比較（原文文数 vs 訳文文数）
3. ですます調混入
4. 数値の取りこぼし
5. 図表参照番号

**章確定可能（OK）判定**：第1章、第2章、第3章、第4章、第5章、第6章、付録A、付録B。

**章境界での偽陽性**：
- 第7章は §6.2 のスピルオーバー（PDF p.69前半に表6.2 続き）により「表参照欠落: 6.2」を検出。実体は前章の図表で、訳文は第6章側に配置済み。
- 第3〜第7章で「VR/AR/AI」等の原語が訳文に未検出と判定される場合があるが、本訳では英略語（VR/AR/AI）を維持しているため。

**許容変異の採用例**：
- "life outcomes" → 文脈により「人生の主要な成果」「人生の成果」を併用。
- "job performance" → 文脈により「職務遂行」「職務遂行能力」を併用。
- "game-based assessment" → 「ゲームベースのアセスメント」「ゲームベース・アセスメント」併用。

これらは glossary の代表訳と微差があるが、文脈適合の表記揺れとして許容。

---

## 7. 制約と将来の改善余地

1. **画像形式の図表（Table 4.1, Figure 4.1, 4.3, 4.4-4.8 など）**: 本翻訳ではキャプションと注のみ訳出。図内テキスト（スクリーンショット内の英文等）は別途、画像処理（OCR）または手動転記で対応する必要がある。
2. **References 翻訳**: CLAUDE.md ルールにより原文維持。日本語版書誌が存在する文献（OECD刊行物の邦訳など）の併記は次フェーズの作業として留保。
3. **対訳版の段落アラインメント**: `bilingual.md` は章境界での突合せ。段落単位の対応は翻訳のリフローにより一意でないため、段落アラインメントには NLP ツール（例：bertalign）の併用が望ましい。
4. **`reference bias`、`immediacy bias` の訳**: 定訳未確立のため、専門家レビューで再確認が望ましい。
5. **`neurodivergent` の訳**: 「神経発達症的」採用だが、当事者運動の文脈ではカタカナ「ニューロダイバージェント」が選好される場合がある。出版媒体の方針に応じて要再検討。
