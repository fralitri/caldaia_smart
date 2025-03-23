import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback  # Aggiunto
from homeassistant.helpers import selector
from .const import (
    DOMAIN, CONF_NAME, CONF_TEMP_ACS, CONF_TEMP_ACF, CONF_TEMP_MANDATA, CONF_TEMP_RITORNO, CONF_TEMP_FUMI, CONF_CONSUMO_ELETTRICO,
    CONF_STANDBY_THRESHOLD, CONF_ACS_THRESHOLD, CONF_CIRCOLATORE_THRESHOLD, CONF_RISCALDAMENTO_THRESHOLD,
    DEFAULT_STANDBY_THRESHOLD, DEFAULT_ACS_THRESHOLD, DEFAULT_CIRCOLATORE_THRESHOLD, DEFAULT_RISCALDAMENTO_THRESHOLD
)

class CaldaiaSmartConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Caldaia Smart."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Validazione input
            if not user_input[CONF_NAME]:
                errors[CONF_NAME] = "name_required"
            else:
                # Creazione entry
                return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        # Form per l'utente
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_NAME): str,  # Nome del dispositivo
                vol.Required(CONF_TEMP_ACS): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(CONF_TEMP_ACF): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(CONF_TEMP_MANDATA): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(CONF_TEMP_RITORNO): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(CONF_TEMP_FUMI): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(CONF_CONSUMO_ELETTRICO): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Optional(CONF_STANDBY_THRESHOLD, default=DEFAULT_STANDBY_THRESHOLD): vol.Coerce(float),
                vol.Optional(CONF_ACS_THRESHOLD, default=DEFAULT_ACS_THRESHOLD): vol.Coerce(float),
                vol.Optional(CONF_CIRCOLATORE_THRESHOLD, default=DEFAULT_CIRCOLATORE_THRESHOLD): vol.Coerce(float),
                vol.Optional(CONF_RISCALDAMENTO_THRESHOLD, default=DEFAULT_RISCALDAMENTO_THRESHOLD): vol.Coerce(float),
            }),
            errors=errors,
        )

    @staticmethod
    @callback  # Decoratore corretto
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return CaldaiaSmartOptionsFlow(config_entry)

class CaldaiaSmartOptionsFlow(config_entries.OptionsFlow):
    """Handle options flow for Caldaia Smart."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        # Mostra tutti i campi configurabili
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(CONF_NAME, default=self.config_entry.data.get(CONF_NAME)): str,
                vol.Required(CONF_TEMP_ACS, default=self.config_entry.data.get(CONF_TEMP_ACS)): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(CONF_TEMP_ACF, default=self.config_entry.data.get(CONF_TEMP_ACF)): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(CONF_TEMP_MANDATA, default=self.config_entry.data.get(CONF_TEMP_MANDATA)): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(CONF_TEMP_RITORNO, default=self.config_entry.data.get(CONF_TEMP_RITORNO)): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(CONF_TEMP_FUMI, default=self.config_entry.data.get(CONF_TEMP_FUMI)): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(CONF_CONSUMO_ELETTRICO, default=self.config_entry.data.get(CONF_CONSUMO_ELETTRICO)): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Optional(CONF_STANDBY_THRESHOLD, default=self.config_entry.options.get(CONF_STANDBY_THRESHOLD, DEFAULT_STANDBY_THRESHOLD)): vol.Coerce(float),
                vol.Optional(CONF_ACS_THRESHOLD, default=self.config_entry.options.get(CONF_ACS_THRESHOLD, DEFAULT_ACS_THRESHOLD)): vol.Coerce(float),
                vol.Optional(CONF_CIRCOLATORE_THRESHOLD, default=self.config_entry.options.get(CONF_CIRCOLATORE_THRESHOLD, DEFAULT_CIRCOLATORE_THRESHOLD)): vol.Coerce(float),
                vol.Optional(CONF_RISCALDAMENTO_THRESHOLD, default=self.config_entry.options.get(CONF_RISCALDAMENTO_THRESHOLD, DEFAULT_RISCALDAMENTO_THRESHOLD)): vol.Coerce(float),
            }),
        )
