class Residence:
    def __init__(self):
        self.count_rooms = 10
        self.rooms = {}
        self.people = []
        self.has_place = True
    def check_people_in_rooms(self):
        if len(self.people) == 8:
            return False
        return True

    def no_place(self):
        if len(self.people) == 8 and self.rooms == 0:
            self.has_place =  False
        return self.has_place
