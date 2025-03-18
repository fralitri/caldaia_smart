import logging
from homeassistant.helpers.entity import Entity
from homeassistant.const import POWER_WATT

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    power_sensor = config.get('power_sensor')
    thresholds = {
        'standby': config.get('standby_threshold', 20),
        'acs': config.get('acs_threshold', 60),
        'circolatore': config.get('circolatore_threshold', 100),
        'riscaldamento': config.get('riscaldamento_threshold', 140)
    }
    add_entities([CaldaiaSmartSensor(power_sensor, thresholds)])

class CaldaiaSmartSensor(Entity):
    """Representation of a Caldaia Smart Sensor."""

    def __init__(self, power_sensor, thresholds):
        """Initialize the sensor."""
        self._power_sensor = power_sensor
        self._thresholds = thresholds
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Stato Caldaia"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor."""
        power = self.hass.states.get(self._power_sensor).state
        if power <= self._thresholds['standby']:
            self._state = 'Standby'
        elif power <= self._thresholds['acs']:
            self._state = 'ACS'
        elif power <= self._thresholds['circolatore']:
            self._state = 'Circolatore'
        elif power <= self._thresholds['riscaldamento']:
            self._state = 'Riscaldamento'
        else:
            self._state = 'Errore'