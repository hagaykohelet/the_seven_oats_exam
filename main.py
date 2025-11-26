from fastapi import FastAPI
import uvicorn

from classes.solider import Solider
from functions.create_soldier_list import create_solider, sort_soldier_by_distance
from functions.create_residence import create_residence
from classes.residence import Residence, Room

app = FastAPI()

dorm_a = []
dorm_b = []
await_list = []


# solider = create_solider("data_solider/hayal_300_no_status.csv")
# r= create_residence(solider)
@app.post("/assignWithCsv")
def initial_placemet(PATH):
    global dorm_a, dorm_b, await_list
    solider = create_solider(PATH)
    dorm_a = create_residence(solider)
    dorm_b = create_residence(solider)
    await_list = solider.copy()
    return dorm_a, dorm_b


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
