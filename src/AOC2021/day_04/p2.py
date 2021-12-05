from pathlib import Path

from board import Board


input_file = Path(__file__).parent / Path("./p1_input")


with input_file.open() as input_file_handler:
    numbers = next(input_file_handler)
    numbers = map(int, numbers.split(","))

    boards = []
    board = []
    for line in input_file_handler:
        sanitized_line = line.strip()

        if sanitized_line == "":
            if board == []:
                continue
            boards.append(Board(board))
            board = []

        else:
            board.append(map(int, sanitized_line.split()))


scores = []
for number in numbers:
    for board in reversed(boards):

        board.set_number(number)
        scores.append(board.score())


scores = [score for score in scores if score != 0]
score = scores[-1]
print(score)
