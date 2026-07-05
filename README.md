# ResearchPilot

ResearchPilot 是一个开源的 [Agent Skill](https://agentskills.io/)，用于系统开展学术课题调研。它可以帮助 Codex 将宽泛的研究想法转化为可追溯的检索策略、证据矩阵、文献综合与有理有据的研究空白分析。

仓库内置的技能名为 $conduct-topic-research，支持中文和英文调研工作流。

## 功能

- 将课题拆解为研究对象、问题、方法、情境与结果。
- 构建双语关键词矩阵和可复用的布尔检索式。
- 分层检索综述、奠基性研究、引文脉络、当前前沿、现实资料与矛盾证据。
- 记录准确的检索式、平台、筛选条件、日期与筛选决策。
- 使用结构化表格比较论文，而不是生成彼此孤立的摘要。
- 综合共识、条件性结论、分歧、失败与前沿信号。
- 从存在性、重要性、可行性、独特性与可证伪性等方面检验候选研究空白。
- 使用 Markdown 和 CSV 模板创建可复用的调研工作区。

## 示例

```text
使用 $conduct-topic-research 系统调研“多模态基础模型在医学影像中的应用”。
先拆分课题和中英文检索词，再比较代表性文献，并找出可验证的研究空白。
```

英文示例：

```text
Use $conduct-topic-research to investigate multimodal foundation models
for medical imaging. Start with a bilingual keyword matrix, compare the
representative literature, and identify feasible research gaps.
```

## 工作流程

```text
明确需要支持的决策
→ 拆解课题
→ 构建双语检索式
→ 检索并追踪引文
→ 筛选并提取证据
→ 比较来源
→ 综合观点与分歧
→ 检验新颖性与可行性
→ 报告局限与后续步骤
```

该技能支持四种模式：

| 模式 | 用途 |
|---|---|
| 规划 | 设计检索策略，但不声称已经获得检索结果 |
| 快速扫描 | 梳理术语、研究分支、代表性工作与前沿信号 |
| 系统调研 | 记录可复现的检索过程、筛选标准、证据与停止条件 |
| 更新 | 使用更新的、相互矛盾的或足以改变领域认识的证据扩展现有综述 |

### 选择模式

你可以在提示词中使用自然语言显式指定模式，无需使用特殊命令：

```text
使用 $conduct-topic-research，以规划模式研究“你的课题”。只设计检索策略，不执行检索。

使用 $conduct-topic-research，以快速扫描模式研究“你的课题”，梳理主要分支、代表性文献和前沿信号。

使用 $conduct-topic-research，以系统调研模式研究“你的课题”，记录检索式、筛选标准、证据和停止条件。

使用 $conduct-topic-research，以更新模式检查“现有综述或研究目录”，重点查找更新的、矛盾的或足以改变领域认识的证据。
```

如果没有指定模式，技能会根据请求自动判断。它会在给出实质性发现前说明所选模式和研究范围；只有当课题或研究目的过于模糊、无法负责任地开展检索时，才会要求补充信息。

## 安装

### 为当前用户安装

克隆本仓库，然后将技能复制或链接到 Codex 用户技能目录：

```bash
git clone https://github.com/Jo-CRuiSe/ResearchPilot.git
mkdir -p ~/.agents/skills
cp -R ResearchPilot/skills/conduct-topic-research ~/.agents/skills/
```

开发时可使用符号链接，使本地修改立即生效：

```bash
mkdir -p ~/.agents/skills
ln -s /absolute/path/to/ResearchPilot/skills/conduct-topic-research \
  ~/.agents/skills/conduct-topic-research
```

### 为单个仓库安装

将技能复制到目标仓库：

```text
<repository>/.agents/skills/conduct-topic-research/
```

Codex 可以在 CLI、IDE 扩展和应用中发现技能。你可以使用 $conduct-topic-research 显式调用该技能，也可以在请求符合其描述时让 Codex 自动选择。如果新安装的技能没有出现，请重启 Codex。

仓库发布后，你也可以让 $skill-installer 从该 GitHub 仓库安装此技能。

## 生成调研工作区

内置脚本仅使用 Python 标准库，需要 Python 3.10 或更高版本：

```bash
python3 skills/conduct-topic-research/scripts/init_research_workspace.py \
  --topic "your research topic" \
  --root "/path/to/project" \
  --slug "optional-topic-slug"
```

脚本会创建：

```text
research/<topic-slug>/
├── README.md
├── scope.md
├── keywords.md
├── search-log.csv
├── literature-matrix.md
├── evidence-matrix.csv
├── synthesis.md
└── gaps.md
```

已有文件会被保留：脚本只创建缺失的文件。

## 仓库结构

```text
ResearchPilot/
├── README.md
├── LICENSE
├── .gitignore
├── .gitattributes
└── skills/
    └── conduct-topic-research/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        │   ├── output-templates.md
        │   └── research-method.md
        └── scripts/
            └── init_research_workspace.py
```

- SKILL.md 包含核心工作流程与触发说明。
- agents/openai.yaml 提供 Codex 应用的展示元数据与默认提示词。
- references/ 包含详细的调研标准与可复用的输出表格。
- scripts/ 包含确定性的工作区初始化脚本。

## 要求与局限

- 技能本身没有第三方运行时依赖。
- 可选的初始化脚本需要 Python 3.10+。
- 时效性调研需要宿主智能体具备互联网搜索、学术数据库或连接器访问能力。
- 数据库覆盖范围取决于用户的订阅与可用工具。
- 该工作流支持系统调研，但除非用户明确采用 PRISMA 等特定正式综述标准，否则不会声称符合这些标准。
- 新颖性结论受已记录的数据库、检索词、语言、日期与可访问来源所限。

## 验证

该技能已通过 Codex skill-creator 验证器检查。工作区初始化脚本也已通过冒烟测试，确认能够生成所有预期的 Markdown 和 CSV 文件，且不会覆盖现有工作。

## 贡献

欢迎提交 Issue 和 Pull Request。以下贡献尤其有帮助：

- 针对特定学科的检索与证据质量指南；
- 更强的可复现性或偏差检查；
- 保持广泛复用性的其他输出模板；
- 初始化脚本的跨平台改进；
- 真实的测试提示词与有记录的失败案例。

请保持技能定位聚焦，保留渐进式披露原则，并避免在 SKILL.md 中重复详细的参考资料。

## 许可证

[MIT](LICENSE)

---

# ResearchPilot (English)

ResearchPilot is an open-source [Agent Skill](https://agentskills.io/) for systematic academic topic research. It helps Codex turn a broad research idea into a traceable search strategy, evidence matrix, literature synthesis, and defensible research-gap analysis.

The included skill is named $conduct-topic-research and supports Chinese and English research workflows.

## What it does

- Decomposes a topic into object, problem, method, context, and outcome.
- Builds bilingual keyword matrices and reusable Boolean search strings.
- Searches in layers: reviews, seminal work, citation trails, current frontier, real-world sources, and contradictory evidence.
- Records exact queries, platforms, filters, dates, and screening decisions.
- Compares papers in structured tables instead of producing isolated summaries.
- Synthesizes consensus, conditional findings, disagreements, failures, and frontier signals.
- Tests candidate gaps for existence, importance, feasibility, distinctiveness, and falsifiability.
- Creates a reusable research workspace with Markdown and CSV templates.

## Example

```text
Use $conduct-topic-research to investigate multimodal foundation models
for medical imaging. Start with a bilingual keyword matrix, compare the
representative literature, and identify feasible research gaps.
```

中文示例：

```text
使用 $conduct-topic-research 系统调研“多模态基础模型在医学影像中的应用”。
先拆分课题和中英文检索词，再比较代表性文献，并找出可验证的研究空白。
```

## Workflow

```text
Scope the decision
→ decompose the topic
→ build bilingual queries
→ search and trace citations
→ screen and extract evidence
→ compare sources
→ synthesize claims and disagreements
→ test novelty and feasibility
→ report limits and next steps
```

The skill supports four modes:

| Mode | Use |
|---|---|
| Plan | Design the search strategy without claiming search results |
| Rapid scan | Map terminology, branches, representative work, and frontier signals |
| Systematic investigation | Record reproducible searches, screening, evidence, and stopping conditions |
| Update | Extend an existing review with newer, contradictory, or field-changing evidence |

### Choosing a mode

You can select a mode explicitly in natural language; no special command is required:

```text
Use $conduct-topic-research in Plan mode for "your topic." Design the search strategy without running the search.

Use $conduct-topic-research in Rapid scan mode for "your topic." Map the major branches, representative literature, and frontier signals.

Use $conduct-topic-research in Systematic investigation mode for "your topic." Record queries, screening criteria, evidence, and stopping conditions.

Use $conduct-topic-research in Update mode on "an existing review or research folder." Focus on newer, contradictory, or field-changing evidence.
```

If you do not specify a mode, the skill infers one from your request. It states the selected mode and scope before presenting substantive findings, and asks for clarification only when the topic or intended decision is too ambiguous to search responsibly.

## Installation

### Install for your user account

Clone this repository, then copy or link the skill into the Codex user skill directory:

```bash
git clone https://github.com/Jo-CRuiSe/ResearchPilot.git
mkdir -p ~/.agents/skills
cp -R ResearchPilot/skills/conduct-topic-research ~/.agents/skills/
```

For development, use a symbolic link so local edits take effect immediately:

```bash
mkdir -p ~/.agents/skills
ln -s /absolute/path/to/ResearchPilot/skills/conduct-topic-research \
  ~/.agents/skills/conduct-topic-research
```

### Install for one repository

Copy the skill into the target repository:

```text
<repository>/.agents/skills/conduct-topic-research/
```

Codex discovers skills in the CLI, IDE extension, and app. Invoke the skill explicitly with $conduct-topic-research, or let Codex select it when the request matches its description. If a newly installed skill does not appear, restart Codex.

You can also ask $skill-installer to install the skill from this GitHub repository after it is published.

## Generated research workspace

The bundled script uses only the Python standard library and requires Python 3.10 or newer:

```bash
python3 skills/conduct-topic-research/scripts/init_research_workspace.py \
  --topic "your research topic" \
  --root "/path/to/project" \
  --slug "optional-topic-slug"
```

It creates:

```text
research/<topic-slug>/
├── README.md
├── scope.md
├── keywords.md
├── search-log.csv
├── literature-matrix.md
├── evidence-matrix.csv
├── synthesis.md
└── gaps.md
```

Existing files are preserved: the script only creates missing files.

## Repository structure

```text
ResearchPilot/
├── README.md
├── LICENSE
├── .gitignore
├── .gitattributes
└── skills/
    └── conduct-topic-research/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        ├── references/
        │   ├── output-templates.md
        │   └── research-method.md
        └── scripts/
            └── init_research_workspace.py
```

- SKILL.md contains the core workflow and trigger description.
- agents/openai.yaml provides Codex app display metadata and a default prompt.
- references/ contains detailed research criteria and reusable output tables.
- scripts/ contains the deterministic workspace initializer.

## Requirements and limitations

- The skill itself has no third-party runtime dependencies.
- The optional initializer requires Python 3.10+.
- Current-state research requires the host agent to have internet search, scholarly database, or connector access.
- Database coverage depends on the user's subscriptions and available tools.
- The workflow supports systematic investigation, but it does not claim compliance with a specific formal review standard such as PRISMA unless the user explicitly applies that standard.
- Novelty conclusions are bounded by the recorded databases, search terms, languages, dates, and accessible sources.

## Validation

The skill has been checked with the Codex skill-creator validator. The workspace initializer has also been smoke-tested to confirm that it generates all expected Markdown and CSV files without overwriting existing work.

## Contributing

Issues and pull requests are welcome. Useful contributions include:

- discipline-specific search and evidence-quality guidance;
- stronger reproducibility or bias checks;
- additional output templates that remain broadly reusable;
- cross-platform improvements to the initializer;
- realistic test prompts and documented failure cases.

Keep the skill focused, preserve progressive disclosure, and avoid duplicating detailed reference material inside SKILL.md.

## License

[MIT](LICENSE)
