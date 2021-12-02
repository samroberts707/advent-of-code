with open ('input.txt', 'r') as _file:
    entries = [entry.rstrip().split(" ") for entry in _file]

depth = 0
hozPos = 0
aim = 0

for entry in entries:
  # Note this requires Python 3.10 to work
  match entry[0]:
    case "forward":
      hozPos += int(entry[1])
      depth += aim*int(entry[1])
    case "up":
      aim -= int(entry[1])
    case "down":
      aim += int(entry[1])

print("Depth is: ", depth)
print("Horizontal Position is: ", hozPos)
print("Aim is: ", aim)
print("Multiplied: ", depth*hozPos)