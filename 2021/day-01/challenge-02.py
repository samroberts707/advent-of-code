with open ('input.txt', 'r') as _file:
    entries = [int(entry.rstrip()) for entry in _file]

depthIncreases = 0

for index, depthVal in enumerate(entries):
  if (depthVal + entries[index-1] + entries[index-2]) > (entries[index-1] + entries[index-2] + entries[index-3]):
    depthIncreases = depthIncreases + 1

print('Total sliding increases: ', depthIncreases)