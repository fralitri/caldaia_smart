from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from .sensor import async_setup_entry

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Caldaia Smart integration."""
    return True

async def async_setup_entry(hass, config_entry):
    """Set up the integration from a config entry."""
    return await async_setup_entry(hass, config_entry)
