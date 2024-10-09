import os

from fastapi import FastAPI
from tapo import ApiClient

app = FastAPI()

async def P100_client(tapo_username, tapo_password, device_ip):
    client = ApiClient(tapo_username, tapo_password)
    device = await client.p100(device_ip)
    return device

async def P100_on(tapo_username, tapo_password, device_ip):
    device = await P100_client(tapo_username, tapo_password, device_ip)
    await device.on()

async def P100_off(tapo_username, tapo_password, device_ip):
    device = await P100_client(tapo_username, tapo_password, device_ip)
    await device.off()

async def P100_info(tapo_username, tapo_password, device_ip):
    device = await P100_client(tapo_username, tapo_password, device_ip)
    device_info = await device.get_device_info()
    return device_info.to_dict()

async def P100_usage(tapo_username, tapo_password, device_ip):
    device = await P100_client(tapo_username, tapo_password, device_ip)
    device_usage = await device.get_device_usage()
    return device_usage.to_dict()

@app.get("/")
async def accueil():
    return {"message": "Bienvenue sur mon site web FastAPI !"}

@app.get('/tapo/info')
async def tapo_info():
    tapo_username = os.getenv("TAPO_USERNAME")
    tapo_password = os.getenv("TAPO_PASSWORD")
    device_ip = os.getenv("DEVICE_IP")
    result = await P100_info(tapo_username,tapo_password,device_ip)
    return result

@app.get('/tapo/usage')
async def tapo_usage():
    tapo_username = os.getenv("TAPO_USERNAME")
    tapo_password = os.getenv("TAPO_PASSWORD")
    device_ip = os.getenv("DEVICE_IP")
    result = await P100_usage(tapo_username,tapo_password,device_ip)
    return result

@app.get('/tapo/on')
async def tapo_on():
    tapo_username = os.getenv("TAPO_USERNAME")
    tapo_password = os.getenv("TAPO_PASSWORD")
    device_ip = os.getenv("DEVICE_IP")
    await P100_on(tapo_username,tapo_password,device_ip)
    return {"device_on":True}

@app.get('/tapo/off')
async def tapo_off():
    tapo_username = os.getenv("TAPO_USERNAME")
    tapo_password = os.getenv("TAPO_PASSWORD")
    device_ip = os.getenv("DEVICE_IP")
    await P100_off(tapo_username,tapo_password,device_ip)
    return {"device_on":False}

@app.get('/tapo/status')
async def tapo_status():
    tapo_username = os.getenv("TAPO_USERNAME")
    tapo_password = os.getenv("TAPO_PASSWORD")
    device_ip = os.getenv("DEVICE_IP")
    result = await P100_info(tapo_username,tapo_password,device_ip)
    return {"device_on": result["device_on"]}