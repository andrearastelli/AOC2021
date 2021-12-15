from collections import deque, defaultdict
from itertools import pairwise, accumulate, tee
from pathlib import Path
from functools import reduce


group = {
    "open": "[(<{",
    "close": "])>}"
}




def get_chunks(line):

    list_wrong_closed = []

    def group_finder(p, n):
        if len(p) > 0 and p[-1] in group["open"] and n in group["close"]:
            open_idx = group["open"].find(p[-1])
            close_idx = group["close"].find(n)
            if open_idx != close_idx:
                list_wrong_closed.append((n, group["close"][open_idx]))

            p = p[0:-1]
            n = ""

        return f"{p}{n}"

    data_list = reduce(group_finder, line)

    return data_list, list_wrong_closed


def syntax_error_checker(input_lines):
    scoreboard = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    group_count = defaultdict(int)

    for line in input_lines:
        chunk_data = get_chunks(line)

        for closed in chunk_data[1]:
            group_count[closed[0]] += scoreboard[closed[0]]

    print(group_count)

    return sum(group_count.values())


def syntax_error_fixer(input_lines):
    scoreboard = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4
    }

    scores = []

    for line in input_lines:
        data_list, list_wrongly_closed = get_chunks(line)

        if len(list_wrongly_closed) == 0:

            print(data_list)

            score = 0

            for character in reversed(data_list):
                score = (score * 5) + scoreboard[character]

            scores.append(score)

    scores = sorted(scores)

    print(len(scores))

    return scores[len(scores)//2]


if __name__ == "__main__":
    input_file = Path(__file__).parent / Path("p1_input")

    p1_input_data = input_file.open().readlines()
    p1_input_data = map(str.strip, p1_input_data)

    p1_input_data, p2_input_data = tee(p1_input_data)

    p1_test_input_data = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]

    result = syntax_error_checker(p1_input_data)
    print(result)

    result = syntax_error_fixer(p2_input_data)
    print(result)