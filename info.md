### Caldaia Smart Integration

Raggruppa i sensori di una caldaia sotto un unico dispositivo logico in Home Assistant.

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
- **1.0.8**: Aggiunto listener per aggiornamenti in tempo reale. Cambiate le icone per gli stati.
- **1.0.7**: Correzione del file `manifest.json` e miglioramenti alla configurazione.
- **1.0.6**: Correzione della logica di determinazione dello stato Riscaldamento.
- **1.0.5**: Migliorate le descrizioni dei campi di configurazione.
- **1.0.4**: Aggiunta entità di stato e configurazione delle soglie di consumo.
- **1.0.3**: Corrette le descrizioni dei campi nel form di configurazione.
- **1.0.2**: Aggiunte traduzioni in italiano e migliorate le descrizioni.
- **1.0.1**: Corretto bug e aggiunte descrizioni user-friendly.
- **1.0.0**: Prima versione.
