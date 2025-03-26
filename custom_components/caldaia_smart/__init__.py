"""The caldaia_smart integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.typing import ConfigType

from .const import CONF_NAME, DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS = [Platform.SENSOR]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Caldaia Smart integration."""
    _LOGGER.info("Initializing Caldaia Smart integration")
    
    # Register the integration in hass.data if needed
    hass.data.setdefault(DOMAIN, {})
    
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Caldaia Smart from a config entry."""
    _LOGGER.debug(f"Setting up config entry: {entry.entry_id}")
    
    # Store the config entry in hass.data
    hass.data[DOMAIN][entry.entry_id] = entry.data
    
    # Create device registry entry
    device_registry = dr.async_get(hass)
    device_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        identifiers={(DOMAIN, entry.entry_id)},
        name=entry.data[CONF_NAME],
        manufacturer="Caldaia Smart",
        model="Generic",
        sw_version="1.0",
    )

    # Forward the setup to the sensor platform
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    _LOGGER.info(f"Caldaia Smart setup complete for {entry.data[CONF_NAME]}")
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.debug(f"Unloading config entry: {entry.entry_id}")
    
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)
        _LOGGER.info(f"Successfully unloaded entry {entry.entry_id}")
    else:
        _LOGGER.warning(f"Failed to unload entry {entry.entry_id}")
    
    return unload_ok

async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload config entry."""
    _LOGGER.debug(f"Reloading config entry: {entry.entry_id}")
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)
