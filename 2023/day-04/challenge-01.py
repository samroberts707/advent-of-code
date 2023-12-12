import re

with open ('input.txt', 'r') as _file:
    scratch_cards = [entry.rstrip() for entry in _file]

total_points = 0

for card in scratch_cards:
    card_points = 0
    card_numbers = card.split(':')[1].split('|')
    winners = re.findall(r'\d+',card_numbers[0])
    your_numbers = re.findall(r'\d+',card_numbers[1])

    for number in your_numbers:
        if number in winners:
            if card_points == 0:
                card_points = 1
            else:
                card_points = card_points*2
    
    total_points += card_points

print('Total Point: ', total_points)