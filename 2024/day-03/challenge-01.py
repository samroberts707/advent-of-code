import re

with open ('input.txt', 'r') as _file:
    memory_lines = [entry.rstrip() for entry in _file]

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
total = 0

for chunk in memory_lines:
    readable_muls = re.findall(pattern, chunk)
    # print(readable_muls)

    for mul in readable_muls:
        x, y = mul
        x, y = int(x), int(y)
        # print(f"X: {x}, Y: {y} Total: {x*y}; Standing Total: {total}")
        total = total + (x*y)

print("Total:",total)

    