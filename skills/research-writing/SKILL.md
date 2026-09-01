---
name: research-writing
description: Create and revise academic outlines, section architectures, optional paragraph plans, drafts, manuscripts, and argument-led prose; audit arguments and citations, compress text, convert stable content to LaTeX, and improve rhetoric while preserving the researcher's claims, voice, citations, and uncertainty. Use when Codex needs to turn researcher-supplied materials into a writing artifact or directly continue editing a designated artifact, introducing structural planning only when requested or materially necessary. Do not use to invent evidence, decide the research question, analyze raw research objects, or manage project progress.
---

# Research Writing

Use only materials supplied or designated for the task. Do not require a fixed project-file schema.

## Authority and Objects

Prioritize: current instruction; researcher-confirmed decisions and outlines; designated source or seed outline; active working artifact; supplementary context. Do not infer confirmation from recency, filenames, or file existence.

Keep source inputs read-only and distinguish:

- **architecture / outline**: structural responsibilities and principal argumentative movement;
- **paragraph plan**: optional, provisional implementation aid;
- **draft**: prose whose paragraph boundaries and local sequence may change.

Architecture governs structure; a paragraph plan does not. Return to architecture only when drafting reveals a structural problem. Keep separate artifacts when more than one object is requested.

## Modes

- `outline`: create or revise a manuscript structure with distinct section tasks and dependencies.
- `section-architecture`: define or revise a concise hierarchy of section responsibilities and claims.
- `paragraph-plan`: create or revise a separate provisional map from a confirmed section architecture to possible paragraph functions, evidence use, and local sequence.
- `section-draft`: draft the requested section from relevant claims, notes, and evidence.
- `rewrite`: revise a designated text with the smallest change that satisfies the request.
- `argument-audit`: inspect claims, evidence, inference, counterarguments, and paragraph functions.
- `citation-audit`: check whether citations exist and support nearby claims; distinguish internal consistency from external verification.
- `compression`: preserve indispensable claims and evidence while removing repetition or excess background.
- `polish`: improve clarity, rhythm, transitions, diction, and academic register without redesigning the argument.
- `latex-output`: convert stable content and verified citation keys without inventing BibTeX entries.

## Workflow

1. Identify the mode, current object, objective, audience, length, format, and destination. Ask only when an unresolved choice would materially change the result.
2. Read only directly relevant inputs. Extract claims, evidence, inference, terminology, constraints, and gaps.
3. Work at the requested level:
   - For `rewrite`, `compression`, `polish`, audits, and `latex-output`, work directly on the designated text.
   - For a section draft with sufficiently clear and confirmed responsibilities, draft directly; do not recreate architecture or a paragraph plan.
   - Create or revise architecture only when requested or when section ownership, hierarchy, principal claim sequence, or inference boundaries are materially unresolved.
   - Create a paragraph plan only when requested or genuinely useful. Never make it a prerequisite by default.
4. Keep architecture compressed: state each unit's task, claim or output, relation to adjacent units, evidence families, and inference boundary. Avoid proto-prose, fixed paragraph counts, and sentence scripts. If boundaries are difficult, add a concise optional **Section Contract**: Owns, Inputs, Produces, Reserves, Must not claim. Ask for confirmation only of choices that block writing.
5. Draft for argumentative movement rather than mechanically filling a plan. Merge, split, add, remove, or reorder paragraphs when structure remains intact. If drafting exposes a local problem, revise the prose; return to architecture only for a structural problem.
6. Mark genuine gaps specifically with `[需证据]`, `[需引用]`, `[待核页码]`, or `[待确认]`; never fill them by invention.
7. Revise in place by default. Preserve numbered versions when the user requests versioning, an existing `vN` sequence establishes it, or a substantive revision should remain recoverable. Record lineage only when it helps distinguish governing sources.
8. Deliver the requested artifact first, then briefly report substantive changes, unresolved gaps, and any decision that truly requires confirmation. Identify project-level conflicts as unresolved rather than silently changing the global argument.

Templates in `templates/` are optional.

## Authorship and Evidence

- Preserve strong researcher judgments unless asked to challenge them.
- Preserve citations, quotations, uncertainty, and deliberate terminology.
- Do not turn a provisional thought into false certainty.
- Do not let rhetorical fluency conceal a conceptual or evidentiary gap.
- Do not update research questions, other outlines, or project status unless explicitly requested.

## Optional External Models

Use `scripts/call_model.py` only when the user explicitly requests a named external provider or cross-model comparison. Read `references/providers.md` first, protect unpublished or sensitive text, use configured credentials, and never overwrite the source.

## Researcher Review

Treat any model-created or substantially expanded outline, paragraph plan, claim, interpretation, section, or manuscript prose as researcher-reviewable. Preserve the researcher's authorship, citations, uncertainty, and ability to reject structural as well as local changes. Fluent prose is not researcher confirmation.

## Independent Scope and Later Reuse

- This Skill independently owns the requested writing artifact and the structural or rhetorical work required to produce it.
- It may start directly from researcher-designated literature notes, thought records, analysis results, programme maps, reviews, outlines, drafts, or other supplied materials; those inputs do not need to have been produced by another Research Skill.
- It does not invent evidence, verify new scholarship, decide the research question, newly analyze raw research objects, design a paper portfolio, adapt a stable paper to another medium, or manage project state.
- If evidence, a core intellectual decision, source verification, or new analysis is missing, complete the stable writing that the present materials support, mark the exact gap, and stop at the boundary. Do not automatically invoke, schedule, or assign another Skill.
- A researcher-reviewed outline, section, or manuscript may later be designated as input to manuscript development, publishing, programme design, or meta-reflection. Preserve citations, uncertainty, version lineage when relevant, and review status so later reuse does not turn provisional prose into a confirmed claim.
