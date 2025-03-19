from homeassistant.helpers.entity import Entity
from .const import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    config = config_entry.data
    sensors = [
        CaldaiaSmartSensor(config["device_name"], "ACS Temperature", config["acs_temp"]),
        CaldaiaSmartSensor(config["device_name"], "AFS Temperature", config["afs_temp"]),
        CaldaiaSmartSensor(config["device_name"], "Mandata Temperature", config["mandata_temp"]),
        CaldaiaSmartSensor(config["device_name"], "Ritorno Temperature", config["ritorno_temp"]),
        CaldaiaSmartSensor(config["device_name"], "Fumi Temperature", config["fumi_temp"]),
        CaldaiaSmartSensor(config["device_name"], "Consumo Caldaia", config["consumo_caldaia"]),
    ]
    async_add_entities(sensors)

class CaldaiaSmartSensor(Entity):
    def __init__(self, device_name, sensor_type, entity_id):
        self._device_name = device_name
        self._sensor_type = sensor_type
        self._entity_id = entity_id
        self._state = None

    @property
    def name(self):
        return f"{self._device_name} {self._sensor_type}"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        self._state = self.hass.states.get(self._entity_id).state
