# SVG rendering guide

Use this guide after the research content and topology are settled enough to compose. It defines a restrained default visual system and the checks required for an editable SVG. Adapt it when the researcher supplies another visual direction.

## SVG structure

- Set a `viewBox` that tightly contains the complete composition, with a deliberate outer margin. Give the root an accessible `<title>` and `<desc>` and use `role="img"` when appropriate.
- Keep ordinary labels as live `<text>` with explicit `<tspan>` line breaks. Avoid `foreignObject`, text converted to paths, and unsupported web fonts. Use a fallback stack such as `Inter, "Avenir Next", "Helvetica Neue", Arial, sans-serif`.
- Group each semantic region and each node with stable, descriptive IDs. Keep connectors in a group before the node groups so lines render behind shapes.
- Define repeated colours, type styles, markers, and node styles in `<defs><style>`. Reuse classes instead of duplicating inline attributes.
- Use vector shapes and paths. Add `vector-effect="non-scaling-stroke"` to strokes when the SVG may be resized substantially. Leave enough room around marker ends so arrowheads are not clipped by the viewBox or node boundary.

## Default visual system

Use this palette only when the project has no established visual language:

| Role | Colour |
| --- | --- |
| Canvas | `#F7F8F6` |
| Surface | `#FFFFFF` |
| Primary ink | `#18212B` |
| Muted ink | `#66717C` |
| Hairline | `#C9D0D5` |
| Theory / framing | fill `#E3EEE9`, accent `#2F6B59` |
| Question / focal issue | fill `#F5E8C8`, accent `#9A6815` |
| Inquiry / method | fill `#E3EAF6`, accent `#3F6092` |
| Open or proposed | fill `#F3F0EA`, accent `#8B806F` |

Use colour in broad, quiet areas and reserve saturated accents for short rules, small labels, or focal outlines. Check that the figure remains understandable in grayscale.

Establish three text levels rather than styling every node independently. At a 1200–1600 px wide viewBox, a useful starting range is 28–36 px for the figure title, 17–21 px for group or focal labels, and 14–17 px for node text. Relationship labels may be 12–14 px. Adjust the canvas or wording before reducing body text below a comfortable page-width reading size.

## Geometry and text

- Align visible edges and centres to a shared grid. Use consistent corner radii within a role; variation should signal a different role, not accidental styling.
- Fit boxes to their content and importance. Keep at least one line-height of vertical padding and roughly 1.3–1.8 em of horizontal padding around text.
- Keep node text left aligned when it contains more than one short line. Centre only compact labels or a deliberately focal question.
- Aim for two to four short lines per node. Avoid manual line breaks that leave a single word or punctuation mark on its own line.
- Use whitespace to separate semantic regions. Do not use extra empty canvas as a substitute for grouping or alignment.

## Connector treatment

- Use paths with explicit anchors on the visible node boundary. Keep the main route solid and 1.5–2 px; use a dashed route for revision, feedback, or unresolved relations.
- Use one arrow marker system across the figure. Arrowheads should be smaller than the node text height and visually attached to the line.
- Put edge labels in a dedicated group with a canvas-coloured or surface-coloured rounded background. Keep a clear gap between the label and arrowhead.
- Route around nodes with 16 px or more visual clearance. Prefer one bend for a diagonal relation and no bend for aligned nodes. Move nodes before adding several compensating bends.

## Render, inspect, revise

Render the saved SVG with a renderer that preserves the full `viewBox`. Inspect both the full canvas and the figure at the size at which it will appear in the proposal, slide, or document.

Run these passes in order:

1. **Fidelity:** every substantive source component and relation is present; compression has not altered agency, direction, modality, or certainty.
2. **Five-second scan:** the focal relation or question and the overall reading route are visible before the body text is read.
3. **Composition:** the viewBox is balanced, content fills the page appropriately, and no node is stranded or crowded.
4. **Typography:** no clipping, awkward wrap, isolated token, or unreadably small label.
5. **Connectors:** no line crosses a node or label, arrowheads meet the correct boundary, feedback routes stay distinct, and edge labels sit in clear space.
6. **Reduction:** inspect a thumbnail or half-size rendering. Hierarchy and group boundaries should remain legible even when body text cannot be read.

Fix the observed problems in one coordinated pass, render again, and perform a focused second inspection. Continue only when the second rendering reveals a concrete defect that affects meaning or usability.
