# User-first landing + Checkpoint UX acceptance — 2026-09-07

## Principal direction

The Principal approved restructuring the Agnir public website around the user's first questions rather than protocol exposition:

- keep the public surface concise, clear, direct, and user-first;
- put installation and ordinary use before concepts;
- remove adoption doubts early;
- move protocol explanation later;
- use the visible **without Agnir / with Agnir** fresh-session comparison in the hero instead of the abstract continuity-state card;
- make the normal use loop include an explicit Checkpoint trigger step.

The Principal also identified that the use flow must explicitly show how a user signals a Checkpoint boundary.

## Accepted public information order

The bilingual landing page now follows this sequence:

1. fresh-session pain + visible without/with Agnir outcome;
2. one-sentence installation;
3. ordinary use loop: Install → Work normally → Checkpoint → Continue in a fresh session;
4. direct reassurance about Agent lock-in, private-chat dependency, workflow takeover, and opaque-memory concerns;
5. Project Continuity concept, State / Next Actions / Decisions / Evidence, portability, and technical credibility.

This is a public/adoption presentation decision and does not redefine Core/profile semantics.

## Accepted Checkpoint UX

The website now explicitly tells users that at a meaningful save/finish boundary they can say `checkpoint`.

Natural-language examples may also communicate the same intent, including:

- `save progress`;
- `stop here`;
- `收尾`;
- `先到这里`;
- `保存进度`.

These are user-intent examples, not a normative fixed-string parser. The Agnir Agent/Skill procedure remains responsible for interpreting checkpoint/save/finish/commit boundaries and applying the actual checkpoint semantics.

## Receipts

- PR #41 head revision: `715e8dd89cafd241f40055c73e220b4cd6d6f469`;
- PR #41 synthetic-merge conformance: run `34096055249`, repository job `101659863443` — success;
- authoritative squash merge: `11b94443a276d8f7595056c0b8acf044cc9777d3`;
- authoritative post-merge conformance: run `34096205540`, repository job `101660318267` — success;
- automatic Pages run: `34096205574`;
- Pages build job `101660318417` — success;
- Pages deploy job `101660345565` — success.

## Result

The accepted website baseline is now explicitly user-first: value and contrast first, installation and use before concepts, Checkpoint visible in the ordinary user loop, doubts answered before technical depth, and protocol credibility later.
