from homeassistant.helpers.entity import Entity
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.event import async_track_state_change
from homeassistant.core import callback
from .const import (
    DOMAIN, CONF_CONSUMO_ELETTRICO,
    CONF_STANDBY_THRESHOLD, CONF_ACS_THRESHOLD, CONF_CIRCOLATORE_THRESHOLD, CONF_RISCALDAMENTO_THRESHOLD,
    STATO_STANDBY, STATO_ACS, STATO_CIRCOLATORE, STATO_RISCALDAMENTO,
    DEFAULT_STANDBY_THRESHOLD, DEFAULT_ACS_THRESHOLD, DEFAULT_CIRCOLATORE_THRESHOLD, DEFAULT_RISCALDAMENTO_THRESHOLD  # Aggiunto
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
        self._attr_device_info = DeviceInfo(
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

class CaldaiaSmartACSTimeSensor(Entity):
    """Representation of a Caldaia Smart ACS Time Sensor."""

    def __init__(self, hass, stato_caldaia_entity_id, device_id):
        """Initialize the sensor."""
        self.hass = hass
        self._stato_caldaia_entity_id = stato_caldaia_entity_id
        self._device_id = device_id
        self._state = 0  # Tempo in ore
        self._icon = "mdi:clock"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device_id)},
            name="Caldaia Smart",  # Questo verrà sovrascritto dal nome inserito dall'utente
            manufacturer="Caldaia Smart",
            model="Generic",
        )

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Tempo ACS Ultime 24 Ore"

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
                self.hass, self._stato_caldaia_entity_id, async_state_changed_listener
            )
        )

    def _update_state(self):
        """Update the state of the sensor."""
        # Calcola il tempo trascorso in stato ACS nelle ultime 24 ore
        history = self.hass.states.get(self._stato_caldaia_entity_id).attributes.get("history", [])
        acs_time = sum(
            (end - start).total_seconds() / 3600  # Converti secondi in ore
            for start, end in history
            if self.hass.states.get(self._stato_caldaia_entity_id, start).state == STATO_ACS
        )
        self._state = round(acs_time, 2)  # Arrotonda a 2 decimali

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Caldaia Smart sensor platform."""
    # Crea l'entità Stato Caldaia
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

    # Crea l'entità Tempo ACS Ultime 24 Ore
    acs_time_sensor = CaldaiaSmartACSTimeSensor(
        hass,
        stato_sensor.entity_id,  # Usa l'ID dell'entità Stato Caldaia
        config_entry.entry_id
    )
    async_add_entities([acs_time_sensor])
