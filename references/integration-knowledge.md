# Integration knowledge: retained for explanation

These are descriptions of the pinned upstream designs, not configured capabilities.
No LinkedIn login, browser session access, API account, scheduler, paid provider,
message sender or publisher was installed or run during this learning task.

| Repository | Upstream design | What can be reused locally |
|---|---|---|
| quantumbyte31/linkedin-skills | Python CLI, Chrome extension and local WebSocket bridge; auth, discovery, publishing, interactions, compound analysis and leads | Workflow decomposition and input/output contracts |
| browsing-skills/browsing-skills | Site action index plus JavaScript action references, real browser/optional Chrome bridge | Five LinkedIn data shapes and focused action routing |
| sergebulaev/linkedin-skills | Writing/planning/editing library; manual mode with optional Publora, Apify and Pixfaro layers | Drafting, interviews, hooks, profiles, analysis and manual-review methods |
| Jakeschincariol/linkedin-agent-skill | Eleven mostly manual-use skills, hook/rubric JSON, optional local humanizer scripts and Claude-specific file locations | Copy preparation, voice, planning, profile and analytical methods |
| Linked-API/linkedin-skills | Hosted browser CLI plus SQLite/Node growth pipeline and OS scheduler | Data models, qualification reasoning and lifecycle explanations |

## Authentication and reading

Quantumbyte separates login-state checks from a person's manual login and routes
operations through a single CLI. Its extension and bridge are required runtime
components, not capabilities provided by reading `SOURCE.md`.

Browsing-skills has five LinkedIn actions: post-data, profile-data, job-search,
company-data and saved-posts. The archived references describe navigation,
parameters, JavaScript and return shapes. Session-dependent actions require a real
account context. These have been retained for reference, not executed against a
session. They do not imply permission to read cookies or launch a bridge.

Sergey's manual mode can use pasted posts and comment threads; its optional read
layer and publish layer are separate dependencies. Jake's collection mainly uses
pasted text, screenshots and exports. Prefer the input the user already supplied.

## Publishing and interaction architecture

Quantumbyte offers text/image submission and likes/comments/connections/messages.
Sergey's wrapper routes manual/Publora/custom backends and distinguishes post,
comment, reply and reshare. Linked API supplies broader account, company-page,
connection, message, post and Sales Navigator operations through a cloud browser.

Upstream post identifiers differ: activity, share and ugcPost identifiers cannot
safely be interchanged by replacing their prefixes. Sergey's reply workflow carries
the top-level comment identifier through nested reply queues. These are useful
architecture notes; re-check the actual provider contract before any future
implementation. Reaction names, media limits, prices and scheduling behavior vary
by provider and version.

Permission to learn, draft, plan, classify, or review does not authorize executing
those external operations. Follow the user's actual request and the applicable
project scope. Do not silently select a backend, install global CLIs, introduce a
paid dependency, upload drafts to detectors or create a background process.

## Lead pipeline architecture

Quantumbyte's simple progression is discovery, qualification, enrichment and outreach.
Linked API's growth skill separates interactive import from recurring maintenance:

1. Prepare an import batch with an explicit source and size.
2. Assess each candidate against the user's criteria and retain the reason.
3. Deduplicate and commit qualified records with ownership.
4. Track invite and response state separately from technical failures.

Its database separates accounts, leads, operation runs, import batches and settings.
Prepare is not idempotent, while a batch cannot be committed twice. Hashed Sales
Navigator URLs and public URLs can duplicate one person across search types; identity
resolution must not assume string equality. A timed-out external operation may have
succeeded, so checking status precedes retrying a mutation.

The source also describes automated invites, withdrawals, cross-account retries
and an OS scheduler. These are archived descriptions, not adopted workflows or
permission to contact people. No database or scheduler was created here.

## Evidence and conflicting claims

The repositories differ on note lengths, post cutoffs, hooks, emoji, punctuation,
cadence, link placement, timing and media counts. Some values are provider limits,
some are author's preferences and some are unverified marketing claims. Keep those
categories separate. Do not use the most restrictive number as a universal rule.

Humanizer scores and detector demonstration output do not establish authorship.
In particular, Sergey's detector demo uses canned values, not real detections.
No upstream code was run to produce a quality or performance score during review.
