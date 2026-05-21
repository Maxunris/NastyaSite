## Context

The page is built from a large Figma PNG with absolute-position HTML controls over it. This approach works for simple hotspots, but the FAQ needs two visual states that are not both present in the PNG: a collapsed list with plus marks and an expanded inline-answer state with minus marks.

## Goals / Non-Goals

**Goals:**

- Replace the FAQ hotspot layer with a real accordion overlay that matches the supplied Figma collapsed and expanded references.
- Keep the FAQ block visually aligned with the Figma section: centered title, green flower asset, question typography, thin dividers, and right-aligned plus/minus marks.
- Allow each FAQ row to expand inline without using the old floating answer panel.
- Preserve section navigation and the rest of the PNG-backed page.

**Non-Goals:**

- Rebuilding the full page away from the PNG artboard.
- Changing FAQ content beyond matching the wording shown in the Figma reference.
- Changing hosting, domain, deployment, or other site sections.

## Decisions

1. Use a real positioned FAQ section overlay.

The FAQ will be rendered as semantic HTML inside the artboard and placed over the baked FAQ area. A white background on the overlay hides the old PNG FAQ artwork, while keeping the rest of the source image intact.

2. Use independent accordion rows.

Each row toggles its own expanded state. This lets one item open at a time or all items be opened to match the fully expanded Figma reference.

3. Draw plus/minus marks with CSS.

The marks will use pseudo-elements on a small fixed-size control area. This avoids the previous offset issue where a decorative ring was positioned relative to a wide transparent row.

4. Keep answers in the DOM.

Answers remain in each row and animate via height/opacity. This gives stable accessibility semantics and avoids a detached floating panel.

## Risks / Trade-offs

- The overlay must cover the baked PNG FAQ precisely enough that doubled text is not visible. -> Use a white FAQ section background and inspect it in browser.
- Expanding all rows increases visual height. -> Position the block inside the existing FAQ area, whose vertical space is large enough before the contacts anchor.
- Font metrics may not exactly match Figma. -> Use the same heavy, compact Arial styling already used by the page and verify visually.
