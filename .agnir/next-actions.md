# Agnir Next Actions

Agnir `v1.0.0` remains latest published stable. Repository `1.0.1` activation/packaging hardening is implemented on PR #50 and the exact pre-checkpoint source candidate passed full conformance.

1. **Validate the checkpointed PR #50 head.** The continuity checkpoint itself changes repository source, so require one final PR synthetic-merge conformance run after this checkpoint commit. Do not treat the earlier successful run as verification of the later checkpoint revision.
2. **Reconcile PR #50 into authoritative `main` only after the final synthetic-merge gate is green.** Source/staging continuity is reconciliation input, not automatic target truth. Preserve authoritative Project identity/lineage and `refs/heads/main` binding.
3. **Keep stable publication separate.** Merging the implementation does not authorize `v1.0.1` publication. Publication requires a separate explicit Principal/policy authorization and exact authoritative-main arm; until then `v1.0.0` remains latest stable.
4. **After any authorized publication, verify actual host state.** Confirm immutable `v1.0.1` tag, non-draft/non-prerelease Release, `releases/latest == v1.0.1`, unchanged `v1.0.0` and `v1.0.0-rc.1` tags, then reconcile authoritative Agnir continuity and `agnir/operations` provenance.
5. **Operate the 1.0 line in stable-maintenance mode.** Preserve Core/profile 1.0 semantics and historical 0.1/0.2 compatibility/migration surfaces. Patch releases must not silently expand or redefine the stable contract.
6. **Produce the canonical 30-second fresh-session demo.** Demonstrate the visible contrast between an unassisted fresh session and a fresh Executor resuming Project-owned Agnir continuity. Lead with value, not protocol vocabulary.
7. **Recruit the first external design users and collect material adoption evidence.** Prioritize genuine external cold-start resumes, second-session value, cross-Executor cases, new execution surfaces, repeat use, and independently built integrations.
8. **Keep brand/public-surface truth locked.** README, website, adoption/demo and social materials may consume approved brand assets/deterministic derivatives but must not reinterpret approved identity or Core semantics.
9. **Keep merged-head cleanup enabled.** `main` remains the sole intended long-lived authoritative branch; retire completed staging branches after their material result and evidence are safely represented.
10. **Shift active product execution back to Svif where appropriate.** Svif owns its own canonical continuity and ChatGPT/Plugins publication path; do not smuggle Svif changes into Agnir maintenance.
11. **Keep FishUp production publication separate.** No FishUp main advancement without separate authorization.

## v1.0.1 acceptance receipts so far

- PR: `#50` — `Agnir v1.0.1: harden Project activation`;
- pre-checkpoint exact candidate: `ea254e09b999dde8024a76d32e55d5d5fe5868d6`;
- conformance run: `34254831971` — success;
- repository job: `102157842277` — success;
- stable publication job: skipped as intended;
- evidence: `.agnir/evidence/2026-09-09-v1.0.1-activation-hardening-candidate.md`.

## Adoption targets

These remain product-learning targets, not conformance requirements or release gates:

- 10 external Projects initialized;
- 5 users reach a second genuinely fresh session;
- 3 users continue using Agnir for more than 7 days;
- 3 distinct execution surfaces represented across adoption evidence;
- 2 cross-Executor continuation cases;
- 1 external integration or independent implementation beyond the v1 release gate.
