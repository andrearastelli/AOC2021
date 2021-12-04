from collections import Counter
from typing import Iterable, AnyStr
from pathlib import Path

input_file = Path(__file__).parent / Path("./p1_input")

input_data = []
with input_file.open() as in_file:
    for line in in_file.readlines():
        input_data.append(line.strip())


def find_gamma_rate(input_data:Iterable) -> AnyStr:
    for idx in range(len(input_data[0])):
        b = []
        for data in input_data:
            b.append(data[idx])
        most_significant = Counter(b).most_common(1)[0][0]
        yield most_significant

def find_epsilon_rate(input_data:Iterable) -> AnyStr:
    for idx in range(len(input_data[0])):
        b = []
        for data in input_data:
            b.append(data[idx])
        least_significant = Counter(b).most_common()[-1][0]
        yield least_significant


if __name__ == "__main__":
    gamma_rate_bin_string = "".join(list(find_gamma_rate(input_data)))
    gamma_rate = int(gamma_rate_bin_string, 2)
    print(gamma_rate)

    epsilon_rate_bin_string = "".join(list(find_epsilon_rate(input_data)))
    epsilon_rate = int(epsilon_rate_bin_string, 2)
    print(epsilon_rate)

    print(gamma_rate * epsilon_rate)