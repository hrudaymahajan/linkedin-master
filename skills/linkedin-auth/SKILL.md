---
name: linkedin-auth
description: "Check or explain LinkedIn authentication and account readiness when requested; identify the selected backend and its requirements."
---

# Authentication and account readiness

Use the shared scope and factual rules in the [master skill](../../SKILL.md).
This module can be read directly but requires the repository references.

## Inputs

Account or backend requested by the user, and whether they want explanation, setup, status or logout.

## Workflow

1. Determine whether this is a question or an account operation. Read the applicable project instructions and existing authorization first.
2. Identify a configured, callable backend. The source choices are Quantumbyte browser bridge, a publishing provider, and Linked API cloud browser; their credentials are not interchangeable.
3. For explanation, report requirements without accessing a session. For authorized setup, use the provider's supported login flow and keep credentials out of chat, source control and command output.
4. For status, perform one supported read-only check. If the provider is absent, explain that precise dependency; do not repeatedly probe browser sessions.
5. Execute logout only when requested. Distinguish account disconnection from revoking a provider token, clearing browser data or removing local configuration.

## Deliverable

Backend, observed connection state, capability availability and any exact missing setup. Never label an untested account connected.

## Detailed guidance

- [integration knowledge](../../references/integration-knowledge.md)
