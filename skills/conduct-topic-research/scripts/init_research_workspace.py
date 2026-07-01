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

    write_text_if_absent(
        destination / "README.md",
        f"""# {topic}\n\n## 目标\n\n系统梳理课题边界、研究现状、前沿争议与可验证的研究空白。\n\n## 关键文件\n\n- `scope.md`：问题定义、范围与筛选标准\n- `keywords.md`：课题拆分、中英文检索词和可执行检索式\n- `search-log.csv`：真实检索式、平台、日期及筛选数量\n- `literature-matrix.md`：便于阅读的文章与来源对比表\n- `evidence-matrix.csv`：逐项证据抽取\n- `synthesis.md`：按主张组织的综合分析\n- `gaps.md`：研究空白及其支持/反对证据\n\n## 来源原则\n\n所有结论应链接到真实来源；明确区分来源事实、综合判断与推测。\n""",
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
        f"""# 综合分析：{topic}\n\n## 领域地图\n\n## 发展脉络\n\n## 已形成的共识\n\n## 条件性结论\n\n## 主要争议与相反证据\n\n## 失败案例与适用边界\n\n## 最新前沿信号\n\n## 覆盖限制与不确定性\n""",
    )
    write_text_if_absent(
        destination / "gaps.md",
        f"""# 候选研究空白：{topic}\n\n## 排序原则\n\n综合重要性、证据强度、独特性、可行性与可证伪性排序。\n\n## 候选空白 1\n\n- 精确表述：\n- 最近的 3–5 项工作：\n- 支持证据：\n- 反对或削弱证据：\n- 持续存在的原因：\n- 可能贡献：\n- 可行性：\n- 决定性实验或分析：\n- 置信度及理由：\n""",
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
