import logging
from homeassistant.const import Platform
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType
from .const import DOMAIN

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

    # Carica le piattaforme supportate
    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(config_entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(config_entry.entry_id)
    return unload_ok
