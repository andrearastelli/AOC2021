import prettytable

from pathlib import Path


def show_tangle(tangle, size=10):
    table = prettytable.PrettyTable()

    # Build empty matrix
    input_matrix = [[0 for i in range(size)] for j in range(size)]
    for y in range(size):
        for x in range(size):
            # Color-code the 0s to be more visible in the terminal print
            if tangle[(x, y)] == 0:
                input_matrix[y][x] = u"\u001b[33m{}\u001b[0m".format(tangle[(x, y)])
            else:
                input_matrix[y][x] = tangle[(x, y)]

    table.add_rows(input_matrix)
    table.set_style(prettytable.DEFAULT)
    table.header = False

    print(table.get_string())


if __name__ == "__main__":
    input_file = Path(__file__).parent / Path("p1_input")

    tangle = [
        [int(number) for number in line.strip()]
        for line in input_file.open().readlines()
    ]

    tangle = {
        (x, y): tangle[y][x]
        for y in range(len(tangle))
        for x in range(len(tangle[y]))
    }

    num_iterations = 1000

    print(f"Step 0")
    show_tangle(tangle)

    num_flashes = 0
    iteration_full_flash = 0

    for iteration in range(1, num_iterations+1):
        # Step 1: Increment the octupi energy levels
        tangle = {k: v+1 for k, v in tangle.items()}

        # Step 2: Look for octopus that are flashing
        flashing_octopi_coordinates = []

        while True:
            new_flashing_octopi = [
                k
                for k, v in tangle.items()
                if v > 9 and k not in flashing_octopi_coordinates
            ]

            num_flashes += len(new_flashing_octopi)
            if len(new_flashing_octopi) == 0:
                break

            # Step 3: Increase the energy level of the octopi near a flashing octopus
            for x, y in new_flashing_octopi:
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (dx, dy) == (0, 0):
                            continue

                        try:
                            tangle[(x+dx, y+dy)] += 1
                        except:
                            pass

            # Step 4: Store the coordinates of the octopi that have flashed
            flashing_octopi_coordinates.extend(new_flashing_octopi)


        # Step 5: Return to step 2, but ignore all the octopi that have already flashed
        tangle = {k: 0 if v > 9 else v for k, v in tangle.items()}

        # Step 6: Print the result
        print(f"Step {iteration}")
        show_tangle(tangle)

        # PART 2 - check when all the octopi are flashing together
        if all(v == 0 for v in tangle.values()):
            iteration_full_flash = iteration
            break

    print(f"Num flashes: {num_flashes}")
    print(f"Iteration full flash: {iteration_full_flash}")