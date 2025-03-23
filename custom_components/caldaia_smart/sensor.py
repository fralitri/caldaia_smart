from homeassistant.helpers.entity import Entity
from homeassistant.helpers.device_registry import DeviceInfo  # Aggiunto
from homeassistant.helpers.event import async_track_state_change
from homeassistant.const import CONF_NAME
from .const import (
    DOMAIN, CONF_CONSUMO_ELETTRICO,
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
        self._icon = "mdi:power-standby"
        self._attr_device_info = DeviceInfo(  # Aggiunto
            identifiers={(DOMAIN, device_id)},
            name="Caldaia Smart",  # Questo verrà sovrascritto dal nome inserito dall'utente
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
            """Handle state
