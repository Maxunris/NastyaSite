## ADDED Requirements

### Requirement: Precise hotspot geometry
The site SHALL size each transparent hotspot to the visible text, card, icon, row, or button it controls, without broad hover rectangles covering unrelated artwork.

#### Scenario: Text link hotspots align to text
- **WHEN** a user hovers or focuses a top navigation, hero menu, or footer contact link
- **THEN** the animated feedback SHALL stay within the visible text/link bounds
- **AND** the clickable hotspot SHALL NOT extend across unrelated whitespace or neighboring text

#### Scenario: Control hotspots align to controls
- **WHEN** a user hovers or focuses a dog card, carousel arrow, activity button, partner area, market area, shelter button, FAQ row, or modal close button
- **THEN** the animated feedback SHALL match the visible control shape
- **AND** the animated feedback SHALL NOT obscure nearby content outside that control

### Requirement: Harmonized button motion
All interactive controls SHALL use a consistent motion system that communicates hover, focus, active press, selection, and dialog state without abrupt jumps.

#### Scenario: User hovers any hotspot
- **WHEN** a pointer hovers over any hotspot
- **THEN** the control SHALL show a smooth, fitted hover affordance within 260ms
- **AND** transform changes SHALL be subtle enough that the hotspot remains visually attached to the visible target

#### Scenario: User presses any clickable control
- **WHEN** a user activates a hotspot or modal close button
- **THEN** the active state SHALL use a consistent press motion
- **AND** the control SHALL return smoothly after activation

#### Scenario: User opens and closes a dialog
- **WHEN** a dog or info dialog opens and then closes
- **THEN** both the dialog panel and backdrop SHALL animate in and out smoothly

### Requirement: Full interaction QA
The repository SHALL include an automated browser QA command that verifies every button and hotspot in desktop and mobile contexts.

#### Scenario: QA exercises every interactive target
- **WHEN** the interaction QA command runs
- **THEN** it SHALL hover, focus, and click every hotspot/button on the page
- **AND** it SHALL verify expected navigation, modal, carousel, FAQ, focus, and console outcomes

#### Scenario: QA checks hotspot geometry
- **WHEN** the interaction QA command inspects hotspot geometry
- **THEN** text-link hotspots SHALL be checked against tight text-aligned bounds
- **AND** non-text controls SHALL be checked against fitted visible-control bounds
