with open ('input.txt', 'r') as _file:
    calories = [entry.rstrip() for entry in _file]

topElf = 0
secondElf = 0
thirdElf = 0
currentElf = 0

for snack in calories:
    if snack != "":
        currentElf = currentElf + int(snack)
    else:
        if currentElf > topElf:
            thirdElf = secondElf
            secondElf = topElf
            topElf = currentElf
        elif currentElf > secondElf:
            thirdElf = secondElf
            secondElf = currentElf
        elif currentElf > thirdElf:
            thirdElf = currentElf
        currentElf = 0

print(topElf+secondElf+thirdElf)
print('Top elf: ', topElf)
print('Second elf: ', secondElf)
print('Third elf: ', thirdElf)