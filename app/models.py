from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from .database import Base

class EnergyData(Base):
    __tablename__ = "energy_data"

    id = Column(Integer, primary_key=True, index=True)
    voltage = Column(Float)
    current = Column(Float)
    power = Column(Float)
    kwh = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
