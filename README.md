# Caldaia Smart

Integrazione per Home Assistant che monitora lo stato della caldaia basandosi sul consumo elettrico.

## Installazione

1. Aggiungi questa repository a HACS.
2. Installa l'integrazione "Caldaia Smart".
3. Configura l'integrazione tramite il file `configuration.yaml`.

## Configurazione YAML

Aggiungi la seguente configurazione al tuo file `configuration.yaml`:

```yaml
caldaia_smart:
  power_sensor: sensor.potenza_caldaia  # Sostituisci con il tuo sensore di potenza
  standby_threshold: 20                 # Soglia per lo stato Standby (W)
  acs_threshold: 60                     # Soglia per lo stato ACS (W)
  circolatore_threshold: 100            # Soglia per lo stato Circolatore (W)
  riscaldamento_threshold: 140          # Soglia per lo stato Riscaldamento (W)