---
name: linkedin-comments
description: "Draft contextual LinkedIn comments and replies, triage supplied inbox messages and review thread follow-up status."
---

# Comments, replies and inbox triage

Use the shared scope and factual rules in the [master skill](../../SKILL.md).
This module can be read directly but requires the repository references.

## Inputs

Post and relevant thread or inbox messages, including author/target information available to the user.

## Workflow

1. Read the actual source and surrounding exchange. Distinguish top-level comments, nested replies and private messages before drafting.
2. A comment should contribute a sourced fact, missing condition, useful example, direct answer or respectful correction. Avoid generic praise and paraphrasing the whole post.
3. For replies, answer the real question, acknowledge valid disagreement and retain target context. Do not invent experience or reply to the user's own comment as another person.
4. For batches, group substantive questions, collaboration opportunities, peers, simple support and noise. Deduplicate and report skipped categories. Produce the requested drafts together unless the user asks for staged review.
5. For inbox triage, classify leads, recruiters, peers, specific asks and unwanted pitches using visible evidence; draft appropriate responses. Classification does not authorize sending or archiving messages.
6. For thread monitoring, compare supplied/authorized snapshots by comment identifier and time, identify new unanswered substantive replies and propose follow-ups. Do not invent urgency from a universal 72-hour cutoff. A request for a one-time report does not create recurring monitoring.
7. Run quality review and return target-labelled copy-ready drafts. Sending any draft follows the separate engagement workflow.

## Deliverable

Target-labelled drafts, batch counts and skip reasons, or a dated follow-up report with observed status.

## Detailed guidance

- [engagement and analysis](../../references/engagement-and-analysis.md)
