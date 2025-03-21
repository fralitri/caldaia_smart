async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry) -> bool:
    """Set up the Caldaia Smart integration from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][config_entry.entry_id] = config_entry.data

    # Crea l'entità Stato Caldaia
    consumo_elettrico = config_entry.data[CONF_CONSUMO_ELETTRICO]
    standby_threshold = config_entry.data.get(CONF_STANDBY_THRESHOLD, DEFAULT_STANDBY_THRESHOLD)
    acs_threshold = config_entry.data.get(CONF_ACS_THRESHOLD, DEFAULT_ACS_THRESHOLD)
    circolatore_threshold = config_entry.data.get(CONF_CIRCOLATORE_THRESHOLD, DEFAULT_CIRCOLATORE_THRESHOLD)
    riscaldamento_threshold = config_entry.data.get(CONF_RISCALDAMENTO_THRESHOLD, DEFAULT_RISCALDAMENTO_THRESHOLD)

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
