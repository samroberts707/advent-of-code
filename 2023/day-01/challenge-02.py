import re

with open ('input.txt', 'r') as _file:
    calibrations = [entry.rstrip() for entry in _file]

calibration_sum = 0

for value in calibrations:
    numbers = re.findall(r'\d',value)
    full_number = int(numbers[0] + numbers[-1])
    calibration_sum += full_number

print('Full calibration is: ', calibration_sum)