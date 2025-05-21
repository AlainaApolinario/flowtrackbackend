from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Temporary in-memory store for latest energy reading
latest_energy_data = {
    "voltage": 0.0,
    "current": 0.0,
    "power": 0.0,
    "kwh": 0.0
}

# Allow frontend to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data model matching ESP32's JSON payload
class EnergyData(BaseModel):
    voltage: float
    current: float
    power: float
    kwh: float

# POST endpoint for ESP32
@app.post("/data")
def receive_energy_data(data: EnergyData):
    global latest_energy_data
    latest_energy_data = data.dict()
    print("Received:", latest_energy_data)
    return {"status": "success", "received": latest_energy_data}

# GET endpoint for frontend/dashboard
@app.get("/data")
def get_energy_data():
    return latest_energy_data
