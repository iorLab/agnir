# Agnir Next Actions

Agnir `v1.0.0` remains latest published stable. Repository `1.0.1` activation/packaging hardening is implemented, merged into authoritative `main`, and post-merge conformance verified.

1. **Keep stable publication separate.** Do not infer `v1.0.1` publication from implementation, merge, or green CI. Publication requires separate explicit Principal/policy authorization and exact authoritative-main arm; until then `v1.0.0` remains latest stable.
2. **If publication is authorized, create the exact prepublication boundary on authoritative `main`.** Re-resolve current Project truth, verify no newer incompatible advancement, then use the dormant main-only publication gate with exact commit intent `release: publish v1.0.1 stable`.
3. **After any authorized publication, verify actual host state.** Confirm immutable `v1.0.1` tag, non-draft/non-prerelease Release, `releases/latest == v1.0.1`, unchanged `v1.0.0` and `v1.0.0-rc.1` tags, successful publication workflow, then reconcile authoritative Agnir continuity and `agnir/operations` provenance.
4. **Operate the 1.0 line in stable-maintenance mode.** Preserve Core/profile 1.0 semantics and historical 0.1/0.2 compatibility/migration surfaces. Patch releases must not silently expand or redefine the stable contract.
5. **Produce the canonical 30-second fresh-session demo.** Demonstrate the visible contrast between an unassisted fresh session and a fresh Executor resuming Project-owned Agnir continuity. Lead with value, not protocol vocabulary.
6. **Recruit the first external design users and collect material adoption evidence.** Prioritize genuine external cold-start resumes, second-session value, cross-Executor cases, new execution surfaces, repeat use, and independently built integrations.
7. **Keep brand/public-surface truth locked.** README, website, adoption/demo and social materials may consume approved brand assets/deterministic derivatives but must not reinterpret approved identity or Core semantics.
8. **Keep merged-head cleanup enabled.** `main` remains the sole intended long-lived authoritative branch; completed staging branches should remain retired after their material result and evidence are durably represented.
9. **Shift active product execution back to Svif where appropriate.** Svif owns its own canonical continuity and ChatGPT/Plugins publication path; do not smuggle Svif changes into Agnir maintenance.
10. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

## v1.0.1 implementation acceptance receipts

- PR: `#50` — merged;
- final staging checkpoint head: `162b9069ed485834f3f2c6f68ab49e41200cfd4d`;
- final synthetic-merge conformance run: `34255122900` — success;
- authoritative merge: `f07a792816956815876703472d55f711b5528387`;
- authoritative post-merge conformance run: `34255207555` — success;
- repository job: `102159143123` — success;
- `Publish v1.0.1 stable release`: skipped as intended;
- GitHub latest stable readback: `v1.0.0`;
- branch readback: only `main`;
- candidate evidence: `.agnir/evidence/2026-09-09-v1.0.1-activation-hardening-candidate.md`;
- authoritative acceptance evidence: `.agnir/evidence/2026-09-09-v1.0.1-activation-hardening-main-acceptance.md`.

## Adoption targets

These remain product-learning targets, not conformance requirements or release gates:

- 10 external Projects initialized;
- 5 users reach a second genuinely fresh session;
- 3 users continue using Agnir for more than 7 days;
- 3 distinct execution surfaces represented across adoption evidence;
- 2 cross-Executor continuation cases;
- 1 external integration or independent implementation beyond the v1 release gate.
