# TapoP100API

Base on [mihai-dinculescu/tapo](https://github.com/mihai-dinculescu/tapo/tree/main)

How to run :

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
