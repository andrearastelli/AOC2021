from itertools import chain
from pathlib import Path

input_file = Path(__file__).parent / Path("p1_input")


def read_input_stream(input_file):
    output_data = []
    with input_file.open() as f:
        for line in f.readlines():
            input, output = line.strip().split(" | ")
            output_data.append((input.split(), output.split()))

    return output_data


digit_segments = {
    # 0: 6,
    1: 2,
    # 2: 5,
    # 3: 5,
    4: 4,
    # 5: 5,
    # 6: 6,
    7: 3,
    8: 7,
    # 9: 6
}


def count_digits_1_4_7_8(input_data):
    lines = [output for input, output in input_data]

    list_numbers = [
        [len(number) in digit_segments.values() for number in output]
        for output in lines
    ]

    num_digits = sum(map(int, chain.from_iterable(list_numbers)))

    return num_digits


def extract_all_digits(input_data):
    # First need to map the 10 numbers as input so that they make sense as
    # numbers for a segment display.
    # Then, based on the mapping for the input, evaluate the corresponding
    # output numbers.

    # Invert the digit mapping so we can get the number corresponding to the
    # length of the segments
    digit_mapping = dict((segments, number) for number, segments in digit_segments.items())

    def sorting_key(item):
        return digit_mapping.get(len(item), len(item)*2)

    # Iterate over the input and output data
    for input, output in input_data:

        line_mapping_dict = dict()

        # Iterate over the input data sorted by the length of the segments
        for number, mixed_segments in enumerate(sorted(input, key=sorting_key)):

            # Extract the potential number corresponding to the length of the
            # segments
            potential_number = digit_mapping.get(len(mixed_segments))

            # If the number exists then try to map it to build a potential structure
            if potential_number is not None:
                line_mapping_dict[potential_number] = mixed_segments

            # Else try to extrapolate the numbers based on the known informations
            # and because of the sorting order we are sure that we're gonna hit
            # this branch ONLY after we already have a mapping for the numbers
            # 1, 4, 7, and 8
            else:
                # Extract the common letters between all the known numbers
                # and we already know that 1 has the common letters to all the
                # known numbers
                common_letters = line_mapping_dict[1]

                # Of those common letters, 1 is shared with the number 2
                # and 1 is shared with the number 5
                # in both cases, only 1 of the two and NOT the other
                # so we could start by looking at which number could potentially
                # be either of the two
                if len(mixed_segments) == 5:
                    # if the segments of the number 1 are common to the number
                    # and if the number if of length 5 then it must be a 3
                    if common_letters[0] in mixed_segments and common_letters[1] in mixed_segments:
                        potential_number = 3
                        line_mapping_dict[potential_number] = mixed_segments

                    elif common_letters[0] in mixed_segments and common_letters[1] not in mixed_segments:
                        potential_number = 2
                        line_mapping_dict[potential_number] = mixed_segments

                    else:
                        potential_number = 5
                        line_mapping_dict[potential_number] = mixed_segments

                # If the length is 6 then it could be a 9, a 0 or a 6
                if len(mixed_segments) == 6:

                    # it's a 9 if it has all letters of a 3, plus one more
                    if common_letters[0] in mixed_segments and common_letters[1] in mixed_segments:
                        segments_for_3 = line_mapping_dict[3]
                        is_number_9 = sum([digit in segments_for_3 for digit in mixed_segments])

                        if is_number_9 == len(segments_for_3):
                            potential_number = 9
                            line_mapping_dict[potential_number] = mixed_segments

                        # If it's not a 9 then it's a 0
                        else:
                            potential_number = 0
                            line_mapping_dict[potential_number] = mixed_segments

                    # Else it's a 6
                    else:
                        potential_number = 6
                        line_mapping_dict[potential_number] = mixed_segments


        # Refine 5 and 2 to be more accurate
        segments5 = line_mapping_dict[5]
        segments2 = line_mapping_dict[2]
        segments6 = line_mapping_dict[6]
        is_number_5 = sum([digit in segments5 for digit in segments6])
        if is_number_5 == 5:
            line_mapping_dict[5] = segments5
            line_mapping_dict[2] = segments2
        else:
            line_mapping_dict[2] = segments5
            line_mapping_dict[5] = segments2

        # Let's flip the dictionary now, in order to more easily retrieve the
        # numbers from the result
        mapping_numbers = dict(
            ("".join(sorted(segments)), number)
            for number, segments in line_mapping_dict.items()
        )

        final_number = ""
        for mixed_digits in output:
            final_number += str(mapping_numbers[''.join(sorted(mixed_digits))])


        yield int(final_number)


if __name__ == "__main__":
    input_data = read_input_stream(input_file)

    result_p1 = count_digits_1_4_7_8(input_data)
    print(f"Number of digits 1, 4, 7, and 8 are: {result_p1}")

    result_p2 = extract_all_digits(input_data)
    print(f"Sum of all digits is {sum(result_p2)}")