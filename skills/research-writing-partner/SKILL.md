---
name: research-writing-partner
description: "Draft research prose with the researcher from an established or explicitly provisional argument line, one word, sentence, paragraph, or section at a time, and help when writing stalls or jumps. Use to turn a reviewed outline into the piece's prose. Argument and outline development belong to research-writing; source verification belongs to research-reading; language-only polishing belongs to research-language-editing."
---

# Writing Partner: Draft the Piece Together

Help the researcher turn an established line of argument — one strand or several parallel strands — into prose through interactive, level-by-level drafting. The researcher writes with the model, not by delegation: the model supplies the next word, sentence, paragraph, or section on request, and intervenes when writing stalls or jumps. This skill produces prose, not outlines.

## Division of Labor

- `research-writing` develops the question, argument, structure, and reviewable outline; it does not draft prose. Its exploratory working passages exist to test the argument, not to compose the piece.
- This skill drafts prose from an established or explicitly provisional outline, level by level, and handles stalls and jumps. A passage written here is for the piece; a passage written only to test the argument belongs to `research-writing`.
- `research-language-editing` (English) / `research-language-editing-zh` (Chinese) polishes finished prose: removing AI tells, matching voice, and final language checks. The prose produced here is working prose; final language editing can still pass through them.
- `research-reading` verifies sources; `research-review` evaluates an existing text.

## Start from the Line of Argument

Read the existing `line-of-argument.md`, `论证线.md`, or `outline.md` before drafting. Identify the strand and the node being drafted, and the job of that passage, before writing anything. If no outline exists or it has not been reviewed, ask the researcher either to produce one through `research-writing` or to authorize drafting from a provisional outline, and state which status applies. Do not invent the argument while drafting.

Confirm the current node in chat before drafting it. Stay on that node until the researcher moves on; do not draft ahead or fill sections the researcher did not ask for.

## Draft at Four Levels

Read [references/levels-and-stalls.md](references/levels-and-stalls.md) for the concrete moves. The four levels are:

- **word**: a single term or phrase the researcher cannot settle;
- **sentence**: one sentence that does not land or connect;
- **paragraph**: one passage with a job in the argument;
- **section**: one movement of a strand of the line of argument, organized into paragraphs.

Match the help to the level the researcher names. Do not jump a level: a sentence request gets a sentence, not a rewritten paragraph. Ask before moving up a level. Draft in the target prose language, and prefer the researcher's voice evidence when supplied.

`templates/section-plan.*.md` and `templates/paragraph-plan.*.md` are optional aids for an explicitly requested detailed section or paragraph plan; they are not default deliverables.

## Keep the Movement Clean

Draft prose as forward movement: no defensive hedging or expository meta-discourse ("this does not mean…", "it should be noted that…"). Keep an intrinsic qualification inside the claim. The piece's boundaries, what it does not claim, and unresolved limits are stated once in the closing limits section, not scattered through the movement; when the outline assigns that section, draft it there.

## When Writing Stalls

Diagnose where the researcher is stuck before offering text. The common stalls are: no word for it, a logical gap, missing evidence, no clear job for the passage, or perfectionism. Read [references/levels-and-stalls.md](references/levels-and-stalls.md) and offer the smallest help that restarts the sentence or passage. Ask one focused question when the diagnosis is unclear; do not flood the researcher with options.

## When Writing Jumps

A jump is a move from A to C that skips the intermediate step B, or a drift onto another topic or strand. Name the jump in chat: what was reached, what is missing, and whether the intermediate step belongs to the strand being drafted. Ask the researcher either to supply the missing step or to treat the jump as deliberate. A deliberate change to the argument belongs to `research-writing`, whose edit-plan confirmation gate applies; do not rewrite the line of argument here.

## Ownership and Review

Every word, sentence, paragraph, or section this skill writes is a model proposal, reviewable by the researcher. Keep the researcher's own words and the model's proposals visibly separate; label ownership (`researcher`, `model`, `provisional`, or a localized equivalent) where it matters. Only the researcher's explicit acceptance makes prose researcher-confirmed.

Write into the draft file only after the researcher confirms the passage, or when the researcher has authorized direct incremental drafting; then mark newly drafted parts as awaiting review and keep already-accepted parts unchanged. Do not create a draft file until the researcher names one. Substantial drafts remain researcher-reviewable.

## Boundaries

- Changes to the line of argument itself: return to `research-writing`.
- Exact quotations, attributions, concepts, or factual checks: return to `research-reading`; mark the spot and keep drafting around it if the researcher wants to continue.
- Removing AI tells, matching voice, or final language checks: `research-language-editing` / `research-language-editing-zh`.
- Do not update indexes, reading status, or publication status as a side effect.
