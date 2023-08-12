from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.NubbinBattery import NubbinBattery


class Rorschach(WilloughbyEngine, NubbinBattery):
    def needs_service(self):
        return WilloughbyEngine.needs_service or NubbinBattery.needs_service
