import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import selector
from .const import DOMAIN, CONF_NAME, CONF_TEMP_ACS, CONF_TEMP_ACF, CONF_TEMP_MANDATA, CONF_TEMP_RITORNO, CONF_TEMP_FUMI, CONF_CONSUMO_ELETTRICO

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
                vol.Required(
                    CONF_NAME,
                    description="Inserisci un nome identificativo per la caldaia."
                ): str,
                vol.Required(
                    CONF_TEMP_ACS,
                    description="Seleziona il sensore per la temperatura dell'acqua calda sanitaria (ACS)."
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_TEMP_ACF,
                    description="Seleziona il sensore per la temperatura dell'acqua fredda sanitaria (ACF)."
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_TEMP_MANDATA,
                    description="Seleziona il sensore per la temperatura di mandata del riscaldamento."
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_TEMP_RITORNO,
                    description="Seleziona il sensore per la temperatura di ritorno del riscaldamento."
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_TEMP_FUMI,
                    description="Seleziona il sensore per la temperatura dei fumi."
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_CONSUMO_ELETTRICO,
                    description="Seleziona il sensore per il consumo elettrico."
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
            }),
            errors=errors,
        )

    @staticmethod
    @callback
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

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional(
                    CONF_TEMP_ACS,
                    default=self.config_entry.data.get(CONF_TEMP_ACS),
                    description="Seleziona il sensore per la temperatura dell'acqua calda sanitaria (ACS)."
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Optional(
                    CONF_TEMP_ACF,
                    default=self.config_entry.data.get(CONF_TEMP_ACF),
                    description="Seleziona il sensore per la temperatura dell'acqua fredda sanitaria (ACF)."
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Optional(
                    CONF_TEMP_MANDATA,
                    default=self.config_entry.data.get(CONF_TEMP_MANDATA),
                    description="Seleziona il sensore per la temperatura di mandata del riscaldamento."
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Optional(
                    CONF_TEMP_RITORNO,
                    default=self.config_entry.data.get(CONF_TEMP_RITORNO),
                    description="Seleziona il sensore per la temperatura di ritorno del riscaldamento."
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Optional(
                    CONF_TEMP_FUMI,
                    default=self.config_entry.data.get(CONF_TEMP_FUMI),
                    description="Seleziona il sensore per la temperatura dei fumi."
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Optional(
                    CONF_CONSUMO_ELETTRICO,
                    default=self.config_entry.data.get(CONF_CONSUMO_ELETTRICO),
                    description="Seleziona il sensore per il consumo elettrico."
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
            }),
        )
