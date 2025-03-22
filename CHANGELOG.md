# Changelog

## [1.0.8] - 2023-10-31
### Added
- Aggiunto un listener per aggiornamenti in tempo reale dello stato della caldaia.
- Migliorata la reattività dell'entità Stato Caldaia.
### Changed
- Cambiate le icone per gli stati:
  - Standby: `mdi:power-standby`
  - ACS: `mdi:water-pump`
  - Circolatore: `mdi:pump`

## [1.0.7] - 2023-10-30
### Fixed
- Corretto errore di sintassi nel file `__init__.py` che impediva il caricamento dell'integrazione.
- Aggiunte le importazioni mancanti per `HomeAssistant`, `ConfigType`, e `config_entries`.
- Integrata correttamente l'entità **Stato Caldaia** nel file `__init__.py`.

### [1.0.6] - 2023-10-30
### Fixed
- Correzione della logica di determinazione dello stato Riscaldamento: ora la caldaia è in Riscaldamento solo quando il consumo è compreso tra la soglia Circolatore e la soglia Riscaldamento.
- Aggiunto uno stato "Massima Potenza" per consumi superiori alla soglia Riscaldamento.
- Migliorate le descrizioni delle soglie nei file di traduzione e nel README.md.

### [1.0.5] - 2023-10-25
### Improved
- Migliorate le descrizioni dei campi di configurazione delle soglie di consumo per renderle più chiare e user-friendly.
- Aggiunte descrizioni dettagliate nel README.md per la configurazione delle soglie.

### [1.0.4] - 2023-10-25
### Added
- Aggiunta un'entità di stato per la caldaia, con icone dinamiche e stati personalizzati:
  - Standby
  - ACS
  - Circolatore
  - Riscaldamento
- Configurazione delle soglie di consumo per determinare lo stato della caldaia.

### [1.0.3] - 2023-10-25
### Fixed
- Corrette le descrizioni dei campi nel form di configurazione:
  - Temperatura Acqua Calda Sanitaria
  - Temperatura Acqua Fredda Sanitaria
  - Temperatura Mandata Riscaldamento
  - Temperatura Ritorno Riscaldamento
  - Temperatura Fumi Caldaia
  - Consumo Elettrico Caldaia

### [1.0.2] - 2023-10-25
### Added
- Aggiunte traduzioni in italiano per i testi dell'interfaccia utente.
- Migliorate le descrizioni user-friendly nei campi del form di configurazione.

### [1.0.1] - 2023-10-25
### Fixed
- Corretto il bug che impediva il caricamento del Config Flow.
- Aggiunte descrizioni user-friendly e menu a discesa per la selezione delle entità.

### [1.0.0] - 2023-10-20
### Added
- Prima versione dell'integrazione.
