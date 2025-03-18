import voluptuous as vol
from homeassistant import config_entries
from . import DOMAIN

class CaldaiaSmartConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Caldaia Smart."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Caldaia Smart", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("power_sensor"): str,
                vol.Required("standby_threshold", default=20): int,
                vol.Required("acs_threshold", default=60): int,
                vol.Required("circolatore_threshold", default=100): int,
                vol.Required("riscaldamento_threshold", default=140): int
            })
        )