# Dog Port Figma Rework Design

## Goal

Update the Dog Port Fest static site to match the newer Figma/page assets while preserving all useful interactive behavior. The full-page artwork is a visual layer only; menu items, FAQ, dog cards, carousel arrows, brand/partner links, contact links, and modal dialogs remain live DOM elements above it.

## Approach

- Use `/Users/max/Downloads/сайт 2.png` as the new page base image and update artboard height from `8576` to `9556`.
- Keep existing header/menu/dream sections visually intact by preserving the visible artwork and maintaining overlay hotspots.
- Replace the current four-dog clickable area with a live carousel of 12 dog frame images from `/Users/max/Downloads/Рамки собак`. Each frame opens its matching large info card from `/Users/max/Downloads/Собачки`.
- Add event photos and instant portrait assets before the local brand market while preserving partner-logo hover animation behavior.
- Update the local brand market to six brands with six info cards and links: Petvkus, Собака Мама, Собакин, Shaggy Dog, Держись меня, Hug Me Dog.
- Move the DJ block before FAQ according to the new page order. FAQ remains a live accordion, not a flattened image.
- Add the fifth contact link for all questions: `https://t.me/anastasia_sabanina`.

## Interaction Guarantees

- The full background image must not block clicks. All hotspots and live sections stay above it via positioning/z-index.
- Existing button/logo animation classes are reused for old and new buttons.
- New carousel motion respects `prefers-reduced-motion`.
- New data arrays are append-friendly so eight future dogs can be added by extending data, not rewriting behavior.
