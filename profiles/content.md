# Content Profile

Version: 1.0.0

Use this profile for durable editorial, publishing, brand, campaign, or reusable content-production work.

## Optional artifacts

Create lazily when justified:

```text
docs/content/STYLE_GUIDE.md
docs/content/CONTENT_STRATEGY.md
docs/content/TOPIC_BACKLOG.md
docs/content/PUBLISHING_LOG.md
```

### STYLE_GUIDE

Create or update when reusable visual, tonal, editorial, formatting, brand, naming, or platform conventions become stable enough to apply across future outputs.

Examples include aspect ratios, watermark rules, typography conventions, voice, forbidden patterns, logo usage, or platform-specific formatting.

### CONTENT_STRATEGY

Use for durable audience definition, platform goals, content pillars, positioning, cadence, distribution strategy, or success criteria.

### TOPIC_BACKLOG

Use for accepted or promising future topics that have not yet been produced. Keep speculative throwaway brainstorming out unless the backlog is explicitly intended to capture it.

### PUBLISHING_LOG

Use only when tracking published outputs, destinations, dates, versions, or performance references has durable project value.

## Persistence triggers specific to content work

Persist when:

- a reusable style or brand rule is confirmed;
- a recurring editorial structure is adopted;
- target audience or platform strategy changes;
- a topic is accepted into the durable backlog;
- a production workflow is standardized;
- a significant piece is published and publication tracking is part of the project;
- feedback establishes a reusable do/don't rule.

## Decision discipline

A one-off aesthetic preference SHOULD NOT automatically become a project-wide style rule. Promote it to durable guidance only when it is explicitly intended to recur or has become a stable pattern.

## Recommended manifest extension

```yaml
extensions:
  content:
    style_guide: docs/content/STYLE_GUIDE.md
    strategy: docs/content/CONTENT_STRATEGY.md
    topic_backlog: docs/content/TOPIC_BACKLOG.md
    publishing_log: docs/content/PUBLISHING_LOG.md
```
