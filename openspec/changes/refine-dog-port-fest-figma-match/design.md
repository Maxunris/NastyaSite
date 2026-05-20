## Overview

The site should render the latest complete Figma page export as the visible source of truth. Interactive behavior is layered on top with transparent, responsive hotspots aligned to the exported `1440x7859` artboard.

## Asset Roles

- `site-full.png`: final visible page, exported at `1440x7859`; this is the 1:1 visual layer.
- `design-map.png`: wide Figma-canvas reference, exported at `7277x7859`; this explains where expanded dog cards and future partner/program states live.
- `dog-belka.png`, `dog-tolik.png`, `dog-klepa.png`, `dog-persey.png`: expanded dog-card states shown when the matching dog is selected.
- `1 экран.png` through `10 экран.png`: section-level exports for QA and future reconstruction if the site later needs to become fully native HTML rather than PNG-backed.
- `Group 89`, `Group 93`, `Group 94`, `Layer_1`, `+клепа 2`, `курсоры`: decorative/reference fragments from the Figma export set.

## Interaction

Clicking a dog card in the “20 собак из приюта” row opens the matching expanded card. The click target must cover the dog card itself, not an unrelated button elsewhere.

## Local Verification

Use a port other than `8080`; default verification port for this change is `8091`.
