# TapoP100API

Base on [mihai-dinculescu/tapo](https://github.com/mihai-dinculescu/tapo/tree/main)

## How to run

- Create a venv : `python3 -m venv ./venv`
- Source the venv : `source ./venv/bin/activate`
- Install the requirements before start the API : `pip install -r requirements.txt`
- Export your environement variables : `export TAPO_USERNAME='<username>' && export TAPO_PASSWORD='<password>' && export DEVICE_IP='<ip>'`
- Start the API : `uvicorn app:app --reload --host 127.0.0.1 --port 5000`

These are the pages you can get :

- `/` :
- `/tapo/info` : device INFO
- `/tapo/usage` : device USAGE
- `/tapo/on` : device ON
- `/tapo/off` : device OFF
- `/tapo/status` : device STATUS (ON or OFF)

## Klipper/Moonraker implementation

I build this API for Klipper/Moonraker implementation, this is the configuration you have to set in order to work in `moonraker.conf`:

```ini
[power printer_plug]
type: http
on_url: http://127.0.0.1:5000/tapo/on
off_url: http://127.0.0.1:5000/tapo/off
status_url: http://127.0.0.1:5000/tapo/status
response_template:
  {% set resp = http_request.last_response().json() %}
  {resp["status"].lower()}
```

## Tapo P100 API as a service

If you want to make this python web server as a service do the following :

- follow the download and venv creation describe un [How to run](https://github.com/lduriez/TapoP100API?tab=readme-ov-file#how-to-run)
- go to the `TapoP100API` directory and create a `.env` file with

```ini
TAPO_USERNAME='<your_tapo_username>'
TAPO_PASSWORD='<your_tapo_password>'
DEVICE_IP='<your_tapo_device_ip>'
```

- create a file `/etc/systemd/system/tapo_api.service``

```ini
[Unit]
Description=Tapo FastAPI
After=network.target

[Service]
User=pi
Group=pi
WorkingDirectory=/home/pi/TapoP100API
Environment="PATH=/home/pi/TapoP100API/venv/bin"
EnvironmentFile=/home/pi/TapoP100API/.env
ExecStart=/home/pi/TapoP100API/venv/bin/uvicorn app:app --reload --host 127.0.0.1 --port 5000
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

- reload systemctl: `sudo systemctl daemon-relaod`
- start the service: `sudo systemctl start tapo_api`
- enable the service: `sudo systemctl enable tapo_api`
