from utils import add_years_to_date
from Battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        date_to_change_battery = add_years_to_date(self.last_service_date, 3)
        return date_to_change_battery < self.current_date