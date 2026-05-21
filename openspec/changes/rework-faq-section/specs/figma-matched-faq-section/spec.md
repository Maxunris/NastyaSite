## ADDED Requirements

### Requirement: FAQ renders as a Figma-matched accordion
The site SHALL render the FAQ section as a real accordion overlay matching the provided Figma collapsed and expanded references.

#### Scenario: Collapsed FAQ rows
- **WHEN** the FAQ section first renders
- **THEN** all six questions are visible as compact rows with thin dividers and right-aligned plus marks

#### Scenario: Expanded FAQ row
- **WHEN** a user opens a FAQ row
- **THEN** that row reveals its answer inline below the question and changes the right-side mark from plus to minus

#### Scenario: Fully expanded FAQ
- **WHEN** a user opens every FAQ row
- **THEN** all answers are visible inline and the layout matches the fully expanded Figma reference with consistent spacing and dividers

### Requirement: FAQ interaction zones are aligned and accessible
The site SHALL keep FAQ click, hover, and focus areas aligned to each visible row without decorative animation offset from the plus or minus mark.

#### Scenario: Keyboard and pointer operation
- **WHEN** a user clicks or focuses a FAQ row button
- **THEN** the interactive area covers the visible row and exposes an accessible expanded/collapsed state

#### Scenario: Removed detached panel
- **WHEN** a FAQ row is opened
- **THEN** the answer appears inside that row and no separate floating FAQ answer panel is shown
