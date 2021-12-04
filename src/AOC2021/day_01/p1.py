from itertools import pairwise
from pathlib import Path

input_data = Path(__file__).parent / Path("./p1_input")

evaluated_data = []
with input_data.open() as input_file:
    input_lines = input_file.readlines()

    for line in input_lines:
        value = int(line.strip())
        evaluated_data.append(value)

num_measurements_larger_than_prev = len(
    list(
        filter(
            # Will compare the next element to the previous
            # Returning True when it's bigger.
            lambda p: p[1]>p[0],

            # This will pair the elements in the list
            pairwise(evaluated_data)
        )
    )
)

print(num_measurements_larger_than_prev)
