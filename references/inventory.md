# Reviewed LinkedIn skill inventory

Reviewed on 2026-09-29 from the five repositories listed below.
**35 entrypoints: 32 functional skills and three routers.** The 13 copies under
Sergey's `.codex-marketplace/linkedin-skills/` were byte-identical and excluded.
Only the LinkedIn action skill and umbrella router were selected from the multi-site
browsing registry; unrelated website skills are outside this LinkedIn collection.

The master skill and 12 focused modules consolidate the learning. Original instructions and supporting
documents are reference snapshots, not separately installed/runnable integrations.
All 35 entrypoints and six humanizer sub-workflows were read; supporting documentation
is retained for use as needed. No claim is made that every support file was fully reviewed.

## Repository snapshots

| Repository | Entrypoints | Pinned commit |
|---|---:|---|
| [quantumbyte31/linkedin-skills](https://github.com/quantumbyte31/linkedin-skills) | 7 | [e37c3d4749f7](https://github.com/quantumbyte31/linkedin-skills/tree/e37c3d4749f7c2981b06b51c690a181507f90c28) |
| [browsing-skills/browsing-skills](https://github.com/browsing-skills/browsing-skills) | 2 | [07855b500d21](https://github.com/browsing-skills/browsing-skills/tree/07855b500d210751fa4d5c54bc553bf30581d345) |
| [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills) | 13 | [14d332b9e91e](https://github.com/sergebulaev/linkedin-skills/tree/14d332b9e91e314f2e35b299246ced6df2594fab) |
| [Jakeschincariol/linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill) | 11 | [add2c23882fe](https://github.com/Jakeschincariol/linkedin-agent-skill/tree/add2c23882fe79180737d242ff80a5da205eda6a) |
| [Linked-API/linkedin-skills](https://github.com/Linked-API/linkedin-skills) | 2 | [e46beb9aea0a](https://github.com/Linked-API/linkedin-skills/tree/e46beb9aea0af3896fd49dd7b39cff1061bf8f6d) |

## Reading the archive

Every upstream `SKILL.md` is saved byte-for-byte as `SOURCE.md` so it does not become
a competing active skill. References to `SKILL.md` inside original documents mean the
corresponding `SOURCE.md` here. Other retained reference paths keep their original
layout. Scripts, runtime libraries, credentials, integration configuration and binaries
were not installed. Links to those absent runtime files should be resolved at the
pinned upstream commit, not treated as locally executable. Source documents can
contain promotional language, author-specific instructions or unsupported claims;
use the consolidated guidance to resolve them.

The [machine-readable manifest](source-manifest.json) records original paths, local
paths and SHA-256 hashes for every retained file. Each repository directory contains
its original MIT license.

## quantumbyte31/linkedin-skills

| Skill | Purpose | Source |
|---|---|---|
| [linkedin-skills](sources/quantumbyte31/SOURCE.md) | Route authentication, discovery, publishing, interaction, analysis and leads. | [GitHub](https://github.com/quantumbyte31/linkedin-skills/blob/e37c3d4749f7c2981b06b51c690a181507f90c28/SKILL.md) |
| [linkedin-auth](sources/quantumbyte31/skills/linkedin-auth/SOURCE.md) | Login-state checks and logout workflow. | [GitHub](https://github.com/quantumbyte31/linkedin-skills/blob/e37c3d4749f7c2981b06b51c690a181507f90c28/skills/linkedin-auth/SKILL.md) |
| [linkedin-content-ops](sources/quantumbyte31/skills/linkedin-content-ops/SOURCE.md) | Competitor, trend, campaign and profile-analysis workflows. | [GitHub](https://github.com/quantumbyte31/linkedin-skills/blob/e37c3d4749f7c2981b06b51c690a181507f90c28/skills/linkedin-content-ops/SKILL.md) |
| [linkedin-explore](sources/quantumbyte31/skills/linkedin-explore/SOURCE.md) | Feed, post, people, company and profile discovery. | [GitHub](https://github.com/quantumbyte31/linkedin-skills/blob/e37c3d4749f7c2981b06b51c690a181507f90c28/skills/linkedin-explore/SKILL.md) |
| [linkedin-interact](sources/quantumbyte31/skills/linkedin-interact/SOURCE.md) | Likes, comments, connections and messages. | [GitHub](https://github.com/quantumbyte31/linkedin-skills/blob/e37c3d4749f7c2981b06b51c690a181507f90c28/skills/linkedin-interact/SKILL.md) |
| [linkedin-lead-gen](sources/quantumbyte31/skills/linkedin-lead-gen/SOURCE.md) | Discover, qualify and enrich leads; prepare outreach. | [GitHub](https://github.com/quantumbyte31/linkedin-skills/blob/e37c3d4749f7c2981b06b51c690a181507f90c28/skills/linkedin-lead-gen/SKILL.md) |
| [linkedin-publish](sources/quantumbyte31/skills/linkedin-publish/SOURCE.md) | Text and image publishing workflow. | [GitHub](https://github.com/quantumbyte31/linkedin-skills/blob/e37c3d4749f7c2981b06b51c690a181507f90c28/skills/linkedin-publish/SKILL.md) |

## browsing-skills/browsing-skills

| Skill | Purpose | Source |
|---|---|---|
| [browsing-skills](sources/browsing-skills/SOURCE.md) | Route supported domains to site-specific action indexes. | [GitHub](https://github.com/browsing-skills/browsing-skills/blob/07855b500d210751fa4d5c54bc553bf30581d345/SKILL.md) |
| [browsing-linkedin](sources/browsing-skills/skills/linkedin.com/SOURCE.md) | Post, profile, job, company and saved-post data actions. | [GitHub](https://github.com/browsing-skills/browsing-skills/blob/07855b500d210751fa4d5c54bc553bf30581d345/skills/linkedin.com/SKILL.md) |

## sergebulaev/linkedin-skills

| Skill | Purpose | Source |
|---|---|---|
| [linkedin-marketing](sources/sergebulaev/SOURCE.md) | Route content work and distinguish manual/read/publish layers. | [GitHub](https://github.com/sergebulaev/linkedin-skills/blob/14d332b9e91e314f2e35b299246ced6df2594fab/SKILL.md) |
| [linkedin-comment-drafter](sources/sergebulaev/skills/linkedin-comment-drafter/SOURCE.md) | Draft top-level comments and reshare commentary. | [GitHub](https://github.com/sergebulaev/linkedin-skills/blob/14d332b9e91e314f2e35b299246ced6df2594fab/skills/linkedin-comment-drafter/SKILL.md) |
| [linkedin-content-planner](sources/sergebulaev/skills/linkedin-content-planner/SOURCE.md) | Plan content angles, formats, pillars and goals. | [GitHub](https://github.com/sergebulaev/linkedin-skills/blob/14d332b9e91e314f2e35b299246ced6df2594fab/skills/linkedin-content-planner/SKILL.md) |
| [linkedin-employee-advocacy](sources/sergebulaev/skills/linkedin-employee-advocacy/SOURCE.md) | Plan team participation, governance and measurement. | [GitHub](https://github.com/sergebulaev/linkedin-skills/blob/14d332b9e91e314f2e35b299246ced6df2594fab/skills/linkedin-employee-advocacy/SKILL.md) |
| [linkedin-engager-analytics](sources/sergebulaev/skills/linkedin-engager-analytics/SOURCE.md) | Deduplicate and segment supplied engager records. | [GitHub](https://github.com/sergebulaev/linkedin-skills/blob/14d332b9e91e314f2e35b299246ced6df2594fab/skills/linkedin-engager-analytics/SKILL.md) |
| [linkedin-hook-extractor](sources/sergebulaev/skills/linkedin-hook-extractor/SOURCE.md) | Classify source hooks and extract reusable structures. | [GitHub](https://github.com/sergebulaev/linkedin-skills/blob/14d332b9e91e314f2e35b299246ced6df2594fab/skills/linkedin-hook-extractor/SKILL.md) |
| [linkedin-humanizer](sources/sergebulaev/skills/linkedin-humanizer/SOURCE.md) | Edit/audit writing and calibrate voice; six nested workflows. | [GitHub](https://github.com/sergebulaev/linkedin-skills/blob/14d332b9e91e314f2e35b299246ced6df2594fab/skills/linkedin-humanizer/SKILL.md) |
| [linkedin-interviewer](sources/sergebulaev/skills/linkedin-interviewer/SOURCE.md) | Collect confirmed facts, stories and a post spine. | [GitHub](https://github.com/sergebulaev/linkedin-skills/blob/14d332b9e91e314f2e35b299246ced6df2594fab/skills/linkedin-interviewer/SKILL.md) |
| [linkedin-post-writer](sources/sergebulaev/skills/linkedin-post-writer/SOURCE.md) | Draft posts with 20 hook formulas and optional founder angles. | [GitHub](https://github.com/sergebulaev/linkedin-skills/blob/14d332b9e91e314f2e35b299246ced6df2594fab/skills/linkedin-post-writer/SKILL.md) |
| [linkedin-profile-optimizer](sources/sergebulaev/skills/linkedin-profile-optimizer/SOURCE.md) | Review nine profile areas and prepare rewrites. | [GitHub](https://github.com/sergebulaev/linkedin-skills/blob/14d332b9e91e314f2e35b299246ced6df2594fab/skills/linkedin-profile-optimizer/SKILL.md) |
| [linkedin-reply-handler](sources/sergebulaev/skills/linkedin-reply-handler/SOURCE.md) | Draft individual or batch replies with thread context. | [GitHub](https://github.com/sergebulaev/linkedin-skills/blob/14d332b9e91e314f2e35b299246ced6df2594fab/skills/linkedin-reply-handler/SKILL.md) |
| [linkedin-repurposer](sources/sergebulaev/skills/linkedin-repurposer/SOURCE.md) | Adapt a source asset into a native LinkedIn post. | [GitHub](https://github.com/sergebulaev/linkedin-skills/blob/14d332b9e91e314f2e35b299246ced6df2594fab/skills/linkedin-repurposer/SKILL.md) |
| [linkedin-thread-monitor](sources/sergebulaev/skills/linkedin-thread-monitor/SOURCE.md) | Analyze recent comment threads and follow-up status. | [GitHub](https://github.com/sergebulaev/linkedin-skills/blob/14d332b9e91e314f2e35b299246ced6df2594fab/skills/linkedin-thread-monitor/SKILL.md) |

## Jakeschincariol/linkedin-agent-skill

| Skill | Purpose | Source |
|---|---|---|
| [li-audit](sources/Jakeschincariol/skills/li-audit/SOURCE.md) | Analyze supplied post performance and content patterns. | [GitHub](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/add2c23882fe79180737d242ff80a5da205eda6a/skills/li-audit/SKILL.md) |
| [li-carousel](sources/Jakeschincariol/skills/li-carousel/SOURCE.md) | Develop slide copy, cover, recap and document-post structure. | [GitHub](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/add2c23882fe79180737d242ff80a5da205eda6a/skills/li-carousel/SKILL.md) |
| [li-comment](sources/Jakeschincariol/skills/li-comment/SOURCE.md) | Draft comments using nine contribution types. | [GitHub](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/add2c23882fe79180737d242ff80a5da205eda6a/skills/li-comment/SKILL.md) |
| [li-dm](sources/Jakeschincariol/skills/li-dm/SOURCE.md) | Draft specific connection notes and follow-ups. | [GitHub](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/add2c23882fe79180737d242ff80a5da205eda6a/skills/li-dm/SKILL.md) |
| [li-human](sources/Jakeschincariol/skills/li-human/SOURCE.md) | Review mechanical cleanup and five local style heuristics. | [GitHub](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/add2c23882fe79180737d242ff80a5da205eda6a/skills/li-human/SKILL.md) |
| [li-inbox](sources/Jakeschincariol/skills/li-inbox/SOURCE.md) | Triage supplied inbox items and draft worthwhile responses. | [GitHub](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/add2c23882fe79180737d242ff80a5da205eda6a/skills/li-inbox/SKILL.md) |
| [li-plan](sources/Jakeschincariol/skills/li-plan/SOURCE.md) | Build a weekly content and engagement plan. | [GitHub](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/add2c23882fe79180737d242ff80a5da205eda6a/skills/li-plan/SKILL.md) |
| [li-post](sources/Jakeschincariol/skills/li-post/SOURCE.md) | Draft posts using 21 hook formulas. | [GitHub](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/add2c23882fe79180737d242ff80a5da205eda6a/skills/li-post/SKILL.md) |
| [li-profile](sources/Jakeschincariol/skills/li-profile/SOURCE.md) | Review profiles with a 12-part, 100-point editorial rubric. | [GitHub](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/add2c23882fe79180737d242ff80a5da205eda6a/skills/li-profile/SKILL.md) |
| [li-reply](sources/Jakeschincariol/skills/li-reply/SOURCE.md) | Triage supplied comments and draft contextual replies. | [GitHub](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/add2c23882fe79180737d242ff80a5da205eda6a/skills/li-reply/SKILL.md) |
| [li-repurpose](sources/Jakeschincariol/skills/li-repurpose/SOURCE.md) | Extract standalone angles from a long source asset. | [GitHub](https://github.com/Jakeschincariol/linkedin-agent-skill/blob/add2c23882fe79180737d242ff80a5da205eda6a/skills/li-repurpose/SKILL.md) |

## Linked-API/linkedin-skills

| Skill | Purpose | Source |
|---|---|---|
| [linkedin](sources/Linked-API/linkedin/SOURCE.md) | Hosted browser CLI covering profiles, companies, posts, connections and messages. | [GitHub](https://github.com/Linked-API/linkedin-skills/blob/e46beb9aea0af3896fd49dd7b39cff1061bf8f6d/linkedin/SKILL.md) |
| [linkedin-growth](sources/Linked-API/linkedin-growth/SOURCE.md) | Import/qualify leads and explain database, lifecycle and scheduled maintenance. | [GitHub](https://github.com/Linked-API/linkedin-skills/blob/e46beb9aea0af3896fd49dd7b39cff1061bf8f6d/linkedin-growth/SKILL.md) |

## Additional nested workflows

These six documents are inside the humanizer skill and are not counted as separate
`SKILL.md` entrypoints.

- [voice-profile](sources/sergebulaev/skills/linkedin-humanizer/sub-skills/voice-profile.md)
- [post-audit](sources/sergebulaev/skills/linkedin-humanizer/sub-skills/post-audit.md)
- [emoji-detector](sources/sergebulaev/skills/linkedin-humanizer/sub-skills/emoji-detector.md)
- [rules-explainer](sources/sergebulaev/skills/linkedin-humanizer/sub-skills/rules-explainer.md)
- [detector-tester](sources/sergebulaev/skills/linkedin-humanizer/sub-skills/detector-tester.md)
- [illustration](sources/sergebulaev/skills/linkedin-humanizer/sub-skills/illustration.md)

## LinkedIn browser action references

These are five action specifications within `browsing-linkedin`, not five additional skills.

- [post-data](sources/browsing-skills/skills/linkedin.com/references/post-data.md)
- [profile-data](sources/browsing-skills/skills/linkedin.com/references/profile-data.md)
- [job-search](sources/browsing-skills/skills/linkedin.com/references/job-search.md)
- [company-data](sources/browsing-skills/skills/linkedin.com/references/company-data.md)
- [saved-posts](sources/browsing-skills/skills/linkedin.com/references/saved-posts.md)

## What was adopted

- Reusable writing, hook, interview, planning, profile, comment, reply, repurposing and analytical methods.
- Exact source provenance, supporting reference files and alternative approaches.
- Manual content mode, with current project instructions controlling work in existing applications.

## What remains reference knowledge

Authentication, scraping, live account analytics, automated publishing, messaging,
connection management, paid provider calls and recurring growth maintenance require
runtime setup and an independently authorized task. Studying them did not activate them.
