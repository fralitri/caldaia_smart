from homeassistant.helpers.entity import Entity
from homeassistant.helpers.device_registry import DeviceEntryType
from .const import (
    DOMAIN, CONF_NAME, CONF_CONSUMO_ELETTRICO,
    CONF_STANDBY_THRESHOLD, CONF_ACS_THRESHOLD, CONF_CIRCOLATORE_THRESHOLD, CONF_RISCALDAMENTO_THRESHOLD,
    STATO_STANDBY, STATO_ACS, STATO_CIRCOLATORE, STATO_RISCALDAMENTO
)

class CaldaiaSmartStatoSensor(Entity):
    """Representation of a Caldaia Smart Stato Sensor."""

    def __init__(self, hass, consumo_elettrico, standby_threshold, acs_threshold, circolatore_threshold, riscaldamento_threshold, device_id):
        """Initialize the sensor."""
        self.hass = hass
        self._entity_id = consumo_elettrico
        self._standby_threshold = standby_threshold
        self._acs_threshold = acs_threshold
        self._circolatore_threshold = circolatore_threshold
        self._riscaldamento_threshold = riscaldamento_threshold
        self._device_id = device_id
        self._state = None
        self._icon = "mdi:power-plug-off"

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

    @property
    def device_info(self):
        """Return device info."""
        return {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": "Caldaia Smart",
            "manufacturer": "Caldaia Smart",
            "model": "Generic",
        }

    def update(self):
        """Fetch new state data for the sensor."""
        consumo = float(self.hass.states.get(self._entity_id).state)

        if consumo < self._standby_threshold:
            self._state = STATO_STANDBY
            self._icon = "mdi:power-plug-off"
        elif consumo < self._acs_threshold:
            self._state = STATO_ACS
            self._icon = "mdi:water-boiler"
        elif consumo < self._circolatore_threshold:
            self._state = STATO_CIRCOLATORE
            self._icon = "mdi:pipe"
        else:
            self._state = STATO_RISCALDAMENTO
            self._icon = "mdi:radiator"
