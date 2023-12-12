import re

with open ('input.txt', 'r') as _file:
    scratch_cards = [entry.rstrip() for entry in _file]

total_scratch_cards = 0

for index, card in enumerate(scratch_cards):
    total_scratch_cards += 1
    winners_in_hand = 0
    card_numbers = card.split(':')[1].split('|')
    winners = re.findall(r'\d+',card_numbers[0])
    your_numbers = re.findall(r'\d+',card_numbers[1])

    for number in your_numbers:
        if number in winners:
            winners_in_hand += 1

    print('Hand ', index, 'winners: ', winners_in_hand)
    
    for i in range(winners_in_hand):
        # print('Adding ', scratch_cards[index+1+i].split(':')[0])
        hand_to_duplicate = scratch_cards[(index+i+1)]
        print(hand_to_duplicate)
        scratch_cards.insert((index+i+1), hand_to_duplicate)

print('Total Scratch cards: ', total_scratch_cards)