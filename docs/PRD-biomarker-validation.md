# PRD: Biomarker Validation Workflow

## Overview

**Product:** Genesee - Biomarker Evidence Synthesis Tool
**Company:** Genesee Sciences
**Target User:** Translational cancer researchers in biotech/pharma
**First User:** Dr. Jianhui Ma, BeOne Medicines

---

## The Job to Be Done

> "Help me build a compelling evidence package for a candidate biomarker so I can convince the clinical biomarker team to run validation experiments."

| State       | Experience                                                             |
| ----------- | ---------------------------------------------------------------------- |
| **Current** | 6+ browser tabs, manual copy-paste, hours of work → PPT                |
| **Desired** | Input biomarker → structured investigation → presentation-ready output |

---

## Problem Statement

When a translational researcher identifies a candidate biomarker (gene, mutation, protein), they must manually investigate its validity across 6+ fragmented data sources before presenting a recommendation to the clinical biomarker team.

**Current workflow pain points:**

- 6+ browser tabs open simultaneously
- Manual searches across PubMed, ClinicalTrials.gov, FDA, COSMIC, cBioPortal, KEGG, etc.
- Copy-paste evidence into PowerPoint slides
- No structured framework - easy to miss important sources
- Time-consuming: hours per biomarker candidate
- Difficult to compare multiple candidates systematically

**Consequence:** Slow decision-making, inconsistent evidence quality, researcher frustration.

---

## Solution

An AI-powered tool that takes a candidate biomarker as input and produces a structured evidence synthesis ready for presentation and team discussion.

**One sentence:** "From candidate biomarker to evidence-backed presentation in minutes, not hours."

---

## Target User Profile

| Attribute | Description                                                                                                        |
| --------- | ------------------------------------------------------------------------------------------------------------------ |
| Role      | Translational researcher, Principal Scientist, Research Director                                                   |
| Domain    | Oncology / Cancer biology                                                                                          |
| Education | PhD or MD/PhD in molecular biology, cell biology, or related                                                       |
| Context   | Biotech or pharma company with clinical development pipeline                                                       |
| Workflow  | Identifies targets/biomarkers → builds evidence case → hands off to clinical biomarker team for validation studies |

**Key insight:** The user is not running the experiments. They are building the scientific rationale for _why_ the biomarker team should invest resources in validation.

---

