# Dogport Figma Rework Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Match the updated Dog Port Fest Figma/page assets while keeping menu, FAQ, dog carousel, partner/brand links, and contact links clickable.

**Architecture:** The site remains a static artboard: one full-page base image plus live absolutely positioned DOM layers for interactions. New dogs and brands are represented as data arrays in `script.js`, with rendered DOM elements for scalable carousel/card behavior.

**Tech Stack:** Static HTML/CSS/JS, PNG assets, Playwright/Pytest interaction tests.

---

### Task 1: Asset Import And Test Expectations

**Files:**
- Modify: `tests/test_button_interactions.py`
- Add assets under: `assets/images/figma-2026/`

- [ ] Update tests to expect 9556px artboard height, 12 dog carousel buttons, six brand buttons, and five contact links.
- [ ] Copy the provided PNG assets into repo-local folders with stable ASCII-friendly filenames.
- [ ] Run `python -m pytest tests/test_button_interactions.py -q` and confirm the new expectations fail against current implementation.

### Task 2: Live Dog Carousel

**Files:**
- Modify: `index.html`
- Modify: `styles.css`
- Modify: `script.js`
- Modify: `tests/test_button_interactions.py`

- [ ] Replace four static dog hotspots with a `.dog-carousel` live layer that renders 12 frame buttons.
- [ ] Implement next/prev buttons that update carousel index and apply animated track transforms.
- [ ] Make each dog frame open its matching large dog info PNG in the existing modal.
- [ ] Verify carousel buttons remain clickable above the full-page image.

### Task 3: Partner Events, Portrait, Brands

**Files:**
- Modify: `index.html`
- Modify: `styles.css`
- Modify: `script.js`
- Modify: `tests/test_button_interactions.py`

- [ ] Add live image layers for the three event photos and instant portrait block if the base image does not already contain them.
- [ ] Update brand data to six brands with imported card PNGs and the requested hrefs.
- [ ] Reuse the existing logo hover overlay animation for all old and new brand buttons.
- [ ] Verify brand card modal and brand-link behavior for all six brands.

### Task 4: DJ/FAQ/Contacts Repositioning

**Files:**
- Modify: `index.html`
- Modify: `styles.css`
- Modify: `script.js`
- Modify: `tests/test_button_interactions.py`

- [ ] Reposition anchors and live FAQ section to match the new order: shelter, DJs, FAQ, contacts.
- [ ] Preserve FAQ accordion behavior and focus states.
- [ ] Add fifth contact hotspot linking to `https://t.me/anastasia_sabanina`.
- [ ] Verify all navigation and contact hotspots remain clickable.

### Task 5: Browser QA

**Files:**
- Modify as needed from QA findings.

- [ ] Run the local site with `python3 -m http.server 8092`.
- [ ] Run the Playwright/Pytest suite.
- [ ] Open the page in the in-app browser and verify desktop/mobile screenshots for non-overlap, live carousel interaction, FAQ accordion, and modal behavior.
