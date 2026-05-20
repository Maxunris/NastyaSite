## Why

The current implementation needs to be validated against the latest exported Figma assets and adjusted so the dog cards behave like the design state: each dog in the card row reveals its matching detailed card.

## What Changes

- Replace the previously referenced full-page export with the latest `Дог порт фест (2)` full-page PNG.
- Import and organize all latest section, dog-card, and design-map images.
- Reposition clickable dog hotspots so the click target is the dog/card itself.
- Preserve the 1:1 visual rendering of the main page by keeping the full exported artboard as the visible layer.
- Open the correct expanded dog card when a user clicks Клепа, Белка, Толик, or Персей.
- Update documentation and local verification instructions to use a port other than `8080`.

## Capabilities

### New Capabilities
- `dog-card-expansion`: Clickable dog cards reveal the corresponding exported detailed card while preserving the Figma-matched main artboard.

### Modified Capabilities
- None.

## Impact

- Affected code: `index.html`, `styles.css`, `script.js`, `README.md`.
- Affected assets: `assets/images/figma-final/*`.
- APIs: none.
- Dependencies: none.
