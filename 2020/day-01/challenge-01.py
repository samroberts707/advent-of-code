with open ('input.txt', 'r') as _file:
    entries = set([int(entry) for entry in _file.readlines()])

for firstVal in entries:
    # Subtract value from 2020 and check if the remainder is in the array
    if 2020 - firstVal in entries:
        answer = firstVal * (2020 - firstVal)
        break

# Answer One
print("Two entries that add to 2020 are:", firstVal, ' and ', 2020 - firstVal, '. Multiplied = ', answer)