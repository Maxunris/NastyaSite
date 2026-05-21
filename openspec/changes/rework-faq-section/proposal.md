## Why

The FAQ section currently relies on transparent hotspots over the exported page image, so the plus animations are detached from the visible symbols and the answers appear in a separate floating panel. The Figma reference shows a real accordion: collapsed rows use right-aligned plus marks, and expanded rows reveal the answer inline with the same divider, spacing, typography, and a right-aligned minus mark.

## What Changes

- Rebuild the FAQ area as a real HTML/CSS accordion overlay that visually matches the Figma reference instead of using the old floating answer panel.
- Show all six FAQ rows collapsed by default with consistent typography, dividers, and right-aligned plus marks.
- Reveal each answer inline when its row is opened, using a minus mark and expanded spacing matching the fully opened Figma state.
- Remove the misaligned plus-ring animation from the FAQ block.
- Keep the existing section navigation anchor and page structure intact.
- Preserve the surrounding PNG-backed page design outside the FAQ section.

## Capabilities

### New Capabilities

- `figma-matched-faq-section`: Covers the rebuilt FAQ accordion layout, collapsed and expanded states, visible answers, right-side marks, and interaction behavior matching the provided Figma reference.

### Modified Capabilities

- `button-hit-zone-motion`: FAQ requirements change from animated plus hotspots and a floating answer panel to a Figma-matched accordion with stable click/focus areas.

## Impact

- Affected files: `index.html`, `styles.css`, `script.js`, `tests/test_button_interactions.py`, and OpenSpec artifacts.
- No backend, external API, dependency, domain, or deployment changes are required.
- The result should make the FAQ block visually clear, aligned, and closer to the supplied Figma design.
