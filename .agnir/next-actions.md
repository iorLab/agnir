# Agnir Next Actions

Agnir `v1.0.1` is published and verified as the latest stable repository/distribution release. Core/profile remain `1.0` / `repository-filesystem/1.0`.

1. **Operate the 1.0 line in stable-maintenance mode.** Preserve Core/profile 1.0 semantics and historical 0.1/0.2 compatibility/migration surfaces. Future patch releases must not silently expand or redefine the stable contract.
2. **Optionally repair the v1.0.1 GitHub Release-body wording.** One cosmetic sentence omitted the literal `AGNIR.md` because of shell command substitution in an unquoted heredoc. Any repair must update host metadata only; do not move/recreate `v1.0.1` or change release identity.
3. **Complete human visual review of the conversational fresh-session demo v2.** The first live review rejected the slide/card presentation model, and PR `#52` replaced it with a persistent Agent-chat playback. Review the live English and Simplified Chinese versions on desktop/mobile and confirm that the experience now reads as one continuous Agent workflow: streamed messages, inline tool activity, explicit Session A closure, fresh private-transcript reset, `Continue.`-only recovery, Agnir discovery/load, and resumed test work. If accepted, close the visual-review item; if not, fix only observed presentation defects without changing Core semantics or returning to scene-card slides.
4. **Recruit the first external design users and collect material adoption evidence.** After the conversational demo passes human visual review, use it as the primary first-contact proof surface. Prioritize genuine external cold-start resumes, second-session value, cross-Executor cases, new execution surfaces, repeat use, and independently built integrations.
5. **Keep brand/public-surface truth locked.** README, website, adoption/demo and social materials may consume approved brand assets/deterministic derivatives but must not reinterpret approved identity or Core semantics.
6. **Keep merged-head cleanup enabled.** `main` remains the sole intended long-lived authoritative branch; completed staging branches should remain retired after their material result and evidence are durably represented.
7. **Shift active product execution back to Svif where appropriate.** Svif owns its own canonical continuity and ChatGPT/Plugins publication path; do not smuggle Svif changes into Agnir maintenance.
8. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

## Conversational demo v2 correction receipts

- Principal visual review of v1: **rejected** — presentation looked like slide/card replacement instead of a live Agent conversation;
- correction PR: `#52` — merged;
- correction source head: `423bc22410d0a225f185d9cc2eabe20c644bd361`;
- authoritative merge: `e87e3a3eaf24d25ae209659f8764c59041b45f7e`;
- PR conformance: run `34810732745` — success;
- post-merge conformance: run `34810775853` — success;
- Pages publication: run `34810776075` — build and deploy success;
- Pages build job: `103871507283` — success;
- Pages deploy job: `103871540152` — success;
- Pages artifact: `10335125320`;
- artifact digest: `sha256:1d5c069f64bbbadddc18966b4e477b2e90b2ebb33ca8a94593aa96bcccc24e9f`;
- canonical presentation contract: `adoption/demos/fresh-session/README.md`;
- deterministic conversation trace: `adoption/demos/fresh-session/trace.json`;
- correction evidence: `.agnir/evidence/2026-09-14-conversational-demo-correction.md`.

## Canonical demo v1 receipts

- implementation PR: `#51` — merged;
- authoritative merge: `226ac6f502e4fefc1a3bbb10472802d83ef51c03`;
- PR conformance: run `34808633866` — success;
- post-merge conformance: run `34808679959` — success;
- Pages publication: run `34808679937` — build and deploy success;
- Pages build job: `103865504185` — success;
- Pages deploy job: `103865531573` — success;
- Pages artifact: `10333823384`;
- artifact digest: `sha256:15bd2907feec1ab772f7484fe040f42fb0b717db0e6c91c45240f013050b1fab`;
- initial publication evidence: `.agnir/evidence/2026-09-14-canonical-fresh-session-demo.md`.

## v1.0.1 stable publication receipts

- implementation PR: `#50` — merged;
- authoritative implementation merge: `f07a792816956815876703472d55f711b5528387`;
- implementation post-merge conformance: run `34255207555`, job `102159143123` — success;
- authoritative implementation checkpoint: `7613638b1d116a84481ee25ab0ae4de54f663f64`;
- publication arm / stable source: `f56d25b22997c259c660651e7357334b063093e1`;
- publication workflow: `34301559338` — success;
- repository/conformance job: `102309347343` — success;
- stable publication job: `102309386242` — success;
- stable tag: `v1.0.1` -> `f56d25b22997c259c660651e7357334b063093e1`;
- GitHub Release id: `385176185`;
- latest stable readback: `v1.0.1`;
- previous `v1.0.0`: unchanged at `6d16dcfd17b8e9f22fd25804e22b9f8a516d06c3`;
- accepted RC `v1.0.0-rc.1`: unchanged at `092945289f1a0a9803e4fe0583104aa380ceaadc`;
- publication evidence: `.agnir/evidence/2026-09-09-v1.0.1-stable-publication.md`.

## Adoption targets

These remain product-learning targets, not conformance requirements or release gates:

- 10 external Projects initialized;
- 5 users reach a second genuinely fresh session;
- 3 users continue using Agnir for more than 7 days;
- 3 distinct execution surfaces represented across adoption evidence;
- 2 cross-Executor continuation cases;
- 1 external integration or independent implementation beyond the v1 release gate.
