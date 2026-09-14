# Split-screen demo v3 — human visual acceptance

Date: 2026-09-14

## Observation

The Principal reviewed the live synchronized split-screen fresh-session demo v3 after publication and stated:

> 看过了，这个版本我觉得可以。

This is accepted human visual-review evidence for the current primary demo surface.

## Accepted presentation

The accepted demo presentation is the synchronized split-screen model introduced by PR `#53`:

- left window: **Without Agnir**;
- right window: **With Agnir**;
- both windows remain visible simultaneously on desktop;
- both run dynamic Agent-workspace transcripts on one shared timeline;
- both begin with the same Project task and reach the same stopping point;
- both start genuinely fresh Session B instances and receive only `Continue.` / `继续。`;
- Without Agnir stalls because durable Project context is unavailable;
- With Agnir discovers and loads Project-owned continuity, resumes the pending tests, and verifies the work successfully;
- narrow/mobile layouts stack Without first and With second.

## Receipts

- implementation PR: `#53`;
- source head: `a74371b37f044af2837c7de3d4178f26cf299d8d`;
- authoritative merge: `64e61ad1f21d15362cedbfb8376ab1d0adb6343d`;
- PR conformance: run `34819370697` — success;
- post-merge conformance: run `34819425531` — success;
- Pages publication: run `34819425549` — build and deploy success;
- Pages artifact: `10338020626`;
- artifact digest: `sha256:50ae43bdc8d18e5ab05057fee5406fbb6c7f9282eb585109de34a5dbb94501de`;
- trace schema: `agnir.demo.split-screen/3`.

## Result

The canonical fresh-session demo human visual-review gate is **closed / accepted**.

This acceptance does not change Agnir Core, repository/filesystem profile semantics, checkpoint semantics, Project identity, or Continuity Lineage behavior. It closes a public/adoption presentation gate only.

The next product-learning priority is external design-user adoption evidence: genuine cold-start resumes, second-session value, cross-Executor continuation, new execution surfaces, repeat usage, and independently built integrations.
