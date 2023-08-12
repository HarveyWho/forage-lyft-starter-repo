from tire.tires import Tires

class Octoprime(Tires):
    def __init__(self, tire_arr) -> None:
        self.tire_arr = tire_arr
    def needs_service(self):
        sum = 0
        for tire_wear in self.tire_arr:
            sum += tire_wear
        if sum>=3:
            return True
        else:
            return False