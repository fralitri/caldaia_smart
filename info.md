### Caldaia Smart Integration

Raggruppa i sensori di una caldaia sotto un unico dispositivo logico in Home Assistant.

**Compatibilità:**
- Home Assistant 2025.3.4 o superiore.

**Funzionalità:**
- Configurazione guidata tramite UI.
- Supporto per più caldaie.
- Nessuna modifica manuale del codice richiesta.
- Menu a discesa per la selezione delle entità con nomi user-friendly.
- Entità di stato con icone dinamiche e stati personalizzati:
  - **Standby**: `mdi:power-standby`
  - **ACS**: `mdi:water-pump`
  - **Circolatore**: `mdi:pump`
  - **Riscaldamento**: `mdi:radiator`
- Aggiornamenti in tempo reale dello stato della caldaia tramite listener.

**Installazione:**
- Disponibile tramite HACS.

**Soglie di Consumo:**
Lo stato della caldaia viene determinato in base al consumo elettrico. Ecco come impostare le soglie:
- **Standby**: La caldaia è in standby quando il consumo è inferiore a **20W**.
- **ACS**: La caldaia è in modalità ACS (acqua calda sanitaria) quando il consumo è compreso tra **20W** e **60W**.
- **Circolatore**: La caldaia è in modalità Circolatore quando il consumo è compreso tra **60W** e **85W**.
- **Riscaldamento**: La caldaia è in modalità Riscaldamento quando il consumo è compreso tra **85W** e **130W**.
- **Massima Potenza**: La caldaia è in modalità Massima Potenza quando il consumo supera **130W**.

**Changelog:**
- **1.0.9 (2025-03-22)**: Aggiunta la possibilità di modificare tutti i campi (nome del dispositivo, sensori e soglie) durante la configurazione avanzata.
- **1.0.8 (2025-03-22)**: Aggiunto listener per aggiornamenti in tempo reale. Cambiate le icone per gli stati.
- **1.0.7 (2025-03-21)**: Corretto errore nel file `manifest.json`.
- **1.0.6 (2025-03-20)**: Correzione della logica di determinazione dello stato Riscaldamento.
- **1.0.5 (2025-03-19)**: Migliorate le descrizioni dei campi di configurazione.
- **1.0.4 (2025-03-18)**: Aggiunta entità di stato e configurazione delle soglie di consumo.
- **1.0.3 (2025-03-17)**: Corrette le descrizioni dei campi nel form di configurazione.
- **1.0.2 (2025-03-16)**: Aggiunte traduzioni in italiano e migliorate le descrizioni.
- **1.0.1 (2025-03-15)**: Corretto bug e aggiunte descrizioni user-friendly.
- **1.0.0 (2025-03-14)**: Prima versione.
