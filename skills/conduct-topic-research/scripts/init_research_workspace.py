#!/usr/bin/env python3
"""Create a traceable topic-research workspace using only the standard library."""

from __future__ import annotations

import argparse
import csv
import re
import unicodedata
from pathlib import Path


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).strip().lower()
    ascii_slug = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")
    if ascii_slug:
        return ascii_slug[:64]
    codepoints = "-".join(f"u{ord(char):x}" for char in normalized if not char.isspace())
    return codepoints[:120] or "topic-research"


def write_text_if_absent(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def write_csv_if_absent(path: Path, headers: list[str]) -> None:
    if path.exists():
        return
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        csv.writer(handle).writerow(headers)


def create_workspace(root: Path, topic: str, slug: str | None) -> Path:
    destination = root.resolve() / "research" / (slug or slugify(topic))
    destination.mkdir(parents=True, exist_ok=True)
    visuals_dir = destination / "visuals"
    literature_dir = destination / "literature"
    papers_dir = literature_dir / "papers"
    metadata_dir = literature_dir / "metadata"
    visuals_dir.mkdir(exist_ok=True)
    papers_dir.mkdir(parents=True, exist_ok=True)
    metadata_dir.mkdir(parents=True, exist_ok=True)

    write_text_if_absent(
        destination / "README.md",
        f"""# {topic}\n\n## 目标\n\n系统梳理课题边界、研究现状、前沿争议与可验证的研究空白。\n\n## 关键文件\n\n- `report.md`：面向用户的主 Markdown 调研报告\n- `scope.md`：问题定义、范围与筛选标准\n- `keywords.md`：课题拆分、中英文检索词和可执行检索式\n- `search-log.csv`：真实检索式、平台、日期及筛选数量\n- `literature-matrix.md`：便于阅读的文章与来源对比表\n- `evidence-matrix.csv`：逐项证据抽取\n- `synthesis.md`：按主张组织的综合分析\n- `gaps.md`：研究空白及其支持/反对证据\n- `visuals/`：Mermaid 图和可视化草稿\n- `literature/`：下载的开放文献、元数据与不可下载记录\n\n## 来源原则\n\n所有结论应链接到真实来源；明确区分来源事实、综合判断与推测。只下载合法可访问的开放全文、预印本、作者版、机构仓储文件或公开技术报告；不可访问或权限不明的文献记录到 `literature/unavailable.md`。\n""",
    )
    write_text_if_absent(
        destination / "report.md",
        f"""# 调研报告：{topic}\n\n## 执行结论\n\n## 范围与研究问题\n\n## 课题拆分\n\n| 维度 | 当前定义 | 边界或排除项 |\n|---|---|---|\n| 研究对象 | | |\n| 核心问题 | | |\n| 方法 | | |\n| 场景 | | |\n| 结果或评价指标 | | |\n\n## 中英文关键词与检索式\n\n## 检索方法与覆盖限制\n\n## 领域地图与发展脉络\n\n```mermaid\nmindmap\n  root(({topic}))\n    主要分支\n      代表性问题\n      代表性方法\n    数据与场景\n      数据集或样本\n      应用约束\n    研究空白\n      待验证方向\n```\n\n```mermaid\ntimeline\n  title 研究发展脉络\n  早期阶段 : 基础概念或经典方法\n  发展阶段 : 方法扩展或数据变化\n  当前阶段 : 前沿信号与开放问题\n```\n\n## 文章与来源对比\n\n| 论文或来源 | 年份 | 问题 | 方法 | 数据集或样本 | 指标或结果 | 主要贡献 | 局限 | 可借鉴点 |\n|---|---:|---|---|---|---|---|---|---|\n| 引文与稳定链接 | | | | | | | | |\n\n## 共识与条件性结论\n\n## 争议、失败案例与适用边界\n\n## 最新前沿信号\n\n## 候选研究空白\n\n```mermaid\nquadrantChart\n  title 候选研究空白：重要性与可行性\n  x-axis 低可行性 --> 高可行性\n  y-axis 低重要性 --> 高重要性\n  quadrant-1 优先验证\n  quadrant-2 重要但困难\n  quadrant-3 暂缓\n  quadrant-4 快速探索\n```\n\n## 推荐研究问题或实验\n\n## 文献文件与不可下载来源\n\n| Source ID | Local file | Title | DOI/URL | Access status | Download or access date | Rights/access note |\n|---|---|---|---|---|---|---|\n| | | | | | | |\n\n## 本次调研限制\n\n## References\n""",
    )
    write_text_if_absent(
        destination / "scope.md",
        f"""# 调研范围：{topic}\n\n## 决策目标\n\n## 核心研究问题\n\n## 课题拆分表\n\n| 维度 | 当前定义 | 边界或排除项 |\n|---|---|---|\n| 研究对象 | | |\n| 核心问题 | | |\n| 方法 | | |\n| 场景 | | |\n| 结果或评价指标 | | |\n\n## 覆盖范围\n\n- 学科：\n- 时间：\n- 语言与地区：\n- 来源类型：\n\n## 纳入标准\n\n## 排除标准\n""",
    )
    write_text_if_absent(
        destination / "keywords.md",
        f"""# 课题拆分与检索词：{topic}\n\n## 中英文检索词矩阵\n\n| 概念块 | 中文核心词 | 英文核心词 | 同义词、缩写与变体 | 上下位或邻近概念 | 歧义词与排除词 |\n|---|---|---|---|---|---|\n| 研究对象 | | | | | |\n| 核心问题 | | | | | |\n| 方法 | | | | | |\n| 场景 | | | | | |\n| 结果或评价指标 | | | | | |\n\n## 可执行检索式\n\n| 目的 | 平台或来源类型 | 完整检索式 | 筛选条件 | 设计理由 |\n|---|---|---|---|---|\n| 发现术语 | | | | |\n| 查找综述 | | | | |\n| 查找经典工作 | | | | |\n| 查找最新前沿 | | | | |\n| 查找失败与争议 | | | | |\n| 验证创新性 | | | | |\n""",
    )
    write_csv_if_absent(
        destination / "search-log.csv",
        ["date", "platform", "query", "filters", "result_count", "screened_count", "included_count", "notes"],
    )
    write_csv_if_absent(
        destination / "evidence-matrix.csv",
        [
            "source_id", "title", "year", "source_type", "research_question",
            "context_or_sample", "method_or_intervention", "comparison", "outcomes",
            "key_result", "limitations", "evidence_strength", "relevance", "doi_or_url", "notes",
        ],
    )
    write_text_if_absent(
        destination / "literature-matrix.md",
        f"""# 文章与来源对比：{topic}\n\n| 论文或来源 | 年份 | 问题 | 方法 | 数据集或样本 | 指标或结果 | 主要贡献 | 局限 | 可借鉴点 |\n|---|---:|---|---|---|---|---|---|---|\n| 引文与稳定链接 | | | | | | | | |\n\n## 主张级证据综合\n\n| 主张 | 支持来源 | 反对或限定来源 | 证据强度 | 成立条件 | 综合判断 |\n|---|---|---|---|---|---|\n| | | | | | |\n""",
    )
    write_text_if_absent(
        destination / "synthesis.md",
        f"""# 综合分析：{topic}\n\n## 领域地图\n\n```mermaid\nmindmap\n  root(({topic}))\n    主要分支\n    方法谱系\n    数据与场景\n    研究空白\n```\n\n## 发展脉络\n\n```mermaid\ntimeline\n  title 研究发展脉络\n  早期阶段 : 基础概念或经典方法\n  发展阶段 : 方法扩展或数据变化\n  当前阶段 : 前沿信号与开放问题\n```\n\n## 已形成的共识\n\n## 条件性结论\n\n## 主要争议与相反证据\n\n```mermaid\nflowchart TD\n  Claim[核心主张] --> Support[支持证据]\n  Claim --> Qualifier[限定条件]\n  Claim --> Conflict[相反或削弱证据]\n  Support --> Judgment[综合判断]\n  Qualifier --> Judgment\n  Conflict --> Judgment\n```\n\n## 失败案例与适用边界\n\n## 最新前沿信号\n\n## 覆盖限制与不确定性\n""",
    )
    write_text_if_absent(
        destination / "gaps.md",
        f"""# 候选研究空白：{topic}\n\n## 排序原则\n\n综合重要性、证据强度、独特性、可行性与可证伪性排序。\n\n```mermaid\nquadrantChart\n  title 候选研究空白：重要性与可行性\n  x-axis 低可行性 --> 高可行性\n  y-axis 低重要性 --> 高重要性\n  quadrant-1 优先验证\n  quadrant-2 重要但困难\n  quadrant-3 暂缓\n  quadrant-4 快速探索\n```\n\n## 候选空白 1\n\n- 精确表述：\n- 最近的 3–5 项工作：\n- 支持证据：\n- 反对或削弱证据：\n- 持续存在的原因：\n- 可能贡献：\n- 可行性：\n- 决定性实验或分析：\n- 置信度及理由：\n""",
    )
    write_text_if_absent(
        visuals_dir / "README.md",
        f"""# 可视化说明：{topic}\n\n## 用途\n\n保存 Mermaid 图、图形草稿和支持图形关系的来源说明。主报告中的关键图应同步或扩展到本目录，便于后续修改。\n\n## 建议图形\n\n- `mindmap`：领域地图、概念地图、分类体系\n- `flowchart`：方法路线、筛选流程、证据链\n- `timeline`：研究发展脉络\n- `graph`：论文、数据集、方法、主张之间的关系\n- `quadrantChart`：候选研究空白的重要性与可行性定位\n\n## 证据要求\n\n重要节点或关系应能追溯到 `literature-matrix.md`、`evidence-matrix.csv` 或 `References` 中的来源。推断性的聚类或关系需要明确标注为综合判断。\n""",
    )
    write_text_if_absent(
        literature_dir / "README.md",
        f"""# 文献归档：{topic}\n\n## 目录\n\n- `papers/`：合法下载的开放全文、预印本、作者版、机构仓储文件或公开技术报告\n- `metadata/`：BibTeX、RIS、JSON、网页快照说明或其他引用元数据\n- `unavailable.md`：无法合法下载、访问受限或权限不明确的来源\n\n## 命名规则\n\n使用稳定、可去重的文件名：\n\n```text\nsNN-first-author-year-short-title-version.ext\n```\n\n示例：\n\n```text\ns03-vaswani-2017-attention-is-all-you-need-conference.pdf\ns03-vaswani-2017-attention-is-all-you-need-arxiv.pdf\ns12-smith-2024-benchmark-survey-metadata.json\n```\n\n## 访问原则\n\n只下载合法可访问的文件。付费墙、登录限制、访问失败或权限不明确的来源，只记录 DOI/URL、访问日期、尝试来源和使用方式，不绕过访问控制。\n""",
    )
    write_text_if_absent(
        literature_dir / "unavailable.md",
        f"""# 不可下载或访问受限来源：{topic}\n\n| Source ID | Title | DOI/URL | Attempted source | Date | Reason not downloaded | How it was used |\n|---|---|---|---|---|---|---|\n| | | | publisher / DOI / repository / author page | | paywalled / access denied / no PDF / uncertain rights | metadata only / abstract only / excluded |\n""",
    )
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize a systematic topic-research workspace.")
    parser.add_argument("--topic", required=True, help="Human-readable research topic")
    parser.add_argument("--root", required=True, type=Path, help="Project root")
    parser.add_argument("--slug", help="Optional lowercase ASCII directory slug")
    args = parser.parse_args()
    if args.slug and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.slug):
        parser.error("--slug must contain lowercase letters, digits, and single hyphens only")
    print(create_workspace(args.root, args.topic, args.slug))


if __name__ == "__main__":
    main()
