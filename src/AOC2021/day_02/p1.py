from pathlib import Path

input_file = Path(__file__).parent / Path("./p1_input")

input_data = []
with input_file.open() as in_file:
    for line in in_file.readlines():
        direction, amount = line.strip().split()
        input_data.append((direction, int(amount)))

forward = 0
depth = 0
for directions in input_data:
    direction, amount = directions
    if direction == "forward":
        forward += amount
    elif direction == "up":
        depth -= amount
    elif direction == "down":
        depth += amount
    else:
        continue

print(f"Forward: {forward}")
print(f"Depth: {depth}")

print(forward * depth)