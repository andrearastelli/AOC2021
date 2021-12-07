from dataclasses import dataclass
from pathlib import Path

p1_input = Path(__file__).parent / Path("p1_input")

@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def intersect(self, other_line) -> bool:
        xdiff = (self.x1 - self.x2, self.x2 - self.x1)
        ydiff = (self.y1 - self.y2, self.y2 - self.y1)

        def det(a, b):
            return a[0]*b[1] - a[1]*b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            return False

        return True

hv_lines = []
lines = []

with p1_input.open() as input_file:
    for line in input_file:
        coord1, coord2 = line.split("->")
        x1, y1 = list(map(int, coord1.split(",")))
        x2, y2 = list(map(int, coord2.split(",")))

        if x1 == x2 or y1 == y2:
            hv_lines.append(Line(x1, y1, x2, y2))

        lines.append(Line(x1, y1, x2, y2))


max_y = max([max(line.x1, line.x2) for line in hv_lines])
max_x = max([max(line.y1, line.y2) for line in hv_lines])

print(f"X: {max_x} | Y: {max_y}")

grid = []
for iy in range(max_y+1):
    row = []
    for ix in range(max_x+1):
        row.append(0)
    grid.append(row)

print(f"{len(grid[0])}, {len(grid)}")

for line in hv_lines:
    if line.x1 == line.x2:
        for step_y in range(line.y1, line.y2):
            # print(f"{line.x1},{step_y} [{len(grid)},{len(gripython d[line.x1])}]")
            grid[line.x1][step_y] += 1

    if line.y1 == line.y2:
        for step_x in range(line.x1, line.x2):
            # print(f"{step_x},{line.y1} [{len(grid)},{len(grid[step_x])}]")
            grid[step_x][line.y1] += 1

num_zero_cells = len([cell for row in grid for cell in row if cell <= 1])
print(num_zero_cells)



