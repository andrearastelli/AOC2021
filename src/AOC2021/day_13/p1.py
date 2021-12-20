from pathlib import Path


input_file = Path(__file__).parent / Path("p1_input")

coordinates, folding_instructions = input_file.open().read().split("\n\n")

coordinates = [
    tuple(map(int, coordinate.split(",")))
    for coordinate in coordinates.split("\n")
]
# print(coordinates)

folding_instructions = [
    instruction.strip().split(" ")[-1].split("=")
    for instruction in folding_instructions.split("\n")
]
folding_instructions = [
    (direction, int(position))
    for direction, position in folding_instructions
]
# print(folding_instructions)

max_x = max(x for x, y in coordinates)
max_y = max(y for x, y in coordinates)


first_instruction = folding_instructions[0]

new_coordinates = []
for x, y in sorted(coordinates):
    print(f"({x}, {y}) / ({x - first_instruction[1] if x > first_instruction[1] else x}, {y})")
    if x > first_instruction[1]:
        new_coordinates.append((x-first_instruction[1], y))
    else:
        new_coordinates.append((x, y))

print(first_instruction)
print(len(set(new_coordinates)))

# print(coordinates)
# print(len(set(coordinates)))


