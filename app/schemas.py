from pydantic import BaseModel, Field
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .models import EnergyDataOut  # This will not be evaluated at runtime

class EnergyDataList(BaseModel):
    data: List["EnergyDataOut"]  # Forward reference as string

class EnergyDataOut(BaseModel):
    id: int
    voltage: float
    current: float
    power: float
    kwh: float
    timestamp: str
