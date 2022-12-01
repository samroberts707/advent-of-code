with open ('input.txt', 'r') as _file:
    calories = [entry.rstrip() for entry in _file]

maxCalories = 0
currentElf = 0

for snack in calories:
    if snack != "":
        currentElf = currentElf + int(snack)
    else:
        if currentElf > maxCalories:
            maxCalories = currentElf
        currentElf = 0

print(maxCalories)