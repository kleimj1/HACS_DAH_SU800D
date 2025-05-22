# Home Assistant Integration for DAH Solar SU800D

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz)
[![GitHub license](https://img.shields.io/github/license/kleimj1/HACS_DAH_SU800D)](https://github.com/kleimj1/HACS_DAH_SU800D/blob/main/LICENSE)

This custom integration brings DAH Solar SU800D system data into Home Assistant using the official DAH Cloud API.

---

## Features

- Live PV power output
- Daily and total energy production
- Installed capacity (kWp)
- CO₂ emission reduction stats
- Device status (online, offline, fault, warning)
- System details: name, address, runtime, etc.
- Configuration via Home Assistant UI
- Fully localized (English & German)
- Auto-refresh with token handling

---

## Installation

### Step 1: Add this Repository to HACS

1. Go to HACS > Integrations > Custom Repositories
2. Add this repository:  
   `https://github.com/kleimj1/HACS_DAH_SU800D`
3. Category: Integration

### Step 2: Install

1. After adding, install the integration via HACS.
2. Restart Home Assistant.

### Step 3: Configure

1. Go to **Settings > Devices & Services > Add Integration**
2. Search for **DAH SU800D**
3. Enter your credentials and station ID

---

## Configuration Fields

- `Username`: Your DAH cloud login email
- `Password`: Your DAH cloud password
- `Station ID`: From your DAH dashboard URL or system info
- `Language`: Optional (default = German 🇩🇪)

---

## Example Entities

| Entity ID                              | Description               |
|----------------------------------------|---------------------------|
| `sensor.pv_power`                      | Current power (W)         |
| `sensor.pv_energy_today`               | Energy today (kWh)        |
| `sensor.pv_total_energy`               | Total yield (kWh)         |
| `sensor.total_emission_reduction`      | CO₂ saved (kg)            |
| `sensor.devices_online`                | Number of online devices  |

---

## Troubleshooting

- Ensure the DAH cloud account is active and the station ID is valid.
- Check logs if login or data fetching fails.

---

## License

[MIT License](LICENSE)

---

**Developed with ❤️ for the Home Assistant Community**
