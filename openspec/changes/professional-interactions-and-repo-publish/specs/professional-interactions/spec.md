## ADDED Requirements

### Requirement: Accurate hotspot feedback
Interactive hover and focus feedback SHALL stay visually aligned with the visible Figma control it belongs to.

#### Scenario: User hovers a top navigation link
- **WHEN** the pointer is over a top navigation link
- **THEN** the feedback is a small underline/press cue
- **AND** it does not render a large filled rectangle over neighboring text

### Requirement: Dog carousel interaction
The dog-card block SHALL support both direct dog-card selection and previous/next arrow cycling.

#### Scenario: User clicks a dog card
- **WHEN** the user clicks Клепа, Белка, Толик, or Персей
- **THEN** the matching detailed exported card opens

#### Scenario: User clicks carousel arrows
- **WHEN** the user clicks previous or next
- **THEN** the active dog changes
- **AND** the active dog card receives a subtle card-shaped selected state

### Requirement: Inline FAQ expansion
FAQ plus controls SHALL expand their answer inline on the page.

#### Scenario: User clicks an FAQ row
- **WHEN** the user clicks a FAQ plus or row
- **THEN** the corresponding answer appears below the row
- **AND** clicking it again collapses the answer

### Requirement: QA verification
The implementation SHALL be tested in desktop and mobile viewports.

#### Scenario: QA pass
- **WHEN** tests run in the browser
- **THEN** the console has no errors
- **AND** there is no horizontal scroll on mobile
- **AND** dog and FAQ interactions work
