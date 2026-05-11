# 翻訳進捗管理

最終更新: 全章完了時

## 全体ステータス

| 章 | タイトル | 原文ページ | 状態 | 検出問題 |
|---|---|---|---|---|
| 1 | Introduction | PDF p.9 | ✅ 完了 | 0（情報レベルのみ） |
| 2 | Expanding beyond indirect assessment | PDF p.10–13 | ✅ 完了 | 0 |
| 3 | Review of direct assessment tools | PDF p.14–18 | ✅ 完了 | 0 |
| 4 | Behaviour-based assessment tools | PDF p.19–52 | ✅ 完了（4セグメント） | 0 |
| 5 | New technological approaches | PDF p.53–64 | ✅ 完了 | 0 |
| 6 | Review discussion | PDF p.65–68 | ✅ 完了 | 0 |
| 7 | Conclusion | PDF p.69–70 | ✅ 完了 | 章境界の偽陽性のみ |
| Annex A | Search terms for SES | PDF p.86 | ✅ 完了 | – |
| Annex B | Full list of behavioural tools | PDF p.87–89 | ✅ 完了 | – |

## References
- 訳出方針により翻訳しない（CLAUDE.md）。`output/references_raw.md` に原文転載済み（PDF p.71–85、約500件）。

## 最終成果物（`output/` 配下）
- `full_ja.md` — 統合版日本語訳（要旨＋全章＋付録、約 160KB）
- `bilingual.md` — 対訳版（章単位の原文＋訳文、約 350KB）
- `glossary_final.json` — 最終用語集（99項目）
- `translation_log.md` — 翻訳判断記録
- `references_raw.md` — References 原文転載

## 統計
- 翻訳対象本文: 約 65 ページ（References を除く）
- glossary 規模: 81 → 99 項目（途中で18件を `glossary_pending.json` → `glossary.json` に承認移行）
- コミット数: 12（各章セグメントごと）
- QC 自動検査: 9 章すべてで「章確定可能」（軽微な偽陽性を除く）
