---
name: linkedin-analytics
description: "Analyze supplied LinkedIn post results and engager records, with explicit metric definitions, missing data and uncertainty."
---

# Performance and audience analysis

Use the shared scope and factual rules in the [master skill](../../SKILL.md).
This module can be read directly but requires the repository references.

## Inputs

Exports or supplied counts, observation period, goal and optional professional audience criteria.

## Workflow

1. Inspect available fields, time windows and post ages. Retain missing values and clarify which outcome matters: reach, conversation, saves, collaboration or business results.
2. Calculate engagement rate, comment ratio and reach multiple only with valid denominators using engagement-and-analysis.md. Label percent versus ratio and weighted aggregate versus mean post rate.
3. Compare similar cohorts by topic, format, hook and age. Show evidence and sample sizes; do not infer causation from timing or a handful of posts.
4. For audience analysis, deduplicate known engagers and assess user-specified professional fit from actual fields. Mark unknowns and do not identify anonymous viewers or equate a like with buying intent.
5. Identify useful experiments and changes for the next plan. Distinguish source-author benchmarks from this account's measurements.
6. Use the spreadsheet skill when handling spreadsheet files. Do not claim live account analytics unless a supported authorized source actually supplied it.

## Deliverable

Metric table, evidence-backed findings, uncertainty and practical next experiments; optional audience roster with observed fit.

## Detailed guidance

- [engagement and analysis](../../references/engagement-and-analysis.md)
