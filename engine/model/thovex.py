from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery.NubbinBattery import NubbinBattery


class Thovex(CapuletEngine, NubbinBattery):
    def needs_service(self):
        return CapuletEngine.needs_service or NubbinBattery.needs_service
