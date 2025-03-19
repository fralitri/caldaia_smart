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

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("device_name"): str,
                vol.Required("acs_temp"): str,
                vol.Required("afs_temp"): str,
                vol.Required("mandata_temp"): str,
                vol.Required("ritorno_temp"): str,
                vol.Required("fumi_temp"): str,
                vol.Required("consumo_caldaia"): str,
            }),
            errors=errors,
        )

    async def async_step_import(self, import_data):
        return await self.async_step_user(import_data)
