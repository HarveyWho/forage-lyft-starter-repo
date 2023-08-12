from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.NubbinBattery import NubbinBattery
from tire.Octoprime import Octoprime

class Rorschach(WilloughbyEngine, NubbinBattery):
    def needs_service(self):
        return WilloughbyEngine.needs_service or NubbinBattery.needs_service or Octoprime.needs_service
