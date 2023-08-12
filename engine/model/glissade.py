from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.SpindlerBattery import SpindlerBattery

class Glissade(WilloughbyEngine, SpindlerBattery):
    def needs_service(self):
        return WilloughbyEngine.needs_service or SpindlerBattery.needs_service
