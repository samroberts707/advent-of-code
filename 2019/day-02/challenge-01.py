def runProgram(programArray):
    for operator in range(0, len(programArray), 4):
        if programArray[operator] == 99:
            break
        else:
            changingIndex = programArray[operator + 3]
            valueOne = programArray[(operator + 1)]
            valueTwo = programArray[(operator + 2)]
            if programArray[operator] == 1:
                programArray[changingIndex] = programArray[valueOne] + programArray[valueTwo]
            elif programArray[operator] == 2:
                programArray[changingIndex] = programArray[valueOne] * programArray[valueTwo]
    return programArray

with open('input.txt') as _file:
    masterArray = []
    for var in _file:
        masterArray.append(int(var))

masterArray[1] = 12
masterArray[2] = 2
 
print runProgram(masterArray)
