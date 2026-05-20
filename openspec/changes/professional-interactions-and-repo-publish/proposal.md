## Why

The current PNG-backed site visually matches the Figma export, but the interactive layer is too coarse: hover areas do not match the visible controls, dog carousel arrows do not work, dog cards need reliable expansion, and FAQ plus controls should expand inline.

## What Changes

- Publish the project to a GitHub repository under the `maxunris` account.
- Replace broad hover rectangles with interaction states that visually fit the underlying Figma elements.
- Make the dog-card row behave like a carousel: arrows cycle the active dog and clicking a dog opens the matching detailed card.
- Add inline FAQ expansion when users click the plus controls.
- Re-test desktop and mobile viewports with Playwright, including hover/click target geometry and console errors.

## Capabilities

### New Capabilities
- `professional-interactions`: Accurate hotspot geometry, dog carousel behavior, inline FAQ expansion, and polished button/link motion over the Figma artboard.
- `repository-publish`: GitHub repository creation and push under the `maxunris` account.

### Modified Capabilities
- None.

## Impact

- Affected code: `index.html`, `styles.css`, `script.js`, `README.md`.
- Affected workflow: local git repository gains remote `origin` and is pushed to GitHub.
- Dependencies: none.
