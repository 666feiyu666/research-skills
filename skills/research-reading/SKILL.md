---
name: research-reading
description: Discover, screen, retrieve, verify, closely read, and synthesize scholarly literature; create traceable reading notes, literature maps, bibliographies, and matrices. Use when Codex needs to search a field, identify or compare scholarship, inspect a source with page or location mappings, or consolidate verified literature notes. Do not use to analyze the project's empirical or primary research objects, manage project progress, or draft the paper itself.
---

# Research Reading

Treat literature discovery, screening, close reading, and synthesis as distinct evidence states within one connected workflow.

## Inputs

Use the research question, search scope, supplied texts, existing notes, and requested output that the researcher provides for the current task. Do not require fixed project filenames. Read only project context that materially helps determine relevance.

## Modes

- `discovery`: search for relevant scholarship, resolve names and titles, verify metadata, and map a field or debate.
- `screening`: assess likely relevance from authoritative metadata, abstracts, tables of contents, or limited previews.
- `close-reading`: extract and critically read a supplied full text while preserving page, section, or paragraph mappings.
- `synthesis`: consolidate already-processed sources into literature notes, conceptual comparisons, reading paths, or matrices.

Infer the mode from the request. Combine modes only when the available evidence supports the transition.

## Evidence States

Keep these states explicit:

1. discovered;
2. bibliographically verified;
3. abstract- or preview-verified;
4. full-text verified;
5. secondary-only.

Do not present an abstract-level inference as a full-text claim. Separate author claims, researcher judgments, and model suggestions.

## Workflow

1. Establish the question, scope, language, date range, disciplines, and supplied materials relevant to the task.
2. For discovery, search multiple formulations and prefer original works, DOI records, publishers, journals, proceedings, repositories, or library catalogs.
3. Deduplicate by DOI, then normalized title, author, year, edition, and translation.
4. For close reading, inspect the native text layer first. Use `scripts/pdf_text.py` for PDFs and `scripts/ocr_fallback.py` only when extraction is missing or unreliable.
5. Preserve source locations for definitions, arguments, evidence, quotations, tables, figures, and footnotes. Mark OCR uncertainty.
6. For synthesis, organize verified material by question, concept, chronology, method, position, or disagreement without erasing source attribution.
7. Write to the user-specified file or return the requested artifact. Do not silently update research questions, arguments, or manuscript text.

## Outputs

Adapt the output to the mode:

- search map or prioritized bibliography;
- screening table;
- page-mapped reading record;
- literature note or concept comparison;
- literature matrix;
- evidence gaps and next reading path.

Use `templates/reading-record.md`, `templates/note-batch.md`, or `templates/literature-matrix.md` only when they fit the requested artifact. See `references/output-formats.md` for reusable discovery formats.

## Quality Boundaries

- Do not invent bibliographic metadata, page numbers, DOI, quotations, or source positions.
- Do not bypass access restrictions.
- Treat literature as evidence about scholarship, not as a substitute for analysis of the project's actual research objects.
- Send project-level implications to `research-thinking`, empirical materials to `research-analysis`, and verified sources needed for prose to `research-writing`.
