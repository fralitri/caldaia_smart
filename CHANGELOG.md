## [1.0.9] - 2025-03-22
### Added
- Aggiunta la possibilità di modificare tutti i campi (nome del dispositivo, sensori e soglie) durante la configurazione avanzata.

### [1.0.8] - 2025-03-22
### Added
- Aggiunto un listener per aggiornamenti in tempo reale dello stato della caldaia.
- Migliorata la reattività dell'entità Stato Caldaia.

### Changed
- Cambiate le icone per gli stati:
  - Standby: `mdi:power-standby`
  - ACS: `mdi:water-pump`
  - Circolatore: `mdi:pump`

### [1.0.7] - 2025-03-21
### Fixed
- Corretto errore nel file `manifest.json` che impediva il caricamento dell'integrazione.

### [1.0.6] - 2025-03-20
### Fixed
- Correzione della logica di determinazione dello stato Riscaldamento.
- Aggiunto uno stato "Massima Potenza" per consumi superiori alla soglia Riscaldamento.

### [1.0.5] - 2025-03-19
### Improved
- Migliorate le descrizioni dei campi di configurazione delle soglie di consumo.

### [1.0.4] - 2025-03-18
### Added
- Aggiunta un'entità di stato per la caldaia, con icone dinamiche e stati personalizzati.
- Configurazione delle soglie di consumo per determinare lo stato della caldaia.

### [1.0.3] - 2025-03-17
### Fixed
- Corrette le descrizioni dei campi nel form di configurazione.

### [1.0.2] - 2025-03-16
### Added
- Aggiunte traduzioni in italiano per i testi dell'interfaccia utente.
- Migliorate le descrizioni user-friendly nei campi del form di configurazione.

### [1.0.1] - 2025-03-15
### Fixed
- Corretto il bug che impediva il caricamento del Config Flow.
- Aggiunte descrizioni user-friendly e menu a discesa per la selezione delle entità.

### [1.0.0] - 2025-03-14
### Added
- Prima versione dell'integrazione.
