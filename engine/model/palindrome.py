from datetime import datetime

from engine.sternman_engine import SternmanEngine
from battery.SpindlerBattery import SpindlerBattery

class Palindrome(SternmanEngine, SpindlerBattery):
    def needs_service(self):
        return SternmanEngine.needs_service or SpindlerBattery.needs_service
