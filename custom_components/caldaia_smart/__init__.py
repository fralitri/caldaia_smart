"""Integrazione Caldaia Smart per Home Assistant."""
import logging
import voluptuous as vol
from homeassistant.helpers import config_validation as cv

DOMAIN = "caldaia_smart"

# Schema per la configurazione YAML
CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required("power_sensor"): cv.entity_id,
        vol.Optional("standby_threshold", default=20): cv.positive_int,
        vol.Optional("acs_threshold", default=60): cv.positive_int,
        vol.Optional("circolatore_threshold", default=100): cv.positive_int,
        vol.Optional("riscaldamento_threshold", default=140): cv.positive_int,
    })
}, extra=vol.ALLOW_EXTRA)

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    """Set up the Caldaia Smart integration."""
    conf = config.get(DOMAIN)
    if conf is None:
        return True

    power_sensor = conf["power_sensor"]
    standby_threshold = conf["standby_threshold"]
    acs_threshold = conf["acs_threshold"]
    circolatore_threshold = conf["circolatore_threshold"]
    riscaldamento_threshold = conf["riscaldamento_threshold"]

    # Aggiungi il sensore
    hass.helpers.discovery.load_platform("sensor", DOMAIN, {
        "power_sensor": power_sensor,
        "standby_threshold": standby_threshold,
        "acs_threshold": acs_threshold,
        "circolatore_threshold": circolatore_threshold,
        "riscaldamento_threshold": riscaldamento_threshold
    }, config)

    return True