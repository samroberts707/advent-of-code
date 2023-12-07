with open ('input.txt', 'r') as _file:
    games = [entry.rstrip() for entry in _file]

powerScore = 0

for index, game in enumerate(games):

    red_min = 0
    green_min = 0
    blue_min = 0
    gameScore = 0

    game = game.split(':')
    hands = game[1].split(';')

    for hand in hands:
        cubes = hand.split(',')
        for check_cube in cubes:
            check_cube = check_cube.split(' ')
            if check_cube[2] == 'red':
                if int(check_cube[1]) > red_min:
                    red_min = int(check_cube[1])
            if check_cube[2] == 'green':
                if int(check_cube[1]) > green_min:
                    green_min = int(check_cube[1])
            if check_cube[2] == 'blue':
                if int(check_cube[1]) > blue_min:
                    blue_min = int(check_cube[1])

    gameScore = red_min*green_min*blue_min
    print('Game power score is: ', gameScore)
    powerScore += gameScore
    print('Power score is: ', powerScore)

print('Power sum:', powerScore)