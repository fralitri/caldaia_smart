import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN, CONF_NAME, CONF_TEMP_ACS, CONF_TEMP_ACF, CONF_TEMP_MANDATA, CONF_TEMP_RITORNO, CONF_TEMP_FUMI, CONF_CONSUMO_ELETTRICO

class CaldaiaSmartConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Caldaia Smart Integration."""

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
                vol.Required(CONF_NAME): str,
                vol.Required(CONF_TEMP_ACS): str,
                vol.Required(CONF_TEMP_ACF): str,
                vol.Required(CONF_TEMP_MANDATA): str,
                vol.Required(CONF_TEMP_RITORNO): str,
                vol.Required(CONF_TEMP_FUMI): str,
                vol.Required(CONF_CONSUMO_ELETTRICO): str,
            }),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return CaldaiaSmartOptionsFlow(config_entry)

class CaldaiaSmartOptionsFlow(config_entries.OptionsFlow):
    """Handle options flow for Caldaia Smart Integration."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional(
                    CONF_TEMP_ACS,
                    default=self.config_entry.data.get(CONF_TEMP_ACS),
                ): str,
                vol.Optional(
                    CONF_TEMP_ACF,
                    default=self.config_entry.data.get(CONF_TEMP_ACF),
                ): str,
                vol.Optional(
                    CONF_TEMP_MANDATA,
                    default=self.config_entry.data.get(CONF_TEMP_MANDATA),
                ): str,
                vol.Optional(
                    CONF_TEMP_RITORNO,
                    default=self.config_entry.data.get(CONF_TEMP_RITORNO),
                ): str,
                vol.Optional(
                    CONF_TEMP_FUMI,
                    default=self.config_entry.data.get(CONF_TEMP_FUMI),
                ): str,
                vol.Optional(
                    CONF_CONSUMO_ELETTRICO,
                    default=self.config_entry.data.get(CONF_CONSUMO_ELETTRICO),
                ): str,
            }),
        )
