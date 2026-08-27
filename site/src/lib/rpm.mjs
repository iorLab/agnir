import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { marked } from 'marked';
import sanitizeHtml from 'sanitize-html';

const repoRoot = resolve(process.cwd(), '..');

const groups = [
  { kind: 'spec', label: 'Protocol', description: 'Normative PPMP protocol semantics and migration rules.', files: ['CORE.md','MANIFEST.md','CLASSIFICATION.md','PERSISTENCE.md','BOOTSTRAP.md','VERSIONING.md','MIGRATION.md'] },
  { kind: 'profiles', label: 'Profiles', description: 'Composable domain extensions layered on PPMP Core.', files: ['software.md','product.md','content.md','research.md','planning.md','generic.md'] },
  { kind: 'implementations', label: 'Implementation', description: 'iorMemory reference Skill behavior kept distinct from PPMP protocol requirements.', files: ['IORMEMORY.md'] },
  { kind: 'backends', label: 'Backends', description: 'Concrete durable-storage strategies.', files: ['REPOSITORY.md'] },
  { kind: 'adapters', label: 'Adapters', description: 'Platform-specific discovery and lifecycle integration.', files: ['CHATGPT.md'] },
  { kind: 'templates', label: 'Templates', description: 'Copy-ready reference serialization and ChatGPT setup for iorMemory.', files: ['PROJECT_INSTRUCTIONS.md','project-memory.yaml','PROJECT_STATE.md','NEXT_STEPS.md','DECISIONS.md','SESSION.md'] }
];

function readRepoFile(relativePath) { return readFileSync(resolve(repoRoot, relativePath), 'utf8').trimEnd(); }
function slugFor(filename) { return filename.replace(/\.[^.]+$/, '').replaceAll('_', '-').toLowerCase(); }
function titleFromSource(filename, source) { return source.match(/^#\s+(.+)$/m)?.[1]?.trim() || filename.replace(/\.[^.]+$/, '').replaceAll('_', ' '); }
function stripLeadingTitle(source) { return source.replace(/^#\s+.+\n+/, ''); }

export const version = readRepoFile('VERSION');
export const projectInstructions = readRepoFile('templates/PROJECT_INSTRUCTIONS.md');
export const manifestTemplate = readRepoFile('templates/project-memory.yaml');
export function getGroups() { return groups.map((group) => ({ ...group, documents: group.files.map((filename) => { const path = `${group.kind}/${filename}`; const source = readRepoFile(path); return { kind: group.kind, groupLabel: group.label, filename, path, slug: slugFor(filename), title: titleFromSource(filename, source), source }; }) })); }
export function getAllDocuments() { return getGroups().flatMap((group) => group.documents); }
export function renderMarkdown(source) { return sanitizeHtml(marked.parse(stripLeadingTitle(source), { gfm: true }), { allowedTags: sanitizeHtml.defaults.allowedTags.concat(['img']), allowedAttributes: { ...sanitizeHtml.defaults.allowedAttributes, a: ['href','title'], code: ['class'], img: ['src','alt','title'] }, allowedSchemes: ['http','https','mailto'] }); }
