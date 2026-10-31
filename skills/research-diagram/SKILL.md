---
name: research-diagram
description: Create or revise publication-quality editable SVG diagrams of conceptual relations, arguments, and research designs for theory-led humanities and social-science work. Use for research frameworks, proposal diagrams, and faithful redraws; do not treat a diagram as approval of a research position.
---

# Research Diagram

Make a visual argument that lets a reader see what the research asks, how its parts relate, and which claims remain open. The diagram is a visual expression of the researcher's material, not a new authority for research questions, methods, or conclusions.

## Choose the task

- **Conceptual or argument map:** show distinctions, tensions, candidate inferences, objections, and revisions.
- **Research design:** show the question, theoretical resources, materials, analytical operations, and intended argument. Show iteration when concepts and cases inform one another.
- **Faithful redraw:** preserve the supplied diagram's content, topology, and visual hierarchy unless the user asks for redesign. Report any illegible or ambiguous part rather than guessing.

Read the [diagram model and layouts](references/diagram-design.md) before converting prose into nodes, relations, and a composition. For SVG output, also read the [SVG rendering guide](references/svg-rendering.md). These references offer visual grammars and production rules, not a universal research method.

## Work from the selected sources

Read only the material relevant to the requested diagram. Identify the source of each substantive node and connection. Preserve the difference between researcher wording, verified source claims, agent interpretation, and an open question. Follow the applicable Research and project `AGENTS.md` files for intellectual authority and review states. Do not promote a tentative question, case choice, method, interpretation, or expected contribution into an established result. Do not invent a literature gap or case finding.

Before drawing, make a compact working model of zones, nodes, and labelled relationships. Keep it format independent so the same intellectual structure can be rendered in SVG, PPTX, draw.io, or another suitable format. The working model is a production aid; the cited research files remain canonical. Do not create a new research tracker or update proposal prose as a side effect.

Do not translate prose mechanically into one equal box per sentence or numbered item. Identify the diagram's focal problem, conceptual core, theoretical lens, inquiry, and supporting steps, then choose forms and visual weight by role. Preserve multi-part relations as structures: if a claim concerns a participant, a system, and music in one relation, keep all three visible instead of compressing them into a simpler sentence. Shorten labels only when the meaning and degree of certainty remain intact.

If a crucial relationship is absent or materially ambiguous, present a small number of diagram choices and their consequences. A draft can still mark an unresolved relation as `agent-proposed`; file creation or polished layout never changes its review state.

## Render and deliver

The requested output format takes priority. If none is specified, deliver an editable SVG as the main file. Use a low-detail composition draft when the structure is uncertain, then produce a final SVG with live text, separate vector shapes and connectors, and meaningful groups or IDs. Do not flatten the diagram into a bitmap, convert ordinary labels to outlines, or embed the whole figure as one image.

If the user wants to edit the figure as slide objects in macOS WPS Office, produce an optional PPTX with independent native text, shapes, connectors, and arrows. Use the available presentation authoring runtime for PPTX, resolving its workspace dependencies first; inspect the saved file in WPS Office when available and state if compatibility was not checked. For draw.io, use editable nodes and edges in a `.drawio` file. PNG and PDF are optional viewing or insertion copies; neither replaces the SVG source by default. Keep rendering choices separate from the working model so a later renderer can use the same content without changing its meaning.

Separate the passes: first source fidelity and topology, then composition and hierarchy, then typography, colour, and connector refinement. Render from the saved final file after each material layout change. Inspect the whole canvas and the figure at its intended document or slide size; revise observed defects instead of trusting coordinates or source code alone. Do not make a routine approval gate for cosmetic choices. Ask the researcher to decide only when a proposed question, conceptual relation, case role, method, or contribution would otherwise be silently selected on their behalf.

Inspect the final SVG itself at its intended viewing size, and inspect any additional exported format separately. Confirm that the visual hierarchy is apparent at thumbnail size, the reading route is recoverable without reading every sentence, and the focal question or relation has the strongest visual weight. Check text clipping, contrast, canvas balance, connector endpoints, arrow direction, and whether line style or colour makes uncertain relations appear settled. When an output format cannot preserve a feature, describe the difference. Deliver the editable SVG and any requested companion files, with a short note on the source material, any `agent-proposed` content, and remaining researcher decisions.
