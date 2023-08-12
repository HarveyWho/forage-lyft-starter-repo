from abc import ABC, abstractmethod
from Battery import Battery
from datetime import datetime

class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.current_date = current_date


    @abstractmethod
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < datetime.today().date()