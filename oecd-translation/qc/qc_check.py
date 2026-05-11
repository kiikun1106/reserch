#!/usr/bin/env python3
"""Chapter-level QC for OECD translation project.

Usage: python3 qc_check.py <chapter_num> <pdf_pages_start> <pdf_pages_end>
e.g.,  python3 qc_check.py 1 9 9
       python3 qc_check.py 2 10 13
"""
import json, re, sys, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def load_glossary():
    with open(ROOT / "glossary.json", encoding="utf-8") as f:
        return json.load(f)["terms"]

def load_source(start, end):
    text = ""
    for i in range(start, end + 1):
        with open(ROOT / "extracted" / f"page_{i:03d}.txt", encoding="utf-8") as f:
            page = f.read()
        # Strip header/footer noise: page number + "EDU/WKP(2024)11" pattern, title, "Unclassified"
        page = re.sub(r"\d{1,3}\s+EDU/WKP\(2024\)11", "", page)
        page = re.sub(r"EDU/WKP\(2024\)11\s+\d{1,3}", "", page)
        page = re.sub(r"EDU/WKP\(2024\)11", "", page)
        page = re.sub(r"INNOVATIVE TOOLS FOR THE DIRECT ASSESSMENT OF SOCIAL AND EMOTIONAL SKILLS", "", page)
        page = re.sub(r"\bUnclassified\b", "", page)
        text += page + "\n"
    return text

def load_translation(chapter):
    p = ROOT / "output" / f"chapter_{chapter:02d}.md"
    if not p.exists():
        return ""
    return p.read_text(encoding="utf-8")

def check_terminology(src, tgt, glossary):
    issues = []
    for entry in glossary:
        term = entry["term"]
        ja = entry["proposed_ja"]
        base = re.split(r"\s*[/(（]", term)[0].strip()
        if not re.search(re.escape(base), src, re.IGNORECASE):
            continue
        # accept any of the slash-separated alternates
        ja_forms = [a.strip() for a in re.split(r"[/／]", re.split(r"[(（]", ja)[0]) if a.strip()]
        # also strip suffix particles like 「（〜）」 and add minimal stems
        stems = set()
        for f in ja_forms:
            stems.add(f)
            # drop trailing 「）」「（」
            stems.add(re.sub(r"[（）()].*$", "", f))
        if not any(s and s in tgt for s in stems):
            issues.append(f"  - '{base}' 出現するが訳語『{ja_forms[0]}』系が訳文に未検出")
    return issues

def check_style(tgt):
    issues = []
    bad = []
    for pat in ["です。", "ます。", "でしょう", "ですね", "ですが、", "ました。"]:
        n = tgt.count(pat)
        if n:
            bad.append(f"『{pat}』 × {n}")
    if bad:
        issues.append("  - ですます調混入: " + ", ".join(bad))
    return issues

def count_numbers(text):
    # Match standalone numbers; use ASCII-only boundaries since \w matches Japanese chars.
    nums = re.findall(r"(?<![A-Za-z0-9_.])\d{1,4}(?:[\.,]\d+)?%?(?![A-Za-z0-9_.])", text)
    return nums

def check_numbers(src, tgt):
    # Strip citation markers like [1], [42], (2023) etc. before counting
    def clean(t):
        t = re.sub(r"\[\d+\]", "", t)
        t = re.sub(r"\(\d{4}[a-z]?(?:\[\d+\])?\)", "", t)
        t = re.sub(r",\s*\d{4}(?:\[\d+\])?", "", t)
        return t
    src_clean = clean(src)
    tgt_clean = clean(tgt)
    src_nums = count_numbers(src_clean)
    tgt_nums = count_numbers(tgt_clean)
    src_c = {n: src_nums.count(n) for n in set(src_nums)}
    tgt_c = {n: tgt_nums.count(n) for n in set(tgt_nums)}
    missing = []
    for n, c in src_c.items():
        if c > tgt_c.get(n, 0):
            # Only flag substantive numbers: percentages, decimals, or >= 10
            if "%" in n or "." in n or "," in n or int(re.sub(r"[^\d]", "", n) or "0") >= 10:
                missing.append(f"{n} (原文 {c} → 訳文 {tgt_c.get(n,0)})")
    return missing

