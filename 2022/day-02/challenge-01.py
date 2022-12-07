with open ('input.txt', 'r') as _file:
    rounds = [entry.rstrip() for entry in _file]

roundScore = 0
totalScore = 0

# A & X = Rock
# B & Y = Paper
# C & Z = Scissors

for round in rounds:
    roundScore = 0
    # My selection
    if round[2] == 'X': # Rock
        roundScore += 1
        if round[0] == 'A':
            roundScore += 3
        elif round[0] == 'B':
            roundScore += 0
        elif round[0] == 'C':
            roundScore += 6
    elif round[2] == 'Y': # Paper
        roundScore += 2
        if round[0] == 'A':
            roundScore += 6
        elif round[0] == 'B':
            roundScore += 3
        elif round[0] == 'C':
            roundScore += 0
    elif round[2] == 'Z': # Scissors
        roundScore += 3
        if round[0] == 'A':
            roundScore += 0
        elif round[0] == 'B':
            roundScore += 6
        elif round[0] == 'C':
            roundScore += 3

    totalScore += roundScore
    


print('Total score: ', totalScore)
