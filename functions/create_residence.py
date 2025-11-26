from classes.residence import Residence, Room
from functions.create_soldier_list import create_solider, sort_soldier_by_distance


def create_residence(soliders:list):
    sorted_soldier_list = sort_soldier_by_distance(soliders)
    residence = Residence()
    for i in range(10):
        room = Room()
        for j in range(8):
            solider = sorted_soldier_list.pop(0)
            solider.change_status()
            room.add_people(solider)
        residence.add_room(room)

    return residence


