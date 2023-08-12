from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.SpindlerBattery import SpindlerBattery
from tire.Octoprime import Octoprime

class Glissade(WilloughbyEngine, SpindlerBattery):
    def needs_service(self):
        return WilloughbyEngine.needs_service or SpindlerBattery.needs_service or Octoprime.needs_service
