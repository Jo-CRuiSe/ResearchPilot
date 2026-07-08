# Output Templates

Use these templates when producing a research report. Expand or adapt fields to the discipline, but do not silently remove core traceability fields.

## 1. Topic decomposition

| Dimension | Guiding question | Current definition | Boundary or exclusion |
|---|---|---|---|
| Object | What population, material, system, or phenomenon? | | |
| Problem | What question, mechanism, task, or pain point? | | |
| Method | What theory, technique, instrument, or intervention? | | |
| Context | In what application, geography, environment, or constraint? | | |
| Outcome | What effect, metric, cost, risk, or decision target? | | |

## 2. Bilingual keyword matrix

| Concept block | Chinese core terms | English core terms | Synonyms/variants/acronyms | Broader/narrower or adjacent terms | Ambiguous terms to exclude |
|---|---|---|---|---|---|
| Object | | | | | |
| Problem | | | | | |
| Method | | | | | |
| Context | | | | | |
| Outcome | | | | | |

## 3. Search-string plan

| Search purpose | Platform/source type | Exact query | Filters | Reason |
|---|---|---|---|---|
| Discover terminology | | | | |
| Find reviews | | | | |
| Find seminal work | | | | |
| Find recent frontier | | | | |
| Find failures/critiques | | | | |
| Validate novelty | | | | |

Preserve the query exactly as executed in the search log; do not replace it later with a cleaned-up approximation.

## 4. Article/source comparison

Default schema:

| Paper/source | Year | Problem | Method | Data/sample | Metrics/outcomes | Main contribution | Limitations | Reusable insight |
|---|---:|---|---|---|---|---|---|---|
| Citation + stable link | | | | | | | | |

Optional computational/AI extensions:

| Code/data | Baselines | Compute | Ablation | Robustness/generalization | Reproducibility |
|---|---|---|---|---|---|
| | | | | | |

Optional experimental/clinical extensions:

| Design | Sample size | Comparator | Effect size/uncertainty | Bias/validity | Replication |
|---|---:|---|---|---|---|
| | | | | | |

Optional humanities/social-science extensions:

| Theory | Corpus/archive | Analytical lens | Context | Alternative interpretation | Positionality/limits |
|---|---|---|---|---|---|
| | | | | | |

## 5. Claim synthesis

| Claim | Supporting sources | Contradicting/qualifying sources | Evidence strength | Conditions | Interpretation |
|---|---|---|---|---|---|
| | | | | | |

Use this table to prevent majority-by-paper-count reasoning. Weigh design quality, independence, relevance, and uncertainty.

## 6. Candidate gap ranking

| Candidate gap | Closest prior art | Why it matters | Evidence gap exists | Evidence against | Feasibility | Decisive test | Confidence |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Avoid a single unexplained numerical score. If ranking is needed, explain the ordinal criteria and preserve the underlying arguments.

## 7. Mermaid visualization templates

Use diagrams only when they clarify the analysis. Keep labels short and cite the table rows, source IDs, or references that justify non-obvious relationships.

### Domain or concept map

```mermaid
mindmap
  root((Research topic))
    Branch A
      Representative method or claim
      Key source IDs
    Branch B
      Dataset, population, or context
    Branch C
      Open problem
```

### Method or evidence flow

```mermaid
flowchart TD
  Q[Research question] --> S[Search and screening boundary]
  S --> E1[Evidence cluster A]
  S --> E2[Evidence cluster B]
  E1 --> C[Supported claim]
  E2 --> L[Limitation or contradiction]
  C --> G[Candidate gap]
  L --> G
```

### Development timeline

```mermaid
timeline
  title Field development
  2000 : Foundational concept or baseline
  2015 : Method family becomes practical
  2022 : Benchmark, dataset, or deployment shift
  2026 : Current frontier signal
```

### Relationship graph

```mermaid
graph LR
  P1[Source A] --> M1[Method family]
  P2[Source B] --> M1
  M1 --> D1[Dataset or setting]
  M1 --> C1[Claim]
  C2[Contradicting claim] -. qualifies .-> C1
```

### Gap positioning

```mermaid
quadrantChart
  title Candidate gaps by importance and feasibility
  x-axis Low feasibility --> High feasibility
  y-axis Low importance --> High importance
  quadrant-1 Prioritize
  quadrant-2 Important but hard
  quadrant-3 Defer
  quadrant-4 Quick validation
  Gap A: [0.78, 0.82]
  Gap B: [0.38, 0.74]
```

If the renderer does not support `quadrantChart`, replace it with a compact table using the same axes and rationale.

## 8. Literature file index

| Source ID | Local file | Title | DOI/URL | Access status | Download or access date | Rights/access note |
|---|---|---|---|---|---|---|
| S01 | `literature/papers/s01-author-year-short-title.pdf` | | | downloaded / metadata-only / unavailable | | |

Use stable, deduplicated file names. Distinguish preprint, conference, journal, accepted manuscript, and technical-report versions when they differ.

For unavailable sources, also record them in `literature/unavailable.md`:

| Source ID | Title | DOI/URL | Attempted source | Date | Reason not downloaded | How it was used |
|---|---|---|---|---|---|---|
| | | | publisher / DOI / repository / author page | | paywalled / access denied / no PDF / uncertain rights | metadata only / abstract only / excluded |

## 9. Final `report.md` skeleton

1. Executive conclusion
2. Scope and research questions
3. Topic decomposition
4. Bilingual keywords and search strings
5. Search method and coverage limits
6. Field map and development, including Mermaid diagrams where useful
7. Article/source comparison
8. Consensus and conditional findings
9. Disputes, failures, and boundary conditions
10. Recent frontier signals
11. Candidate research gaps, including gap positioning when useful
12. Recommended research questions or experiments
13. Literature files and unavailable sources
14. Limitations of this investigation
15. References
