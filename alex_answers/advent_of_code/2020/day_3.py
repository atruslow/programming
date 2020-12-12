from day_3_input import puzzle_input
from collections import Counter
from functools import reduce

puzzle_input = [list(i) for i in puzzle_input.strip().split("\n")]

slopes = ((3, 1), (1,1), (5,1), (7,1), (1,2))
col_len = len(puzzle_input[0])
row_len = len(puzzle_input)
tree_hits = Counter()

for slope in slopes:
    slope_x, slope_y = slope
    position = (0, 0)

    while position[1] < row_len:

        x, y = position
        x_adj = x % col_len

        tree_hits[slope] += 1 if puzzle_input[y][x_adj] == "#" else 0

        position = (x + slope_x, y + slope_y)

print(reduce(lambda x, y: x*y, tree_hits.values()))