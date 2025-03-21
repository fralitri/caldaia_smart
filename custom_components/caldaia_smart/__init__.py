import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant import config_entries
from homeassistant.const import Platform
from .const import DOMAIN, CONF_CONSUMO_ELETTRICO, CONF_STANDBY_THRESHOLD, CONF_ACS_THRESHOLD, CONF_CIRCOLATORE_THRESHOLD, CONF_RISCALDAMENTO_THRESHOLD
from .sensor import CaldaiaSmartStatoSensor

# Configura il logger
_LOGGER = logging.getLogger(__name__)

# Definisci le piattaforme supportate (ad esempio, sensor)
PLATFORMS = [Platform.SENSOR]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Caldaia Smart integration."""
    _LOGGER.info("Caldaia Smart integration is being set up.")
    return True

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool:
    """Set up the Caldaia Smart integration from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][config_entry.entry_id] = config_entry.data

    # Crea l'entità Stato Caldaia
    consumo_elettrico = config_entry.data[CONF_CONSUMO_ELETTRICO]
    standby_threshold = config_entry.data.get(CONF_STANDBY_THRESHOLD, 20.0)
    acs_threshold = config_entry.data.get(CONF_ACS_THRESHOLD, 60.0)
    circolatore_threshold = config_entry.data.get(CONF_CIRCOLATORE_THRESHOLD, 85.0)
    riscaldamento_threshold = config_entry.data.get(CONF_RISCALDAMENTO_THRESHOLD, 130.0)

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
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(config_entry, "sensor")
    )

    return True

async def async_unload_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(config_entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(config_entry.entry_id)
    return unload_ok
