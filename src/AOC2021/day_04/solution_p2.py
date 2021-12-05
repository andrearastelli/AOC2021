from functools import partial, reduce


def transpose(board):
    return list(zip(*board))


def update_board(num, board):
    return [[-1 if x == num else x for x in row] for row in board]


def draw_num(boards, draws, idx=0):
    for i, board in enumerate(boards):
        if -5 in map(sum, board) or -5 in map(sum, transpose(board)):
            return idx - 1, i, board
    return draw_num(list(map(partial(update_board, draws[idx]) , boards)), draws, idx + 1)


def board_sum(board):
    return sum([x for x in reduce(lambda x, y: x + y, board) if x != -1])


def parse_input(data):
    seq = [list(map(int, x.split())) for x in data[1:] if x != "\n"]
    return list(map(int, data[0].split(","))), [seq[i:i+5] for i, x in enumerate(seq) if i % 5 == 0]


if __name__ == '__main__':

    from pathlib import Path
    p1_input = Path(__file__).parent / Path("p1_input")
    with p1_input.open() as f:
        input_data = f.readlines()
        draws, boards = parse_input(input_data)

    # PART 1
    draw_idx, win_idx, win_board = draw_num(boards, draws)
    print(draws[draw_idx] * board_sum(win_board))

    # PART 2
    draw_idx = 0
    while boards:
        draw_idx, win_idx, win_board = draw_num(boards, draws)
        del boards[win_idx]
    print(draws[draw_idx] * board_sum(win_board))