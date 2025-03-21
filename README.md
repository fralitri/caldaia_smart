# Caldaia Smart Integration

Questa integrazione permette di raggruppare i sensori di una caldaia (ad esempio, temperatura ACS, ACF, mandata, ritorno, fumi e consumo elettrico) sotto un unico dispositivo logico in Home Assistant.

## Installazione tramite HACS
1. Aggiungi questo repository a HACS:
   - Vai su **HACS > Integrations > Explore & Add Repositories**.
   - Cerca `fralitri/caldaia_smart` e aggiungilo.
2. Installa l'integrazione "Caldaia Smart".
3. Configura l'integrazione tramite l'interfaccia grafica di Home Assistant.

## Configurazione
- Assegna un nome identificativo alla caldaia.
- Seleziona le entità corrispondenti (ad esempio, i sensori Shelly).

## Changelog
### [1.0.1] - 2023-10-25
- **Fixed**: Corretto il bug che impediva il caricamento del Config Flow.
- **Improved**: Aggiunte descrizioni user-friendly e menu a discesa per la selezione delle entità.

### [1.0.0] - 2023-10-20
- **Added**: Prima versione dell'integrazione.

## Supporto
Per problemi o richieste, apri un'issue su GitHub.
