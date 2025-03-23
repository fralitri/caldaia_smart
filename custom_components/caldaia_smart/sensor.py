from homeassistant.components.history_stats.sensor import HistoryStatsSensor
from homeassistant.const import CONF_NAME

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Caldaia Smart sensors."""
    # Aggiungi il sensore di stato della caldaia
    stato_sensor = CaldaiaSmartStatoSensor(
        hass,
        config_entry.data[CONF_CONSUMO_ELETTRICO],
        config_entry.data.get(CONF_STANDBY_THRESHOLD, DEFAULT_STANDBY_THRESHOLD),
        config_entry.data.get(CONF_ACS_THRESHOLD, DEFAULT_ACS_THRESHOLD),
        config_entry.data.get(CONF_CIRCOLATORE_THRESHOLD, DEFAULT_CIRCOLATORE_THRESHOLD),
        config_entry.data.get(CONF_RISCALDAMENTO_THRESHOLD, DEFAULT_RISCALDAMENTO_THRESHOLD),
        config_entry.entry_id
    )
    async_add_entities([stato_sensor])

    # Crea il sensore di tempo di attività ACS
    acs_time_sensor = HistoryStatsSensor(
        hass,
        name=f"{config_entry.data[CONF_NAME]} Tempo ACS Ultime 24 Ore",  # Nome personalizzato
        entity_id="sensor.stato_caldaia",  # ID dell'entità Stato Caldaia
        state="ACS",  # Stato da monitorare
        type="time",  # Tipo di statistica (tempo)
        start="{{ now().replace(hour=0, minute=0, second=0) }}",  # Inizio dell'intervallo
        end="{{ now() }}",  # Fine dell'intervallo
        duration={"hours": 24}  # Durata dell'intervallo (24 ore)
    )
    async_add_entities([acs_time_sensor])
