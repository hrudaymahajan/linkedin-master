---
name: linkedin-publishing
description: "Prepare LinkedIn text, image, document or reshare packages; execute publication only with authorization, supported tooling and compatible project scope."
---

# Publication preparation and delivery

Use the shared scope and factual rules in the [master skill](../../SKILL.md).
This module can be read directly but requires the repository references.

## Inputs

Final content, attachments, target account/page and requested delivery mode.

## Workflow

1. Distinguish preparing a post from publishing it. Default to a manual-copy package when the request is drafting or when the project is manual-only.
2. Assemble the exact copy, attachment order, alt text where appropriate, attribution and target. Validate current provider limits only when needed; upstream media counts conflict and are not interchangeable.
3. For manual delivery, provide the copy and actual local/downloadable files. Mark it prepared, not posted. Do not require approval merely to finish reversible artifact work already requested.
4. For an authorized live action in a compatible project, verify the configured provider, target account/page and final content. Resolve any missing essential details and meet any genuinely applicable approval requirement after the concrete package is ready; reuse existing explicit authorization.
5. Use one supported provider call with a stable operation identifier if available. Verify returned success and a published URL or scheduled state. A scheduler receipt is not proof that a post is live.
6. On ambiguous timeout, inspect status before retrying. Stop on account restrictions or rate limits; report partial results. Cancellation, deletion and target changes are distinct actions and need their own user intent.

## Deliverable

Manual publication package or a verified provider receipt with precise state, target and URL; report failures without claiming success.

## Detailed guidance

- [integration knowledge](../../references/integration-knowledge.md)
