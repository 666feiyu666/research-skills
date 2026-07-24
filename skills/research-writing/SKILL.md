---
name: research-writing
description: Create and iteratively revise academic outlines, sections, manuscripts, notes, and argument-led prose; audit arguments and citations, compress text, convert to LaTeX, and improve rhetoric while preserving the researcher's claims, voice, citations, and uncertainty. Use when Codex needs to turn a researcher-supplied task packet into a writing artifact or continue editing a designated working artifact. Do not use to invent evidence, decide the research question, analyze raw research objects, or manage project progress.
---

# Research Writing

Work from the materials supplied for the current writing task rather than requiring a predetermined project-file schema.

## Task Inputs

A task packet may contain:

- the current research question, purpose, or intended contribution;
- relevant reading or analysis notes;
- a research or argument plan;
- a manuscript mind map or rough structure;
- an existing outline, section, or draft;
- audience, length, format, and destination.

These inputs may appear in the prompt, conversation, or any user-designated files. Give priority to the current user instruction, then designated materials, then the active working artifact, and only then supplementary project context. Missing standard filenames are not a defect.

## Working Artifact

Distinguish:

- **source inputs**: research questions, notes, evidence, records, and reference drafts that remain read-only;
- **working artifact**: the outline, section, manuscript, or note explicitly being created or revised.

Create the working artifact at the requested location. On follow-up revisions, update the same artifact by default. Create a separate version only when the user requests alternatives, the direction changes substantially, or the existing text must remain as a historical source.

## Modes

- `outline`: create or revise a manuscript structure with distinct section tasks and dependencies.
- `section-draft`: draft the requested section from relevant claims, notes, and evidence.
- `rewrite`: revise a designated text with the smallest change that satisfies the request.
- `argument-audit`: inspect claims, evidence, inference, counterarguments, and paragraph functions.
- `citation-audit`: check whether citations exist and support nearby claims; distinguish internal consistency from external verification.
- `compression`: preserve indispensable claims and evidence while removing repetition or excess background.
- `polish`: improve clarity, rhythm, transitions, diction, and academic register without redesigning the argument.
- `latex-output`: convert stable content and verified citation keys without inventing BibTeX entries.

## Workflow

1. Identify the mode, writing objective, working artifact, audience, length, and output format. Ask only when an unresolved choice would materially change the result.
2. Read only the supplied and directly relevant inputs.
3. Extract the current claim, necessary subclaims, evidence, inference, terminology, constraints, and unresolved gaps.
4. Create or revise the working artifact. Mark genuine gaps with `[需证据]`, `[需引用]`, or `[待确认]` instead of filling them by invention.
5. Check that each section or paragraph has a distinct function and that the strength of the prose matches the evidence.
6. Deliver the artifact first. Briefly report substantive changes, unresolved gaps, and any conflict that requires `research-thinking`.

Templates in `templates/` are optional aids, not mandatory output formats.

## Authorship and Evidence

- Preserve strong researcher judgments unless asked to challenge them.
- Preserve citations, quotations, uncertainty, and deliberate terminology.
- Do not turn a provisional thought into false certainty.
- Do not let rhetorical fluency conceal a conceptual or evidentiary gap.
- Do not update official research questions or project status unless explicitly requested.

## Optional External Models

Use `scripts/call_model.py` only when the user explicitly requests a named external provider or cross-model comparison. Read `references/providers.md` first, protect unpublished or sensitive text, use configured credentials, and never overwrite the source.

## Handoffs

Receive verified literature from `research-reading`, analysis results from `research-analysis`, and intellectual direction from `research-thinking`. Return project-level conflicts to `research-thinking`, confirmed task status to `research-managing`, and stable research artifacts to `research-publishing`.
