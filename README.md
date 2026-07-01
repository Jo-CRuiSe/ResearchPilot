# ResearchPilot

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
