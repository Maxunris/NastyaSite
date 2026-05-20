## Overview

Keep the full Figma PNG as the visual source of truth, but treat the transparent interactive layer like production UI: target boxes must match the visible element, hover states must be subtle, and click behavior must be observable and useful.

## Interaction Model

- Top nav and hero menu links use small underline/press feedback instead of large filled rectangles.
- Dog cards use card-sized hit areas and a selected state that hugs the card shape.
- Carousel arrows cycle the selected dog and update an inline hint; clicking the selected dog opens its exported detail card.
- FAQ rows use inline expansion overlays, not generic info modals.
- Informational items that lack real URLs still open a small modal, but their hover treatment is minimal and shaped to the visible button/card.

## Testing

Use Playwright on port `8092` to verify:

- Main image loads at `1440x7859`.
- No horizontal scroll on mobile.
- All dog cards open the matching exported card.
- Previous/next arrows change the active dog.
- FAQ rows expand and collapse.
- Console stays clean.
- Hover/focus boxes remain within expected target bounds.
