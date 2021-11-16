


def diagonalDifference(arr):

    diagonal_fwd = []
    diagonal_back = []

    for i, row in enumerate(arr):
        diagonal_fwd.append(row[i])
        diagonal_back.append(row[-(i+1)])

    return abs(sum(diagonal_fwd) - sum(diagonal_back))





if __name__ == "__main__":

    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9],
    ]

    print(diagonalDifference(arr))

