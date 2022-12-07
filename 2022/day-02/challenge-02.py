with open ('input.txt', 'r') as _file:
    rounds = [entry.rstrip() for entry in _file]

roundScore = 0
totalScore = 0

# A = Rock
# B = Paper
# C = Scissors

for round in rounds:
    roundScore = 0
    # My selection
    if round[2] == 'X': # Lose
        roundScore += 0
        if round[0] == 'A':
            roundScore += 3
        elif round[0] == 'B':
            roundScore += 1
        elif round[0] == 'C':
            roundScore += 2
    elif round[2] == 'Y': # Draw
        roundScore += 3
        if round[0] == 'A':
            roundScore += 1
        elif round[0] == 'B':
            roundScore += 2
        elif round[0] == 'C':
            roundScore += 3
    elif round[2] == 'Z': # Win
        roundScore += 6
        if round[0] == 'A':
            roundScore += 2
        elif round[0] == 'B':
            roundScore += 3
        elif round[0] == 'C':
            roundScore += 1

    totalScore += roundScore
    


print('Total score: ', totalScore)
