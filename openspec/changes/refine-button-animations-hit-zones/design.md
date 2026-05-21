## Context

The site is a static, PNG-backed landing page: `site-full.png` is the visual source of truth and transparent HTML hotspots provide navigation, buttons, modals, carousel, and FAQ behavior. Because the visible text and buttons live in the image, interaction quality depends on carefully sized absolute-position overlays and pseudo-element feedback.

The current layer works functionally, but several hotspots are sized like broad rows instead of text/control bounds, and different button groups use different transform patterns. The requested refinement is visual and behavioral: every clickable area should feel attached to the visible text or control, and the motion should feel consistent across the page.

## Goals / Non-Goals

**Goals:**

- Align top nav, menu links, footer links, FAQ rows, pill buttons, dog cards, carousel arrows, activity cards, and modal close controls to their visible targets.
- Use one coherent motion system based on subtle lift, underline reveal, active press, focus ring, and dialog enter/exit transitions.
- Preserve the current exported PNG and content.
- Add automated browser QA that visits the local page and exercises every interactive hotspot/button at desktop and mobile widths.

**Non-Goals:**

- Rebuilding the page from semantic text instead of the Figma PNG.
- Changing festival copy, images, dog-card assets, or external links.
- Adding new dependencies unless the existing Python Playwright runtime is unavailable.

## Decisions

1. Keep the absolute hotspot architecture and refine coordinates in CSS.

The visible text is baked into the PNG, so replacing it with real DOM text would be a larger redesign and could break the Figma match. The safer path is to keep hotspots and shrink/reposition broad link zones to match the text/control they cover.

2. Split interaction styling by control type.

Text links get a precise underline/capsule cue; pill/card controls get a fitted outline and lift; circular arrow controls get a ring and scale; FAQ rows highlight only the plus/text row. This keeps animations modern without painting large rectangles over the artboard.

3. Add a small JavaScript dialog-close helper.

Native `<dialog>.close()` is abrupt. A helper class can animate out and then close on `animationend`, while keeping the existing click handlers and Escape/backdrop behavior intact.

4. Use browser QA as the contract for "each button".

The test will enumerate all anchors/buttons/dialog controls, verify hitbox expectations by class, hover each item and inspect pseudo-element state, click each item and verify its intended outcome, check focus visibility, and run desktop plus mobile viewport checks.

## Risks / Trade-offs

- **Risk:** Pixel-perfect matching is constrained by the source PNG and responsive scaling. → **Mitigation:** Use percentage geometry tied to the 1440px artboard and verify at two viewport widths.
- **Risk:** Very tight text-aligned zones can become hard to tap. → **Mitigation:** Match visible text/control bounds while preserving enough vertical height for the actual visible row/button; mobile QA checks minimum practical touch sizes for non-text controls.
- **Risk:** Pseudo-element animation can hide feedback if opacity/transform rules conflict. → **Mitigation:** Centralize animation tokens and test every hotspot's hover feedback.
- **Risk:** Dialog exit animation can race with repeated close actions. → **Mitigation:** Guard close helper against already-closing dialogs and keep immediate close available when animation is disabled.
