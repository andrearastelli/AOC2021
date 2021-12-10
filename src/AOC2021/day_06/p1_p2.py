from itertools import islice
from pathlib import Path
from collections import deque
from time import time
from array import array

def read_from_input():
    input_file = Path(__file__).parent / Path("p1_input")

    with input_file.open() as f:
        fishes = map(int, f.read().split(","))

    return array('B', fishes)

def timeit(func):
    def _(*args, **kwargs):
        start = time()
        return_value = func(*args, **kwargs)
        end = time()
        print(f"Processing time for {func.__name__}: {end-start}")
        return return_value
    return _

@timeit
def count_after_generation(fish_array, num_generations):
    for _ in range(num_generations):
        num_to_add = fish_array.count(0)

        fish_array = [6 if fish==0 else fish-1 for fish in fish_array]

        if num_to_add>0:
            fish_array.extend([8 for i in range(num_to_add)])

    return len(fish_array)

@timeit
def faster_count(fish_array, num_generations):
    # Builds a deque to have a data structure that can rotate for each generation
    totals = deque(fish_array.count(i) for i in range(9))

    for generation in range(num_generations):
        # move the number of 0s to the back to be the new number of 8s
        totals.rotate(-1)

        # Adds to the 6s the number of 0s because those are all the 0s that
        # have looped around to be 6s
        totals[6] += totals[8]

    return sum(totals)


if __name__ == "__main__":
    fish_array = read_from_input()

    p1_generations = 80
    p2_generations = 256

    num_after_80_gen = count_after_generation(fish_array, p1_generations)
    print(f"Num lanternfish after {p1_generations} generations: {num_after_80_gen}")

    print(faster_count(fish_array, p1_generations))
    print(faster_count(fish_array, p2_generations))
