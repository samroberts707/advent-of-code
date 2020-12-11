highest_seat_id = 0

def AnalysePass(combination):
    combination = combination.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1').replace('\n', '')
    return int(combination[:7], 2) * 8 + int(combination[-3:], 2)

with open ('input.txt', 'r') as _file:
    for val in _file:
        current_pass = AnalysePass(val)
        if current_pass > highest_seat_id:
            highest_seat_id = current_pass

print 'Highest seat ID: ' + str(highest_seat_id)