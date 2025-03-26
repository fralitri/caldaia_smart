from homeassistant.helpers.entity import Entity
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.event import async_track_state_change
from homeassistant.core import callback
from homeassistant.components.sensor import SensorEntity
from homeassistant.util import dt as dt_util
from datetime import timedelta
from .const import (
    DOMAIN, CONF_NAME, CONF_CONSUMO_ELETTRICO,
    CONF_STANDBY_THRESHOLD, CONF_ACS_THRESHOLD, 
    CONF_CIRCOLATORE_THRESHOLD, CONF_RISCALDAMENTO_THRESHOLD,
    STATO_STANDBY, STATO_ACS, STATO_CIRCOLATORE, STATO_RISCALDAMENTO,
    DEFAULT_STANDBY_THRESHOLD, DEFAULT_ACS_THRESHOLD,
    DEFAULT_CIRCOLATORE_THRESHOLD, DEFAULT_RISCALDAMENTO_THRESHOLD
)

class CaldaiaSmartStatoSensor(Entity):
    """Sensor per lo stato della caldaia."""
    
    def __init__(self, hass, consumo_elettrico, standby_threshold, acs_threshold, 
                 circolatore_threshold, riscaldamento_threshold, device_id):
        """Initialize the sensor."""
        self.hass = hass
        self._entity_id = consumo_elettrico
        self._standby_threshold = standby_threshold
        self._acs_threshold = acs_threshold
        self._circolatore_threshold = circolatore_threshold
        self._riscaldamento_threshold = riscaldamento_threshold
        self._device_id = device_id
        self._state = None
        self._icon = "mdi:power-standby"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device_id)},
            name="Caldaia Smart",
            manufacturer="Caldaia Smart",
            model="Generic",
        )

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Stato Caldaia"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return self._icon

    async def async_added_to_hass(self):
        """Call when entity is added to hass."""
        @callback
        def async_state_changed_listener(entity_id, old_state, new_state):
            """Handle state changes."""
            self._update_state()
            self.async_write_ha_state()

        self.async_on_remove(
            async_track_state_change(
                self.hass, self._entity_id, async_state_changed_listener
            )
        )

    def _update_state(self):
        """Update the state of the sensor."""
        state = self.hass.states.get(self._entity_id)
        if state is None or state.state in (None, "unknown", "unavailable"):
            return

        try:
            consumo = float(state.state)
        except ValueError:
            return

        if consumo < self._standby_threshold:
            self._state = STATO_STANDBY
            self._icon = "mdi:power-standby"
        elif consumo < self._acs_threshold:
            self._state = STATO_ACS
            self._icon = "mdi:water-pump"
        elif consumo < self._circolatore_threshold:
            self._state = STATO_CIRCOLATORE
            self._icon = "mdi:pump"
        elif consumo < self._riscaldamento_threshold:
            self._state = STATO_RISCALDAMENTO
            self._icon = "mdi:radiator"
        else:
            self._state = "Massima Potenza"
            self._icon = "mdi:alert"

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
        
    async def async_update(self):
        """Calculate time in ACS state."""
        now = dt_util.now()
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        
        history_list = await self._hass.async_add_executor_job(
            self._get_history,
            today_start,
            now,
            self._stato_sensor.entity_id
        )
        
        acs_time = timedelta()
        prev_state = None
        prev_time = today_start
        
        for item in history_list:
            state = item.state
            time = dt_util.parse_datetime(item.last_updated)
            
            if prev_state == STATO_ACS:
                acs_time += time - prev_time
                
            prev_state = state
            prev_time = time
        
        # Aggiungi il tempo dall'ultimo cambiamento di stato
        if prev_state == STATO_ACS:
            acs_time += now - prev_time
            
        self._state = round(acs_time.total_seconds() / 3600, 2)

    def _get_history(self, start_time, end_time, entity_id):
        """Get history from recorder."""
        from homeassistant.components.recorder import history
        return history.state_changes_during_period(
            self._hass,
            start_time,
            end_time,
            entity_id,
            include_start_time_state=True
        )

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the sensors."""
    # Creazione del sensore stato
    stato_sensor = CaldaiaSmartStatoSensor(
        hass,
        config_entry.data[CONF_CONSUMO_ELETTRICO],
        config_entry.data.get(CONF_STANDBY_THRESHOLD, DEFAULT_STANDBY_THRESHOLD),
        config_entry.data.get(CONF_ACS_THRESHOLD, DEFAULT_ACS_THRESHOLD),
        config_entry.data.get(CONF_CIRCOLATORE_THRESHOLD, DEFAULT_CIRCOLATORE_THRESHOLD),
        config_entry.data.get(CONF_RISCALDAMENTO_THRESHOLD, DEFAULT_RISCALDAMENTO_THRESHOLD),
        config_entry.entry_id
    )
    
    # Creazione del sensore durata ACS
    acs_sensor = ACSDurationSensor(hass, config_entry, stato_sensor)
    
    async_add_entities([stato_sensor, acs_sensor])
