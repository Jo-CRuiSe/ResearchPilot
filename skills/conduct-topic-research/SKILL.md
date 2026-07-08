---
name: conduct-topic-research
description: Systematically investigate an academic topic, research direction, thesis subject, or proposed project by mapping concepts, designing reproducible searches, triangulating scholarly and real-world sources, tracing citations, synthesizing evidence, and identifying defensible research gaps. Use when a user asks for 课题调研、研究现状、文献调研、文献综述、选题分析、前沿追踪、创新点、research landscape、literature search、state of the art, or help deciding whether a research idea is novel and worthwhile.
---

# Conduct Topic Research

Produce a traceable research map rather than a pile of paper summaries. Separate what sources establish from what you infer.

## Choose the operating mode

- **Plan**: Design keywords, databases, scope, screening rules, and deliverable structure without claiming search results.
- **Rapid scan**: Establish terminology, major branches, representative work, current frontier, and candidate gaps. Label it as non-exhaustive.
- **Systematic investigation**: Record queries, dates, inclusion/exclusion criteria, deduplication, evidence, limitations, and stopping conditions.
- **Update**: Start from an existing review or research folder and search only for later, contradictory, or field-changing evidence.

Infer the mode from the request. Ask a question only when the topic or intended decision is too ambiguous to search responsibly. State the chosen scope and mode before substantive findings.

## Execute the workflow

### 1. Frame and decompose the topic

Translate the request into:

`object × problem × method × context × outcome`

Record the intended use, relevant disciplines, time window, languages, geography, acceptable evidence, and exclusions. Treat the user's initial wording as a hypothesis, not necessarily the field's preferred terminology.

Before searching, show a topic-decomposition table. Use "not specified" rather than inventing a dimension:

| Dimension | Meaning | Candidate terms |
|---|---|---|
| Object | Population, material, system, or phenomenon | ... |
| Problem | Question, mechanism, task, or pain point | ... |
| Method | Theory, algorithm, instrument, or intervention | ... |
| Context | Application, geography, environment, or constraint | ... |
| Outcome | Effect, metric, cost, risk, or evaluation target | ... |

### 2. Build a concept and query map

Create Chinese and English terms, abbreviations, synonyms, broader/narrower concepts, legacy terms, and adjacent-field vocabulary. Present them before reporting search findings:

| Concept block | Chinese terms | English terms | Abbreviations/variants | Exclusions or ambiguous terms |
|---|---|---|---|---|
| Object | ... | ... | ... | ... |
| Problem | ... | ... | ... | ... |
| Method | ... | ... | ... | ... |
| Context/outcome | ... | ... | ... | ... |

Then provide reusable query strings for Chinese databases, international scholarly databases, and broad web/repository search where relevant. Combine term blocks with Boolean operators. Run at least one broad discovery query and one precise validation query.

Read [references/research-method.md](references/research-method.md) when designing a substantial investigation, adapting the workflow to experimental, computational, engineering, clinical, or humanities/social-science work. Read [references/output-templates.md](references/output-templates.md) whenever producing a report or research files.

### 3. Search in layers

Search sources appropriate to the field and access available:

1. Recent reviews or authoritative syntheses to map the field.
2. Seminal work and backward citations to recover foundations.
3. Forward citations, related work, and author/lab trails to follow development.
4. Recent journal articles, conference proceedings, early-access papers, and relevant preprints to locate the frontier.
5. Datasets, benchmarks, standards, patents, grants, policy documents, technical reports, open-source projects, and practitioner evidence when relevant.
6. Negative results, replications, critiques, retractions, failure cases, and robustness studies.

Use live search or connected databases for actual current-state research. Never imply that memory alone is a database search. Record the exact query, platform, filters, and date. Prefer primary sources for factual and novelty claims; use reviews for orientation and discovery.

For papers and technical reports, attempt lawful full-text acquisition after screening metadata. Download only openly accessible files such as open-access publisher PDFs, preprints, accepted manuscripts, author-hosted copies, institutional repository files, or public technical reports. Store downloaded files under `research/<topic-slug>/literature/papers/`, store metadata or citation exports under `research/<topic-slug>/literature/metadata/`, and record paywalled, inaccessible, or uncertain-access items in `research/<topic-slug>/literature/unavailable.md` with the DOI/URL, access date, and reason. Do not bypass access controls or imply that a paywalled source was fully read when only metadata or an abstract was available.

### 4. Screen and extract consistently

Define inclusion and exclusion rules before deep reading. Screen title/abstract first, then inspect full text for central items. Deduplicate versions and distinguish preprint, conference, and journal versions.

For each central source, capture:

- bibliographic identity and stable link/DOI;
- research question, context, sample/data, and method;
- baseline or comparison, outcomes, and uncertainty;
- contribution, assumptions, limitations, and failure cases;
- evidence strength, relevance, and relationship to other sources.

