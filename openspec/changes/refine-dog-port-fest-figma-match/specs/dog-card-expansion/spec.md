## ADDED Requirements

### Requirement: Latest Figma export rendering
The page SHALL render the latest complete Figma export from `Дог порт фест (2)` as the primary visible artboard.

#### Scenario: Page loads
- **WHEN** the user opens the site
- **THEN** the visible page is based on the latest `1440x7859` full-page export
- **AND** there are no browser-default margins or image baseline gaps

### Requirement: Dog-card expansion
The page SHALL reveal the correct detailed dog card when a user clicks the matching dog card in the dog section.

#### Scenario: User clicks Белка
- **WHEN** the user clicks the Белка card in the dog row
- **THEN** the Белка detail image opens

#### Scenario: User clicks Толик
- **WHEN** the user clicks the Толик card in the dog row
- **THEN** the Толик detail image opens

#### Scenario: User clicks Клепа
- **WHEN** the user clicks the Клепа card in the dog row
- **THEN** the Клепа detail image opens

#### Scenario: User clicks Персей
- **WHEN** the user clicks the Персей card in the dog row
- **THEN** the Персей detail image opens

### Requirement: Non-8080 local preview
The project documentation SHALL use a local preview port other than `8080`.

#### Scenario: Developer starts preview
- **WHEN** the developer follows the README
- **THEN** the preview command uses port `8091`
