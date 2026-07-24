---
name: literature-scout
description: Discover, retrieve, verify, deduplicate, and organize scholarly literature for a research question. Use when Codex needs to search for classic or current scholarship, map a debate or school, identify key authors and works, follow backward or forward citation trails, resolve names and bibliographic metadata, compare positions, build a chronological bibliography or literature matrix, or deliver a source-backed Markdown research overview. Do not use to manage existing project notes, closely read full texts, maintain the whole research project, or draft polished paper prose.
---

# Literature Scout

Find the relevant literature and turn the search results into a traceable source map. Treat discovery, bibliographic verification, claim verification, and full-text reading as different evidence states.

## Boundary with Research Notes

- Use this skill to answer **what literature exists, where it can be found, how it relates, and how confidently its position is known**.
- Use `critical-reading` to closely read newly acquired full texts with page mappings.
- Use `research-notes` to consolidate already-processed reading records, claims, concepts, and researcher judgments into durable project notes.
- Do not silently update `LITERATURE_NOTES.md`, `TERMINOLOGY.md`, or `references.bib`. Offer a candidate handoff after verification.

## Workflow

1. Define the research question, date range, disciplines, languages, output depth, and inclusion criteria. Resolve likely name transliterations or title variants, but label uncertain identifications.
2. Build a query map with core concepts, synonyms, translations, opposing terms, major names, canonical titles, and likely venues. Search more than one formulation.
3. Find seed sources in this priority order:
   - original articles, books, chapters, proceedings, dissertations, or author manuscripts;
   - journal, conference, university repository, DOI, library catalog, or publisher pages;
   - scholarly indexes and high-quality reviews for discovery;
   - secondary summaries only for orientation, never as the sole support for an author's position.
4. Expand from seed sources through reference lists, related works, author bibliographies, special issues, and cited-by trails when accessible. Seek both foundational texts and later corrections or syntheses.
5. Record each candidate with title, author, year, venue or publisher, work type, DOI or stable URL, access status, relevance, school or role, and evidence state.
6. Deduplicate by DOI first, then normalized title, author, year, and edition. Keep translations and substantially revised editions linked rather than merged.
7. Verify before synthesis:
   - **discovered**: title or search result only;
   - **bibliographically verified**: metadata confirmed by an authoritative record;
   - **abstract-verified**: relevance or broad claim supported by an abstract;
   - **full-text verified**: position supported by the work itself, with page, section, or paragraph location where possible;
   - **secondary-only**: position known only through another scholar and requiring follow-up.
8. Separate an author's direct claim from later interpretation. Do not infer a strong theoretical position from a title, keyword list, publisher blurb, or isolated quotation.
9. Synthesize the corpus by chronology, conceptual axis, debate role, method, object, and points of agreement or disagreement. Explicitly distinguish direct participants, precursors, critics, and later synthesizers.
10. Report coverage limits, paywalls, inaccessible texts, ambiguous identities, missing page evidence, and unanswered search branches.

## Source and Search Rules

- Prefer primary and authoritative sources; use current web search when information or access may have changed.
- Cite the page that supports each claim, not a generic homepage or search-results page.
- Preserve DOI and stable URLs. Do not invent DOI, ISBN, page numbers, translations, or publication dates.
- Respect access controls. Do not bypass paywalls, authentication, robots restrictions, or technical barriers.
- Keep quotations short and verify them against the full text. Paraphrase when exact wording is unnecessary.
- Search in the source language and English when the topic is multilingual. Record translated names and titles as aliases.
- Include contrary and revisionist literature; do not build a canon only from sources that confirm the initial framing.

## Default Deliverable

Produce a Markdown document with:

1. scope, naming decisions, and search date;
2. a short conclusion about the shape of the field or debate;
3. a chronological literature table;
4. a scholar or position comparison table;
5. central disagreements and later syntheses;
6. a prioritized reading path;
7. evidence gaps and follow-up queries;
8. linked primary or authoritative sources near the claims they support.

For reusable table schemas and a compact search log, read [references/output-formats.md](references/output-formats.md).

## Quality Check

- Every included work satisfies the stated inclusion criteria or is marked as contextual.
- Canonical status is justified by field position, repeated citation, venue, or influence—not asserted from familiarity alone.
- Each summarized position carries an evidence state; abstract-level knowledge is not presented as full-text analysis.
- Direct participants are not confused with precursors or later method providers.
- Similar-sounding terms such as story, narrative, narration, fiction, discourse, play, game, simulation, and interactivity remain distinct.
- The output makes uncertainty and missing coverage visible.

## Handoff

- Send newly found full texts to `critical-reading` for page-mapped analysis.
- Send verified reading records and claim-level notes to `research-notes` for consolidation.
- Send literature gaps that affect project direction to `research-editor` for project-level review.
- Send only verified sources and claims to `paper-writing`.
