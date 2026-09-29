---
name: linkedin-research
description: "Research LinkedIn content, people, companies, profiles, jobs and saved posts using supplied material or an authorized available source."
---

# Research and discovery

Use the shared scope and factual rules in the [master skill](../../SKILL.md).
This module can be read directly but requires the repository references.

## Inputs

Question, topic or URL; desired scope and time window when material.

## Workflow

1. Identify the question and the required source type: post, person, company, jobs, saved posts or public topic evidence.
2. Reuse supplied content. For current technical topics, find primary documentation and compare publication and event dates. For account-specific data, check that a supported reading integration is authorized and available.
3. Select only the needed fields and action. The browsing registry has five action references: post-data, profile-data, company-data, job-search and saved-posts. Load the matching reference through the inventory when needed.
4. Keep canonical URL, source, observation date and relevant evidence with each result. Deduplicate by stable identifiers, retaining ambiguity instead of merging different people.
5. Distinguish inaccessible content, zero results and incomplete pagination. Do not infer post text or profile details from a URL slug, or call popularity a trend without observations over time.

## Deliverable

Source-backed brief or structured records with evidence, dates, coverage and gaps.

## Detailed guidance

- [content methods](../../references/content-methods.md)
- [integration knowledge](../../references/integration-knowledge.md)
