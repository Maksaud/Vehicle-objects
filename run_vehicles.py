# import all the classes
from car_class import *
from vehicle_class import *
# create 2 vehicle instances
bus = Vehicle(20, 300)
van = Vehicle(2, 300)

# call methods and attributes to test
print(bus.n_passengers)
print(bus.accelerate())
print(van.car_break())
# create 2 car instances
# make car accelerate and make them break
# make car honk and park
my_car = Car(1, 0, 'Mercedes Benz', 200, 300)
your_car = Car(2, 0, 'BMW M4', 200, 300)


print(my_car.accelerate())
print(your_car.car_break())
print(my_car.honk())
print(your_car.park())

# create 2 plane instances here
# make plane accelerate and make them break
# make plane fly and land
