import logging
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.const import Platform
from .const import (
    DOMAIN, CONF_NAME, CONF_CONSUMO_ELETTRICO,
    CONF_STANDBY_THRESHOLD, CONF_ACS_THRESHOLD, CONF_CIRCOLATORE_THRESHOLD, CONF_RISCALDAMENTO_THRESHOLD
)
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

    # Carica le piattaforme supportate
    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)

    # Aggiungi l'entità di stato
    consumo_elettrico = config_entry.data[CONF_CONSUMO_ELETTRICO]
    standby_threshold = config_entry.options.get(CONF_STANDBY_THRESHOLD, 20.0)
    acs_threshold = config_entry.options.get(CONF_ACS_THRESHOLD, 60.0)
    circolatore_threshold = config_entry.options.get(CONF_CIRCOLATORE_THRESHOLD, 85.0)
    riscaldamento_threshold = config_entry.options.get(CONF_RISCALDAMENTO_THRESHOLD, 130.0)

    device_registry = hass.helpers.device_registry.async_get(hass)
    device = device_registry.async_get_or_create(
        config_entry_id=config_entry.entry_id,
        identifiers={(DOMAIN, config_entry.entry_id)},
        name=config_entry.data[CONF_NAME],
        manufacturer="Caldaia Smart",
        model="Generic",
    )

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(
            config_entry, Platform.SENSOR
        )
    )

    hass.data[DOMAIN][config_entry.entry_id] = {
        "stato_sensor": CaldaiaSmartStatoSensor(
            hass, consumo_elettrico, standby_threshold, acs_threshold, circolatore_threshold, riscaldamento_threshold, device.id
        )
    }

    return True

async def async_unload_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(config_entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(config_entry.entry_id)
    return unload_ok
