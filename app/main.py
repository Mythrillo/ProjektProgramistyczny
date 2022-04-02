from api import vehicle_counting
from fastapi import FastAPI

app = FastAPI(
    title="Vehicle Counting",
    description="Vehicle Counting API, not much more to say.",
    contact={"name": "Mikołaj Kałuża", "email": "mikolaj.kaluza1@edu.uekat.pl"},
)
app.include_router(vehicle_counting.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