## Core Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│  INPUT                                                          │
│  ─────                                                          │
│  • Biomarker (gene symbol, mutation, protein)                   │
│  • Cancer type / indication (e.g., NSCLC, GBM, breast)         │
│  • Optional: specific hypothesis or context                     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  INVESTIGATION ENGINE                                           │
│  ────────────────────                                           │
│  Parallel queries across:                                       │
│  1. Literature (PubMed) - publications, reviews, meta-analyses  │
│  2. Clinical trials (ClinicalTrials.gov) - active/completed     │
│  3. FDA (companion diagnostics, approvals)                      │
│  4. Mutation databases (COSMIC, cBioPortal) - frequencies       │
│  5. Pathway databases (KEGG, Reactome) - mechanism context      │
│  6. Commercial assays - available validated kits                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  SYNTHESIS & SCORING                                            │
│  ───────────────────                                            │
│  • Evidence strength assessment                                 │
│  • Gap identification (what's missing?)                         │
│  • Conflict detection (contradictory findings)                  │
│  • Recommendation generation                                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  OUTPUT                                                         │
│  ──────                                                         │
│  • Structured report (markdown)                                 │
│  • Presentation-ready slides (PPT export)                       │
│  • Evidence table with citations                                │
│  • Recommended next steps for validation team                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Data Sources (MVP)

| Source                 | Data Type                          | Access Method                 |
| ---------------------- | ---------------------------------- | ----------------------------- |
| **PubMed**             | Publications, abstracts            | NCBI E-utilities API          |
| **ClinicalTrials.gov** | Trial protocols, status            | ClinicalTrials.gov API        |
| **FDA**                | Companion diagnostics, drug labels | FDA API / web scrape          |
| **COSMIC**             | Somatic mutation frequencies       | COSMIC API (requires license) |
| **cBioPortal**         | Cancer genomics data               | cBioPortal API (open)         |
| **KEGG**               | Pathway maps                       | KEGG API                      |
| **Reactome**           | Pathway data                       | Reactome API                  |

**MVP priority:** PubMed + ClinicalTrials.gov + cBioPortal (all open access)

---

## Output Specification

### Structured Report Sections

1. **Executive Summary**

   - Biomarker overview (gene function, known roles)
   - Evidence strength score (Strong / Moderate / Weak / Insufficient)
   - Key finding highlights
   - Recommendation

2. **Literature Evidence**

   - Key publications (ranked by relevance)
   - Publication trends (is interest growing?)
   - Notable authors/institutions

3. **Clinical Evidence**

   - Trials using this biomarker (as inclusion criteria, endpoint, or stratification)
   - Trial phases and status
   - Sponsor companies (competitive landscape)

4. **Genomic Evidence**

   - Mutation frequency in target cancer type
   - Co-occurring mutations
   - Comparison across cancer types

5. **Regulatory Status**

   - FDA-approved companion diagnostics
   - Relevant drug approvals mentioning this biomarker

6. **Pathway Context**

   - Signaling pathway membership
   - Upstream/downstream relationships
   - Druggable nodes in pathway

7. **Evidence Gaps**

   - What data is missing?
   - Suggested validation experiments

8. **References**
   - Full citation list with links

---

## User Experience

### Core Concept: Claude Code for Biomedical Research

The model is **agentic chat**, not forms. Like Claude Code, but specialized for life sciences:

- Run `genesee` in a project directory
- Chat naturally about your research
- Tools get called automatically (PubMed, trials, genomics, etc.)
- Results appear in a rich TUI
- You decide what to keep

### Project Structure

Researchers have multiple ongoing projects, each with subprojects:

```
~/research/
├── egfr-nsclc-study/           ← run `genesee` here
│   ├── literature/
│   ├── biomarkers/
│   ├── notes.md
│   └── .genesee/            ← project state/history
│       ├── history.json
│       ├── cache/
│       └── lancedb/            ← vector embeddings
├── pten-gbm-resistance/
└── ctdna-monitoring-panel/
```

Each directory is a project context. Genesee scans files, builds a tree, understands what you're working on.

### Launch

```bash
$ cd ~/research/egfr-nsclc-study
$ genesee
```

### TUI Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  🧬 Genesee                                          egfr-nsclc-study       │
├────────────────────────┬────────────────────────────────────────────────────┤
│                        │                                                    │
│  📁 Project Files      │  Chat                                              │
│  ──────────────────    │  ────                                              │
│  ▼ egfr-nsclc-study    │                                                    │
│    ▼ literature/       │  You: What's the mutation frequency of EGFR in     │
│      review-2024.pdf   │       NSCLC patients?                              │
│      key-papers.md     │                                                    │
│    ▼ biomarkers/       │  ┌─────────────────────────────────────────────┐   │
│      candidates.csv    │  │ 🔧 Tool: cBioPortal                         │   │
│    notes.md            │  │ Querying EGFR mutations in lung cancer...   │   │
│                        │  └─────────────────────────────────────────────┘   │
│                        │                                                    │
│                        │  Genesee: Based on cBioPortal data, EGFR mutations   │
│                        │  occur in approximately 15-20% of NSCLC cases.     │
│                        │                                                    │
│                        │  The most common mutations are:                    │
│                        │  • Exon 19 deletions (45%)                         │
│                        │  • L858R point mutation (40%)                      │
│                        │  • T790M (acquired resistance)                     │
│                        │                                                    │
│                        │  ┌──────────────┐ ┌──────────────┐                 │
│                        │  │ 💾 Save      │ │ 📋 Copy      │                 │
│                        │  └──────────────┘ └──────────────┘                 │
│                        │                                                    │
├────────────────────────┴────────────────────────────────────────────────────┤
│  > Ask anything about your research...                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Agentic Workflow

User asks naturally, tools are called as needed:

```
You: Find recent clinical trials for EGFR inhibitors in NSCLC

┌─────────────────────────────────────────────────────────────┐
│ 🔧 Tool: ClinicalTrials.gov                                 │
│ Searching: EGFR inhibitor AND NSCLC, Phase 2-3, 2023-2024   │
│ Found: 47 trials                                            │
└─────────────────────────────────────────────────────────────┘

Genesee: I found 47 recent trials. Here are the most relevant:

1. **NCT05774951** - Osimertinib + Chemotherapy (Phase 3)
   Sponsor: AstraZeneca | Status: Recruiting

2. **NCT05504044** - Amivantamab + Lazertinib (Phase 3)
   Sponsor: Janssen | Status: Active

3. **NCT05388669** - CLN-081 for EGFR Exon 20 (Phase 2)
   Sponsor: Cullinan | Status: Recruiting

┌──────────────┐ ┌──────────────┐ ┌──────────────────────┐
│ 💾 Save All  │ │ 📊 Export    │ │ 🔍 Show More (44)    │
└──────────────┘ └──────────────┘ └──────────────────────┘
```

### Tool Results are Interactive

When tools return results, the user can:

- **Save** — add to project files
- **Copy** — to clipboard
- **Export** — to markdown, CSV, or PPT
- **Discard** — don't keep this result
- **Refine** — ask follow-up questions

### Subagents (MVP)

These aren't simple function calls — they're **specialized subagents** that can reason, make multiple API calls, and synthesize results. Like Claude Code's Task tool spawning agents.

| Subagent     | Capability                                                                                          |
| ------------ | --------------------------------------------------------------------------------------------------- |
| `literature` | Searches PubMed + Semantic Scholar, filters by relevance, summarizes key findings, tracks citations |
| `trials`     | Queries ClinicalTrials.gov, understands phases/status, identifies competitors                       |
| `genomics`   | Queries cBioPortal, interprets mutation frequencies, finds co-occurring alterations                 |
| `chemistry`  | Queries PubChem/ChEMBL, retrieves compound structures, drug properties, ADMET data                  |
| `files`      | Reads/writes project files, understands context from existing documents                             |
| `synthesize` | Combines information from multiple sources into coherent summaries                                  |

Each subagent:

- Understands natural language intent
- Makes multiple API calls if needed
- Filters and ranks results
- Returns structured, actionable output

### Context Awareness

Genesee understands project context:

```
You: What biomarkers should I add to this panel?

Genesee: Based on your project files, you're studying EGFR resistance
in NSCLC. Looking at candidates.csv, you already have:
- EGFR (primary)
- KRAS (exclusion)
- T790M (resistance)

Let me search for commonly co-occurring mutations...

┌─────────────────────────────────────────────────────────────┐
│ 🔧 Tool: cBioPortal                                         │
│ Querying co-mutations with EGFR in lung adenocarcinoma...   │
└─────────────────────────────────────────────────────────────┘
```

### Navigation

- **Type** — chat naturally
- **↑/↓** — scroll through history
- **Tab** — switch between file tree and chat
- **Enter** — send message / confirm action
- **Esc** — cancel current operation
- **Ctrl+S** — save current results

---

## MVP Scope

### In Scope (V1)

- **TUI with agentic chat** (just run `genesee`)
- **Project awareness** — scans directory, builds file tree, understands context
- **Natural language input** — ask questions, get answers
- **Core subagents:**
  - `literature` — PubMed search, filtering, summarization
  - `trials` — ClinicalTrials.gov search, parsing, ranking
  - `genomics` — cBioPortal queries, interpretation
  - `chemistry` — PubChem/ChEMBL, compound data, drug properties
  - `files` — read/write project files, context extraction
- **Interactive results** — save, copy, export, discard
- **Conversation history** — persisted in `.genesee/`
- **Markdown export**

### Out of Scope (V1)

- PPT export (Phase 2)
- COSMIC integration (requires license)
- FDA database integration (complex scraping)
- Pathway visualization
- Multi-project dashboard
- Team collaboration features

---

## Success Metrics

| Metric                         | Target                                     |
| ------------------------------ | ------------------------------------------ |
| Time to first investigation    | < 1 minute from launch (no learning curve) |
| Time to complete investigation | < 10 minutes (vs. hours)                   |
| Data sources covered           | 3+ per query                               |
| User satisfaction (first user) | "I would use this daily"                   |
| Zero confusion                 | No "how do I...?" questions                |
| Output usability               | Directly usable in team meeting            |

---

## Technical Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      TUI Interface                          │
│                       (Textual)                             │
│  ┌──────────────┐  ┌────────────────────────────────────┐   │
│  │  File Tree   │  │  Chat Panel                        │   │
│  │  (project)   │  │  (conversation + subagent results) │   │
│  └──────────────┘  └────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   Orchestrator Agent                        │
│      Understands intent, spawns subagents, synthesizes      │
└─────────────────────────────────────────────────────────────┘
                            │
      ┌─────────────────────┼─────────────────────┐
      ▼                     ▼                     ▼
┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐
│literature │   │  trials   │   │ genomics  │   │ chemistry │
│           │   │           │   │           │   │           │
│ • PubMed  │   │ • CTgov   │   │• cBioPortal│  │ • PubChem │
│ • filter  │   │ • parse   │   │• interpret│   │ • ChEMBL  │
│ • summary │   │ • rank    │   │• correlate│   │ • ADMET   │
└───────────┘   └───────────┘   └───────────┘   └───────────┘
      │               │               │               │
      └───────────────┴───────────────┴───────────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
       ┌─────────────┐             ┌─────────────┐
       │    files    │             │  synthesize │
       │             │             │             │
       │ • read      │             │ • combine   │
       │ • write     │             │ • cite      │
       │ • context   │             │ • conclude  │
       └─────────────┘             └─────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   Project State                              │
│  .genesee/history.json  — conversation history           │
│  .genesee/cache/        — cached API responses           │
│  .genesee/lancedb/      — vector embeddings (LanceDB)    │
│  project files             — user's research documents      │
└─────────────────────────────────────────────────────────────┘
```

---

## Existing Components (from genesee-desktop)

The `genesee-desktop` PySide6 project has reusable backend components:

| Module                       | Description                                | Reuse                                       |
| ---------------------------- | ------------------------------------------ | ------------------------------------------- |
| `search/pubmed.py`           | PubMed E-utilities API client, XML parsing | ✅ Direct                                   |
| `search/semantic_scholar.py` | Semantic Scholar API client                | ✅ Direct                                   |
| `search/arxiv.py`            | ArXiv search client                        | ✅ Direct                                   |
| `search/vector_search.py`    | Vector/semantic search                     | 🔄 Rewrite with LanceDB                     |
| `ai/providers.py`            | Anthropic, OpenAI, Ollama abstraction      | ✅ Direct                                   |
| `ai/embeddings.py`           | Embedding generation                       | ✅ Direct                                   |
| `core/document.py`           | Document model with sources, chunking      | ✅ Direct                                   |
| `core/pdf_processor.py`      | PDF text extraction                        | ✅ Direct                                   |
| `core/database.py`           | SQLite for document metadata               | 🔄 Adapt (metadata only, vectors → LanceDB) |
| `ui/*`                       | PySide6 widgets                            | ❌ Replace with Textual                     |

**Strategy:** Extract the `search/`, `ai/`, and `core/` modules into a shared package, then build TUI on top.

---

## Open Questions

1. **Authentication:** Do we need user accounts, or is this a local-first tool?
2. **Data freshness:** Cache results? How long?
3. **LLM choice:** Claude API for synthesis? Local model option?
4. **PPT templates:** Should we allow custom branding/templates?
5. **Validation team handoff:** Any integration with lab systems?

---

## Roadmap (Features, not timeline)

### Phase 1: Agentic Chat Foundation

- TUI with file tree + chat panel
- Orchestrator agent + subagent architecture
- Core subagents: `literature`, `trials`, `genomics`, `chemistry`, `files`
- Project directory scanning and context
- Conversation history persistence
- Interactive results (save, copy, discard)

### Phase 2: Enhanced Output & Export

- PPT export with professional template
- Structured report generation
- Evidence strength scoring
- Gap analysis summaries

### Phase 3: Extended Data Sources

- COSMIC integration
- FDA companion diagnostics
- KEGG/Reactome pathways
- UniProt protein data

### Phase 4: Deeper Context Awareness

- Parse and understand PDFs in project
- Cross-reference project files with external data
- Smart suggestions based on project state

### Phase 5: Multi-Project & Collaboration

- Project dashboard (switch between projects)
- Shareable reports
- Team annotations
- Integration with internal knowledge bases

---

## Appendix: Competitive Landscape

| Tool                   | Strength                       | Weakness                                  |
| ---------------------- | ------------------------------ | ----------------------------------------- |
| **Manual research**    | Flexible, trusted              | Slow, inconsistent                        |
| **Ingenuity (QIAGEN)** | Comprehensive pathway analysis | Expensive, complex, not biomarker-focused |
| **cBioPortal**         | Great genomic data             | No synthesis, no literature               |
| **PubMed**             | Authoritative literature       | No structure, manual work                 |
| **ChatGPT/Claude**     | Fast synthesis                 | No real-time data, hallucination risk     |
| **Claude Code**        | Agentic, project-aware, tools  | Built for software, not life sciences     |

**Our positioning:** Claude Code for biomedical research.

**Our differentiator:**

- Real-time data from authoritative biomedical sources (PubMed, trials, genomics)
- AI synthesis with citations
- Project-aware context
- Specialized tools for life sciences workflows
- Rich TUI designed for non-developers
