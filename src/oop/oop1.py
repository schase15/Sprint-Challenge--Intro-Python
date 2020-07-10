# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class



# Base class 
class Vehicle():
    pass

# GroundVehicle class that inherits from Vehicle class
class GroundVehicle(Vehicle):
    pass

# Car class that inherits from GroundVehicle class
class Car(GroundVehicle):
    pass

# Motorcycle class that inherits from GroundVehicle class
class Motorcycle(GroundVehicle):
    pass

# FlightVehicle class that inherits from Vehicle class
class FlightVehicle(Vehicle):
    pass

# Airplane class that inherits from the FlightVehicle class
class Airplane(FlightVehicle):
    pass


# Starship class that inherits from the FlightVehicle class
class Starship(FlightVehicle):
    pass
