startRange = 240298
endRange = 784956

def checkIncrement(val):
    # Join string with blank space then compare if new array sorted is same as initial val
    # If True means no descending numbers, else there is a descending number
    return "".join(sorted(val)) == val

def checkRepeat(val):
    for valOne, valTwo in zip(val, val[1:]):
        if valOne == valTwo:
            return True

def checkDoubleRepeat(val):
    for valOne, valTwo, valThree in zip(val, val[1:], val[2:]):
        if valOne == valTwo == valThree:
            return False
        elif valOne == valTwo or valOne == valThree or valTwo == valThree:
            return True
        

passwordCount = 0

for i in range(startRange, endRange):
    i = str(i)
    if checkIncrement(i):
        if checkDoubleRepeat(i):
            passwordCount += 1
            print i

print 'Password Count:', passwordCount