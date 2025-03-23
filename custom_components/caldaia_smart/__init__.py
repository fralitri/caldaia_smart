import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant import config_entries
from homeassistant.helpers import device_registry as dr  # Aggiunto
from homeassistant.const import Platform
from .const import DOMAIN, CONF_NAME

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

    # Crea il dispositivo principale
    device_registry = dr.async_get(hass)  # Correzione: async_get non richiede argomenti
    device_registry.async_get_or_create(
        config_entry_id=config_entry.entry_id,
        identifiers={(DOMAIN, config_entry.entry_id)},
        name=config_entry.data[CONF_NAME],  # Usa il nome inserito dall'utente
        manufacturer="Caldaia Smart",
        model="Generic",
    )

    # Carica le piattaforme supportate
    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(config_entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(config_entry.entry_id)
    return unload_ok
