import re

with open ('input.txt', 'r') as _file:
    schematic = [entry.rstrip() for entry in _file]

engine_parts = 0

for value in schematic:
    numbers = re.findall(r'\d+',value)
    # print('Found part number: ', full_number)
    # calibration_sum += full_number