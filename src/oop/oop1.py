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


# Vehicle is the base class
class Vehicle:
    pass

# GroundVehicle inherits from Vehicle
class GroundVehicle(Vehicle):
    pass

# Car inherits from GroundVehicle
class Car(GroundVehicle):
    pass

# Motorcycle inherits from GroundVehicle
class Motorcycle(GroundVehicle):
    pass

# FlightVehicle inherits from Vehicle
class FlightVehicle(Vehicle):
    pass

# Starship inherits from FlightVehicle
class Starship(FlightVehicle):
    pass

# Airplance inherits from FlightVehicle
class Airplane(FlightVehicle):
    pass