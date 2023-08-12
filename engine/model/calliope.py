from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery import SpindlerBattery

class Calliope(CapuletEngine, SpindlerBattery):
    def needs_service(self):
        return (CapuletEngine.needs_service or SpindlerBattery.SpindlerBattery.needs_service)
