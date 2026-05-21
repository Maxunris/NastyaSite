## MODIFIED Requirements

### Requirement: Accurate hotspot feedback
Interactive hover and focus feedback SHALL stay visually aligned with the visible Figma control it belongs to, and text-link hotspots SHALL be sized to their visible text rather than to broad surrounding rows.

#### Scenario: User hovers a top navigation link
- **WHEN** the pointer is over a top navigation link
- **THEN** the feedback is a small underline/press cue
- **AND** it does not render a large filled rectangle over neighboring text
- **AND** the hoverable area stays fitted to the visible link text

#### Scenario: User hovers a hero menu link
- **WHEN** the pointer is over a central hero menu link
- **THEN** the feedback tracks the visible text or pill shape for that specific item
- **AND** the hoverable area does not span the full menu row beyond the visible label

#### Scenario: User hovers a footer contact link
- **WHEN** the pointer is over a footer contact link
- **THEN** the feedback appears as a fitted underline
- **AND** the hoverable area does not overlap neighboring contact labels

### Requirement: QA verification
The implementation SHALL be tested in desktop and mobile viewports, and the tests SHALL exercise every interactive hotspot and modal button.

#### Scenario: QA pass
- **WHEN** tests run in the browser
- **THEN** the console has no errors
- **AND** there is no horizontal scroll on mobile
- **AND** dog and FAQ interactions work
- **AND** every hotspot/button has verified hover feedback and click behavior
