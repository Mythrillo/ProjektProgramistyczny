from api import vehicle_counting
from fastapi import FastAPI

app = FastAPI()
app.include_router(vehicle_counting.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
