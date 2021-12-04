from itertools import count, tee, pairwise as pw
from pathlib import Path

input_data = Path(__file__).parent / Path("./p1_input")

evaluated_data = []
with input_data.open() as input_file:
    input_lines = input_file.readlines()

    for line in input_lines:
        value = int(line.strip())
        evaluated_data.append(value)

def pairwise(iterable):
    a, b, c = tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)

    return zip(a, b, c)


result = filter(
    lambda p: sum(p[1])>sum(p[0]),
    pw(pairwise(evaluated_data))
)

count_result = len(list(result))

print(count_result)