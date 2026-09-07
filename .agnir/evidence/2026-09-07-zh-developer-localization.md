# Simplified Chinese developer-localization acceptance — 2026-09-07

## Principal direction

The Principal requested that the public Simplified Chinese website stop using uncommon literal AI terminology such as `智能体` and instead follow terminology Chinese developers actually use, especially **Agent**.

This is a public localization decision, not a Core/profile semantic change.

## Accepted localization policy

For Simplified Chinese developer-facing Agnir copy:

- prefer **Agent** over `智能体`;
- keep familiar developer terms such as `API`, `IDE`, `Core`, `profile`, `Skill`, `Checkpoint`, and `prompt` in English when that is more idiomatic;
- translate explanatory prose into natural Simplified Chinese rather than mechanically mirroring English sentence structure;
- preserve the approved Project Continuity positioning and do not redefine Core/profile semantics through localization.

The policy is documented in `website/README.md`.

## Public-surface change

PR #39 rewrote the Simplified Chinese landing page around the same approved product story with more natural developer-facing language, including:

- `Agent 会忘。项目不该忘。` as the Chinese hero line;
- `新会话，继续同一个项目。` for the fresh-session value story;
- `换 Agent，不换项目。` for portability;
- `给 Agent 一句话就够了。` for the install handoff;
- `Checkpoint` and other familiar developer terms retained where natural.

The English website, Core/profile contracts, brand geometry, release tags, and release identity were unchanged.

## Receipts

- PR #39 head revision: `2fa610fa7620a64a0d70660a908c7d00f541de29`;
- PR #39 synthetic-merge conformance: run `34094408280`, repository job `101654655516` — success;
- authoritative squash merge: `4e49092a5bc87168f2aa290460d381d39eaa8a02`;
- authoritative post-merge conformance: run `34094559213`, repository job `101655124756` — success;
- automatic Pages run: `34094559226`;
- Pages build job `101655124864` — success;
- Pages deploy job `101655171121` — success.

## Result

The Simplified Chinese public site now treats localization as developer-native product copy rather than literal translation. This is the accepted baseline for future Chinese public-site edits.
