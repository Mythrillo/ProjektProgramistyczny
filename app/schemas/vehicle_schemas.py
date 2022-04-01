from datetime import datetime
from typing import Optional

import pydantic


class BaseVehicleCount(pydantic.BaseModel):
    status: str


class VehicleCount(BaseVehicleCount):
    id: int
    started: datetime
    ended: Optional[datetime]
    number_of_vehicles: Optional[int]

    class Config:
        orm_mode = True


class CreateVehicleCount(BaseVehicleCount):
    id: int

    class Config:
        orm_mode = True


class UpdateVehicleCount(BaseVehicleCount):
    ended: datetime
    number_of_vehicles: int

    class Config:
        orm_mode = True
