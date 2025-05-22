"""The DAH SU800D integration."""
from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, PLATFORMS
from .dhsolar_api import DAHSolarClient

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up DAH SU800D from a config entry."""
    _LOGGER.debug("Setting up DAH SU800D integration with config: %s", entry.data)

    hass.data.setdefault(DOMAIN, {})

    client = DAHSolarClient(
        username=entry.data["username"],
        password=entry.data["password"],
        station_id=entry.data["station_id"],
        lang=entry.data.get("lang", 3),
        session=hass.helpers.aiohttp_client.async_get_clientsession(hass),
    )

    try:
        await client.async_login()
    except Exception as e:
        _LOGGER.error("Login to DAH API failed: %s", e)
        return False

    hass.data[DOMAIN][entry.entry_id] = client

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unloaded:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unloaded
#
