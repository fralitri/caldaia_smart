import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
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
                vol.Required(
                    CONF_NAME,
                    description={"it": "Inserisci un nome identificativo per la caldaia.", "en": "Enter a name for the boiler."}
                ): str,
                vol.Required(
                    CONF_TEMP_ACS,
                    description={"it": "Seleziona il sensore per la Temperatura Acqua Calda Sanitaria.", "en": "Select the sensor for the Hot Water Temperature."}
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_TEMP_ACF,
                    description={"it": "Seleziona il sensore per la Temperatura Acqua Fredda Sanitaria.", "en": "Select the sensor for the Cold Water Temperature."}
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_TEMP_MANDATA,
                    description={"it": "Seleziona il sensore per la Temperatura Mandata Riscaldamento.", "en": "Select the sensor for the Heating Supply Temperature."}
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_TEMP_RITORNO,
                    description={"it": "Seleziona il sensore per la Temperatura Ritorno Riscaldamento.", "en": "Select the sensor for the Heating Return Temperature."}
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_TEMP_FUMI,
                    description={"it": "Seleziona il sensore per la Temperatura Fumi Caldaia.", "en": "Select the sensor for the Flue Gas Temperature."}
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_CONSUMO_ELETTRICO,
                    description={"it": "Seleziona il sensore per il Consumo Elettrico Caldaia.", "en": "Select the sensor for the Boiler Power Consumption."}
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Optional(
                    CONF_STANDBY_THRESHOLD,
                    default=DEFAULT_STANDBY_THRESHOLD,
                    description={"it": "Soglia di consumo per lo stato Standby (W).", "en": "Power threshold for Standby state (W)."}
                ): vol.Coerce(float),
                vol.Optional(
                    CONF_ACS_THRESHOLD,
                    default=DEFAULT_ACS_THRESHOLD,
                    description={"it": "Soglia di consumo per lo stato ACS (W).", "en": "Power threshold for ACS state (W)."}
                ): vol.Coerce(float),
                vol.Optional(
                    CONF_CIRCOLATORE_THRESHOLD,
                    default=DEFAULT_CIRCOLATORE_THRESHOLD,
                    description={"it": "Soglia di consumo per lo stato Circolatore (W).", "en": "Power threshold for Circolatore state (W)."}
                ): vol.Coerce(float),
                vol.Optional(
                    CONF_RISCALDAMENTO_THRESHOLD,
                    default=DEFAULT_RISCALDAMENTO_THRESHOLD,
                    description={"it": "Soglia di consumo per lo stato Riscaldamento (W).", "en": "Power threshold for Riscaldamento state (W)."}
                ): vol.Coerce(float),
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

        # Mostra tutti i campi configurabili
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(
                    CONF_NAME,
                    default=self.config_entry.data.get(CONF_NAME),
                    description={"it": "Nome della caldaia.", "en": "Boiler name."}
                ): str,
                vol.Required(
                    CONF_TEMP_ACS,
                    default=self.config_entry.data.get(CONF_TEMP_ACS),
                    description={"it": "Sensore per la Temperatura Acqua Calda Sanitaria.", "en": "Sensor for Hot Water Temperature."}
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_TEMP_ACF,
                    default=self.config_entry.data.get(CONF_TEMP_ACF),
                    description={"it": "Sensore per la Temperatura Acqua Fredda Sanitaria.", "en": "Sensor for Cold Water Temperature."}
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_TEMP_MANDATA,
                    default=self.config_entry.data.get(CONF_TEMP_MANDATA),
                    description={"it": "Sensore per la Temperatura Mandata Riscaldamento.", "en": "Sensor for Heating Supply Temperature."}
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_TEMP_RITORNO,
                    default=self.config_entry.data.get(CONF_TEMP_RITORNO),
                    description={"it": "Sensore per la Temperatura Ritorno Riscaldamento.", "en": "Sensor for Heating Return Temperature."}
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_TEMP_FUMI,
                    default=self.config_entry.data.get(CONF_TEMP_FUMI),
                    description={"it": "Sensore per la Temperatura Fumi Caldaia.", "en": "Sensor for Flue Gas Temperature."}
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Required(
                    CONF_CONSUMO_ELETTRICO,
                    default=self.config_entry.data.get(CONF_CONSUMO_ELETTRICO),
                    description={"it": "Sensore per il Consumo Elettrico Caldaia.", "en": "Sensor for Boiler Power Consumption."}
                ): selector.EntitySelector(selector.EntitySelectorConfig(domain="sensor")),
                vol.Optional(
                    CONF_STANDBY_THRESHOLD,
                    default=self.config_entry.options.get(CONF_STANDBY_THRESHOLD, DEFAULT_STANDBY_THRESHOLD),
                    description={"it": "Soglia di consumo per lo stato Standby (W).", "en": "Power threshold for Standby state (W)."}
                ): vol.Coerce(float),
                vol.Optional(
                    CONF_ACS_THRESHOLD,
                    default=self.config_entry.options.get(CONF_ACS_THRESHOLD, DEFAULT_ACS_THRESHOLD),
                    description={"it": "Soglia di consumo per lo stato ACS (W).", "en": "Power threshold for ACS state (W)."}
                ): vol.Coerce(float),
                vol.Optional(
                    CONF_CIRCOLATORE_THRESHOLD,
                    default=self.config_entry.options.get(CONF_CIRCOLATORE_THRESHOLD, DEFAULT_CIRCOLATORE_THRESHOLD),
                    description={"it": "Soglia di consumo per lo stato Circolatore (W).", "en": "Power threshold for Circolatore state (W)."}
                ): vol.Coerce(float),
                vol.Optional(
                    CONF_RISCALDAMENTO_THRESHOLD,
                    default=self.config_entry.options.get(CONF_RISCALDAMENTO_THRESHOLD, DEFAULT_RISCALDAMENTO_THRESHOLD),
                    description={"it": "Soglia di consumo per lo stato Riscaldamento (W).", "en": "Power threshold for Riscaldamento state (W)."}
                ): vol.Coerce(float),
            }),
        )
