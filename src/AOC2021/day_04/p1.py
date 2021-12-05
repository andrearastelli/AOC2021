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


# For each extracted number
for number in numbers:
    # print(f"Extracted number: {number}")

    # Check every board
    for board in boards:
        # And mark the corresponding cell if the number exists in that board
        board.set_number(number)

        if board.is_done:
            # Print the board for debugging purposes
            board.print()
            # Extract the score (sum of all unmarked cells)
            score = board.score()
            print(score)

            # kill the application as we don't need to do anything else
            break

    else:
        continue

    break



