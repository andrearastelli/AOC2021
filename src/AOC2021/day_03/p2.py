from collections import Counter
from typing import Any, Iterable
from pathlib import Path

input_file = Path(__file__).parent / Path("./p1_input")

input_data = []
with input_file.open() as in_file:
    for line in in_file.readlines():
        input_data.append(line.strip())


oxygen_data = input_data[:]

valid_bits = []
for idx in range(len(oxygen_data[0])):
    bits = [data[idx] for data in oxygen_data]
    most_common = Counter(bits).most_common()
    if most_common[0][1] == most_common[1][1]:
        most_relevant_bit = "1"
    else:
        most_relevant_bit = most_common[0][0]

    idx1 = len(oxygen_data) - 1
    for data in reversed(oxygen_data):
        if data[idx] != most_relevant_bit:
            # print(f"{idx} - {idx1} - {oxygen_data[idx1]}")
            del oxygen_data[idx1]
        idx1 -= 1

oxygen_data_value = int(oxygen_data[0], 2)

co2_data = input_data[:]

valid_bits = []
for idx in range(len(co2_data[0])):
    bits = [data[idx] for data in co2_data]
    least_common = Counter(bits).most_common()
    if least_common[0][1] == least_common[1][1]:
        lest_relevant_bit = "0"
    else:
        lest_relevant_bit = least_common[-1][0]

    idx1 = len(co2_data) - 1
    for data in reversed(co2_data):
        if data[idx] != lest_relevant_bit:
            # print(f"{idx} - {idx1} - {co2_data[idx1]}")
            del co2_data[idx1]
        idx1 -= 1

    if len(co2_data) == 1:
        break

co2_data_value = int(co2_data[0], 2)

print(co2_data_value * oxygen_data_value)