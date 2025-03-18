import logging
from homeassistant.helpers.entity import Entity
from homeassistant.const import POWER_WATT

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    if discovery_info is None:
        _LOGGER.error("Questa integrazione deve essere configurata tramite YAML.")
        return

    power_sensor = discovery_info.get("power_sensor")
    thresholds = {
        "standby": discovery_info.get("standby_threshold", 20),
        "acs": discovery_info.get("acs_threshold", 60),
        "circolatore": discovery_info.get("circolatore_threshold", 100),
        "riscaldamento": discovery_info.get("riscaldamento_threshold", 140)
    }

    # Verifica che il sensore di potenza esista
    if not hass.states.get(power_sensor):
        _LOGGER.error(f"Sensore di potenza non trovato: {power_sensor}")
        return

    add_entities([CaldaiaSmartSensor(power_sensor, thresholds)])

class CaldaiaSmartSensor(Entity):
    """Rappresentazione di un sensore per la Caldaia Smart."""

    def __init__(self, power_sensor, thresholds):
        """Inizializza il sensore."""
        self._power_sensor = power_sensor
        self._thresholds = thresholds
        self._state = None

    @property
    def name(self):
        """Restituisce il nome del sensore."""
        return "Stato Caldaia"

    @property
    def state(self):
        """Restituisce lo stato del sensore."""
        return self._state

    def update(self):
        """Aggiorna lo stato del sensore."""
        power = float(self.hass.states.get(self._power_sensor).state)
        if power <= self._thresholds["standby"]:
            self._state = "Standby"
        elif power <= self._thresholds["acs"]:
            self._state = "ACS"
        elif power <= self._thresholds["circolatore"]:
            self._state = "Circolatore"
        elif power <= self._thresholds["riscaldamento"]:
            self._state = "Riscaldamento"
        else:
            self._state = "Errore"