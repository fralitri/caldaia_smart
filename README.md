# Caldaia Smart Integration

Questa integrazione permette di raggruppare i sensori di una caldaia (ad esempio, temperatura ACS, ACF, mandata, ritorno, fumi e consumo elettrico) sotto un unico dispositivo logico in Home Assistant. Inoltre, include un'entità di stato che indica lo stato attuale della caldaia (Standby, ACS, Circolatore, Riscaldamento, Massima Potenza) basandosi sul consumo elettrico.

## Installazione tramite HACS
1. Aggiungi questo repository a HACS:
   - Vai su **HACS > Integrations > Explore & Add Repositories**.
   - Cerca `fralitri/caldaia_smart` e aggiungilo.
2. Installa l'integrazione "Caldaia Smart".
3. Configura l'integrazione tramite l'interfaccia grafica di Home Assistant.

## Configurazione
- Assegna un nome identificativo alla caldaia.
- Seleziona le entità corrispondenti (ad esempio, i sensori Shelly).
- Configura le soglie di consumo per determinare lo stato della caldaia.

## Soglie di Consumo
Lo stato della caldaia viene determinato in base al consumo elettrico. Ecco come impostare le soglie:

- **Standby**: La caldaia è in standby quando il consumo è inferiore a **20W**.
- **ACS**: La caldaia è in modalità ACS (acqua calda sanitaria) quando il consumo è compreso tra **20W** e **60W**.
- **Circolatore**: La caldaia è in modalità Circolatore quando il consumo è compreso tra **60W** e **85W**.
- **Riscaldamento**: La caldaia è in modalità Riscaldamento quando il consumo è compreso tra **85W** e **130W**.
- **Massima Potenza**: La caldaia è in modalità Massima Potenza quando il consumo supera **130W**.

### Icone degli Stati
- **Standby**: `mdi:power-standby`
- **ACS**: `mdi:water-pump`
- **Circolatore**: `mdi:pump`
- **Riscaldamento**: `mdi:radiator`
- **Massima Potenza**: `mdi:alert`

### Aggiornamenti in Tempo Reale
L'entità **Stato Caldaia** è ora più reattiva grazie a un listener che aggiorna lo stato ogni volta che il valore del sensore di consumo elettrico cambia.

## Changelog
### [1.0.8] - 2023-10-31
### Added
- Aggiunto un listener per aggiornamenti in tempo reale dello stato della caldaia.
- Migliorata la reattività dell'entità Stato Caldaia.

### Changed
- Cambiate le icone per gli stati:
  - Standby: `mdi:power-standby`
  - ACS: `mdi:water-pump`
  - Circolatore: `mdi:pump`

### [1.0.7] - 2023-10-30
### Fixed
- Corretto errore nel file `manifest.json` che impediva il caricamento dell'integrazione.

### [1.0.6] - 2023-10-30
### Fixed
- Correzione della logica di determinazione dello stato Riscaldamento.
- Aggiunto uno stato "Massima Potenza" per consumi superiori alla soglia Riscaldamento.

### [1.0.5] - 2023-10-25
### Improved
- Migliorate le descrizioni dei campi di configurazione delle soglie di consumo.

### [1.0.4] - 2023-10-25
### Added
- Aggiunta un'entità di stato per la caldaia, con icone dinamiche e stati personalizzati.
- Configurazione delle soglie di consumo per determinare lo stato della caldaia.

### [1.0.3] - 2023-10-25
### Fixed
- Corrette le descrizioni dei campi nel form di configurazione.

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

## Supporto
Per problemi o richieste, apri un'issue su GitHub.
