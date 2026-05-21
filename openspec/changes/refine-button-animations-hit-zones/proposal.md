## Why

The current PNG-backed page has useful interactions, but several transparent hotspots are broader or taller than the visible text/control they represent, and button motion feels uneven across sections. This change makes the interactive layer feel intentional: hover/focus feedback should land exactly on the visible target and use one coherent motion language.

## What Changes

- Tighten navigation, menu, FAQ, contact, and button hotspot geometry so interactive zones align with the visible text or visible control shape in the Figma export.
- Replace mixed hover/active transforms with a consistent, modern interaction system for text links, pill buttons, card buttons, circular arrows, FAQ rows, and modal close buttons.
- Add exit motion for dialogs so opening and closing feel symmetric instead of abrupt.
- Add automated QA coverage that exercises every hotspot/button, verifies geometry classes, hover/focus/active affordances, click behavior, and console health.
- Preserve the PNG-backed visual design and existing public HTML structure.

## Capabilities

### New Capabilities

- `button-hit-zone-motion`: Covers precise hotspot alignment, button animation consistency, modal motion, and full-button QA expectations for the static festival page.

### Modified Capabilities

- `professional-interactions`: Tightens the existing interaction requirements from broad functional hotspots to visually precise text/control-aligned hover and focus zones.

## Impact

- Affected files: `styles.css`, `script.js`, automated QA scripts/tests, and OpenSpec artifacts.
- No backend, API, dependency, or content changes are expected.
- The user-facing result is smoother button feedback and more accurate clickable/animated areas across desktop and mobile.
