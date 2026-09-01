---
name: research-reading
description: Discover, screen, retrieve, verify, closely read, and synthesize scholarly literature, including resolving and reading attachments from a user's Zotero Desktop library through its local API; create traceable source-faithful notes, accessible source routes, researcher-processed notes, literature maps, bibliographies, and matrices. Use when Codex needs to search a field, locate a work or readable file in Zotero, inspect a full text with page or location mappings, review or restructure existing reading notes, distinguish source notes from processed notes, compare scholarship, or help a researcher absorb theory without replacing the researcher's own intellectual work. Do not use to organize the Zotero library, analyze the project's empirical or primary research objects, manage project progress, or draft the paper itself.
---

# Research Reading

Keep literature evidence, source-faithful reconstruction, and later intellectual processing distinct within one connected workflow.

## Inputs

Use the question, scope, language, supplied texts, Zotero item query or key, existing notes, and requested output. Read only project context that materially helps. Do not require fixed filenames.

## Zotero Retrieval

When the user asks to read a work in their Zotero library, use the Zotero Desktop skill and local API. Check `status`, resolve a unique bibliographic item with `search`, inspect its attachments with `children`, then obtain the selected attachment through `file-url` or `fulltext` as appropriate. Keep Zotero's role limited to library lookup, attachment resolution, and requested indexed-text access; hand content reading to the matching file workflow.

- In this workspace, treat the active local Zotero library as the source library for humanities and social-science learning and research.
- Treat collection names and parent chains as mutable navigation state. Preserve stable collection, item, and attachment keys for reusable routes, then refresh the current displayed collection path and resolved attachment path through the local API instead of trusting a historical path.
- Prefer an existing local file for the requested edition, translation, or attachment type. Do not silently choose among substantively different versions.
- Preserve the Zotero item key, attachment key, filename, content type, link mode, and resolved local path in the reading artifact when relevant.
- Treat attachment lookup or indexed full text as access provenance, not evidence verification. Promote a work to `full-text verified` only after opening and checking the resolved file or verifying the requested passages against the attachment.
- If no usable file URL, local path, or indexed full text is available, report the attachment metadata as an access blocker; do not claim that the file was read.
- Hand the resolved file to the matching local file-reading workflow. For PDFs, follow the text-layer and OCR sequence below.

## Modes

- `discovery`: find scholarship, verify metadata, and map a field or debate.
- `screening`: assess likely relevance from authoritative metadata, abstracts, tables of contents, or limited previews.
- `close-reading`: inspect a supplied full text and preserve page, section, paragraph, figure, table, and footnote mappings.
- `source-noting`: build an accessible note that follows the author's questions, argument, evidence, qualifications, and answers.
- `researcher-processing`: reorganize verified source material around a selected question, theme, concept, debate, chronology, or method while preserving attribution.
- `synthesis`: compare or consolidate multiple already-processed sources without erasing differences among works or evidence states.

Infer the mode from the request. Combine modes only when the evidence and requested note state support the transition.

## Evidence States

Keep these states explicit:

1. discovered;
2. bibliographically verified;
3. abstract- or preview-verified;
4. full-text verified;
5. secondary-only.

Do not present an abstract-level inference as a full-text claim.

## Note States

Keep note state separate from evidence state:

1. `source-record`: detailed, source-ordered reconstruction of what the author writes and how the argument proceeds;
2. `source-entry`: a concise, source-faithful route into a longer text or source record;
3. `processed-note`: material actively selected, connected, restated, questioned, or compared for learning;
4. `cross-source-synthesis`: a comparison or consolidation across works.

A processed note may follow the author’s or researcher’s question, a concept, debate, method, or another explicit line. Processing means active reorganization and interpretation.

## Workflow

