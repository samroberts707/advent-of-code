from collections import Counter

with open ('input.txt', 'r') as _file:
    entries = [entry.rstrip() for entry in _file]

def rateCalc(binaryList):
  binaryOutput = {
    'gammaRate': [],
    'epsilonRate': []
  }
  for index in range(len(binaryList[0])):
    indexCounter = Counter(item[index] for item in binaryList)
    if indexCounter["0"] < indexCounter["1"]:
      binaryOutput['gammaRate'].append("0")
      binaryOutput['epsilonRate'].append("1")
    else:
      binaryOutput['gammaRate'].append("1")
      binaryOutput['epsilonRate'].append("0")
  binaryOutput['gammaRate'] = int(''.join(binaryOutput['gammaRate']), 2)
  binaryOutput['epsilonRate'] = int(''.join(binaryOutput['epsilonRate']), 2)
  return binaryOutput


rates = rateCalc(entries)

print("Gamma rate: ", rates['gammaRate'])
print("Epsilon rate: ", rates['epsilonRate'])
print("Power consumption: ", rates['gammaRate']*rates['epsilonRate'])