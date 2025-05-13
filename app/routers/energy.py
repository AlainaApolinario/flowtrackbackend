# app/routes/energy.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter()

@router.get("/api/energy/")
def read_energy(db: Session = Depends(get_db)):
    # Temporary static response (you can replace with actual DB query later)
    return [
        {"id": 1, "voltage": 230, "current": 5, "power": 1150, "kwh": 0.23},
        {"id": 2, "voltage": 231, "current": 4.9, "power": 1131.9, "kwh": 0.25},
        {"id": 3, "voltage": 229, "current": 5.1, "power": 1167.9, "kwh": 0.27},
    ]
