def runProgram(programArray):
    instructionLength = 4
    for operator in range(0, len(programArray), instructionLength):
        if programArray[operator] == 99:
            break
        else:
            # Get the parameters 
            parameterOne = programArray[(operator + 1)]
            parameterTwo = programArray[(operator + 2)]
            changingIndex = programArray[(operator + 3)]
            if programArray[operator] == 1:
                programArray[changingIndex] = programArray[parameterOne] + programArray[parameterTwo]
                instructionLength = 4
            elif programArray[operator] == 2:
                programArray[changingIndex] = programArray[parameterOne] * programArray[parameterTwo]
                instructionLength = 4
            elif programArray[operator] == 3:
                userInput = raw_input('User input integer')
                programArray[(operator + 1)] = userInput
                instructionLength = 2
            elif programArray[operator] == 4:
                print programArray[(operator + 1)]
                instructionLength = 2


    return programArray[0]
    
# Read file to array
with open('input.txt') as _file:
    masterArray = []
    for var in _file:
        masterArray.append(var)

print runProgram(masterArray)