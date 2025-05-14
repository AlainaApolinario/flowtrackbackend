from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/api/energy",
    tags=["energy"]
)

# Sample in-memory storage
energy_db = []

class EnergyData(BaseModel):
    id: int
    voltage: float
    current: float
    power: float
    kwh: float

@router.get("/", response_model=List[EnergyData])
def get_all_energy():
    return energy_db

@router.post("/", response_model=EnergyData)
def create_energy(data: EnergyData):
    # Simple check for duplicate id
    if any(item['id'] == data.id for item in energy_db):
        raise HTTPException(status_code=400, detail="ID already exists")
    energy_db.append(data.dict())
    return data