import math

def calcFuelForMass(mass):
    fuelForMass = int(math.floor(mass / 3) - 2)
    fuelForMassFuel = calcFuelForFuel(fuelForMass)
    return fuelForMass + fuelForMassFuel

def calcFuelForFuel(massFuel):
    newFuel = 0
    fuelToCalc = massFuel
    tempVal = 0
    while fuelToCalc > 0:
        tempVal = int(math.floor(fuelToCalc / 3) - 2)
        if tempVal > 0:
            fuelToCalc = tempVal
            newFuel += tempVal
        else: 
            fuelToCalc = 0
    return int(newFuel)

with open('input.txt') as _file:
    fuelRequired = 0
    for val in _file:
        fuelRequired += calcFuelForMass(int(val))
    
print "Fuel needed: ", fuelRequired