from tire.tires import Tires

class Carrigan(Tires):
    def __init__(self, tire_arr) -> None:
        self.tire_arr = tire_arr
    def needs_service(self):
        for tire_wear in self.tire_arr:
            if tire_wear >= 0.9:
                return True
        return False
        