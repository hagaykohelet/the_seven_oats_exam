class Solider:
    def __init__(self, personal_id:int, first_name:str, last_name:str, gender:str,city:str, distance:int):
        self.personal_id = personal_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city = city
        self.distance = distance
        self.placement_status = "awaiting placement"

    def change_status(self):
        self.placement_status = "assigned to residence"

