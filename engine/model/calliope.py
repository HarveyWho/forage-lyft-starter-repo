from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery.SpindlerBattery import SpindlerBattery
from tire.Octoprime import Octoprime

class Calliope(CapuletEngine, SpindlerBattery, Octoprime):
    def needs_service(self):
        return CapuletEngine.needs_service or SpindlerBattery.needs_service or Octoprime.needs_service
