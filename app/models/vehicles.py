from datetime import datetime

import sqlalchemy
from db import database


class VehicleCount(database.Base):
    __tablename__ = "vehicle_count"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    started = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.utcnow)
    ended = sqlalchemy.Column(sqlalchemy.DateTime)
    status = sqlalchemy.Column(sqlalchemy.String)
    number_of_vehicles = sqlalchemy.Column(sqlalchemy.Integer)
