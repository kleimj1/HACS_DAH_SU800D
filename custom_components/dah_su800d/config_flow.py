"""Config flow for DAH SU800D integration."""
from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers.schema_config_entry_flow import (
    SchemaFlowFormStep,
    SchemaOptionsFlowHandler,
)
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema({
    vol.Required("username"): str,
    vol.Required("password"): str,
    vol.Required("station_id"): int,
    vol.Optional("lang", default=3): vol.In([1, 2, 3])  # 3 = Deutsch, 1 = Englisch
})


class DAHSU800DConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for DAH SU800D."""

    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult:
        """Handle the initial step."""
        if user_input is not None:
            await self.async_set_unique_id(f"dahsu800d_{user_input['station_id']}")
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=f"DAH SU800D Station {user_input['station_id']}",
                data=user_input
            )

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> SchemaOptionsFlowHandler:
        return DAHSU800DOptionsFlowHandler(config_entry)


class DAHSU800DOptionsFlowHandler(SchemaOptionsFlowHandler):
    """Handle options flow for DAH SU800D."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        super().__init__(config_entry)
        self.options_schema = vol.Schema({
            vol.Optional("lang", default=self.config_entry.data.get("lang", 3)): vol.In([1, 2, 3])
        })

    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> FlowResult:
        return await self.async_step_user(user_input)
