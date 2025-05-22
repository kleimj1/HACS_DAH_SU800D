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
        "name": "PV Leistung",
        "unit": "W",
        "icon": "mdi:solar-power",
    },
    "electricity": {
        "name": "PV Energie (heute)",
        "unit": "kWh",
        "icon": "mdi:counter",
    },
    "cumulativeElectricity": {
        "name": "PV Energie gesamt",
        "unit": "kWh",
        "icon": "mdi:transmission-tower-export",
    },
    "installedPower": {
        "name": "Installierte PV-Leistung",
        "unit": "kWp",
        "icon": "mdi:solar-panel-large",
    },
    "emissionReduction": {
        "name": "CO₂-Ersparnis (heute)",
        "unit": "kg",
        "icon": "mdi:leaf",
    },
    "totalEmissionReduction": {
        "name": "CO₂-Ersparnis gesamt",
        "unit": "kg",
        "icon": "mdi:leaf-circle",
    },
    "profit": {
        "name": "Heutiger Gewinn",
        "unit": "€",
        "icon": "mdi:currency-eur",
    },
    "currency": {
        "name": "Währung",
        "unit": "",
        "icon": "mdi:currency-sign",
    },
}

# Sensor Keys aus /stationState
STATUS_SENSORS = {
    "normalNo": {
        "name": "Geräte online",
        "unit": "",
        "icon": "mdi:check-circle-outline",
    },
    "offlineNo": {
        "name": "Geräte offline",
        "unit": "",
        "icon": "mdi:close-circle-outline",
    },
    "faultNo": {
        "name": "Geräte mit Fehler",
        "unit": "",
        "icon": "mdi:alert-circle-outline",
    },
    "warningNo": {
        "name": "Geräte mit Warnung",
        "unit": "",
        "icon": "mdi:alert-outline",
    },
}

# Sensor Keys aus /stationInfo
INFO_SENSORS = {
    "stationName": {
        "name": "Anlagenname",
        "unit": "",
        "icon": "mdi:home-solar-panel",
    },
    "days": {
        "name": "Anlagetage",
        "unit": "Tage",
        "icon": "mdi:calendar",
    },
    "userName": {
        "name": "Benutzername",
        "unit": "",
        "icon": "mdi:account",
    },
    "address": {
        "name": "Standort",
        "unit": "",
        "icon": "mdi:map-marker",
    },
    "localTime": {
        "name": "Lokale Zeit",
        "unit": "",
        "icon": "mdi:clock-outline",
    },
}
