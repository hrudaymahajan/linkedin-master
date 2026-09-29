# LinkedIn Master

One modular AI-agent skill for LinkedIn research, writing, editing, strategy,
comments, profiles, visual content and analytics.

Combines **32 functional skills and three routers from five MIT-licensed
repositories** into **12 focused workflow modules**. Includes six nested editing
and visual workflows, two hook libraries, profile rubrics and pinned source references.

## What it does

- Research a topic and produce a source-backed LinkedIn post.
- Develop hooks, repurpose articles and plan a content calendar.
- Learn voice from real samples, collect confirmed stories, edit and audit drafts.
- Draft comments, replies, connection notes and inbox responses.
- Review profiles and analyze supplied performance or audience data.
- Develop carousels, quote cards, illustrations and team advocacy plans.
- Prepare publication packages and describe or route authorized account operations
  when a compatible backend is already available.

**Manual content work is the default.** The repository does not contain a LinkedIn
connector, automated poster, browser extension, scheduler or paid API subscription.
Publication and other account actions require separate tooling, authorization and
compatible project scope. Creating a draft never implies publishing it.

## Install

### Codex

Clone the complete repository into the skills directory:

```bash
git clone https://github.com/hrudaymahajan/linkedin-master.git ~/.codex/skills/linkedin-master
```

If that destination already exists, inspect it before updating; do not overwrite a
customized installation. The master needs its `skills/` and `references/` folders.
Invoke it as `$linkedin-master` in a new turn/session once the host discovers it.

### Other SKILL.md-compatible agents

Place the complete repository in the host's skill directory and load the root
`SKILL.md`. Relative references are portable. Tool availability and skill discovery
vary by host; the optional `agents/openai.yaml` contains Codex display metadata.
The modules are bundled components, not independently installable packages.

## Usage

```text
Use $linkedin-master to turn this article into a source-backed post for students.
Use $linkedin-master to improve this draft without changing its technical meaning.
Use $linkedin-master to plan a week of practical Python and SQL content.
Use $linkedin-master to draft replies to these comments.
Use $linkedin-master to audit my profile using the sections below.
Use $linkedin-master to analyze this post-performance export.
Use $linkedin-master to create a carousel explaining this workflow.
```

The agent chooses the relevant module, reuses context, asks only for consequential
missing information and delivers the requested output. See [examples](examples/requests.md).

## Modules

| Module | Covers |
|---|---|
| [Authentication](skills/linkedin-auth/SKILL.md) | Backend readiness, status and account setup guidance |
| [Research](skills/linkedin-research/SKILL.md) | Sources, posts, people, companies, profiles, jobs and saved posts |
| [Strategy](skills/linkedin-strategy/SKILL.md) | Topics, competitor study, calendars and employee advocacy |
| [Writing](skills/linkedin-writing/SKILL.md) | Posts, hooks, extraction and repurposing |
| [Quality](skills/linkedin-quality/SKILL.md) | Voice, interviewing, editing, audits, emoji and detector interpretation |
| [Comments](skills/linkedin-comments/SKILL.md) | Comments, replies, inbox triage and thread follow-up |
| [Publishing](skills/linkedin-publishing/SKILL.md) | Manual packages and conditional live delivery |
| [Engagement](skills/linkedin-engagement/SKILL.md) | Outreach drafts and conditional account actions |
| [Profile](skills/linkedin-profile/SKILL.md) | Audit, scoring and section rewrites |
| [Leads](skills/linkedin-leads/SKILL.md) | Candidate research, qualification and pipeline design |
| [Analytics](skills/linkedin-analytics/SKILL.md) | Performance, audiences and next experiments |
| [Visuals](skills/linkedin-visuals/SKILL.md) | Carousels, illustrations, quote cards and document posts |

## Repository layout

```text
SKILL.md                  Master routing and shared rules
skills/                   12 focused SKILL.md workflow modules
references/               Combined guidance, inventory and source coverage
references/sources/       Original reference documents and upstream licenses
agents/openai.yaml        Codex display metadata
examples/requests.md      Example requests and expected workflow behavior
scripts/validate.py       Offline structural and source-integrity checks
```

## How the skills were combined

Overlapping methods are grouped by task, while every source entrypoint remains
traceable in the [coverage map](references/coverage.md). Archived `SKILL.md` files
are named `SOURCE.md` to distinguish source material from the combined procedures.
Their bytes and licenses are preserved; upstream runtime scripts are not included.

The two hook libraries contain 21 and 20 formulas with overlapping ideas. Their IDs
are separate namespaces. They are writing options, not 41 independently verified
performance guarantees. Author-specific preferences and unverified algorithm claims
are not adopted as universal rules. Source snapshots were reviewed on 2026-09-29;
current platform limits, integrations and pricing must be checked when relevant.

## Validation

No third-party Python packages are needed for the repository checks:

```bash
python3 scripts/validate.py
```

This checks the skill layout, internal links, complete source coverage, retained
source hashes and expected module count. It does not certify editorial quality or
verify a live LinkedIn integration. No external account is contacted.

## Attribution and license

This repository contains original integration guidance and MIT-licensed source
material from:

- [quantumbyte31/linkedin-skills](https://github.com/quantumbyte31/linkedin-skills)
- [browsing-skills/browsing-skills](https://github.com/browsing-skills/browsing-skills)
- [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills)
- [Jakeschincariol/linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill)
- [Linked-API/linkedin-skills](https://github.com/Linked-API/linkedin-skills)

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for pinned versions and copyright
notices. Original authors retain copyright in their respective material. No
endorsement by LinkedIn or the upstream authors is implied. MIT license: [LICENSE](LICENSE).
