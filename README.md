# Caldaia Smart Integration

Questa integrazione permette di raggruppare i sensori di una caldaia (ad esempio, temperatura ACS, ACF, mandata, ritorno, fumi e consumo elettrico) sotto un unico dispositivo logico in Home Assistant. Inoltre, include un'entità di stato che indica lo stato attuale della caldaia (Standby, ACS, Circolatore, Riscaldamento, Massima Potenza) basandosi sul consumo elettrico.

**Compatibilità:**
- Home Assistant 2025.3.4 o superiore.

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
### [1.0.9] - 2025-03-22
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
- Migliorate
