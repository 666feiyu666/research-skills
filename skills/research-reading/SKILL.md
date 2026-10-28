---
name: research-reading
description: Discover, retrieve, verify, closely read, discuss, and synthesize scholarly literature, including sources resolved through Zotero. Use for bibliographic discovery, evidence-state checks, source-grounded reading dialogue, compact source records, optional session or semantic cards, and cross-source synthesis. Do not use to organize the Zotero library, analyze primary research objects, choose the researcher's position, draft manuscript prose, or manage project progress.
---

# Research Reading

Help the researcher understand and use scholarship while keeping source evidence, researcher interpretation, and model inference distinguishable.

## Inputs and Evidence

Start from the researcher's question, scope, supplied texts, Zotero key or query, existing notes, and requested output. Exploratory reading may begin from a broad theme or puzzle; do not require an established paper question or immediate manuscript use.

Keep evidence state explicit where it affects the answer:

1. `discovered`;
2. `bibliographically verified`;
3. `abstract- or preview-verified`;
4. `full-text verified`;
5. `secondary-only`.

Do not present an abstract-level inference as a full-text claim. Preserve locators for definitions, disputed claims, argumentative moves, answers, and passages on which later reasoning depends. Never invent metadata, quotations, page numbers, DOI, translations, or source positions.

## Modes

- `discovery`: find and deduplicate scholarship, then verify identity and access;
- `screening`: assess likely relevance from metadata, abstracts, contents, or previews;
- `close-reading`: inspect the designated full text and reconstruct relevant passages with locators;
- `reading-dialogue`: answer source-grounded questions in the order they arise;
- `source-record`: maintain a compact work-level index of identity, access, actual coverage, and links to existing reading artifacts;
- `session`: preserve an authorized chronological checkpoint from a substantive reading dialogue;
- `knowledge-card` or `question-card`: preserve one researcher-selected semantic unit or unresolved question;
- `synthesis`: compare sources around an explicit question without erasing differences or evidence states.

Combine modes only when the request calls for them.

## Zotero Retrieval

When the researcher asks to read a work in Zotero, use the local Zotero route to resolve a unique item, inspect its attachments, and obtain the selected file or indexed text. Treat collection paths as mutable and preserve stable item and attachment keys when useful. Do not silently choose among different editions or translations.

Attachment metadata or indexed text establishes access provenance, not full-text verification. Promote a source to `full-text verified` only after checking the resolved file or relevant passages. For PDFs, inspect the native text layer first; use `scripts/pdf_text.py` when helpful and `scripts/ocr_fallback.py` only when extraction is missing or unreliable.

## Reading Dialogue

Answer the immediate question before expanding outward. Distinguish:

- what the source clearly supports;
- what is a reasonable interpretation;
- what is the researcher's formulation;
- what is a model suggestion;
- what remains uncertain or requires another passage or source.

Preserve the researcher's puzzle in their own terms. Test a proposed resolution for source support, compatibility, extension, or conflict without supplying a polished position on the researcher's behalf. Ask at most one focused question when a missing distinction materially changes the inquiry.

## Optional Durable Artifacts

Source records, sessions, cards, processed notes, and syntheses are available artifact roles, not a mandatory chain.

Create only the substantive artifact the researcher requests or clearly authorizes. A card does not require creating a session first, and saving a session does not authorize creating a card or synthesis.

When an authorized write creates, moves, or renames a durable reading artifact, keep the same work's canonical source record and direct backlinks synchronized as mechanical navigation maintenance. If the project requires a work-level source record and none exists, create the minimal record from verified source identity, actual coverage, artifact links, review state, and dates. This maintenance is part of the authorized write; it does not authorize a new interpretation, card, session, synthesis, project application, research-position change, draft revision, or project-status update.

Before creating, revising, relocating, or indexing a source record, reading session, knowledge card, or question card, read [Source Records, Reading Sessions, and Semantic Cards](references/reading-dialogue-and-cards.md). Use its storage, backlink, and maintenance rules together with the current project's canonical artifact policy.

Keep the roles distinct:

- a `source-record` owns compact identity, access, actual coverage, and links; it is not a comprehensive summary;
- a `session` owns chronological dialogue provenance and consequential corrections;
- a `knowledge-card` owns one stable source-grounded concept, distinction, relation, or argumentative movement selected by the researcher;
- a `question-card` owns one consequential unresolved question, current support, and a concrete route back into inquiry;
- a `processed-note` is an explicitly requested thematic working document;
- a `synthesis` compares several sources around a stated organizing question.

For a card, recover the semantic center from the researcher's dialogue or instruction. If it is absent or materially ambiguous, ask one focused construction question. Do not invent a priority or turn uncertainty into settled knowledge to fill a template.

Templates in `templates/` and format references are optional. Select a locale variant according to the intended artifact language, not automatically from the language of the conversation.

## Workflow

1. Establish the question, evidence level, source scope, and requested output.
2. Discover or resolve the source through authoritative bibliographic routes and deduplicate by DOI, then title, author, year, edition, and translation.
3. Verify access before claiming coverage. Mark OCR, translation, excerpt, preview, or secondary-source limits.
4. Read only what the question and requested coverage require.
5. Reconstruct relevant content with locators and distinguish evidence from interpretation.
6. In cross-source work, state the comparison line and preserve disagreements, edition differences, and unresolved conflicts.
7. Return or save only the requested substantive artifact, together with the minimal same-source navigation maintenance described above. Do not silently revise research questions, project positions, outlines, drafts, or project status.

## Researcher Authority

Treat source records, sessions, cards, syntheses, and model interpretations as researcher-reviewable. Verification establishes what a source says or how it can be recovered; it does not make the model's organization the researcher's position.

This skill owns scholarship work. It does not newly analyze the project's empirical objects, decide the research problem, draft manuscript prose, or execute a research plan. It may use researcher-designated questions, plans, drafts, or analysis results as context without modifying them.
