from fastapi import FastAPI
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

# Enable CORS for frontend access (adjust origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace "*" with your frontend domain
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the expected data model for POST request
class EnergyData(BaseModel):
    voltage: float
    current: float
    power: float
    kwh: float

# POST endpoint to receive data from ESP32
@app.post("/data")
async def receive_energy_data(data: EnergyData):
    global latest_energy_data
    latest_energy_data = data.dict()
    print("Received data:", latest_energy_data)
    return {"status": "success", "received": latest_energy_data}

# GET endpoint to provide latest data to frontend
@app.get("/data")
async def get_energy_data():
    return latest_energy_data
