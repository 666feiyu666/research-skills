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

## Choose a renderer

| Output | Best use | Editable source requirement |
| --- | --- | --- |
| SVG (default) | Main research figure for proposals, documents, slides, and the web | Live text, separate vector elements, meaningful groups or IDs, and a tested rendered view. |
| PPTX (optional) | Figure edited as slide objects in WPS Office or PowerPoint | Native text, shapes, and connectors; inspect the saved file in the intended editor when available. |
| draw.io | Repeated structural editing and dense boxed diagrams | Separate nodes and edges in `.drawio`; export a viewing copy if needed. |

The working model is shared; visual style and file generation belong to the chosen renderer. Additional formats can be added without changing research-content rules. SVG editability does not imply that WPS Office will expose each SVG element as a native slide object; use PPTX when that specific editing workflow matters. When multiple editable formats are requested, inspect each exported file because their layouts may diverge.

## Layout choices

**Conceptual map:** Place the focal problem centrally. Group theories and neighbouring concepts around the specific tensions they illuminate. Draw candidate inferences and counterexamples with distinct line styles; do not imply that every branch converges on one settled answer.

**Research-design framework:** A three-column or layered page can place the question and theoretical resources, materials and analytical operations, and intended argument in separate regions. Connect concepts and cases in both directions when the method calls for revision through analysis. Differentiate principal methods from supplementary material by grouping and labels, not only colour.

**Research sequence:** Use a timeline only for genuinely temporal commitments. A phase may produce a provisional analytical result that feeds back into earlier concepts; show that feedback rather than forcing a one-way pipeline.

**Faithful redraw:** First record the visible nodes, exact wording, region boundaries, and connector topology. Preserve the source's visual organization unless the user explicitly authorizes a reinterpretation. If dense source material is illegible, ask for a better source or mark only the unreadable elements.

## Visual language

- Prefer a small number of meaningful regions, a clear entry point, and legible grouping. Dense academic layouts are appropriate when the content warrants them; do not add boxes to fill space.
- Use colour for roles or regions and line style for relationship status. Include a small legend when these encodings carry meaning. Do not rely on colour alone.
- Keep uncertain or `agent-proposed` nodes visibly distinguishable in a working draft, and explain that status in the accompanying note. Remove a status marker only after explicit researcher confirmation.
- Use labelled feedback connections sparingly. Make arrowheads, endpoints, and crossing paths readable.
- For a single-page proposal figure, prefer a concise diagram with a caption over unreadably small text. If the user requires all detail on one page, explain the readability tradeoff and offer a larger page or a second figure.
