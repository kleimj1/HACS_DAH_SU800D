"""Sensoren für DAH SU800D."""
from __future__ import annotations

from datetime import timedelta
import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)

from .const import (
    DOMAIN,
    EQUIPMENT_SENSORS,
    STATUS_SENSORS,
    INFO_SENSORS,
    DEFAULT_SCAN_INTERVAL,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Sensoren hinzufügen."""
    client = hass.data[DOMAIN][entry.entry_id]

    async def async_update_data():
        try:
            return await client.async_get_all_data()
        except Exception as err:
            _LOGGER.warning("Abruf fehlgeschlagen – versuche Re-Login: %s", err)
            try:
                await client.async_login()
                return await client.async_get_all_data()
            except Exception as login_err:
                raise UpdateFailed(f"Re-Login fehlgeschlagen: {login_err}") from login_err

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="DAH SU800D Coordinator",
        update_method=async_update_data,
        update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
    )

    await coordinator.async_config_entry_first_refresh()

    entities = []

    # Equipment-Sensoren
    for key, desc in EQUIPMENT_SENSORS.items():
        if key in coordinator.data.get("equipment", {}):
            entities.append(DAHSensor(coordinator, entry.entry_id, "equipment", key, desc))

    # Status-Sensoren
    for key, desc in STATUS_SENSORS.items():
        if key in coordinator.data.get("status", {}):
            entities.append(DAHSensor(coordinator, entry.entry_id, "status", key, desc))

    # Info-Sensoren
    for key, desc in INFO_SENSORS.items():
        if key in coordinator.data.get("info", {}):
            entities.append(DAHSensor(coordinator, entry.entry_id, "info", key, desc))

    async_add_entities(entities)


class DAHSensor(CoordinatorEntity, SensorEntity):
    """Ein einzelner DAH Sensor."""

    def __init__(
        self,
        coordinator: DataUpdateCoordinator,
        config_entry_id: str,
        source: str,  # "equipment", "status", "info"
        key: str,
        description: dict,
    ) -> None:
        super().__init__(coordinator)
        self._attr_unique_id = f"dah_su800d_{config_entry_id}_{source}_{key}"
        self._attr_translation_key = f"{source}.{key}"
        self._attr_translation_placeholders = {}
        self._attr_has_entity_name = True
        self._attr_icon = description.get("icon")
        self._attr_unit_of_measurement = description.get("unit")
        self.entity_description_key = key
        self.source = source

    @property
    def native_value(self):
        """Rückgabe des aktuellen Wertes."""
        return self.coordinator.data.get(self.source, {}).get(self.entity_description_key)
