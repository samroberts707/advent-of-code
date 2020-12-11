highest_seat_id = 0
pass_arr = []
my_seat = 0

def AnalysePass(combination):
    combination = combination.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1').replace('\n', '')
    return int(combination[:7], 2) * 8 + int(combination[-3:], 2)

with open ('input.txt', 'r') as _file:
    for val in _file:
        current_pass = AnalysePass(val)
        pass_arr.append(current_pass)
        if current_pass > highest_seat_id:
            highest_seat_id = current_pass

pass_arr.sort()
for x in range(pass_arr[0], highest_seat_id):
    if x not in pass_arr:
        my_seat = x

print 'Highest seat ID: ' + str(highest_seat_id)
print 'My Seat: ' + str(my_seat)