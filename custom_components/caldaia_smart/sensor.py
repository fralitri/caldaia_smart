from homeassistant.helpers.entity import Entity
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.event import async_track_state_change
from homeassistant.core import callback
from homeassistant.components.sensor import SensorEntity
from homeassistant.util import dt as dt_util
from datetime import timedelta
import logging
from .const import (
    DOMAIN, CONF_NAME, CONF_CONSUMO_ELETTRICO,
    CONF_STANDBY_THRESHOLD, CONF_ACS_THRESHOLD, 
    CONF_CIRCOLATORE_THRESHOLD, CONF_RISCALDAMENTO_THRESHOLD,
    STATO_STANDBY, STATO_ACS, STATO_CIRCOLATORE, STATO_RISCALDAMENTO,
    DEFAULT_STANDBY_THRESHOLD, DEFAULT_ACS_THRESHOLD,
    DEFAULT_CIRCOLATORE_THRESHOLD, DEFAULT_RISCALDAMENTO_THRESHOLD
)

_LOGGER = logging.getLogger(__name__)

class CaldaiaSmartStatoSensor(Entity):
    """Sensor per lo stato della caldaia."""
    # ... (mantieni l'implementazione esistente)

class ACSDurationSensor(SensorEntity):
    """Sensor per il tempo trascorso in modalità ACS."""
    
    def __init__(self, hass, config_entry, stato_sensor):
        """Initialize the sensor."""
        self._hass = hass
        self._config_entry = config_entry
        self._stato_sensor = stato_sensor
        self._state = 0
        self._attr_name = f"{config_entry.data[CONF_NAME]} Tempo ACS"
        self._attr_unique_id = f"{config_entry.entry_id}_acs_time"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, config_entry.entry_id)}
        )
        self._attr_unit_of_measurement = "h"
        self._attr_should_poll = True
        
    async def async_update(self):
        """Calculate time in ACS state."""
        try:
            _LOGGER.debug("Aggiornamento sensore tempo ACS in corso...")
            
            now = dt_util.now()
            today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            
            _LOGGER.debug(f"Periodo analizzato: da {today_start} a {now}")
            
            history_list = await self._get_history(today_start, now)
            
            if not history_list:
                _LOGGER.debug("Nessun dato storico trovato")
                self._state = 0
                return
            
            acs_time = timedelta()
            prev_state = None
            prev_time = today_start
            
            _LOGGER.debug(f"Trovati {len(history_list)} eventi storici")
            
            for item in history_list:
                state = item.state
                time = dt_util.parse_datetime(item.last_updated)
                
                if prev_state == STATO_ACS:
                    time_diff = time - prev_time
                    acs_time += time_diff
                    _LOGGER.debug(f"Periodo ACS: {prev_time} - {time} = {time_diff}")
                
                prev_state = state
                prev_time = time
            
            # Aggiungi il tempo dall'ultimo cambiamento di stato
            if prev_state == STATO_ACS:
                last_diff = now - prev_time
                acs_time += last_diff
                _LOGGER.debug(f"Ultimo periodo ACS: {prev_time} - {now} = {last_diff}")
            
            total_hours = round(acs_time.total_seconds() / 3600, 2)
            _LOGGER.debug(f"Tempo totale ACS: {total_hours} ore")
            
            self._state = total_hours
            
        except Exception as e:
            _LOGGER.error(f"Errore durante il calcolo del tempo ACS: {str(e)}")
            self._state = 0

    async def _get_history(self, start_time, end_time):
        """Get history from recorder."""
        from homeassistant.components.recorder import history
        
        _LOGGER.debug(f"Recupero history per {self._stato_sensor.entity_id}")
        
        return await self._hass.async_add_executor_job(
            history.state_changes_during_period,
            self._hass,
            start_time,
            end_time,
            str(self._stato_sensor.entity_id),
            include_start_time_state=True,
            no_attributes=True
        )

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the sensors."""
    # ... (mantieni l'implementazione esistente)
