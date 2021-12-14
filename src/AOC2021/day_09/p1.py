from operator import mul
from functools import reduce
from collections import deque
from pathlib import Path

input_file = Path(__file__).parent / Path("p1_input")

def input_data(input_file):
    with input_file.open() as f:
        data_matrix = [[int(digit) for digit in line.strip()] for line in f.readlines()]

    return data_matrix


def find_low_points(data_matrix):
    search_list = [
        (-1,  0), # LEFT
        ( 0, -1), # TOP
        ( 1,  0), # RIGHT
        ( 0,  1)  # BOTTOM
    ]
    low_points = []
    for x in range(len(data_matrix)):
        for y in range(len(data_matrix[x])):
            search_areas = search_list[:]
            if x==0:
                search_areas.remove((-1, 0))
            if y==0:
                search_areas.remove((0, -1))
            if x==len(data_matrix)-1:
                search_areas.remove((1, 0))
            if y==len(data_matrix[x])-1:
                search_areas.remove((0, 1))

            current_value = data_matrix[x][y]
            surrounding_values = [data_matrix[x+cx][y+cy] for cx, cy in search_areas]
            # print(f"{current_value}: {search_areas} [{', '.join(map(str, surrounding_values))}]")
            is_lowest_point = [current_value < neighbor for neighbor in surrounding_values]
            if sum(is_lowest_point) == len(search_areas):
                low_points.append((current_value, (x, y)))

    return low_points

def print_matrix_position(matrix, basin_position, lowest_point):

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            elem = matrix[x][y]
            if (x, y) in basin_position:
                elem = u"\u001b[92m{}\u001b[0m".format(elem)
            if (x, y) == lowest_point:
                    elem = u"\u001b[93m{}\u001b[0m".format(elem)
            print(f"{elem}", end="")
        print("")

def find_basins(data_matrix):
    low_points = find_low_points(data_matrix)

    basins_list = []

    # crawl around the coordinates of each low points to look for a basin.
    searched_areas = deque()
    for _, low_point_coordinates in low_points:

        # On the first iteration for each low_point_coordinates the basin
        # is going to contain the low_point_coordinates
        basin = set([low_point_coordinates])

        # Add the low_point_coordinate to the already searched areas
        searched_areas.append(low_point_coordinates)

        # Add in the seach areas the 4 points around the low_point_coordinates
        x, y = low_point_coordinates
        search_areas = deque()
        if x-1 >= 0:
            search_areas.append((x-1,y))
        if x+1 < len(data_matrix):
            search_areas.append((x+1, y))
        if y-1 >= 0:
            search_areas.append((x, y-1))
        if y+1 < len(data_matrix[x]):
            search_areas.append((x, y+1))

        while len(search_areas) > 0:
            # Extract the coordinates to search around of from the search_areas
            coordinates = search_areas.popleft()
            # Append the current coordinates immediately to the searched areas
            searched_areas.append(coordinates)

            # Extract the coordinates
            x, y = coordinates

            # Check if the current position x is valid
            if data_matrix[x][y] != 9:
                basin.add((x, y))
            else:
                continue

            if x-1 >= 0 and data_matrix[x-1][y] != 9:
                search_areas.append((x-1,y))
            if x+1 < len(data_matrix) and data_matrix[x+1][y] != 9:
                search_areas.append((x+1, y))
            if y-1 >= 0 and data_matrix[x][y-1] != 9:
                search_areas.append((x, y-1))
            if y+1 < len(data_matrix[x]) and data_matrix[x][y+1] != 9:
                search_areas.append((x, y+1))

            for searched_position in searched_areas:
                if searched_position in search_areas:
                    search_areas.remove(searched_position)

        basins_list.append(basin)
        # print_matrix_position(data_matrix, basin, low_point_coordinates)

    return basins_list

if __name__ == "__main__":
    matrix = input_data(input_file)

    test_input = [
        "2199943210",
        "3987894921",
        "9856789892",
        "8767896789",
        "9899965678",
    ]
    test_input = [[int(digit) for digit in line] for line in test_input]

    low_points = find_low_points(matrix)
    print(sum([1+low_point for low_point, _ in low_points]))

    basins = find_basins(matrix)
    basins = list(sorted(map(list, basins), key=len, reverse=True))
    largest_basins = list(map(len, basins[:3]))
    print(largest_basins)
    print(reduce(mul, largest_basins))

    print_matrix_position(matrix, basins[0]+basins[1]+basins[2], (10, 10))