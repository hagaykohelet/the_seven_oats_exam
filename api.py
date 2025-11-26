from fastapi import FastAPI
import uvicorn

from classes.solider import Solider
from functions.create_soldier_list import create_solider,sort_soldier_by_distance
from classes.residence import Residence, Room

app = FastAPI()

PATH = "data_solider/hayal_300_no_status.csv"


@app.get("/assignWithCsv")
def initial_placemet():
    soliders = create_solider(PATH)
    sorted_soldier_list = sort_soldier_by_distance(soliders)
    residence1 = Residence()
    for i in range(10):
        room = Room()
        for j in range(8):
            sorted_soldier_list[j].change_status()
            room.add_people(sorted_soldier_list[j])
        residence1.add_room(room)
    return residence1




if __name__ == "__main__":
    uvicorn.run(app,host="localhost", port=8000)