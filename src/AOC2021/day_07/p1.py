from pathlib import Path
from collections import Counter

input_file = Path(__file__).parent / Path("p1_input")

with input_file.open() as f:
    input_data = list(map(int, f.read().split(",")))

input_data_test = [16,1,2,0,4,2,7,1,2,14]

def fuel_to_optimal_position(input_data):
    input_data_counter = Counter(input_data)

    # array containing all the distances between each point from the min and
    # max of the input data
    distances = [
        sum(
            abs(distance-position)*quantity
            for position, quantity in input_data_counter.items()
        )
        # Iterate over all the distances
        for distance in range(min(input_data), max(input_data))
    ]

    return distances

def fuel_to_optimal_position_p2(input_data):
    input_data_counter = Counter(input_data)

    distances = (
        sum(
            sum(range(1, abs(distance-position)+1)) * quantity
            for position, quantity in input_data_counter.items()
        )
        for distance in range(min(input_data), max(input_data)+1)
    )

    return distances


if __name__ == "__main__":
    d = fuel_to_optimal_position(input_data)
    print(min(d))

    d = fuel_to_optimal_position_p2(input_data)
    print(min(d))