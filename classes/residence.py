class Residence:
    def __init__(self):
        self.rooms = 10
        self.people = []

    def check_people_in_rooms(self):
        if len(self.people) == 8:
            self.rooms -= 1
            return False
        return True


