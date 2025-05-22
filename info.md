# DAH SU800D – Home Assistant Integration

Integration for DAH Solar SU800D balcony power systems.

This integration fetches live data from the DAH Solar Cloud (https://cloud.dahsolar.com) and exposes it as Home Assistant sensors.

---

## 🌞 Features

- Login and automatic token refresh
- Live PV production data
- Total and daily energy yields
- Installed PV capacity
- CO₂ emission savings
- Device status (online, fault, offline)
- System metadata (name, address, runtime, etc.)
- Configuration via Home Assistant UI
- Native multilingual support (🇬🇧 English & 🇩🇪 Deutsch)

---

## ⚙️ Configuration

Go to **Settings > Devices & Services > Add Integration** and search for:

```
DAH SU800D
```

Then enter your:

- **Username** (email address)
- **Password**
- **Station ID** (from your DAH cloud URL or system info)

You can also change the language (default is German 🇩🇪).

---

## 🧠 Sensor Example

| Sensor                           | Description                 |
|----------------------------------|-----------------------------|
| `sensor.pv_power`                | Current power output (W)    |
| `sensor.pv_energy_today`         | Energy produced today (kWh) |
| `sensor.total_emission_reduction` | Total CO₂ saved (kg)       |
| `sensor.devices_online`          | Number of active devices    |

---

## 🛠️ Requirements

- DAH SU800D registered in the cloud
- Access to https://cloud.dahsolar.com

---

## 📦 Installation

1. Add this repository to HACS (as a custom repository)
2. Install the integration
3. Restart Home Assistant
4. Add the integration from the UI

---

## 👨‍💻 Code & Support

GitHub: [https://github.com/kleimj1/HACS_DAH_SU800D](https://github.com/kleimj1/HACS_DAH_SU800D)

Issues welcome via GitHub!

---

*Developed with ❤️ by the Home Assistant community.*
