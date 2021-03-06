def runProgram(programArray):
    for operator in range(0, len(programArray), 4):
        if programArray[operator] == 99:
            break
        else:
            # Get the parameters 
            parameterOne = programArray[(operator + 1)]
            parameterTwo = programArray[(operator + 2)]
            changingIndex = programArray[(operator + 3)]
            if programArray[operator] == 1:
                programArray[changingIndex] = programArray[parameterOne] + programArray[parameterTwo]
            elif programArray[operator] == 2:
                programArray[changingIndex] = programArray[parameterOne] * programArray[parameterTwo]
    return programArray[0]
    
# Read file to array
with open('input.txt') as _file:
    masterArray = []
    for var in _file:
        masterArray.append(int(var))
        
noun = 0
verb = 0

# For each Noun
while noun <= 99:
    # Start Verb at 0 for each Noun
    verb = 0
    while verb <= 99:
        attemptArr = masterArray[:]
        # set the master array to the current Noun and Verb
        attemptArr[1] = noun
        attemptArr[2] = verb
        output = runProgram(attemptArr)
        if  output == 19690720:
            print('Noun: ', noun, '; Verb: ', verb, '; Output: ', output)
            print 100 * noun + verb
            break
        else:
            verb += 1
    noun += 1