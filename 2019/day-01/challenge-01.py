import math

def calcFuelForMass(mass):
    return int(math.floor(mass / 3) - 2)

with open('input.txt') as _file:
    fuelRequired = 0
    for val in _file:
        fuelRequired += calcFuelForMass(int(val))
    
print "Fuel needed: ", fuelRequired