Create a human-readable comparison table in addition to any CSV evidence store. Use this minimum schema and adapt "data/sample" and "metrics/outcomes" to the discipline:

| Paper/source | Problem | Method | Data/sample | Metrics/outcomes | Main contribution | Limitations | Reusable insight |
|---|---|---|---|---|---|---|---|
| Citation + link | ... | ... | ... | ... | ... | ... | ... |

For a large corpus, keep the detailed matrix in a file and show a representative or decision-relevant subset in the response. Never omit a central source merely to keep the table short.

Do not treat citation count as quality. Check corrections, retractions, conflicts of interest, benchmark leakage, and whether conclusions exceed the evidence.

### 5. Synthesize by claims

Organize findings around questions, methods, evidence, and disagreement—not one paragraph per paper. Distinguish:

- established consensus;
- dominant but conditional findings;
- active disagreements;
- missing or weak evidence;
- recent signals that are promising but not mature.

Triangulate important claims across independent source types. Cite the source closest to each claim and mark inference explicitly.

Use visual synthesis whenever it clarifies structure or reasoning. For any report that covers field structure, method families, time development, evidence conflict, citation relationships, or research gaps, include 2-4 Mermaid diagrams in `report.md` and, when useful, mirror or expand them under `visuals/`. Prefer:

- `mindmap` for domain maps, concept maps, and taxonomy.
- `flowchart` for research pipelines, evidence chains, screening decisions, and method workflows.
- `timeline` for historical development and frontier waves.
- `graph` for relationships among papers, datasets, methods, institutions, benchmarks, or claims.
- `quadrantChart` or a compact table for value/feasibility positioning of candidate gaps.

Every diagram must be evidence-aware: label inferred groupings as inference, cite the sources or matrix rows that support important relationships, and avoid decorative diagrams that add no analytical value.

### 6. Test research gaps and novelty

Generate candidate gaps across problem, theory, method, data, evaluation, population/context, deployment, and conflicting evidence. For every candidate, test:

1. **Existence** — is it truly under-studied, or merely described with different vocabulary?
2. **Importance** — would resolving it change knowledge, decisions, or practice?
3. **Causality** — why has the gap persisted: no value, no data, hard measurement, or genuine opportunity?
4. **Feasibility** — can the user access data, tools, participants, expertise, time, and ethics approval?
5. **Distinctiveness** — what differs from the closest three to five works?
6. **Falsifiability** — what result would show the proposed contribution does not work?

Never state “no one has studied this.” Use bounded language such as “Within the searched databases, terms, languages, and date range, no directly equivalent study was found.” Treat a new model swap, dataset swap, or context swap as weak novelty unless it enables a meaningful new capability or inference.

### 7. Stop transparently

Stop when additional searches mostly reproduce known concepts and citation trails, all major branches have representative evidence, recent frontier venues have been checked, and major claims have support or an explicit evidence gap. Report coverage limits and unresolved uncertainty.

## Produce the deliverable

Match depth to the request. A useful report normally contains:

1. Scope, research questions, and topic-decomposition table.
2. Chinese/English keyword matrix and executable search strings.
3. Search strategy, source channels, screening rules, and coverage limits.
4. Field map or taxonomy and chronological/methodological development.
5. Article/source comparison table and detailed evidence matrix.
6. Consensus, disputes, failures, and frontier signals.
7. Ranked candidate gaps with supporting and defeating evidence.
8. Recommended next research questions or experiments.
9. Source list with stable links and access dates where appropriate.

When producing files, the primary user-facing deliverable is `research/<topic-slug>/report.md`. Supporting files such as scope notes, keyword matrices, search logs, evidence tables, visual drafts, and downloaded literature should live beside it in the same topic folder. Do not scatter deliverables in the project root.

If files are requested, keep them in the current project's established research/docs structure. If no structure exists, run:

```bash
python3 scripts/init_research_workspace.py --topic "<topic>" --root "<project-root>"
```

Populate the generated files rather than creating duplicate notes elsewhere. Downloaded literature must be organized under `literature/`; visual source snippets or diagram notes must be organized under `visuals/`.

## Enforce a quality gate

Before delivery, verify:

- every major conclusion is traceable to evidence;
- the topic decomposition and bilingual keyword matrix appear before findings;
- representative articles are compared in a structured table rather than only summarized serially;
- dates distinguish publication date from event/data date;
- recent claims were checked against current sources;
- contradictory evidence is represented fairly;
- primary and secondary evidence are not conflated;
- search limitations and inaccessible material are explicit;
- `report.md` exists when files are requested and contains the final integrated Markdown report;
- relevant Mermaid diagrams appear in `report.md` for field maps, development, evidence relationships, or gaps;
- downloaded literature, citation metadata, and unavailable-source notes are organized under `literature/`;
- candidate innovation is compared with its nearest prior art;
- recommendations separate evidence, inference, and speculation.
