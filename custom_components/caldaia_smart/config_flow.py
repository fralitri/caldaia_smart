import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from . import DOMAIN

class CaldaiaSmartConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Caldaia Smart."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Verifica che il sensore di potenza esista
            power_sensor = user_input["power_sensor"]
            if not self.hass.states.get(power_sensor):
                errors["power_sensor"] = "sensor_not_found"
            else:
                # Salva la configurazione
                return self.async_create_entry(title="Caldaia Smart", data=user_input)

        # Schema per l'interfaccia di configurazione
        data_schema = vol.Schema({
            vol.Required("power_sensor"): str,
            vol.Required("standby_threshold", default=20): int,
            vol.Required("acs_threshold", default=60): int,
            vol.Required("circolatore_threshold", default=100): int,
            vol.Required("riscaldamento_threshold", default=140): int
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
            description_placeholders={
                "power_sensor": "Selezionare il sensore di consumo elettrico (W)",
                "standby_threshold": "Soglia per lo stato Standby (W)",
                "acs_threshold": "Soglia per lo stato ACS (W)",
                "circolatore_threshold": "Soglia per lo stato Circolatore (W)",
                "riscaldamento_threshold": "Soglia per lo stato Riscaldamento (W)"
            }
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Opzioni di configurazione."""
        return CaldaiaSmartOptionsFlow(config_entry)

class CaldaiaSmartOptionsFlow(config_entries.OptionsFlow):
    """Gestione delle opzioni di configurazione."""

    def __init__(self, config_entry):
        """Inizializza il flusso delle opzioni."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Gestisce le opzioni di configurazione."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        # Precarica i valori attuali
        options = self.config_entry.options

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required("standby_threshold", default=options.get("standby_threshold", 20)): int,
                vol.Required("acs_threshold", default=options.get("acs_threshold", 60)): int,
                vol.Required("circolatore_threshold", default=options.get("circolatore_threshold", 100)): int,
                vol.Required("riscaldamento_threshold", default=options.get("riscaldamento_threshold", 140)): int
            })
        )
