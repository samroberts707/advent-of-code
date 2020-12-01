with open ('input.txt', 'r') as _file:
    entries = set([int(entry) for entry in _file.readlines()])

for firstVal in entries:
    # Subtract value from 2020 and check if the remainder is in the array
    for secondVal in entries:
        if (2020 - firstVal - secondVal) in entries:
            answerTwo = firstVal * secondVal * (2020 - firstVal - secondVal)
            # Answer Two
            print("Three entries that add to 2020 are:", firstVal, ', ', secondVal, ' and ', (2020 - firstVal - secondVal), '. Multiplied = ', answerTwo)
            break



