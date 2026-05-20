## ADDED Requirements

### Requirement: Pixel-oriented section layout
Сайт SHALL предоставлять вертикальную структуру секций, визуально соответствующую Figma-композиции (hero, инфо, карточки, призы, партнеры, FAQ, CTA).

#### Scenario: Initial page render
- **WHEN** пользователь открывает страницу
- **THEN** отображается полный лендинг со всеми секциями в корректном порядке
- **AND** используется единая визуальная тема (зеленые/белые/оранжевые акценты, скругленные карточки)

### Requirement: Responsive behavior
Сайт SHALL корректно адаптироваться под mobile/tablet/desktop брейкпоинты.

#### Scenario: Mobile viewport
- **WHEN** ширина viewport <= 767px
- **THEN** контент отображается в 1 колонку
- **AND** интерактивные элементы доступны без горизонтального скролла

#### Scenario: Tablet/Desktop viewport
- **WHEN** ширина viewport >= 768px
- **THEN** карточки и списки переходят в многоколоночный режим
- **AND** основной контейнер центрируется

### Requirement: Interactive states
Сайт SHALL поддерживать состояния hover/focus/active/disabled для кликабельных элементов.

#### Scenario: FAQ interaction
- **WHEN** пользователь нажимает на вопрос
- **THEN** соответствующий ответ раскрывается/скрывается
- **AND** `aria-expanded` переключается между `true` и `false`

### Requirement: Asset gap reporting
Проект SHALL содержать явный список недостающих исходников при ограниченном доступе к Figma-ассетам.

#### Scenario: Delivery review
- **WHEN** разработчик передает реализацию
- **THEN** в документации присутствует перечень недостающих файлов и мест использования
