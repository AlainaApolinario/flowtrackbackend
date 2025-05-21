from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union
import uvicorn

app = FastAPI()

# CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can limit this to specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the expected data format
class SensorData(BaseModel):
    voltage: float
    current: float
    power: float
    kwh: float

@app.post("/data")
async def receive_data(data: SensorData):
    print("📡 Received data:")
    print(f"🔌 Voltage: {data.voltage} V")
    print(f"⚡ Current: {data.current} A")
    print(f"🔋 Power: {data.power} W")
    print(f"📈 kWh: {data.kwh}")

    return {
        "message": "Data received successfully",
        "status": "ok"
    }

# Optional: for local testing
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
