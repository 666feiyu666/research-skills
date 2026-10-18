---
name: research-language-editing
description: Edit English research prose for clarity, precision, coherence, rhythm, register, and consistency while preserving the argument, evidence, citations, uncertainty, and authorial voice. Use for copyediting, sentence- or paragraph-level polishing, refinement of supplied English translations, and final language checks. Use research-language-editing-zh for Chinese prose. Do not redesign the argument, add scholarship or evidence, or optimize text for AI detectors.
---

# Research Language Editing

Improve how the text says what it already means. Preserve the researcher's intellectual content and make the smallest changes that achieve the requested linguistic result.

Select by the target passage's language, not the language of the request. Use this skill for English, including supplied Chinese-to-English translations; use `research-language-editing-zh` for Chinese. For bilingual text, apply each skill only to the relevant passages and preserve cross-language terminology and meaning. Do not translate an artifact merely to edit it.

## Inputs and Authority

Use the designated text, target language, audience, disciplinary register, style guide if supplied, and any researcher-provided samples of preferred voice. Preserve deliberate terminology, technical distinctions, citation placement, quotation wording, uncertainty, and degree of claim strength.

Do not infer that conventional academic phrasing is better than the researcher's specific voice. Naturalness means language responsive to the actual argument, not generic variation or simulated personality.

## Modes

- `copyedit`: correct grammar, syntax, punctuation, agreement, and consistency;
- `clarity`: reduce ambiguity, unnecessary abstraction, repetition, and overloaded sentences;
- `flow`: improve real inferential, contrastive, temporal, or qualifying relations between sentences and paragraphs;
- `register`: calibrate formality and disciplinary tone without inflating claims;
- `bilingual-refinement`: improve a supplied translation or bilingual passage while preserving meaning and source-language distinctions;
- `final-language-check`: identify and fix remaining language-level problems in a stable draft.

## Workflow

1. Establish whether the task is language-only and identify the intended language, audience, register, and permitted degree of intervention.
2. Infer a local voice profile from the supplied prose: characteristic terminology, sentence movement, preferred level of explicitness, and deliberate qualifications.
3. Edit directly at the smallest useful unit. Prefer concrete subjects, precise verbs, and transitions that express actual relations.
4. Check that no edit changed a claim, causal relation, scope, modality, chronology, citation function, or attribution.
5. Return the edited text first, followed by only consequential language choices or unresolved substantive problems.

Remove empty scene-setting, repeated conclusions, mechanical signposting, stock academic phrases, unnecessary symmetry, and formulaic lists when they do not serve the argument. Vary sentence and paragraph form only according to function, not artificial randomness.

## English Editing Priorities

- Correct agreement, possessives, clause punctuation, and dangling modifiers; follow the supplied style guide and established spelling conventions.
- Prefer active clauses when agency is known and relevant; retain passive constructions when the agent is unknown or the research object deserves emphasis.
- Use direct, specific wording and remove verbal padding. Preserve meaningful negation and qualifications; concision must not strengthen a claim.
- Keep modifiers near their referents and coordinate ideas in parallel form. Repair ambiguity without changing analytical relationships.
- Keep paragraphs focused and sentences connected. Adjust emphasis and tense for the passage's function without imposing identical paragraph openings or flattening chronology.
- Replace inflated praise, empty participial tails, and decorative formatting only when they obscure or repeat meaning; technical vocabulary is not a blacklist.

Adapted from [Writing Clearly and Concisely](https://github.com/richyuh/claude-skills/blob/main/writing-clearly-and-concisely/SKILL.md). Apply these preferences within the research boundaries below.

Read [editing examples](references/editing-examples.md) when a concrete comparison would help with concision, agency, parallelism, or the limits of rephrasing. They are illustrations, not a required output format.

## Substantive Boundary

If a sentence cannot be improved without choosing among different meanings, changing the argument, supplying evidence, interpreting a source, or resolving a conceptual problem, preserve the text and flag the exact choice. Do not conceal a substantive gap through fluent prose.

Do not add citations, examples, personal experiences, stylistic quirks, empirical claims, or confidence. Do not rewrite to evade AI detection or claim that wording is human-authored. Do not erase productive hesitation or disciplinary precision merely to make prose smoother.

Treat substantial rephrasing and every meaning-sensitive choice as researcher-reviewable. Language cleanup does not confirm the underlying research claim.