def check_figrefs(src, tgt):
    issues = []
    # Find figure/table/box references in source
    src_fig = set(re.findall(r"\bFigure\s+(\d+\.\d+)", src))
    src_tab = set(re.findall(r"\bTable\s+(\d+\.\d+)", src))
    src_box = set(re.findall(r"\bBox\s+(\d+\.\d+)", src))
    tgt_fig = set(re.findall(r"図\s*(\d+\.\d+)", tgt))
    tgt_tab = set(re.findall(r"表\s*(\d+\.\d+)", tgt))
    tgt_box = set(re.findall(r"コラム\s*(\d+\.\d+)", tgt))
    for label, s, t in [("図", src_fig, tgt_fig), ("表", src_tab, tgt_tab), ("コラム", src_box, tgt_box)]:
        miss = s - t
        extra = t - s
        if miss:
            issues.append(f"  - {label}参照欠落: {sorted(miss)}")
        if extra:
            issues.append(f"  - {label}参照に原文にない番号: {sorted(extra)}")
    return issues

def check_paragraphs(src, tgt):
    # Source: every '.' followed by space + capital letter (end of sentence)
    src_sents = len(re.findall(r"[a-zA-Z\)\]][\.!?](?:\s|$)", src))
    tgt_sents = len(re.findall(r"[。．！？]", tgt))
    ratio = tgt_sents / max(src_sents, 1)
    return src_sents, tgt_sents, ratio

def run(chapter, start, end):
    glossary = load_glossary()
    src = load_source(start, end)
    tgt = load_translation(chapter)
    if not tgt:
        print(f"Chapter {chapter}: translation not found.")
        return

    report = [f"# 第{chapter}章 QCレポート", "",
              f"対象: PDF p.{start}〜{end} / output/chapter_{chapter:02d}.md", ""]

    # 1. terminology
    term_issues = check_terminology(src, tgt, glossary)
    report.append("## 1. 用語整合性チェック")
    if term_issues:
        report.append(f"未検出の訳語: {len(term_issues)}件")
        report.extend(term_issues)
    else:
        report.append("OK: 用語集の該当項目は全て訳文に出現")
    report.append("")

    # 2. paragraphs
    src_n, tgt_n, ratio = check_paragraphs(src, tgt)
    report.append("## 2. 文量比較（文末句点数で代用）")
    report.append(f"原文 {src_n} 文 / 訳文 {tgt_n} 文 / 比率 {ratio:.2f}")
    if ratio < 0.5 or ratio > 2.8:
        report.append("⚠ 文量の乖離が大きい（0.5〜2.8の範囲外）")
    else:
        report.append("OK")
    report.append("")

    # 3. style
    style_issues = check_style(tgt)
    report.append("## 3. 文体チェック（である調）")
    if style_issues:
        report.extend(style_issues)
    else:
        report.append("OK: ですます調混入なし")
    report.append("")

    # 4. numbers
    num_issues = check_numbers(src, tgt)
    report.append("## 4. 数値の取りこぼし")
    if num_issues:
        report.append(f"訳文で減少: {len(num_issues)}件")
        for n in num_issues[:20]:
            report.append(f"  - {n}")
        if len(num_issues) > 20:
            report.append(f"  - ... 他 {len(num_issues)-20}件")
    else:
        report.append("OK")
    report.append("")

    # 5. figure refs
    fig_issues = check_figrefs(src, tgt)
    report.append("## 5. 図表参照番号")
    if fig_issues:
        report.extend(fig_issues)
    else:
        report.append("OK: 図表参照は全て一致")
    report.append("")

    # Aggregate
    has_blocker = bool(fig_issues or style_issues) or ratio < 0.5 or ratio > 2.8
    report.append("## 総合判定")
    report.append("⚠ 問題あり: issues.md を確認のうえ章を再検討" if has_blocker else "OK: 章確定可能")

    out = ROOT / "qc" / f"chapter_{chapter:02d}.md"
    out.write_text("\n".join(report), encoding="utf-8")
    print(f"Wrote {out}")
    if has_blocker:
        return False
    return True

if __name__ == "__main__":
    ch = int(sys.argv[1])
    s = int(sys.argv[2])
    e = int(sys.argv[3])
    run(ch, s, e)
