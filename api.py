from fastapi import FastAPI

from classes.solider import Solider
from functions.read_csv import create_solider
from classes.residence import Residence


app = FastAPI()

PATH = "data_solider/hayal_300_no_status.csv"


# soliders = create_solider(PATH)
# resisdence1 =  Residence()
# for i in range(8):
#     for solider_l in soliders:
#         while resisdence1.check_people_in_rooms():
#             solider = solider_l
#         resisdence1.people.append(solider_l)
#
# אני רוצה להכניס פה רשימה שך 8 אנישם שכל פעם יכנס לדיקט