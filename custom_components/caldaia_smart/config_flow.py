vol.Optional(
    CONF_STANDBY_THRESHOLD,
    default=DEFAULT_STANDBY_THRESHOLD,
    description={"it": "Soglia di consumo per lo stato Standby (W). Valore predefinito: 20W.", "en": "Power threshold for Standby state (W). Default: 20W."}
): vol.Coerce(float),
vol.Optional(
    CONF_ACS_THRESHOLD,
    default=DEFAULT_ACS_THRESHOLD,
    description={"it": "Soglia di consumo per lo stato ACS (W). Valore predefinito: 60W.", "en": "Power threshold for ACS state (W). Default: 60W."}
): vol.Coerce(float),
vol.Optional(
    CONF_CIRCOLATORE_THRESHOLD,
    default=DEFAULT_CIRCOLATORE_THRESHOLD,
    description={"it": "Soglia di consumo per lo stato Circolatore (W). Valore predefinito: 85W.", "en": "Power threshold for Circolatore state (W). Default: 85W."}
): vol.Coerce(float),
vol.Optional(
    CONF_RISCALDAMENTO_THRESHOLD,
    default=DEFAULT_RISCALDAMENTO_THRESHOLD,
    description={"it": "Soglia di consumo per lo stato Riscaldamento (W). Valore predefinito: 130W.", "en": "Power threshold for Riscaldamento state (W). Default: 130W."}
): vol.Coerce(float),
