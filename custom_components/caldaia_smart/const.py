DOMAIN = "caldaia_smart"
CONF_NAME = "name"
CONF_TEMP_ACS = "temp_acs"
CONF_TEMP_ACF = "temp_acf"
CONF_TEMP_MANDATA = "temp_mandata"
CONF_TEMP_RITORNO = "temp_ritorno"
CONF_TEMP_FUMI = "temp_fumi"
CONF_CONSUMO_ELETTRICO = "consumo_elettrico"

# Nuove costanti per lo stato della caldaia
CONF_STANDBY_THRESHOLD = "standby_threshold"
CONF_ACS_THRESHOLD = "acs_threshold"
CONF_CIRCOLATORE_THRESHOLD = "circolatore_threshold"
CONF_RISCALDAMENTO_THRESHOLD = "riscaldamento_threshold"

DEFAULT_STANDBY_THRESHOLD = 20.0
DEFAULT_ACS_THRESHOLD = 60.0
DEFAULT_CIRCOLATORE_THRESHOLD = 85.0
DEFAULT_RISCALDAMENTO_THRESHOLD = 130.0

# Stati della caldaia
STATO_STANDBY = "Standby"
STATO_ACS = "ACS"
STATO_CIRCOLATORE = "Circolatore"
STATO_RISCALDAMENTO = "Riscaldamento"
