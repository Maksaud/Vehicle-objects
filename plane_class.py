from vehicle_class import *
class Plane(Vehicle):
    def __init__(self, n_passengers, size_cargo, type):
        super().__init__(n_passengers, size_cargo)
        self.type = type

    def fly(self):
        return 'flying'

    def land(self):
        return 'landing'

