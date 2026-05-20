## ADDED Requirements

### Requirement: GitHub repository publication
The project SHALL be pushed to a GitHub repository under the `maxunris` account when credentials are available.

#### Scenario: Repository does not exist
- **WHEN** publication runs
- **THEN** a repository is created under `maxunris`
- **AND** local `origin` points to that repository
- **AND** branch `main` is pushed

#### Scenario: Repository already exists
- **WHEN** publication runs and the repository exists
- **THEN** local `origin` points to the existing repository
- **AND** branch `main` is pushed
