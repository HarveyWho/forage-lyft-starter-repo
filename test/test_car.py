import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex
from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery
from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(last_service_date, today)
        current_mileage = 0
        last_service_mileage = 0
        engine = capulet_engine(current_mileage, last_service_mileage)

        car = Calliope(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        current_mileage = 0
        last_service_mileage = 0
        engine = capulet_engine(current_mileage, last_service_mileage)

        car = Calliope(engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        current_mileage = 30001
        last_service_mileage = 0
        engine = capulet_engine(current_mileage, last_service_mileage)
        car = Calliope(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        current_mileage = 30000
        last_service_mileage = 0
        engine = capulet_engine(current_mileage, last_service_mileage)
        car = Calliope(engine, battery)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(last_service_date, today)
        current_mileage = 0
        last_service_mileage = 0
        engine = willoughby_engine(current_mileage, last_service_mileage)

        car = Glissade(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        current_mileage = 0
        last_service_mileage = 0
        engine = willoughby_engine(current_mileage, last_service_mileage)

        car = Glissade(engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        current_mileage = 60001
        last_service_mileage = 0
        engine = willoughby_engine(current_mileage, last_service_mileage)

        car = Glissade(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        current_mileage = 60000
        last_service_mileage = 0
        engine = willoughby_engine(current_mileage, last_service_mileage)

        car = Glissade(engine, battery)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = SpindlerBattery(last_service_date, today)
        warning_light = False
        engine = sternman_engine(warning_light)

        car = Palindrome(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        warning_light = False
        engine = sternman_engine(warning_light)

        car = Palindrome(engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        warning_light = True
        engine = sternman_engine(warning_light)

        car = Palindrome(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(last_service_date, today)
        warning_light = False
        engine = sternman_engine(warning_light)

        car = Palindrome(engine, battery)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(last_service_date, today)
        current_mileage = 0
        last_service_mileage = 0
        engine = willoughby_engine(current_mileage, last_service_mileage)

        car = Rorschach(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(last_service_date, today)
        current_mileage = 0
        last_service_mileage = 0
        engine = willoughby_engine(current_mileage, last_service_mileage)

        car = Rorschach(engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(last_service_date, today)
        current_mileage = 60001
        last_service_mileage = 0
        engine = willoughby_engine(current_mileage, last_service_mileage)

        car = Rorschach(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(last_service_date, today)
        current_mileage = 60000
        last_service_mileage = 0
        engine = willoughby_engine(current_mileage, last_service_mileage)

        car = Rorschach(engine, battery)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(last_service_date, today)
        current_mileage = 0
        last_service_mileage = 0
        engine = capulet_engine(current_mileage, last_service_mileage)

        car = Thovex(engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(last_service_date, today)
        current_mileage = 0
        last_service_mileage = 0
        engine = capulet_engine(current_mileage, last_service_mileage)

        car = Thovex(engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(last_service_date, today)
        current_mileage = 30001
        last_service_mileage = 0
        engine = capulet_engine(current_mileage, last_service_mileage)
        car = Thovex(engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        battery = NubbinBattery(last_service_date, today)
        current_mileage = 30000
        last_service_mileage = 0
        engine = capulet_engine(current_mileage, last_service_mileage)
        car = Thovex(engine, battery)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
