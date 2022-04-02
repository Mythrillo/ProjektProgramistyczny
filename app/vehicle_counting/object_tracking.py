import gc
from datetime import datetime

import cv2
import imageio.v3 as iio
import numpy as np
from models import vehicles
from schemas import vehicle_schemas
from sqlalchemy.orm import Session


def _get_centroid(x: int, y: int, w: int, h: int) -> tuple[int, int]:
    """Get center of a rectangle"""
    x1 = int(w / 2)
    y1 = int(h / 2)

    cx = x + x1
    cy = y + y1
    return cx, cy


def _update_vehicle_count(db: Session, data: vehicle_schemas.UpdateVehicleCount) -> vehicle_schemas.UpdateVehicleCount:
    data = vehicles.VehicleCount(**data)
    vehicle_count = db.query(vehicles.VehicleCount).filter(vehicles.VehicleCount.id == data.id).first()
    if not vehicle_count:
        return
    try:
        vehicle_count.ended = data.ended
        vehicle_count.number_of_vehicles = data.number_of_vehicles
        vehicle_count.status = data.status
        db.commit()
        db.refresh(vehicle_count)
        return vehicle_count
    except Exception:
        return


def count_vehicles(contents: bytes, id: int, db: Session) -> None:
    """Method to count number of vehicles in a given video."""
    frames = iio.imread(contents, index=None, format_hint=".mp4")
    del contents
    gc.collect()
    min_contour_width = 40
    min_contour_height = 40
    offset = 10
    line_height = frames.shape[1] - 200
    matches = []
    cars = 0
    frame1 = frames[0]
    for i in range(1, len(frames)):
        frame2 = frames[i]
        contours = cv2.absdiff(frame1, frame2)
        contours = cv2.cvtColor(contours, cv2.COLOR_BGR2GRAY)
        contours = cv2.GaussianBlur(contours, (5, 5), 0)
        _, contours = cv2.threshold(contours, 20, 255, cv2.THRESH_BINARY)
        contours = cv2.dilate(contours, np.ones((3, 3)))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))

        contours = cv2.morphologyEx(contours, cv2.MORPH_CLOSE, kernel)
        contours, h = cv2.findContours(contours, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for i, c in enumerate(contours):
            (x, y, w, h) = cv2.boundingRect(c)
            contour_valid = w >= min_contour_width and h >= min_contour_height
            if not contour_valid:
                continue
            centroid = _get_centroid(x, y, w, h)
            matches.append(centroid)
            for x, y in matches:
                if y < line_height + offset and y > line_height - offset:
                    cars += 1
                    matches.remove((x, y))
        frame1 = frame2
    _update_vehicle_count(db, {"id": id, "status": "done", "ended": datetime.utcnow(), "number_of_vehicles": cars})
