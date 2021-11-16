

matrix = [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]


def flippingMatrix(matrix):
    # Write your code here

    n = int(len(matrix) / 2)
    current_sum = _compute_sum(matrix)
    max_value = 0
    max_value_location = (0,0)

    for i, row in enumerate(matrix[n:]):
        for col, item in enumerate(row[n:]):

            if item < max_value:
                max_value_location = (i, col)

    if max_value_location[0] <= n:
        _reverse_column(matrix, )




    return current_sum



def _compute_sum(matrix):
    n = int(len(matrix) / 2)
    sum = 0

    for row in matrix[:n]:
        for i in row[:n]:
            sum += i

    return sum

def _reverse_column(matrix, col):
    column_reversed = list(reversed([i[col] for i in matrix]))
    for i, row in enumerate(matrix):
        row[col] = column_reversed[i]

def _reverse_row(matrix, row):
    matrix[row] = list(reversed(matrix[row]))




if __name__ == '__main__':

    print(flippingMatrix(matrix))

