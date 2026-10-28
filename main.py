import enum
from abc import ABC
from getopt import error


class VehicleSize(enum.Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class vehicle (ABC):
    def __init__ (self, vehicle_size: VehicleSize, licence_plate: str):
        self.licence_plate = licence_plate
        self.vehicle_size = vehicle_size
    def get_licence_plate(self):
        return self.licence_plate
    def get_vehicle_size(self):
        return self.vehicle_size.name

class car (vehicle):
    def __init__ (self, licence_plate: str):
        self.licence_plate = licence_plate
        self.vehicle_size = VehicleSize.MEDIUM

class MotorCycle(vehicle):
    def __init__(self, licence_plate: str):
        self.licence_plate = licence_plate
        self.vehicle_size = VehicleSize.SMALL

class truck (vehicle):
    def __init__ (self, licence_plate: str):
        self.licence_plate = licence_plate
        self.vehicle_size = VehicleSize.LARGE
class ParkingSpot (ABC):

    def __init__ (self, spotName: str, vehicle: vehicle):
        self.spotName = spotName
        self.vehicle = vehicle
    def isAvailable(self, sot):
        return self.vehicle is None
    def occupy (self, v):
        if self.isAvailable(v):
            self.vehicle = v
        else:
            pass # should throw error
    def vacate(self):
        self.vehicle = None


my_car = car("1234")
print(my_car.get_licence_plate())
print(my_car.get_vehicle_size())
