from typing import Iterable
from itertools import tee, pairwise
from pathlib import Path

input_data = Path(__file__).parent / Path("./p1_input")

evaluated_data = []
with input_data.open() as input_file:
    input_lines = input_file.readlines()

    for line in input_lines:
        value = int(line.strip())
        evaluated_data.append(value)

def triplewise(iterable:Iterable) -> Iterable:
    """Need a custom "pairwise" function that generates a tuple
    with 3 elements instead of 2.

    Args:
        iterable (Iterable): The input iterable

    Returns:
        Iterable: The resulting iterable.
    """
    a, b, c = tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)

    return zip(a, b, c)


result = filter(
    lambda p: sum(p[1])>sum(p[0]),
    pairwise(triplewise(evaluated_data))
)

count_result = len(list(result))

print(count_result)