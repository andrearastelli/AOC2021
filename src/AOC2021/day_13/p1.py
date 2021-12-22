from pathlib import Path


def folding(coordinate_list, folding_instructions):
    new_coords = set()

    for coordinate in coordinate_list:
        x, y = coordinate
        x1, y1 = x, y

        for fold_instruction in folding_instructions:
            direction, amount = fold_instruction

            if direction == "x" and x1 > amount:
                x1 = x1 - (2 * (x1 - amount))

            elif direction == "y" and y1 > amount:
                y1 = y1 - (2 * (y1 - amount))

        new_coords.add((x1, y1))

    return new_coords


if __name__ == "__main__":
    input_file = Path(__file__).parent / Path("p1_input")

    coordinates, folding_instructions = input_file.open().read().split("\n\n")

    coordinates = [
        tuple(map(int, coordinate.split(",")))
        for coordinate in coordinates.split("\n")
    ]

    folding_instructions = [
        instruction.strip().split(" ")[-1].split("=")
        for instruction in folding_instructions.split("\n")
    ]
    folding_instructions = [
        (direction, int(position))
        for direction, position in folding_instructions
    ]

    first_fold = [folding_instructions[0]]
    new_coords = folding(coordinates, first_fold)
    print(f"Points after just the first fold: {len(new_coords)}")

    new_coords = folding(coordinates, folding_instructions)
    print(f"Points after all the folding: {len(new_coords)}")

    # Prints the letters on screen
    # Retrieve the max X and Y coordinates in order to better show the graphics
    # on the terminal
    max_x = max(x for x, y in new_coords)
    max_y = max(y for x, y in new_coords)

    print(f"Code in a {max_x+1}x{max_y+1} grid.")
    for i in range(max_y+1):
        for j in range(max_x+1):
            if (j, i) in new_coords:
                print("#", end="")
            else:
                print(" ", end="")

        print("")




