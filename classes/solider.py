from pydantic import BaseModel



class Solider(BaseModel):
    personal_id: int
    first_name: str
    last_name: str
    gender: str
    city: str
    distance: int
    placement_status: str = "awaiting placement"

    def change_status(self):
        self.placement_status = "assigned to residence"
