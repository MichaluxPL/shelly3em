# Shelly3EM to InfluxDB
Small utility to read data from Shelly3EM power monitoring device and store it in InfluxDB.
Requires python3 to run.

# Required python modules
```
urllib3
influxdb
urlencode
json
configparser
```
# Configuration
Edit the config.cfg and enter the following data:
```
[Shelly3EM]
IP=X.X.X.X                  # Shelly3EM IP address
userpass=user:pass          # Username and password delimited by colon

[InfluxDB]
influxdb=0                  # 0 - disabled, 1 - enabled
influxdb_host=127.0.0.1     # InfluxDB host IP address
influxdb_port=8086          # InfluxDB port number
influxdb_user=grafana       # InfluxDB username
influxdb_password=          # InfluxDB password
influxdb_dbname=            # InfluxDB database name (have to be created manually)

[General]
verbose=1                   # Output verbose data
terminal_output=1           # Output values on terminal
lang=en                     # en/pl - language version (corresponds to params_XX.json file)
```
# Run
```
bash:/python3 shelly3em.py  (or ./shelly3em.py)
* Shelly3EM response: **
{
    "wifi_sta": {
        "connected": true,
        "ssid": "Test",
        "ip": "192.168.1.1",
        "rssi": -67
    },
    "cloud": {
        "enabled": false,
        "connected": false
    },
    "mqtt": {
        "connected": false
    },
    "time": "09:00",
    "unixtime": 1651129257,
    "serial": 57905,
    "has_update": false,
    "mac": "C4ABAB1212AB",
    "cfg_changed_cnt": 0,
    "actions_stats": {
        "skipped": 0
    },
    "relays": [
        {
            "ison": true,
            "has_timer": false,
            "timer_started": 0,
            "timer_duration": 0,
            "timer_remaining": 0,
            "overpower": false,
            "is_valid": true,
            "source": "input"
        }
    ],
    "emeters": [
        {
            "power": 3.22,
            "pf": 0.02,
            "current": 0.6,
            "voltage": 240.23,
            "is_valid": true,
            "total": 33543.3,
            "total_returned": 101878.3
        },
        {
            "power": -28.99,
            "pf": -0.22,
            "current": 0.56,
            "voltage": 239.2,
            "is_valid": true,
            "total": 34410.8,
            "total_returned": 104140.1
        },
        {
            "power": -33.66,
            "pf": -0.24,
            "current": 0.6,
            "voltage": 238.11,
            "is_valid": true,
            "total": 55933.9,
            "total_returned": 90470.4
        }
    ],
    "total_power": -59.43,
    "fs_mounted": true,
    "update": {
        "status": "idle",
        "has_update": false,
        "new_version": "20220324-123835/v1.11.8-3EM-fix-g0014dcb",
        "old_version": "20220324-123835/v1.11.8-3EM-fix-g0014dcb"
    },
    "ram_total": 49440,
    "ram_free": 31476,
    "fs_size": 233681,
    "fs_free": 156875,
    "uptime": 2223746
}
Home grid statistics:
Phase 1
 Power [W]: -67.62
 Current [A]: 0.66
 Voltage [V]: 240.9
 Power from grid [Wh]: 33544.5
 Power returned [Wh]: 101890.0
Phase 2
 Power [W]: -103.23
 Current [A]: 0.7
 Voltage [V]: 241.41
 Power from grid [Wh]: 34411.5
 Power returned [Wh]: 104166.0
Phase 3
 Power [W]: -58.34
 Current [A]: 0.78
 Voltage [V]: 241.25
 Power from grid [Wh]: 55934.9
 Power returned [Wh]: 90494.0
Power usage (all phases) [W] : -229.19
Total power from grid [Wh] : 123890.9
Total power returned [Wh] : 296550.0
```
# Known Issues
You tell me :)

# Contrib
Feel free to suggest :)
If You want to rewrite or/add change anything - please fork Your own project.

Enjoy :)
