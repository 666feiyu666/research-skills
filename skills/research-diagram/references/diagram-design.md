# Diagram model and layouts

Use these distinctions when they help the actual research. Keep labels short enough to read on the page; put necessary nuance in a caption or accompanying note rather than shrinking everything to fit.

## Format-independent working model

Represent the diagram as zones, nodes, and directed or undirected relations before choosing a renderer:

| Part | Record | Why |
| --- | --- | --- |
| Zone | title, purpose, contained node IDs | Makes visual grouping meaningful. |
| Node | ID, short label, role, source pointer, review state when needed | Prevents a polished box from concealing uncertain authorship. |
| Relation | endpoint IDs, type, direction, short label, source or rationale | Prevents an arrow from implying an unsupported causal or temporal claim. |

Useful node roles include question, concept, theoretical resource, tension, research material, case, analytical operation, candidate inference, intended argument, and open issue. A prototype or system can be a research material or exploratory device; its completion or effectiveness is not automatically the thesis's contribution.

Useful relation labels include *frames*, *contrasts with*, *raises a problem for*, *examines*, *offers a case for*, *tests the scope of*, *may revise*, and *precedes*. Use *supports* only when the cited material warrants support. A plain arrow with no label should have an unmistakable meaning from the layout.

## Convert prose into a visual grammar

Start from the claim structure, not the source document's paragraph or list structure. Decide what the reader should understand after five seconds and what they should discover after reading the labels.

- Find the focal problem or relation. Give it a central position, distinct enclosure, or the strongest accent.
- Separate framing steps from the conceptual core. Short premises can form a quiet argument spine; they do not each need a large card.
- Preserve structures that carry the research claim. A triadic relation, opposition, loop, or nested distinction should become geometry rather than another paragraph inside a rectangle.
- Treat a theory as a lens or framing resource when that is its role. Place it beside or around what it clarifies instead of presenting it as the next temporal step.
- Treat a research question as a hinge between problem construction and inquiry. A method or case analysis can follow from the question without appearing to answer it in advance.
- Do not display item numbers merely because the source uses them. Retain them only when the audience needs to cross-reference the source.

Before drawing, write a one-line composition statement such as: “A quiet three-step premise leads into a central participant–system–music relation; a theoretical lens turns that relation into the focal question; case comparison operationalizes the inquiry.” Use it to judge whether the layout expresses the argument.

## Choose a renderer

| Output | Best use | Editable source requirement |
| --- | --- | --- |
| SVG (default) | Main research figure for proposals, documents, slides, and the web | Live text, separate vector elements, meaningful groups or IDs, and a tested rendered view. |
| PPTX (optional) | Figure edited as slide objects in WPS Office or PowerPoint | Native text, shapes, and connectors; inspect the saved file in the intended editor when available. |
| draw.io | Repeated structural editing and dense boxed diagrams | Separate nodes and edges in `.drawio`; export a viewing copy if needed. |

The working model is shared; visual style and file generation belong to the chosen renderer. Additional formats can be added without changing research-content rules. SVG editability does not imply that WPS Office will expose each SVG element as a native slide object; use PPTX when that specific editing workflow matters. When multiple editable formats are requested, inspect each exported file because their layouts may diverge.

## Layout choices

**Argument spine with relational core:** Use for a line of argument that contains one structurally rich claim. Compress the framing premises into a restrained spine, enlarge the relational core, and let the theory, question, and inquiry form a second movement. This avoids a row or column of equal boxes.

**Conceptual map:** Place the focal problem centrally. Group theories and neighbouring concepts around the specific tensions they illuminate. Draw candidate inferences and counterexamples with distinct line styles; do not imply that every branch converges on one settled answer.

**Research-design framework:** A three-column or layered page can place the question and theoretical resources, materials and analytical operations, and intended argument in separate regions. Connect concepts and cases in both directions when the method calls for revision through analysis. Differentiate principal methods from supplementary material by grouping and labels, not only colour.

**Research sequence:** Use a timeline only for genuinely temporal commitments. A phase may produce a provisional analytical result that feeds back into earlier concepts; show that feedback rather than forcing a one-way pipeline.

**Faithful redraw:** First record the visible nodes, exact wording, region boundaries, and connector topology. Preserve the source's visual organization unless the user explicitly authorizes a reinterpretation. If dense source material is illegible, ask for a better source or mark only the unreadable elements.

## Composition and visual hierarchy

- Give the composition one dominant element, one supporting level, and one quiet level. Use size, position, enclosure, type weight, and colour together; do not make colour carry the hierarchy alone.
- Size nodes by semantic importance and content. Equal boxes are appropriate only for genuinely parallel roles. A focal relation, a brief premise, and a method should not share the same visual weight.
- Prefer a compact page-shaped composition for proposal figures. Start near 1.5:1 to 1.8:1 for a landscape document figure; use a wider canvas only when the topology requires it. If the diagram will be inserted at page width, test it at that width before delivery.
- Keep the occupied content visually balanced within the viewBox. Avoid a title floating above a distant diagram, a large empty band between related groups, or a final node stranded at the canvas edge.
- Use a spacing system rather than ad hoc coordinates. As a starting point, use 8 px increments, 20–28 px node padding, 28–48 px gaps within a group, and 56–88 px between major regions. Adjust for the chosen canvas and type size.
- Use containers or soft background regions to show semantic grouping. A container needs a title or clear visual purpose; do not place a border around every set of nearby objects.
- Put secondary detail in callouts or a caption. Do not shrink the whole diagram to preserve sentences that can be shortened without changing the claim.

## Connectors

- Route connectors behind nodes. Prefer straight orthogonal paths or restrained curves; use diagonals only when they clarify a close relation and do not disturb alignment.
- Connect from the side facing the target. Avoid lines through unrelated nodes, crossings, small S-bends, and arrowheads that touch text or borders.
- Route feedback or revision relations through an exterior corridor and distinguish them with a dashed line. Keep the loop close to the nodes it connects.
- Place a relationship label on the longest clear segment. Give it a small background or knockout so the line does not run through the text. Shorten the label before forcing it into a crowded gap.
- Use separate directional arrows when each direction means something different. A bidirectional arrow is appropriate only when the same relation truly works both ways.

## Visual language

- Prefer a small number of meaningful regions, a clear entry point, and legible grouping. Dense academic layouts are appropriate when the content warrants them; do not add boxes to fill space.
- Use a restrained neutral foundation plus one primary and one secondary accent. Use colour for roles or regions and line style for relationship status. Include a small legend when these encodings carry meaning. Do not rely on colour alone.
- Prefer solid fills, subtle borders, and flat depth. Avoid gradients, strong shadows, glossy effects, and a page made entirely of outlined grey cards.
- Keep uncertain or `agent-proposed` nodes visibly distinguishable in a working draft, and explain that status in the accompanying note. Remove a status marker only after explicit researcher confirmation.
- Use labelled feedback connections sparingly. Make arrowheads, endpoints, and crossing paths readable.
- For a single-page proposal figure, prefer a concise diagram with a caption over unreadably small text. If the user requires all detail on one page, explain the readability tradeoff and offer a larger page or a second figure.
