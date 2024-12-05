import re

with open ('input.txt', 'r') as _file:
    memory_lines = [entry.rstrip() for entry in _file]

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"

executable = True
total = 0

for chunk in memory_lines:
    readable_commands = re.findall(pattern, chunk)
    
    for command in readable_commands:
        # print(command)
        if command[0]:  # match for mul(X,Y)
            x, y = command
            x, y = int(x), int(y)
            if executable:
                total = total + (x*y)
                print(f"Executing X: {x}, Y: {y} Total: {x*y}; Standing Total: {total}")
            else:
                print(f"Not Executing X: {x}, Y: {y} Total: {x*y}; Standing Total: {total}")
        else: # match for do() or don't()
            sub_match = re.search(r"(do\(\)|don't\(\))", chunk)
            if sub_match.group() == "do()":
                executable = True
                print("Setting executable to True")
            elif sub_match.group() == "don't()":
                executable = False
                print("Setting executable to False")

print("Total:",total)