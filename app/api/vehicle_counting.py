from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, UploadFile
from models import vehicles
from schemas import vehicle_schemas
from services import get_db
from sqlalchemy.orm import Session
from vehicle_counting.object_tracking import count_vehicles

router = APIRouter()


def _get_vehicle_count(db: Session, id: int) -> vehicle_schemas.VehicleCount:
    return db.query(vehicles.VehicleCount).filter(vehicles.VehicleCount.id == id).first()


def _create_vehicle_count(
    db: Session, vehicle_count: vehicle_schemas.CreateVehicleCount
) -> vehicle_schemas.CreateVehicleCount:
    vehicle_count = vehicles.VehicleCount(**vehicle_count)
    db.add(vehicle_count)
    db.commit()
    db.refresh(vehicle_count)
    return vehicle_count


@router.get("/vehicles/{id}", tags=["vehicles"], response_model=vehicle_schemas.VehicleCount)
def get_vehicle_count(id: int, db: Session = Depends(get_db)):
    vehicle_count = _get_vehicle_count(db, id)
    if vehicle_count is None:
        raise HTTPException(status_code=404, detail="Process id not found")
    return vehicle_count


@router.post("/vehicles/", tags=["vehicles"], status_code=202, response_model=vehicle_schemas.CreateVehicleCount)
async def start_vehicle_counting(file: UploadFile, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    contents = await file.read()
    vehicle_count = _create_vehicle_count(db, {"status": "processing"})
    background_tasks.add_task(count_vehicles, contents, vehicle_count.id, db)
    return vehicle_count
