from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery.NubbinBattery import NubbinBattery
from tire.Octoprime import Octoprime

class Thovex(CapuletEngine, NubbinBattery):
    def needs_service(self):
        return CapuletEngine.needs_service or NubbinBattery.needs_service or Octoprime.needs_service
