# Caldaia Smart Integration

Questa integrazione permette di raggruppare i sensori di una caldaia (ad esempio, temperatura ACS, ACF, mandata, ritorno, fumi e consumo elettrico) sotto un unico dispositivo logico in Home Assistant. Inoltre, include un'entità di stato che indica lo stato attuale della caldaia (Standby, ACS, Circolatore, Riscaldamento) basandosi sul consumo elettrico.

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
- **Riscaldamento**: La caldaia è in modalità Riscaldamento quando il consumo supera **85W**.

### Come Scegliere i Valori delle Soglie
I valori di default sono stati impostati in base ai seguenti consumi tipici:
- **Standby**: 13,10W → Impostato a **20W** per maggiore sicurezza.
- **ACS**: 53,80W → Impostato a **60W** per maggiore sicurezza.
- **Circolatore**: 78,20W → Impostato a **85W** per maggiore sicurezza.
- **Riscaldamento**: 121,90W → Impostato a **130W** per maggiore sicurezza.

Se i consumi della tua caldaia sono diversi, puoi regolare le soglie nella configurazione dell'integrazione.

## Changelog
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

## Supporto
Per problemi o richieste, apri un'issue su GitHub.
