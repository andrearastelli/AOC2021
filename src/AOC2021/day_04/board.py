from prettytable import PrettyTable, PLAIN_COLUMNS

from cell import Cell

class Board:
    def __init__(self, cells):
        # build a 5x5 matrix
        self.data = [[0 for r in cells] for r in cells]
        # for each row
        for ridx, row in enumerate(cells):
            # for each cell
            for cidx, cell in enumerate(row):
                # store the cell value
                self.data[ridx][cidx] = Cell(cell)

        self.is_done = False
        self.counter_done = -1
        self.extraction_number = -1
        self.already_called = False

    def print(self):
        # Print the board in a pretty format
        print(self._get_table())
        print("-"*100)

    def _get_table(self):
        table = PrettyTable()
        table.set_style(PLAIN_COLUMNS)
        table.header = False
        table.add_rows(self.data)

        return table.get_string()

    def set_number(self, number):
        # If the board has already won, no need to set any new number
        if self.is_done:
            return

        self.extraction_number = number

        # For each row
        for row in self.data:
            # and for each cell in the row
            for cell in row:
                # if the number in the cell match the extracted number
                if cell.number == number:
                    # set the cell as marked
                    cell.marked = True

        # After marking the extracted number on the board, let's check if
        # the board won
        self.is_done = self.check_full_column() or self.check_full_row()

    def check_full_row(self):
        if self.is_done:
            return True

        # For each row
        for row in self.data:
            # Check if all cells are marked and if so, return True
            if all([cell.marked for cell in row]):
                self.is_done = True
                return True

        # Return False in every other case
        return False

    def check_full_column(self):
        if self.is_done:
            return True

        for cidx in range(5):
            marked = True
            for ridx in range(5):
                cell = self.data[ridx][cidx]
                marked = cell.marked and marked
            if marked:
                self.is_done = True
                return True
        return False

    def score(self):
        numbers = [
            cell.number
            for row in self.data for cell in row
            if cell.marked == False
        ]

        if self.already_called == False:
            self.already_called = True
            return sum(numbers) * self.extraction_number
        else:
            return 0

    def clean(self):
        for row in self.data:
            for cell in row:
                cell.marked = False