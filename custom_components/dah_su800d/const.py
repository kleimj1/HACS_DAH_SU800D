"""Constants for the DAH SU800D integration."""

DOMAIN = "dah_su800d"

PLATFORMS = ["sensor"]

DEFAULT_LANG = 3  # Deutsch
DEFAULT_SCAN_INTERVAL = 300  # Sekunden

# API
BASE_URL = "https://interface.dhhome-e.com"
LOGIN_ENDPOINT = "/dh/auth/login"
EQUIPMENT_ENDPOINT = "/dh/stationBoard/equipmentStatistic"
STATUS_ENDPOINT = "/dh/stationBoard/stationState"
INFO_ENDPOINT = "/dh/stationBoard/stationInfo"
USERINFO_ENDPOINT = "/dh/stationBoard/stationUserInfo"

# Sensor Keys aus /equipmentStatistic
EQUIPMENT_SENSORS = {
    "power": {
        "name_key": "sensor.equipment.power.name",
        "unit": "W",
        "icon": "mdi:solar-power",
    },
    "electricity": {
        "name_key": "sensor.equipment.electricity.name",
        "unit": "kWh",
        "icon": "mdi:counter",
    },
    "cumulativeElectricity": {
        "name_key": "sensor.equipment.cumulativeElectricity.name",
        "unit": "kWh",
        "icon": "mdi:transmission-tower-export",
    },
    "installedPower": {
        "name_key": "sensor.equipment.installedPower.name",
        "unit": "kWp",
        "icon": "mdi:solar-panel-large",
    },
    "emissionReduction": {
        "name_key": "sensor.equipment.emissionReduction.name",
        "unit": "kg",
        "icon": "mdi:leaf",
    },
    "totalEmissionReduction": {
        "name_key": "sensor.equipment.totalEmissionReduction.name",
        "unit": "kg",
        "icon": "mdi:leaf-circle",
    },
    "profit": {
        "name_key": "sensor.equipment.profit.name",
        "unit": "€",
        "icon": "mdi:currency-eur",
    },
    "currency": {
        "name_key": "sensor.equipment.currency.name",
        "unit": "",
        "icon": "mdi:currency-sign",
    },
}

# Sensor Keys aus /stationState
STATUS_SENSORS = {
    "normalNo": {
        "name_key": "sensor.status.normalNo.name",
        "unit": "",
        "icon": "mdi:check-circle-outline",
    },
    "offlineNo": {
        "name_key": "sensor.status.offlineNo.name",
        "unit": "",
        "icon": "mdi:close-circle-outline",
    },
    "faultNo": {
        "name_key": "sensor.status.faultNo.name",
        "unit": "",
        "icon": "mdi:alert-circle-outline",
    },
    "warningNo": {
        "name_key": "sensor.status.warningNo.name",
        "unit": "",
        "icon": "mdi:alert-outline",
    },
}

# Sensor Keys aus /stationInfo
INFO_SENSORS = {
    "stationName": {
        "name_key": "sensor.info.stationName.name",
        "unit": "",
        "icon": "mdi:home-solar-panel",
    },
    "days": {
        "name_key": "sensor.info.days.name",
        "unit": "Tage",
        "icon": "mdi:calendar",
    },
    "userName": {
        "name_key": "sensor.info.userName.name",
        "unit": "",
        "icon": "mdi:account",
    },
    "address": {
        "name_key": "sensor.info.address.name",
        "unit": "",
        "icon": "mdi:map-marker",
    },
    "localTime": {
        "name_key": "sensor.info.localTime.name",
        "unit": "",
        "icon": "mdi:clock-outline",
    },
}
