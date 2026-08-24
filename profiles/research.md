# Research Profile

Version: 1.0.0

Use this profile when durable work centers on questions, evidence, sources, hypotheses, experiments, or synthesized findings.

## Optional artifacts

Create lazily when justified:

```text
docs/research/RESEARCH_QUESTIONS.md
docs/research/FINDINGS.md
docs/research/SOURCES.md
docs/research/hypotheses/
```

### RESEARCH_QUESTIONS

Maintain important open and answered questions that organize the investigation. Remove or mark resolved questions when appropriate.

### FINDINGS

Record synthesized findings that are supported by evidence. Findings SHOULD distinguish established evidence, interpretation, uncertainty, and unresolved contradictions.

### SOURCES

Track key sources, what each supports, and any material reliability or freshness limitations. A source list is not a substitute for findings.

### hypotheses/

Use for significant testable hypotheses that need independent lifecycle tracking. Trivial guesses SHOULD remain in working discussion rather than becoming files.

## Persistence triggers specific to research

Persist when:

- a research question becomes central or is resolved;
- evidence materially changes a conclusion;
- a finding becomes sufficiently supported to reuse later;
- a source is uniquely important to future reasoning;
- a hypothesis is accepted for testing, rejected, or supported;
- uncertainty or contradiction is important enough to affect future work.

## Evidence discipline

Do not convert tentative evidence into a settled finding. Where useful, findings SHOULD include confidence, scope, date/freshness, and source references.

Historical or time-sensitive findings SHOULD carry enough date context to prevent stale reuse.

## Recommended manifest extension

```yaml
extensions:
  research:
    questions: docs/research/RESEARCH_QUESTIONS.md
    findings: docs/research/FINDINGS.md
    sources: docs/research/SOURCES.md
    hypotheses: docs/research/hypotheses
```
