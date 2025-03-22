from homeassistant.helpers.entity import Entity
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.const import Platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.event import async_track_state_change
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
        self._icon = "mdi:power-standby"  # Icona predefinita per lo standby

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
        consumo = float(self.hass.states.get(self._entity_id).state)

        if consumo < self._standby_threshold:
            self._state = STATO_STANDBY
            self._icon = "mdi:power-standby"  # Nuova icona per lo standby
        elif consumo < self._acs_threshold:
            self._state = STATO_ACS
            self._icon = "mdi:water-pump"  # Nuova icona per ACS
        elif consumo < self._circolatore_threshold:
            self._state = STATO_CIRCOLATORE
            self._icon = "mdi:pump"  # Nuova icona per il circolatore
        elif consumo < self._riscaldamento_threshold:
            self._state = STATO_RISCALDAMENTO
            self._icon = "mdi:radiator"
        else:
            self._state = "Massima Potenza"
            self._icon = "mdi:alert"

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Caldaia Smart sensor platform."""
    # Recupera i dati di configurazione
    consumo_elettrico = config_entry.data[CONF_CONSUMO_ELETTRICO]
    standby_threshold = config_entry.data.get(CONF_STANDBY_THRESHOLD, 20.0)
    acs_threshold = config_entry.data.get(CONF_ACS_THRESHOLD, 60.0)
    circolatore_threshold = config_entry.data.get(CONF_CIRCOLATORE_THRESHOLD, 85.0)
    riscaldamento_threshold = config_entry.data.get(CONF_RISCALDAMENTO_THRESHOLD, 130.0)

    # Crea l'entità Stato Caldaia
    stato_sensor = CaldaiaSmartStatoSensor(
        hass,
        consumo_elettrico,
        standby_threshold,
        acs_threshold,
        circolatore_threshold,
        riscaldamento_threshold,
        config_entry.entry_id
    )

    # Aggiungi l'entità a Home Assistant
    async_add_entities([stato_sensor])
