from homeassistant.helpers.entity import Entity
from homeassistant.helpers.device_registry import DeviceEntryType
from .const import DOMAIN, CONF_NAME, CONF_TEMP_ACS, CONF_TEMP_ACF, CONF_TEMP_MANDATA, CONF_TEMP_RITORNO, CONF_TEMP_FUMI, CONF_CONSUMO_ELETTRICO

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Caldaia Smart sensors."""
    name = config_entry.data[CONF_NAME]
    temp_acs = config_entry.data[CONF_TEMP_ACS]
    temp_acf = config_entry.data[CONF_TEMP_ACF]
    temp_mandata = config_entry.data[CONF_TEMP_MANDATA]
    temp_ritorno = config_entry.data[CONF_TEMP_RITORNO]
    temp_fumi = config_entry.data[CONF_TEMP_FUMI]
    consumo_elettrico = config_entry.data[CONF_CONSUMO_ELETTRICO]

    # Crea un dispositivo
    device_registry = hass.helpers.device_registry.async_get(hass)
    device = device_registry.async_get_or_create(
        config_entry_id=config_entry.entry_id,
        identifiers={(DOMAIN, config_entry.entry_id)},
        name=name,
        manufacturer="Caldaia Smart",
        model="Generic",
    )

    # Aggiungi le entità al dispositivo
    async_add_entities([
        CaldaiaSmartSensor(hass, temp_acs, "Temperatura ACS", "°C", device.id),
        CaldaiaSmartSensor(hass, temp_acf, "Temperatura ACF", "°C", device.id),
        CaldaiaSmartSensor(hass, temp_mandata, "Temperatura Mandata", "°C", device.id),
        CaldaiaSmartSensor(hass, temp_ritorno, "Temperatura Ritorno", "°C", device.id),
        CaldaiaSmartSensor(hass, temp_fumi, "Temperatura Fumi", "°C", device.id),
        CaldaiaSmartSensor(hass, consumo_elettrico, "Consumo Elettrico", "W", device.id),
    ])

class CaldaiaSmartSensor(Entity):
    """Representation of a Caldaia Smart Sensor."""

    def __init__(self, hass, entity_id, name, unit, device_id):
        """Initialize the sensor."""
        self.hass = hass
        self._entity_id = entity_id
        self._name = name
        self._unit = unit
        self._device_id = device_id
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit

    @property
    def device_info(self):
        """Return device info."""
        return {
            "identifiers": {(DOMAIN, self._device_id)},
            "name": self._name,
            "manufacturer": "Caldaia Smart",
            "model": "Generic",
        }

    def update(self):
        """Fetch new state data for the sensor."""
        self._state = self.hass.states.get(self._entity_id).state
