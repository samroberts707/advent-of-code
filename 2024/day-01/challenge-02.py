with open ('input.txt', 'r') as _file:
    pairings = [entry.rstrip() for entry in _file]

similarities = 0
list = [[],[]]

for pair in pairings:
    pair = pair.split('   ')
    list[0].append(int(pair[0]))
    list[1].append(int(pair[1]))

list[0].sort()
list[1].sort()

for x in range(len(list[0])):
    similarities += abs(list[0][x] * list[1].count(list[0][x]))

print(similarities)