1. Establish the requested evidence state, note state, scope, and organizing line.
2. For discovery, search multiple formulations and prefer original works, DOI records, publishers, journals, proceedings, repositories, and library catalogs.
3. Deduplicate by DOI, then normalized title, author, year, edition, and translation.
4. Resolve access before claiming evidence. For a Zotero source, follow the Zotero retrieval route above and retain the item-to-attachment-to-file chain.
5. For close reading, inspect the native text layer first. Use `scripts/pdf_text.py` for PDFs and `scripts/ocr_fallback.py` only when extraction is missing or unreliable.
6. Preserve source content and location. For important definitions, questions, argumentative moves, answers, examples, qualifications, tables, figures, and footnotes, record a paraphrase and locator; add a short original-language excerpt when it directly supports the point. Mark translations and OCR uncertainty.
7. For `source-noting`, follow the author's order. Add a `source-entry` before a long record rather than deleting detail. State the question, why it arises, the argument route, answer, and indispensable distinctions; attach verified excerpts and locators when available.
8. Keep the detailed source record below the entry. Preserve argumentative transitions and functions, not every sentence. Distinguish the author's claim from the note writer's explanation.
9. For `researcher-processing`, use an explicit organizing line and verified notes or full text. Preserve excerpts and locators for definitions, contested claims, argumentative steps, and answers. Separate `[作者主张]`, `[研究者表述]`, and `[模型建议]`.
10. When the researcher identifies a source-based puzzle, tension, or ambiguity, preserve it in the researcher's own terms. If the researcher proposes a resolution, check its internal coherence and whether it is source-supported, source-compatible, an extension, or a conflict. Do not require every processed note to contain a puzzle or resolution.
11. Do not label model-generated prose as the researcher's understanding. If the researcher has not supplied a formulation, offer prompts, a source-grounded candidate, or a structure labeled `[模型建议／待研究者确认]`; do not supply a polished resolution before the researcher has begun formulating one.
12. For synthesis, preserve source attribution, differences among works, changes across editions or dates, and unresolved conflicts.
13. Write to the user-specified file or return the requested artifact. Do not silently update research questions, arguments, or manuscript text.

## Reviewing Existing Notes

Classify the note state; check source content and locations; separate author claims, researcher judgments, model suggestions, and project implications. If a record is hard to enter, add or repair its source-entry before rewriting it. Keep a source route distinct from a later theory map. Move to processing only when requested or when the researcher has begun reformulation.

## Outputs and Resources

Adapt output to the mode. Use these resources only when helpful; templates are optional:

- `templates/reading-record.md` for a source-entry plus detailed source record;
- `templates/source-route-map.md` for a work-level or multi-chapter source route;
- `templates/processed-note.md` for researcher processing;
- `templates/note-batch.md` for consolidating existing fragments;
- `templates/literature-matrix.md` for cross-source comparison;
- `references/output-formats.md` for discovery and comparison formats.

## Researcher Review

Treat every source note, processed note, synthesis, literature map, bibliography, or matrix created or substantially revised here as researcher-reviewable. Ask the researcher to inspect consequential source reconstructions, organizing choices, model interpretations, omissions, and distinctions between source content and researcher understanding. Source verification does not by itself make the model's organization the researcher's confirmed view.

## Independent Scope and Later Reuse

- This Skill independently owns scholarship discovery, retrieval, verification, close reading, source-faithful noting, researcher-directed processing, and literature synthesis.
- It may use a researcher-supplied question, research problem, outline, draft, prior note, or source list as an organizing input without requiring the capability that produced it.
- It does not analyze the project's empirical objects, choose the researcher's substantive position, redesign the research problem, draft manuscript prose, or update project status.
- When the current task reveals a need for object-level analysis, intellectual design, or writing, finish the supported reading result and state the exact unresolved need.
- A verified reading artifact may later serve as input to research thinking, analysis design, writing, manuscript development, programme design, or meta-reflection when the researcher designates it. Preserve source identity, evidence state, locators, model interpretation, researcher-review state, and open checks so later use does not erase provenance.
- Do not launch, schedule, or assign that later work.

## Quality Boundaries

- Do not invent bibliographic metadata, page numbers, DOI, quotations, translations, or source positions.
- Keep quotations short and functional; use accurate explanation or paraphrase for extended material.
- Do not treat source fidelity as exhaustive paragraph-by-paragraph summary.
- Do not insert project applications throughout a source note unless explicitly requested; keep them in a labeled, separate layer.
- Do not treat a source route map as the researcher's theory map.
- Do not bypass access restrictions.
- Treat literature as evidence about scholarship, not as a substitute for analysis of the project's actual research objects.
