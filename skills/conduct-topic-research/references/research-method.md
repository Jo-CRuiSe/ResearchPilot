# Research Method Reference

Use this reference for substantial rapid scans, systematic investigations, and novelty checks.

## 1. Scope card

Complete this card before searching:

| Field | Decision |
|---|---|
| Working topic | User wording plus normalized field term |
| Intended decision | Learn, select a topic, write a review, design a study, or validate novelty |
| Core questions | Three to seven answerable questions |
| Disciplines | Primary and adjacent fields |
| Time window | Foundational range plus recent frontier range |
| Languages/geography | Included and excluded |
| Evidence types | Papers, reviews, patents, standards, datasets, projects, interviews, etc. |
| Exclusions | Explicit reasons, not convenience after seeing results |

## 2. Concept matrix

Build term blocks for:

| Block | Include |
|---|---|
| Object | Formal name, common name, subtype, population |
| Problem | Task, mechanism, phenomenon, pain point |
| Method | Theory, algorithm, instrument, intervention |
| Context | Sector, environment, geography, constraints |
| Outcome | Performance, behavior, cost, safety, social effect |

For each block, include Chinese/English forms, spelling variants, acronyms, historical names, and terms used by adjacent disciplines.

General Boolean pattern:

```text
(object synonyms) AND (problem synonyms) AND (method OR outcome terms)
```

Create several queries instead of one over-constrained query:

- discovery: object + problem;
- method: problem + method family;
- frontier: core query + recent method/benchmark term;
- limitations: core query + limitation/failure/robustness/replication;
- novelty: exact proposed contribution + synonyms + nearest alternative;

## 3. Source portfolio

Choose sources by discipline rather than using every database mechanically.

| Purpose | Useful source types |
|---|---|
| Field map | Recent reviews, handbooks, authoritative reports |
| Foundations | Seminal papers/books and backward citations |
| Current frontier | Recent journals, proceedings, early access, preprints |
| Evidence quality | Replications, meta-analyses, critiques, retractions |
| Engineering reality | Standards, benchmarks, datasets, repositories, issue trackers |
| Commercial novelty | Patents, products, company technical material |
| Public relevance | Policy, regulation, grants, government statistics |

Use at least two independent discovery routes for high-confidence coverage: for example, keyword search plus citation chaining, or a bibliographic database plus a field-specific repository.

## 4. Full-text acquisition and file organization

After title/abstract screening, attempt lawful full-text access for included central sources.

Access priority:

1. DOI or publisher page for canonical metadata, version, and licensing.
2. Open-access publisher PDF when explicitly available.
3. arXiv, OpenReview, PubMed Central, SSRN, HAL, institutional repositories, government or standards portals, and other legitimate open repositories.
4. Author homepages, lab pages, or project pages that host a public manuscript.
5. Metadata-only record when no lawful full text is available.

Download only files that are openly accessible or that the user is authorized to access. Do not bypass paywalls, login gates, robots restrictions, or license limits. If access is unavailable or rights are uncertain, record the item in `literature/unavailable.md` with the attempted source, date, reason, and whether only metadata or abstract evidence was used.

Store files under:

```text
research/<topic-slug>/literature/
├── papers/
├── metadata/
└── unavailable.md
```

Use stable file names:

```text
sNN-first-author-year-short-title-version.ext
```

Examples:

```text
s03-vaswani-2017-attention-is-all-you-need-conference.pdf
s03-vaswani-2017-attention-is-all-you-need-arxiv.pdf
s12-smith-2024-benchmark-survey-metadata.json
```

Deduplicate by DOI, arXiv ID, title, authors, year, and venue. Preserve distinct versions only when they differ materially, and label the version in both the file name and the literature index.

## 5. Visualization selection

Choose Mermaid diagrams according to the research question:

| Analytical need | Preferred diagram | Use when |
|---|---|---|
| Domain structure or taxonomy | `mindmap` | The user needs a quick map of branches, concepts, and boundaries |
| Method pipeline or evidence logic | `flowchart` | The synthesis depends on screening, causal chains, workflows, or decision paths |
| Historical development | `timeline` | The field has meaningful waves, milestones, or frontier shifts |
| Relationships among papers, methods, datasets, or claims | `graph` | The analysis compares influence, reuse, contradiction, or convergence |
| Research-gap prioritization | `quadrantChart` or table | Gaps differ by importance, feasibility, evidence strength, or risk |

Prefer two to four diagrams in `report.md` for a substantial report. Add more only if each diagram answers a distinct analytical question. Label inferred groupings and connect important diagram relationships to source IDs, evidence-matrix rows, or citations.

## 6. Search log schema

Record one row per search:

```text
date,platform,query,filters,result_count,screened_count,included_count,notes
```

Do not fabricate result counts when a platform does not expose them. Record `not reported`.

## 7. Evidence matrix schema

Record one row per distinct study or authoritative source:

```text
source_id,title,year,source_type,research_question,context_or_sample,method_or_intervention,
comparison,outcomes,key_result,limitations,evidence_strength,relevance,doi_or_url,notes
```

Use transparent evidence labels such as `high / medium / low / unclear` and explain the criteria for the domain. Do not calculate a universal score that disguises judgment.

## 8. Discipline adapters

### Experimental, clinical, and behavioral research

Check study design, sampling, preregistration, power, measurement validity, attrition, effect size, uncertainty, multiple testing, external validity, ethics, and replication.

### Computational and AI research

Check data provenance, train/test contamination, baseline fairness, ablation, compute budget, random seeds, confidence intervals, benchmark saturation, code/data availability, robustness, distribution shift, and real-world utility.

### Engineering and applied research

Check requirements, operating conditions, maturity level, safety, standards, manufacturability, cost, maintainability, scalability, integration constraints, and field validation.

### Humanities and social sciences

Check theoretical lineage, archive/corpus selection, positionality, translation, historical context, interpretive alternatives, representativeness, causal identification where claimed, and whether concepts travel across cultures.

## 9. Gap ledger

For each proposed gap, maintain both supporting and defeating evidence:

| Field | Question |
|---|---|
| Gap statement | What exactly is missing or unresolved? |
| Closest prior art | Which three to five works are nearest? |
| Supporting evidence | Why believe the gap exists and matters? |
| Defeating evidence | What may mean it is already solved or unimportant? |
| Root cause | Why has it persisted? |
| Proposed contribution | New knowledge, capability, evidence, or method |
| Feasibility | Data, method, access, time, cost, ethics |
| Decisive test | What experiment or analysis could resolve it? |
| Confidence | High, medium, or low, with rationale |

## 10. Saturation and completion

Consider the map provisionally saturated when:

- new searches add few new concepts, branches, or representative studies;
- backward and forward citation trails converge on recurring sources;
- all major methodological families have coverage;
- the latest relevant venues and repositories have been checked;
- central claims have corroboration or are labeled uncertain;
- exclusions and inaccessible sources are documented.

Saturation supports bounded completeness, not universal completeness.

## 11. Recommended synthesis language

Prefer:

- “Evidence from X and Y converges on …, under the conditions …”
- “The literature disagrees, plausibly because studies differ in …”
- “This is a recent signal rather than an established result.”
- “No directly equivalent work was found within the recorded search boundary.”
- “The proposed novelty depends on whether …; the nearest prior art is …”

Avoid:

- “The literature proves …” when evidence is observational or mixed.
- “This field is blank” without a recorded, reproducible search.
- “Highly cited means reliable.”
- “Recent means better.”
- “Different setting/model/dataset automatically means innovation.”
