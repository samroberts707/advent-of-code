from collections import Counter

with open ('input.txt', 'r') as _file:
    entries = [entry.rstrip() for entry in _file]

def gammaRateCalc(binaryList):
  binaryOutput = []
  for index in range(len(binaryList[0])):
    indexCounter = Counter(item[index] for item in binaryList)
    if indexCounter["0"] > indexCounter["1"]:
      binaryOutput.append("0")
    else:
      binaryOutput.append("1")
  binaryOutput = ''.join(binaryOutput)
  return binaryOutput

def epsilonRateCalc(binaryList):
  binaryOutput = []
  for index in range(len(binaryList[0])):
    indexCounter = Counter(item[index] for item in binaryList)
    if indexCounter["0"] < indexCounter["1"]:
      binaryOutput.append("0")
    else:
      binaryOutput.append("1")
  binaryOutput = ''.join(binaryOutput)
  return binaryOutput


gammaRate = int(gammaRateCalc(entries), 2)
epsilonRate = int(epsilonRateCalc(entries), 2)

print("Gamma rate: ", gammaRate)
print("Epsilon rate: ", epsilonRate)
print("Power consumption: ", gammaRate*epsilonRate)