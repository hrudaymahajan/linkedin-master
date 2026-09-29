---
name: linkedin-engagement
description: "Prepare connection notes and follow-ups, or handle explicitly requested LinkedIn reactions, messages and connection actions through an available backend."
---

# Account interactions and outreach drafts

Use the shared scope and factual rules in the [master skill](../../SKILL.md).
This module can be read directly but requires the repository references.

## Inputs

Target, exact action, content when applicable and a genuine reason for outreach.

## Workflow

1. Separate message drafting from sending, reacting and connection management. Use visible context and user-confirmed facts for personalization.
2. Draft concise connection notes or follow-ups that state a genuine reason and add value; do not fabricate shared history. Stop when the recipient has declined or the user does not want further follow-up.
3. For a live request, apply the same readiness and authorization checks as linkedin-publishing. Do not operate a live account in a manual-only project. Verify the exact recipient or post, account and action rather than relying on a name match.
4. Check current backend requirements and note limits when relevant. For comments/replies carry the intended target and supported parent identifier; verify the backend's actual threading contract.
5. Execute only authorized actions, record per-item results and avoid duplicate sends after uncertainty. Stop on limits or restrictions. A batch request does not create a recurring campaign or imply permission to message additional people.
6. Treat accept, ignore, withdraw, remove and logout as different actions. Preserve state and explain partial completion if a batch stops.

## Deliverable

Copy-ready outreach drafts or verified per-target action results. Never imply that a draft was sent.

## Detailed guidance

- [engagement and analysis](../../references/engagement-and-analysis.md)
- [integration knowledge](../../references/integration-knowledge.md)
