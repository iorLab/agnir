import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { marked } from 'marked';
import sanitizeHtml from 'sanitize-html';

const repoRoot = resolve(process.cwd(), '..');

const groups = [
  {
    kind: 'spec',
    label: 'Specification',
    description: 'Normative RPM behavior. These files define the standard.',
    files: ['CORE.md', 'MANIFEST.md', 'CLASSIFICATION.md', 'PERSISTENCE.md', 'BOOTSTRAP.md', 'VERSIONING.md']
  },
  {
    kind: 'profiles',
    label: 'Profiles',
    description: 'Composable domain extensions layered on top of the RPM Core.',
    files: ['software.md', 'product.md', 'content.md', 'research.md', 'planning.md', 'generic.md']
  },
  {
    kind: 'templates',
    label: 'Templates',
    description: 'Copy-ready starting points for manifests, memory files, and Project Instructions.',
    files: ['PROJECT_INSTRUCTIONS.md', 'project-memory.yaml', 'PROJECT_STATE.md', 'NEXT_STEPS.md', 'DECISIONS.md', 'SESSION.md']
  }
];

function readRepoFile(relativePath) {
  return readFileSync(resolve(repoRoot, relativePath), 'utf8').trimEnd();
}

function slugFor(filename) {
  return filename.replace(/\.[^.]+$/, '').replaceAll('_', '-').toLowerCase();
}

function titleFromSource(filename, source) {
  const heading = source.match(/^#\s+(.+)$/m)?.[1]?.trim();
  if (heading) return heading;
  return filename.replace(/\.[^.]+$/, '').replaceAll('_', ' ');
}

function stripLeadingTitle(source) {
  return source.replace(/^#\s+.+\n+/, '');
}

export const version = readRepoFile('VERSION');
export const projectInstructions = readRepoFile('templates/PROJECT_INSTRUCTIONS.md');
export const manifestTemplate = readRepoFile('templates/project-memory.yaml');

export function getGroups() {
  return groups.map((group) => ({
    ...group,
    documents: group.files.map((filename) => {
      const path = `${group.kind}/${filename}`;
      const source = readRepoFile(path);
      return {
        kind: group.kind,
        groupLabel: group.label,
        filename,
        path,
        slug: slugFor(filename),
        title: titleFromSource(filename, source),
        source
      };
    })
  }));
}

export function getAllDocuments() {
  return getGroups().flatMap((group) => group.documents);
}

export function renderMarkdown(source) {
  const rendered = marked.parse(stripLeadingTitle(source), {
    gfm: true
  });

  return sanitizeHtml(rendered, {
    allowedTags: sanitizeHtml.defaults.allowedTags.concat(['img']),
    allowedAttributes: {
      ...sanitizeHtml.defaults.allowedAttributes,
      a: ['href', 'title'],
      code: ['class'],
      img: ['src', 'alt', 'title']
    },
    allowedSchemes: ['http', 'https', 'mailto']
  });
}
