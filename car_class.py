# import my vehicle class
from vehicle_class import *
# define car class here and make it inherit from vehicle
class Car(Vehicle):
#Characterists:
# brand
# horse_power
# max_speed
    def __init__(self, n_passengers, size_cargo, brand, horse_power, max_speed):
        super().__init__(n_passengers, size_cargo)
        self.brand = brand
        self.horse_power = horse_power
        self.max_speed = max_speed

#methods :
# park
# honk
    def park(self):
        return 'parking'

    def honk(self):
        return 'beep beep'

