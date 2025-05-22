"""API-Client für DAH SU800D."""
import logging
from typing import Any

import aiohttp
from aiohttp import ClientSession, ClientResponseError

from .const import (
    BASE_URL,
    LOGIN_ENDPOINT,
    EQUIPMENT_ENDPOINT,
    STATUS_ENDPOINT,
    INFO_ENDPOINT,
    USERINFO_ENDPOINT,
)

_LOGGER = logging.getLogger(__name__)


class DAHSolarClient:
    """DAH Solar API-Client für die SU800D-Serie."""

    def __init__(self, username: str, password: str, station_id: int, lang: int, session: ClientSession) -> None:
        self.username = username
        self.password = password
        self.station_id = station_id
        self.lang = lang
        self.session = session
        self._access_token = None
        self._client_id = "e5cd7e4891bf95d1d19206ce24a7b32e"

    async def async_login(self) -> None:
        """Melde dich an und speichere den Access Token."""
        url = f"{BASE_URL}{LOGIN_ENDPOINT}"
        payload = {
            "username": self.username,
            "password": self.password,
            "clientId": self._client_id,
            "grantType": "terminal",
            "lang": self.lang,
        }

        async with self.session.post(url, json=payload) as resp:
            resp.raise_for_status()
            data = await resp.json()

        if data.get("code") != 200 or "access_token" not in data.get("data", {}):
            raise Exception(f"Login fehlgeschlagen: {data.get('msg')}")

        self._access_token = data["data"]["access_token"]
        _LOGGER.debug("DAH login erfolgreich, Access Token gesetzt.")

    async def _get(self, endpoint: str, retry: bool = True) -> dict[str, Any]:
        """Interner GET-Call mit optionalem automatischem Re-Login."""
        url = f"{BASE_URL}{endpoint}?stationId={self.station_id}&lang={self.lang}"
        headers = {
            "Authorization": f"Bearer {self._access_token}",
            "clientid": self._client_id,
        }

        try:
            async with self.session.get(url, headers=headers) as resp:
                if resp.status in (401, 403) and retry:
                    _LOGGER.warning("Token ungültig, versuche Re-Login...")
                    await self.async_login()
                    return await self._get(endpoint, retry=False)

                resp.raise_for_status()
                data = await resp.json()
                if data.get("code") != 200:
                    raise Exception(f"Fehlerhafte Antwort: {data}")
                return data.get("data", {})
        except ClientResponseError as e:
            _LOGGER.error("HTTP-Fehler: %s", e)
            raise
        except Exception as e:
            _LOGGER.error("Fehler beim Abrufen von %s: %s", endpoint, e)
            raise

    async def async_get_equipment_data(self) -> dict[str, Any]:
        """Lade Produktionsdaten."""
        return await self._get(EQUIPMENT_ENDPOINT)

    async def async_get_status_data(self) -> dict[str, Any]:
        """Lade Gerätestatus (online/offline/fault)."""
        return await self._get(STATUS_ENDPOINT)

    async def async_get_info_data(self) -> dict[str, Any]:
        """Lade Standortinformationen."""
        return await self._get(INFO_ENDPOINT)

    async def async_get_all_data(self) -> dict[str, dict[str, Any]]:
        """Kombiniere alle relevanten Daten in einem Aufruf."""
        equipment = await self.async_get_equipment_data()
        status = await self.async_get_status_data()
        info = await self.async_get_info_data()
        return {
            "equipment": equipment,
            "status": status,
            "info": info,
        }
