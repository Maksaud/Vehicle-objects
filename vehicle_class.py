# define vehicle class here
class Vehicle():
#Characterists:
# n_passangers
# size_cargo
    def __init__(self, n_passengers, size_cargo):
        self.n_passengers = n_passengers
        self.size_cargo = size_cargo

    def accelerate(self):
        return 'vroom'

    def car_break(self):
        return 'scrrt'
#methods :
# accelerate
# break

