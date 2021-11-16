#!/bin/python3

import decimal

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):

    decimal.getcontext().prec = 6

    length = decimal.Decimal(len(arr))
    pos = []
    neg = []
    zero = []

    for i in arr:
        if i > 0:
            pos.append(i)
        if i == 0:
            zero.append(i)
        if i < 0:
            neg.append(i)

    print("{0:.6f}".format(decimal.Decimal(len(pos)) / length))
    print("{0:.6f}".format(decimal.Decimal(len(neg)) / length))
    print("{0:.6f}".format(decimal.Decimal(len(zero)) / length))


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
