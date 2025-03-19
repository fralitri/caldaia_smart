import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import selector
from .const import DOMAIN

class CaldaiaSmartConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title=user_input["device_name"], data=user_input)

        sensors = self.hass.states.async_entity_ids("sensor")
        temperature_sensors = [s for s in sensors if "temperature" in s]
        power_sensors = [s for s in sensors if "power" in s]

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("device_name"): str,
                vol.Required("acs_temp"): selector.SelectSelector(
                    selector.SelectSelectorConfig(options=temperature_sensors)
                ),
                vol.Required("afs_temp"): selector.SelectSelector(
                    selector.SelectSelectorConfig(options=temperature_sensors)
                ),
                vol.Required("mandata_temp"): selector.SelectSelector(
                    selector.SelectSelectorConfig(options=temperature_sensors)
                ),
                vol.Required("ritorno_temp"): selector.SelectSelector(
                    selector.SelectSelectorConfig(options=temperature_sensors)
                ),
                vol.Required("fumi_temp"): selector.SelectSelector(
                    selector.SelectSelectorConfig(options=temperature_sensors)
                ),
                vol.Required("consumo_caldaia"): selector.SelectSelector(
                    selector.SelectSelectorConfig(options=power_sensors)
                ),
            }),
            errors=errors,
        )
