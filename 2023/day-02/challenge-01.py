with open ('input.txt', 'r') as _file:
    games = [entry.rstrip() for entry in _file]

red_limit = 12
green_limit = 13
blue_limit = 14

gamesSum = 0

for index, game in enumerate(games):
    game_possible = True
    game = game.split(':')
    hands = game[1].split(';')

    for hand in hands:
        cubes = hand.split(',')
        for check_cube in cubes:
            check_cube = check_cube.split(' ')
            if check_cube[2] == 'red':
                if int(check_cube[1]) > red_limit:
                    game_possible = False
            if check_cube[2] == 'green':
                if int(check_cube[1]) > green_limit:
                    game_possible = False
            if check_cube[2] == 'blue':
                if int(check_cube[1]) > blue_limit:
                    game_possible = False

    if game_possible:
        print('Game ', index+1, ' is possible')
        gamesSum += index+1
    else:
        print('Game ', index+1, ' isnt possible')

print('Sum of possible games:', gamesSum)