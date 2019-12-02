import math

def calcFuelForMass(mass):
    if(isinstance(mass, int) == False):
        return False;
    return int(math.floor(mass / 3) - 2)

fuelRequired = 0

fileInput = open('input.txt' , "r")
for val in fileInput:
    # Convert string to int
    val = int(val)
    # Calc fuel needed for component mass
    newVal = calcFuelForMass(val)
    # Add fuel to counter
    fuelRequired = fuelRequired + newVal
    
print "Fuel needed: ", fuelRequired