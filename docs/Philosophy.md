# Genesee: Product Philosophy

## The Vision

Build a comprehensive tool for biological, medical, and clinical scientists to do research.

The domain is vast:
- **Wet lab:** DNA/RNA analysis, primer design, cloning strategies
- **Computational biology:** Sequence alignment, variant calling, pathway analysis
- **Translational research:** Biomarker discovery, target validation
- **Clinical development:** Trial design, patient stratification
- **Regulatory:** FDA submissions, companion diagnostic requirements

One platform. The entire research lifecycle.

---

## The Trap We're Avoiding

The temptation is to build 20 tools:
- A primer designer
- A BLAST interface
- A pathway visualizer
- A trial search engine
- A regulatory chatbot

Each individually useful. None complete. Users bounce between them, context lost at every boundary. This is the current state of bioinformatics software: fragmented, specialized, disconnected.

**We refuse to build another collection of disconnected features.**

---

## The Philosophy: One Working Flow First

> "Don't boil the ocean. Nail one complete workflow before adding the next."

A "working flow" means:
1. **Clear input** — what the user brings to the tool
2. **Real processing** — the tool does meaningful work
3. **Valuable output** — something the user can act on immediately

Not a demo. Not a prototype. A tool that solves a real problem, end-to-end, today.

### Why This Matters

1. **Proves value immediately** — Users can accomplish real work on day one
2. **Forces hard integration decisions** — We learn what's actually hard
3. **Creates a foundation** — The second workflow builds on the first
4. **Earns trust** — One excellent experience beats ten mediocre ones

---

## Why Biomarker Validation First

We considered several candidate workflows:

| Workflow | Description |
|----------|-------------|
| Primer design | Gene → validated primers ready to order |
| Biomarker validation | Candidate marker → evidence synthesis → recommendation |
| Clinical trial feasibility | Indication → eligibility criteria → site recommendations |
| Regulatory pathway | Drug/device → FDA pathway + requirements |

### Decision Criteria

**1. First user alignment**

Our first user is Dr. Jianhui Ma — a translational cancer researcher at BeOne Medicines with MD/PhD training in molecular biology. Her expertise:
- mTOR signaling pathways
- DNA repair mechanisms in glioblastoma
- Tumor suppressor biology (PTEN)
- ctDNA for cancer monitoring

She operates at the **translational layer** — taking biological insights and building the scientific case for clinical validation. Biomarker validation is her daily work.

**2. Pain intensity**

Current biomarker investigation requires:
- 6+ browser tabs (PubMed, ClinicalTrials.gov, COSMIC, cBioPortal, FDA, KEGG...)
- Hours of manual searching and copy-pasting
- Synthesis into PowerPoint for team presentation
- No structured framework — easy to miss sources
- Difficult to compare candidates systematically

The pain is acute, frequent, and time-consuming.

**3. AI leverage**

Biomarker validation is an ideal AI application:
- Information retrieval across structured databases
- Synthesis of unstructured literature
- Pattern recognition across sources
- Structured report generation

The task requires breadth (many sources) and synthesis (combining into insight) — exactly what LLMs excel at.

**4. Data accessibility**

Critical data sources are publicly available:
- PubMed (NCBI E-utilities API)
- ClinicalTrials.gov (public API)
- cBioPortal (open source, open API)

No licensing roadblocks for MVP.

**5. Clear output value**

The output is a presentation-ready evidence package. Success is measurable: "Can she walk into a meeting with the clinical biomarker team and make her case using only what the tool produced?"

### What We're NOT Starting With

**Primer design** — Well-served by existing tools (Primer3, IDT). Commodity problem.

**Clinical trial feasibility** — Requires proprietary site data, complex eligibility parsing. Higher barriers.

**Regulatory pathway** — Highly specialized, narrow user base, requires deep FDA expertise.

---

## The Expansion Principle

Once biomarker validation works, we expand along natural edges:

```
                    Biomarker Validation (V1)
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
      Multi-marker      Pathway         Trial
       Comparison       Context       Matching
            │               │               │
            └───────────────┼───────────────┘
                            ▼
                    Target Assessment
                    (Is this druggable?)
                            │
                            ▼
                    Competitive Intel
                    (Who else is working on this?)
                            │
                            ▼
                    Clinical Strategy
                    (How to design the trial?)
```

Each expansion:
- Builds on data already gathered
- Serves the same user persona
- Adds capability without breaking existing workflows

---

## Design Principles

### 1. Real Data, Real Sources

Never hallucinate. Every claim traced to a citation. Every number from an authoritative database. Users must trust the output enough to present it to colleagues.

### 2. Agentic, Not Mechanical

Not a form with fixed inputs and outputs. An intelligent assistant that understands context, calls tools as needed, and lets the user decide what to keep.

Like Claude Code, but for biomedical research:
- Project/directory aware
- Natural language interaction
- Tools invoked automatically
- Results are interactive (save, discard, refine)

### 3. TUI First, Intuitive Always

The user runs `genesee` — nothing else. No commands, no flags, no arguments. Everything happens inside an intuitive TUI (Text User Interface).

Why TUI over CLI commands:
- **Zero learning curve** — no syntax to memorize
- **Guided experience** — the interface leads the user through each step
- **Immediate feedback** — see results as they come in
- **Non-technical friendly** — our first user is a scientist, not a developer

Why TUI over web GUI:
- **No deployment complexity** — just run it
- **Local-first** — data stays on machine
- **Fast iteration** — easier to build and refine
- **Terminal is universal** — works anywhere

The interface should be so intuitive that a non-technical user can accomplish their task without confusion or documentation.

### 4. Synthesis, Not Just Search

Search is table stakes. The value is synthesis:
- Across sources (literature + trials + genomics)
- Across evidence types (publications + data + regulatory)
- Into actionable insight (strength score, gaps, recommendations)

### 5. Output-Driven Design

Start with the output and work backwards:
- What does the PPT slide need to say?
- What evidence supports each point?
- What data sources provide that evidence?
- What queries retrieve that data?

The workflow is designed around the deliverable.

---

## Success Definition

**V1 is successful when:**

Dr. Ma runs `genesee`, and without hesitation or confusion, walks into her biomarker team meeting 10 minutes later with a presentation that:
- Summarizes the evidence landscape
- Cites authoritative sources
- Identifies evidence gaps
- Makes a clear recommendation
- Answers the team's first-level questions

**The usability bar:**
- She never asks "how do I...?"
- She never reads documentation
- She never feels lost

If she can do that, we've built something real.

---

## What This Document Is For

This philosophy guides every decision:

- **Feature requests:** Does this serve the working flow, or is it a distraction?
- **Prioritization:** What moves us toward a complete workflow fastest?
- **Architecture:** Does this enable future expansion, or paint us into a corner?
- **Quality bar:** Would Dr. Ma trust this in a team meeting?

When in doubt, return to the principle: **One working flow, done well, before anything else.**
