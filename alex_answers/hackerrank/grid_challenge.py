

GRID = ['ebacd', 'fghij', 'olmkn', 'trpqs']


def grid_challenge(grid):

    is_col_sorted_list = []

    for i, row in enumerate(grid):
        grid[i] = list(sorted(row))

    for col_index in range(len(grid[0])):
        column = [i[col_index] for i in grid]
        is_col_sorted_list.append(column == list(sorted(column)))

    return "YES" if all(is_col_sorted_list) else "NO"


print(grid_challenge(GRID))

